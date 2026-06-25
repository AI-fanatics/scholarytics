---
name: paper-super-reviewer
description: "端到端学术论文超审系统 — 15 个独立 Skill，每个包含完整的 SKILL.md + manifest.yaml + 结构化 JSON 输出。从快速扫描到完整超审，每个智能体可独立调用。"
version: 4.0.0
author: TheeTarnished
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [paper-review, academic, peer-review, latex-audit, multi-agent-review]
    category: research
    homepage: https://github.com/TheeTarnished/paper-super-reviewer
---

# Paper Super Reviewer — 论文超审 v3.0

[![Stars](https://img.shields.io/github/stars/TheeTarnished/paper-super-reviewer?style=social)](https://github.com/TheeTarnished/paper-super-reviewer)

端到端学术论文超审系统。**12 个独立 Skill**，每个可单独调用或通过主 Skill 编排。

## 设计哲学

> *"Skill 其实是这个过渡时代留给我们的一份珍贵礼物——它不只是一套静态的工具，更是凝结了专家隐性经验的知识晶体。"*

每个审稿人智能体都应该像一个真实的、有性格的、有专业偏好的学者。不是冷冰冰的检查清单，而是带着自己的学术品味和判断力去读一篇论文。

## Skill 家族 (12 个)

```
skills/
├── paper-super-reviewer/          # 主编排器 — 调用全部子 skill
│
├── 🔬 核心审稿 (6 Agent)
├── paper-methodology-reviewer/    # Agent 1: 方法论仲裁者 · 12项检查
├── paper-domain-reviewer/         # Agent 2: 领域导航者 · 10项检查
├── paper-narrative-editor/        # Agent 3: 叙事编辑者 · 12项检查
├── paper-format-guardian/         # Agent 4: 格式守卫者 · LaTeX审计
├── paper-reference-auditor/       # Agent 5: 引用审计者 · 质量评分
├── paper-integrity-detective/     # Agent 6: 完整性侦探 · claim追踪
│
├── ⚡ 专项工具 (4 个)
├── paper-quick-scan/              # 5分钟快速扫描 — 论文一页纸画像
├── paper-latex-check/             # LaTeX专项 — 编译审计+精确修复
├── paper-citation-check/          # 引用专项 — 香火检测+遗漏推荐
├── paper-claim-tracker/           # 声称追踪 — claim→evidence映射
│
├── 🎯 投稿辅助 (1 个)
├── paper-venue-matcher/           # 会议匹配 — CCF/SCI推荐
│
├── manifest.yaml                  # Skill 清单与路由
└── GENERATION_LOG.md              # 生成日志 — 完全透明
```

## 六智能体详解

### Agent 1 — 方法论仲裁者 · Methodology Arbiter
**人格**: 严谨到近乎苛刻的实证主义者。相信只有可复现的结果才是科学。
**12 项检查**: 消融实验 · 统计显著性 · 超参敏感 · 代码开源 · 数据偏倚 · 样本/参数比 · look-ahead bias · 硬件报告 · overclaiming · 误差线 · 基线公平性

### Agent 2 — 领域导航者 · Domain Navigator
**人格**: 该领域的活字典。瞬间定位论文在领域全景图中的位置。
**10 项检查**: 创新类型 · SOTA差距 · 相关工作覆盖 · 遗漏基线 · 提升显著性 · 数据集代表性 · 基线强度 · 局限诚实 · 自引率 · 新方向潜力

### Agent 3 — 叙事编辑者 · Narrative Editor
**人格**: 前 Nature 编辑。相信好论文应让非该子领域的聪明读者也能读懂。
**12 项检查**: Abstract结构 · 贡献展示 · 段落逻辑 · 段落连接 · 术语定义 · 术语一致 · 图表caption · 图表讨论 · 公式清晰 · 结论一致 · AI-isms · 语法

### Agent 4 — 格式守卫者 · Format Guardian
**人格**: 完美主义者。格式就是学术态度。
**10 项检查**: LaTeX编译 · 引用完整 · 孤立引用 · 图表分辨率 · 表格溢出 · 公式编号 · 页数限制 · 盲审匿名 · 缩写统一 · 交叉引用

### Agent 5 — 引用审计者 · Reference Auditor
**人格**: 文献计量学专家。引用网络揭示一切。
**8 项检查**: 引用数量 · 时效性 · 香火引用 · 实质讨论 · 自引率 · retracted · 准确性 · 遗漏关键

**引用质量评分 (1-5)**:
| 5/5 | >40篇, 近3年>50%, 每篇实质性讨论 |
| 4/5 | >25篇, 近3年>40% |
| 3/5 | >15篇, 无明显遗漏 |
| 2/5 | <15篇或遗漏关键工作 |
| 1/5 | <10篇或虚假引用 |

### Agent 6 — 完整性侦探 · Integrity Detective
**人格**: 怀疑论者。数字不会说谎，但作者可能会。
**10 项检查**: claim-evidence对齐 · 数字一致 · 图表-正文一致 · cherry-picking · SOTA真实性 · ghost results · 统计声明 · 结论新增 · 作者贡献 · AI虚假引用

## 审核模式

| 模式 | 智能体 | 耗时 | 适用场景 |
|------|:-----:|:--:|------|
| `quick` | 快速扫描 | 5 min | 投稿前自查 |
| `science` | Agent 1+2 | 10 min | 方法+领域审核 |
| `writing` | Agent 3 | 5 min | 写作质量检查 |
| `format` | Agent 4+5 + LaTeX + 引用 | 5 min | 格式+引用审计 |
| `integrity` | Agent 6 + Claim Tracker | 5 min | 完整性验证 |
| `full` | 全部 12 Skill | 30 min | 完整超审 |

## 安装

```bash
# Hermes Agent
hermes skills install paper-super-reviewer

# 安装全部 12 个 Skill
git clone https://github.com/TheeTarnished/paper-super-reviewer.git
cp -R skills/* ~/.hermes/skills/research/

# Claude Code
cp -R skills/* ~/.claude/skills/

# Codex CLI
cp -R skills/* ~/.codex/skills/
```

## 使用

```bash
# 完整超审
审核论文: path/to/paper.tex, mode=full

# 单个 Skill 独立调用
审核实验设计: path/to/paper.tex          # → Agent 1
检查引用: path/to/paper.tex refs.bib     # → Agent 5
快速扫描: path/to/paper.pdf              # → Quick Scan
匹配会议: path/to/review_report.json     # → Venue Matcher
```

## 审核触发规则 ⚠️

当用户说"审核这篇论文"而未指定具体文件时:
- **必须确认**是哪个论文文件，列出桌面上的候选 (.tex/.pdf)
- 不要假定是最近讨论过的论文
- 教训: 曾错误审核了 ACML 论文而非用户要的何恺明 ResNet

## 本地依赖路径

| 体系 | 路径 | 用途 |
|------|------|------|
| PaperSpine v3.3.0 | `C:/Users/82578/Desktop/PaperSpine_repo/` | 16 scripts (integrity_audit, structured_review, citation_quality...) |
| Nature-Skills | `C:/Users/82578/Desktop/nature-skills_repo/` | _shared + manifest 动态路由 + static/21 fragments |
| CCFA-Skills | `C:/Users/82578/Desktop/CCFA-Skills_repo/` | ccf-common governance + venue guides |

## GitHub Push

```bash
# gh CLI portable
/c/Users/82578/Desktop/gh_portable/bin/gh auth login --web
/c/Users/82578/Desktop/gh_portable/bin/gh repo create TheeTarnished/super-review-repo --public --source=. --push
```

## 整合方法论

从外部 GitHub skill 仓库整合为 Hermes skill:
1. `git clone --depth 1` 完整仓库，不只 curl SKILL.md
2. 理解共享层 (_shared, ccf-common) 和路由系统 (manifest/static)
3. 保留可执行脚本路径，让 Hermes 能实际运行
4. 标注版本号和本地路径
