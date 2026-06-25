---
name: paper-super-reviewer
description: "端到端学术论文超审系统 — 15 个独立 Skill × 6 智能体。每个 agent 输出独立 log + 最终 report 自动导出。"
version: 4.1.0
author: TheeTarnished
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [paper-review, academic, peer-review, latex-audit, multi-agent-review]
    category: research
    homepage: https://github.com/TheeTarnished/paper-super-reviewer
---

# Paper Super Reviewer — 论文超审 v4.1

[![Stars](https://img.shields.io/github/stars/TheeTarnished/paper-super-reviewer?style=social)](https://github.com/TheeTarnished/paper-super-reviewer)

端到端学术论文超审系统。**15 个独立 Skill**，每个可单独调用或通过主 Skill 编排。

## 核心功能

1. **多智能体并行审稿** — 6 个 Agent 独立评审，不共享中间状态
2. **每个 Agent 独立 Log** — 审查过程透明可追溯
3. **最终 Report 自动导出** — Markdown + 结构化 JSON 双格式
4. **单 Skill 独立调用** — 15 个 Skill 全部可单独使用

---

## 工作流

```
输入: paper.tex
  ↓
Phase 1: Quick Scan (paper-quick-scan)          → logs/01_quick_scan.md
  ↓
Phase 2: 并行审稿 (6 agents)
  ├── Agent 1 方法论仲裁者                         → logs/02_methodology_review.md + .json
  ├── Agent 2 领域导航者                           → logs/03_domain_review.md + .json
  ├── Agent 3 叙事编辑者                           → logs/04_narrative_review.md + .json
  ├── Agent 4 格式守卫者                           → logs/05_format_review.md + .json
  ├── Agent 5 引用审计者                           → logs/06_reference_review.md + .json
  └── Agent 6 完整性侦探                           → logs/07_integrity_review.md + .json
  ↓
Phase 3: 深度审计 (可选)
  ├── LaTeX Audit                                → logs/08_latex_audit.md + .json
  ├── Citation Audit                             → logs/09_citation_audit.md + .json
  ├── Claim Audit                                → logs/10_claim_audit.md + .json
  └── Data Audit                                 → logs/11_data_audit.md + .json
  ↓
Phase 4: 跨审稿综合 + 评分卡
  ↓
Export:
  ├── reports/{paper_name}_REVIEW_REPORT.md       ← 最终审稿报告
  ├── reports/{paper_name}_SCORECARD.json         ← 定量评分卡
  └── logs/                                       ← 全部过程日志
```

## 日志文件说明

每次审核在 `logs/` 目录生成：

```
logs/
├── 00_review_session.json      # 审核会话元信息
├── 01_quick_scan.md            # 5分钟快速画像
├── 02_methodology_review.md    # Agent 1: 实验设计审计
├── 02_methodology_review.json  # Agent 1: 结构化输出
├── 03_domain_review.md         # Agent 2: 领域评估
├── 03_domain_review.json       # Agent 2: 结构化输出
├── 04_narrative_review.md      # Agent 3: 写作质量
├── 04_narrative_review.json
├── 05_format_review.md         # Agent 4: LaTeX/格式
├── 05_format_review.json
├── 06_reference_review.md      # Agent 5: 引用质量
├── 06_reference_review.json
├── 07_integrity_review.md      # Agent 6: 完整性
├── 07_integrity_review.json
└── ...
```

每个 `.json` 包含该 Agent 的结构化输出（评分、问题列表、修复建议）。
每个 `.md` 包含该 Agent 的人类可读审稿意见。

## 导出格式

### 最终 Report (Markdown)
```markdown
# Paper Super Review Report
## Review Setup
## Paper Summary
## Quick Scan
## Quantitative Scorecard (6维 × 5分)
## Reviewer Panel (6 Agent 详细意见)
## Cross-Review Synthesis
## Concern-to-Action Table
## AC / Meta-Review
## Appendix: Full Agent Logs
```

### 评分卡 (JSON)
```json
{
  "paper": "ab_test_report.tex",
  "timestamp": "2026-06-25T13:00:00",
  "scores": {
    "novelty": 3, "soundness": 4, "evidence": 2,
    "related_work": 3, "reproducibility": 4, "significance": 3
  },
  "total": 19,
  "verdict": "Weak Accept",
  "confidence": 0.85
}
```

---

## 六智能体

### Agent 1 — 方法论仲裁者
实验设计审计 · 12项检查 · 统计检验验证 · 可复现性评估

### Agent 2 — 领域导航者
创新定位 · SOTA对比 · 遗漏基线检测 · 贡献评估

### Agent 3 — 叙事编辑者
写作质量 · 段落逻辑流 · AI-ism检测 · 可读性

### Agent 4 — 格式守卫者
LaTeX 3遍编译 · warning全解析 · 精确修复代码

### Agent 5 — 引用审计者
引用质量评分(1-5) · BibTeX完整性 · 香火引用检测

### Agent 6 — 完整性侦探
Claim-evidence对齐 · 数字一致性 · 数据诚实

---

## 15 Skill 家族

| # | Skill | 类型 | 说明 |
|---|-------|------|------|
| 1 | `paper-super-reviewer` | 主编排 | 调度全部子 skill，输出综合报告 |
| 2 | `paper-methodology-reviewer` | 核心 | Agent 1 · 实验设计审计 |
| 3 | `paper-domain-reviewer` | 核心 | Agent 2 · 领域评估 |
| 4 | `paper-narrative-editor` | 核心 | Agent 3 · 写作质量 |
| 5 | `paper-format-guardian` | 核心 | Agent 4 · LaTeX审计 |
| 6 | `paper-reference-auditor` | 核心 | Agent 5 · 引用审计 |
| 7 | `paper-integrity-detective` | 核心 | Agent 6 · 完整性 |
| 8 | `paper-quick-scan` | 快速 | 5分钟论文画像 |
| 9 | `paper-scorecard` | 快速 | CCF 6维评分卡 |
| 10 | `paper-venue-match` | 快速 | 投稿匹配 |
| 11 | `paper-latex-audit` | 深度 | LaTeX深度审计 |
| 12 | `paper-citation-audit` | 深度 | 引用深度审计 |
| 13 | `paper-claim-audit` | 深度 | Claim审计 |
| 14 | `paper-data-audit` | 深度 | 数据审计 |
| 15 | `paper-rebuttal-builder` | 产出 | Rebuttal生成 |

---

## 安装

```bash
# Hermes Agent
hermes skills install paper-super-reviewer

# Claude Code
mkdir -p ~/.claude/skills/paper-super-reviewer
cp SKILL.md ~/.claude/skills/paper-super-reviewer/

# Codex CLI
mkdir -p ~/.codex/skills/paper-super-reviewer
cp -R skills/* ~/.codex/skills/paper-super-reviewer/

# 完整安装
git clone https://github.com/TheeTarnished/paper-super-reviewer.git
cp -R skills/* ~/.hermes/skills/research/
```

## 使用

```
# 完整超审 (自动生成 log + report)
审核论文: path/to/paper.tex, mode=full

# 快速扫描
快速扫描: path/to/paper.pdf

# 单个 Agent
审核实验设计: path/to/paper.tex
检查引用: path/to/paper.tex path/to/refs.bib
```
