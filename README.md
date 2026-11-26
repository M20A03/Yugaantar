# Yugaantar — AI Coding Environment & Tools

Consolidated reference for everything installed and configured in this workspace and machine.

> For the complete list of all installed skills (`3,133` global + `16` built-in + plugin-bundled skills), see [`skills.md`](./skills.md).

---

## 1. Downloaded Repositories in This Workspace

| Project | Path | Purpose |
| :--- | :--- | :--- |
| **Hermes Agent** | [`./hermes-agent`](./hermes-agent) | Nous Research autonomous self-improving AI agent (`NousResearch/hermes-agent`). |
| **OmniRoute** | [`./OmniRoute`](./OmniRoute) | Local AI gateway aggregating 160+ free-tier providers behind `http://localhost:20128/v1` (`cheaper-inference/OmniRoute`). |
| **Skills Master List** | [`./skills.md`](./skills.md) | Single consolidated index of all installed Antigravity skills. |

### Quick Start: OmniRoute + Hermes Agent
1. Start **OmniRoute** (`npx omniroute` or from `./OmniRoute`), open `http://localhost:20128`, connect your free-tier provider accounts (Groq, Mistral, OpenRouter, etc.), and generate a local API key.
2. Install & configure **Hermes Agent** (`uv sync` inside `./hermes-agent` or `curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash`), then run `hermes setup` and point it to:
   - **Base URL:** `http://localhost:20128/v1`
   - **API Key:** your local OmniRoute key *(or use `hermes setup --portal` for Nous Portal OAuth)*.

---

## 2. GitHub Connection
- **CLI:** `gh` (`/home/mayankraj/.local/bin/gh`)
- **Account:** `M20A03` (`github.com`, HTTPS protocol, keyring storage, `gh auth setup-git` configured)
- **Scopes:** `repo`, `read:org`, `gist`
- **Git Identity:** `Mayank Raj <mayankrajgupta01@gmail.com>`

---

## 3. Core Built-In Antigravity Tools

| Tool | Purpose |
| :--- | :--- |
| `run_command` | Execute shell commands in Linux sandbox (`BypassSandbox: true` for network/elevated access). |
| `read_file` | Read text, code, image, PDF, audio, or video files (up to 800 lines / 45KB per call). |
| `write_file` | Create or overwrite files, or append text. |
| `edit_file` | Exact-string replacement within existing files. |
| `search_web` | Live web search for docs, APIs, and facts. |
| `invoke_subagent` / `define_subagent` / `manage_subagents` | Spawn, define, and manage specialized background subagents (`browser`, `research`, `image-generator`, `self`, etc.). |
| `manage_task` | Inspect, send input to, or kill background tasks. |
| `schedule` | One-shot timers and recurring cron triggers. |
| `run_workflow` | Execute Python multi-agent orchestration pipelines. |
| `update_focus` / `update_steps` | Live status phrase and step checklist in chat UI. |
| `call_mcp_tool` / `list_resources` / `read_resource` | Interact with lazy-loaded MCP server tools and resources. |
| `search_marketplace` / `list_plugin_accounts` | Search Agent Marketplace plugins/skills and check connected plugin accounts. |
| `ask_question` | Interactive multiple-choice prompts in chat. |
| `send_message` / `swarm` | Agent-to-agent messaging and swarm coordination. |

---

## 4. MCP Servers (`~/.gemini/antigravity/mcp/`)

**Active in this session:**
- `canva_canva` — Canva design creation, editing, assets, brand kits
- `figma_figma` — Figma design context, screenshots, Code Connect, FigJam, shaders, Weave
- `gemini-api_gemini-api-docs` — Gemini API documentation
- `notion_notion` — Notion search, pages, databases, comments, calendar, sessions
- `railway_mcp` — Railway projects, deployments, services, variables, logs, domains, metrics
- `tavily_tavily` — `tavily_search`, `tavily_extract`, `tavily_crawl`, `tavily_map`, `tavily_research`
- `zapier_zapier` — Zapier actions, workflows, drafts, and triggers across 10,000+ apps

**Additional MCP directories present in `~/.gemini/antigravity/mcp/`:**
`chrome_devtools`, `context7`, `docker`, `fetch`, `figma`, `github`, `huggingface`, `memory`, `playwright`, `postgres`, `redis`, `sequential-thinking`, `StitchMCP`, `vercel-plugin_vercel` *(waiting on user sign-in)*.

---

## 5. Installed Plugins (`~/.gemini/config/plugins/`)
- `canva`
- `figma`
- `gemini-api`
- `invideo`
- `lemo-opuscar`
- `n8n-skills` *(includes 15 official n8n skills: `n8n-agents-official`, `n8n-ai-nodes-official`, `n8n-binary-and-data-official`, `n8n-code-nodes-official`, `n8n-credentials-and-security-official`, `n8n-data-tables-official`, `n8n-debugging-official`, `n8n-error-handling-official`, `n8n-expressions-official`, `n8n-extending-mcp-official`, `n8n-loops-official`, `n8n-node-configuration-official`, `n8n-subworkflows-official`, `n8n-workflow-lifecycle-official`, `using-n8n-skills-official`)*
- `notion`
- `railway` *(includes `use-railway` skill)*
- `tavily`
- `vercel-plugin` *(requires user sign-in)*
- `zapier`

