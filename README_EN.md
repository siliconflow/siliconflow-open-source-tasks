# SiliconFlow Open Source Contribution Tasks

Welcome to the **SiliconFlow Ecosystem Program**!

AI products are evolving faster than ever. To make SiliconFlow more accessible and reduce integration friction for users, we're launching an ecosystem co-building initiative, inviting contributors to bring SiliconFlow support to popular open-source projects. Whether you'd like to help submit an integration PR, or suggest a project that should support SiliconFlow, we'd love to have you involved.

Once your PR is successfully merged by the target open source project, you'll receive a SiliconFlow credit voucher valid across the entire international platform, plus a chance to receive exclusive SiliconFlow merch 🎉

---

## 📋 Task List

👉 [View Task List (CSV)](https://github.com/siliconflow/siliconflow-open-source-tasks/blob/main/tasks.csv)

> **Notes**
> - The `Owner` and `PR` columns are updated when a task is claimed or a PR is submitted. `Source` distinguishes official tasks from community-submitted ones.
> - Data is auto-generated from Issues.

---

## 🧩 How to Claim a Task

1. Browse the task list and pick a project you're interested in
2. Open the corresponding Issue
3. Leave a comment in the Issue:

```
/claim
```

**Once claimed:**
- The task will be automatically marked as taken
- Your GitHub ID will be recorded as the `Owner`

> **Notes**
> - Each task can only be claimed by one person — first come, first served
> - Please don't claim tasks that are already taken
> - Make reasonable progress after claiming; tasks with no progress for more than **2 weeks** may be released back to the pool

---

## 🚀 How to Submit a PR

Once your work is done, reply in the same Issue:

```
/submit <your PR link>
```

**The system will automatically:**
- Record your PR link
- Update the task table ([`tasks.csv`](https://github.com/siliconflow/siliconflow-open-source-tasks/blob/main/tasks.csv))

> **Notes**
> - [`tasks.csv`](https://github.com/siliconflow/siliconflow-open-source-tasks/blob/main/tasks.csv) is auto-generated and merged manually by maintainers — there may be a short delay; the Issue is the source of truth
> - PR status is checked periodically (`open` / `merged` / `closed`)
> - A task is considered complete only when the PR is successfully merged by the target project

---

## ✨ Propose a New Task

Don't see the project you want to integrate? Or is there a tool you use and love that you'd like to see support SiliconFlow? Submit it as a new task — community proposals are very welcome.

1. Click **New Issue**
2. Select **New Task Proposal** → [Direct link](https://github.com/siliconflow/siliconflow-open-source-tasks/issues/new/choose)
3. Fill in:
   - Project name
   - GitHub Repo
   - Why this integration matters

**Once approved, we will:**
- Add it to the task pool ([`tasks.csv`](https://github.com/siliconflow/siliconflow-open-source-tasks/blob/main/tasks.csv))
- Tag it as `Source = community`
- Open it up for anyone to claim

---

## 🌐 API Platform

All integrations in this repo target the **SiliconFlow international platform**:

| | |
|---|---|
| Website | [siliconflow.com](https://siliconflow.com) |
| Base URL | `https://api.siliconflow.com/v1` |
| API Key | [cloud.siliconflow.com](https://cloud.siliconflow.com) |

---

## 🎯 Integration Reference

API Reference: [docs.siliconflow.com](https://docs.siliconflow.com)

We support two widely-used API specs. Choose based on what the target project already uses:

### 1. OpenAI-Compatible API *(Recommended — works for most projects)*

Quickstart guide: [SiliconFlow OpenAI-Compatible Quickstart](https://docs.siliconflow.com)

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://api.siliconflow.com/v1"  # International platform endpoint
)

response = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3",  # Browse all models: https://www.siliconflow.com/models
    messages=[{"role": "user", "content": "Hello, introduce yourself."}],
    max_tokens=1024
)

print(response.choices[0].message.content)
```

> **Note:** This snippet targets the SiliconFlow international platform (`base_url: api.siliconflow.com`). If you're looking for the China endpoint, refer to the CN version of this guide.

### 2. Anthropic-Compatible API

API Reference: [SiliconFlow Anthropic-Compatible API Docs](https://docs.siliconflow.com)

```python
from anthropic import Anthropic

client = Anthropic(
    api_key="YOUR_API_KEY",
    base_url="https://api.siliconflow.com/"  # International platform endpoint
)

response = client.messages.create(
    model="deepseek-ai/DeepSeek-V3",  # Browse all models: https://www.siliconflow.com/models
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, introduce yourself."}
    ]
)

print(response.content[0].text)
```

> **Note:** This snippet targets the SiliconFlow international platform (`base_url: api.siliconflow.com`). If you're looking for the China endpoint, refer to the CN version of this guide.

---

## 📌 Guidelines

- Follow GitHub community standards when claiming and submitting tasks
- Make sure your PR provides a complete, working integration — not just a stub

---

## 🎁 Rewards *(Claim after your PR is merged)*

Once your PR is successfully merged by the target open source project, you'll receive:

- 🎟️ SiliconFlow credit voucher, valid across the entire international platform
- 🎁 SiliconFlow merch, shipped directly to you as a thank-you from the community

> Rewards may vary based on project impact and contribution quality. Merch availability subject to stock.

### 📬 How to Claim

Send an email to [community@siliconflow.com](mailto:community@siliconflow.com) with the subject line:

```
[SiliconFlow Open Source Reward] + your GitHub ID
```

**Include the following in your email:**
- GitHub ID
- Task Issue link
- PR link (merged)
- The SiliconFlow account email you'd like the credit applied to

**Attach screenshots of:**
- The merged PR on GitHub
- Your GitHub profile page (to verify account ownership)

### ⚠️ Additional Notes

- Each task is eligible for one reward claim only
- Please ensure all information is accurate to avoid delays in credit issuance
- Credits will be issued in batches after review
- For questions, leave a comment on the Issue or reach out via email
