

<h2 align="center">SiliconFlow 开源贡献任务招募</h2>

<div align="center">

简体中文 / [English](./README_EN.md)

</div>



欢迎加入 **SiliconFlow 生态合作计划**！  

我们诚邀热爱开源的开发者，为热门开源项目贡献 SiliconFlow 模型接入 PR，共同推动开源社区发展。



## 📋 任务列表


👉 [查看任务列表（CSV）](./tasks.csv)


> ⚠️ 注
> - 表格中的 `Owner`、`PR`列由用户认领和提交 PR 时更新，`Source` 区分官方任务 / 用户提交任务
> - 数据由 Issue 同步生成



## 🧩 如何认领任务

1. 在任务列表中选择你感兴趣的项目  
2. 点击进入对应任务的 Issue  
3. 在 Issue 评论区回复：
   ```
   /claim
   ```

 👉 认领成功后：
- 系统会自动标记任务已被认领  
- 你的 GitHub ID 会自动记录为 Owner

> ⚠️ 注
> - 每个任务仅限一人认领，先到先得  
> - 已被认领的任务请勿重复认领  
> - 请在认领后尽快推进，若长期占用未推进，该任务可能会被释放


## 🚀 如何提交 PR

完成开发后，在同一个 Issue 下回复：
```
/submit <你的PR链接>
```

👉 系统会自动：
- 记录 PR 链接  
- 同步更新任务表（ [`tasks.csv`](https://github.com/siliconflow/siliconflow-open-source-tasks/blob/main/tasks.csv) ）  


> ⚠️ 注
> - 任务表（tasks.csv）更新为自动生成，会由维护者手动合并到仓库，可能会有延时，具体以 issue 体现为准
> - PR 状态会定期检测（open / merged / closed）  
> - PR 需被目标开源项目成功合并（Merge）才视为完成   



## ✨ 提交新任务

如果你想接入的项目不在列表中，欢迎提交新任务：

1. 点击 **New Issue**  
2. 选择 **New Task Proposal**   [直达链接](https://github.com/siliconflow/siliconflow-open-source-tasks/issues/new/choose)
3. 填写：
   - 项目名称  
   - GitHub Repo  
   - 接入价值说明  

👉 我们审核通过后将：
- 自动加入任务池（ [`tasks.csv`](https://github.com/siliconflow/siliconflow-open-source-tasks/blob/main/tasks.csv)）  
- 标记 `Source = community`  
- 开放给开发者认领  



## 🌐 API 站点说明（重要）

硅基流动提供两个**完全独立**的 API 平台，请根据使用场景选择接入：

| 站点 | 地址 |  中文界面名称 | 英文界面名称 |Base URL |
|------|------|----------|------|----------|
| 中文站 | https://www.siliconflow.cn | 硅基流动   |  SiliconFlow CN | https://api.siliconflow.cn/v1 |
| 国际站 | https://www.siliconflow.com | SiliconFlow | SiliconFlow |https://api.siliconflow.com/v1 |


> ⚠️ 注
> - 两个站点的账号体系、API Key **不互通**
> - 模型列表、调用地址 **不同**
> - 如需支持全球用户，建议同时接入两站点



## 🎯 参考示例


中文站详细文档可见：[API 手册](https://docs.siliconflow.cn/cn/api-reference)
国际站文档见：[API Reference](https://docs.siliconflow.com/en/api-reference/)


我们提供两种主流兼容规范，开发者可根据目标开源项目的实际情况选择：

### 1. OpenAI 兼容规范（**强烈推荐**，大多数项目首选）

**标准接入说明文档**：  
[SiliconFlow OpenAI 兼容 API 快速开始](https://docs.siliconflow.cn/cn/userguide/quickstart)

**API 兼容示例代码**（Python + `openai` SDK）：

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_KEY",
    base_url="https://api.siliconflow.cn/v1"   # 国际站改为 .com
)

response = client.chat.completions.create(
    model="Pro/zai-org/GLM-4.7",
    messages=[{"role": "user", "content": "你好，请介绍一下自己"}],
    max_tokens=1024
)

print(response.choices[0].message.content)
```

### 2. Anthropic 兼容规范

**标准接入说明文档**：  
[SiliconFlow Anthropic 兼容 API 文档](https://docs.siliconflow.cn/cn/api-reference/chat-completions/messages)

**API 兼容示例代码**（Python + 官方 `anthropic` SDK）：

```python
from anthropic import Anthropic

client = Anthropic(
    api_key="YOUR_KEY",
    base_url="https://api.siliconflow.cn/"   # 国际站改为 .com
)

response = client.messages.create(
    model="Pro/zai-org/GLM-4.7",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "你好，请介绍一下你自己"}
    ]
)

print(response.content[0].text)
```

> ⚠️ 注：国际站与中文站接入方式完全一致，只需将代码中的 `.cn` 替换为 `.com` 即可


## 📌 注意事项

- 认领任务请遵循 GitHub 社区规范  
- 保证提交的 PR 是完整、可运行的接入方案  

---

## 🎁 奖励说明（PR Merge 后领取周边）

当你提交的 PR 被目标开源项目成功 **Merge** 后，即可申请领取 SiliconFlow 官方周边及平台奖励券 🎉


### 📬 领取方式

请将以下信息发送至指定邮箱 community@siliconflow.com：

**邮件标题：**
【SiliconFlow 开源活动奖励申请】+ GitHub ID


#### 📋 邮件内容需包含

请务必提供以下完整信息：

- GitHub ID  
- 对应任务 Issue 链接  
- PR 链接（已 Merge）  
- 收件人姓名  
- 收件地址  
- 联系电话  

并在邮件中附上截图证明：

- PR 已成功 Merge 的截图（GitHub 页面）  
- 该 GitHub ID 的个人主页（证明该账号归属）

---

## ⚠️ 注意事项

- 每个任务仅限领取一次奖励  
- 请确保信息真实有效，否则可能影响发放  
- 我们将在审核通过后统一寄出周边礼品  
- 如有问题可在 Issue 中留言或邮件咨询  



