# Notion 同步合同

这个仓库会与 Notion 协作，但不会完全依赖 Notion。

## 当前映射

见 [`config/notion_sources.json`](../../config/notion_sources.json)。

## 规则

1. 每个案例应是独立记录。
2. 每个长期能力应是独立记录。
3. 创建回执不算完成，必须 fetch-back 和最终验证。
4. 系统页只保留结构，不再承载日报正文。
5. 本仓库保留同一知识的本地可版本化表示。

## 真相源模型

- Git 仓库：公开知识和可复用规则的版本化真相源
- Notion：协作数据库和运营界面

## 未来同步要求

后续同步脚本应做到：

- 先读 schema
- 先按原始链接去重
- 写后回读
- 不能把 create receipt 当成功
