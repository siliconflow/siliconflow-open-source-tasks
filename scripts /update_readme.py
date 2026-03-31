import pandas as pd
import requests
import os
import sys

def get_pr_status(pr_url):
    try:
        if not isinstance(pr_url, str) or pr_url.strip() == "":
            return ""

        api_url = pr_url.replace("https://github.com/", "https://api.github.com/repos/").replace("/pull/", "/pulls/")

        res = requests.get(api_url)

        if res.status_code != 200:
            return ""

        data = res.json()

        if data.get("merged_at"):
            return "merged"
        return data.get("state")  # open / closed

    except Exception as e:
        print(f"获取 PR 状态失败: {e}")
        return ""

try:
    if not os.path.exists("tasks.csv"):
        raise FileNotFoundError("tasks.csv 不存在")

    if not os.path.exists("README.md"):
        raise FileNotFoundError("README.md 不存在")

    df = pd.read_csv("tasks.csv").fillna("")

    # 🔥 更新 PR 状态（保留你的逻辑）
    for i, row in df.iterrows():
        pr = row.get("PR")
        if pr:
            status = get_pr_status(pr)
            df.at[i, "Status"] = status
        else:
            df.at[i, "Status"] = ""   # ✅ 没 PR 就清空状态（修你刚刚的问题）

    # 保存 CSV
    df.to_csv("tasks.csv", index=False)

    # 🔥 新表头（加 Issue）
    table_md = "| Project | Repo | Issue | Owner | PR | Status | Source |\n"
    table_md += "|---------|------|-------|-------|----|--------|--------|\n"

    for _, row in df.iterrows():
        project = row.get("Project", "")
        repo = row.get("Repo", "")
        issue = row.get("Issue", "")
        owner = row.get("Owner", "")
        pr = row.get("PR", "")
        status = row.get("Status", "")
        source = row.get("Source", "")

        # 👉 优化显示（推荐）
        repo_md = f"[link]({repo})" if repo else ""

        # Issue 显示成 #123
        issue_md = ""
        if issue:
            issue_number = issue.split("/")[-1]
            issue_md = f"[#{issue_number}]({issue})"

        pr_md = f"[link]({pr})" if pr else ""

        table_md += f"| {project} | {repo_md} | {issue_md} | {owner} | {pr_md} | {status} | {source} |\n"

    # 更新 README
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = "<!-- TASK_TABLE_START -->"
    end_marker = "<!-- TASK_TABLE_END -->"

    if start_marker not in content or end_marker not in content:
        raise ValueError("README 缺少标记")

    new_content = (
        content.split(start_marker)[0]
        + start_marker + "\n"
        + table_md + "\n"
        + end_marker
        + content.split(end_marker)[1]
    )

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_content)

    print("✅ PR 状态 + README 更新完成")

except Exception as e:
    print(f"❌ 失败: {e}")
    sys.exit(1)
