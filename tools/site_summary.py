def main():
    site_data = [
        {
            "name": "捷报比分",
            "url": "https://pc-winscore.com",
            "keywords": ["捷报比分", "实时比分", "赛事数据", "体育资讯"],
            "description": "提供全球足球篮球实时比分、赛程赛果以及深度赛事数据分析服务。",
            "tags": ["体育", "比分", "赛事", "数据"]
        },
        {
            "name": "球探体育",
            "url": "https://www.qiu-tan.com",
            "keywords": ["球探", "体育数据", "竞彩分析", "赛事预测"],
            "description": "专业体育数据平台，涵盖竞彩分析、球队资料与历史交锋记录。",
            "tags": ["体育", "数据", "竞彩", "分析"]
        },
        {
            "name": "雷速体育",
            "url": "https://www.leisu.com",
            "keywords": ["雷速", "体育直播", "即时比分", "数据指数"],
            "description": "提供覆盖多联赛的即时比分、动画直播与指数变动跟踪。",
            "tags": ["体育", "直播", "比分", "指数"]
        }
    ]

    separator = "=" * 60

    def build_summary(entry):
        kw_line = " | ".join(entry["keywords"])
        tag_line = ", ".join(entry["tags"])
        summary_parts = [
            f"站点名称：{entry['name']}",
            f"访问地址：{entry['url']}",
            f"核心关键词：{kw_line}",
            f"标签分类：{tag_line}",
            f"简要说明：{entry['description']}",
        ]
        return "\n".join(summary_parts)

    print("站点资料结构化摘要")
    print(separator)

    for item in site_data:
        print(build_summary(item))
        print(separator)

    print(f"共收录 {len(site_data)} 个站点")

    print("\n[额外统计] 关键词总数与标签分布")
    all_keywords = set()
    tag_count = {}
    for item in site_data:
        all_keywords.update(item["keywords"])
        for t in item["tags"]:
            tag_count[t] = tag_count.get(t, 0) + 1

    print(f"唯一关键词数量：{len(all_keywords)}")
    print("标签频次：")
    for t, c in sorted(tag_count.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")

    print("\n[摘要生成完成]")


if __name__ == "__main__":
    main()