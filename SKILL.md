---
name: paper-super-reviewer
description: "端到端学术论文超审系统 — 集成定量评分卡、三智能体审稿面板、跨审稿综合、引用质量审计、LaTeX格式检查。模拟真实学术评审全流程，输出结构化审稿报告。"
version: 2.0.0
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

端到端学术论文质量审核系统。模拟真实学术评审全流程，通过三个专业化智能体协同工作，生成结构化审稿报告。

## 三智能体架构

本系统采用三智能体并行审稿 + 跨审稿综合的架构。每个智能体从不同专业视角独立评审同一篇论文，最后综合形成统一的审稿意见。

### Agent 1: 方法论审稿人 (Methodology Reviewer)

**职责**: 从技术健全性角度深挖论文的方法论质量。

**评审维度**:
- 实验设计是否严谨：有无对照实验、消融实验、统计显著性检验
- 方法论正确性：数学推导是否无误、算法实现是否有逻辑漏洞
- 超参设置是否合理：是否有超参敏感性分析
- 可复现性：代码是否开源、数据是否可获取、随机种子是否固定

**典型发现**: "Transformer 的 132K 参数在仅有 2,146 样本上严重欠定——样本/参数比仅 16:1，结论不可靠。"

### Agent 2: 领域审稿人 (Domain Reviewer)

**职责**: 从领域知识角度评估论文的创新性和贡献。

**评审维度**:
- 创新性：与 SOTA 的实质性差异是什么，是否只是组合现有方法
- 相关工作覆盖：是否遗漏关键基线（如 iTransformer, DLinear, Mamba）
- 贡献显著性：对领域是否有实质推动，还是增量改进
- 实验说服力：实验设置是否符合领域标准，数据集选择是否有偏

**典型发现**: "论文声称 23 个模型但仅测试 6 个——严重的 claim-evidence gap。Kronos 作为唯一的金融基础模型未被实际对比。"

### Agent 3: 通才审稿人 (General Reviewer)

**职责**: 从写作质量、可读性和格式规范角度评估。

**评审维度**:
- 段落逻辑流：每段是否有清晰的 topic sentence → evidence → transition
- 贡献展示：Introduction 是否清晰列出贡献
- Claim-evidence 一致性：每个声称是否有证据支撑
- 术语一致性：关键术语全文统一
- 图表叙述：图表是否在正文中被充分讨论
- LaTeX 格式：编译是否零错误、引用是否完整、表格是否溢出

**典型发现**: "参考文献 hochreiter1997 和 cho2014 在正文中被引用，但摘要中未提及——需统一。Table 1 溢出 ACM 双栏格式。"

### 跨审稿综合 (Cross-Review Synthesis)

三智能体完成独立评审后，系统自动综合：

- **共识优势**: 三位审稿人均认可的强项
- **共识风险**: 三位审稿人均关注的问题（最高优先级）
- **侧重差异**: 不同视角的关注点分歧
- **关键问题排序**: 按严重度 Fatal > Major > Moderate > Minor 排列

## 审核模式

| 模式 | 覆盖内容 | 参与智能体 |
|------|---------|:--:|
| `scientific` | 科学创新性、技术健全性、实验证据、相关工作 | Agent 1 + 2 |
| `writing` | 段落逻辑、贡献展示、术语一致性、图表叙述 | Agent 3 |
| `format` | LaTeX编译、引用完整性、图表质量、页面限制 | Agent 3 |
| `full` | 以上全部 + 完整性审计 + 跨审稿综合 | Agent 1 + 2 + 3 |

## 使用方式

加载 skill 后，提供论文文件路径和审核模式：

```
审核论文: path/to/paper.tex, mode=full
```

## 输出格式

```markdown
# Paper Super Review Report
## Review Setup (审核设置)
## Paper Summary (论文摘要)
## Quantitative Scorecard (定量评分卡, 6维×5分制)
## Reviewer Panel (三智能体独立审稿意见)
## Cross-Review Synthesis (跨审稿综合)
## Reference Quality Audit (引用质量审计)
## Format & LaTeX Audit (格式检查)
## Integrity Audit (完整性审计)
## Concern-to-Action Table (关注-行动表)
## AC / Meta-Review (最终审稿决定)
```

## 评分体系

六维度 1-5 分制，总分 30：

| 维度 | 评估内容 |
|------|---------|
| Novelty | 与 SOTA 的实质性差异 |
| Soundness | 方法论正确性、实验设计 |
| Evidence | 实验充分性、统计显著性 |
| Related Work | 相关工作覆盖度 |
| Reproducibility | 代码/数据/超参完整性 |
| Significance | 对领域的潜在影响 |

## 红线和禁止事项

- 不编造审稿人身份、实验数据或引用
- 不将审稿转为 rebuttal 撰写
- 评分严格但有建设性：每个扣分附带修复路径
- 智能体间分歧来自真实证据差异，不强行调和
- 引用审计是客观检查，不编造"缺失的引用"
