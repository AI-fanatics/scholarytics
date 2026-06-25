# Paper Super Reviewer

[![Stars](https://img.shields.io/github/stars/TheeTarnished/paper-super-reviewer?style=social)](https://github.com/TheeTarnished/paper-super-reviewer)
[![Version](https://img.shields.io/badge/version-2.1.0-blue)](https://github.com/TheeTarnished/paper-super-reviewer)

端到端学术论文超审系统 — Hermes Agent Skill。三智能体并行审稿 + 跨审稿综合。

## 架构

| Agent | 角色 | 职责 |
|-------|------|------|
| Agent 1 | 方法论审稿人 | 技术健全性、实验设计、可复现性 |
| Agent 2 | 领域审稿人 | 创新性、SOTA对比、贡献显著性 |
| Agent 3 | 通才审稿人 | 写作质量、可读性、格式规范 |

## 示范

**[ResNet 审稿报告 →](demo/RESNET_REVIEW.md)** — 何恺明 "Deep Residual Learning" 获 30/30 满分

## 功能

- 定量评分卡 (6维 × 5分制 = 30总分)
- 三智能体独立审稿意见
- 跨审稿综合 (共识优势/风险/分歧)
- 引用质量审计
- LaTeX 格式检查
- 完整性审计 (claim-evidence)
- 关注-行动表 (按严重度排序)

## 安装

### Hermes Agent
```bash
hermes skills install paper-super-reviewer
```

### Claude Code
```bash
mkdir -p ~/.claude/skills/paper-super-reviewer
cp SKILL.md ~/.claude/skills/paper-super-reviewer/
# 使用: /claude skill load paper-super-reviewer
```

### Codex CLI
```bash
mkdir -p ~/.codex/skills/paper-super-reviewer
cp SKILL.md ~/.codex/skills/paper-super-reviewer/
```

## 使用

```
审核论文: path/to/paper.tex, mode=full
```
