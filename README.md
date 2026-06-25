# Paper Super Reviewer / 论文超审

[![Stars](https://img.shields.io/github/stars/TheeTarnished/paper-super-reviewer?style=social)](https://github.com/TheeTarnished/paper-super-reviewer)
[![Version](https://img.shields.io/badge/version-3.0.0-blue)](https://github.com/TheeTarnished/paper-super-reviewer)

**[English](#english) | [中文](#中文)**

受 **Nature-Skills** (袁一哲, 20K⭐) 的三审稿人面板哲学、**CCFA-Skills** 的定量评分卡和 **PaperSpine** 的完整性审计启发。

---

## English

End-to-end academic paper review system — **6 specialized AI agents** conduct parallel peer review with distinct academic personalities.

### Demo — ResNet (He et al., 2015)

> 🏆 **30/30 — Landmark Paper. Unanimous Strong Accept.**
→ **[Full Bilingual Review →](demo/RESNET_REVIEW.md)**

### 6 Agents

| # | Agent | Personality | Focus |
|---|-------|------------|-------|
| 1 | Methodology Arbiter | Rigorous empiricist | Experimental design, ablation, reproducibility |
| 2 | Domain Navigator | Living encyclopedia | Novelty, SOTA positioning, contribution |
| 3 | Narrative Editor | Former Nature editor | Writing clarity, flow, readability |
| 4 | Format Guardian | Perfectionist | LaTeX, figures, page limits |
| 5 | Reference Auditor | Bibliometrician | Citation quality, completeness |
| 6 | Integrity Detective | Skeptic | Claim-evidence alignment, data consistency |

### Scoring
- CCF 6-dim × 5pts = **30 total**
- Nature 5-axis evaluation
- Reference quality scoring

### Install
```bash
# Hermes Agent
hermes skills install paper-super-reviewer

# Claude Code
mkdir -p ~/.claude/skills/paper-super-reviewer && cp SKILL.md $_

# Codex CLI (Nature-Skills compatible)
mkdir -p ~/.codex/skills/paper-super-reviewer && cp -R . $_
```

### Usage
```
Review paper: path/to/paper.tex, mode=full
```

---

## 中文

端到端学术论文超审系统 — **6 个专业化 AI 智能体**并行审稿，每个都有独特的学术人格。

### 示范 — ResNet (何恺明, 2015)

> 🏆 **30/30 满分 — Landmark Paper.**
→ **[中英双语完整审稿 →](demo/RESNET_REVIEW.md)**

### 六智能体

| # | 智能体 | 人格 | 审查重点 |
|---|--------|------|---------|
| 1 | 方法论仲裁者 | 严谨的实证主义者 | 实验设计、消融、可复现 |
| 2 | 领域导航者 | 活的文献字典 | 创新性、SOTA定位、贡献 |
| 3 | 叙事编辑者 | 前 Nature 编辑 | 写作清晰度、流畅性 |
| 4 | 格式守卫者 | 完美主义者 | LaTeX、图表、页数 |
| 5 | 引用审计者 | 文献计量学家 | 引用质量、完整性 |
| 6 | 完整性侦探 | 怀疑论者 | 声称-证据对齐、数据一致性 |

### 评分
- CCF 六维 × 5 分 = **30 总分**
- Nature 五轴评估
- 引用质量评分

### 安装
```bash
hermes skills install paper-super-reviewer
```

### 使用
```
审核论文: path/to/paper.tex, mode=full
```
