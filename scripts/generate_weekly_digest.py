#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import date, datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KB = ROOT / "knowledge_base"
REPORTS = ROOT / "reports" / "weekly"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def load_cases() -> list[dict]:
    cases: list[dict] = []
    for path in sorted((KB / "cases").glob("*.json")):
        cases.extend(load_json(path))
    return cases


def load_abilities() -> list[dict]:
    return load_json(KB / "abilities" / "seed_abilities.json")


def build_report(target_date: date) -> str:
    iso_year, iso_week, _ = target_date.isocalendar()
    cases = load_cases()
    abilities = load_abilities()

    stage_counter = Counter()
    type_counter = Counter()
    linked_abilities = Counter()

    for case in cases:
        stage_counter.update(case.get("stages", []))
        type_counter.update(case.get("content_types", []))
        linked_abilities.update(case.get("ability_links", []))

    top_stages = ", ".join(f"{name}({count})" for name, count in stage_counter.most_common(5))
    top_types = ", ".join(f"{name}({count})" for name, count in type_counter.most_common(5))

    lines: list[str] = []
    lines.append(f"# AI 视频大师Agent 周报｜{iso_year}-W{iso_week:02d}")
    lines.append("")
    lines.append(f"- 生成日期：{target_date.isoformat()}")
    lines.append(f"- 案例总数：{len(cases)}")
    lines.append(f"- 能力总数：{len(abilities)}")
    lines.append(f"- 高频阶段：{top_stages or '无'}")
    lines.append(f"- 高频类型：{top_types or '无'}")
    lines.append("")
    lines.append("## 本周重点结论")
    lines.append("")
    lines.append("- 公开高质量方法页仍然优先来自官方博客和开发者文档，而不是二手转述。")
    lines.append("- 稳定能力的核心趋势继续指向 `reference-first`、`selector-first`、`audio/voice consistency`。")
    lines.append("- changelog 类型内容很适合沉淀参数边界和路由规则，但不应直接冒充成片案例。")
    lines.append("")
    lines.append("## 案例清单")
    lines.append("")
    for case in sorted(cases, key=lambda item: item["published_at"], reverse=True):
        lines.append(f"### {case['title']}")
        lines.append("")
        lines.append(f"- 来源：{case['source']}")
        lines.append(f"- 发布时间：{case['published_at']}")
        lines.append(f"- 链接：{case['url']}")
        lines.append(f"- 类型：{', '.join(case['content_types'])}")
        lines.append(f"- 阶段：{', '.join(case['stages'])}")
        lines.append(f"- 方法摘要：{case['summary']}")
        lines.append(f"- 可复制模板：{case['template']}")
        if case.get("ability_links"):
            lines.append(f"- 关联能力：{', '.join(case['ability_links'])}")
        lines.append(f"- 证据边界：{case['evidence_boundary']}")
        lines.append("")
    lines.append("## 能力沉淀")
    lines.append("")
    for ability in sorted(abilities, key=lambda item: item["ability_id"]):
        lines.append(f"### {ability['name']} (`{ability['ability_id']}`)")
        lines.append("")
        lines.append(f"- 类别：{ability['category']}")
        lines.append(f"- 状态：{ability['status']}")
        lines.append(f"- 适用阶段：{', '.join(ability['stages'])}")
        lines.append(f"- 定义：{ability['summary']}")
        lines.append(f"- 模板：{ability['template']}")
        lines.append("")
    lines.append("## 证据边界")
    lines.append("")
    lines.append("- 周报基于本地知识库 seed，而不是实时重新抓全网。")
    lines.append("- 若需要“过去 24 小时”严格时效，应重新执行日常雷达扫描并覆盖相关 seed。")
    lines.append("- 官方 changelog 更适合当作参数约束证据，而非独立视觉质量证明。")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date", default=None, help="Target date in YYYY-MM-DD")
    args = parser.parse_args()

    target_date = (
        datetime.strptime(args.date, "%Y-%m-%d").date() if args.date else date.today()
    )
    iso_year, iso_week, _ = target_date.isocalendar()
    REPORTS.mkdir(parents=True, exist_ok=True)
    output_path = REPORTS / f"{iso_year}-W{iso_week:02d}.md"
    output_path.write_text(build_report(target_date), encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
