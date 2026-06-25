# Paper Super Reviewer / 论文超审

[![Stars](https://img.shields.io/github/stars/TheeTarnished/paper-super-reviewer?style=social)](https://github.com/TheeTarnished/paper-super-reviewer)
[![Version](https://img.shields.io/badge/version-4.1.0-blue)](https://github.com/TheeTarnished/paper-super-reviewer)
[![Skills](https://img.shields.io/badge/skills-15-green)](https://github.com/TheeTarnished/paper-super-reviewer/tree/main/skills)

[![Star History Chart](https://api.star-history.com/svg?repos=TheeTarnished/paper-super-reviewer&type=Date)](https://star-history.com/#TheeTarnished/paper-super-reviewer&Date)

**[English](#english) | [中文](#中文)**

---

## English

End-to-end academic paper review system — **15 independent skills** × **6 specialized AI agents** produce structured peer review reports.

### Demo — ResNet (He et al., 2015)
> 🏆 **30/30 — Landmark Paper.** → **[Full Bilingual Review →](demo/RESNET_REVIEW.md)**

---

### 15 Skills · Complete Table

| # | Skill | Type | Agent | Description |
|---|-------|------|:-----:|-------------|
| 1 | `paper-super-reviewer` | Orchestrator | All 6 | Main orchestrator — dispatches all sub-skills, synthesizes cross-review report |
| 2 | `paper-methodology-reviewer` | Core Agent | Agent 1 | Experimental design audit · 12-point ablation/stats/reproducibility checklist |
| 3 | `paper-domain-reviewer` | Core Agent | Agent 2 | Novelty assessment · SOTA comparison · missing baseline detection |
| 4 | `paper-narrative-editor` | Core Agent | Agent 3 | Writing quality · paragraph logic flow · AI-ism detection (12 checks) |
| 5 | `paper-format-guardian` | Core Agent | Agent 4 | LaTeX 3-pass compilation · all warnings parsed · exact fix code generated |
| 6 | `paper-reference-auditor` | Core Agent | Agent 5 | Citation quality scoring (1-5) · BibTeX integrity · token-cite detection |
| 7 | `paper-integrity-detective` | Core Agent | Agent 6 | Claim-evidence alignment · numerical consistency · data honesty verification |
| 8 | `paper-quick-scan` | Quick Assess | — | 5-minute paper snapshot: contribution type · method summary · red/green flags |
| 9 | `paper-scorecard` | Quick Assess | — | CCF 6-dim × 5-pt quantitative scorecard with confidence intervals |
| 10 | `paper-venue-match` | Quick Assess | — | Venue recommendation: CCF tier matching · SCI journal ranking · acceptance probability |
| 11 | `paper-latex-audit` | Deep Audit | — | Deep LaTeX audit: 3× compile · all warnings decoded · per-issue fix code |
| 12 | `paper-citation-audit` | Deep Audit | — | Deep citation audit: semantic alignment · citation network analysis · missing key refs |
| 13 | `paper-claim-audit` | Deep Audit | — | Deep claim audit: extract all claims → locate evidence → detect false claims |
| 14 | `paper-data-audit` | Deep Audit | — | Data integrity audit: leakage detection · distribution shift · annotation quality |
| 15 | `paper-rebuttal-builder` | Output | — | Auto-rebuttal: reviewer comments → per-point response strategy + revision plan |

---

### Install
```bash
# Hermes Agent
hermes skills install paper-super-reviewer

# Full install (all 15 skills)
git clone https://github.com/TheeTarnished/paper-super-reviewer.git
cp -R skills/* ~/.hermes/skills/research/
```

### Usage
```bash
paper-review path/to/paper.tex --mode full       # 完整超审
paper-quick-scan path/to/paper.pdf               # 5分钟快速扫描
paper-latex-audit path/to/paper.tex              # LaTeX深度审计
paper-citation-audit paper.tex refs.bib          # 引用深度审计
```

---

## 中文

端到端学术论文超审系统 — **15 个独立 Skill** × **6 个专业化 AI 智能体**并行审稿。

### 示范 — ResNet (何恺明, 2015)
> 🏆 **30/30 满分 — Landmark Paper.** → **[中英双语完整审稿 →](demo/RESNET_REVIEW.md)**

---

### 15 Skill · 完整表格

| # | Skill | 类型 | 智能体 | 说明 |
|---|-------|------|:-----:|------|
| 1 | `paper-super-reviewer` | 主编排 | 全部6个 | 主编排器 — 调度全部子 skill，输出跨审稿综合报告 |
| 2 | `paper-methodology-reviewer` | 核心审稿 | Agent 1 | 实验设计审计 · 12项消融/统计/可复现检查 |
| 3 | `paper-domain-reviewer` | 核心审稿 | Agent 2 | 创新性评估 · SOTA对比 · 遗漏基线检测 |
| 4 | `paper-narrative-editor` | 核心审稿 | Agent 3 | 写作质量 · 段落逻辑流 · AI-ism检测 (12项) |
| 5 | `paper-format-guardian` | 核心审稿 | Agent 4 | LaTeX 3遍编译 · 全部warning解析 · 精确修复代码 |
| 6 | `paper-reference-auditor` | 核心审稿 | Agent 5 | 引用质量评分(1-5分) · BibTeX完整性 · 香火引用检测 |
| 7 | `paper-integrity-detective` | 核心审稿 | Agent 6 | 声称-证据对齐 · 数字一致性 · 数据诚实验证 |
| 8 | `paper-quick-scan` | 快速评估 | — | 5分钟论文画像：贡献类型 · 方法概要 · 红/绿旗标记 |
| 9 | `paper-scorecard` | 快速评估 | — | CCF 6维×5分定量评分卡 + 置信区间 |
| 10 | `paper-venue-match` | 快速评估 | — | 投稿推荐：CCF分层匹配 · SCI期刊排名 · 接受概率 |
| 11 | `paper-latex-audit` | 深度审计 | — | LaTeX深度审计：3次编译 · 全部warning解码 · 逐项修复 |
| 12 | `paper-citation-audit` | 深度审计 | — | 引用深度审计：语义对齐 · 引用网络分析 · 遗漏关键文献 |
| 13 | `paper-claim-audit` | 深度审计 | — | Claim深度审计：提取声称→定位证据→检测虚假声称 |
| 14 | `paper-data-audit` | 深度审计 | — | 数据完整性审计：泄露检测 · 分布偏移 · 标注质量 |
| 15 | `paper-rebuttal-builder` | 产出 | — | 自动Rebuttal：审稿意见→逐条回复策略+修改计划 |

---

### 安装
```bash
hermes skills install paper-super-reviewer
git clone https://github.com/TheeTarnished/paper-super-reviewer.git
cp -R skills/* ~/.hermes/skills/research/
```

### 使用
```bash
审核论文: path/to/paper.tex --mode full        # 完整超审
快速扫描: path/to/paper.pdf                     # 5分钟画像
检查 LaTeX: path/to/paper.tex                   # LaTeX深度审计
检查引用: paper.tex refs.bib                    # 引用深度审计
```
