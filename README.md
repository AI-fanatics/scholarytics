# Paper Super Reviewer / 论文超审

[![Stars](https://img.shields.io/github/stars/TheeTarnished/paper-super-reviewer?style=social)](https://github.com/TheeTarnished/paper-super-reviewer)
[![Version](https://img.shields.io/badge/version-4.0.0-blue)](https://github.com/TheeTarnished/paper-super-reviewer)

**[English](#english) | [中文](#中文)**

---

## English

End-to-end academic paper review system — **15 independent skills** × **6 specialized AI agents** work in parallel to produce structured peer review reports.

### Demo — ResNet (He et al., 2015)

> 🏆 **30/30 — Landmark Paper. Unanimous Strong Accept.**
→ **[Full Bilingual Review →](demo/RESNET_REVIEW.md)**

### 15 Skills

| Layer | Skills |
|-------|--------|
| **Core Review** (6 agents) | Methodology Arbiter · Domain Navigator · Narrative Editor · Format Guardian · Reference Auditor · Integrity Detective |
| **Quick Assessment** (3) | Quick Scan (5min) · Scorecard (6-dim × 5pts) · Venue Match |
| **Deep Audit** (4) | LaTeX Audit · Citation Audit · Claim Audit · Data Audit |
| **Output** (2) | Rebuttal Builder · Slides Builder |

### Scoring
- **CCF 6-dim × 5pts = 30 total**
- Nature 5-axis evaluation
- Reference quality scoring (1-5)

### Install
```bash
# Hermes Agent
hermes skills install paper-super-reviewer

# Claude Code
mkdir -p ~/.claude/skills/paper-super-reviewer && cp SKILL.md $_

# Codex CLI
mkdir -p ~/.codex/skills/paper-super-reviewer && cp -R skills/* $_

# Full install (all 15 skills)
git clone https://github.com/TheeTarnished/paper-super-reviewer.git
cp -R skills/* ~/.hermes/skills/research/
```

### Usage
```
paper-review path/to/paper.tex --mode full
paper-quick-scan path/to/paper.pdf
paper-latex-audit path/to/paper.tex
paper-citation-audit path/to/paper.tex path/to/refs.bib
```

---

## 中文

端到端学术论文超审系统 — **15 个独立 Skill** × **6 个专业化 AI 智能体**并行审稿。

### 示范 — ResNet (何恺明, 2015)

> 🏆 **30/30 满分 — Landmark Paper.**
→ **[中英双语完整审稿 →](demo/RESNET_REVIEW.md)**

### 15 个 Skill

| 层级 | Skill |
|------|-------|
| **核心审稿** (6 智能体) | 方法论仲裁者 · 领域导航者 · 叙事编辑者 · 格式守卫者 · 引用审计者 · 完整性侦探 |
| **快速评估** (3) | 快速扫描(5分钟) · 评分卡(6维×5分) · 投稿匹配 |
| **深度审计** (4) | LaTeX审计 · 引用审计 · Claim审计 · 数据审计 |
| **产出** (2) | Rebuttal生成 · PPT生成 |

### 评分
- **CCF 六维 × 5 分 = 30 总分**
- Nature 五轴评估
- 引用质量评分 (1-5)

### 安装
```bash
hermes skills install paper-super-reviewer
git clone https://github.com/TheeTarnished/paper-super-reviewer.git
cp -R skills/* ~/.hermes/skills/research/
```

### 使用
```
审核论文: path/to/paper.tex --mode full
快速扫描: path/to/paper.pdf
检查 LaTeX: path/to/paper.tex
检查引用: path/to/paper.tex path/to/refs.bib
```
