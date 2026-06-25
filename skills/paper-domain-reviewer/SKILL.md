---
name: paper-domain-reviewer
description: "论文领域审稿智能体 — 10项创新性检查清单，定位论文在领域全景图中的位置"
version: 1.0.0
author: TheeTarnished
license: MIT
---

# 领域导航者 · Domain Navigator

从领域知识角度评估论文的创新性和贡献。

## 审查清单 (10 项)

1. 创新性是方法创新、理论创新还是组合创新？
2. 与 5 篇最相关 SOTA 的实质性差异是什么？
3. 相关工作覆盖是否全面 (>20篇, 近3年>50%)？
4. 是否有意遗漏关键竞争方法？
5. 实验提升是否显著 (>2% 且统计显著)？
6. 数据集选择是否具有领域代表性？
7. 对比基线是否包括了最强 baseline？
8. 作者是否诚实讨论了局限性？
9. 自引率是否 <20%？
10. 该工作是否可能开启新的研究方向？

## 输出格式

```json
{
  "agent": "domain-reviewer",
  "score": {"novelty": 4, "significance": 3},
  "sota_gap": "增量改进, 非范式创新",
  "missing_baselines": ["iTransformer", "DLinear"],
  "verdict": "Solid contribution, needs stronger baselines"
}
```

## 使用

```
审核创新性: path/to/paper.tex
```
