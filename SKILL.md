---
name: paper-super-reviewer
description: "端到端学术论文超审系统 — 三智能体协同审稿 + 跨审稿综合 + 定量评分卡 + 引用审计 + LaTeX检查。模拟真实学术评审全流程。"
version: 2.1.0
author: TheeTarnished
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [paper-review, academic, peer-review, latex-audit, multi-agent-review]
    category: research
    homepage: https://github.com/TheeTarnished/paper-super-reviewer
---

# Paper Super Reviewer — 论文超审

[![Stars](https://img.shields.io/github/stars/TheeTarnished/paper-super-reviewer?style=social)](https://github.com/TheeTarnished/paper-super-reviewer)
[![Version](https://img.shields.io/badge/version-2.1.0-blue)](https://github.com/TheeTarnished/paper-super-reviewer)

端到端学术论文质量审核系统。三个专业化智能体并行审稿，模拟真实学术评审全流程——从定量评分到格式检查到跨审稿综合，输出完整的结构化审稿报告。

## 为什么是三个智能体？

真实学术评审中，一篇论文通常由 2-4 位审稿人独立评审。三位是最佳平衡点：

- **2 位太少**：当意见分歧时（一位 Accept、一位 Reject），缺乏第三个独立视角打破僵局
- **4+ 位冗余**：边际信息增益递减，增加协调成本
- **3 位恰好**：保证多视角覆盖（技术/领域/写作），同时分歧时有决定性一票

每位智能体从完全不同但互补的专业视角审视同一篇论文，不共享中间状态，以保证评审独立性。

## 三智能体详解

### Agent 1 — 方法论审稿人 (Methodology Reviewer)

**核心使命**: 从技术健全性角度，像一位严格的方法论学者一样审视论文。

**审查清单**:
- **实验设计**: 有无对照实验？消融实验是否充分？统计显著性检验是否执行？
- **方法论正确性**: 数学推导是否有漏洞？算法伪代码与实现是否一致？
- **超参合理性**: 是否有超参敏感性分析？学习率、batch size、层数是否有消融？
- **可复现性**: 代码是否开源？随机种子是否固定？依赖版本是否锁定？
- **硬件与效率**: 训练/推理时长是否合理？参数量与数据量是否匹配？

**典型工作方式**: 会主动追踪 paper 中的每一个 claim 是否被实验结果支撑。发现 "23 个模型声称，6 个实测" 会标记为 Fatal。

**输出风格**: 技术性强、引用具体行号和表格数据、扣分附带精确修复路径。

### Agent 2 — 领域审稿人 (Domain Reviewer)

**核心使命**: 从领域知识和 SOTA 对比角度，判断论文的创新性和贡献。

**审查清单**:
- **创新性定位**: 与 SOTA 的实质性差异是什么？是方法创新还是组合创新？
- **相关工作覆盖**: 是否遗漏关键基线？引用是否全面且最新（近 3 年）？
- **贡献显著性**: 对领域是增量改进还是范式推动？实验提升是否显著？
- **实验说服力**: 数据集选择是否代表领域？对比基线是否公平？
- **局限诚实性**: 作者是否诚实地讨论了方法的局限性？

**典型工作方式**: 会从领域知识库中检索相关论文，对比方法、数据集、实验结果，判断该工作的真实定位。

**输出风格**: 宏观视角、关注论文在领域全景中的位置、建议补充的基线和方法。

### Agent 3 — 通才审稿人 (General Reviewer)

**核心使命**: 从写作质量和可读性角度，确保论文能够被广泛读者理解。

**审查清单**:
- **段落逻辑流**: 每段是否有 topic sentence → evidence → transition？段落间连接是否自然？
- **贡献展示**: Introduction 是否在首段清晰列出 2-4 条贡献？
- **Claim-Evidence 对齐**: 每个 claim 在实验部分是否有对应证据？
- **术语一致性**: 同一概念是否全文使用统一术语？缩写首次出现是否定义？
- **图表叙述**: 每个图表在正文中是否被充分讨论？caption 是否 self-contained？
- **LaTeX 格式**: 编译是否零错误？表格是否溢出？引用是否完整？
- **盲审合规**: 是否无意中暴露作者身份？

**典型工作方式**: 像一位非该子领域的学者阅读——不能被专业术语遮挡，必须能无障碍理解核心贡献。

**输出风格**: 关注 clarity 和 presentation，提出具体的文字修改建议。

## 关于 Sub-Agent 的说明

当前三智能体架构暂不引入 sub-agent。理由：

1. **审稿是判断性任务，非生成性任务**——审稿人需要全局视野来形成整体判断，拆分为 sub-agent 会导致碎片化评估，失去 "这篇论文到底能不能发" 的整体感
2. **审稿独立性至关重要**——sub-agent 会引入 coordination overhead，破坏评审独立性
3. **三智能体的输出已经足够结构化和全面**——每个 agent 的输出涵盖其专业领域的所有关键维度

当审稿需求扩展到多篇论文对比、期刊级批量审稿、或需要专项检查（如数学公式推导验证）时，可考虑引入专项 sub-agent。

## 审核模式

| 模式 | 覆盖内容 | 参与智能体 |
|------|---------|:--:|
| `scientific` | 创新性、健全性、实验证据、相关工作 | Agent 1 + 2 |
| `writing` | 段落逻辑、贡献展示、术语一致性 | Agent 3 |
| `format` | LaTeX、引用完整性、图表、页面 | Agent 3 |
| `full` | 全部 + 完整性审计 + 跨审稿综合 | 1 + 2 + 3 |

## 安装

### Hermes Agent

```bash
# 通过 Hermes Hub (推荐)
hermes skills install paper-super-reviewer

# 手动安装
mkdir -p ~/.hermes/skills/research/paper-super-reviewer
cp SKILL.md ~/.hermes/skills/research/paper-super-reviewer/
cp -r templates/ ~/.hermes/skills/research/paper-super-reviewer/
```

### Claude Code

```bash
# 手动安装
mkdir -p ~/.claude/skills/paper-super-reviewer
cp SKILL.md ~/.claude/skills/paper-super-reviewer/
cp -r templates/ ~/.claude/skills/paper-super-reviewer/

# 在 Claude Code 会话中加载
/claude skill load paper-super-reviewer
```

或直接放入项目级 skill 目录：
```bash
mkdir -p .claude/skills/paper-super-reviewer
cp SKILL.md .claude/skills/paper-super-reviewer/
```

### Codex CLI (OpenAI)

```bash
# 手动安装到 Codex skills 目录
mkdir -p ~/.codex/skills/paper-super-reviewer
cp SKILL.md ~/.codex/skills/paper-super-reviewer/
cp -r templates/ ~/.codex/skills/paper-super-reviewer/

# 在 Codex 会话中使用
# Codex 会自动发现 ~/.codex/skills/ 下的 skill 文件
```

## 使用方式

加载 skill 后，提供论文文件路径和审核模式：

```
审核论文: path/to/paper.tex, mode=full
```

## 输出格式 (full mode)

```markdown
# Paper Super Review Report
## Review Setup
## Paper Summary
## Quantitative Scorecard (6维 × 5分制 = 30总分)
## Reviewer 1 — 方法论审稿人
## Reviewer 2 — 领域审稿人
## Reviewer 3 — 通才审稿人
## Cross-Review Synthesis
## Reference Quality Audit
## Format & LaTeX Audit
## Integrity Audit
## Concern-to-Action Table
## AC / Meta-Review
```

## 红线和禁止事项

- 不编造审稿人身份、实验数据或引用
- 不将审稿转为 rebuttal 撰写
- 评分严格但有建设性：每个扣分附带修复路径
- 智能体间分歧来自真实证据差异，不强行调和
- 引用审计是客观检查，不编造"缺失的引用"