*(Other Marketplace plugins such as `clickup`, `gdocs`, `gsheets`, `gslides`, `chrome-devtools-plugin`, `android-cli-plugin`, `firebase`, `mobbin`, `atlassian-twg-cli`, `cloudflare`, `netlify`, `databricks`, `arize-skills`, and `looker` are available in the Agent Marketplace catalog and not installed locally.)*

---

## 6. Added Tools, AI Agents, Security & Automation Stack

### AI Coding, Agents & Media Tools
- **Freebuff** (`CodebuffAI/freebuff`) — Free terminal/desktop AI coding agent (`npm install -g freebuff`)
- **Palmier Pro** (`palmier-io/palmier-pro`) — AI-native nonlinear video editor with local MCP server
- **Meetily** (`Zackriya-Solutions/meeting-minutes`) — Open-source local AI meeting assistant & transcription
- **Arena AI** (`lmarena.ai`) — Model benchmarking & side-by-side LLM evaluation
- **OpenMontage** (`calesthio/OpenMontage`) — Open-source agentic video production studio
- **AI Agent Dots** (`diggerhq/opendots`, `CopilotKit/OpenDots`, `dot-agents`) — Persistent agent runners & unified `.agents/` config
- **Muse** — AI creative/audio assistant
- **Grok Bot** — Covered by installed skills: `grok-agents`, `grok-build`, `grok-delegate`
- **OpenClaw** — Covered by installed skills: `openclaw-deployment-hardening`, `openclaw-github-repo-commander`, `openclaw-local-mac-mini`, `openclaw-security-hardening`
- **SkillTree** (`24kchengYe/human-skill-tree`) — Modular AI skill tree & learning framework

### Security & AppSec Repositories
- **SafeLine WAF** (`chaitin/SafeLine`) — Self-hosted Web Application Firewall
- **OWASP ZAP** (`zaproxy/zaproxy`) — Dynamic application security testing (DAST) proxy & scanner
- **MobSF** (`MobSF/Mobile-Security-Framework-MobSF`) — Automated mobile app (Android/iOS) security framework

### Automation, Workflows & Productivity
- **Dynamic Workflows** — Installed skill: `open-dynamic-workflows`
- **n8n** — Installed plugin `n8n-skills` (15 official skills: `n8n-agents-official`, `n8n-ai-nodes-official`, `n8n-binary-and-data-official`, `n8n-code-nodes-official`, `n8n-credentials-and-security-official`, `n8n-data-tables-official`, `n8n-debugging-official`, `n8n-error-handling-official`, `n8n-expressions-official`, `n8n-extending-mcp-official`, `n8n-loops-official`, `n8n-node-configuration-official`, `n8n-subworkflows-official`, `n8n-workflow-lifecycle-official`, `using-n8n-skills-official`) + global skills (`n8n-agents`, `n8n-binary-and-data`, `n8n-code-javascript`, `n8n-code-python`, `n8n-code-tool`, `n8n-error-handling`, `n8n-expression-syntax`, `n8n-mcp-tools-expert`, `n8n-multi-instance`, `n8n-node-configuration`, `n8n-subworkflows`, `n8n-validation-expert`, `n8n-workflow-patterns`, `using-n8n-mcp-skills`)
- **Zapier** — Installed plugin `zapier` (`zapier_zapier` MCP) + global skill `zapier-make-patterns`
- **Manus** — Installed skill: `planning-with-files` (Manus-style persistent markdown planning)
- **ClickUp / ClickUp Brain** — Installed skill: `clickup-automation` (+ Marketplace plugin `antigravity-plugins-partners/plugin/clickup`)
- **Runway** — Installed skill: `runway-to-invideo`
- **Notion** — Installed plugin `notion` (`notion_notion` MCP) + global skills: `notion-automation`, `notion-manual-import`, `notion-template-business`

### Deep Learning, Reinforcement Learning, Google Colab & Kaggle
- **Google Colab** — Installed official skill: `colab-operator` (`googlecolab/google-colab-cli`)
- **Kaggle** — Installed official skills: `kaggle-cli` (`kaggle/kaggle-cli`), `write-kaggle-benchmarks` (`kaggle/kaggle-skills`)
- **Reinforcement Learning & Post-Training** — Installed skills: `verl-rl-training` (`orchestra-research/ai-research-skills`), `grpo-rlvr-training` (`wshobson/agents`), `trl-training`
- **Deep Learning & LLM Training** — Installed skills: `huggingface-llm-trainer` (`huggingface/skills`), `finetune-llm`, `train-sentence-transformers`, `unsloth-finetuning`, `huggingface-model-trainer`, `huggingface-vision-trainer`, `huggingface-zerogpu`, `remote-gpu-trainer`, `gpu-server-management`, `gpu-kubernetes-operations`, `machine-learning-ops-ml-pipeline`, `ml-engineer`, `mlops-engineer`, `claude-scientific-skills`
- **Related Marketplace Plugins** — `antigravity-plugins-partners/plugin/databricks`, `antigravity-plugins-partners/plugin/arize-skills` (LLM evals & tracing), `antigravity-plugins-official/plugin/science-overview`

