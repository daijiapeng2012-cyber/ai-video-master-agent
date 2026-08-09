# Knowledge Base

本目录保存 AI 视频大师Agent 的本地知识底座。

## 文件说明

- `abilities/seed_abilities.json`：当前可复用能力 seed
- `cases/*.json`：公开案例 seed
- `schemas/ability.schema.json`：能力结构
- `schemas/case.schema.json`：案例结构

## 设计目标

1. 支持 Git 管理
2. 支持后续同步到 Notion
3. 支持每周生成公开周报
4. 支持未来做搜索、路由和推荐

## 字段原则

### 能力

能力应回答：

- 这个规则叫什么
- 它解决什么问题
- 适用于哪个阶段
- 规则最小模板是什么
- 来自哪些案例

### 案例

案例应回答：

- 来源是谁
- 类型是什么
- 可信度如何
- 方法亮点是什么
- 能抽出什么能力
- 证据边界在哪里
