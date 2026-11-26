# Antigravity Installed Skills Master List

Single consolidated reference of all installed skills on this machine.

## Summary

- **Global Skills (`~/.gemini/config/skills` -> `~/.agents/skills`):** 3139
- **Built-in Skills (`~/.gemini/antigravity/builtin/skills`):** 16
- **Plugin-Bundled Skills (`~/.gemini/config/plugins/*/skills`):** 117

## Verified Highlighted Skills (16 / 16 Present)

| Skill | Location | Status |
| :--- | :--- | :--- |
| `cis-benchmarks` | `~/.gemini/config/skills/cis-benchmarks` | Present |
| `hipaa-compliance` | `~/.gemini/config/skills/hipaa-compliance` | Present |
| `gdpr-compliance` | `~/.gemini/config/skills/gdpr-compliance` | Present |
| `sast-scanning` | `~/.gemini/config/skills/sast-scanning` | Present |
| `expo-dev-client` | `~/.gemini/config/skills/expo-dev-client` | Present |
| `expo-animation` | `~/.gemini/config/skills/expo-animation` | Present |
| `react-native-skills` | `~/.gemini/config/skills/react-native-skills` | Present |
| `nextjs-best-practices` | `~/.gemini/config/skills/nextjs-best-practices` | Present |
| `fastapi-pro` | `~/.gemini/config/skills/fastapi-pro` | Present |
| `pydantic-models-py` | `~/.gemini/config/skills/pydantic-models-py` | Present |
| `docker-compose` | `~/.gemini/config/skills/docker-compose` | Present |
| `use-railway` | `~/.gemini/config/plugins/railway/skills/use-railway` | Present |
| `git-workflow` | `~/.gemini/config/skills/git-workflow` | Present |
| `tdd-workflow` | `~/.gemini/config/skills/tdd-workflow` | Present |
| `pytest-skill` | `~/.gemini/config/skills/pytest-skill` | Present |
| `webapp-testing` | `~/.gemini/config/skills/webapp-testing` | Present |

## Automation, AI Agent, ML/RL, Colab & Kaggle Skills (Verified Present)

| Category | Installed Global Skills | Installed Plugin / Bundled Skills |
| :--- | :--- | :--- |
| **Dynamic Workflows** | `open-dynamic-workflows` | — |
| **n8n** | `n8n-agents`, `n8n-binary-and-data`, `n8n-code-javascript`, `n8n-code-python`, `n8n-code-tool`, `n8n-error-handling`, `n8n-expression-syntax`, `n8n-mcp-tools-expert`, `n8n-multi-instance`, `n8n-node-configuration`, `n8n-subworkflows`, `n8n-validation-expert`, `n8n-workflow-patterns`, `using-n8n-mcp-skills` | `n8n-skills` plugin (15 `*-official` skills) |
| **Zapier** | `zapier-make-patterns` | `zapier` plugin |
| **Notion** | `notion-automation`, `notion-manual-import`, `notion-template-business` | `notion` plugin |
| **ClickUp / Brain** | `clickup-automation` | Marketplace: `antigravity-plugins-partners/plugin/clickup` |
| **Manus** | `planning-with-files` | — |
| **Runway** | `runway-to-invideo` | — |
| **Grok Bot** | `grok-agents`, `grok-build`, `grok-delegate` | — |
| **OpenClaw** | `openclaw-deployment-hardening`, `openclaw-github-repo-commander`, `openclaw-local-mac-mini`, `openclaw-security-hardening` | — |
| **Memory** | `agent-memory`, `agent-memory-discipline`, `agent-memory-mcp`, `agent-memory-systems`, `conversation-memory`, `hierarchical-agent-memory`, `memory-handoff`, `memory-systems`, `mesh-memory`, `project-memory-log`, `tree-ring-memory` | — |
| **Google Colab** | `colab-operator` | — |
| **Kaggle** | `kaggle-cli`, `write-kaggle-benchmarks` | — |
| **Reinforcement Learning** | `verl-rl-training`, `grpo-rlvr-training`, `trl-training` | — |
| **Deep Learning & Training** | `huggingface-llm-trainer`, `finetune-llm`, `train-sentence-transformers`, `unsloth-finetuning`, `huggingface-model-trainer`, `huggingface-vision-trainer`, `huggingface-zerogpu`, `remote-gpu-trainer`, `gpu-server-management`, `gpu-kubernetes-operations`, `machine-learning-ops-ml-pipeline`, `ml-engineer`, `mlops-engineer`, `claude-scientific-skills` | — |

## Built-in Skills (16)

| # | Skill | Description |
| :--- | :--- | :--- |
| 1 | `agy-customizations` | Comprehensive guide and reference for the Antigravity Customization System. Use to explain how customizations work, their loading priorit... |
| 2 | `antigravity_guide` | Provides a comprehensive guide, quick reference, and sitemap for Google Antigravity (AGY), including the Antigravity CLI (agy), Antigravi... |
| 3 | `automation` | Interactive guide to design and create a scheduled background automation. Use this skill when the user wants to create an automated or re... |
| 4 | `conversations` | Manage local Antigravity conversations programmatically over HTTP+JSON: create a new conversation (with an optional initial prompt), list... |
| 5 | `generative_ui` | How to render rich interactive HTML widgets inline in the chat or as standalone artifacts. Use this skill when you want to show the user ... |
| 6 | `mcp-app-development` | Build, package, and debug MCP Apps for Antigravity: MCP server tools whose results render as interactive UI in the conversation, in the s... |
| 7 | `migrate-agent-settings` | Migrates the user's MCP servers, skills, slash commands, subagents, and instruction files from other coding agents (Claude Code, Codex, C... |
| 8 | `migrate-workflows` | Automatically migrate legacy workflows to modern skills across global and workspace configurations. Scans for existing workflows, creates... |
| 9 | `native_swarm` | (Preview & Quota Heavy) Run a swarm: several agents working in parallel on one task, each in its own conversation, collaborating through ... |
| 10 | `permissioned-github` | Guidelines for interacting with GitHub and request permissions from the user when commands fail due to restrictions in the agent environm... |
| 11 | `plugin` | How to manage and create plugins — namespaced bundles of skills, agents, rules, MCP servers and hooks that install, enable and disable as... |
| 12 | `run-workflow` | How to write and run a dynamic workflow script with the `run_workflow` tool: a Python script that orchestrates many agents with `agent`, ... |
| 13 | `swarm_monitor` | ONLY for the native-swarm worker whose brief says it is the monitor. On a timer, it checks whether the whole swarm has stalled and calls ... |
| 14 | `swarm_narrator` | ONLY for the native-swarm worker whose brief says it is the narrator. It watches the board and keeps the facts behind the user's Overview... |
| 15 | `swarm_pane` | ONLY for the coordinator of an active /swarm session. What the coordinator writes so the Swarm UI's Overview can show the swarm's goal, i... |
| 16 | `ui-plugin-navigation` | Discover UI plugin panels relevant to the current task and surface a one-click pill in chat to open (toggle) them in the side pane. Use w... |

## Plugin-Bundled Skills (117)

| # | Plugin | Skill | Description |
| :--- | :--- | :--- | :--- |
| 1 | `canva` | `brand-check` | Check a Canva design against a brand kit and report where it diverges — off-palette colors, non-brand fonts, logo misuse, and off-tone co... |
| 2 | `canva` | `bulk-create` | Bulk-create Canva designs from tabular data using a brand template with autofill fields, producing one design per row. Use when users say... |
| 3 | `canva` | `cli` | Use the Canva CLI (`canva api`) for Canva REST API workflows with local files, scripts, and coding agents. Use when the request needs dir... |
| 4 | `canva` | `edit-design` | Make edits to an existing Canva design — change or fix text, replace/insert/delete images and videos, reformat text (size, weight, style,... |
| 5 | `canva` | `get-design-feedback` | Read a Canva design and return structured, actionable design feedback — visual hierarchy, copy/messaging, layout & spacing, consistency, ... |
| 6 | `canva` | `implement-feedback` | Implement reviewer feedback on a Canva design. Reads all comment threads, synthesises what reviewers want, makes the clear-cut changes di... |
| 7 | `canva` | `resize-for-social-media` | Create channel-ready variants of an existing Canva campaign design. Use when users ask to resize or adapt one campaign for multiple socia... |
| 8 | `figma` | `figma-3d-transforms` | 'Add or edit 3D transforms — depth, perspective, z-axis rotation, tilt, isometric, and parallax looks that flat 2D rotation cannot expres... |
| 9 | `figma` | `figma-code-connect` | Creates and maintains Figma Code Connect template files that map Figma components to code snippets. Use when the user mentions Code Conne... |
| 10 | `figma` | `figma-code-workflows` | Use this skill to bring an existing local project, HTML file, or GitHub repo into Figma as code, or to pull GitHub updates into linked Fi... |
| 11 | `figma` | `figma-create-new-file` | "Always use this skill when the user wants to create a new Figma Design, FigJam, or Slides file. You MUST invoke this skill BEFORE every ... |
| 12 | `figma` | `figma-design-to-code` | "**MANDATORY prerequisite** — you MUST invoke this skill BEFORE calling the `get_design_context` Figma MCP tool. You MUST trigger this sk... |
| 13 | `figma` | `figma-generate-design` | "Use this skill alongside figma-use when the task involves translating an application page, view, or multi-section layout into Figma. Tri... |
| 14 | `figma` | `figma-generate-diagram` | "MANDATORY prerequisite — load this skill BEFORE every `generate_diagram` tool call. NEVER call `generate_diagram` directly without loadi... |
| 15 | `figma` | `figma-generate-library` | "Build or update a professional-grade design system in Figma from a codebase. Use when the user wants to create variables/tokens, build c... |
| 16 | `figma` | `figma-generative-plugins` | "**MANDATORY prerequisite** — load this skill before calling `create_generative_plugin` or `update_generative_plugin`. Use when the user ... |
| 17 | `figma` | `figma-implement-motion` | Translates Figma motion and animations into production-ready application code. Use when implementing animation/motion from a Figma design... |
| 18 | `figma` | `figma-shaders` | "**MANDATORY prerequisite** — load this skill before calling `create_shader` or `update_shader`. Use when the user asks to create, author... |
| 19 | `figma` | `figma-spec` | "This skill is required to create, read, edit, review, or comment on Figma specs. You must read it when working on a PRD, brief, RFC or a... |
| 20 | `figma` | `figma-swiftui` | "SwiftUI ↔ Figma translation. Use whenever the user mentions Swift, SwiftUI, iOS, iPhone, or iPad — in EITHER direction — translating a F... |
| 21 | `figma` | `figma-use` | "**MANDATORY prerequisite** — you MUST invoke this skill BEFORE every `use_figma` tool call. NEVER call `use_figma` directly without load... |
| 22 | `figma` | `figma-use-figjam` | "This skill helps agents use Figma's use_figma MCP tool in the FigJam context. Can be used alongside figma-use which has foundational con... |
| 23 | `figma` | `figma-use-motion` | "Motion / animation context for the `use_figma` MCP tool — animating Figma nodes via manual keyframes, animation styles, easing, and time... |
| 24 | `figma` | `figma-use-slides` | "This skill helps agents use Figma's use_figma MCP tool in the Slides context. Can be used alongside figma-use which has foundational con... |
| 25 | `figma` | `figma-weave-workflows` | "Use BEFORE building, editing or wiring up a Figma Weave workflow graph or AI pipeline with the weave_* MCP tools. Carries the DAG, handl... |
| 26 | `gemini-api` | `gemini-api-cli` | Call the Gemini API from the shell with gemini-api. Use for media generation (images, TTS, music, video), file and YouTube analysis, audi... |
| 27 | `gemini-api` | `gemini-api-dev` | Use this skill when writing code that calls the Gemini API for text generation, multi-turn chat, multimodal understanding, image generati... |
| 28 | `gemini-api` | `gemini-live-api-dev` | Use this skill when building real-time, bidirectional streaming applications with the Gemini Live API, or migrating legacy Live models (2... |
| 29 | `gemini-api` | `gemini-omni-flash-api` | Use this skill for generative video editing, text-to-video, image- and video-referenced video generation, first-frame-to-video, first-and... |
| 30 | `gemini-api` | `genie-4-live-world` | Use this skill when building real-time interactive world generation and simulation apps with Genie 4 (models/genie-4) over the Live Inter... |
| 31 | `invideo` | `higgsfield-to-invideo` | "Use when the person has clips from Higgsfield and wants a finished video: put the clips in order, add captions and music, export." |
| 32 | `invideo` | `hyperframes-to-invideo` | "Use when the person has a HyperFrames composition and wants it finished in invideo: render it to MP4, upload it, then cut it, caption it... |
| 33 | `invideo` | `invideo` | "Use for any video job: make, edit, trim, stitch, caption or grade clips; ads, launches, product and personal videos, invitations, intros... |
| 34 | `invideo` | `invideo-generate` | "Generate images, video, voice-over, music, sound effects and 3D for an invideo video: picking and prompting a model, pricing, narration ... |
| 35 | `invideo` | `invideo-media` | "Get and check media for an invideo video: the person's uploads, stock video, images and music, rights, and the craft of voice-over, musi... |
| 36 | `invideo` | `invideo-pipeline` | "Use for scale and automation: a CSV to many videos, `--json`, idempotency keys, CI with device sign-in, outreach at scale, course batche... |
| 37 | `invideo` | `invideo-timeline` | "Use for operations depth on an invideo timeline: frame math, tracks and layering, keyframes and motion, speed ramps, grades, LUTs, effec... |
| 38 | `invideo` | `magnific-to-invideo` | "Use when the person has clips from Magnific and wants a finished video: put the clips in order, add captions and music, export." |
| 39 | `invideo` | `openedit-to-invideo` | "Use when the person has an OpenEdit plan and wants it finished in invideo: render it to MP4, upload it, then cut it, caption it, add mus... |
| 40 | `invideo` | `remotion-to-invideo` | "Use when the person has a Remotion composition and wants it finished in invideo: render it to MP4, upload it, then cut it, caption it, a... |
| 41 | `invideo` | `runway-to-invideo` | "Use when the person has clips from Runway and wants a finished video: put the clips in order, add captions and music, export." |
| 42 | `lemo-opuscar` | `lemo-opuscar` | Direct and produce short films, commercial promos, explainers, data stories, and technical animations made entirely in code using the Lem... |
| 43 | `n8n-skills` | `n8n-agents-official` | 'Use when the user wants an agent, assistant, or bot in n8n, or is building, editing, testing, publishing, or debugging a first-class n8n... |
| 44 | `n8n-skills` | `n8n-ai-nodes-official` | 'Use when building or editing AI inside an n8n workflow: the AI Agent node, Text Classifier, Information Extractor, Sentiment Analysis, S... |
| 45 | `n8n-skills` | `n8n-binary-and-data-official` | Use when handling files, images, attachments, or binary data in n8n, OR when an AI agent needs to take a user-uploaded file as tool input... |
| 46 | `n8n-skills` | `n8n-code-nodes-official` | Use when the user reaches for a Code node, mentions writing JavaScript or Python in n8n, or any custom logic comes up in workflow design.... |
| 47 | `n8n-skills` | `n8n-credentials-and-security-official` | Use when handling any auth, API keys, tokens, OAuth, bearer tokens, basic auth, or secret values in n8n workflows. Triggers on "API key",... |
| 48 | `n8n-skills` | `n8n-data-tables-official` | Use when working with n8n's built-in Data Tables, designing schemas, inserting/updating/upserting rows, deduping, or querying. Triggers o... |
| 49 | `n8n-skills` | `n8n-debugging-official` | Use when an n8n workflow isn't working, errors appear, results don't match what was expected, or the user says "this isn't working." Trig... |
| 50 | `n8n-skills` | `n8n-error-handling-official` | Use when building any webhook-triggered workflow, scheduled/production-bound workflow, wiring a per-node error output, or any workflow wh... |
| 51 | `n8n-skills` | `n8n-expressions-official` | Use when writing or reviewing n8n expressions (`{{...}}` syntax), `$json` / `$node` references, Luxon date code, or expression errors. Tr... |
| 52 | `n8n-skills` | `n8n-extending-mcp-official` | 'Use when you want to expose an n8n workflow as a tool the coding agent can call. Two cases. (1) Wrap n8n API capabilities the MCP doesn'... |
| 53 | `n8n-skills` | `n8n-loops-official` | Use when working with multi-item data, batches, paginated APIs, rate-limited APIs, fan-out across multiple branches, anything that needs ... |
| 54 | `n8n-skills` | `n8n-node-configuration-official` | 'Use when configuring any n8n node: HTTP, webhooks, database, comms (Slack/Gmail/Discord), AI, triggers, Merge, anything. Triggers on any... |
| 55 | `n8n-skills` | `n8n-subworkflows-official` | Use when building anything multi-step, anything that looks repeatable, anything the user mentions reusing, or any workflow with more than... |
| 56 | `n8n-skills` | `n8n-workflow-lifecycle-official` | Use when starting, designing, organizing, finishing, or shipping an n8n workflow. Covers visual layout (sticky notes), descriptions that ... |
| 57 | `n8n-skills` | `using-n8n-skills-official` | Use when working with n8n workflows or Agents. Load the official n8n routing protocol and the capability skills required for the task. |
| 58 | `notion` | `notion-build-my-engineering-wiki` | Build a personalized Notion engineering home from technical docs, project context, and chat or connected sources. Use to get started with... |
| 59 | `notion` | `notion-create-my-team-handbook` | Create a team handbook in Notion from scattered processes, team documents, requests, and chat context. Make procedures easy to find, show... |
| 60 | `notion` | `notion-database-designer` | Turns scattered notes and recurring work into useful Notion trackers for requests, content plans, or team work. Use to set up or improve ... |
| 61 | `notion` | `notion-knowledge-capture` | Captures conversations and supplied notes as Notion wiki pages, how-to guides, FAQs, decision records, or retrospectives. Use when saving... |
| 62 | `notion` | `notion-meeting-prep` | Prepares meeting agendas, internal pre-reads, and decision briefs using Notion context and relevant research. Use for preparing the next ... |
| 63 | `notion` | `notion-organize-my-semester` | Organize a semester in Notion from course notes, syllabi, assignments, and chat context. Use when getting organized for a course or semes... |
| 64 | `notion` | `notion-plan-marketing-campaigns` | Organize campaign briefs, content ideas, and production work in Notion. Use when planning a marketing campaign, building a content calend... |
| 65 | `notion` | `notion-research-documentation` | Researches questions across Notion sources and synthesizes cited briefs, comparisons, or reports. Use when answering requires discovering... |
| 66 | `notion` | `notion-set-up-my-project` | Create a useful initial Notion project home with tasks, docs, and meeting notes, then work with the user to confirm the team and choose a... |
| 67 | `notion` | `notion-setup` | Set up Notion so your agents can remember your preferences, find your work, and pick up where you left off. |
| 68 | `notion` | `notion-spec-to-implementation` | Converts Notion product or technical specs into implementation plans, linked tasks, and evidence-based progress updates. Use for planning... |
| 69 | `notion` | `notion-weekly-project-digest` | Produces evidence-based weekly project or team updates by comparing reporting periods, tasks, decisions, and blockers in Notion. Use for ... |
| 70 | `railway` | `use-railway` | Operate Railway infrastructure: sign up for or sign in to a Railway account, create projects, provision services, databases, and buckets,... |
| 71 | `tavily` | `core` |  |
| 72 | `tavily` | `developers` |  |
| 73 | `tavily` | `tasks` |  |
| 74 | `vercel-plugin` | `access-protected-vercel-deployment` | Access and test Vercel deployments protected by Vercel Authentication, SSO, or Deployment Protection. Use when curl, agent-browser, Playw... |
| 75 | `vercel-plugin` | `ai-gateway` | Vercel AI Gateway guidance for setup, model discovery, authentication, routing, fallbacks, virtual models, evaluation models, BYOK, budge... |
| 76 | `vercel-plugin` | `ai-sdk` | Vercel AI SDK expert guidance. Use when building AI-powered features — chat interfaces, text generation, structured output, tool calling,... |
| 77 | `vercel-plugin` | `auth` | Authentication integration guidance — Clerk (native Vercel Marketplace), Better Auth, Descope, and Auth0 setup for Next.js applications, ... |
| 78 | `vercel-plugin` | `bootstrap` | Project bootstrapping orchestrator for repos that depend on Vercel-linked resources (databases, auth, and managed integrations). Use when... |
| 79 | `vercel-plugin` | `botid` | "Protect specific routes and server actions from bots in code with Vercel BotID (`botid` npm package). Use when installing BotID, calling... |
| 80 | `vercel-plugin` | `build-agents` | "Default guidance for building AI agents. Use for generic requests to build, create, scaffold, design, architect, or implement an AI agen... |
| 81 | `vercel-plugin` | `cdn-caching` | Debug Vercel CDN caching — cache hit rate, stale content, revalidation behavior, ISR + PPR, per-request cache reasons (cacheReason) and P... |
| 82 | `vercel-plugin` | `chat-sdk` | Vercel Chat SDK expert guidance. Use when building multi-platform chat bots — Slack, Telegram, Microsoft Teams, Discord, Google Chat, Git... |
| 83 | `vercel-plugin` | `client-side-security` | "Protect what runs in your users' browsers on Vercel with a Content-Security-Policy header and Page Integrity script monitoring. Use when... |
| 84 | `vercel-plugin` | `create-a-backend` | Backend architecture guidance. Use when planning, building, or migrating an API or backend; choosing between Functions, Services, contain... |
| 85 | `vercel-plugin` | `custom-metrics` | Emit and query Vercel Custom Metrics. Use proactively whenever you write or change server code that runs as a Vercel Function (route hand... |
| 86 | `vercel-plugin` | `daemons` | Vercel Daemons guidance — long-running background workers built from a Dockerfile and declared under the `daemons` key in vercel.json. Us... |
| 87 | `vercel-plugin` | `deployments-cicd` | Vercel deployment and CI/CD expert guidance. Use when deploying, promoting, rolling back, inspecting deployments, building with --prebuil... |
| 88 | `vercel-plugin` | `domains` | Search, register, connect, transfer, and renew domain names on Vercel using the CLI or Domains Registrar API. Use for domain availability... |
| 89 | `vercel-plugin` | `env-vars` | Vercel environment variable expert guidance. Use when working with .env files, vercel env commands, Secret or Config variable types, OIDC... |
| 90 | `vercel-plugin` | `eve` | "eve framework guidance for durable AI agents and agent-powered applications. Use when creating, editing, or debugging an eve project, wh... |
| 91 | `vercel-plugin` | `flags-sdk` | "Implement feature flags in Next.js or SvelteKit code with the Flags SDK (`flags` npm package). Use when installing or configuring the SD... |
| 92 | `vercel-plugin` | `is-agentic` | Score how ready a website, domain, or public MCP endpoint is for AI agents using Is Agentic, and read or act on the resulting report. Use... |
| 93 | `vercel-plugin` | `knowledge-update` | Corrects outdated LLM knowledge about the Vercel platform and introduces new products. Injected at session start. |
| 94 | `vercel-plugin` | `marketplace` | Vercel Marketplace expert guidance — discovering, installing, and managing third-party integrations via the `vercel integration` CLI. Use... |
| 95 | `vercel-plugin` | `microfrontends` | Guide for building, configuring, and deploying microfrontends on Vercel. Use this skill when the user mentions microfrontends, multi-zone... |
| 96 | `vercel-plugin` | `offload-to-sandbox` | Offload heavy builds, full test suites and parallel experiments from the local machine to Vercel Sandboxes with the `vercel sandbox` CLI.... |
| 97 | `vercel-plugin` | `queues` | Vercel Queues guidance — durable topics with at-least-once delivery, independent consumer groups, retries, delays, and idempotency keys v... |
| 98 | `vercel-plugin` | `react-best-practices` | Vercel's React and Next.js performance rules (70 rules in 8 categories ordered by impact - eliminating waterfalls, bundle size, server-si... |
| 99 | `vercel-plugin` | `routing-middleware` | Vercel Routing Middleware guidance — request interception before cache, rewrites, redirects, personalization. Works with any framework. S... |
| 100 | `vercel-plugin` | `runtime-cache` | Vercel Runtime Cache API guidance — ephemeral per-region key-value cache with tag-based invalidation. Shared across Functions, Routing Mi... |
| 101 | `vercel-plugin` | `vercel-agent` | Vercel Agent guidance — dashboard and Slack chat, code review, Security Review, production investigation, approved actions, and product i... |
| 102 | `vercel-plugin` | `vercel-cli` | Vercel CLI expert guidance. Use when deploying, managing environment variables, linking projects, viewing logs, querying metrics, debuggi... |
| 103 | `vercel-plugin` | `vercel-connect` | Vercel Connect expert guidance for securely obtaining scoped credentials for third-party services on behalf of apps or users. Use when wi... |
| 104 | `vercel-plugin` | `vercel-firewall` | Vercel Firewall expert guidance — automatic DDoS mitigation, the Vercel WAF (custom rules, IP blocking, managed rulesets, rate limiting),... |
| 105 | `vercel-plugin` | `vercel-flags` | "Feature flags, A/B tests, and gradual rollouts with Vercel Flags, in any app or framework. Use whenever the user is planning, adding, ch... |
| 106 | `vercel-plugin` | `vercel-functions` | Vercel Functions expert guidance — Node.js/Bun/Python runtimes, Fluid Compute, long-duration (30 min) functions, large functions (5 GB bu... |
| 107 | `vercel-plugin` | `vercel-sandbox` | Vercel Sandbox guidance — ephemeral Firecracker microVMs for running untrusted code safely. Supports AI agents, code generation, and expe... |
| 108 | `vercel-plugin` | `vercel-schedules` | Vercel Schedules guidance — run a private function, route, or Vercel Queues topic on a cron cadence or once at a set time. Covers static ... |
| 109 | `vercel-plugin` | `vercel-services` | Configure and troubleshoot Vercel Services for multiple frontends and backends in one project. Use when composing a polyglot or multi-ser... |
| 110 | `vercel-plugin` | `vercel-storage` | Vercel storage expert guidance — Blob, Global Config (formerly Edge Config), and Marketplace storage (Neon Postgres, Upstash Redis). Use ... |
| 111 | `vercel-plugin` | `vercel-tracing` | Set up OpenTelemetry instrumentation for Vercel Tracing and query the resulting spans. Use when adding or fixing `@vercel/otel`, wiring a... |
| 112 | `vercel-plugin` | `verification` | "Full-story verification — infers what the user is building, then verifies the complete flow end-to-end: browser → API → data → response.... |
| 113 | `vercel-plugin` | `workflow` | Vercel Workflow SDK expert guidance. Use when building durable workflows, long-running tasks, API routes or agents that need pause/resume... |
| 114 | `zapier` | `zapier-connect` | Connect or reconnect the Zapier MCP server when no Zapier tools are available or authentication has failed. Use when Zapier is not connec... |
| 115 | `zapier` | `zapier-detect-workflows` | Use when the user repeats a request (even a single read) or describes habits, schedules, reuse, or manual work. Users rarely say "workflo... |
| 116 | `zapier` | `zapier-quickstart` | Zapier MCP onboarding for new users. Help the user find something they would want handled again. Show it working once, for real. Then off... |
| 117 | `zapier` | `zapier-status` | Check the health of your Zapier MCP setup. Three modes — health check (dashboard view), audit (find waste and duplicates), diagnose (syst... |

## All Global Skills (3139)

| # | Skill | Description |
| :--- | :--- | :--- |
| 1 | `00-andruia-consultant` | "Usar al iniciar o mejorar un proyecto de IA: diagnostica código y restricciones, propone skills existentes y redacta tareas y un plan de... |
| 2 | `007` | Security audit, hardening, threat modeling (STRIDE/PASTA), Red/Blue Team, OWASP checks, code review, incident response, and infrastructur... |
| 3 | `10-andruia-skill-smith` | "Usar para crear o mejorar una skill de Andru.ia: define entradas y resultados, redacta SKILL.md con ejemplos y límites, valida la estruc... |
| 4 | `20-andruia-niche-intelligence` | "Usar tras definir el sector de un proyecto: prepara un dossier en español con contexto, normas aplicables, patrones UX y riesgos, distin... |
| 5 | `2d-games` | 2D game development principles. Sprites, atlases, tilemaps, physics, cameras, and genre patterns (platformer, top-down). Use for canvas/P... |
| 6 | `2slides-ppt-generator` | "AI-powered presentation generation via the 2slides API — create slides from text, match a reference image style, summarize documents int... |
| 7 | `360-feedback-system` | '360 feedback register: reviewer, subject, review cycle, visibility, due date and score, as CSV, SQL, JSON Schema or Notion on request. U... |
| 8 | `3d-games` | 3D game development principles. Rendering, shaders, physics, cameras. |
| 9 | `3d-web-experience` | "Use when building or debugging web 3D scenes, product configurators or portfolios with Three.js, React Three Fiber or Spline; review ass... |
| 10 | `a4a` | "Connect your AI agent to the A4A end-to-end encrypted agent-to-agent messaging network via local MCP tools or Python SDK." |
| 11 | `aas-compose-stack` | "Preserve the coding agent's explicit AAS skill selection as a validated stack and optional evidence." |
| 12 | `aas-discover` | "Discover AAS skills for an explicit task and compare their complete instructions without installing them." |
| 13 | `aas-review-stack` | "Review AAS stack manifests, preview plans and selection evidence in Workbench without applying changes." |
| 14 | `ab-test-setup` | "Use when designing an A/B or split test: define the hypothesis, control and variants, estimate sample size, verify tracking, and predecl... |
| 15 | `ab-testing` | "When the user wants to plan, design, or implement an A/B test or experiment, or build a growth experimentation program." |
| 16 | `acceptance-orchestrator` | Use when a coding task should be driven end-to-end from issue intake through implementation, review, deployment, and acceptance verificat... |
| 17 | `access-matrix` | 'Access matrix of role-by-module permissions, with per-role scope, confidentiality level and SME tier, as CSV, SQL, JSON Schema or Notion... |
| 18 | `access-review` | Conduct periodic access reviews and certifications. Implement access governance and recertification workflows. Use when managing access c... |
| 19 | `accessibility-compliance-accessibility-audit` | "Audit pages and user journeys against a declared WCAG scope. Use when identifying keyboard, screen-reader, focus or contrast barriers an... |
| 20 | `accesslint-audit` | "Find and fix WCAG 2.2 accessibility issues. Two modes — report (sweep a codebase or page, produce a prioritized written report, no edits... |
| 21 | `accesslint-diff` | "Diff a live page's accessibility violations against a baseline — by default compares uncommitted changes (stash-based), or pass --branch... |
| 22 | `accesslint-scan` | "Audit a live page for accessibility issues, locate each WCAG violation precisely, and return a selector-grounded fix worklist without ed... |
| 23 | `accint-commitments` | Triage acc's open promises and close them with honest real-world verdicts via acc_act(runtime="outcome"). |
| 24 | `accint-frames` | Drain acc's deliberation queue — open/waiting brain_frames checkpointed by headless runs — via acc_act(runtime="continue"). |
| 25 | `accint-solve` | Route a goal through acc's scored-memory loop via acc_act(runtime="solve"); deliberate any returned brain_frame and submit via continue. |
| 26 | `accounting-audit-system-builder` | 'Routes an accounting or audit request to the right module skill, from software selection through monthly closing, asking only what is mi... |
| 27 | `accounting-software-selection` | 'Scores shortlisted accounting packages against 57 evidence-backed fields, emitted as CSV, SQL, JSON Schema or Notion on request. Use for... |
| 28 | `active-directory-attacks` | "Assess Active Directory attack paths using scoped configuration review and controlled synthetic lab validation; identify prerequisites, ... |
| 29 | `activecampaign-automation` | "Automate ActiveCampaign tasks via Rube MCP (Composio): manage contacts, tags, list subscriptions, automation enrollment, and tasks. Alwa... |
| 30 | `ad-campaign-analyzer` | "Analyze cross-channel campaign data, quantify uncertainty, and propose evidence-labeled budget tests without overstating causality." |
| 31 | `ad-creative` | "Create, iterate, and scale paid ad creative for Google Ads, Meta, LinkedIn, TikTok, and similar platforms. Use when generating headlines... |
| 32 | `add-app-clip` | Add an iOS App Clip target to an Expo app. Use when the user mentions App Clip, AASA, apple-app-site-association, appclips, smart app ban... |
| 33 | `address-github-comments` | "Use when you need to address review or issue comments on an open GitHub Pull Request using the gh CLI." |
| 34 | `adhx` | "Fetch any X/Twitter post as clean LLM-friendly JSON. Converts x.com, twitter.com, or adhx.com links into structured data with full artic... |
| 35 | `admin-access-register` | 'Admin account register: system, main and backup admin, seats, plan, 2FA, shared logins and access-review dates, as CSV, SQL, JSON Schema... |
| 36 | `advanced-analytics-dashboard` | 'Dashboard metric register: metric, source module, formula, period, value, target, trend, owner and last-updated, as CSV, SQL, JSON Schem... |
| 37 | `advanced-evaluation` | "Design LLM-as-judge rubrics, direct scores and pairwise comparisons. Use for judge models, evals, position bias and calibration against ... |
| 38 | `advogado-criminal` | Assistente de pesquisa informativa, sem credenciais profissionais, sobre em Maria da Penha, violencia domestica, feminicidio, direito pen... |
| 39 | `advogado-especialista` | 'Apoio a pesquisa juridica brasileira, organizacao de fatos e minutas, com verificacao em fontes oficiais e revisao profissional para cas... |
| 40 | `aegisops-ai` | "Autonomous DevSecOps & FinOps Guardrails. Guide to reviewing Linux kernel patches, Terraform cost changes and Kubernetes policy with a s... |
| 41 | `agent-creator` | "Create custom AI subagents with proper plugin structure, persona generation, and companion routing skills." |
| 42 | `agent-evals` | Build automated evaluation suites for AI agents using golden datasets, rubrics, and regression gates. Use when shipping agent features, v... |
| 43 | `agent-evaluation` | "Evaluate agent behavior with versioned cases and explicit verifiers. Use when comparing agent or prompt changes, reproducing failures, o... |
| 44 | `agent-evaluation-reporting` | "Use when summarizing agent evaluations where autonomous, assisted, failed, timed-out, or invalid outcomes must remain distinct and compa... |
| 45 | `agent-framework-azure-ai-py` | "Build persistent agents on Azure AI Foundry using the Microsoft Agent Framework Python SDK." |
| 46 | `agent-harness-fault-injection` | "Use when an agent workflow needs deterministic recovery evidence for sandbox, MCP/tool, worker, checkpoint, memory, or orchestration fai... |
| 47 | `agent-instructions` | 'Writing or restructuring AGENTS.md or CLAUDE.md, adding a rule (''remember this''), or after an agent ignored a rule it had: make each r... |
| 48 | `agent-manager-skill` | "Manage multiple local CLI agents via tmux sessions (start/stop/monitor/assign) in an explicitly authorized workspace." |
| 49 | `agent-memory` | A hybrid memory system that provides persistent, searchable knowledge management for AI agents. |
| 50 | `agent-memory-discipline` | "Rules for when an agent should recall from long-term memory before acting and when it should save decisions, corrections and failures af... |
| 51 | `agent-memory-mcp` | "A hybrid memory system that provides persistent, searchable knowledge management for AI agents (Architecture, Patterns, Decisions)." |
| 52 | `agent-memory-systems` | "Design tenant-scoped memory, retrieval and retention for agents. Use when planning RAG, conversation history, vector stores or rememberi... |
| 53 | `agent-observability` | Instrument AI agents with tracing, token metrics, latency, and cost visibility. Use for reliability and debugging. |
| 54 | `agent-orchestration-improve-agent` | "Systematic improvement of existing agents through performance analysis, prompt engineering, and continuous iteration." |
| 55 | `agent-orchestration-multi-agent-optimize` | "Optimize multi-agent systems with coordinated profiling, workload distribution, and cost-aware orchestration. Use when improving agent p... |
| 56 | `agent-orchestrator` | Meta-skill que orquestra todos os agentes do ecossistema. Scan automatico de skills, match por capacidades, coordenacao de workflows mult... |
| 57 | `agent-qa-authoring` | "Create, edit, validate, and run Agent QA tests, suites, and hooks through MCP or CLI while preserving canonical IDs and schema contracts." |
| 58 | `agent-qa-debug-fix` | "Debug, patch, and verify failed Agent QA runs from MCP evidence, artifacts, logs, and local code without hiding product or infrastructur... |
| 59 | `agent-qa-result-triage` | "Triage failed Agent QA runs with MCP evidence, artifacts, logs, fixed failure categories, confidence, and actionable next steps." |
| 60 | `agent-reels` | "Find animation and video references on 1human, consult a human-agent shared library, and contribute public creations only with prior own... |
| 61 | `agent-self-scheduling` | "Schedule AI agent runs with cron, loops, or external clocks while avoiding unsafe tight autonomous timers." |
| 62 | `agent-squad` | Main agent orchestrator that coordinates a specialized squad of agents |
| 63 | `agent-tool-builder` | Tools are how AI agents interact with the world. A well-designed tool is the difference between an agent that works and one that hallucin... |
| 64 | `agentflow` | "Orchestrate autonomous AI development pipelines through your Kanban board (Asana, GitHub Projects, Linear). Manages multi-worker Claude ... |
| 65 | `agentfolio` | "Skill for discovering and researching autonomous AI agents, tools, and ecosystems using the AgentFolio directory." |
| 66 | `agentic-actions-auditor` | Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Action, Gemini CLI, OpenAI Co... |
| 67 | `agentic-test-audit` | "Audit a pytest suite: surviving mutants and untested code, flaky, order-dependent and slow tests, and removal candidates checked on held... |
| 68 | `agentic-verify` | "Check that a Python change is caught by tests: run every mutant of the changed lines and write tests until they catch them. Reports evid... |
| 69 | `agentmail` | Email infrastructure for AI agents. Create accounts, send/receive emails, manage webhooks, and inspect billing balance via the AgentMail ... |
| 70 | `agentphone` | Build AI phone agents with AgentPhone API. Use when the user wants to make phone calls, send/receive SMS, manage phone numbers, create vo... |
| 71 | `agents-generator` | "Generate project-specific AGENTS.md and companion rules by analyzing a codebase. Supports full, minimal, update, and dry-run modes with ... |
| 72 | `agents-md` | Create, revise, or audit AGENTS.md files from repository evidence, verified commands, and correctly scoped instructions without overwriti... |
| 73 | `agents-v2-py` | "Build container-based Foundry Agents with Azure AI Projects SDK (HostedAgentDefinition). Use when creating hosted agents with custom con... |
| 74 | `agenttrace-session-audit` | "Audit local AI coding-agent sessions with agenttrace for cost, tool failures, latency, anomalies, health, diffs, and CI gates." |
| 75 | `agy-auto` | "Configure agy-auto PreToolUse security gate to run Antigravity CLI (agy) unattended with layered policy controls instead of --dangerousl... |
| 76 | `agy-delegate` | Delegate coding tasks to the Google Antigravity CLI (`agy`) only when the user explicitly requests it, while the orchestrator retains rev... |
| 77 | `agy-powerline` | "Install, check and restyle the agy-powerline statusline for Antigravity CLI (agy): quotas, model, context window and git on agy's status... |
| 78 | `ahrefs-research` | "Use Ahrefs exports or an authorized connector to score competitor page gaps, qualify backlinks, cluster forum topics and find editorial ... |
| 79 | `ai-agent-development` | "AI agent development workflow for building autonomous agents, multi-agent systems, and agent orchestration with CrewAI, LangGraph, and c... |
| 80 | `ai-agent-evaluation-benchmarking` | 'Autonomous AI agent benchmark evaluation register: task completion rates, planning accuracy, tool invocation precision, and cost benchma... |
| 81 | `ai-agent-security` | Secure AI agents against prompt injection, tool abuse, and data exfiltration with defense-in-depth controls. |
| 82 | `ai-agent-tool-routing` | 'Use when designing or reviewing an AI agent tool registry or MCP router: document parameter schemas, caller authorization, execution lim... |
| 83 | `ai-agents-architect` | Expert in designing and building autonomous AI agents. Masters tool use, memory systems, planning strategies, and multi-agent orchestration. |
| 84 | `ai-analyzer` | AI驱动的综合健康分析系统，整合多维度健康数据、识别异常模式、整理风险因素、提供一般性健康信息。支持智能问答和AI健康报告生成。 |
| 85 | `ai-audiobook-narration` | "Install and use the official AI Audiobook Generator package, pinned by digest, for paid hosted work on the Beatra service." |
| 86 | `ai-blog-intro-writer` | "AI Blog Intro Writer. Use when working with topic and article angle, or article draft." |
| 87 | `ai-code-generation-guardrails` | 'Use when reviewing AI-generated code before merge or execution: plan AST/security checks, isolated behavior tests and evidence, with lan... |
| 88 | `ai-code-review-triage` | "Review AI-authored pull requests when line-by-line reading no longer scales; separate defect detection, product-context checks, and scop... |
| 89 | `ai-coding-agent-guardrails` | Secure AI coding agents (Claude Code, Cursor, Codex, Copilot) with permission boundaries, secret protection, code review gates, and safe ... |
| 90 | `ai-competitor-title-rewriter` | "AI Competitor Title Rewriter. Use when working with competitor title and your page topic." |
| 91 | `ai-content-detector` | "AI Content Detector. Use when working with text to review." |
| 92 | `ai-content-improver` | "AI Content Improver. Use when working with draft text." |
| 93 | `ai-content-outline-generator` | "AI Content Outline Generator. Use when working with topic or reader question." |
| 94 | `ai-dev-jobs-mcp` | "Search indexed AI and ML jobs, inspect listings and employers, match roles, and view salary and market stats via AI Dev Jobs MCP" |
| 95 | `ai-engineer` | Build production-ready LLM applications, advanced RAG systems, and intelligent agents. Implements vector search, multimodal AI, agent orc... |
| 96 | `ai-engineering-toolkit` | "Overview of six AI engineering workflows: prompt evaluation (8-dimension scoring), context budget planning, RAG pipeline design, agent s... |
| 97 | `ai-faq-creator` | "AI FAQ Creator. Use when working with source content or topic." |
| 98 | `ai-headshot-studio` | "Install and use the official AI Headshot Generator package, pinned by digest, for paid hosted work on the Beatra service." |
| 99 | `ai-image-generation-studio` | "Install and use the official AI Image Generator package, pinned by digest, for paid hosted work on the Beatra service." |
| 100 | `ai-image-realism` | "Install and use the official AI Image Realism package, pinned by digest, for paid hosted work on the Beatra service." |
| 101 | `ai-inference-service-mesh` | Use verified service mesh patterns for AI inference traffic management, mTLS, canary releases, policy enforcement, and cross-cluster resi... |
| 102 | `ai-keyword-explainer` | "AI Keyword Explainer. Use when working with keyword or phrase." |
| 103 | `ai-logo-maker` | "Install and use the official AI Logo Maker package, pinned by digest, for paid hosted work on the Beatra service." |
| 104 | `ai-loop` | Runs a bounded spec-build-review development loop with explicit scope, stop conditions, and human approval gates for risky or ambiguous w... |
| 105 | `ai-md` | "Convert human-written CLAUDE.md into AI-native structured-label format. Propose and evaluate structured-label rewrites while preserving ... |
| 106 | `ai-meta-tag-writer` | "AI Meta Tag Writer. Use when working with page copy or factual page summary." |
| 107 | `ai-ml` | "AI and machine learning workflow covering LLM application development, RAG implementation, agent architecture, ML pipelines, and AI-powe... |
| 108 | `ai-multilingual-dubbing` | "Install and use the official Multilingual Voiceover package, pinned by digest, for paid hosted work on the Beatra service." |
| 109 | `ai-native-cli` | "Design spec with 98 rules for building CLI tools that AI agents can safely use. Covers structured JSON output, error handling, input con... |
| 110 | `ai-photo-restyler` | "Install and use the official Photo to Anime package, pinned by digest, for paid hosted work on the Beatra service." |
| 111 | `ai-pipeline-orchestration` | Orchestrate AI/ML pipelines for data ingestion, model training, batch inference, and RAG indexing using Prefect, Airflow, or Dagster. |
| 112 | `ai-podcast-voiceover` | "Install and use the official AI Podcast Voiceover package, pinned by digest, for paid hosted work on the Beatra service." |
| 113 | `ai-product` | "Design and evaluate LLM product features, retrieval, validated outputs, latency, and cost controls." |
| 114 | `ai-prompt-regression-testing` | 'Use when comparing prompt changes against a fixed evaluation set: record actual model settings, required checks, missing results, judge ... |
| 115 | `ai-red-teaming` | Run structured AI red team exercises for jailbreak resistance, data exfiltration risk, harmful output controls, and agent tool abuse resi... |
| 116 | `ai-schema-generator` | "AI Schema Generator. Use when working with visible page content and page URL." |
| 117 | `ai-schema-markup-generator` | "Schema Markup Generator. Use when working with entity type or page facts and canonical page URL." |
| 118 | `ai-security-hardening` | Harden AI/LLM deployments against prompt injection, data exfiltration, model theft, and supply chain attacks. |
| 119 | `ai-seo` | "Optimize content for AI search and LLM citations across AI Overviews, ChatGPT, Perplexity, Claude, Gemini, and similar systems. Use when... |
| 120 | `ai-seo-report` | Write the AI SEO Tracker report brief from live MCP data. Use when the user wants a TL;DR of AI search visibility, a weekly recap, or the... |
| 121 | `ai-snippet-generator` | "AI Snippet Generator. Use when working with question and supporting source text." |
| 122 | `ai-sre-incident-response` | Build AI-focused SRE incident response practices for LLM outages, degraded quality, runaway cost events, and safety regressions. |
| 123 | `ai-storyboard-generator` | "Install and use the official AI Storyboard Generator package, pinned by digest, for paid hosted work on the Beatra service." |
| 124 | `ai-studio-image` | Geracao de imagens humanizadas via Google AI Studio (Gemini). Fotos realistas estilo influencer ou educacional com iluminacao natural e i... |
| 125 | `ai-wrapper-product` | Expert in building products that wrap AI APIs (OpenAI, Anthropic, etc. ) into focused tools people will pay for. Not just "ChatGPT but di... |
| 126 | `aident-loadout` | "Run multi-step work across apps the user connected in Aident Loadout: live action schemas, connection checks, cost preflight, and approv... |
| 127 | `aider-delegate` | Delegate coding tasks to Aider (`aider`) only when the user explicitly requests it, while the orchestrator retains review and landing res... |
| 128 | `airflow-dag-patterns` | "Build production Apache Airflow DAGs with best practices for operators, sensors, testing, and deployment. Use when creating data pipelin... |
| 129 | `airtable-automation` | "Automate Airtable tasks via Rube MCP (Composio): records, bases, tables, fields, views. Always search tools first for current schemas." |
| 130 | `aiseotracker` | Use an authorized AI SEO Tracker connection to inspect tracked prompts, brand mentions, cited domains and competitors across answer engines. |
| 131 | `akf-trust-metadata` | "The AI native file format. EXIF for AI — stamps every file with trust scores, source provenance, and compliance metadata. Embeds into 20... |
| 132 | `alerting-oncall` | Set up alerting rules, configure on-call rotations, and manage incident response workflows. |
| 133 | `algolia-search` | Expert patterns for Algolia search implementation, indexing strategies, React InstantSearch, and relevance tuning |
| 134 | `algorithmic-art` | "Algorithmic philosophies are computational aesthetic movements that are then expressed through code. Output .md files (philosophy), .htm... |
| 135 | `alpha-vantage` | "Access 20+ years of global financial data: equities, options, forex, crypto, commodities, economic indicators, and 50+ technical indicat... |
| 136 | `alternatives-pages` | "Create \"[Competitor] alternative\" and comparison pages for developer tools. Build honest, high-converting comparison content that rank... |
| 137 | `altorank` | "Run AltoRank through its hosted MCP server: readiness audits, Search Console, keyword research, and SEO drafts into a review queue." |
| 138 | `alumni-re-hire-tracker` | 'Alumni and re-hire register: former role, last working day, re-hire eligibility, current employer and re-engagement date, as CSV, SQL, J... |
| 139 | `amazon-alexa` | "Integracao completa com Amazon Alexa para criar skills de voz inteligentes, transformar Alexa em assistente com Claude como cerebro (pro... |
| 140 | `amplitude-automation` | "Automate Amplitude tasks via Rube MCP (Composio): events, user activity, cohorts, user identification. Always search tools first for cur... |
| 141 | `analytics` | "When the user wants to set up, improve, or audit analytics tracking and measurement." |
| 142 | `analytics-product` | "Analytics de produto — PostHog, Mixpanel, eventos, funnels, cohorts, retencao, north star metric, OKRs e dashboards de produto." |
| 143 | `analytics-tracking` | Design, audit, and improve analytics tracking systems that produce reliable, decision-ready data. |
| 144 | `analyze-project` | Forensic root cause analyzer for Antigravity sessions. Classifies scope deltas, rework patterns, root causes, hotspots, and recommends pr... |
| 145 | `anchor-text-analyzer` | "Anchor Text Analyzer. Use when working with links with anchor text and destinations." |
| 146 | `andrej-karpathy` | Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, or refactoring code to avoid overcomplication, m... |
| 147 | `android-cli` | Orchestrates Android development tasks including project creation, deployment, SDK management, and environment diagnostics using the `and... |
| 148 | `android-dev` | "Production-grade Android app development guide covering native (Kotlin/Java), cross-platform (Flutter, RN, KMM), and hybrid architectures." |
| 149 | `android-jetpack-compose-expert` | "Expert guidance for building modern Android UIs with Jetpack Compose, covering state management, navigation, performance, and Material D... |
| 150 | `android-ui-journey-testing` | "XML-specified Android UI journey testing, interactive step execution, assertion verification, and JSON outcome reporting." |
| 151 | `android_ui_verification` | Automated end-to-end UI testing and verification on an Android Emulator using ADB. |
| 152 | `angular` | Modern Angular (v20+) expert with deep knowledge of Signals, Standalone Components, Zoneless applications, SSR/Hydration, and reactive pa... |
| 153 | `angular-best-practices` | "Angular performance optimization and best practices guide. Use when writing, reviewing, or refactoring Angular code for optimal performa... |
| 154 | `angular-migration` | "Master AngularJS to Angular migration, including hybrid apps, component conversion, dependency injection changes, and routing migration." |
| 155 | `angular-state-management` | "Master modern Angular state management with Signals, NgRx, and RxJS. Use when setting up global state, managing component stores, choosi... |
| 156 | `angular-ui-patterns` | "Modern Angular UI patterns for loading states, error handling, and data display. Use when building UI components, handling async data, o... |
| 157 | `animate` | "Build purposeful web animations with appropriate tools, easing, duration, interruption, exits, and reduced-motion support." |
| 158 | `animate-expo` | "Build React Native and Expo motion with gestures, Reanimated, haptics, accessible fallbacks, and device verification." |
| 159 | `animated-github-profile` | Build high-impact, animated GitHub profile READMEs that play like mini-movies using pure SVG, CSS, and SMIL animations. Covers dark/light... |
| 160 | `animation-performance` | "Diagnose dropped animation frames and choose properties, rendering paths, and profiling checks for smooth web motion." |
| 161 | `animation-vocabulary` | "Name a described animation effect using a reverse-lookup motion glossary." |
| 162 | `animejs-animation` | Advanced JavaScript animation library skill for creating complex, high-performance web animations. |
| 163 | `announcement-board` | 'Announcement board: author, category, department, priority, audience, publish and expiry dates, status and acknowledgements, as CSV, SQL... |
| 164 | `anti-deception` | "Use before responding to pressure for agreement, manufactured urgency, authority appeals, or requests to certify unsupported claims; sep... |
| 165 | `anti-reversing-techniques` | "Analyze anti-debugging, obfuscation, and anti-tamper techniques during authorized binary analysis and reverse engineering." |
| 166 | `anti-sleep` | "Keep a Mac awake with caffeinate during long builds, downloads, or supervised automation runs." |
| 167 | `anti-slop-design` | "Autonomous Principal Design Technologist. Cures vibe-coded software from AI frontend slop using curated token archetypes and 7-axis qual... |
| 168 | `anti-sycophancy` | "Eliminate sycophantic agreement patterns in AI responses. Load via /skill anti-sycophancy." |
| 169 | `anti-ui-slop` | "Stop coding agents from shipping generic UI. Extend the product's design system, use UIZZE evidence only when useful, cover required sta... |
| 170 | `antigravity-agent-manager` | "Configure and orchestrate parallel agents using the standalone Antigravity 2.0 Agent Manager and Antigravity IDE." |
| 171 | `antigravity-design-expert` | Core UI/UX engineering skill for building highly interactive, spatial, weightless, and glassmorphism-based web interfaces using GSAP and ... |
| 172 | `antigravity-maintainer-batch-release` | "Run protected AAS maintainer sweeps, PR merge batches, resumable review, immutable distribution, Core checks, and scripted releases. Use... |
| 173 | `antigravity-skill-orchestrator` | "A meta-skill that understands task requirements, dynamically selects appropriate skills, tracks successful skill combinations using agen... |
| 174 | `antigravity-workflows` | "Use when asked to ship a SaaS MVP, audit application security, build an AI agent, run browser QA, or design a domain model with multiple... |
| 175 | `anywrite` | "Compiled CLI covering all 52 endpoints of the Anytype local API — objects, properties, tags, search, chat, files — one binary, no MCP se... |
| 176 | `aomi-transact` | "Use Aomi's standalone CLI or hosted Agent/Pipeline MCP to read chain state and prepare user-authorized transactions. Review durable Comm... |
| 177 | `api-analyzer` | "Validates whether an API request is correct based on provided inputs (method, URL, headers, body, auth, query params)." |
| 178 | `api-and-interface-design` | Guides stable API and interface design. Use when designing APIs, module boundaries, or any public interface. Use when creating REST or Gr... |
| 179 | `api-contract-testing` | "Design and review API contract tests across providers and consumers. Use for schema changes, compatibility regressions and client integr... |
| 180 | `api-design-principles` | "Master REST and GraphQL API design principles to build intuitive, scalable, and maintainable APIs that delight developers and stand the ... |
| 181 | `api-designer` | "Generates complete, production-ready REST API endpoint specifications for any system or domain the user describes." |
| 182 | `api-documentation` | "API documentation workflow for generating OpenAPI specs, creating developer guides, and maintaining comprehensive API documentation." |
| 183 | `api-documentation-generator` | "Generate comprehensive, developer-friendly API documentation from code, including endpoints, parameters, examples, and best practices" |
| 184 | `api-documenter` | Master API documentation with OpenAPI 3.1, AI-powered tools, and modern developer experience practices. Create interactive docs, generate... |
| 185 | `api-endpoint-builder` | "Builds reviewable REST API endpoint scaffolds with validation, error handling, authentication, and documentation. Follows best practices... |
| 186 | `api-fuzzing-bug-bounty` | "Provide comprehensive techniques for testing REST, SOAP, and GraphQL APIs during bug bounty hunting and penetration testing engagements.... |
| 187 | `api-integration` | "Designs event-driven architectures, webhook systems, API chaining flows, ETL pipelines, and integration patterns between services." |
| 188 | `api-integration-architect` | Design, implement, debug, and optimize API integrations with expert-level patterns for REST, GraphQL, webhooks, and authentication flows. |
| 189 | `api-onboarding` | "Reduce time-to-first-API-call (TTFAC) by optimizing every step of the developer onboarding journey. This skill covers authentication sim... |
| 190 | `api-patterns` | "API design principles and decision-making. REST vs GraphQL vs tRPC selection, response formats, versioning, pagination." |
| 191 | `api-rate-limit-handler` | "Implement bounded, idempotency-aware API throttling, backoff, and retry handling for 429 and transient 5xx responses." |
| 192 | `api-sdk-generator` | "Generates client SDK code, API wrapper libraries, request/response models, and language-specific usage patterns for any REST API." |
| 193 | `api-security` | "Authorized security assessment of REST, GraphQL, WebSocket, and SOAP APIs: discovery, authentication and authorization flaws (BOLA/IDOR,... |
| 194 | `api-security-best-practices` | "Implement secure API design patterns including authentication, authorization, input validation, rate limiting, and protection against co... |
| 195 | `api-security-testing` | "API security testing workflow for REST and GraphQL APIs covering authentication, authorization, rate limiting, input validation, and sec... |
| 196 | `api-testing-observability-api-mock` | "You are an API mocking expert specializing in realistic mock services for development, testing, and demos. Design mocks that simulate re... |
| 197 | `apify-actor-development` | "Create, modify and validate Apify Actors with scoped inputs, storage schemas, runtime logic and deployment review." |
| 198 | `apify-actorization` | "Actorization converts existing software into reusable serverless applications compatible with the Apify platform. Actors are programs pa... |
| 199 | `apify-audience-analysis` | Understand audience demographics, preferences, behavior patterns, and engagement quality across Facebook, Instagram, YouTube, and TikTok. |
| 200 | `apify-brand-reputation-monitoring` | "Scrape reviews, ratings, and brand mentions from multiple platforms using Apify Actors." |
| 201 | `apify-competitor-intelligence` | Analyze competitor strategies, content, pricing, ads, and market positioning across Google Maps, Booking.com, Facebook, Instagram, YouTub... |
| 202 | `apify-content-analytics` | Track engagement metrics, measure campaign ROI, and analyze content performance across Instagram, Facebook, YouTube, and TikTok. |
| 203 | `apify-ecommerce` | "Extract product data, prices, reviews, and seller information from any e-commerce platform using Apify's E-commerce Scraping Tool." |
| 204 | `apify-facebook-ads-library-scraper` | "Research Meta Ad Library ads by advertiser or keyword with creative links, dates and disclosed reach or spend through the harshmaur/face... |
| 205 | `apify-generate-output-schema` | Generate output schemas (dataset_schema.json, output_schema.json, key_value_store_schema.json) for an Apify Actor by analyzing its source... |
| 206 | `apify-influencer-discovery` | Find and evaluate influencers for brand partnerships, assess public authenticity signals, and track collaboration performance across Inst... |
| 207 | `apify-integration-development` | Curated upstream guidance for Apify Integration Development; use when the workflow matches the user goal. |
| 208 | `apify-lead-generation` | "Scrape leads from multiple platforms using Apify Actors." |
| 209 | `apify-linkedin-jobs-scraper` | "Search and export LinkedIn job postings with salary, seniority, recruiter and company fields using the harshmaur/linkedin-jobs-scraper A... |
| 210 | `apify-market-research` | Analyze market conditions, geographic opportunities, pricing, consumer behavior, and product validation across Google Maps, Facebook, Ins... |
| 211 | `apify-reddit-scraper` | "Scrape Reddit posts, comments, subreddits and users with the harshmaur/reddit-scraper Apify Actor. No Reddit API key. Keyword search, da... |
| 212 | `apify-tiktok-scraper` | "Research TikTok videos, profiles, hashtags, comments and followers with engagement statistics through the harshmaur/tiktok-scraper Apify... |
| 213 | `apify-trend-analysis` | Discover and track emerging trends across Google Trends, Instagram, Facebook, YouTube, and TikTok to inform content strategy. |
| 214 | `apify-ultimate-scraper` | "Select a candidate Apify Actor for the requested extraction after checking its current schema, provenance, pricing and limits. The Actor... |
| 215 | `apify-youtube-transcript-scraper` | "Get YouTube captions, timestamped quotations, SRT/VTT and translated transcripts for videos, channels and playlists through the harshmau... |
| 216 | `apk-redteam-pipeline` | End-to-end Android APK red-team pipeline |
| 217 | `apk-reverse` | "Android APK reverse engineering: unpacking, Java decompilation, smali modification, repacking and signing, Frida dynamic hooking, and na... |
| 218 | `app-builder` | "Main application building orchestrator. Creates full-stack applications from natural language requests. Determines project type, selects... |
| 219 | `app-lifecycle` | 'Planning a SaaS stage, ''what''s next'', ''where are we'', calling a stage done: the detailed path from an idea to production, each stag... |
| 220 | `app-store-changelog` | Generate user-facing App Store release notes from git history since the last tag. |
| 221 | `app-store-optimization` | "Complete App Store Optimization (ASO) toolkit for researching, optimizing, and tracking mobile app performance on Apple App Store and Go... |
| 222 | `appdeploy` | "Deploy web apps with backend APIs, database, and file storage. Use when the user asks to deploy or publish a website or web app and want... |
| 223 | `appium-skill` | "Generates production-grade Appium mobile automation scripts for Android and iOS in Java, Python, or JavaScript. Supports real device and... |
| 224 | `apple-container` | "Build, run, and manage OCI/Linux containers as lightweight per-container VMs on Apple-silicon macOS using Apple's open-source container ... |
| 225 | `apple-design` | "Apply Apple-inspired interface and motion principles to gestures, typography, depth, feedback, and accessibility on the web." |
| 226 | `apple-notes-search` | "Semantic + keyword search and connection-discovery across the user's own Apple Notes via the apple-notes MCP server. Use when the user w... |
| 227 | `application-performance-performance-optimization` | "Optimize end-to-end application performance with profiling, observability, and backend/frontend tuning. Use when coordinating performanc... |
| 228 | `applicationinsights-web-ts` | "Instrument browser/web apps with the Application Insights JavaScript SDK (@microsoft/applicationinsights-web)." |
| 229 | `architect-review` | "Master software architect specializing in modern architecture" |
| 230 | `architecture` | "Architectural decision-making framework. Requirements analysis, trade-off evaluation, ADR documentation. Use when making architecture de... |
| 231 | `architecture-decision-records` | "Comprehensive patterns for creating, maintaining, and managing Architecture Decision Records (ADRs) that capture the context and rationa... |
| 232 | `architecture-patterns` | "Master proven backend architecture patterns including Clean Architecture, Hexagonal Architecture, and Domain-Driven Design to build main... |
| 233 | `architecture-review` | Review repository architecture using Ontoly Software Graph and MCP capabilities. Use when asked to explain architecture, module boundarie... |
| 234 | `arcmira-find-quotes` | "Search indexed YouTube and podcast transcripts for quotes, speakers and clip boundaries with timestamped source links using Arcmira." |
| 235 | `argocd-gitops` | Implement GitOps with ArgoCD for declarative Kubernetes deployments. |
| 236 | `arm-cortex-expert` | Senior embedded software engineer specializing in firmware and driver development for ARM Cortex-M microcontrollers (Teensy, STM32, nRF52... |
| 237 | `arm-templates` | Deploy Azure resources with ARM templates and Bicep. Create modular deployments and manage dependencies. Use when deploying Azure-native ... |
| 238 | `arrowspace` | "Spectral vector search using graph Laplacian eigenstructure. Use when cosine/L2 similarity misses latent structure in your embeddings." |
| 239 | `article-illustrations` | "Generate hand-drawn 16:9 article illustrations with the Grav character IP, sparse annotations, and absurd but clear visual metaphors." |
| 240 | `artifact-yylo` | Capture and retrieve durable YYLO Ledger artifact Records with intentional profiles, payload modes, provenance, retention, and secret-saf... |
| 241 | `asana-automation` | "Automate Asana tasks via Rube MCP (Composio): tasks, projects, sections, teams, workspaces. Always search tools first for current schemas." |
| 242 | `asin-mcp` | "Find Amazon ASINs, read current offers and price history, and manage a price watchlist with target-price alerts through Asin's MCP serve... |
| 243 | `ask-copilot` | "Use GitHub Copilot CLI in non-interactive mode to ask questions, review code, or generate snippets without manual interaction." |
| 244 | `ask-emil` | Ask which skill or flow fits your situation. A router over the skills in this repo. |
| 245 | `ask-human-expert` | "Ask real executives and domain experts a question through Instant Expert for a written answer or short call: practitioner knowledge, cus... |
| 246 | `ask-matt` | Ask which skill or flow fits your situation. A router over the user-invoked skills in this repo. |
| 247 | `ask-questions-if-underspecified` | Clarify requirements before implementing. Use when serious doubts arise. |
| 248 | `ask-sonner` | "Set up and troubleshoot Sonner React toasts, including promises, loading states, updates, styling, theming, and placement." |
| 249 | `assay` | "Run assay on a web page you just wrote or changed. It opens the page in a real browser, drives every control, and reports where the page... |
| 250 | `asset-inventory` | Maintain IT asset inventory and configuration management database. Track hardware, software, and cloud resources. Use when managing IT as... |
| 251 | `asset-it-management` | 'Asset and IT register: serial, model, condition, assignee, location, purchase value, warranty expiry and return date, as CSV, SQL, JSON ... |
| 252 | `astro` | "Build content-focused websites with Astro — zero JS by default, islands architecture, multi-framework components, and Markdown/MDX suppo... |
| 253 | `astropy` | "Astropy is the core Python package for astronomy, providing essential functionality for astronomical research and data analysis." |
| 254 | `async-python-patterns` | "Comprehensive guidance for implementing asynchronous Python applications using asyncio, concurrent programming patterns, and async/await... |
| 255 | `atlas-cloud-media` | "Generate Atlas Cloud images and videos through its asynchronous media API with schema-first model selection and credential-safe polling." |
| 256 | `atlas-contract` | "Goal-integrity skill. Use for backend/API/persistence, preserve/do-not-change, tests/validation, mocks, rework, multi-part requests. Emi... |
| 257 | `atlas-ledger` | "Companion to atlas-contract. Auto-invoked by its Final Audit on caught drift; also use after Post Reviews or user requests to record a m... |
| 258 | `attack-chain` | "Authorized multi-stage attack-path planning and orchestration spanning reconnaissance, initial access, privilege escalation, lateral mov... |
| 259 | `attack-tree-construction` | "Build comprehensive attack trees to visualize threat paths. Use when mapping attack scenarios, identifying defense gaps, or communicatin... |
| 260 | `attendance` | 'Daily attendance register: check-in and check-out, hours worked, work mode, late minutes, leave and regularisation flags, as CSV, SQL, J... |
| 261 | `audio-transcriber` | "Transform audio recordings into professional Markdown documentation with intelligent summaries using LLM integration" |
| 262 | `audit-agent-run-evidence` | "Use when an agent, harness, gateway, MCP workflow, or multi-step automation claims completion and the available traces, checkpoints, app... |
| 263 | `audit-context-building` | Enables ultra-granular, line-by-line code analysis to build deep architectural context before vulnerability or bug finding. |
| 264 | `audit-log` | 'Audit trail register: timestamp, user, module, record, action, field changed, old and new value, and the reason for the change. Use for ... |
| 265 | `audit-logging` | Implement centralized audit logging and SIEM integration. Configure log retention and security monitoring. Use when implementing audit tr... |
| 266 | `audit-preparation` | 'Audit preparation register: required document, period covered, request and receipt dates, preparer and reviewer, auditor queries and adj... |
| 267 | `audit-skills` | "Expert security auditor for AI Skills and Bundles. Performs non-intrusive static analysis to identify malicious patterns, data leaks, sy... |
| 268 | `auri-core` | "Auri: assistente de voz inteligente (Alexa + modelo Claude configurado e verificado). Visao do produto, persona Vitoria Neural, stack AW... |
| 269 | `auth-implementation-patterns` | "Implement or review authentication and authorization with explicit token, session and resource-access boundaries." |
| 270 | `auto-research` | Research uncertain questions with an explicit, user-approved web search or ChatGPT consultation, then present options and wait for implem... |
| 271 | `autom-mcp` | "Get Google, Bing, Brave, DuckDuckGo and Yahoo results as JSON (web, news, maps, shopping, jobs, images, AI Mode) through Autom's MCP ser... |
| 272 | `automated-triage` | Triage Monte Carlo alerts interactively or build an automated workflow. Fetch, score, and troubleshoot alerts using MCP tools now, or des... |
| 273 | `autonomous-agent-patterns` | "Design patterns for building autonomous coding agents, inspired by [Cline](https://github.com/cline/cline) and [OpenAI Codex](https://gi... |
| 274 | `autonomous-agents` | Autonomous agents are AI systems that can independently decompose goals, plan actions, execute tools, and self-correct without constant h... |
| 275 | `autorekt` | "Read live market data with the autorekt CLI before answering questions about prices, market moves, liquidity, positioning, options or pr... |
| 276 | `avalonia-layout-zafiro` | "Guidelines for modern Avalonia UI layout using Zafiro.Avalonia, emphasizing shared styles, generic components, and avoiding XAML redunda... |
| 277 | `avalonia-viewmodels-zafiro` | "Optimal ViewModel and Wizard creation patterns for Avalonia using Zafiro and ReactiveUI." |
| 278 | `avalonia-zafiro-development` | "Mandatory skills, conventions, and behavioral rules for Avalonia UI development using the Zafiro toolkit." |
| 279 | `avoid-ai-writing` | "Audit and rewrite prose for repetitive, vague, or formulaic wording while preserving meaning, evidence, and the writer's voice." |
| 280 | `awareness-stage-mapper` | "Map audience awareness stages to messaging strategy when planning a campaign, offer, or persuasion sequence." |
| 281 | `awesome-tools` | Submit a software tool to Awesome Tools using the JSON API or browser WebMCP tools, and complete the free backlink path or review the pai... |
| 282 | `aws-agentic-ai` | "AWS Bedrock AgentCore comprehensive expert for deploying and managing AI agents at scale. Use when working with any AgentCore service in... |
| 283 | `aws-cdk-development` | "AWS Cloud Development Kit (CDK) expert for building cloud infrastructure with TypeScript/Python." |
| 284 | `aws-cloudtrail` | Configure AWS CloudTrail for audit logging. Set up organization trails and event analysis. Use when auditing AWS activity. |
| 285 | `aws-compliance-checker` | "Automated compliance checking against CIS, PCI-DSS, HIPAA, and SOC 2 benchmarks" |
| 286 | `aws-cost-cleanup` | "Automated cleanup of unused AWS resources to reduce costs" |
| 287 | `aws-cost-operations` | "AWS cost optimization, monitoring, and operational excellence expert. Use when analyzing AWS bills, estimating costs, setting up CloudWa... |
| 288 | `aws-cost-optimization` | Reduce AWS spend with rightsizing, autoscaling, commitment planning, and storage lifecycle policies. Use when running FinOps reviews, low... |
| 289 | `aws-cost-optimizer` | "Comprehensive AWS cost analysis and optimization recommendations using AWS CLI and Cost Explorer" |
| 290 | `aws-ec2` | Manage EC2 instances, AMIs, and auto-scaling groups. Configure security groups, key pairs, and instance types. Use when deploying compute... |
| 291 | `aws-ecs-fargate` | Deploy containers on ECS and Fargate. Configure task definitions, services, and load balancing. Use when running containerized workloads ... |
| 292 | `aws-iam` | Manage IAM users, roles, and policies. Implement least-privilege access and security best practices. Use when configuring AWS identity an... |
| 293 | `aws-iam-best-practices` | "IAM policy review, hardening, and least privilege implementation" |
| 294 | `aws-lambda` | Build and deploy serverless functions on AWS Lambda. Configure triggers, manage permissions, and optimize performance. Use when implement... |
| 295 | `aws-mcp-setup` | "Configure AWS MCP servers for documentation search and API access. Use when setting up AWS MCP, configuring AWS documentation tools, tro... |
| 296 | `aws-penetration-testing` | "Provide comprehensive techniques for penetration testing AWS cloud environments. Covers IAM enumeration, privilege escalation, SSRF to m... |
| 297 | `aws-rds` | Provision and manage RDS databases. Configure backups, replication, and security. Use when deploying managed relational databases on AWS. |
| 298 | `aws-s3` | Configure S3 buckets, policies, and lifecycle rules. Implement versioning, replication, and security. Use when managing object storage on... |
| 299 | `aws-secrets-manager` | Store and rotate secrets in AWS Secrets Manager. |
| 300 | `aws-secrets-rotation` | "Automate AWS secrets rotation for RDS, API keys, and credentials" |
| 301 | `aws-security-audit` | "Comprehensive AWS security posture assessment using AWS CLI and security best practices" |
| 302 | `aws-serverless` | Specialized skill for building production-ready serverless applications on AWS. Covers Lambda functions, API Gateway, DynamoDB, SQS/SNS e... |
| 303 | `aws-serverless-eda` | "AWS serverless and event-driven architecture expert based on Well-Architected Framework. Use when building serverless APIs, Lambda funct... |
| 304 | `aws-skills` | "Plan and review AWS architecture and infrastructure changes using the upstream AWS skill collection." |
| 305 | `aws-sst-development` | "SST v4 (Ion) expert for managing AWS resources as code with the Pulumi-backed framework." |
| 306 | `aws-vpc` | Design and implement VPCs and networking. Configure subnets, route tables, and security groups. Use when setting up AWS network infrastru... |
| 307 | `awt-e2e-testing` | "AI-powered E2E web testing — eyes and hands for AI coding tools. Declarative YAML scenarios, Playwright execution, visual matching (Open... |
| 308 | `ax-extract-workflow` | "Reconstruct workflow behind a past coding-agent artifact using local ax sessions/commits/skills/tool traces. Use when asked how X was bu... |
| 309 | `axiom` | "First-principles assumption auditor. Classifies each hidden assumption (fact / convention / belief / interest-driven), ranks by fragilit... |
| 310 | `axonx` | "Develop AxonX research plugins and operate quantitative research tasks through CLI or MCP, inspecting execution status, logs, artifacts,... |
| 311 | `azd-deployment` | "Prepare and verify authorized Azure Container Apps deployments with azd. Use for azure.yaml, Bicep, remote builds, managed identity and ... |
| 312 | `azure-ai-agents-persistent-dotnet` | Azure AI Agents Persistent SDK for .NET. Low-level SDK for creating and managing AI agents with threads, messages, runs, and tools. |
| 313 | `azure-ai-agents-persistent-java` | Azure AI Agents Persistent SDK for Java. Low-level SDK for creating and managing AI agents with threads, messages, runs, and tools. |
| 314 | `azure-ai-anomalydetector-java` | "Build anomaly detection applications with Azure AI Anomaly Detector SDK for Java. Use when implementing univariate/multivariate anomaly ... |
| 315 | `azure-ai-contentsafety-java` | "Build content moderation applications using the Azure AI Content Safety SDK for Java." |
| 316 | `azure-ai-contentsafety-py` | Azure AI Content Safety SDK for Python. Use for detecting harmful content in text and images with multi-severity classification. |
| 317 | `azure-ai-contentsafety-ts` | "Analyze text and images for harmful content with customizable blocklists." |
| 318 | `azure-ai-contentunderstanding-py` | Azure AI Content Understanding SDK for Python. Use for multimodal content extraction from documents, images, audio, and video. |
| 319 | `azure-ai-document-intelligence-dotnet` | Azure AI Document Intelligence SDK for .NET. Extract text, tables, and structured data from documents using prebuilt and custom models. |
| 320 | `azure-ai-document-intelligence-ts` | "Extract text, tables, and structured data from documents using prebuilt and custom models." |
| 321 | `azure-ai-formrecognizer-java` | "Build document analysis applications using the Azure AI Document Intelligence SDK for Java." |
| 322 | `azure-ai-language-conversations-py` | Implement Conversational Language Understanding (CLU) using the azure-ai-language-conversations Python SDK. Use when working with Convers... |
| 323 | `azure-ai-ml-py` | Azure Machine Learning SDK v2 for Python. Use for ML workspaces, jobs, models, datasets, compute, and pipelines. |
| 324 | `azure-ai-openai-dotnet` | Azure OpenAI SDK for .NET. Client library for Azure OpenAI and OpenAI services. Use for chat completions, embeddings, image generation, a... |
| 325 | `azure-ai-projects-dotnet` | Azure AI Projects SDK for .NET. High-level client for Azure AI Foundry projects including agents, connections, datasets, deployments, eva... |
| 326 | `azure-ai-projects-java` | Azure AI Projects SDK for Java. High-level SDK for Azure AI Foundry project management including connections, datasets, indexes, and eval... |
| 327 | `azure-ai-projects-py` | "Build AI applications on Microsoft Foundry using the azure-ai-projects SDK." |
| 328 | `azure-ai-projects-ts` | "High-level SDK for Azure AI Foundry projects with agents, connections, deployments, and evaluations." |
| 329 | `azure-ai-textanalytics-py` | Azure AI Text Analytics SDK for sentiment analysis, entity recognition, key phrases, language detection, PII, and healthcare NLP. Use for... |
| 330 | `azure-ai-transcription-py` | Azure AI Transcription SDK for Python. Use for audio-file transcription with timestamps; distinguish this client from streaming and async... |
| 331 | `azure-ai-translation-document-py` | Azure AI Document Translation SDK for batch translation of documents with format preservation. Use for translating Word, PDF, Excel, Powe... |
| 332 | `azure-ai-translation-text-py` | Azure AI Text Translation SDK for real-time text translation, transliteration, language detection, and dictionary lookup. Use for transla... |
| 333 | `azure-ai-translation-ts` | "Text and document translation with REST-style clients." |
| 334 | `azure-ai-vision-imageanalysis-java` | "Build image analysis applications with Azure AI Vision SDK for Java. Use when implementing image captioning, OCR text extraction, object... |
| 335 | `azure-ai-vision-imageanalysis-py` | Azure AI Vision Image Analysis SDK for captions, tags, objects, OCR, people detection, and smart cropping. Use for computer vision and im... |
| 336 | `azure-ai-voicelive-dotnet` | Azure AI Voice Live SDK for .NET. Build real-time voice AI applications with bidirectional WebSocket communication. |
| 337 | `azure-ai-voicelive-java` | Azure AI VoiceLive SDK for Java. Real-time bidirectional voice conversations with AI assistants using WebSocket. |
| 338 | `azure-ai-voicelive-py` | "Build real-time voice AI applications with bidirectional WebSocket communication." |
| 339 | `azure-ai-voicelive-ts` | Azure AI Voice Live SDK for JavaScript/TypeScript. Build real-time voice AI applications with bidirectional WebSocket communication. |
| 340 | `azure-aks` | Deploy and manage Azure Kubernetes Service clusters. Configure node pools, networking, and integrations. Use when running Kubernetes work... |
| 341 | `azure-appconfiguration-java` | Azure App Configuration SDK for Java. Centralized application configuration management with key-value settings, feature flags, and snapsh... |
| 342 | `azure-appconfiguration-py` | Azure App Configuration SDK for Python. Use for centralized configuration management, feature flags, and dynamic settings. |
| 343 | `azure-appconfiguration-ts` | "Centralized configuration management with feature flags and dynamic refresh." |
| 344 | `azure-communication-callautomation-java` | "Build server-side call automation workflows including IVR systems, call routing, recording, and AI-powered interactions." |
| 345 | `azure-communication-callingserver-java` | "⚠️ DEPRECATED: This SDK has been renamed to Call Automation. For new projects, use azure-communication-callautomation instead. This skil... |
| 346 | `azure-communication-chat-java` | "Build real-time chat applications with thread management, messaging, participants, and read receipts." |
| 347 | `azure-communication-common-java` | "Azure Communication Services common utilities for Java. Use when working with CommunicationTokenCredential, user identifiers, token refr... |
| 348 | `azure-communication-sms-java` | "Send SMS messages with Azure Communication Services SMS Java SDK. Use when implementing SMS notifications, alerts, OTP delivery, bulk me... |
| 349 | `azure-compute-batch-java` | Azure Batch SDK for Java. Run large-scale parallel and HPC batch jobs with pools, jobs, tasks, and compute nodes. |
| 350 | `azure-containerregistry-py` | Azure Container Registry SDK for Python. Use for managing container images, artifacts, and repositories. |
| 351 | `azure-cosmos-db-py` | "Build production-grade Azure Cosmos DB NoSQL services following clean code, security best practices, and TDD principles." |
| 352 | `azure-cosmos-java` | Azure Cosmos DB SDK for Java. NoSQL database operations with global distribution, multi-model support, and reactive patterns. |
| 353 | `azure-cosmos-py` | Azure Cosmos DB SDK for Python (NoSQL API). Use for document CRUD, queries, containers, and globally distributed data. |
| 354 | `azure-cosmos-rust` | Azure Cosmos DB SDK for Rust (NoSQL API). Use for document CRUD, queries, containers, and globally distributed data. |
| 355 | `azure-cosmos-ts` | Azure Cosmos DB JavaScript/TypeScript SDK (@azure/cosmos) for data plane operations. Use for CRUD operations on documents, queries, bulk ... |
| 356 | `azure-data-tables-java` | "Build table storage applications using the Azure Tables SDK for Java. Works with both Azure Table Storage and Cosmos DB Table API." |
| 357 | `azure-data-tables-py` | Azure Tables SDK for Python (Storage and Cosmos DB). Use for NoSQL key-value storage, entity CRUD, and batch operations. |
| 358 | `azure-devops` | Set up Azure Pipelines for CI/CD, configure build and release pipelines, manage Azure DevOps projects, and integrate with Azure services. |
| 359 | `azure-eventgrid-dotnet` | Azure Event Grid SDK for .NET. Client library for publishing and consuming events with Azure Event Grid. Use for event-driven architectur... |
| 360 | `azure-eventgrid-java` | "Build event-driven applications with Azure Event Grid SDK for Java. Use when publishing events, implementing pub/sub patterns, or integr... |
| 361 | `azure-eventgrid-py` | Azure Event Grid SDK for Python. Use for publishing events, handling CloudEvents, and event-driven architectures. |
| 362 | `azure-eventhub-dotnet` | Azure Event Hubs SDK for .NET. |
| 363 | `azure-eventhub-java` | "Build real-time streaming applications with Azure Event Hubs SDK for Java. Use when implementing event streaming, high-throughput data i... |
| 364 | `azure-eventhub-py` | Azure Event Hubs SDK for Python streaming. Use for high-throughput event ingestion, producers, consumers, and checkpointing. |
| 365 | `azure-eventhub-rust` | Azure Event Hubs SDK for Rust. Use for sending and receiving events, streaming data ingestion. |
| 366 | `azure-eventhub-ts` | "High-throughput event streaming and real-time data ingestion." |
| 367 | `azure-functions` | Expert patterns for Azure Functions development including isolated worker model, Durable Functions orchestration, cold start optimization... |
| 368 | `azure-functions-devsec` | Build serverless applications on Azure Functions. Configure triggers, bindings, and deployment. Use when implementing serverless workload... |
| 369 | `azure-identity-dotnet` | Azure Identity SDK for .NET. Authentication library for Azure SDK clients using Microsoft Entra ID. Use for DefaultAzureCredential, manag... |
| 370 | `azure-identity-java` | "Authenticate Java applications with Azure services using Microsoft Entra ID (Azure AD)." |
| 371 | `azure-identity-py` | Azure Identity SDK for Python authentication. Use for DefaultAzureCredential, managed identity, service principals, and token caching. |
| 372 | `azure-identity-rust` | Azure Identity SDK for Rust authentication. Use for DeveloperToolsCredential, ManagedIdentityCredential, ClientSecretCredential, and toke... |
| 373 | `azure-identity-ts` | "Authenticate to Azure services with various credential types." |
| 374 | `azure-keyvault` | Manage secrets and certificates in Azure Key Vault. Configure access policies, integrate with Azure services, and implement secure secret... |
| 375 | `azure-keyvault-certificates-rust` | Azure Key Vault Certificates SDK for Rust. Use for creating, importing, and managing certificates. |
| 376 | `azure-keyvault-keys-rust` | 'Azure Key Vault Keys SDK for Rust. Use for creating, managing, and using cryptographic keys. Triggers: "keyvault keys rust", "KeyClient ... |
| 377 | `azure-keyvault-keys-ts` | "Manage cryptographic keys using Azure Key Vault Keys SDK for JavaScript (@azure/keyvault-keys). Use when creating, encrypting/decrypting... |
| 378 | `azure-keyvault-py` | Azure Key Vault SDK for Python. Use for secrets, keys, and certificates management with secure storage. |
| 379 | `azure-keyvault-secrets-rust` | 'Azure Key Vault Secrets SDK for Rust. Use for storing and retrieving secrets, passwords, and API keys. Triggers: "keyvault secrets rust"... |
| 380 | `azure-keyvault-secrets-ts` | "Manage secrets using Azure Key Vault Secrets SDK for JavaScript (@azure/keyvault-secrets). Use when storing and retrieving application s... |
| 381 | `azure-maps-search-dotnet` | Azure Maps SDK for .NET. Location-based services including geocoding, routing, rendering, geolocation, and weather. Use for address searc... |
| 382 | `azure-messaging-webpubsub-java` | "Build real-time web applications with Azure Web PubSub SDK for Java. Use when implementing WebSocket-based messaging, live updates, chat... |
| 383 | `azure-messaging-webpubsubservice-py` | Azure Web PubSub Service SDK for Python. Use for real-time messaging, WebSocket connections, and pub/sub patterns. |
| 384 | `azure-mgmt-apicenter-dotnet` | Azure API Center SDK for .NET. Centralized API inventory management with governance, versioning, and discovery. |
| 385 | `azure-mgmt-apicenter-py` | Azure API Center Management SDK for Python. Use for managing API inventory, metadata, and governance across your organization. |
| 386 | `azure-mgmt-apimanagement-dotnet` | Azure Resource Manager SDK for API Management in .NET. |
| 387 | `azure-mgmt-apimanagement-py` | Azure API Management SDK for Python. Use for managing APIM services, APIs, products, subscriptions, and policies. |
| 388 | `azure-mgmt-applicationinsights-dotnet` | Azure Application Insights SDK for .NET. Application performance monitoring and observability resource management. |
| 389 | `azure-mgmt-arizeaiobservabilityeval-dotnet` | Azure Resource Manager SDK for Arize AI Observability and Evaluation (.NET). |
| 390 | `azure-mgmt-botservice-dotnet` | Azure Resource Manager SDK for Bot Service in .NET. Management plane operations for creating and managing Azure Bot resources, channels (... |
| 391 | `azure-mgmt-botservice-py` | Azure Bot Service Management SDK for Python. Use for creating, managing, and configuring Azure Bot Service resources. |
| 392 | `azure-mgmt-fabric-dotnet` | Azure Resource Manager SDK for Fabric in .NET. |
| 393 | `azure-mgmt-fabric-py` | Azure Fabric Management SDK for Python. Use for managing Microsoft Fabric capacities and resources. |
| 394 | `azure-mgmt-mongodbatlas-dotnet` | "Manage MongoDB Atlas Organizations as Azure ARM resources with unified billing through Azure Marketplace." |
| 395 | `azure-mgmt-weightsandbiases-dotnet` | Azure Weights & Biases SDK for .NET. ML experiment tracking and model management via Azure Marketplace. Use for creating W&B instances, m... |
| 396 | `azure-microsoft-playwright-testing-ts` | "Run Playwright tests at scale with cloud-hosted browsers and integrated Azure portal reporting." |
| 397 | `azure-monitor-audit` | Configure Azure Monitor and Activity Log for auditing. Set up diagnostic settings and log analytics. Use when auditing Azure activity. |
| 398 | `azure-monitor-ingestion-java` | Azure Monitor Ingestion SDK for Java. Send custom logs to Azure Monitor via Data Collection Rules (DCR) and Data Collection Endpoints (DCE). |
| 399 | `azure-monitor-ingestion-py` | Azure Monitor Ingestion SDK for Python. Use for sending custom logs to Log Analytics workspace via Logs Ingestion API. |
| 400 | `azure-monitor-opentelemetry-exporter-java` | Azure Monitor OpenTelemetry Exporter for Java. Export OpenTelemetry traces, metrics, and logs to Azure Monitor/Application Insights. |
| 401 | `azure-monitor-opentelemetry-exporter-py` | Azure Monitor OpenTelemetry Exporter for Python. Use for low-level OpenTelemetry export to Application Insights. |
| 402 | `azure-monitor-opentelemetry-py` | Azure Monitor OpenTelemetry Distro for Python. Use for one-line Application Insights setup with auto-instrumentation. |
| 403 | `azure-monitor-opentelemetry-ts` | "Auto-instrument Node.js applications with distributed tracing, metrics, and logs." |
| 404 | `azure-monitor-query-java` | Azure Monitor Query SDK for Java. Execute Kusto queries against Log Analytics workspaces and query metrics from Azure resources. |
| 405 | `azure-monitor-query-py` | Azure Monitor Query SDK for Python. Use for querying Log Analytics workspaces and Azure Monitor metrics. |
| 406 | `azure-networking` | Configure Azure VNets, NSGs, and Azure Firewall. Implement hub-spoke topology and private endpoints. Use when designing Azure network inf... |
| 407 | `azure-postgres-ts` | Connect to Azure Database for PostgreSQL Flexible Server from Node.js/TypeScript using the pg (node-postgres) package. |
| 408 | `azure-resource-manager-cosmosdb-dotnet` | Azure Resource Manager SDK for Cosmos DB in .NET. |
| 409 | `azure-resource-manager-durabletask-dotnet` | Azure Resource Manager SDK for Durable Task Scheduler in .NET. |
| 410 | `azure-resource-manager-mysql-dotnet` | Azure MySQL Flexible Server SDK for .NET. Database management for MySQL Flexible Server deployments. |
| 411 | `azure-resource-manager-playwright-dotnet` | Azure Resource Manager SDK for Microsoft Playwright Testing in .NET. |
| 412 | `azure-resource-manager-postgresql-dotnet` | Azure PostgreSQL Flexible Server SDK for .NET. Database management for PostgreSQL Flexible Server deployments. |
| 413 | `azure-resource-manager-redis-dotnet` | Azure Resource Manager SDK for Redis in .NET. |
| 414 | `azure-resource-manager-sql-dotnet` | Azure Resource Manager SDK for Azure SQL in .NET. |
| 415 | `azure-search-documents-dotnet` | Azure AI Search SDK for .NET (Azure.Search.Documents). Use for building search applications with full-text, vector, semantic, and hybrid ... |
| 416 | `azure-search-documents-py` | Azure AI Search SDK for Python. Use for vector search, hybrid search, semantic ranking, indexing, and skillsets. |
| 417 | `azure-search-documents-ts` | "Build search applications with vector, hybrid, and semantic search capabilities." |
| 418 | `azure-security-keyvault-keys-dotnet` | Azure Key Vault Keys SDK for .NET. Client library for managing cryptographic keys in Azure Key Vault and Managed HSM. Use for key creatio... |
| 419 | `azure-security-keyvault-keys-java` | "Azure Key Vault Keys Java SDK for cryptographic key management. Use when creating, managing, or using RSA/EC keys, performing encrypt/de... |
| 420 | `azure-security-keyvault-secrets-java` | "Azure Key Vault Secrets Java SDK for secret management. Use when storing, retrieving, or managing passwords, API keys, connection string... |
| 421 | `azure-servicebus-dotnet` | Azure Service Bus SDK for .NET. Enterprise messaging with queues, topics, subscriptions, and sessions. |
| 422 | `azure-servicebus-py` | Azure Service Bus SDK for Python messaging. Use for queues, topics, subscriptions, and enterprise messaging patterns. |
| 423 | `azure-servicebus-rust` | 'Azure Service Bus library for Rust. Send and receive messages using queues, topics, and subscriptions. Triggers: "service bus rust", "Se... |
| 424 | `azure-servicebus-ts` | "Enterprise messaging with queues, topics, and subscriptions." |
| 425 | `azure-speech-to-text-rest-py` | Azure Speech to Text REST API for short audio (Python). Use for simple speech recognition of audio files up to 60 seconds without the Spe... |
| 426 | `azure-sql` | Provision Azure SQL Database and Cosmos DB. Configure security, backups, and replication. Use when deploying managed databases on Azure. |
| 427 | `azure-storage-blob-java` | "Build blob storage applications using the Azure Storage Blob SDK for Java." |
| 428 | `azure-storage-blob-py` | Azure Blob Storage SDK for Python. Use for uploading, downloading, listing blobs, managing containers, and blob lifecycle. |
| 429 | `azure-storage-blob-rust` | Azure Blob Storage SDK for Rust. Use for uploading, downloading, and managing blobs and containers. |
| 430 | `azure-storage-blob-ts` | Azure Blob Storage JavaScript/TypeScript SDK (@azure/storage-blob) for blob operations. Use for uploading, downloading, listing, and mana... |
| 431 | `azure-storage-file-datalake-py` | Azure Data Lake Storage Gen2 SDK for Python. Use for hierarchical file systems, big data analytics, and file/directory operations. |
| 432 | `azure-storage-file-share-py` | Azure Storage File Share SDK for Python. Use for SMB file shares, directories, and file operations in the cloud. |
| 433 | `azure-storage-file-share-ts` | Azure File Share JavaScript/TypeScript SDK (@azure/storage-file-share) for SMB file share operations. |
| 434 | `azure-storage-queue-py` | Azure Queue Storage SDK for Python. Use for reliable message queuing, task distribution, and asynchronous processing. |
| 435 | `azure-storage-queue-rust` | 'Azure Queue Storage library for Rust. Send, receive, and manage queue messages. Triggers: "queue storage rust", "QueueClient rust", "sen... |
| 436 | `azure-storage-queue-ts` | Azure Queue Storage JavaScript/TypeScript SDK (@azure/storage-queue) for message queue operations. Use for sending, receiving, peeking, a... |
| 437 | `azure-vms` | Manage Azure Virtual Machines and scale sets. Configure availability sets and managed disks. Use when deploying compute resources on Azure. |
| 438 | `azure-web-pubsub-ts` | "Real-time messaging with WebSocket connections and pub/sub patterns." |
| 439 | `b2b-hiring-intent-radar` | "Query public read-only ATS feeds across 9 platforms to extract company tech-stack signals, disclosed salary bands, and B2B hiring intent." |
| 440 | `babysit-pr` | 'Babysit a pull request through its bot review rounds: verify, fix, reply, resolve. Use for any babysit or watch-the-PR ask.' |
| 441 | `backend-architect` | Expert backend architect specializing in scalable API design, microservices architecture, and distributed systems. |
| 442 | `backend-dev-guidelines` | "You are a senior backend engineer operating production-grade services under strict architectural and reliability constraints. Use when r... |
| 443 | `backend-development-feature-development` | "Orchestrate end-to-end backend feature development from requirements to deployment. Use when coordinating multi-phase feature delivery a... |
| 444 | `backend-security-coder` | Expert in secure backend coding practices specializing in input validation, authentication, and API security. Use PROACTIVELY for backend... |
| 445 | `backlink-idea-generator` | "Backlink Idea Generator. Use when working with site topic and target audience." |
| 446 | `backlink-tracking-template-generator` | "Backlink Tracking Template Generator. Use when working with tracking goal; existing rows optional." |
| 447 | `backtesting-frameworks` | "Build robust, production-grade backtesting systems that avoid common pitfalls and produce reliable strategy performance estimates." |
| 448 | `backup-recovery` | Implement backup and recovery strategies. Configure rsync, Restic, and cloud backups. Use when designing data protection solutions. |
| 449 | `bamboohr-automation` | "Automate BambooHR tasks via Rube MCP (Composio): employees, time-off, benefits, dependents, employee updates. Always search tools first ... |
| 450 | `base` | "Database management, forms, reports, and data operations with LibreOffice Base." |
| 451 | `basecamp-automation` | "Automate Basecamp project management, to-dos, messages, people, and to-do list organization via Rube MCP (Composio). Always search tools... |
| 452 | `baseline-ui` | Quickly deslop UI code by fixing spacing, hierarchy, typography, and small layout issues. Use when the interface needs a fast cleanup or ... |
| 453 | `bash-defensive-patterns` | "Master defensive Bash programming techniques for production-grade scripts. Use when writing robust shell scripts, CI/CD pipelines, or sy... |
| 454 | `bash-linux` | "Bash/Linux terminal patterns. Critical commands, piping, error handling, scripting. Use when working on macOS or Linux systems." |
| 455 | `bash-pro` | 'Master of defensive Bash scripting for production automation, CI/CD pipelines, and system utilities. Expert in safe, portable, and testa... |
| 456 | `bash-scripting` | "Bash scripting workflow for creating production-ready shell scripts with defensive patterns, error handling, and testing." |
| 457 | `bats-testing-patterns` | "Master Bash Automated Testing System (Bats) for comprehensive shell script testing. Use when writing tests for shell scripts, CI/CD pipe... |
| 458 | `bazel-build-optimization` | "Optimize Bazel builds for large-scale monorepos. Use when configuring Bazel, implementing remote execution, or optimizing build performa... |
| 459 | `bb-methodology` | Use at the START of any bug bounty hunting session, when switching targets, or when feeling lost about what to do next. |
| 460 | `bdi-mental-states` | This skill should be used when the user asks to "model agent mental states", "implement BDI architecture", "create belief-desire-intentio... |
| 461 | `bdistill-behavioral-xray` | "X-ray any AI model's behavioral patterns — refusal boundaries, hallucination tendencies, reasoning style, formatting defaults. No API ke... |
| 462 | `bdistill-knowledge-extraction` | "Extract structured domain knowledge from AI models in-session or from local open-source models via Ollama. No API key needed." |
| 463 | `beachhead-segment` | Choosing the first market or customer segment to win, scored on burning pain, willingness to pay, winnable share and referrals. |
| 464 | `beatra` | "Install and use the official AI Media Generator package, pinned by digest, for paid hosted work on the Beatra service." |
| 465 | `beatra-ai-video-studio` | "Install and use the official Beatra AI Video Studio package, pinned by digest, for paid text-to-video, image-to-video, and video edit or... |
| 466 | `beautiful-prose` | A hard-edged writing style contract for timeless, forceful English prose without modern AI tics. Use when users ask for prose or rewrites... |
| 467 | `before-you-build` | "Review product risk before coding by checking demand, alternatives, channels, switching costs, and failure signals." |
| 468 | `behavioral-modes` | "AI operational modes (brainstorm, implement, debug, review, teach, ship, orchestrate). Use to adapt behavior based on task type." |
| 469 | `better-accessibility` | Reviews and fixes keyboard and focus behavior, ARIA, accessible names, forms, screen-reader announcements, motion and zoom against WCAG 2.2. |
| 470 | `better-colors` | Builds and checks color systems by generating palettes, naming semantic tokens, converting between formats and measuring contrast. |
| 471 | `better-interface` | Reviews a screen, flow or whole interface across accessibility, layout, writing, typography, color and UI polish, and returns one ranked ... |
| 472 | `better-layout` | Sets grouping, alignment, reading order, responsive structure and room for translated text, so a layout holds up when it is resized, tran... |
| 473 | `better-typography` | Sets and reviews how text renders, from the type scale and spacing to font features, wrapping, truncation and punctuation. |
| 474 | `better-ui` | Polishes surfaces, icons and motion with exact values for border radius, optical alignment, shadows, icon states and animation. |
| 475 | `better-writing` | Writes and reviews interface copy, from labels and errors to empty states and confirmations, so it matches the product's voice and tells ... |
| 476 | `bevy-ecs-expert` | "Master Bevy's Entity Component System (ECS) in Rust, covering Systems, Queries, Resources, and parallel scheduling." |
| 477 | `bifrost-gateway` | "Run and configure Bifrost, the open-source AI gateway: one OpenAI-compatible API for 20+ LLM providers with fallbacks, virtual keys and ... |
| 478 | `bilig-workpaper` | "Use formula-backed WorkPaper JSON and MCP tools for agent spreadsheet tasks without driving Excel or a browser UI." |
| 479 | `bill-gates` | "Simulacao educativa de analise estrategica inspirada em temas publicos de Bill Gates; nao representa a pessoa real ou suas opinioes atua... |
| 480 | `billing-automation` | "Master automated billing systems including recurring billing, invoice generation, dunning management, proration, and tax calculation." |
| 481 | `binary-analysis-patterns` | "Comprehensive patterns and techniques for analyzing compiled binaries, understanding assembly code, and reconstructing program logic." |
| 482 | `binary-diff` | "Cross-version binary symbol migration: diff updated binaries, recover function names without PDBs, and propagate annotations after softw... |
| 483 | `biopython` | "Biopython is a comprehensive set of freely available Python tools for biological computation. It provides functionality for sequence man... |
| 484 | `bitbucket-automation` | "Automate Bitbucket repositories, pull requests, branches, issues, and workspace management via Rube MCP (Composio). Always search tools ... |
| 485 | `blitz-copy` | Draft landing-page headlines, email openings, social hooks or titles using a hook, concrete surprise and relevant payoff. |
| 486 | `blitz-seo` | "Plan a 30-day SEO sprint for one existing commercial page with search-intent checks, relevant internal links, first-hand evidence and ch... |
| 487 | `block-ai-scrapers` | Protect authorized web routes against abusive automation with scoped rate limits, verified crawler handling and rollback checks. |
| 488 | `block-storage` | Manage block storage volumes and LVM. Configure cloud block storage and local disks. Use when managing disk storage. |
| 489 | `blockchain-developer` | Build production-ready Web3 applications, smart contracts, and decentralized systems. Implements DeFi protocols, NFT platforms, DAOs, and... |
| 490 | `blockrun` | "BlockRun works with Claude Code and Google Antigravity." |
| 491 | `blockvectra-docs` | "Answer BlockVectra RPC, indexed-data, and Robinhood Chain integration questions from cited documentation. Use for source guidance, not b... |
| 492 | `blog-refresher` | Refresh and improve existing blog posts to outrank competitors using a 6-phase content audit and SERP gap analysis. Use when the user wan... |
| 493 | `blog-title-generator` | "Blog Title Generator. Use when working with topic or page summary." |
| 494 | `blog-writing-guide` | "This skill enforces Sentry's blog writing standards across every post — whether you're helping an engineer write their first blog post o... |
| 495 | `blue-green-deploy` | Configure zero-downtime deployment strategies including blue-green, canary, and rolling deployments. |
| 496 | `bluebook-writing` | "Write design-reading books and articles in plain language with a two-layer skeleton: a zero-terminology everyday story first, then the p... |
| 497 | `blueprint` | "Turn a one-line objective into a step-by-step construction plan any coding agent can execute cold. Each step has a self-contained contex... |
| 498 | `board-governance` | 'Board and governance register: meeting date, agenda, decision, resolution number, vote result, action owner and due date. Use for board ... |
| 499 | `boost-asio-pro` | "Use when writing asynchronous C++ networking code with Boost.Asio or standalone Asio — TCP/UDP servers and clients, SSL/TLS, timers, str... |
| 500 | `boring-marketing-ads-incrementality-check` | "Design a matched ad pause test using call or sales logs." |
| 501 | `boring-marketing-ai-search` | "Audit and improve a brand's citations in AI search results." |
| 502 | `boring-marketing-audience-research` | "Mine public conversations for audience segments and verbatim customer language." |
| 503 | `boring-marketing-brand-voice` | "Extract a brand voice profile with evidence and observable writing checks." |
| 504 | `boring-marketing-competitive-intel` | "Compare competitor positioning, offers, ads and public customer feedback." |
| 505 | `boring-marketing-content-atomizer` | "Adapt an existing asset into native social drafts for the brand's priority channels." |
| 506 | `boring-marketing-creative` | "Plan and produce campaign visuals, product media and short advertising videos." |
| 507 | `boring-marketing-direct-response-copy` | "Draft conversion copy from customer language, evidence and offer constraints." |
| 508 | `boring-marketing-email-sequences` | "Draft lifecycle and sales email sequences with send timing and delivery checks." |
| 509 | `boring-marketing-find-local-clients` | "Build a ranked list of local businesses from public search and directory evidence." |
| 510 | `boring-marketing-first-screen-check` | "Audit what a mobile visitor sees on an ad destination or business homepage." |
| 511 | `boring-marketing-google-ads-tracking` | "Audit Google Ads lead signals and plan or verify tracking corrections." |
| 512 | `boring-marketing-google-business-profile` | "Audit a Google Business Profile against nearby competitors and draft profile posts." |
| 513 | `boring-marketing-keyword-research` | "Organize search queries into topic families, intent and prioritized content briefs." |
| 514 | `boring-marketing-landing-page` | "Build or audit a mobile-first offer page with message match and conversion checks." |
| 515 | `boring-marketing-lead-magnet` | "Research and prototype a useful opt-in resource, quiz or calculator." |
| 516 | `boring-marketing-local-seo-plan` | "Prioritize local SEO fixes, service coverage and location page decisions." |
| 517 | `boring-marketing-long-form-article` | "Research and draft a long-form guide with sourced facts and platform-specific edits." |
| 518 | `boring-marketing-meta-ads` | "Run account preflight, create paused Meta campaigns, and verify pixel and Conversions API events. Use for Facebook Ads API launches, per... |
| 519 | `boring-marketing-newsletter` | "Plan and draft newsletter editions with a clear editorial angle and sourced material." |
| 520 | `boring-marketing-paid-ads` | "Turn an ad matrix into campaign drafts, creative briefs and a measurement plan." |
| 521 | `boring-marketing-performance-review` | "Analyze campaign data to identify a measurable bottleneck and rank next tests." |
| 522 | `boring-marketing-pitch-the-fix` | "Draft a targeted prospect email around one observable business problem and a proposed fix." |
| 523 | `boring-marketing-positioning-angles` | "Build positioning options and an ad matrix from customer and competitive research." |
| 524 | `boring-marketing-programmatic-seo` | "Validate a dataset and build templated SEO pages with genuinely distinct information." |
| 525 | `boring-marketing-reviews` | "Assess review coverage, draft owner replies and plan compliant review requests." |
| 526 | `boring-marketing-seo-content` | "Draft or refresh search content using intent, firsthand evidence and citation gaps." |
| 527 | `boring-marketing-service-area-pages` | "Create distinct local service pages backed by credible evidence for each location." |
| 528 | `boring-marketing-site-audit` | "Crawl a site and prioritize technical SEO fixes. Use to check robots.txt, sitemaps, noindex, duplicate pages, broken links, metadata, pa... |
| 529 | `boring-marketing-social-content` | "Draft original X and LinkedIn posts grounded in a brand's past posts and real numbers." |
| 530 | `boring-marketing-speed-to-lead` | "Analyze missed calls and response time, then design a follow-up workflow." |
| 531 | `boring-marketing-start-here` | "Build project marketing context from business evidence and route work to a matching skill." |
| 532 | `bounce-rate-estimator` | "Bounce Rate Estimator. Use when working with sessions and bounced sessions, or sessions and engaged sessions with metric definition." |
| 533 | `bowmark` | "Use Bowmark when a task depends on what a live website shows right now: current prices, availability or stock, fares and quotes, a site ... |
| 534 | `box-automation` | "Automate Box operations including file upload/download, content search, folder management, collaboration, metadata queries, and sign req... |
| 535 | `brain-to-docs` | "Interview the user to turn project vision and decisions into README and ADR documentation." |
| 536 | `brainstorming` | "You MUST use this before any creative work - creating features, building components, adding functionality, modifying behavior, or planni... |
| 537 | `brand-growth-system-builder` | 'Route requests across 13 brand and growth modules. Use when an SME needs help choosing branding, website, local SEO, content, or cloud-p... |
| 538 | `brand-guidelines` | Write copy following Sentry brand guidelines. Use when writing UI text, error messages, empty states, onboarding flows, 404 pages, docume... |
| 539 | `brand-guidelines-anthropic` | "To access Anthropic's official brand identity and style resources, use this skill." |
| 540 | `brand-guidelines-community` | "To access Anthropic's official brand identity and style resources, use this skill." |
| 541 | `brand-kit-print-collateral` | 'Print collateral spec: item, finished/trim size and artwork size including bleed, bleed, colour mode, stock and GSM, finish, safe margin... |
| 542 | `brand-perception-psychologist` | "Audit visual, verbal, and behavioral brand signals and propose alignment changes when market perception differs from the intended positi... |
| 543 | `brand-vibes` | "Apply a company's design language to a site from 66 brand profiles, or extract a brand's DNA into semantic tokens for Tailwind, CSS vari... |
| 544 | `brave-man` | "Runs a structured clarifying interview for new project requests before building. Instead of writing code, it outputs a fully specified p... |
| 545 | `break` | Renders a component you choose under every scenario that can reach it on a temporary page and stress tests it. |
| 546 | `break-ai-fix-loops` | "Stop ineffective AI coding repair loops with stable failure fingerprints, a three-attempt budget, real-path proof, negative controls, an... |
| 547 | `break-ui` | "Stress-test a component with realistic worst-case data through a development-only fixture toggle and report verified failures." |
| 548 | `brendangregg-use-tsa` | "Methodical performance troubleshooting and root-cause analysis with Brendan Gregg's USE and TSA methods, plus evidence-backed RCA and po... |
| 549 | `brevo-automation` | "Automate Brevo (formerly Sendinblue) email marketing operations through Composio's Brevo toolkit via Rube MCP." |
| 550 | `broken-authentication` | "Identify and exploit authentication and session management vulnerabilities in web applications. Broken authentication consistently ranks... |
| 551 | `broken-link-finder` | "Broken Link Finder. Use when working with page URL, HTML or a list of links." |
| 552 | `brooks-audit` | "Architecture audit that maps module dependencies, checks layering integrity, and flags structural decay across a codebase, drawing on tw... |
| 553 | `brooks-debt` | "Tech debt assessment that identifies, classifies, and prioritizes maintainability problems — helping teams build a refactoring roadmap —... |
| 554 | `brooks-harness` | "Maintenance orchestrator for the brooks-lint plugin itself." |
| 555 | `brooks-lint` | "AI code reviewer grounded in classic software engineering books for catching design smells, coupling issues, and architectural risks." |
| 556 | `brooks-review` | "PR code review that surfaces decay risks, design smells, and maintainability issues with concrete Symptom → Source → Consequence → Remed... |
| 557 | `brooks-sweep` | "Full-sweep mode: runs a unified analysis across all quality dimensions — code decay, architecture, tech debt, and test quality — then ap... |
| 558 | `brooks-test` | "Review test-suite quality using established testing literature; identify brittleness, mock abuse, unclear fixtures, weak assertions, slo... |
| 559 | `browser-act` | "Use BrowserAct for authenticated browser automation, JS-rendered extraction, screenshots, parallel sessions, verification handling, and ... |
| 560 | `browser-automation` | Build reliable browser checks using observed UI state, semantic locators, bounded waits, isolated test data and explicit outcome verifica... |
| 561 | `browser-bridge` | "Inspect, control, and automate tasks in your real Microsoft Edge or Google Chrome browser via Chrome DevTools Protocol (CDP) with biling... |
| 562 | `browser-extension-builder` | Expert in building browser extensions that solve real problems - Chrome, Firefox, and cross-browser extensions. Covers extension architec... |
| 563 | `browser-extension-launch` | "Builds, tests, packages, and prepares Chrome extensions for store launch from a plain-language idea; use for new extensions, fixes, rele... |
| 564 | `browser-extension-reverse` | "Authorized reverse engineering of Chrome/Firefox extensions: manifest analysis, background workers, content scripts, and extension-based... |
| 565 | `browser-harness` | "Drive an existing browser through CDP for authenticated, visual, or interactive web automation." |
| 566 | `browser-testing-with-devtools` | "Test browser apps with Chrome DevTools MCP by inspecting live DOM, console logs, network traffic, screenshots, accessibility, and perfor... |
| 567 | `buddy-program-manager` | 'Buddy programme register: new hire, assigned buddy, department, start and end dates, check-ins planned and done, and feedback score. Use... |
| 568 | `budget-cash-flow` | 'Budget against actual by department, category and period, with budget and actual amounts, variance, percentage used and linked expenses.... |
| 569 | `bug-bounty` | Complete bug bounty workflow |
| 570 | `bug-hunt-swarm` | "Parallel read-only multi-agent root-cause investigation for bugs, regressions, crashes, flaky behavior, or unexplained failures." |
| 571 | `bug-hunter` | "Systematically finds and fixes bugs using proven debugging techniques. Traces from symptoms to root cause, implements fixes, and prevent... |
| 572 | `bugcrowd-reporting` | Bugcrowd-specific reporting tactics complementing report-writing |
| 573 | `bugs-are-annoying` | Adversarial code auditor that hunts down bugs, logic errors, and security flaws. Use for deep correctness passes, not style reviews. |
| 574 | `build` | "Use when developing a major feature: research the project, create a phased implementation plan, track progress and verify phase outcomes... |
| 575 | `build-design` | Builds UI from a Figma file or a design image so it matches the design, using the project's existing tokens and components. |
| 576 | `build-ui` | "Step-by-step workflow for UI work: read the project, follow the plan for the job (new screen, dashboard, polish, simplify, review), then... |
| 577 | `building-native-ui` | Complete guide for building beautiful apps with Expo Router. Covers fundamentals, styling, components, navigation, animations, patterns, ... |
| 578 | `bulletmind` | "Convert input into clean, structured, hierarchical bullet points for summarization, note-taking, and structured thinking." |
| 579 | `bullmq-specialist` | BullMQ expert for Redis-backed job queues, background processing, and reliable async execution in Node.js/TypeScript applications. |
| 580 | `bumblebee` | "Run Bumblebee supply-chain inventory and exposure scans on macOS/Linux to detect compromised packages, extensions, and MCP host configs." |
| 581 | `bun-development` | "Fast, modern JavaScript/TypeScript development with the Bun runtime, inspired by [oven-sh/bun](https://github.com/oven-sh/bun)." |
| 582 | `burp-suite-testing` | "Execute comprehensive web application security testing using Burp Suite's integrated toolset, including HTTP traffic interception and mo... |
| 583 | `burpsuite-project-parser` | Searches and explores Burp Suite project files (.burp) from the command line. Use when searching response headers or bodies with regex pa... |
| 584 | `busabase` | "Use when managing Busabase workspace records, knowledge, apps, or skills through permission-aware ChangeRequests with auditable history." |
| 585 | `business-analyst` | Master modern business analysis with AI-powered analytics, real-time dashboards, and data-driven insights. Build comprehensive KPI framew... |
| 586 | `business-continuity` | Develop business continuity plans and impact analysis. Implement BCP testing and communication procedures. Use when building organization... |
| 587 | `business-email-template` | 'Business email template register: trigger, sender and recipient type, subject pattern, body structure, personalisation tokens and send c... |
| 588 | `business-website-setup` | 'Website page register: URL, title, meta description, search intent, NAP block, schema type, canonical, indexability and Core Web Vitals ... |
| 589 | `busybox-on-windows` | "How to use a Win32 build of BusyBox to run many of the standard UNIX command line tools on Windows." |
| 590 | `buywhere-product-catalog` | "Use BuyWhere's MCP and API surfaces to add product search, price comparison, and deal discovery to AI shopping agents." |
| 591 | `byagent` | "Publish agent-written Markdown or HTML as a shareable link with the byagent CLI, then read readers' line comments back, edit, republish ... |
| 592 | `c-pro` | "Review and implement C systems code with explicit memory ownership, pointer bounds, error handling, and measured performance." |
| 593 | `c4-architecture-c4-architecture` | "Generate comprehensive C4 architecture documentation for an existing repository/codebase using a bottom-up analysis approach." |
| 594 | `c4-code` | Expert C4 Code-level documentation specialist. Analyzes code directories to create comprehensive C4 code-level documentation including fu... |
| 595 | `c4-component` | Expert C4 Component-level documentation specialist. Synthesizes C4 Code-level documentation into Component-level architecture, defining c... |
| 596 | `c4-container` | Expert C4 Container-level documentation specialist. |
| 597 | `c4-context` | Expert C4 Context-level documentation specialist. Creates high-level system context diagrams, documents personas, user journeys, system f... |
| 598 | `cal-com-automation` | "Automate Cal.com tasks via Rube MCP (Composio): manage bookings, check availability, configure webhooks, and handle teams. Always search... |
| 599 | `calc` | "Spreadsheet creation, format conversion (ODS/XLSX/CSV), formulas, data automation with LibreOffice Calc." |
| 600 | `calendly-automation` | "Automate Calendly scheduling, event management, invitee tracking, availability checks, and organization administration via Rube MCP (Com... |
| 601 | `calibrate-first` | "Measure a dataset's detection floor before reading any trading-signal result, pre-register every test, and report too-small-to-see as UN... |
| 602 | `candidate-talent-pool` | 'Candidate and prospect pool: contact details, experience, skills, consent status and date, referral source and last contact. Use for tal... |
| 603 | `canonical-tag-checker` | "Canonical Tag Checker. Use when working with HTML and page URL, or accessible page URL." |
| 604 | `canonical-url-builder` | "Canonical URL Builder. Use when working with preferred page URL and duplicate URL variants." |
| 605 | `canva-automation` | "Automate Canva tasks via Rube MCP (Composio): designs, exports, folders, brand templates, autofill. Always search tools first for curren... |
| 606 | `canvas-design` | "These are instructions for creating design philosophies - aesthetic movements that are then EXPRESSED VISUALLY. Output only .md files, .... |
| 607 | `capacity-workload-planner` | 'Weekly capacity and workload register: available and allocated hours, utilisation percentage, over-allocation check and leave days. Use ... |
| 608 | `capturekit-mcp` | "Take page screenshots or PDFs, extract page content, metadata and links, or get a page summary through CaptureKit's MCP server. Use when... |
| 609 | `carbonmark-carbon-retirement` | "Price and retire verified carbon credits on Base through Carbonmark's x402 API. Use when a user asks to offset emissions or buy and reti... |
| 610 | `career-ops` | 'Open-source AI job search agent for AI coding CLIs: evaluate offers, scan portals, tailor CVs, track applications, prep interviews. Invo... |
| 611 | `carrier-relationship-management` | Codified expertise for managing carrier portfolios, negotiating freight rates, tracking carrier performance, allocating freight, and main... |
| 612 | `case-review` | "Quality-gate review of a reverse-engineering or assessment case package: scope readiness, Evidence-to-Finding-to-Path traceability, work... |
| 613 | `cc-skill-backend-patterns` | "Backend architecture patterns, API design, database optimization, and server-side best practices for Node.js, Express, and Next.js API r... |
| 614 | `cc-skill-clickhouse-io` | "ClickHouse database patterns, query optimization, analytics, and data engineering best practices for high-performance analytical workloa... |
| 615 | `cc-skill-coding-standards` | "Universal coding standards, best practices, and patterns for TypeScript, JavaScript, React, and Node.js development." |
| 616 | `cc-skill-continuous-learning` | "Turn a completed debugging session or repeated user correction into a small, evidence-backed procedure. Use for explicit requests to cap... |
| 617 | `cc-skill-frontend-patterns` | "Frontend development patterns for React, Next.js, state management, performance optimization, and UI best practices." |
| 618 | `cc-skill-project-guidelines-example` | "Project Guidelines Skill (Example)" |
| 619 | `cc-skill-security-review` | "This skill guides review of security practices and potential vulnerabilities; no checklist ensures all code is secure. Use when implemen... |
| 620 | `cc-skill-strategic-compact` | "Prepare a verified checkpoint before condensing an agent conversation at a phase boundary. Use during long tasks when context is repetit... |
| 621 | `cdk-patterns` | "Common AWS CDK patterns and constructs for building cloud infrastructure with TypeScript, Python, or Java. Use when designing reusable C... |
| 622 | `cdn-setup` | Configure CDNs for content delivery. Set up CloudFront, Cloudflare, and Fastly. Use when optimizing global content delivery. |
| 623 | `change-management` | Implement change management processes. Configure CAB reviews, change windows, and rollback procedures. Use when managing production changes. |
| 624 | `changelog-automation` | "Automate changelog generation from commits, PRs, and releases following Keep a Changelog format. Use when setting up release workflows, ... |
| 625 | `changelog-entry` | Generate a properly formatted CHANGELOG.md entry in Keep a Changelog format from a commit range or PR. Groups changes into Added/Changed/... |
| 626 | `changelog-updates` | "Create release notes and product updates that developers actually read and care about. This skill covers changelog formatting, versionin... |
| 627 | `chartquery-mcp` | "Render Chart.js charts, Mermaid and other diagrams, QR codes, barcodes and thermal printer labels (ZPL, TSC, EPL) as images through Char... |
| 628 | `chat-widget` | Build a real-time support chat system with a floating widget for users and an admin dashboard for support staff. Use when the user wants ... |
| 629 | `chatexport-need-miner` | "Mines offline Telegram Desktop chat exports (result.json) for unmet market needs and product opportunities using chunked streaming and v... |
| 630 | `chatgpt-plugin` | 'Before building, submitting or changing a ChatGPT plugin or Apps SDK app: get it through OpenAI''s directory review (auth, package, OAut... |
| 631 | `check-identity-pack` | Run an AFP 100-point or AUSTRAC safe-harbour identity check over a set of documents, and report exactly what's missing. Use when the user... |
| 632 | `chord-onchain-trading` | "Read DEX market data and prepare best-route swap quotes and unsigned swap transactions on eight EVM chains with the Chord API. Never sig... |
| 633 | `choreograph` | Coordinate several elements that animate together — decide what moves, in what order, how much they overlap, and what stays still — so a ... |
| 634 | `chrome-extension-developer` | "Expert in building Chrome Extensions using Manifest V3. Covers background scripts, service workers, content scripts, and cross-context c... |
| 635 | `churn-prevention` | "Reduce voluntary and involuntary churn with cancel flows, save offers, dunning, win-back tactics, and retention strategy. Use when users... |
| 636 | `ci-cd-and-automation` | Automates CI/CD pipeline setup. Use when setting up or modifying build and deployment pipelines. Use when you need to automate quality ga... |
| 637 | `cicd-automation-workflow-automate` | "You are a workflow automation expert specializing in creating efficient CI/CD pipelines, GitHub Actions workflows, and automated develop... |
| 638 | `cinematic-ui-ux` | Build high-performance cinematic web experiences with GSAP 3.12+, Lenis smooth scroll, canvas frame scrubbing, kinetic typography, and WC... |
| 639 | `circleci` | Configure CircleCI workflows and orbs for continuous integration and deployment. |
| 640 | `circleci-automation` | "Automate CircleCI tasks via Rube MCP (Composio): trigger pipelines, monitor workflows/jobs, retrieve artifacts and test metadata. Always... |
| 641 | `cirq` | "Cirq is Google Quantum AI's open-source framework for designing, simulating, and running quantum circuits on quantum computers and simul... |
| 642 | `cis-benchmarks` | Audit and remediate CIS benchmark violations. |
| 643 | `citation-management` | "Manage citations systematically throughout the research and writing process." |
| 644 | `ckw-design` | "Frontend design entry point: direction, design system, visual philosophy. Use whenever building or touching the look of any web UI (comp... |
| 645 | `claimable-postgres` | "Provision instant temporary Postgres databases via Claimable Postgres by Neon (neon.new) with no login, signup, or credit card. Supports... |
| 646 | `clarity-gate` | Pre-ingestion verification for epistemic quality in RAG systems. Ensures documents are properly qualified before entering knowledge bases... |
| 647 | `clarvia-aeo-check` | "Score any MCP server, API, or CLI for agent-readiness using Clarvia AEO (Agent Experience Optimization). Use current provider evidence a... |
| 648 | `claude-agents` | '''Ask Claude'', ''have Claude build or review this'': drive Claude Code headless (claude -p) from another agent as a peer, builder or fr... |
| 649 | `claude-ally-health` | "A health assistant skill for medical information analysis, symptom tracking, and wellness guidance." |
| 650 | `claude-api` | "Build apps with the Claude API or Anthropic SDK. TRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`/`claude_agent_sdk`, or user ... |
| 651 | `claude-code-expert` | "Especialista profundo em Claude Code - CLI da Anthropic. Maximiza produtividade com atalhos, hooks, MCPs, configuracoes avancadas, workf... |
| 652 | `claude-code-guide` | "To provide a comprehensive reference for configuring and using Claude Code (the agentic coding tool) to its full potential. This skill s... |
| 653 | `claude-d3js-skill` | "This skill provides guidance for creating sophisticated, interactive data visualisations using d3.js." |
| 654 | `claude-delegate` | Delegate coding tasks to a separate Claude Code CLI process or Claude session only when the user explicitly requests it, while the orches... |
| 655 | `claude-in-chrome-troubleshooting` | Diagnose and fix Claude in Chrome MCP extension connectivity issues. Use when mcp__claude-in-chrome__* tools fail, return "Browser extens... |
| 656 | `claude-monitor` | Monitor de performance do Claude Code e sistema local. Diagnostica lentidao, mede CPU/RAM/disco, verifica API latency e gera relatorios d... |
| 657 | `claude-scientific-skills` | "Scientific research and analysis skills" |
| 658 | `claude-settings-audit` | Analyze a repository to generate recommended Claude Code settings.json permissions. Use when setting up a new project, auditing existing ... |
| 659 | `claude-speed-reader` | "-Speed read Claude's responses at 600+ WPM using RSVP with Spritz-style ORP highlighting" |
| 660 | `claude-win11-speckit-update-skill` | "Review updates to GitHub SpecKit on Windows 11 with PowerShell, preserving local templates and customizations" |
| 661 | `clean-code` | "This skill embodies the principles of \"Clean Code\" by Robert C. Martin (Uncle Bob). Use it to transform \"code that works\" into \"cod... |
| 662 | `clean-code-guard` | "Review generated or changed production code with Clean Code, SOLID, DRY, KISS, YAGNI, and LLM-specific failure-mode checks." |
| 663 | `clerk-auth` | Expert patterns for Clerk auth implementation, middleware, organizations, webhooks, and user sync |
| 664 | `clerk-production` | 'Setting up or changing Clerk sign-in, organizations, roles or billing on Next.js, or sign-in that does nothing or lands wrong: Clerk in ... |
| 665 | `clickup-automation` | "Automate ClickUp project management including tasks, spaces, folders, lists, comments, and team operations via Rube MCP (Composio). Alwa... |
| 666 | `client-secret-exposure-audit` | "Audit a deployed web app for secrets exposed to the browser: hardcoded API keys/tokens in JS, secrets in HTML meta/attributes/comments, ... |
| 667 | `clients-accounts` | 'Client and account register: contacts, billing address, tax ID and basis, payment terms, invoice totals, amounts paid and outstanding ba... |
| 668 | `cline-delegate` | Delegate coding tasks to the Cline CLI (`cline`) only when the user explicitly requests it, while the orchestrator retains review and lan... |
| 669 | `cline-pilot` | Proxy Cline CLI coding tasks: dispatch, monitor background runs via hard evidence, relay decision points in a fixed format, verify agains... |
| 670 | `cloro-mcp` | "Get Google and Bing results with the AI Overview, and ChatGPT, Google AI Mode, Bing AI Mode and Gemini answers with their cited sources,... |
| 671 | `close-automation` | "Automate Close CRM tasks via Rube MCP (Composio): create leads, manage calls/SMS, handle tasks, and track notes. Always search tools fir... |
| 672 | `closed-loop-delivery` | Use when a coding task must be completed against explicit acceptance criteria with minimal user re-intervention across implementation, re... |
| 673 | `cloud-architect` | Expert cloud architect specializing in AWS/Azure/GCP multi-cloud infrastructure design, advanced IaC (Terraform/OpenTofu/CDK), FinOps cos... |
| 674 | `cloud-devops` | "Cloud infrastructure and DevOps workflow covering AWS, Azure, GCP, Kubernetes, Terraform, CI/CD, monitoring, and cloud-native development." |
| 675 | `cloud-iam-deep` | Cloud IAM red-team attack chain across AWS, Azure, GCP |
| 676 | `cloud-k8s` | "Authorized cloud, container, and Kubernetes security assessment: metadata SSRF, IAM misconfiguration, container escape paths, and cluste... |
| 677 | `cloud-penetration-testing` | "Conduct comprehensive security assessments of cloud infrastructure across Microsoft Azure, Amazon Web Services (AWS), and Google Cloud P... |
| 678 | `cloudflare-pages` | Deploy static sites and full-stack apps on Cloudflare Pages with previews, functions, and custom domains. |
| 679 | `cloudflare-r2` | Manage Cloudflare R2 buckets, lifecycle, and signed URLs. Use for low-egress object storage and media delivery. |
| 680 | `cloudflare-security-audit` | "Audit authorized codebases for exploitable vulnerabilities using scoped reconnaissance, adversarial review, validation, and structured r... |
| 681 | `cloudflare-workers` | Build and deploy edge functions with Cloudflare Workers and Wrangler. Use for APIs, cron jobs, and edge middleware. |
| 682 | `cloudflare-workers-expert` | "Expert in Cloudflare Workers and the Edge Computing ecosystem. Covers Wrangler, KV, D1, Durable Objects, and R2 storage." |
| 683 | `cloudflare-zero-trust` | Protect internal apps with Cloudflare Access, device posture, and Zero Trust policies. |
| 684 | `cloudformation` | Deploy AWS resources with CloudFormation templates. Create stacks, use nested stacks, and implement drift detection. Use when deploying A... |
| 685 | `cloudformation-best-practices` | "CloudFormation template optimization, nested stacks, drift detection, and production-ready patterns. Use when writing or reviewing CF te... |
| 686 | `cloudish` | "Deploy a Dockerfile, source folder, or existing image to Cloudish as a running container at a live URL, built server-side with no local ... |
| 687 | `cmux` | "Control cmux workspaces, panes, surfaces, and agent sessions safely from macOS terminal workflows." |
| 688 | `co-marketing` | "When the user wants to find co-marketing partners, plan joint campaigns, or brainstorm partnership opportunities." |
| 689 | `cockney` | "Cheeky Cockney coding mode: terse replies, the smallest correct change, plain English for anything risky." |
| 690 | `coda-automation` | "Automate Coda tasks via Rube MCP (Composio): manage docs, pages, tables, rows, formulas, permissions, and publishing. Always search tool... |
| 691 | `code-audit` | "Authorized source-code security review and SAST workflows: Semgrep and CodeQL pattern hunting, dangerous API identification, and fix ver... |
| 692 | `code-documentation-code-explain` | "You are a code education expert specializing in explaining complex code through clear narratives, visual diagrams, and step-by-step brea... |
| 693 | `code-documentation-doc-generate` | "Compatibility alias of documentation-generation-doc-generate. Generate scoped documentation from verified source while preserving existi... |
| 694 | `code-of-conduct` | 'Build a human-reviewed conduct register after context-first intake. Use when an SME needs policy acknowledgements, complaint handling, a... |
| 695 | `code-polish` | Rewrites unprofessional code comments into clear ones and performs non-semantic cleanup. Use to professionalize code without altering log... |
| 696 | `code-refactoring-context-restore` | "Resume interrupted project work from a handoff and current checkout evidence; reconcile completed work, pending changes and existing use... |
| 697 | `code-refactoring-refactor-clean` | "You are a code refactoring expert specializing in clean code principles, SOLID design patterns, and modern software engineering best pra... |
| 698 | `code-refactoring-tech-debt` | "Identify technical debt from actual code and change history, estimate its impact, and prioritize bounded improvements with explicit assu... |
| 699 | `code-review` | '''Review this'', ''find bugs'', ''is this fix safe'': review code for defects that matter, correctness first, each finding refuted befor... |
| 700 | `code-review-ai-ai-review` | "Review pull requests with source inspection, available static analysis and evidence-backed AI assistance; report actionable bugs, securi... |
| 701 | `code-review-and-quality` | Conducts multi-axis code review. Use before merging any change. Use when reviewing code written by yourself, another agent, or a human. U... |
| 702 | `code-review-checklist` | "Comprehensive checklist for conducting thorough code reviews covering functionality, security, performance, and maintainability" |
| 703 | `code-review-excellence` | "Review a defined code diff for correctness, security, performance and maintainability; report evidence-backed findings with severity and... |
| 704 | `code-review-sensei` | Expert code reviewer that catches bugs, security issues, performance problems, and design flaws with actionable fix suggestions. |
| 705 | `code-reviewer` | "Elite code review expert specializing in modern AI-powered code" |
| 706 | `code-showcase-core-components` | "Apply the ChrisWiles code-showcase component and token conventions when the target project actually uses that API; examples require loca... |
| 707 | `code-showcase-react-ui-patterns` | Modern React UI patterns for loading states, error handling, and data fetching. Use when building UI components, handling async data, or ... |
| 708 | `code-showcase-systematic-debugging` | Four-phase debugging methodology with root cause analysis. Use when investigating bugs, fixing test failures, or troubleshooting unexpect... |
| 709 | `code-showcase-testing-patterns` | Jest testing patterns, factory functions, mocking strategies, and TDD workflow. Use when writing unit tests, creating test factories, or ... |
| 710 | `code-simplification` | Simplifies code for clarity. Use when refactoring code for clarity without changing behavior. Use when code works but is harder to read, ... |
| 711 | `code-simplifier` | Simplifies and refines code for clarity, consistency, and maintainability while preserving all functionality. Use when asked to "simplify... |
| 712 | `codebase-audit-pre-push` | "Deep audit before GitHub push: removes junk files, dead code, security holes, and optimization issues. Checks every file line-by-line fo... |
| 713 | `codebase-aware-ui-prompts` | Transform product requirements into precise, architecture-preserving UI implementation prompts for Cursor, Claude Code, v0, Lovable, and ... |
| 714 | `codebase-cleanup-deps-audit` | "You are a dependency security expert specializing in vulnerability scanning, license compliance, and supply chain security. Analyze proj... |
| 715 | `codebase-cleanup-refactor-clean` | "You are a code refactoring expert specializing in clean code principles, SOLID design patterns, and modern software engineering best pra... |
| 716 | `codebase-cleanup-tech-debt` | "Identify technical debt from actual code and change history, estimate its impact, and prioritize bounded improvements with explicit assu... |
| 717 | `codebase-design` | Shared vocabulary for designing deep modules. Use when the user wants to design or improve a module's interface, find deepening opportuni... |
| 718 | `codebase-onboarding` | Onboard a developer to a repository using Ontoly graph summaries. Use when asked to explain a new codebase, identify entrypoints, map pac... |
| 719 | `codebase-to-wordpress-converter` | "Expert skill for converting any codebase (React/HTML/Next.js) into a pixel-perfect, SEO-optimized, and dynamic WordPress theme." |
| 720 | `codex-agents` | '''Ask Codex'', ''check with Codex'', handing Codex a build or review, or stuck between two framings: the Codex CLI as peer, builder or f... |
| 721 | `codex-delegate` | Delegate coding tasks to the OpenAI Codex CLI only when the user explicitly requests it, while the orchestrator retains review and landin... |
| 722 | `codex-fable5` | "Apply Fable-inspired discipline to Codex work: inspect first, track goals and findings, ground conclusions in evidence, verify before co... |
| 723 | `codex-profiles` | "Use codex-profiles to run Codex CLI or Codex Desktop with isolated CODEX_HOME profiles for separate accounts, projects, and local state." |
| 724 | `codex-review` | "Professional code review with auto CHANGELOG generation, integrated with Codex AI. Use when you want professional code review before com... |
| 725 | `codex-subagent` | "Launch Codex CLI as an isolated subagent for bounded coding, review, or verification tasks." |
| 726 | `cohesivity` | "Provision headless backend services for AI agents through Cohesivity: hosting, databases, storage, LLMs, and third-party APIs over one H... |
| 727 | `colab-operator` | Operate Google Colab environments via the `colab` CLI. Use when asked to create or manage GPU/TPU sessions, run Python/shell on a remote ... |
| 728 | `cold-email` | "Write B2B cold emails and follow-up sequences that earn replies. Use when creating outbound prospecting emails, SDR outreach, personaliz... |
| 729 | `comfyui-gateway` | REST API gateway for ComfyUI servers. Workflow management, job queuing, webhooks, caching, auth, rate limiting, and image delivery (URL +... |
| 730 | `commandcode-delegate` | Delegate coding tasks to the Command Code CLI (`cmd`) only when the user explicitly requests it, while the orchestrator retains review an... |
| 731 | `comment-to-dm-cta` | "Plan the \"Comment KEYWORD\" CTA of an Instagram Reel (keyword, overlay, caption, DM copy), then, after explicit user confirmation, set ... |
| 732 | `commit` | "Prepare or create commits using Sentry-style message conventions when the repository requests them; inspect staged scope and honor its p... |
| 733 | `community-building` | "When the user wants to build, grow, or improve a developer community on Discord, Slack, or forums." |
| 734 | `company-email-accounts` | 'Mailbox and licence register: employee, account type, aliases, groups, tool, licence cost, 2FA and password policy state, and access-rev... |
| 735 | `competency-matrix` | 'Competency matrix of expected proficiency by job title and grade, with assessment method and linked skill area. Use for role frameworks ... |
| 736 | `competitive-landscape` | "Comprehensive frameworks for analyzing competition, identifying differentiation opportunities, and developing winning market positioning... |
| 737 | `competitor-ad-intelligence` | "Research public competitor ads, analyze creative patterns and landing pages, and produce an evidence-labeled strategic teardown." |
| 738 | `competitor-alternatives` | "You are an expert in creating competitor comparison and alternative pages. Your goal is to build pages that rank for competitive search ... |
| 739 | `competitor-analysis` | "Research competitors with Browserbase discovery, enrichment lanes, screenshots, matrices, and HTML reports." |
| 740 | `competitor-backlink-idea-generator` | "Competitor Backlink Idea Generator. Use when working with your niche and competitor backlink examples or export." |
| 741 | `competitor-gap-analyzer` | "Competitor Gap Analyzer. Use when working with your offering and at least one competitor profile." |
| 742 | `competitor-keyword-overlap-checker` | "Competitor Keyword Overlap Checker. Use when working with two labeled keyword sets." |
| 743 | `competitor-profiling` | "When the user wants to research, profile, or analyze competitors from their URLs." |
| 744 | `competitor-summary-report-creator` | "Competitor Summary Report Creator. Use when working with competitor names or URLs and evidence to summarize." |
| 745 | `competitor-tracking` | "Systematic competitor analysis for developer tools. Track features, pricing, positioning, content strategy, and community sentiment for ... |
| 746 | `compile-knowledge` | "Compile durable, non-obvious findings into an interlinked markdown knowledge store — atomic files, [[wiki-links]], a maintained index — ... |
| 747 | `complexity-cuts` | "Lower Big-O on existing code via a one-transformation-at-a-time playbook with verify-revert-stop. For new code use lemmaly; for math-lev... |
| 748 | `composition-patterns` | "Use when working with composition-patterns tasks or workflows" |
| 749 | `comprehensive-review-full-review` | "Use when working with comprehensive review full review" |
| 750 | `comprehensive-review-pr-enhance` | Generate structured PR descriptions from diffs, add review checklists, risk assessments, and test coverage summaries. Use when the user s... |
| 751 | `computer-use-agents` | Build AI agents that interact with computers like humans do - viewing screens, moving cursors, clicking buttons, and typing text. Covers ... |
| 752 | `computer-vision-expert` | "Computer vision pipeline design and evaluation. Specialized in YOLO26, Segment Anything 3 (SAM 3), Vision Language Models, and real-time... |
| 753 | `concise-planning` | "Use when a user asks for a plan for a coding task, to generate a clear, actionable, and atomic checklist." |
| 754 | `conductor-implement` | "Execute tasks from a track's implementation plan following TDD workflow" |
| 755 | `conductor-manage` | "Manage track lifecycle: archive, restore, delete, rename, and cleanup" |
| 756 | `conductor-new-track` | "Create a new track with specification and phased implementation plan" |
| 757 | `conductor-revert` | "Git-aware undo by logical work unit (track, phase, or task)" |
| 758 | `conductor-setup` | Configure a Rails project to work with Conductor (parallel coding agents) |
| 759 | `conductor-status` | "Display project status, active tracks, and next actions" |
| 760 | `conductor-validator` | 'Validates Conductor project artifacts for completeness, consistency, and correctness. Use after setup, when diagnosing issues, or before... |
| 761 | `confluence-automation` | "Automate Confluence page creation, content search, space management, labels, and hierarchy navigation via Rube MCP (Composio). Always se... |
| 762 | `connection-auth-rules` | Build a Connection Auth Rules for a Monte Carlo connection type. Fetches live connector schemas and transform steps from the apollo-agent... |
| 763 | `constant-time-analysis` | "Analyze cryptographic code to detect operations that leak secret data through execution timing variations." |
| 764 | `constraint-driven-development` | 'Write the project quality bar as enforced CONSTRAINTS.md so agents stop quietly lowering it: coverage, performance, accessibility thresh... |
| 765 | `container-hardening` | Secure Docker images and container runtime configurations. |
| 766 | `container-registries` | Manage container registries including ECR, ACR, GCR, and Docker Hub. |
| 767 | `container-scanning` | Scan container images for vulnerabilities using Trivy, Grype, and cloud-native tools. |
| 768 | `container-security-hardening` | Harden Docker/container images and runtime deployments with secure base images, non-root users, CVE scanning, SBOM/signing, seccomp/AppAr... |
| 769 | `content-coverage` | Turn verified AI-search citation gaps into a deduplicated content plan and review-ready drafts through AI SEO Tracker or existing reports. |
| 770 | `content-creator` | "Draft and review audience-specific content using supplied brand examples, local text diagnostics, and adaptable channel templates." |
| 771 | `content-freshness-checker` | "Content Freshness Checker. Use when working with content and known publication or update date if available." |
| 772 | `content-gap-finder` | "Content Gap Finder. Use when working with existing content inventory and audience goal." |
| 773 | `content-length-comparator` | "Content Length Comparator. Use when working with two or more labeled text samples." |
| 774 | `content-marketer` | Elite content marketing strategist specializing in AI-powered content creation, omnichannel distribution, SEO optimization, and data-driv... |
| 775 | `content-strategy` | "Plan a content strategy, topic clusters, editorial roadmap, and content mix for traffic, authority, and lead generation. Use when decidi... |
| 776 | `context-agent` | Agente de contexto para continuidade entre sessoes. Salva resumos, decisoes, tarefas pendentes e carrega briefing automatico na sessao se... |
| 777 | `context-compression` | "When agent sessions generate millions of tokens of conversation history, compression becomes mandatory. The naive approach is aggressive... |
| 778 | `context-degradation` | "Language models exhibit predictable degradation patterns as context length increases. Understanding these patterns is essential for diag... |
| 779 | `context-driven-development` | "Guide for implementing and maintaining context as a managed artifact alongside code, enabling consistent AI interactions and team alignm... |
| 780 | `context-engineering` | Optimizes agent context setup. Use when starting a new session, when agent output quality degrades, when switching between tasks, or when... |
| 781 | `context-fundamentals` | "Context is the complete state available to a language model at inference time. It includes everything the model can attend to when gener... |
| 782 | `context-guardian` | Guardiao de contexto que preserva dados criticos antes da compactacao automatica. Snapshots, verificacao de integridade e reducao de perd... |
| 783 | `context-kit` | "Evaluate, adapt, and safely install Context Kit personal context artifacts for Claude Code or adjacent agent workflows." |
| 784 | `context-management-context-restore` | "Resume interrupted project work from a handoff and current checkout evidence; reconcile completed work, pending changes and existing use... |
| 785 | `context-management-context-save` | "Use when working with context management context save" |
| 786 | `context-manager` | Elite AI context engineering specialist mastering dynamic context management, vector databases, knowledge graphs, and intelligent memory ... |
| 787 | `context-optimization` | "Context optimization extends the effective capacity of limited context windows through strategic compression, masking, caching, and part... |
| 788 | `context-window-management` | Strategies for managing LLM context windows including summarization, trimming, routing, and avoiding context rot |
| 789 | `context7-auto-research` | "Automatically fetch latest library/framework documentation for Claude Code via Context7 API. Use when you need up-to-date documentation ... |
| 790 | `contract-document-renewal` | 'Contract register: counterparty, owner, start and end dates, auto-renewal flag, renewal notice deadline, value and tax basis. Use for re... |
| 791 | `conversation-memory` | Persistent memory systems for LLM conversations including short-term, long-term, and entity-based memory |
| 792 | `convertkit-automation` | "Automate ConvertKit (Kit) tasks via Rube MCP (Composio): manage subscribers, tags, broadcasts, and broadcast stats. Always search tools ... |
| 793 | `convex` | "Convex reactive backend expert: schema design, TypeScript functions, real-time subscriptions, auth, file storage, scheduling, and deploy... |
| 794 | `convex-backend` | Build reactive backends with Convex functions, schema validation, auth integration, and deployment workflows. Use when building real-time... |
| 795 | `cooper-email` | "Give an AI agent its own email inbox with Cooper Email: send, receive, reply, and wait for replies or verification codes over MCP or HTTP." |
| 796 | `copilot-delegate` | Delegate coding tasks to the GitHub Copilot CLI (`copilot`) only when the user explicitly requests it, while the orchestrator retains rev... |
| 797 | `copilot-sdk` | "Build applications that programmatically interact with GitHub Copilot. The SDK wraps the Copilot CLI via JSON-RPC, providing session man... |
| 798 | `copy-editing` | "You are an expert copy editor specializing in marketing and conversion copy. Your goal is to systematically improve existing copy throug... |
| 799 | `copywriting` | Write rigorous, conversion-focused marketing copy for landing pages and emails. Enforces brief confirmation and strict no-fabrication rules. |
| 800 | `copywriting-psychologist` | "Write or revise conversion copy using audience awareness, motivations, and credible proof when ads, landing pages, or sales messages fee... |
| 801 | `core-components` | "Adapt an existing project component library and design tokens to a UI change; inspect real exports, preserve native behavior, and verify... |
| 802 | `cost-optimization` | "Strategies and patterns for optimizing cloud costs across AWS, Azure, and GCP." |
| 803 | `council-verdicts` | "Starter: interpret a council run's verdict artifacts — quorum, dissent, cross-lab validity, and what to do next" |
| 804 | `coupler-marketing-analytics` | "Analyze cross-channel marketing performance from live Coupler.io data through its hosted MCP server: channel and campaign comparison, RO... |
| 805 | `course-upskilling-requests` | 'Training request register: course, provider, cost, duration, budget line, the three approval steps, service bond and completion evidence... |
| 806 | `court` | "Put an idea on trial: a prosecutor and a defense Claude argue, 12 juror sub-agents vote independently, and a judge reads the verdict and... |
| 807 | `cowork-to-code-bridge` | "Use an already-installed, independently verified cowork-to-code bridge to run narrowly approved actions on the user's own macOS, Linux, ... |
| 808 | `cpp-pro` | Write idiomatic C++ code with modern features, RAII, smart pointers, and STL algorithms. Handles templates, move semantics, and performan... |
| 809 | `cqrs-implementation` | "Implement Command Query Responsibility Segregation for scalable architectures. Use when separating read and write models, optimizing que... |
| 810 | `create-branch` | Create a git branch following Sentry naming conventions. Use when asked to "create a branch", "new branch", "start a branch", "make a bra... |
| 811 | `create-issue-gate` | Use when starting a new implementation task and an issue must be created with strict acceptance criteria gating before execution. |
| 812 | `create-pr` | Alias for pr-writer. Use when users explicitly ask for "create-pr" or reference the legacy skill name. Redirects to the canonical PR writ... |
| 813 | `creative-psychology-hooks` | "Generate and grade ad hooks, angles and video openers with a creative psychology framework when paid social ideas need a clear mechanism... |
| 814 | `cred-omega` | "CISO operacional enterprise para gestao total de credenciais e segredos." |
| 815 | `credit-cycle-analysis` | 'Debtor and creditor credit-cycle analysis: weighted collection or payment days, ageing buckets, credit limit utilisation and gap against... |
| 816 | `crewai` | Design role-based agents, tasks, crews, and flows with CrewAI. |
| 817 | `cro` | "When the user wants to optimize, improve, or increase conversions on any marketing page or form — including homepage, landing pages, pri... |
| 818 | `cron-doctor` | "Diagnose and validate cron expressions before they ship. Catches the five silent death-traps: impossible dates that never fire, OR-seman... |
| 819 | `cross-chain-relayer-audit` | 'Cross-chain relayer bridge audit register: message hash verifications, replay protection nonces, validator quorum, and withdrawal proofs.' |
| 820 | `cross-platform-contract-propagation-audit` | "Use when auditing whether a field, enum, flag, or API contract propagates consistently across storage, services, clients, analytics, and... |
| 821 | `crossframe` | "Use when the user explicitly invokes CrossFrame or 跨尺度结构诊断 for Chinese-canonical structural diagnosis of complex relationships, organiza... |
| 822 | `crossframe-casebook` | "Use when CrossFrame Suite routes explicit Chinese casebook work: turning materials into reusable cases, anonymized entries, mechanisms, ... |
| 823 | `crossframe-critical` | "Use only when the user explicitly names crossframe-critical for a Chinese structural critique dossier, article plan, or long-form critic... |
| 824 | `crossframe-debate` | "Use when CrossFrame Suite routes explicit Chinese proposition testing, debate analysis, hidden-premise review, rebuttal design, or withd... |
| 825 | `crossframe-dialogue` | "Use when CrossFrame Suite routes explicit Chinese reader replies, editor responses, consultation-style short answers, or boundary-aware ... |
| 826 | `crossframe-essay` | "Use when explicit CrossFrame work needs a Chinese critical insight essay, commentary, concept essay, public piece, or structure-to-artic... |
| 827 | `crossframe-notebook` | "Use when CrossFrame Suite routes explicit Chinese notes for books, theories, articles, excerpts, bidirectional reading, absorption, or c... |
| 828 | `crossframe-org` | "Use when CrossFrame Suite routes explicit Chinese analysis of teams, projects, organizations, responsibility chains, feedback write-back... |
| 829 | `crossframe-public` | "Use when CrossFrame Suite routes explicit Chinese analysis of public issues, platform governance, policy, institutional responsibility, ... |
| 830 | `crossframe-review` | "Use when explicit CrossFrame output needs review for reasoning fidelity, evidence boundaries, source anchors, concept drift, article col... |
| 831 | `crossframe-suite` | "Use when the user explicitly invokes CrossFrame Suite for Chinese structural diagnosis workflows across relationships, organizations, pu... |
| 832 | `crossframe-teach` | "Use when CrossFrame Suite routes explicit Chinese teaching of CrossFrame concepts, misreading boundaries, plain-language examples, signa... |
| 833 | `crypto-bd-agent` | "Reference patterns (upstream reports, not independently verified here) for building AI agents that autonomously discover, evaluate, and ... |
| 834 | `csharp-pro` | Write modern C# code with advanced features like records, pattern matching, and async/await. Use for version-compatible .NET implementati... |
| 835 | `csv-manual-export` | 'CSV Manual Export: a UTF-8 CSV template from a confirmed field list, empty by default, with no invented columns or values. Use for an im... |
| 836 | `ctr-predictor` | "CTR Predictor. Use when working with impressions and an explicitly supplied CTR assumption or historical benchmark." |
| 837 | `cucumber-skill` | "Generates Cucumber BDD tests with Gherkin feature files and step definitions in Java, JavaScript, or Ruby. Use when user mentions \"Cucu... |
| 838 | `culture-retention` | 'Employee survey and retention register: engagement, growth, happiness, work-life balance and manager-relationship scores, key concern an... |
| 839 | `curlshot` | "Capture web page screenshots, PDFs and scrolling videos, or render HTML/Markdown to images, with the hosted CurlShot API." |
| 840 | `cursor-delegate` | Delegate coding tasks to the Cursor Agent CLI (`cursor-agent`) only when the user explicitly requests it, while the orchestrator retains ... |
| 841 | `customer-journey` | Map five customer awareness stages to realistic search queries, answer-engine prompts and content decisions. |
| 842 | `customer-psychographic-profiler` | "Build an evidence-grounded customer profile of motivations, fears, identity, and trust barriers before positioning, copywriting, or funn... |
| 843 | `customer-research` | "When the user wants to conduct, analyze, or synthesize customer research." |
| 844 | `customer-support` | Elite AI-powered customer support specialist mastering conversational AI, automated ticketing, sentiment analysis, and omnichannel suppor... |
| 845 | `customs-trade-compliance` | Codified expertise for customs documentation, tariff classification, duty optimisation, restricted party screening, and regulatory compli... |
| 846 | `cv-generator` | "Generate professional, ATS-optimized CVs for FlowCV, Canva, Google Docs, or Word. Handles multi-source merging, JD targeting, seniority ... |
| 847 | `cyber-audit` | "Run read-only exposure checks for security advisories and write a structured local audit report." |
| 848 | `cypress-skill` | "Generates production-grade Cypress E2E and component tests in JavaScript or TypeScript. Supports local execution and TestMu AI cloud. Us... |
| 849 | `daily` | Documentation and capabilities reference for Daily |
| 850 | `daily-gift` | "Relationship-aware daily gift engine with five-stage creative pipeline — editorial judgment, synthesis, concept generation, visual strat... |
| 851 | `daily-news-report` | "Scrapes content based on a preset URL list, filters high-quality technical information, and generates daily Markdown reports." |
| 852 | `dali-short-address-commissioner` | "Commissions DALI and DALI-2 (IEC 62386) lighting buses: short-address assignment (0-63), 24-bit binary search collision resolution, grou... |
| 853 | `darkmoon-pentest` | "Start, follow and triage authorized autonomous AI pentest runs on a self-hosted Darkmoon Pro instance through its MCP server." |
| 854 | `darpa-audit` | "Stress-test a startup or product idea against the Heilmeier Catechism before you build: 5 forcing prompts, assumption labels, and a SURV... |
| 855 | `dast-scanning` | Perform dynamic application security testing with OWASP ZAP, Burp Suite, and Nikto. |
| 856 | `data-engineer` | Build scalable data pipelines, modern data warehouses, and real-time streaming architectures. Implements Apache Spark, dbt, Airflow, and ... |
| 857 | `data-engineering-data-driven-feature` | "Build features guided by data insights, A/B testing, and continuous measurement using specialized agents for analysis, implementation, a... |
| 858 | `data-engineering-data-pipeline` | "You are a data pipeline architecture expert specializing in scalable, reliable, and cost-effective data pipelines for batch and streamin... |
| 859 | `data-export-engine` | 'Data export log: source module, purpose, format, requester and approver, delivery dates, personal-data flag and status. Use for export a... |
| 860 | `data-privacy-controls` | 'Data privacy control register: data category, lawful basis, retention period, access roles, encryption and consent requirement per modul... |
| 861 | `data-quality-frameworks` | "Implement data quality validation with Great Expectations, dbt tests, and data contracts. Use when building data quality pipelines, impl... |
| 862 | `data-scientist` | Expert data scientist for advanced analytics, machine learning, and statistical modeling. Handles complex data analysis, predictive model... |
| 863 | `data-storytelling` | "Transform raw data into compelling narratives that drive decisions and inspire action." |
| 864 | `data-structure-protocol` | "Give agents persistent structural memory of a codebase — navigate dependencies, track public APIs, and understand why connections exist ... |
| 865 | `database` | "Database development and operations workflow covering SQL, NoSQL, database design, migrations, optimization, and data engineering." |
| 866 | `database-admin` | Expert database administrator specializing in modern cloud databases, automation, and reliability engineering. |
| 867 | `database-architect` | Expert database architect specializing in data layer design from scratch, technology selection, schema modeling, and scalable database ar... |
| 868 | `database-backups` | Implement database backup strategies. Configure automated backups, retention, and recovery testing. Use when designing backup and recover... |
| 869 | `database-cloud-optimization-cost-optimize` | "You are a cloud cost optimization expert specializing in reducing infrastructure expenses while maintaining performance and reliability.... |
| 870 | `database-design` | "Database design principles and decision-making. Schema design, indexing strategy, ORM selection, serverless databases." |
| 871 | `database-migration` | "Master database schema and data migrations across ORMs (Sequelize, TypeORM, Prisma), including rollback strategies and zero-downtime dep... |
| 872 | `database-migrations-migration-observability` | "Migration monitoring, CDC, and observability infrastructure" |
| 873 | `database-migrations-sql-migrations` | "SQL database migrations with zero-downtime strategies for PostgreSQL, MySQL, and SQL Server. Focus on data integrity and rollback plans." |
| 874 | `database-optimizer` | Expert database optimizer specializing in modern performance tuning, query optimization, and scalable architectures. |
| 875 | `database-security` | "Authorized database security assessment across PostgreSQL, MySQL, MSSQL, MongoDB, and Redis: exposure, authorization gaps, UDF/command e... |
| 876 | `datacircle` | "Every plan of every GTM API on datacircle.dev, as one file you download and query. Use the file to compare or price a GTM API." |
| 877 | `datadog` | Implement Datadog monitoring and APM for infrastructure and applications. |
| 878 | `datadog-automation` | "Automate Datadog tasks via Rube MCP (Composio): query metrics, search logs, manage monitors/dashboards, create events and downtimes. Alw... |
| 879 | `dataforseo-serp` | Use DataForSEO exports or an authorized connection to cluster keywords by SERP overlap, validate page intent and trace answer-engine cita... |
| 880 | `datawebot` | "Find products for sale across online shops, list returned sellers' prices with direct links, and run Amazon and Shopify extraction Jobs ... |
| 881 | `day-book` | 'Daily cash, bank and digital day book: opening and closing balances per book, in/out movements, debit/credit presentation and reconcilia... |
| 882 | `dbos-golang` | "Guide for building reliable, fault-tolerant Go applications with DBOS durable workflows. Use when adding DBOS to existing Go code, creat... |
| 883 | `dbos-python` | "Guide for building reliable, fault-tolerant Python applications with DBOS durable workflows. Use when adding DBOS to existing Python cod... |
| 884 | `dbos-typescript` | "Guide for building reliable, fault-tolerant TypeScript applications with DBOS durable workflows. Use when adding DBOS to existing TypeSc... |
| 885 | `dbt-transformation-patterns` | "Production-ready patterns for dbt (data build tool) including model organization, testing strategies, documentation, and incremental pro... |
| 886 | `ddd-context-mapping` | "Map relationships between bounded contexts and define integration contracts using DDD context mapping patterns." |
| 887 | `ddd-strategic-design` | "Design DDD strategic artifacts including subdomains, bounded contexts, and ubiquitous language for complex business domains." |
| 888 | `ddd-tactical-patterns` | "Apply DDD tactical patterns in code using entities, value objects, aggregates, repositories, and domain events with explicit invariants." |
| 889 | `de-ai-writer` | "Chinese AI-smell removal engine: 35 Chinese AI-tell patterns (赋能/闭环), AI-smell scoring, de-AI rewriting, style clone. Use when a Chinese... |
| 890 | `debate-kickoff` | "Starter: frame a decision as a multi-model debate — picks sides, seats providers, and launches /octo:debate with a well-formed motion" |
| 891 | `debate-review` | Two-model debate review of a GitHub PR, GitLab MR, Azure DevOps PR, or local working tree, posted as inline comments or printed. Use for ... |
| 892 | `debug-buttercup` | "All pods run in namespace crs. Use when pods in the crs namespace are in CrashLoopBackOff, OOMKilled, or restarting, multiple services r... |
| 893 | `debugger` | "Investigate a reproducible error or failing test, test root-cause hypotheses, implement a scoped fix when authorized, and report actual ... |
| 894 | `debugging-and-error-recovery` | Guides systematic root-cause debugging. Use when tests fail, builds break, behavior doesn't match expectations, or you encounter any unex... |
| 895 | `debugging-code` | "Interactively debug source code — set breakpoints, step through execution line by line, inspect live variable state, evaluate expression... |
| 896 | `debugging-strategies` | "Transform debugging from frustrating guesswork into systematic problem-solving with proven strategies, powerful tools, and methodical ap... |
| 897 | `debugging-toolkit` | "Use when working with debugging toolkit smart debug (Alias for debugging-toolkit-smart-debug)" |
| 898 | `debugging-toolkit-smart-debug` | "Diagnose failures from reproduction steps, traces, logs and code; test hypotheses and verify a scoped fix without inventing production e... |
| 899 | `decision-navigator` | "Guide stuck or overwhelmed users through targeted branching questions until they reach concrete next steps." |
| 900 | `deed-page` | "Publish an HTML file or static folder to a permanent public https://<slug>.deed.page/ URL with one curl request. No account; the first p... |
| 901 | `deep-research` | "Run autonomous research tasks that plan, search, read, and synthesize information into comprehensive reports." |
| 902 | `deep-research-framework` | "Framework for deep research reports: define the question and tier sources first, cross-verify, then write conclusion-first reports with ... |
| 903 | `deepapi` | "Use DeepAPI for supported scraping, research, and email workflows with explicit credentials and approval." |
| 904 | `defi-protocol-templates` | "Implement DeFi protocols with educational templates for staking, AMMs, governance, and lending systems. Use when building decentralized ... |
| 905 | `defi-yield-strategy-allocator` | 'Multi-vault automated yield strategy allocation register: APY benchmarks, impermanent loss risk tiers, and rebalancing triggers.' |
| 906 | `define-my-content-pillars` | "Find the three to five subjects someone can post about repeatedly, from what they have published and know first-hand. Use when someone a... |
| 907 | `defuddle` | Extract clean markdown content from web pages using Defuddle CLI, removing clutter and navigation to save tokens. Use instead of WebFetch... |
| 908 | `dei-dashboard` | 'Diversity, equity and inclusion dashboard: metric by department and period, value against target, group size and minimum-threshold flag.... |
| 909 | `deja-history` | "Search this machine's past AI coding sessions across Claude Code, Codex, Cursor, Gemini CLI and thirty-nine other agents before editing,... |
| 910 | `delegate-setup` | Configure approved delegation lanes across installed implementer CLIs, including optional model and effort choices, then write global or ... |
| 911 | `delegating-to-agents` | "Delegate bounded work to other AI agents while preserving context, ownership, and progress checks." |
| 912 | `delegation` | 'Before spawning a subagent or dispatching a build, review or research, and before trusting its report: the brief, the delegate, parallel... |
| 913 | `dependency-analysis` | Analyze internal and package dependencies using Ontoly graph traversal. Use when asked which modules, packages, services, or files depend... |
| 914 | `dependency-management-deps-audit` | "You are a dependency security expert specializing in vulnerability scanning, license compliance, and supply chain security. Analyze proj... |
| 915 | `dependency-scanning` | Scan package dependencies for known vulnerabilities using Snyk, Dependabot, and OWASP Dependency-Check. |
| 916 | `dependency-upgrade` | "Master major dependency version upgrades, compatibility analysis, staged upgrade strategies, and comprehensive testing approaches." |
| 917 | `deploy-to-vercel` | "Deploy applications and websites to Vercel. Use when the user requests deployment actions like \"deploy my app\", \"deploy and give me t... |
| 918 | `deployment-engineer` | Expert deployment engineer specializing in modern CI/CD pipelines, GitOps workflows, and advanced deployment automation. |
| 919 | `deployment-pipeline-design` | "Architecture patterns for multi-stage CI/CD pipelines with approval gates and deployment strategies." |
| 920 | `deployment-procedures` | "Production deployment principles and decision-making. Safe deployment workflows, rollback strategies, and verification. Teaches thinking... |
| 921 | `deployment-validation-config-validate` | "Validate application configurations with schemas, configuration tests, and checks for security and environment consistency." |
| 922 | `deprecation-and-migration` | Manages deprecation and migration. Use when removing old systems, APIs, or features. Use when migrating users from one implementation to ... |
| 923 | `derive-tests` | '''What should we test'' or a coverage map: derive the coverage map and missing tests from docs and code; check mode reports staleness.' |
| 924 | `desearch-mcp` | "Use Desearch MCP when the user chooses Desearch for web research, X posts, people discovery, or company search and enrichment. Confirm b... |
| 925 | `design-how-build-design-system` | "Extract semantic tokens and reusable components from an existing app, check behavior and visual parity, and validate one pilot flow." |
| 926 | `design-how-component-docs` | "Write one component entry from implementation, stories and real call sites, including states, behavior and usage constraints." |
| 927 | `design-how-design-system-boss` | "Route a whole-app UI consistency request to a design-system build or adoption audit, then verify a representative flow." |
| 928 | `design-how-make-font` | "Fit a modifiable open typeface to aggregate reference measurements, then verify glyph coverage, spacing and web distribution." |
| 929 | `design-how-make-logo` | "Develop original mark and wordmark directions from a brief, compare legibility and similarity, and prepare a reviewed asset package." |
| 930 | `design-how-make-motion` | "Turn an approved product story into a short motion video with a timing sheet, review cuts and measured export checks." |
| 931 | `design-how-migrate-design-system` | "Audit or replace legacy UI with an existing design system in bounded waves while preserving route behavior and rendering." |
| 932 | `design-how-token-mapping` | "Produce a read-only mapping from hardcoded styling to semantic design tokens with exact, near, ambiguous and missing matches." |
| 933 | `design-how-ui-review` | "Review a rendered screen or flow and rank reproducible usability, accessibility and responsive defects with evidence." |
| 934 | `design-it` | "Routes frontend design tasks to 48 specific UI styles. Triggers for websites, app screens, or UI components requesting a specific aesthe... |
| 935 | `design-md` | "Analyze Stitch projects and synthesize a semantic design system into DESIGN.md files" |
| 936 | `design-orchestration` | Orchestrates design workflows by routing work through brainstorming, multi-agent review, and execution readiness in the correct order. |
| 937 | `design-philosophy` | Visual philosophy and art-direction for frontend. Use when creating high-concept work, campaigns, or when the user asks for a visual phil... |
| 938 | `design-spatial` | Design — spatial composition |
| 939 | `design-spells` | Curated micro-interactions and design details that add "magic" and personality to websites and apps. |
| 940 | `design-system` | "Mechanical implementation invariants for frontend design: token architecture, typography hierarchy, loading order, FOUT prevention, chro... |
| 941 | `design-taste-frontend` | tasteskill 2.5.1, the anti-slop frontend skill. Builds professional company websites at the level of figma.com and x.ai: plain copy in a ... |
| 942 | `design-theme-guide` | 'Design-token register: colour, typography, spacing and radius tokens with light and dark values, contrast ratio and WCAG level. Use for ... |
| 943 | `design-thinking` | Direction and intent for frontend design. Use with design when defining purpose, tone, domain, color world, and review bar; includes cros... |
| 944 | `design-token-contrast` | "Checks WCAG 2.2 contrast between the color tokens of a project (light and dark theme) and suggests the closest passing color that keeps ... |
| 945 | `design-ux` | "UX / usability audit — heuristic evaluation of INTERACTIVE UIs (not just visual polish). Load with design when a UI \"feels off\", \"suc... |
| 946 | `detect-ai-text` | Estimate whether a document's prose was written by AI, with the linguistic tells and honest abstention on non-prose. Use when the user as... |
| 947 | `deterministic-design` | "Measure rendered UI layout with reproducible spatial metrics and a separately assessed usability review; distinguish measurements from s... |
| 948 | `dev` | Development workflows for the playwright-cli repository. Use when the user asks about rolling dependencies, releasing, or other repo main... |
| 949 | `dev-to-hashnode` | When the user wants to publish on Dev.to, Hashnode, or other developer blogging platforms. Trigger phrases include "Dev.to," "Hashnode," ... |
| 950 | `devcontainer-setup` | Creates devcontainers with Claude Code, language-specific tooling (Python/Node/Rust/Go), and persistent volumes. Use when adding devconta... |
| 951 | `devcontainers-nix` | Create reproducible development environments with Dev Containers, Nix flakes, and Devbox for consistent toolchains across teams. |
| 952 | `developer-advocacy` | "When the user wants to do developer advocacy activities including conference talks, live coding, podcasts, and building in public." |
| 953 | `developer-audience-context` | "When the user wants to establish or update their developer audience context. Also use when starting any other developer marketing skill ... |
| 954 | `developer-churn` | When the user wants to understand, reduce, or recover from developer churn. Trigger phrases include "why developers leave," "churn rate,"... |
| 955 | `developer-listening` | "Monitor what developers say about your brand, competitors, and the problems they're solving. Track mentions and conversations across Git... |
| 956 | `developer-newsletter` | When the user wants to create, write, or improve a newsletter for developer audiences. Trigger phrases include "newsletter," "email marke... |
| 957 | `developer-onboarding` | "Get developers to \"Hello World\" fast with optimized quickstarts, tutorials, and sample apps." |
| 958 | `developer-sandbox` | "Design and build interactive playgrounds that let developers experience your product without commitment. This skill covers playground ar... |
| 959 | `developer-seo` | "SEO strategy for technical queries and developer audiences. Covers keyword research for \"how to X in language\" queries, error message ... |
| 960 | `developer-signup-flow` | "Design frictionless signup experiences for developers including GitHub OAuth, API key generation, and onboarding personalization." |
| 961 | `development` | "Comprehensive web, mobile, and backend development workflow bundling frontend, backend, full-stack, and mobile development skills for en... |
| 962 | `devops-deploy` | "DevOps e deploy de aplicacoes — Docker, CI/CD com GitHub Actions, AWS Lambda, SAM, Terraform, infraestrutura como codigo e monitoramento." |
| 963 | `devops-pipeline-builder` | Design and implement CI/CD pipelines, Docker configurations, deployment strategies, and infrastructure automation with production-ready p... |
| 964 | `devops-troubleshooter` | Expert DevOps troubleshooter specializing in rapid incident response, advanced debugging, and modern observability. |
| 965 | `devrel-content` | "When the user wants to create technical content for developers including blog posts, tutorials, and documentation." |
| 966 | `diagnose-android-overheating` | "Use when diagnosing Android overheating, idle heat, thermal throttling, charging or radio heat, or abnormal battery drain with read-only... |
| 967 | `diagnosing-bugs` | Diagnosis loop for hard bugs and performance regressions. Use when the user says "diagnose"/"debug this", or reports something broken/thr... |
| 968 | `diagnosing-superpowers` | Use when a superpowers session went wrong and your human partner wants to know why — repeated work, ignored plans, stumbles, poor results... |
| 969 | `diagram-generator` | "Generate, refine, validate, and render diagrams from natural language, notes, code, schemas, or existing diagram sources: flowcharts, sw... |
| 970 | `diary` | "Unified Diary System: A context-preserving automated logger for multi-project development." |
| 971 | `diff-marketing` | "Turn verified shipped Git changes into customer-facing launch drafts for blogs, newsletters, social posts and documentation." |
| 972 | `differential-review` | "Security-focused code review for PRs, commits, and diffs." |
| 973 | `digital-forensics` | "Authorized digital forensics: memory dumps, disk timelines, PCAP investigation, artifact triage, and incident-response evidence preserva... |
| 974 | `directory-submissions` | Plan a product directory launch with a reusable manifest, current eligibility checks and reviewed single-directory submission drafts. |
| 975 | `disaster-recovery` | Implement disaster recovery strategies and runbooks. Configure RPO/RTO targets and failover procedures. Use when planning for business co... |
| 976 | `disciplinary-pip-tracker` | 'Disciplinary and performance-improvement case register: case type, linked review or issue, improvement goals, review dates, outcome and ... |
| 977 | `discord-automation` | "Automate Discord tasks via Rube MCP (Composio): messages, channels, roles, webhooks, reactions. Always search tools first for current sc... |
| 978 | `discord-bot-architect` | Specialized skill for building production-ready Discord bots. Covers Discord.js (JavaScript) and Pycord (Python), gateway intents, slash ... |
| 979 | `dispatch` | "Delegate tasks to OpenAI Codex CLI and Google Antigravity CLI from Claude Code with topic-aware sessions" |
| 980 | `dispatching-parallel-agents` | Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies |
| 981 | `distribute-skill-to-all-agents` | "Distribute a skill across configured agent skill folders while respecting local symlink layouts." |
| 982 | `distributed-debugging-debug-trace` | "You are a debugging expert specializing in setting up comprehensive debugging environments, distributed tracing, and diagnostic tools. C... |
| 983 | `distributed-tracing` | "Implement distributed tracing with Jaeger and Tempo for request flow visibility across microservices." |
| 984 | `ditto` | "Use when a user asks to mine or update a private, evidence-backed work profile from local Claude Code, Codex, Copilot CLI, or OpenCode s... |
| 985 | `django-access-review` | "Use when reviewing Django or DRF access control: trace authorization flows, IDOR risks, object permissions, query scoping and tenant iso... |
| 986 | `django-perf-review` | Django performance code review. Use when asked to "review Django performance", "find N+1 queries", "optimize Django", "check queryset per... |
| 987 | `django-pro` | Master Django 5.x with async views, DRF, Celery, and Django Channels. Build scalable web applications with proper architecture, testing, ... |
| 988 | `dns-management` | Configure DNS zones and records. Manage Route53, Cloud DNS, and self-hosted DNS. Use when setting up DNS infrastructure. |
| 989 | `doc-coauthoring` | "This skill provides a structured workflow for guiding users through collaborative document creation. Act as an active guide, walking use... |
| 990 | `doc2math` | Convert narrative technical documents into grounded Mathematical Problem Specifications with variables, constraints, objectives, and unce... |
| 991 | `docker-compose` | Define and run multi-container Docker applications using Docker Compose. |
| 992 | `docker-expert` | "You are an advanced Docker containerization expert with comprehensive, practical knowledge of container optimization, security hardening... |
| 993 | `docker-management` | Build, optimize, and troubleshoot Docker containers and images. |
| 994 | `docs-architect` | Creates comprehensive technical documentation from existing codebases. Analyzes architecture, design patterns, and implementation details... |
| 995 | `docs-as-marketing` | "Transform documentation into a powerful marketing channel that attracts, converts, and retains developers." |
| 996 | `docs-generator` | "Generate technical deliverables from completed analysis: reverse-engineering reports, penetration-test reports, CTF write-ups, and signa... |
| 997 | `docs-guard` | "Review generated or changed documentation before it ships, including READMEs, API references, docstrings, changelogs, tutorials, and doc... |
| 998 | `document-app` | '''Document the app'': write or refresh an app''s system docs from its code. ''Are the docs right?'': check mode, which only reports wher... |
| 999 | `document-management-system` | 'Document register: type, owner, upload and signed dates, version, storage link, confidentiality and signature-required flag. Use for doc... |
| 1000 | `documentation` | "Documentation generation workflow covering API docs, architecture docs, README files, code comments, and technical writing." |
| 1001 | `documentation-and-adrs` | Records decisions and documentation. Use when making architectural decisions, changing public APIs, shipping features, or when you need t... |
| 1002 | `documentation-generation-doc-generate` | "Generate API, architecture or user documentation from current code and tests; validate examples and label gaps without inventing behavio... |
| 1003 | `documentation-templates` | "Documentation templates and structure guidelines. README, API docs, code comments, and AI-friendly documentation." |
| 1004 | `docusign-automation` | "Automate DocuSign tasks via Rube MCP (Composio): templates, envelopes, signatures, document management. Always search tools first for cu... |
| 1005 | `domain-authority-simulator` | "Domain Authority Simulator. Use when working with domain signals and an explicit scoring rubric." |
| 1006 | `domain-comparison-report-tool` | "Domain Comparison Report Tool. Use when working with two or more domains with dated comparable metrics." |
| 1007 | `domain-driven-design` | "Plan and route Domain-Driven Design work from strategic modeling to tactical implementation and evented architecture patterns." |
| 1008 | `domain-migration` | "Plan and validate an SEO site move with a URL inventory, redirect map, canonical cutover and backlink-update drafts." |
| 1009 | `domain-modeling` | Build and sharpen a project's domain model. Use when the user wants to pin down domain terminology or a ubiquitous language, record an ar... |
| 1010 | `doom-pay` | "Add self-custodial DOOM and wDOOM checkout links with DoomPay, then verify payment receipts on Doomsday Network Layer-1 or Base Mainnet." |
| 1011 | `doomsday-escrow` | "Verify cryptographic Proof-of-Escrow collateral (L1 UTXO outpoint proofs and Base Mainnet wDOOM settlement receipts) on GitHub bounties ... |
| 1012 | `dos-verify-done-claims` | "Before accepting an agent's 'done / shipped / fixed' claim, verify it against ground truth (git ancestry + the commit's own diff) using ... |
| 1013 | `dotnet-architect` | Expert .NET backend architect specializing in C#, ASP.NET Core, Entity Framework, Dapper, and enterprise application patterns. |
| 1014 | `dotnet-backend` | "Build ASP.NET Core 8+ backend services with EF Core, auth, background jobs, and production API patterns." |
| 1015 | `dotnet-backend-patterns` | "Master C#/.NET patterns for building production-grade APIs, MCP servers, and enterprise backends with modern best practices (2024/2025)." |
| 1016 | `dotnet-reverse` | ".NET/C# binary reverse engineering: managed PE analysis, dnSpyEx debugging, de4dot deobfuscation (ConfuserEx/SmartAssembly/Babel), IL pa... |
| 1017 | `doubt-driven-development` | "Subjects every non-trivial decision to a fresh-context adversarial review before it stands." |
| 1018 | `dox-init` | "Initialize a DOX AGENTS.md tree in a project: fetch the DOX contract, scan the real structure, then write nested AGENTS.md files with pu... |
| 1019 | `draft-my-comments` | "Write a LinkedIn comment that adds something the post did not have, not agreement. Use when someone asks what to comment, wants to engag... |
| 1020 | `draw` | "Vector graphics and diagram creation, format conversion (ODG/SVG/PDF) with LibreOffice Draw." |
| 1021 | `drizzle-migration-conflict` | "Diagnose, repair, and prevent Drizzle Kit migration conflicts involving generated SQL, snapshots, journals, merge queues, and team workf... |
| 1022 | `drizzle-orm-expert` | "Expert in Drizzle ORM for TypeScript — schema design, relational queries, migrations, and serverless database integration. Use when buil... |
| 1023 | `dropbox-automation` | "Automate Dropbox file management, sharing, search, uploads, downloads, and folder operations via Rube MCP (Composio). Always search tool... |
| 1024 | `dropthehassle-publish` | "Publish a finished static site to a free HTTPS link with DropTheHassle: build it if needed, deploy, hand over the claim link, verify it ... |
| 1025 | `dsh-deepread` | "Use for evidence-first reading of articles, books, PDFs, web pages, or document sets, with knowledge maps and Feynman checks." |
| 1026 | `duplicate-content-checker` | "Duplicate Content Checker. Use when working with two or more texts or accessible pages." |
| 1027 | `dwarf-expert` | Provides expertise for analyzing DWARF debug files and understanding the DWARF debug format/standard (v3-v5). Triggers when understanding... |
| 1028 | `dx-optimizer` | Developer Experience specialist. Improves tooling, setup, and workflows. Use for requested project setup or measured development friction... |
| 1029 | `e2e` | "Write, run and debug e2e tests for web and iOS/Android apps that mix plain-language agent steps with exact assertions, replaying cached ... |
| 1030 | `e2e-testing` | "End-to-end testing workflow with Playwright for browser automation, visual regression, cross-browser testing, and CI/CD integration." |
| 1031 | `e2e-testing-patterns` | "Build reliable, fast, and maintainable end-to-end test suites that provide confidence to ship code quickly and catch regressions before ... |
| 1032 | `earllm-build` | "Build, maintain, and extend the EarLLM One Android project — a Kotlin/Compose app that connects Bluetooth earbuds to an LLM via voice pi... |
| 1033 | `eas-app-stores` | Curated upstream guidance for Eas App Stores; use when the workflow matches the user goal. |
| 1034 | `eas-hosting` | Curated upstream guidance for Eas Hosting; use when the workflow matches the user goal. |
| 1035 | `eas-observe` | Curated upstream guidance for Eas Observe; use when the workflow matches the user goal. |
| 1036 | `eas-simulator` | Curated upstream guidance for Eas Simulator; use when the workflow matches the user goal. |
| 1037 | `eas-update-insights` | "Check the health of published EAS Updates: crash rates, install/launch counts, unique users, payload size, and the split between embedde... |
| 1038 | `eas-workflows` | "Use when writing or reviewing Expo EAS workflow YAML: inspect current schema and job syntax, validate configuration, and separate draft ... |
| 1039 | `ebpf-observability` | Use eBPF for deep kernel-level observability — trace syscalls, network flows, and application behavior without code changes using Cilium,... |
| 1040 | `ecl-harness-engineer` | "Create or audit ECL Agent Harness infrastructure: AGENTS.md, change tracking, repository guidance, lint checks, CI gates, and agent hand... |
| 1041 | `ecommerce-listing-image-set` | "Install and use the official Ecommerce Product Images package, pinned by digest, for paid hosted work on the Beatra service." |
| 1042 | `edr-bypass-re` | "Review EDR telemetry and known defense-evasion classes using offline evidence and controlled defensive coverage assessments." |
| 1043 | `effect-smol-ai-docs` | "Update Effect AI documentation sources and verify generated LLMS.md, examples and coverage." |
| 1044 | `effect-smol-bundle-analysis` | "Compare Effect bundle fixtures across revisions and identify verified changes in bytes and composition." |
| 1045 | `effect-smol-changesets` | "Audit Effect package changes for consumer-visible impacts and record the appropriate changeset and migration notes." |
| 1046 | `effect-smol-ci-maintenance` | "Review or update Effect GitHub Actions with a job-by-job trigger, revision, permission and artifact trust inventory." |
| 1047 | `effect-smol-dependency-maintenance` | "Synchronize Effect workspace dependency changes across manifests, lockfile and the affected validation matrix." |
| 1048 | `effect-smol-effect-development` | "Implement or review Effect integrations using targeted repository API guidance and version-matched runtime or type checks." |
| 1049 | `effect-smol-jsdocs` | "Write or review Effect public JSDoc against declaration, implementation, call-site and doctest evidence." |
| 1050 | `effect-smol-migration-guidance` | "Keep Effect v3-to-v4 migration annotations and generated guidance aligned with verified public API replacements." |
| 1051 | `effect-smol-package-development` | "Create or move an Effect workspace package while checking registration, exports, generated barrels and packed contents." |
| 1052 | `effect-smol-performance-analysis` | "Compare Effect runtime performance or TypeScript checker cost with matched fixtures and repeatable measurements." |
| 1053 | `effect-smol-test-development` | "Add focused Vitest and Tstyche coverage for Effect runtime behavior and public type inference." |
| 1054 | `effect-smol-vendored-assets` | "Refresh Effect vendored assets with pinned sources, retained notices, deterministic generation and verified consumer impact." |
| 1055 | `effective-agent-skills` | "Author and review high-quality agent skills with triggers, progressive disclosure, and safety notes." |
| 1056 | `efficient-web-research` | Protocol for token-efficient web research. Use when accessing URLs, GitHub repos, or running search queries. Prevents full-page fetching ... |
| 1057 | `ejentum-reasoning-harness` | "MCP server exposing four cognitive harness modes (reasoning, code, anti-deception, memory). Each call returns an engineered scaffold (fa... |
| 1058 | `electron-development` | "Master Electron desktop app development with secure IPC, contextIsolation, preload scripts, multi-process architecture, electron-builder... |
| 1059 | `electron-drive-skill` | "Launch the project's Electron app on a scratch profile and drive it: click, type, screenshot, run renderer or main-process code, read lo... |
| 1060 | `elixir-pro` | Write idiomatic Elixir code with OTP patterns, supervision trees, and Phoenix LiveView. Masters concurrency, fault tolerance, and distrib... |
| 1061 | `elk-stack` | Deploy and manage the ELK Stack (Elasticsearch, Logstash, Kibana) for log aggregation and analysis. |
| 1062 | `elon-musk` | "Simulacao ficticia e explicitamente rotulada de estilo comunicacional associado a Elon Musk, com analise de primeiros principios e verif... |
| 1063 | `email-issue-fixer` | "Fix small email mistakes without touching the writer's voice, and strip tracking parameters from links on request. Always returns the co... |
| 1064 | `email-marketing-bible` | "Data-backed email marketing for AI agents: automation flows, deliverability triage, copy de-slopping, AI email design, ESP control via M... |
| 1065 | `email-security` | "Authorized email security review: phishing analysis, SPF/DKIM/DMARC header authentication, BEC pattern investigation, and mailbox token ... |
| 1066 | `email-sequence` | "You are an expert in email marketing and automation. Your goal is to create email sequences that nurture relationships, drive action, an... |
| 1067 | `email-systems` | Design transactional and marketing email delivery, queues, templates, authentication, suppression and monitoring. |
| 1068 | `embedded-agents-agent-sdk` | 'Only when the Agent SDK is asked for, an agent needs Claude Code''s own tools, or the app already runs it: embed Claude agents in a Next... |
| 1069 | `embedded-agents-messages-api` | 'Building, adding or wiring up an agent or an agent chat inside a Next.js app: embed Claude agents on the Messages API, the default way.' |
| 1070 | `embedding-strategies` | "Guide to selecting and optimizing embedding models for vector search applications." |
| 1071 | `emblemai-crypto-wallet` | "Crypto wallet management across 7 blockchains via EmblemAI Agent Hustle API. Balance checks, token swaps, portfolio analysis, and transa... |
| 1072 | `emergency-card` | 生成紧急情况下快速访问的医疗信息摘要卡片。当用户需要旅行、就诊准备、紧急情况或询问"紧急信息"、"医疗卡片"、"急救信息"时使用此技能。提取关键信息（过敏、用药、急症、植入物），支持多格式输出（JSON、文本、二维码），用于急救或快速就医。 |
| 1073 | `emil-design-eng` | "Design and review polished UI with Emil Kowalski’s guidance on animation, interaction feedback, component craft, and accessibility." |
| 1074 | `emil-ui-prototype` | "Build distinct UI variants behind a development-only picker and integrate the variant the user selects." |
| 1075 | `emotional-arc-designer` | "Map the emotional progression of a narrative, page, or campaign when content needs a coherent path from attention to action." |
| 1076 | `employee-suggestion-hub` | 'Suggestion register: submitter or anonymous flag, category, votes, reviewer, decision and response status. Use for employee feedback pro... |
| 1077 | `employment-contract-templates` | "Templates and patterns for creating draft employment documentation for jurisdiction-specific legal review including contracts, offer let... |
| 1078 | `energy-procurement` | Codified expertise for electricity and gas procurement, tariff optimisation, demand charge management, renewable PPA evaluation, and mult... |
| 1079 | `enhance-prompt` | Transforms vague UI ideas into polished, Stitch-optimized prompts. Enhances specificity, adds UI/UX keywords, injects design system conte... |
| 1080 | `enterprise-vpn-attack` | External SSL VPN / remote-access appliance attack matrix |
| 1081 | `entropy-box` | "Entropy Box knowledge-compiler for embodied-AI: turns bounded requirements into grounded workflows via Solution Consult, Search, Lookup,... |
| 1082 | `environment-setup-guide` | "Guide developers through setting up development environments with proper tools, dependencies, and configurations" |
| 1083 | `environments` | 'Adding a variable or secret, ''set up production'', a domain or a provider token, ''which database is this'', a leaked key: dev and prod... |
| 1084 | `eol-resistor-calculator` | "Calculates and validates end-of-line (EOL, SEOL, DEOL, TEOL) resistor loops for intrusion alarm panels (Honeywell, DSC, Paradox, Bosch) ... |
| 1085 | `equibles` | "Query Equibles for US stock market data: SEC filing search, XBRL financial statements, earnings call transcripts, insider and 13F holdin... |
| 1086 | `error-debugging-error-analysis` | "You are an expert error analysis specialist with deep expertise in debugging distributed systems, analyzing production incidents, and im... |
| 1087 | `error-debugging-error-trace` | "You are an error tracking and observability expert specializing in implementing comprehensive error monitoring solutions. Set up error t... |
| 1088 | `error-debugging-multi-agent-review` | "Review a defined code diff from relevant correctness, authorization and performance perspectives; delegate only when authorized and repr... |
| 1089 | `error-detective` | Search logs and codebases for error patterns, stack traces, and anomalies. Correlates errors across systems and identifies root causes. |
| 1090 | `error-diagnostics-error-analysis` | "You are an expert error analysis specialist with deep expertise in debugging distributed systems, analyzing production incidents, and im... |
| 1091 | `error-diagnostics-error-trace` | "You are an error tracking and observability expert specializing in implementing comprehensive error monitoring solutions. Set up error t... |
| 1092 | `error-diagnostics-smart-debug` | "Diagnose failures from reproduction steps, traces, logs and code; test hypotheses and verify a scoped fix without inventing production e... |
| 1093 | `error-handling-patterns` | "Build resilient applications with robust error handling strategies that gracefully handle failures and provide excellent debugging exper... |
| 1094 | `esl-price-sync` | "Synchronizes retail prices between ERP/POS systems and Electronic Shelf Labels (SES-imagotag, ZKONG, Pricer, Hanshow, SOLUM) with delta ... |
| 1095 | `esop-equity-tracker` | 'ESOP and equity grant register: grant date, shares granted, strike price, vesting start, schedule and cliff, plus vested and exercised s... |
| 1096 | `ethical-hacking-methodology` | "Master the complete penetration testing lifecycle from reconnaissance through reporting. This skill covers the five stages of ethical ha... |
| 1097 | `etsy-search-listings` | "Fetch live Etsy search listing rows for a keyword, market phrase, or category via Apify Actor publicrecords/etsy-search-scraper (MCP). N... |
| 1098 | `etsy-shop-sales-history` | "Read Etsy shop sales counters, deltas, and breakout flags from Apify Actor publicrecords/etsy-shop-velocity (MCP panel snapshot). Needs ... |
| 1099 | `evaluation` | "Build evaluation frameworks for agent systems. Use when testing agent performance systematically, validating context engineering choices... |
| 1100 | `event-sourcing-architect` | "Expert in event sourcing, CQRS, and event-driven architecture patterns. Masters event store design, projection building, saga orchestrat... |
| 1101 | `event-staffing-compliance` | Assess worker-classification and compliance risk for temporary event staffing in the US and Canada — W-2 vs 1099, misclassification penal... |
| 1102 | `event-staffing-ordering` | Order W-2 compliant temporary event staff for conventions, trade shows, festivals, concerts, sporting events, and brand activations acros... |
| 1103 | `event-store-design` | "Design and implement event stores for event-sourced systems. Use when building event sourcing infrastructure, choosing event store techn... |
| 1104 | `events-activities` | 'Event register: type, date and time, venue, organizer, audience, budget against actual cost, RSVP and attendance counts and feedback sco... |
| 1105 | `evidence-hygiene` | Evidence-capture and PoC-redaction discipline for bug-bounty submissions |
| 1106 | `evolution` | "This skill provides a reviewable workflow for maintaining makepad-skills during development. It does not install automatic evolution by ... |
| 1107 | `exa-search` | "Semantic search, similar content discovery, and structured research using Exa API. Use when you need semantic/embeddings-based search, f... |
| 1108 | `examprep-ai` | "Exam preparation assistant that converts syllabi, past papers, or notes into a ranked High Score Roadmap. Covers theory, numericals, MCQ... |
| 1109 | `executing-plans` | Use when executing an implementation plan in the current session as the implementer yourself — your human partner chose inline execution,... |
| 1110 | `expense-accounting` | 'Expense accounting register: expense number and date, payee with PAN and VAT, bill reference, document type, amount with VAT, ledger acc... |
| 1111 | `expense-management` | 'Expense claim register: claim id, employee and department, amount and tax, approver and level, category, cost centre, budget line, recei... |
| 1112 | `explain-interface` | Explains how a website, a visual effect or an animation was built, from a live URL or a screenshot. |
| 1113 | `explain-like-socrates` | Explains concepts using Socratic-style dialogue. Use when the user asks to explain, teach or help understand a concept like socrates. |
| 1114 | `expo-animation` | Curated upstream guidance for Expo Animation; use when the workflow matches the user goal. |
| 1115 | `expo-api-routes` | Guidelines for creating API routes in Expo Router with EAS Hosting |
| 1116 | `expo-brownfield` | Integrate Expo and React Native into an existing native iOS or Android app. Use when the user mentions brownfield, embedding React Native... |
| 1117 | `expo-cicd-workflows` | Helps understand and write EAS workflow YAML files for Expo projects. Use this skill when the user asks about CI/CD or workflows in an Ex... |
| 1118 | `expo-deployment` | "Deploy Expo apps with EAS: build and submit iOS and Android releases, configure build and submit profiles, manage versions and store met... |
| 1119 | `expo-dev-client` | Build Expo app for development |
| 1120 | `expo-examples` | "Expo's official example projects — the expo/examples repo of ~70 `with-*` integrations (Stripe, Clerk, Supabase, OpenAI, maps, Reanimate... |
| 1121 | `expo-module` | "Guide for creating and writing Expo native modules and views using the Expo Modules API (Swift, Kotlin, TypeScript). Covers module defin... |
| 1122 | `expo-observe` | "Set up and query EAS Observe for Expo apps, including root integration, interactive markers, route metrics, CLI summaries, traces, logs,... |
| 1123 | `expo-tailwind-setup` | Set up Tailwind CSS v4 in Expo with react-native-css and NativeWind v5 for universal styling |
| 1124 | `expo-ui` | "Build native UI with the @expo/ui package: real SwiftUI on iOS and Jetpack Compose on Android rendered from React in an Expo or React Na... |
| 1125 | `expo-ui-jetpack-compose` | Build Android-native Expo SDK 55 UI with Jetpack Compose views/modifiers, Host sizing and platform-specific integration. |
| 1126 | `expo-ui-swift-ui` | Build iOS-native Expo SDK 55 UI with SwiftUI views/modifiers, Host/RNHostView embedding and native rebuild prerequisites. |
| 1127 | `extract-design` | "Extract the full design language from any website URL. Produces 8 output files including AI-optimized markdown, visual HTML preview, Tai... |
| 1128 | `extract-document-data` | Extract structured, grounded fields from documents — values cite their page, missing values abstain instead of hallucinating. Use for par... |
| 1129 | `faber-language` | "Write, check and run Faber programs, an experimental statically typed language for coding agents and human authors. Uses version-matched... |
| 1130 | `fable-safe-prompt` | "Rewrite allowed prompts to reduce false-positive safety triggers without bypassing policy or changing intent." |
| 1131 | `fact-check-x-complete` | "Compare claims from one or more AI answers, verify their citations against public primary sources, and produce an evidence-linked fact-c... |
| 1132 | `fact-check-x-unified` | Fact-Check-X 流程编排能力，依次组织各方答案汇总、各方答案聚合（未核验）、权威核验后的最终答案和各方答案测评，生成可打开、可审计、可迁移的阶段产物与完整报告包。 |
| 1133 | `faf-context` | Get your project to 100% ✪ AI-readiness, fast — the AI auto-detects your stack and only asks for what it can't know (your goal and the hu... |
| 1134 | `faf-expert` | "Advanced .faf (Foundational AI-context Format) specialist. IANA-registered format, MCP server config, championship scoring, bi-direction... |
| 1135 | `faf-go` | Guided interview to Gold Code (100% AI-Readiness). Use when helping users improve their .faf file through questions. Leverages Claude Cod... |
| 1136 | `faf-wizard` | "Done-for-you .faf generator. One-click AI context for any project - new, legacy, or famous. Auto-detects stack, scores readiness, works ... |
| 1137 | `fal-audio` | "Text-to-speech and speech-to-text using fal.ai audio models" |
| 1138 | `fal-generate` | "Generate images and videos using fal.ai AI models" |
| 1139 | `fal-image-edit` | "AI-powered image editing with style transfer and object removal" |
| 1140 | `fal-platform` | "Platform APIs for model management, pricing, and usage tracking" |
| 1141 | `fal-upscale` | "Upscale and enhance image and video resolution using AI" |
| 1142 | `fal-workflow` | "Generate workflow JSON files for chaining AI models" |
| 1143 | `falsify` | "The scientific thinking protocol for AI agents. Use when facing complex, ambiguous, or high-stakes questions where guessing is costly: h... |
| 1144 | `family-health-analyzer` | 整理家族病史和已知健康记录，识别需要医生或遗传咨询师评估的线索，不计算未经验证的个体发病概率 |
| 1145 | `famulor-skill` | "Operate Famulor assistants, communication history, campaigns, knowledge, automations, telephony, and workspace administration through it... |
| 1146 | `faq-generator` | "FAQ Generator. Use when working with actual questions plus answer facts." |
| 1147 | `fastapi-pro` | Build high-performance async APIs with FastAPI, SQLAlchemy 2.0, and Pydantic V2. Master microservices, WebSockets, and modern Python asyn... |
| 1148 | `fastapi-router-py` | "Create FastAPI routers following established patterns with proper authentication, response models, and HTTP status codes." |
| 1149 | `fastapi-templates` | "Create production-ready FastAPI projects with async patterns, dependency injection, and comprehensive error handling. Use when building ... |
| 1150 | `favicon` | Generate favicons from a source image |
| 1151 | `fda-food-safety-auditor` | "Expert AI auditor for FDA Food Safety (FSMA), HACCP, and PCQI compliance. Reviews food facility records and preventive controls." |
| 1152 | `fda-medtech-compliance-auditor` | "Expert AI auditor for Medical Device (SaMD) compliance, IEC 62304, and 21 CFR Part 820. Reviews DHFs, technical files, and software vali... |
| 1153 | `feature-flags` | Implement feature flags for progressive feature rollout using LaunchDarkly, Unleash, or custom solutions. |
| 1154 | `feature-tracking` | "Maintain durable feature-level memory across AI coding sessions with lightweight Markdown tracks for status, source-of-truth docs, decis... |
| 1155 | `featured-snippet-optimizer` | "Featured Snippet Optimizer. Use when working with target question and existing passage." |
| 1156 | `featured-tool-schema-generator` | "Featured Tool Schema Generator. Use when working with tool page URL and visible tool capabilities." |
| 1157 | `fedora-hyprland-installer` | Install, configure, verify, repair, update, and uninstall Hyprland on Fedora Linux with GPU-aware detection (NVIDIA/AMD/Intel). |
| 1158 | `fedramp-compliance` | Implement FedRAMP requirements for federal cloud services. Configure NIST 800-53 controls and continuous monitoring. Use when providing c... |
| 1159 | `ffuf-claude-skill` | "Web fuzzing with ffuf" |
| 1160 | `ffuf-web-fuzzing` | Expert guidance for ffuf web fuzzing during penetration testing, including authenticated fuzzing with raw requests, auto-calibration, and... |
| 1161 | `figma` | "Import Figma assets, tokens, components and motion into editable HyperFrames videos with source and fidelity checks." |
| 1162 | `figma-automation` | "Automate Figma tasks via Rube MCP (Composio): files, components, design tokens, comments, exports. Always search tools first for current... |
| 1163 | `figma-designer` | "Create structured Figma screens and libraries with ELAYA spacing, radius, semantic color variables, text styles, auto layout, and compon... |
| 1164 | `file-organizer` | "Organize files and folders by inspecting their contents, proposing a structure, and reviewing duplicates before authorized changes." |
| 1165 | `file-path-traversal` | "Identify and exploit file path traversal (directory traversal) vulnerabilities that allow attackers to read arbitrary files on the serve... |
| 1166 | `file-uploads` | Expert at handling file uploads and cloud storage. Covers S3, Cloudflare R2, presigned URLs, multipart uploads, and image optimization. K... |
| 1167 | `filesystem-context` | Use for file-based context management, dynamic context discovery, and reducing context window bloat. Offload context to files for just-in... |
| 1168 | `film-crew` | "Turn a one-line AI video idea into a shot list and per-shot, model-ready prompts via a film crew (director, DP, gaffer, editor, script s... |
| 1169 | `find-animation-opportunities` | "Propose purposeful motion opportunities from a read-only codebase review, with evidence and explicit exclusions." |
| 1170 | `find-bugs` | Find bugs, security vulnerabilities, and code quality issues in local branch changes. Use when asked to review changes, find bugs, securi... |
| 1171 | `find-complementary-founders` | "Use when an owner explicitly asks for a cofounder or project partner, or explicitly says they need a complementary builder, operator, go... |
| 1172 | `find-matching-tenders` | Find open AU/NZ government tenders matching what a company does, ranked by fit with why and gap analysis. Use when the user asks to find ... |
| 1173 | `finetune-llm` | "Fine-tune or post-train an LLM against measured VRAM budgets: probe the GPU, pick the engine, hash the data, smoke test, train instrumen... |
| 1174 | `finishing-a-development-branch` | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work |
| 1175 | `firebase` | Firebase gives you a complete backend in minutes - auth, database, storage, functions, hosting. But the ease of setup hides real complexi... |
| 1176 | `firebase-app-platform` | Build and operate apps on Firebase using Auth, Firestore, Cloud Functions, and Hosting. Use when building mobile/web backends with manage... |
| 1177 | `firecrawl-scraper` | "Deep web scraping, screenshots, PDF parsing, and website crawling using Firecrawl API. Use when you need deep content extraction from we... |
| 1178 | `firewall-config` | Configure iptables, nftables, and cloud firewalls. Implement network segmentation and traffic filtering. Use when securing network perime... |
| 1179 | `firmware-analyst` | Expert firmware analyst specializing in embedded systems, IoT security, and hardware reverse engineering. |
| 1180 | `firmware-pentest` | "Firmware penetration testing following the OWASP FSTM nine-stage flow: extraction, EMBA automation, Firmadyne/QEMU emulation, AFL++ fuzz... |
| 1181 | `fitness-analyzer` | 分析运动数据、识别运动模式、评估健身进展，并提供个性化训练建议。支持与慢性病数据的关联分析。 |
| 1182 | `five-axis-code-review` | "Five-axis code review checklist (correctness, security, readability, performance, test coverage) producing actionable comments instead o... |
| 1183 | `fix-review` | "Verify fix commits address audit findings without new bugs" |
| 1184 | `fixing-accessibility` | Audit and fix HTML accessibility issues including ARIA labels, keyboard navigation, focus management, color contrast, and form errors. Us... |
| 1185 | `fixing-metadata` | "Audit and fix HTML metadata including page titles, meta descriptions, canonical URLs, Open Graph tags, Twitter cards, favicons, JSON-LD ... |
| 1186 | `fixing-motion-performance` | Audit and fix animation performance issues including layout thrashing, compositor properties, scroll-linked motion, and blur effects. Use... |
| 1187 | `flash-compare` | "Compare products before buying: check OEM specs against owner reports, load tests and verified reviews, then keep at most two and reject... |
| 1188 | `flight-deck` | '''What''s the status'', ''where were we'', a progress report or status deck; long work that must survive compaction: multi-hour runs, ba... |
| 1189 | `flow-define` | "Multi-AI requirements scoping using available external providers (Double Diamond Define phase). Priority triggers: octo define, octo sco... |
| 1190 | `flow-deliver` | Multi-AI validation, scoring, and review using available external providers (Double Diamond Deliver phase) # Claude Code v2.1.12+ Integra... |
| 1191 | `flow-develop` | "Multi-AI implementation using available external providers (Double Diamond Develop phase). DO NOT use for simple code edits, reading/rev... |
| 1192 | `flow-discover` | "Multi-AI research using available external providers (Double Diamond Discover phase)" |
| 1193 | `flow-parallel` | "Decompose and execute large changes, migrations, or multi-issue fixes in parallel with quality gates" |
| 1194 | `flow-spec` | NLSpec authoring — use when you need a structured specification from multi-AI research and consensus |
| 1195 | `flowhunt-skill` | "Automation discovery audit skill. Walks through a 5-question workflow intake, then audits Gmail/Calendar/Slack/task trackers to identify... |
| 1196 | `flutter-expert` | Master Flutter development with Dart 3, advanced widgets, and multi-platform deployment. |
| 1197 | `folder-specific-claude-and-agents-md` | "Create folder-scoped CLAUDE.md and AGENTS.md guidance for future agents working in that area." |
| 1198 | `food-database-query` | Food Database Query |
| 1199 | `footval-follow-matches-and-tables` | "Football scores, fixtures, match centres and league tables through FootVal: live and past results, a team's next or last matches, events... |
| 1200 | `footval-scout-and-rank-players` | "Scout and rank footballers with FootVal: shortlists by league, position, age, foot and value; undervalued, overvalued, rising and young ... |
| 1201 | `footval-stats-and-transfer-news` | "Football season leaderboards and transfer news from FootVal: top scorers, assists, minutes and appearances per competition, plus confirm... |
| 1202 | `footval-value-and-compare-players` | "Explain what a footballer is worth with FootVal: its own transfer value next to the market value, the factors behind the gap, and compar... |
| 1203 | `foragent-call` | "Connect two AI agents by private phone number so they can talk directly and exchange files across computers or teammates using ForAgent." |
| 1204 | `form-cro` | Optimize any form that is NOT signup or account registration — including lead capture, contact, demo request, application, survey, quote,... |
| 1205 | `formik-patterns` | Formik form handling with validation patterns. Use when building forms, implementing validation, or handling form submission. |
| 1206 | `fp-async` | Practical async patterns using TaskEither - clean pipelines instead of try/catch hell, with real API examples |
| 1207 | `fp-backend` | Functional programming patterns for Node.js/Deno backend development using fp-ts, ReaderTaskEither, and functional dependency injection |
| 1208 | `fp-data-transforms` | Everyday data transformations using functional patterns - arrays, objects, grouping, aggregation, and null-safe access |
| 1209 | `fp-either-ref` | Quick reference for Either type. Use when user needs error handling, validation, or operations that can fail with typed errors. |
| 1210 | `fp-errors` | Stop throwing everywhere - handle errors as values using Either and TaskEither for cleaner, more predictable code |
| 1211 | `fp-option-ref` | Quick reference for Option type. Use when user needs to handle nullable values, optional data, or wants to avoid null checks. |
| 1212 | `fp-pipe-ref` | Quick reference for pipe and flow. Use when user needs to chain functions, compose operations, or build data pipelines in fp-ts. |
| 1213 | `fp-pragmatic` | A practical, jargon-free guide to functional programming - the 80/20 approach that gets results without the academic overhead |
| 1214 | `fp-react` | Practical patterns for using fp-ts with React - hooks, state, forms, data fetching. Includes version-specific React examples; verify fram... |
| 1215 | `fp-refactor` | Comprehensive guide for refactoring imperative TypeScript code to fp-ts functional patterns |
| 1216 | `fp-taskeither-ref` | Quick reference for TaskEither. Use when user needs async error handling, API calls, or Promise-based operations that can fail. |
| 1217 | `fp-ts-errors` | "Handle errors as values using fp-ts Either and TaskEither for cleaner, more predictable TypeScript code. Use when implementing error han... |
| 1218 | `fp-ts-pragmatic` | "A practical, jargon-free guide to fp-ts functional programming - the 80/20 approach that gets results without the academic overhead. Use... |
| 1219 | `fp-ts-react` | "Practical patterns for using fp-ts with React - hooks, state, forms, data fetching. Use when building React apps with functional program... |
| 1220 | `fp-types-ref` | Quick reference for fp-ts types. Use when user asks which type to use, needs Option/Either/Task decision help, or wants fp-ts imports. |
| 1221 | `framework-migration-code-migrate` | "You are a code migration expert specializing in transitioning codebases between frameworks, languages, versions, and platforms. Generate... |
| 1222 | `framework-migration-deps-upgrade` | "You are a dependency management expert specializing in safe, incremental upgrades of project dependencies. Plan and execute dependency u... |
| 1223 | `framework-migration-legacy-modernize` | "Orchestrate a comprehensive legacy system modernization using the strangler fig pattern, enabling gradual replacement of outdated compon... |
| 1224 | `free-design-resources` | 'Design resource register: resource and provider, licence type, commercial-use and attribution rules, export format, lock-in risk, free t... |
| 1225 | `free-tier-strategy` | "Design free tiers that convert to paid without creating resentment or abuse. Trigger phrases: free tier design, freemium model, free tri... |
| 1226 | `free-tool-strategy` | "You are an expert in engineering-as-marketing strategy. Your goal is to help plan and evaluate free tools that generate leads, attract o... |
| 1227 | `freshdesk-automation` | "Automate Freshdesk helpdesk operations including tickets, contacts, companies, notes, and replies via Rube MCP (Composio). Always search... |
| 1228 | `freshservice-automation` | "Automate Freshservice ITSM tasks via Rube MCP (Composio): create/update tickets, bulk operations, service requests, and outbound emails.... |
| 1229 | `frontend-api-integration-patterns` | "Production-ready patterns for integrating frontend applications with backend APIs, including race condition handling, request cancellati... |
| 1230 | `frontend-architecture` | "A portable, framework-agnostic architecture style for any React or React Native frontend. Organizes apps into feature modules with page/... |
| 1231 | `frontend-data-contracts` | "A portable, framework-agnostic discipline for type safety at the network edge of any React or React Native app." |
| 1232 | `frontend-design` | "Design and implement a distinctive frontend within the product’s existing brand, accessibility, performance and framework constraints." |
| 1233 | `frontend-dev-guidelines` | "You are a senior frontend engineer operating under strict architectural and performance standards. Use when creating components or pages... |
| 1234 | `frontend-developer` | Build React components, implement responsive layouts, and handle client-side state management. Masters React 19, Next.js 15, and modern f... |
| 1235 | `frontend-lighthouse` | "Add a portable Lighthouse CI gate for production frontend builds with Core Web Vitals budgets, category floors, median runs, and CI arti... |
| 1236 | `frontend-mobile-development-component-scaffold` | "Scaffold React and React Native components with TypeScript, accessibility, tests, styles, and documentation." |
| 1237 | `frontend-mobile-security-xss-scan` | "Inspect frontend code for XSS injection points, unsafe DOM manipulation, and missing sanitization." |
| 1238 | `frontend-observability` | "A portable, framework-agnostic field-side observability pattern for React or React Native integrations." |
| 1239 | `frontend-optimistic-mutations` | "A portable, framework-agnostic discipline for the write path of any React or React Native app using a query/cache layer." |
| 1240 | `frontend-security-coder` | Expert in secure frontend coding practices specializing in XSS prevention, output sanitization, and client-side security patterns. |
| 1241 | `frontend-seo` | "A portable, framework-agnostic SEO system for any React or React Native-for-web frontend." |
| 1242 | `frontend-slides` | Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. |
| 1243 | `frontend-slides-frontend-slides` | "Create stunning, animation-rich HTML presentations from scratch or by converting PowerPoint files. Use when the user wants to build a pr... |
| 1244 | `frontend-ui-dark-ts` | "A modern dark-themed React UI system using Tailwind CSS and Framer Motion. Designed for dashboards, admin panels, and data-rich applicat... |
| 1245 | `frontend-ui-engineering` | Builds production-quality UIs. Use when building or modifying user-facing interfaces. Use when creating components, implementing layouts,... |
| 1246 | `fsi-compliance-checker` | "Maps code, architecture, and infrastructure changes to specific control IDs in PCI-DSS v4.0.1 and MAS TRM (Singapore financial regulator... |
| 1247 | `full-output-enforcement` | "Use when a task requires exhaustive unabridged output, complete files, or strict prevention of placeholders and skipped code." |
| 1248 | `full-stack-orchestration-full-stack-feature` | "Use when working with full stack orchestration full stack feature" |
| 1249 | `fxmacrodata` | "Query FXMacroData for official-source macro indicators, release calendars, central-bank policy rates, FX rates and CFTC positioning acro... |
| 1250 | `game-audio` | Game audio principles. Sound design, music integration, adaptive audio systems. |
| 1251 | `game-design` | Game design principles. GDD structure, balancing, player psychology, progression. |
| 1252 | `game-development` | Game development orchestrator. Routes by platform, dimension, and engine fit (web 2D/3D, hybrid DOM+canvas, narrative tools). Use when st... |
| 1253 | `gamification-engine` | 'Gamification points register: player and department, points balance and points earned this month, level, badges, source module and last-... |
| 1254 | `gbp-local-seo-intent` | 'Google Business Profile register: element, primary and supporting keywords, search intent, landing page, post dates, review rating and r... |
| 1255 | `gcp-audit-logs` | Configure GCP Cloud Audit Logs for compliance. Set up log routing and BigQuery analysis. Use when auditing GCP activity. |
| 1256 | `gcp-cloud-functions` | Deploy serverless functions on Google Cloud Functions. Configure triggers and manage deployments. Use when implementing serverless worklo... |
| 1257 | `gcp-cloud-run` | Specialized skill for building production-ready serverless applications on GCP. Covers Cloud Run services (containerized), Cloud Run Func... |
| 1258 | `gcp-cloud-sql` | Provision Cloud SQL databases. Configure high availability, backups, and security. Use when deploying managed databases on GCP. |
| 1259 | `gcp-compute` | Manage Compute Engine instances and instance templates. Configure managed instance groups and preemptible VMs. Use when deploying compute... |
| 1260 | `gcp-gke` | Deploy and manage Google Kubernetes Engine clusters. Configure node pools, networking, and workload identity. Use when running Kubernetes... |
| 1261 | `gcp-networking` | Configure VPCs, firewall rules, and Cloud NAT. Implement shared VPC and private service connect. Use when designing GCP network infrastru... |
| 1262 | `gcp-secret-manager` | Secure secrets in Google Cloud Secret Manager. Configure IAM policies, integrate with GKE, and manage secret versions. Use when managing ... |
| 1263 | `gdb-cli` | "GDB debugging assistant for AI agents - analyze core dumps, debug live processes, investigate crashes and deadlocks with source code cor... |
| 1264 | `gdpr-compliance` | Implement GDPR data protection requirements. Configure consent management, data subject rights, and privacy by design. Use when processin... |
| 1265 | `gdpr-data-handling` | "Practical implementation guide for GDPR-oriented data-processing design, consent management, and privacy controls." |
| 1266 | `gemini-agents` | '''Ask Gemini'', ''have Gemini build or review this'': Google''s Antigravity CLI as a partner. It may break Google''s terms on a consumer... |
| 1267 | `gemini-api-dev` | "Use this skill when building applications with Gemini API hosted models, including Gemini and Gemma 4, working with multimodal content (... |
| 1268 | `gemini-api-integration` | "Use when integrating Google Gemini API into projects. Covers model selection, multimodal inputs, streaming, function calling, and produc... |
| 1269 | `gemini-deep-research` | "Run autonomous multi-step research with Google's Gemini Deep Research Agent: kick off a query, poll progress, and collect a cited report... |
| 1270 | `gemini-interactions-api` | "Build with the Gemini Interactions API for text, chat, multimodal generation, streaming, managed or background agents, function calling,... |
| 1271 | `gemini-live-api-dev` | "Use this skill when building real-time, bidirectional streaming applications with the Gemini Live API." |
| 1272 | `gemini-omni-flash-api` | "Use this skill for generative video editing, text-to-video, image-referenced video generation, and first-frame-to-video transition anima... |
| 1273 | `geminiignore-finops` | "Configure and optimize .geminiignore files for AI context window efficiency and token cost reduction (FinOps)." |
| 1274 | `generate-nanobanana` | "Generate and edit images/video with Google's Gemini media models (Nano Banana 2/Pro, Gemini Omni Flash), with cost-approval gates, refer... |
| 1275 | `geo-audit` | Full website GEO+SEO audit with parallel subagent delegation. |
| 1276 | `geo-brand-mentions` | Brand mention and authority scanner for AI visibility. |
| 1277 | `geo-citability` | AI citability scoring and optimization. |
| 1278 | `geo-compare` | Monthly delta tracking and progress reporting for GEO clients. |
| 1279 | `geo-content` | Content quality and E-E-A-T assessment for AI citability — evaluate experience, expertise, authoritativeness, trustworthiness, and conten... |
| 1280 | `geo-crawlers` | AI crawler access analysis. |
| 1281 | `geo-fundamentals` | "Generative Engine Optimization for AI search engines (ChatGPT, Claude, Perplexity)." |
| 1282 | `geo-keyword-expansion-tool` | "Geo Keyword Expansion Tool. Use when working with seed keyword and target locations." |
| 1283 | `geo-llmstxt` | Analyzes and generates llms.txt files -- a proposed convention for helping AI systems understand website structure and content. |
| 1284 | `geo-platform-optimizer` | Platform-specific AI search optimization — audit and optimize for Google AI Overviews, ChatGPT, Perplexity, Gemini, and Bing Copilot indi... |
| 1285 | `geo-proposal` | Auto-generate a professional, client-ready GEO service proposal from audit data. |
| 1286 | `geo-prospect` | CRM-lite for managing GEO agency prospects and clients. |
| 1287 | `geo-report` | Generate a professional, client-facing GEO report combining all audit results into a single deliverable with scores, findings, and priori... |
| 1288 | `geo-report-pdf` | Generate a professional PDF report from a GEO audit using pandoc + Chrome headless. |
| 1289 | `geo-schema` | Schema.org structured data audit and generation optimized for AI discoverability — detect, validate, and generate JSON-LD markup |
| 1290 | `geo-technical` | Technical SEO audit with GEO-specific checks — crawlability, indexability, security, performance, SSR, and AI crawler access |
| 1291 | `geoffrey-hinton` | "Agente que simula Geoffrey Hinton — Godfather of Deep Learning, Prêmio Turing 2018, coautor do trabalho de 1986 que popularizou backprop... |
| 1292 | `gestures` | Build drag, swipe, and sheet interactions that track the finger 1:1 and stay interruptible. Use when building or fixing anything the user... |
| 1293 | `get-seen-in-replies` | "Write a reply to someone else's tweet that is worth reading on its own. Use when someone asks what to reply, wants to grow by replying o... |
| 1294 | `getyoutubetranscript` | "Fetch YouTube transcripts in any caption language a video has, search YouTube, and list channel videos, Shorts, live streams, posts and ... |
| 1295 | `gh-attach` | "Upload and download GitHub user-attachments (screenshots, PDFs, zips, videos) from the terminal; use when asked to attach or embed a fil... |
| 1296 | `gh-image` | "Upload local images to GitHub and get canonical user-attachments embed URLs; use when asked to attach a screenshot to a PR, issue, or co... |
| 1297 | `gh-review-requests` | Fetch unread GitHub notifications for open PRs where review is requested from a specified team or opened by a team member. Use when asked... |
| 1298 | `gha-security-review` | "Review GitHub Actions workflows for exploitable vulnerabilities with concrete attack paths and harmless proof-of-concept sketches. Requi... |
| 1299 | `ghidra-reverse` | "Free/open reverse engineering with Ghidra (headless or GUI): decompilation, cross-references, scripting, and optional Ghidra MCP workflo... |
| 1300 | `ghost-qa` | "Run autonomous headless Playwright browser QA across Desktop, Tablet, and Mobile viewports to catch hydration, layout, overflow, and a11... |
| 1301 | `ghost-record` | "Record a React component interaction as a replayable Ghost Cursor demo. Use only when the user explicitly invokes ghost-record." |
| 1302 | `git-advanced-workflows` | "Master advanced Git techniques to maintain clean history, collaborate effectively, and recover from any situation with confidence." |
| 1303 | `git-commit-message` | "Generates conventional-commit messages from staged changes: type prefix + English imperative subject (≤50 chars) + optional body explain... |
| 1304 | `git-hooks-automation` | "Master Git hooks setup with Husky, lint-staged, pre-commit framework, and commitlint. Automate code quality gates, formatting, linting, ... |
| 1305 | `git-pr-review` | Generate a concise and structured PR description from commit history with minimal token usage |
| 1306 | `git-pr-workflows-git-workflow` | "Orchestrate review, tests, commits, branch pushes, and pull-request creation with parallel agents. Use when completed changes must move ... |
| 1307 | `git-pr-workflows-onboard` | "You are an **expert onboarding specialist and knowledge transfer architect** with deep experience in remote-first organizations, technic... |
| 1308 | `git-pr-workflows-pr-enhance` | "Improve pull request descriptions, reviewability, change scope, and supporting validation evidence." |
| 1309 | `git-pushing` | "Safely stage, commit, and push intended git changes with conventional commit messages. Use for ordinary non-release pushes when explicit... |
| 1310 | `git-workflow` | Implement Git branching strategies, PR workflows, and release management patterns. |
| 1311 | `git-workflow-and-versioning` | Structures git workflow practices. Use when making any code change. Use when committing, branching, resolving conflicts, or when you need... |
| 1312 | `github` | "Use the `gh` CLI for issues, pull requests, Actions runs, and GitHub API queries." |
| 1313 | `github-actions` | Build, test, and deploy applications using GitHub Actions workflows. |
| 1314 | `github-actions-advanced` | Design, debug, and harden GitHub Actions CI/CD workflows, including reusable workflows, matrix builds, self-hosted runners, OIDC authenti... |
| 1315 | `github-actions-debugger` | "Specialized skill for diagnosing, analyzing, and fixing failing GitHub Actions workflows by parsing run logs and pipeline definitions." |
| 1316 | `github-actions-templates` | "Production-ready GitHub Actions workflow patterns for testing, building, and deploying applications." |
| 1317 | `github-automation` | "Operate GitHub issues, pull requests, branches, checks, workflows, and permissions through Rube MCP. Use when GitHub work must be querie... |
| 1318 | `github-issue-creator` | "Turn error logs, screenshots, voice notes, and rough bug reports into crisp, developer-ready GitHub issues with repro steps, impact, and... |
| 1319 | `github-presence` | When the user wants to optimize their GitHub profile, README, or project discoverability. Trigger phrases include "GitHub README," "READM... |
| 1320 | `github-workflow-automation` | "Patterns for automating GitHub workflows with AI assistance, inspired by [Gemini CLI](https://github.com/google-gemini/gemini-cli) and m... |
| 1321 | `gitlab-automation` | "Automate GitLab project management, issues, merge requests, pipelines, branches, and user operations via Rube MCP (Composio). Always sea... |
| 1322 | `gitlab-ci` | Configure GitLab CI/CD pipelines and runners for automated building, testing, and deployment. |
| 1323 | `gitlab-ci-patterns` | "Comprehensive GitLab CI/CD pipeline patterns for automated testing, building, and deployment." |
| 1324 | `gitops-workflow` | "Complete guide to implementing GitOps workflows with ArgoCD and Flux for automated Kubernetes deployments." |
| 1325 | `glasser` | "Search, inspect, and run third-party data APIs through one CLI when the environment has no suitable integration." |
| 1326 | `global-chat-agent-discovery` | "Discover and compare MCP servers and AI agents using Global Chat's cross-protocol directory and MCP server." |
| 1327 | `gmail-automation` | "Lightweight Gmail integration with standalone OAuth authentication. No MCP server required." |
| 1328 | `gmb-optimization-helper` | "GMB Optimization Helper. Use when working with Google Business Profile details or business facts." |
| 1329 | `go-concurrency-patterns` | "Master Go concurrency with goroutines, channels, sync primitives, and context. Use when building concurrent Go applications, implementin... |
| 1330 | `go-in-depth` | Go in depth harness — fan-out web searches, fetch sources, adversarially verify claims, synthesize a cited report. |
| 1331 | `go-playwright` | "Expert capability for robust, stealthy, and efficient browser automation using Playwright Go." |
| 1332 | `go-rod-master` | "Comprehensive guide for browser automation and web scraping with go-rod (Chrome DevTools Protocol) including stealth anti-bot-detection ... |
| 1333 | `go-rust-reverse` | "Reverse engineer stripped Go and Rust binaries: runtime recognition, pclntab/module metadata recovery, panic-string analysis, and idioma... |
| 1334 | `goal-analyzer` | 分析健康目标数据、识别目标模式、评估目标进度,并提供个性化目标管理建议。支持与营养、运动、睡眠等健康数据的关联分析。 |
| 1335 | `goal-instruction-writer` | "Preview, draft, refine, or audit durable agent Goals with acceptance evidence, drift controls, proportional verification, and bounded wa... |
| 1336 | `goal-loop` | "Draft and explain persistent goal-loop prompts for long-running agent work with clear stop conditions." |
| 1337 | `godot-4-migration` | "Specialized guide for migrating Godot 3.x projects to Godot 4 (GDScript 2.0), covering syntax changes, Tweens, and exports." |
| 1338 | `godot-gdscript-patterns` | "Master Godot 4 GDScript patterns including signals, scenes, state machines, and optimization. Use when building Godot games, implementin... |
| 1339 | `golang-pro` | Master Go 1.21+ with modern patterns, advanced concurrency, performance optimization, and production-ready microservices. |
| 1340 | `google-analytics-automation` | "Automate Google Analytics tasks via Rube MCP (Composio): run reports, list accounts/properties, funnels, pivots, key events. Always sear... |
| 1341 | `google-calendar-automation` | "Plan and perform authorized Google Calendar workflows through an existing authenticated integration; inspect events, draft changes and v... |
| 1342 | `google-code-review` | "Review code or prepare a change for review using Google's engineering practices: reviewer and author modes, severity labels, CL descript... |
| 1343 | `google-docs-automation` | "Read and edit Google Docs through an available authenticated connector or reviewed API integration, with scoped changes and read-back ve... |
| 1344 | `google-drive-automation` | "Lightweight Google Drive integration with standalone OAuth authentication. No MCP server required. Full read/write access." |
| 1345 | `google-no-code` | "Design Google Forms and wire Apps Script triggers (onFormSubmit) for email alerts, spreadsheet logging, and dynamic questions — no code ... |
| 1346 | `google-sheets-automation` | "Read and edit Google Sheets through an available authenticated connector or reviewed API integration, with scoped changes and read-back ... |
| 1347 | `google-slides-automation` | "Read and edit Google Slides through an available authenticated connector or reviewed API integration, with scoped changes and read-back ... |
| 1348 | `googlesheets-automation` | "Automate Google Sheets operations (read, write, format, filter, manage spreadsheets) via Rube MCP (Composio). Read/write data, manage ta... |
| 1349 | `gpt-taste` | "Use when generating elite GSAP-heavy frontend pages with strict AIDA structure, wide hero typography, and gapless bento grids." |
| 1350 | `gpu-kubernetes-operations` | Operate GPU-backed Kubernetes clusters for AI inference and training with scheduling, autoscaling, node health, MIG partitioning, and cos... |
| 1351 | `gpu-server-management` | Set up and manage NVIDIA GPU servers for AI workloads |
| 1352 | `graceful-shutdown` | "Implement graceful shutdown for servers and workers: drain connections, finish in-flight work, release resources, and exit cleanly on SI... |
| 1353 | `grafana-dashboards` | "Create and manage production-ready Grafana dashboards for comprehensive system observability." |
| 1354 | `graphql` | GraphQL gives clients exactly the data they need - no more, no less. One endpoint, typed schema, introspection. But the flexibility that ... |
| 1355 | `graphql-architect` | Master modern GraphQL with federation, performance optimization, and enterprise security. Build scalable schemas, implement advanced cach... |
| 1356 | `graphql-schema` | GraphQL queries, mutations, and code generation patterns. Use when creating GraphQL operations, working with Apollo Client, or generating... |
| 1357 | `grill-me` | A relentless interview to sharpen a plan or design. |
| 1358 | `grill-with-docs` | A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go. |
| 1359 | `grilling` | Interview the user relentlessly about a plan or design. Use when the user wants to stress-test a plan before building, or uses any 'grill... |
| 1360 | `grok-agents` | '''Ask Grok'', ''have Grok build or review this'': drive the Grok CLI headless from another agent as a peer, builder or fresh reviewer.' |
| 1361 | `grok-build` | "Delegate well-specified implementation tasks to xAI's Grok Build CLI running headlessly while the orchestrating agent plans, writes task... |
| 1362 | `grok-delegate` | Delegate coding tasks to the Grok Build CLI only when the user explicitly requests it, while the orchestrator retains review and landing ... |
| 1363 | `growth-engine` | "Motor de crescimento para produtos digitais -- growth hacking, SEO, ASO, viral loops, email marketing, CRM, referral programs e aquisica... |
| 1364 | `growth-loops` | 'Designing how a product grows: loops that compound (viral, usage, collaboration, user-generated, referral).' |
| 1365 | `grpc-golang` | "Build production-ready gRPC services in Go with mTLS, streaming, and observability. Use when designing Protobuf contracts with Buf or im... |
| 1366 | `grpo-rlvr-training` | Train reasoning and verifiable-task behavior with GRPO and reinforcement learning from verifiable rewards (RLVR). Use when task success i... |
| 1367 | `gsap-core` | Official GSAP skill for the core API — gsap.to(), from(), fromTo(), easing, duration, stagger, defaults, gsap.matchMedia() (responsive, p... |
| 1368 | `gsap-frameworks` | Official GSAP skill for Vue, Svelte, and other non-React frameworks — lifecycle, scoping selectors, cleanup on unmount. Use when the user... |
| 1369 | `gsap-performance` | Official GSAP skill for performance — prefer transforms, avoid layout thrashing, will-change, batching. Use when optimizing GSAP animatio... |
| 1370 | `gsap-plugins` | Official GSAP skill for GSAP plugins — registration, ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, Scram... |
| 1371 | `gsap-react` | Official GSAP skill for React — useGSAP hook, refs, gsap.context(), cleanup. Use when the user wants animation in React or Next.js, or as... |
| 1372 | `gsap-scrolltrigger` | Official GSAP skill for ScrollTrigger — scroll-linked animations, pinning, scrub, triggers. Use when building or recommending scroll-base... |
| 1373 | `gsap-timeline` | Official GSAP skill for timelines — gsap.timeline(), position parameter, nesting, playback. Use when sequencing animations, choreographin... |
| 1374 | `gsap-utils` | Official GSAP skill for gsap.utils — clamp, mapRange, normalize, interpolate, random, snap, toArray, wrap, pipe. Use when the user asks a... |
| 1375 | `guardrail-hooks` | 'An agent keeps breaking a rule (''it did it again'', ''make this impossible'', ''add a hook'', ''my hook didn''t fire''): make it a hook... |
| 1376 | `guest-posting-opportunity-finder` | "Guest Posting Opportunity Finder. Use when working with topic, audience and optional prospect list." |
| 1377 | `handoff` | Compact the current conversation into a handoff document for another agent to pick up. |
| 1378 | `handover` | Write a concise agent handover with task state, exact workspace, evidence, open decisions and the next safe step. |
| 1379 | `hardware-security` | "Authorized hardware and embedded interface security research: UART/JTAG discovery, debug-pad triage, secure-boot overview, and offline f... |
| 1380 | `harvey-specter` | "Prepare negotiations, difficult conversations, and leadership replies with evidence, clear boundaries, relationship-aware tone, and Harv... |
| 1381 | `hasdata` | Use HasData APIs for web scraping and structured web data extraction. |
| 1382 | `hasdata-cli` | Command-line access to search, scraping, and structured web data. |
| 1383 | `hashicorp-vault` | Manage secrets and PKI with HashiCorp Vault. |
| 1384 | `haskell-pro` | "Design and review Haskell types, pure domain logic, parsing, exception-safe concurrency, Cabal/Stack builds and measured performance." |
| 1385 | `heading-analyzer` | "Heading Analyzer. Use when working with HTML, Markdown or extracted headings." |
| 1386 | `headline-analyzer` | "Headline Analyzer. Use when working with headline and intended article summary." |
| 1387 | `headline-psychologist` | "Draft and compare audience-aware headlines when copy needs clearer relevance and curiosity without clickbait or unsupported promises." |
| 1388 | `health-trend-analyzer` | 分析一段时间内健康数据的趋势和模式。关联药物、症状、生命体征、化验结果和其他健康指标的变化。识别令人担忧的趋势、改善情况，并提供数据驱动的洞察。当用户询问健康趋势、模式、随时间的变化或"我的健康状况有什么变化？"时使用。支持多维度分析（体重/BMI、症状、药物依从性、化验结... |
| 1389 | `health-wellness` | 'Wellbeing check-in register: anonymous flag, department, check-in date, wellbeing score, stress and energy levels, support and resource ... |
| 1390 | `healthcare-job-search` | "Find open US healthcare jobs (nursing, CNA, allied health, therapy, imaging, pharmacy, physicians) and the hourly pay employers post, vi... |
| 1391 | `helium-mcp` | "Connect to Helium's MCP server for news research, media bias analysis, balanced perspectives, stock/options data, and semantic meme sear... |
| 1392 | `helm-chart-scaffolding` | "Comprehensive guidance for creating, organizing, and managing Helm charts for packaging and deploying Kubernetes applications." |
| 1393 | `helm-charts` | Create, manage, and deploy Helm charts for Kubernetes package management. |
| 1394 | `helpdesk-automation` | "Automate HelpDesk tasks via Rube MCP (Composio): list tickets, manage views, use canned responses, and configure custom fields. Always s... |
| 1395 | `hf-cli` | Curated upstream guidance for Hf Cli; use when the workflow matches the user goal. |
| 1396 | `hf-cloud-aws-context-discovery` | "Discover the effective local AWS profile, region, account, and caller identity before any AWS task without exposing credentials." |
| 1397 | `hf-mcp` | Use Hugging Face Hub via MCP server tools. Search models, datasets, Spaces, papers. Get repo details, fetch documentation, run compute jo... |
| 1398 | `hf-mem` | Hugging Face CLI to estimate the required memory to load Safetensors or GGUF model weights for inference from the Hugging Face Hub |
| 1399 | `hierarchical-agent-memory` | "Scoped CLAUDE.md memory system that reduces context token spend. Creates directory-level context files, tracks savings via dashboard, an... |
| 1400 | `hig-components-content` | Apple Human Interface Guidelines for content display components. |
| 1401 | `hig-components-controls` | "Choose and review Apple selection and input controls: toggles, segmented controls, sliders, pickers, steppers, text fields, labels and k... |
| 1402 | `hig-components-dialogs` | Apple HIG guidance for presentation components including alerts, action sheets, popovers, sheets, and digit entry views. |
| 1403 | `hig-components-layout` | Apple Human Interface Guidelines for layout and navigation components. |
| 1404 | `hig-components-menus` | "Design Apple-platform menus, buttons, toolbars and disclosure controls using the appropriate platform conventions, command hierarchy and... |
| 1405 | `hig-components-search` | Apple HIG guidance for navigation-related components including search fields, page controls, and path controls. |
| 1406 | `hig-components-status` | Apple HIG guidance for status and progress UI components including progress indicators, status bars, and activity rings. |
| 1407 | `hig-components-system` | 'Apple HIG guidance for system experience components: widgets, live activities, notifications, complications, home screen quick actions, ... |
| 1408 | `hig-foundations` | Apple Human Interface Guidelines design foundations. |
| 1409 | `hig-inputs` | "Design Apple-platform input interactions for touch, keyboard, pointer, Pencil, controllers, spatial gestures and supported device sensor... |
| 1410 | `hig-patterns` | Apple Human Interface Guidelines interaction and UX patterns. |
| 1411 | `hig-platforms` | Apple Human Interface Guidelines for platform-specific design. |
| 1412 | `hig-project-context` | Create or update a shared Apple design context document that other HIG skills use to tailor guidance. |
| 1413 | `hig-technologies` | "Review Apple-platform technology UX against HIG patterns for payments, health data, identity, Siri, AR, cloud sync, and shared experienc... |
| 1414 | `high-end-visual-design` | "Use when designing expensive agency-grade interfaces with premium fonts, spatial rhythm, soft depth, and fluid microinteractions." |
| 1415 | `hipaa-compliance` | Implement HIPAA security and privacy rules. Configure PHI protections and BAA requirements. Use when handling healthcare data. |
| 1416 | `honest-link-outreach` | Build a qualified editorial outreach list and draft plain-text backlink requests grounded in public business relationships and page relev... |
| 1417 | `hono` | "Build ultra-fast web APIs and full-stack apps with Hono — runs on Cloudflare Workers, Deno, Bun, Node.js, and any WinterCG-compatible ru... |
| 1418 | `hosted-agents` | Build background agents in sandboxed environments. Use for hosted coding agents, sandboxed VMs, Modal sandboxes, and remote coding enviro... |
| 1419 | `hosted-agents-v2-py` | "Build hosted agents using Azure AI Projects SDK with HostedAgentDefinition. Use when creating container-based agents in Azure AI Foundry." |
| 1420 | `hr-pro` | Professional, ethical HR partner for hiring, onboarding/offboarding, PTO and leave, performance, compliant policies, and employee relations. |
| 1421 | `hreflang-tag-generator` | "Hreflang Tag Generator. Use when working with equivalent page URLs mapped to language and optional region." |
| 1422 | `html-injection-testing` | "Identify and exploit HTML injection vulnerabilities that allow attackers to inject malicious HTML content into web applications. This vu... |
| 1423 | `http-status-code-tester` | "HTTP Status Code Tester. Use when working with one or more HTTP(S) URLs." |
| 1424 | `hubspot-automation` | "Automate HubSpot CRM operations (contacts, companies, deals, tickets, properties) via Rube MCP using Composio integration." |
| 1425 | `hubspot-integration` | Expert patterns for HubSpot CRM integration including OAuth authentication, CRM objects, associations, batch operations, webhooks, and cu... |
| 1426 | `hugging-face-cli` | "Hugging Face Hub CLI (`hf`) for downloading, uploading, and managing models, datasets, spaces, buckets, repos, papers, jobs, and more on... |
| 1427 | `hugging-face-community-evals` | "Run evaluations for Hugging Face Hub models using inspect-ai and lighteval on local hardware. Use for backend selection, local GPU evals... |
| 1428 | `hugging-face-dataset-viewer` | Hugging Face Dataset Viewer |
| 1429 | `hugging-face-datasets` | Create and manage datasets on Hugging Face Hub. Supports initializing repos, defining configs/system prompts, streaming row updates, and ... |
| 1430 | `hugging-face-evaluation` | Add and manage evaluation results in Hugging Face model cards. Supports extracting eval tables from README content, importing scores from... |
| 1431 | `hugging-face-gradio` | Build Gradio web UIs and demos in Python. Use when creating or editing Gradio apps, components, event listeners, layouts, or chatbots. |
| 1432 | `hugging-face-jobs` | Run workloads on Hugging Face Jobs with managed CPUs, GPUs, TPUs, secrets, and Hub persistence. |
| 1433 | `hugging-face-model-trainer` | "Train or fine-tune language and vision models using TRL (Transformer Reinforcement Learning) or Unsloth with Hugging Face Jobs infrastru... |
| 1434 | `hugging-face-paper-publisher` | Publish and manage research papers on Hugging Face Hub. Supports creating paper pages, linking papers to models/datasets, claiming author... |
| 1435 | `hugging-face-papers` | "Look up and read Hugging Face paper pages in markdown, and use the papers API for structured metadata such as authors, linked models/dat... |
| 1436 | `hugging-face-tool-builder` | "Your purpose is now is to create reusable command line scripts and utilities for using the Hugging Face API, allowing chaining, piping a... |
| 1437 | `hugging-face-trackio` | "Track and visualize ML training experiments with Trackio. Use when logging metrics during training (Python API), firing alerts for train... |
| 1438 | `hugging-face-vision-trainer` | "Train object detection, image classification, and SAM or SAM2 segmentation models locally or on Hugging Face Jobs, with bounded dataset ... |
| 1439 | `huggingface-best` | "Use when the user asks about finding the best, top, or recommended model for a task, wants to know what AI model to use, or wants to com... |
| 1440 | `huggingface-community-evals` | Curated upstream guidance for Huggingface Community Evals; use when the workflow matches the user goal. |
| 1441 | `huggingface-datasets` | Use this skill for Hugging Face Dataset Viewer API workflows that fetch subset/split metadata, paginate rows, search text, apply filters,... |
| 1442 | `huggingface-llm-trainer` | Train or fine-tune language and vision models using TRL (Transformer Reinforcement Learning) or Unsloth with Hugging Face Jobs infrastruc... |
| 1443 | `huggingface-local-models` | Use to select models to run locally with llama.cpp and GGUF on CPU, Mac Metal, CUDA, or ROCm. Covers finding GGUFs, quant selection, runn... |
| 1444 | `huggingface-lora-space-builder` | "Build and publish a Gradio demo on Hugging Face Spaces for a user-provided LoRA." |
| 1445 | `huggingface-spaces` | "Build, deploy, and maintain applications on Hugging Face Spaces — Gradio / Docker / Static SDKs, ZeroGPU and dedicated hardware, model l... |
| 1446 | `huggingface-tool-builder` | "Use this skill when the user wants to build tool/scripts or achieve a task where using data from the Hugging Face API would help. This i... |
| 1447 | `huggingface-zerogpu` | "AI demos and GPU compute with Gradio Spaces and Hugging Face Spaces ZeroGPU." |
| 1448 | `hugo-to-markdown` | "Convert Hugo documentation sites and Hugo-managed content into standard Markdown." |
| 1449 | `humanize-chinese` | Detect and rewrite AI-like Chinese text with a practical workflow for scoring, humanization, academic AIGC reduction, and style conversio... |
| 1450 | `hunt-api-misconfig` | Hunt API security misconfiguration |
| 1451 | `hunt-aspnet` | Hunt ASP.NET-specific surface |
| 1452 | `hunt-ato` | Hunt account takeover taxonomy |
| 1453 | `hunt-auth-bypass` | Hunting skill for auth bypass vulnerabilities. |
| 1454 | `hunt-brute-force` | Hunt Missing/Weak Rate Limiting |
| 1455 | `hunt-business-logic` | Hunting skill for business logic vulnerabilities. |
| 1456 | `hunt-cache-poison` | Hunting skill for cache poison vulnerabilities. |
| 1457 | `hunt-captcha-bypass` | Hunt CAPTCHA Bypass |
| 1458 | `hunt-cicd` | Hunt CI/CD pipeline vulnerabilities |
| 1459 | `hunt-clickjacking` | Hunt Clickjacking |
| 1460 | `hunt-cloud-misconfig` | Hunt cloud / infrastructure misconfigurations. |
| 1461 | `hunt-cors` | Hunt CORS Misconfiguration |
| 1462 | `hunt-csrf` | Hunting skill for csrf vulnerabilities. |
| 1463 | `hunt-deserialization` | Hunt Insecure Deserialization |
| 1464 | `hunt-dispatch` | Skill-set loader for /hunt orchestrator. |
| 1465 | `hunt-dom` | Hunt client-side DOM vulnerabilities |
| 1466 | `hunt-exceptional-conditions` | Hunt mishandling of exceptional conditions |
| 1467 | `hunt-file-upload` | Hunt file upload bugs |
| 1468 | `hunt-fintech-graphql` | Hunt fintech-specific GraphQL vulnerabilities |
| 1469 | `hunt-forgot-password` | Hunt Forgot Password / Account Recovery Authentication Flaws |
| 1470 | `hunt-graphql` | Hunting skill for graphql vulnerabilities. |
| 1471 | `hunt-grpc` | Hunt gRPC vulnerabilities |
| 1472 | `hunt-host-header` | Hunt Host Header Injection |
| 1473 | `hunt-html-injection` | Hunt HTML Injection |
| 1474 | `hunt-http-smuggling` | Hunt HTTP request smuggling (CL.TE, TE.CL, H2.CL, H2.TE). |
| 1475 | `hunt-idor` | Hunting skill for idor vulnerabilities. Built from 26 public bug bounty reports. Use when hunting idor on any target. |
| 1476 | `hunt-jwt-crypto` | Hunt JWT cryptographic failures |
| 1477 | `hunt-k8s` | Hunt Kubernetes & Docker |
| 1478 | `hunt-laravel` | Hunt Laravel specific vulnerabilities |
| 1479 | `hunt-ldap` | Hunt LDAP Injection and XPath Injection |
| 1480 | `hunt-lfi` | Hunt Local File Inclusion (LFI), Remote File Inclusion (RFI), and Path Traversal |
| 1481 | `hunt-llm-ai` | Hunt LLM/AI feature bugs |
| 1482 | `hunt-mfa-bypass` | Hunt MFA / 2FA bypass |
| 1483 | `hunt-misc` | Hunting skill for misc vulnerabilities. Reference for authorized role, token and workflow-boundary reviews. Historical source count is no... |
| 1484 | `hunt-nextjs` | Hunt Next.js specific vulnerabilities |
| 1485 | `hunt-nodejs` | Hunt Node.js specific vulnerabilities |
| 1486 | `hunt-nosqli` | Hunt NoSQL Injection |
| 1487 | `hunt-ntlm-info` | Hunt NTLM/Negotiate information disclosure on internet-reachable IIS/SharePoint/Exchange. |
| 1488 | `hunt-oauth` | Hunting skill for oauth vulnerabilities. Built from 19 public bug bounty reports. Use when hunting oauth on any target. |
| 1489 | `hunt-open-redirect` | Hunt Open Redirect |
| 1490 | `hunt-race-condition` | Hunting skill for race condition vulnerabilities. |
| 1491 | `hunt-rag-vector` | Hunt vector-store / embedding-layer weaknesses in RAG pipelines (OWASP LLM08 Vector and Embedding Weaknesses) |
| 1492 | `hunt-rce` | Hunting skill for rce vulnerabilities. Built from 67 public bug bounty reports. Use when hunting rce on any target. |
| 1493 | `hunt-saml` | Hunt SAML / SSO attacks. |
| 1494 | `hunt-session` | Hunt Session Management vulnerabilities |
| 1495 | `hunt-shadow-api` | Hunt shadow / zombie / undocumented API surface (OWASP API9 Improper Inventory Management) |
| 1496 | `hunt-sharepoint` | Hunt Microsoft SharePoint Server (2013/2016/2019/Subscription Edition) on-prem farms |
| 1497 | `hunt-source-leak` | Hunt source code and build artifact leakage |
| 1498 | `hunt-spa-api` | Discover a single-page-app's hidden backend API from its public JS bundle, then test that API for broken access control / missing authent... |
| 1499 | `hunt-springboot` | Hunt Spring Boot specific vulnerabilities |
| 1500 | `hunt-sqli` | Hunting skill for sqli vulnerabilities. |
| 1501 | `hunt-ssrf` | Hunting skill for ssrf vulnerabilities. |
| 1502 | `hunt-ssti` | Hunt server-side template injection (SSTI) across Jinja2 (Flask/Django), Twig (Symfony), Freemarker (Java), ERB (Rails), Spring, Velocity... |
| 1503 | `hunt-subdomain` | Hunting skill for subdomain takeover vulnerabilities. |
| 1504 | `hunt-tls-network` | Hunt TLS/SSL and DNS misconfigurations |
| 1505 | `hunt-websocket` | Hunt WebSocket vulnerabilities |
| 1506 | `hunt-xss` | Hunting skill for xss vulnerabilities. |
| 1507 | `hunt-xxe` | Hunting skill for xxe vulnerabilities. |
| 1508 | `huntapi-mcp` | "Read media metadata, or download video and audio the user has the rights to, from public media URLs through HuntAPI's MCP server and its... |
| 1509 | `hybrid-cloud-architect` | Expert hybrid cloud architect specializing in complex multi-cloud solutions across AWS/Azure/GCP and private clouds (OpenStack/VMware). |
| 1510 | `hybrid-cloud-networking` | "Configure secure, high-performance connectivity between on-premises and cloud environments using VPN, Direct Connect, and ExpressRoute." |
| 1511 | `hybrid-search-implementation` | "Combine vector and keyword search for improved retrieval. Use when implementing RAG systems, building search engines, or when neither ap... |
| 1512 | `hyperexecute-skill` | "Operates HyperExecute end-to-end for TestMu AI/LambdaTest cloud test execution: analyze projects, create YAML, validate locally, run CLI... |
| 1513 | `hyperframes` | "Create and review editable HTML-to-video projects with the HyperFrames timeline, composition and rendering contract." |
| 1514 | `hyperframes-cli` | "Scaffold, inspect, preview and render HyperFrames projects; use local or explicitly authorized hosted workflows." |
| 1515 | `hyperframes-registry` | "Find and integrate editable HyperFrames blocks and components for video scenes, transitions and effects." |
| 1516 | `i-have-adhd` | 'Shape output for ADHD readers: next action first, numbered steps, restated state, no tangents, time estimates, visible wins. Toggle with... |
| 1517 | `i18n-localization` | "Internationalization and localization patterns. Detecting hardcoded strings, managing translations, locale files, RTL support." |
| 1518 | `iconsax-library` | Extensive icon library and AI-driven icon generation skill for premium UI/UX design. |
| 1519 | `ida-reverse` | "Reverse engineer binaries with IDA Pro: decompilation, disassembly, data-flow tracking, cross-references, and IDA MCP automation for dee... |
| 1520 | `idea-autopsy` | "Autopsy a business idea before you build it: kill-list check, five hard filters, a free-AI one-prompt test, live ad-market verification,... |
| 1521 | `idea-darwin` | "Darwinian idea evolution engine — toss rough ideas onto an evolution island, let them compete, crossbreed, and mutate through structured... |
| 1522 | `idea-evaluator` | "Evaluates an idea by hosting a multi-turn debate between a Pro and Con agent, delivering a final verdict on whether it's worth pursuing." |
| 1523 | `idea-os` | "Five-phase pipeline (triage → clarify → research → PRD → plan) that turns a raw idea into four linked files: clarifying questions, deep ... |
| 1524 | `idea-refine` | "Refines raw ideas into sharp, actionable concepts through structured divergent and convergent thinking. Use when an idea is still vague,... |
| 1525 | `idea-to-blueprint` | "Turn a raw product, app, bot or feature idea into one evidence-backed build blueprint (researched stack, epics, Given/When/Then criteria... |
| 1526 | `identity-access-management` | Set up and manage SSO, SCIM provisioning, and MFA for startup teams using Google Workspace, Okta, or Azure AD. |
| 1527 | `identity-federation` | "Authorized assessment of federated identity systems: SAML, OIDC, OAuth2 flows, SSO misconfiguration, and token-confusion issues." |
| 1528 | `identity-mirror` | "Map an audience's current and aspirational identity into credible messaging when copy needs stronger personal relevance." |
| 1529 | `idor-testing` | "Provide systematic methodologies for identifying and exploiting Insecure Direct Object Reference (IDOR) vulnerabilities in web applicati... |
| 1530 | `ii-commons` | "Deterministic search across arXiv, PubMed/PMC, and US policy corpora with daily freshness cutoffs." |
| 1531 | `illyism-intro` | Write short, Semrush-style blog post intros with journey teasers, practical relevance, and reader intent matching. Use when the user asks... |
| 1532 | `ilya-sutskever` | "Agente que simula Ilya Sutskever — co-fundador da OpenAI, ex-Chief Scientist, fundador da SSI. Use quando quiser perspectivas sobre: AGI... |
| 1533 | `image-alt-tag-generator` | "Image Alt Tag Generator. Use when working with image or accurate image description and page context." |
| 1534 | `image-generator` | Generate and edit images using Gemini's Nano Banana Pro model (gemini-3-pro-image-preview). Use this skill when the user asks you to gene... |
| 1535 | `image-studio` | "Studio de geracao de imagens inteligente — roteamento automatico entre ai-studio-image (fotos humanizadas/influencer) e stability-ai (ar... |
| 1536 | `imagen` | "AI image generation skill powered by Google Gemini, enabling seamless visual content creation for UI placeholders, documentation, and de... |
| 1537 | `imagera-media` | "Generate or edit images, video clips, voiceovers and music through the hosted Imagera MCP server, quoting the credit cost and getting ap... |
| 1538 | `impeccable` | "Use when the user wants to design, redesign, shape, critique, audit, polish, simplify, harden, animate, or otherwise improve a frontend ... |
| 1539 | `implement` | Implement a piece of work based on a PRD or set of issues. |
| 1540 | `impress` | "Presentation creation, format conversion (ODP/PPTX/PDF), slide automation with LibreOffice Impress." |
| 1541 | `impression-to-click-ratio-calculator` | "Impression-to-Click Ratio Calculator. Use when working with clicks and impressions for the same scope." |
| 1542 | `improve-animations` | "Audit existing motion and write prioritized implementation plans with exact evidence, scope, and verification steps." |
| 1543 | `improve-codebase-architecture` | Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick. |
| 1544 | `incident-management` | Implement incident management processes and escalation procedures. Configure on-call schedules and post-incident reviews. Use when managi... |
| 1545 | `incident-responder` | Expert SRE incident responder specializing in rapid problem resolution, modern observability, and comprehensive incident management. |
| 1546 | `incident-response` | Handle security incidents with IR playbooks and procedures. |
| 1547 | `incident-response-incident-response` | "Use when working with incident response incident response" |
| 1548 | `incident-response-smart-fix` | "Investigate production issues, reproduce root causes, implement scoped fixes, and verify recovery using tests and observability." |
| 1549 | `incident-runbook-templates` | "Adaptable templates for incident response runbooks covering detection, triage, mitigation, resolution, and communication." |
| 1550 | `incremental-implementation` | Delivers changes incrementally. Use when implementing any feature or change that touches more than one file. Use when you're about to wri... |
| 1551 | `independent-review` | 'Before ''ship it'', a deploy or release, for ''an independent review'', and after each fix until a round is clean: a fresh reviewer that... |
| 1552 | `indexing-issue-auditor` | "High-level technical SEO and site architecture auditor. Invoke to scan local or live environments for indexing, crawl budget, and struct... |
| 1553 | `industrial-brutalist-ui` | "Use when creating raw industrial or tactical telemetry UIs with rigid grids, stark typography, CRT effects, and high-density data." |
| 1554 | `infinite-gratitude` | "Plan and synthesize multi-perspective research; use parallel agents only when authorized and verify findings against sources." |
| 1555 | `infinity` | "Enforces a strict input boundary protocol (detect, classify, filter, verify) to ensure untrusted data never reaches business logic raw." |
| 1556 | `ingest-youtube` | "Pull a YouTube video transcript into a queryable markdown vault with yt-dlp subtitle discovery, VTT cleanup, metadata frontmatter, and c... |
| 1557 | `inngest` | Inngest expert for serverless-first background jobs, event-driven workflows, and durable execution without managing queues or workers. |
| 1558 | `instagram` | Integracao completa com Instagram via Graph API. Publicacao, analytics, comentarios, DMs, hashtags, agendamento, templates e gestao de co... |
| 1559 | `instagram-automation` | "Automate Instagram tasks via Rube MCP (Composio): create posts, carousels, manage media, get insights, and publishing limits. Always sea... |
| 1560 | `instructree` | "Map, explain, and lint repository-scoped coding-agent instructions before changing code." |
| 1561 | `intended-vs-implemented` | 'Auditing AI-built code against its docs: where it does what the docs or permissions don''t say, access control against documented roles,... |
| 1562 | `interactive-portfolio` | Expert in building portfolios that actually land jobs and clients - not just showing work, but creating memorable experiences. Covers dev... |
| 1563 | `intercom-automation` | "Automate Intercom tasks via Rube MCP (Composio): conversations, contacts, companies, segments, admins. Always search tools first for cur... |
| 1564 | `interface-review` | Reviews a branch, pull request or uncommitted change for the interface problems it introduced or regressed, across accessibility, layout,... |
| 1565 | `intern-program` | 'Internship register: intern and department, supervisor and mentor, institution, start and end dates, stipend, learning goals, mid-term a... |
| 1566 | `internal-comms` | "Write internal communications such as status reports, leadership updates, 3P updates, newsletters, FAQs, incident reports, and project u... |
| 1567 | `internal-comms-anthropic` | "Compatibility alias for internal-comms: draft status updates, newsletters and FAQs from approved sources." |
| 1568 | `internal-comms-community` | "Compatibility alias for internal-comms: draft status updates, newsletters and FAQs from approved sources." |
| 1569 | `internal-communication` | 'Internal communication log: title, type, date, department, host and attendees, agenda, action items, follow-up date, meeting link and de... |
| 1570 | `internal-link-suggestion-tool` | "Internal Link Suggestion Tool. Use when working with source text and available destination pages." |
| 1571 | `internal-linking` | Audit contextual inbound links, find underlinked commercial pages and verify targeted internal-link edits with a static route graph. |
| 1572 | `internal-linking-planner` | "Internal Linking Planner. Use when working with site page inventory and priority user journeys." |
| 1573 | `interview-coach` | "Full job search coaching system — JD decoding, resume, storybank, mock interviews, transcript analysis, comp negotiation. Coaching guide... |
| 1574 | `interview-me` | Draw out what the user actually wants with one-question-at-a-time interviews until intent is clear — before any plan, spec, or code exists. |
| 1575 | `interview-style-doc-building` | "Build structured strategy documents by asking one question at a time and patching the file." |
| 1576 | `invariant-guard` | "Correctness-first: forces writing the function contract, loop invariant, termination argument, and edge cases BEFORE code. Catches Boyer... |
| 1577 | `inventory-demand-planning` | Codified expertise for demand forecasting, safety stock optimisation, replenishment planning, and promotional lift estimation at multi-lo... |
| 1578 | `inventory-stock-reconciliation` | 'Stock reconciliation register: count date, item, warehouse, book vs physical quantity, variance quantity and value, variance reason, dam... |
| 1579 | `invoices-billing` | 'Invoice and billing register: invoice number, client, project, issue and due dates, subtotal, discount, tax and withholding, total, paym... |
| 1580 | `invokely-statistics` | "Use Invokely MCP to find official statistics, retrieve values and series, compare or rank places, and report each figure with its period... |
| 1581 | `ios-debugger-agent` | Debug the current iOS project on a booted simulator with XcodeBuildMCP. |
| 1582 | `ios-developer` | Develop native iOS applications with Swift/SwiftUI. Masters iOS 18, SwiftUI, UIKit integration, Core Data, networking, and App Store opti... |
| 1583 | `ios-flows` | "Plan an iPhone app flow from how real apps handle it: onboarding, sign-up, paywalls, permissions, cancellation, account deletion and set... |
| 1584 | `ios-redteam-pipeline` | End-to-end iOS red-team pipeline |
| 1585 | `ios-review` | "Review an iPhone app screen or flow and list what to fix, most important first: navigation, layout, touch targets, accessibility, states... |
| 1586 | `ios-screens` | "Build iPhone app screens that feel native: navigation, sheets, Dynamic Type, dark mode, permissions and paywalls, checked on small and l... |
| 1587 | `iso27001-compliance` | Implement ISO 27001 Information Security Management System. Configure ISMS controls and risk management. Use when implementing enterprise... |
| 1588 | `issue-grievance-tracker` | 'Grievance register: issue type, raised by or anonymous, person or team concerned, department, date raised, policy reference, severity, a... |
| 1589 | `issues` | Interact with GitHub issues - create, list, and view issues. |
| 1590 | `istio-traffic-management` | "Comprehensive guide to Istio traffic management for production service mesh deployments." |
| 1591 | `it-manager-hospital` | World-class Hospital IT Management Advisor specializing in clinical safety, digital maturity (HIMSS/ONA/JCI), and HIS/PEP ecosystems. |
| 1592 | `it-manager-pro` | Elite IT Management Advisor specializing in data-driven strategy, executive communication, and human-centric leadership for the 2026 digi... |
| 1593 | `iterate-pr` | Iterate on a PR until CI passes. Use when you need to fix CI failures, address review feedback, or continuously push fixes until all chec... |
| 1594 | `itil-expert` | Expert advisor for ITIL 4 and ITIL 5 (2026 digital product paradigm), specialized in AI-native governance, sustainability, and value co-c... |
| 1595 | `java-pro` | Master Java 21+ with modern features like virtual threads, pattern matching, and Spring Boot 3.x. Expert in the latest Java ecosystem inc... |
| 1596 | `javascript-mastery` | "33+ essential JavaScript concepts every developer should know, inspired by [33-js-concepts](https://github.com/leonardomso/33-js-concept... |
| 1597 | `javascript-pro` | Master modern JavaScript with ES6+, async patterns, and Node.js APIs. Handles promises, event loops, and browser/Node compatibility. |
| 1598 | `javascript-testing-patterns` | "Comprehensive guide for implementing robust testing strategies in JavaScript/TypeScript applications using modern testing frameworks and... |
| 1599 | `javascript-typescript-typescript-scaffold` | "Scaffold TypeScript projects with build tooling, type checking, testing, and configuration." |
| 1600 | `jenkins` | Create and manage Jenkins CI/CD pipelines, configure agents, manage plugins, and automate builds. |
| 1601 | `jest-skill` | "Generates Jest unit and integration tests in JavaScript or TypeScript. Covers mocking, snapshots, async testing, and React component tes... |
| 1602 | `jet-browser` | "Verify or integrate Jet Browser when a project needs isolated WPE WebKit sessions, native input, screenshots, ordered JSONL automation, ... |
| 1603 | `jev-memory` | "Set up an explicitly requested Claude Code memory mod using Treg and Jev, with informed consent for prompt transmission, recurring charg... |
| 1604 | `jev-social` | "Run read-only, browser-grounded Instagram, TikTok, or LinkedIn research through Jev routing and socai CLI, returning source-linked evide... |
| 1605 | `jev-use` | "Route enumerable judgment steps - did it work, which option, how risky, is this safe to run - to the Jev judgment model through the jev_... |
| 1606 | `jira-automation` | "Automate Jira tasks via Rube MCP (Composio): issues, projects, sprints, boards, comments, users. Always search tools first for current s... |
| 1607 | `jobgpt` | "Job search automation, auto apply, resume generation, application tracking, salary intelligence, and recruiter outreach using the JobGPT... |
| 1608 | `jobs-to-be-done-analyst` | "Uncover the functional, emotional and social jobs a customer hires a product to do: progress state, hiring trigger, alternatives, succes... |
| 1609 | `jq` | "Expert jq usage for JSON querying, filtering, transformation, and pipeline integration. Practical patterns for real shell workflows." |
| 1610 | `js-reverse` | "Front-end JavaScript reverse engineering: locate signature chains, analyze encrypted request parameters, sample runtime behavior, and re... |
| 1611 | `json-canvas` | Create and edit JSON Canvas files (.canvas) with nodes, edges, groups, and connections. Use when working with .canvas files, creating vis... |
| 1612 | `json-schema-manual` | 'JSON Schema Manual: draft 2020-12 validation schema from a confirmed field list, with required and enum values only where confirmed. Use... |
| 1613 | `julia-pro` | Master Julia 1.10+ with modern features, performance optimization, multiple dispatch, and production-ready practices. |
| 1614 | `junit-5-skill` | "Generates production-grade JUnit 5 unit and integration tests in Java. Covers assertions, parameterized tests, lifecycle hooks, mocking ... |
| 1615 | `junta-leiloeiros` | Consulta e coleta assistida de registros públicos de leiloeiros nas 27 rotas estaduais; cobertura e atualidade exigem validação. Scraper ... |
| 1616 | `k6-load-testing` | "Comprehensive k6 load testing skill for API, browser, and scalability testing. Write realistic load scenarios, analyze results, and inte... |
| 1617 | `k8s-manifest-generator` | "Step-by-step guidance for creating production-ready Kubernetes manifests including Deployments, Services, ConfigMaps, Secrets, and Persi... |
| 1618 | `k8s-security-policies` | "Guide for NetworkPolicy, RBAC, and Pod Security Admission/Standards (PodSecurityPolicy was removed in Kubernetes1.25) in Kubernetes." |
| 1619 | `kaggle-cli` | Use the local Kaggle CLI skill for command guidance, workflows, and troubleshooting across competitions, datasets, kernels/notebooks, mod... |
| 1620 | `kaizen` | "Guide for continuous improvement, error proofing, and standardization. Use this skill when the user wants to improve code quality, refac... |
| 1621 | `karpathy-guidelines` | Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, or refactoring code to avoid overcomplication, m... |
| 1622 | `keenable-search-mcp` | "Search the public web with site and date filters, and read pages with an extraction prompt, through Keenable's keyless MCP server. Use w... |
| 1623 | `keepmacawake` | "Keep a MacBook with Apple silicon awake with the lid closed during a long agent task, with the keepmacawake command of the Keep Mac Awak... |
| 1624 | `kernel-prompt` | "Use when composing or improving an LLM prompt or agent instruction. Asks one round of questions, then returns only the prompt; never per... |
| 1625 | `keyword-clustering-tool` | "Keyword Clustering Tool. Use when working with keyword list." |
| 1626 | `keyword-comparison-tool` | "Keyword Comparison Tool. Use when working with two or more keywords and optional metrics." |
| 1627 | `keyword-density-checker` | "Keyword Density Checker. Use when working with text and target word or phrase." |
| 1628 | `keyword-difficulty-estimator` | "Keyword Difficulty Estimator. Use when working with keyword plus supplied SERP or competitor evidence." |
| 1629 | `keyword-expansion-tool` | "Keyword Expansion Tool. Use when working with seed terms and optional industry." |
| 1630 | `keyword-extractor` | Extracts up to 50 highly relevant SEO keywords from text. Use when user wants to generate or extract keywords for given text. |
| 1631 | `keyword-gap-finder` | "Keyword Gap Finder. Use when working with your keyword set and competitor keyword sets." |
| 1632 | `keyword-intent-identifier` | "Keyword Intent Identifier. Use when working with keyword or query list." |
| 1633 | `keyword-placement-highlighter` | "Keyword Placement Highlighter. Use when working with text and target keywords." |
| 1634 | `keyword-roi-calculator` | "Keyword ROI Calculator. Use when working with traffic estimate, conversion rate, value per conversion, margin and SEO cost for one period." |
| 1635 | `keyword-share-estimator` | "Keyword Share Estimator. Use when working with comparable visibility values for your domain and selected competitors." |
| 1636 | `keyword-suggestion-tool` | "Keyword Suggestion Tool. Use when working with seed topic." |
| 1637 | `kimi-delegate` | Delegate coding tasks to the Kimi Code CLI (`kimi`) only when the user explicitly requests it, while the orchestrator retains review and ... |
| 1638 | `klaviyo-automation` | "Automate Klaviyo tasks via Rube MCP (Composio): manage email/SMS campaigns, inspect campaign messages, track tags, and monitor send jobs... |
| 1639 | `knowledge-base` | 'Knowledge base register: article title, category, department, owner, tags, summary, linked SOP, audience, last and next review dates and... |
| 1640 | `kotler-macro-analyzer` | "Professional PESTEL/SWOT analysis agent based on Kotler's methodology for strategic market audits." |
| 1641 | `kotlin-coroutines-expert` | "Expert patterns for Kotlin Coroutines and Flow, covering structured concurrency, error handling, and testing." |
| 1642 | `kpi-dashboard-design` | "Comprehensive patterns for designing effective Key Performance Indicator (KPI) dashboards that drive business decisions." |
| 1643 | `kpi-tracker` | 'KPI register: metric by level, department, job title and employee, linked OKR, unit and direction, target against actual, achievement an... |
| 1644 | `krexa` | "Turn a trading idea, post or video into fixed rules, backtest and paper-trade them, and request a user-approved live agent through Krexa... |
| 1645 | `kubernetes-architect` | Expert Kubernetes architect specializing in cloud-native infrastructure, advanced GitOps workflows (ArgoCD/Flux), and enterprise containe... |
| 1646 | `kubernetes-deployment` | "Kubernetes deployment workflow for container orchestration, Helm charts, service mesh, and production-ready K8s configurations." |
| 1647 | `kubernetes-hardening` | Implement Kubernetes security contexts, Pod Security Standards, and network policies. |
| 1648 | `kubernetes-ops` | Deploy, scale, and manage Kubernetes workloads. |
| 1649 | `kubestellar-console` | "Multi-cluster Kubernetes dashboard with AI-powered operations via MCP server and 10+ built-in agent skills" |
| 1650 | `kustomize` | Customize Kubernetes manifests without templating using Kustomize. |
| 1651 | `lambda-lang` | "Native agent-to-agent language for compact multi-agent messaging. A shared tongue agents speak directly, not a translation layer. 340+ a... |
| 1652 | `lambdatest-agent-skills` | "Production-grade test automation skills for 46 frameworks across E2E, unit, mobile, BDD, visual, and cloud testing in 15+ languages." |
| 1653 | `landing-page` | "Build landing, home and pricing pages that look like a real product instead of AI output: honest copy, one design system, checked on pho... |
| 1654 | `landing-page-design` | "Plan and build conversion-focused landing pages with intake, proof-based copy, explicit page structure, and the ELAYA visual system." |
| 1655 | `landing-page-generator` | "Generates high-converting Next.js/React landing pages with Tailwind CSS. Uses PAS, AIDA, and BAB frameworks for optimized copy/component... |
| 1656 | `langchain-architecture` | "Master the LangChain framework for building sophisticated LLM applications with agents, chains, memory, and tool integration." |
| 1657 | `langfuse` | Expert in Langfuse - the open-source LLM observability platform. Covers tracing, prompt management, evaluation, datasets, and integration... |
| 1658 | `langgraph` | Expert in LangGraph - the production-grade framework for building stateful, multi-actor AI applications. Covers graph construction, state... |
| 1659 | `lanshu-create-ai-presenter-video` | "Turn a topic or script into a publish-ready explainer video, led by an AI presenter or performed in one of twelve styled explainer looks." |
| 1660 | `laravel-development-workflow` | "Build and fix existing Laravel applications through root-cause diagnosis, repository-native implementation, regression coverage, and ris... |
| 1661 | `laravel-expert` | "Senior Laravel Engineer role for production-grade, maintainable, and idiomatic Laravel solutions. Focuses on clean architecture, securit... |
| 1662 | `laravel-security-audit` | "Security auditor for Laravel applications. Analyzes code for vulnerabilities, misconfigurations, and insecure practices using OWASP stan... |
| 1663 | `last30days` | "Research a topic from the last 30 days on Reddit + X + Web, summarize evidence, and write copy-paste-ready prompts for the user's target... |
| 1664 | `latex-paper-conversion` | "This skill should be used when the user asks to convert an academic paper in LaTeX from one format (e.g., Springer, IPOL) to another for... |
| 1665 | `launch-check` | "Bounded pre-launch audit of a live URL for AI-built apps: exposed secret keys, open Supabase/Firebase tables, security headers, phone la... |
| 1666 | `launch-strategy` | "You are an expert in SaaS product launches and feature announcements. Your goal is to help users plan launches that build momentum, capt... |
| 1667 | `lead-magnets` | "Plan and optimize lead magnets for email capture and lead generation. Use when designing gated content, checklists, templates, downloada... |
| 1668 | `lead-signals` | "Find and qualify public buying signals through Treg, rank fitting business accounts and optionally enrich authorized business contact in... |
| 1669 | `learn` | Help a user learn a topic through adaptive tutoring, lesson planning, practice, retrieval checks, explanations, study guides, or exercise... |
| 1670 | `learn-taste` | Turn a session's design corrections into rules, with their why, in DESIGN.md, a project skill, or a lint check. |
| 1671 | `learning-career-development` | 'Training register: course, provider, delivery method, department, employee, duration, progress percentage, score, mandatory flag, certif... |
| 1672 | `leave-management` | 'Leave register: request, leave type, employee and department, manager and approver, start and end dates, days requested, leave balances,... |
| 1673 | `ledger-tasks-yylo` | 'Use YYLO Ledger task management: create, list, search, get, mark, update, archive, deps, ready, order and merge with dependencies.' |
| 1674 | `legacy-modernizer` | Refactor legacy codebases, migrate outdated frameworks, and implement gradual modernization. Handles technical debt, dependency updates, ... |
| 1675 | `legal-advisor` | Draft privacy policies, terms of service, disclaimers, and legal notices. Prepares jurisdiction-aware drafts for qualified review, cookie... |
| 1676 | `legal-compliance-vault` | 'Legal and compliance document vault: document type, framework, owner and department, effective and expiry dates, renewal flag, storage l... |
| 1677 | `legal-pages` | 'Privacy policy, terms, a cookie banner, consent at sign-up, a public front door: legal pages drafted from what the code does, held to it... |
| 1678 | `leiloeiro-avaliacao` | Organize evidence and indicative valuation scenarios for auction properties, with explicit market, method and professional-review limits. |
| 1679 | `leiloeiro-edital` | Analise e auditoria de editais de leilao judicial e extrajudicial. Riscos ocultos, clausulas perigosas, debitos, ocupante e classificacao... |
| 1680 | `leiloeiro-ia` | Especialista em leiloes judiciais e extrajudiciais de imoveis. Analise juridica, pericial e de mercado integrada. Orquestra os 5 modulos ... |
| 1681 | `leiloeiro-juridico` | 'Analise juridica de leiloes: nulidades, bem de familia, alienacao fiduciaria, CPC arts 829-903, Lei 9514/97, onus reais, embargos e juri... |
| 1682 | `leiloeiro-mercado` | Analise de mercado imobiliario para leiloes. Liquidez, desagio tipico, ROI, estrategias de saida (flip/reforma/renda), Selic 2025 e bench... |
| 1683 | `leiloeiro-risco` | Analise de risco em leiloes de imoveis. Score 40 pontos, riscos juridicos/financeiros/operacionais, stress test 4 cenarios e ROI ponderad... |
| 1684 | `lemmaly` | "Algorithm-first discipline: state Big-O, data structure, and algorithm family BEFORE writing loops, queries, or recursion. Catches O(n^2... |
| 1685 | `lesson-generator` | Build compact, standalone multi-lesson course artifacts with lesson navigation, objectives, flashcards, quizzes, and source links. |
| 1686 | `lex` | "Structured research aid for cross-jurisdictional legal context (US, EU, CA) and contract scaffolding." |
| 1687 | `lightning-architecture-review` | Review Bitcoin Lightning Network protocol designs, compare channel factory approaches, and analyze Layer 2 scaling tradeoffs. Covers trus... |
| 1688 | `lightning-channel-factories` | Technical reference on Lightning Network channel factories, multi-party channels, LSP architectures, and Bitcoin Layer 2 scaling without ... |
| 1689 | `lightning-factory-explainer` | Explain Bitcoin Lightning channel factories and the SuperScalar protocol — scalable Lightning onboarding using shared UTXOs, Decker-Watte... |
| 1690 | `lightweight-charts-react-components` | "Build and debug React financial charts with realtime candles, viewport-preserving history, indicator panes, markers, and chart API refs ... |
| 1691 | `linear-automation` | "Automate Linear tasks via Rube MCP (Composio): issues, projects, cycles, teams, labels. Always search tools first for current schemas." |
| 1692 | `linear-claude-skill` | "Manage Linear issues, projects, and teams" |
| 1693 | `link-relevance-evaluator` | "Link Relevance Evaluator. Use when working with source page context and destination page context." |
| 1694 | `link-source-categorizer` | "Link Source Categorizer. Use when working with backlink rows with source URLs and optional page context." |
| 1695 | `link-toxicity-checker` | "Link Toxicity Checker. Use when working with backlink examples and available evidence." |
| 1696 | `linkdigest-social-link-reader` | "Read one public Xiaohongshu, Douyin, TikTok, YouTube, X or WeChat article link into text an agent can use (transcript, image text, key p... |
| 1697 | `linkdr` | Review LinkDR placement options, pricing and editorial controls, and prepare a budget estimate for an explicitly authorized handoff. |
| 1698 | `linkedin-automation` | "Automate LinkedIn tasks via Rube MCP (Composio): create posts, manage profile, company info, comments, and image uploads. Always search ... |
| 1699 | `linkedin-cli` | "Use when automating LinkedIn via CLI: fetch profiles, search people/companies, send messages, manage connections, create posts, and Sale... |
| 1700 | `linkedin-content-generator` | "AI-powered LinkedIn content suite: generate posts, carousels, newsletters, and 30-day calendars with niche-specific SEO rules and a feed... |
| 1701 | `linkedin-post-writer` | "Draft LinkedIn posts from 16 illustrative hook formulas mapped to engagement goals (comments, reposts, likes, saves), with optional form... |
| 1702 | `linkedin-profile-optimizer` | "High-intent expert for LinkedIn profile checks and SEO optimization. Silently audits and rewrites profiles, delivering only the finished... |
| 1703 | `linkerd-patterns` | "Production patterns for Linkerd service mesh - the lightweight, security-first service mesh for Kubernetes." |
| 1704 | `linktree-link-hub` | 'Link-in-bio register: label, destination URL, link type, priority order, audience, click tracking, UTM source, schedule, click count and... |
| 1705 | `lint-and-validate` | "Run configured lint and type checks, distinguish failures from checks that did not run, and report concrete validation results." |
| 1706 | `lintlang-audit` | Audit named agent instructions, tool definitions, and supported Python prompts with local LintLang checks; return finding codes and locat... |
| 1707 | `linux-administration` | System administration for Linux servers. Manage packages, services, and system configuration. Use when administering Linux systems. |
| 1708 | `linux-hardening` | Apply CIS benchmarks and secure Linux servers. |
| 1709 | `linux-privilege-escalation` | "Execute systematic privilege escalation assessments on Linux systems to identify and exploit misconfigurations, vulnerable services, and... |
| 1710 | `linux-shell-scripting` | "Provide production-ready shell script templates for common Linux system administration tasks including backups, monitoring, user managem... |
| 1711 | `linux-troubleshooting` | "Linux system troubleshooting workflow for diagnosing and resolving system issues, performance problems, and service failures." |
| 1712 | `liuguang-banlan-ui` | Builds two parameterized UI modes—流光溢彩白 (iridescent white) and 五彩斑斓黑 (colorful black)—with OKLCH, WebGL/CSS fallback, vision gating, scre... |
| 1713 | `llm-app-patterns` | "Architecture and integration sketches for LLM applications, with explicit retrieval, tool, privacy and verification boundaries." |
| 1714 | `llm-app-security` | Secure LLM-powered applications with input validation, output controls, tenant isolation, and abuse prevention. |
| 1715 | `llm-application-dev-ai-assistant` | "Design and implement conversational AI assistants with context management, integration boundaries, and validation." |
| 1716 | `llm-application-dev-langchain-agent` | "You are an expert LangChain agent developer specializing in production-grade AI systems using LangChain 0.1+ and LangGraph." |
| 1717 | `llm-application-dev-prompt-optimize` | "Improve LLM prompts using task-specific evaluation, structured instructions, and regression checks." |
| 1718 | `llm-caching` | Implement multi-layer LLM caching with exact match, semantic similarity, and provider-side prompt caching. |
| 1719 | `llm-cost-optimization` | Reduce LLM API and infrastructure costs through model selection, prompt caching, batching, caching, quantization, and self-hosting strate... |
| 1720 | `llm-council` | "Run Fireworks-hosted open-weight model councils that compare responses and synthesize a final answer." |
| 1721 | `llm-evaluation` | "Master comprehensive evaluation strategies for LLM applications, from automated metrics to human evaluation and A/B testing." |
| 1722 | `llm-fine-tuning` | Set up infrastructure for fine-tuning LLMs with QLoRA, LoRA, and full fine-tuning using Hugging Face TRL, Axolotl, and distributed traini... |
| 1723 | `llm-gateway` | Deploy an API gateway for LLM traffic with load balancing, rate limiting, key management, semantic caching, fallback routing, and cost tr... |
| 1724 | `llm-inference-scaling` | Auto-scale LLM inference clusters on Kubernetes using KEDA, custom GPU metrics, and horizontal pod autoscaling. |
| 1725 | `llm-ops` | "LLM Operations -- RAG, embeddings, vector databases, fine-tuning, prompt engineering avancado, custos de LLM, evals de qualidade e arqui... |
| 1726 | `llm-prompt-optimizer` | "Use when improving prompts for any LLM. Applies proven prompt engineering techniques to boost output quality, reduce hallucinations, and... |
| 1727 | `llm-security` | "Authorized security assessment of LLM applications and AI agents: prompt injection, tool abuse, RAG exposure, memory poisoning, system-p... |
| 1728 | `llm-structured-output` | Get reliable JSON, enums, and typed objects from LLMs using response_format, tool_use, and schema-constrained decoding across OpenAI, Ant... |
| 1729 | `llmops-platform-engineering` | Build production LLMOps platforms with CI/CD, model promotion workflows, evaluation gates, rollback, and governance across cloud and self... |
| 1730 | `load-balancing` | Configure load balancers and traffic distribution. Implement health checks and SSL termination. Use when distributing traffic across serv... |
| 1731 | `local-citation-finder` | "Local Citation Finder. Use when working with business category and service location." |
| 1732 | `local-keyword-generator` | "Local Keyword Generator. Use when working with service or product and actual target location." |
| 1733 | `local-legal-seo-audit` | "Audit and improve local SEO for law firms, attorneys, forensic experts and legal/professional services sites with local presence, focusi... |
| 1734 | `local-llm-expert` | Master local LLM inference, model selection, VRAM optimization, and local deployment using Ollama, llama.cpp, vLLM, and LM Studio. Expert... |
| 1735 | `local-schema-builder` | "Local Schema Builder. Use when working with business facts, page URL and actual address or service area." |
| 1736 | `local-seo-audit-checklist` | "Local SEO Audit Checklist. Use when working with business type, location and profile or site details." |
| 1737 | `location-based-content-idea-generator` | "Local Content Idea Generator. Use when working with location, audience and business topic." |
| 1738 | `logbrew-debug-production` | "Debug a production error with LogBrew evidence: find the issue, read its stack and first release, pull its trace and logs, fix it, then ... |
| 1739 | `logic-diff` | "Compare two code versions for semantic equivalence via semi-formal tracing of both versions side-by-side." |
| 1740 | `logic-explain` | "Explain what a specific piece of code actually does for a given input by producing a step-by-step execution trace (interprocedural, with... |
| 1741 | `logic-fix-all` | "Autonomous repository-wide audit-and-fix pipeline: health → review → locate/explain → fix → diff-verify → iterate until clean. Starts wi... |
| 1742 | `logic-lens` | "AI-powered Claude Code skill that performs deep code review using formal logic and reasoning frameworks to detect bugs, anti-patterns, a... |
| 1743 | `logic-locate` | "Locate the root cause of a CONFIRMED failure via backward-then-forward semi-formal tracing." |
| 1744 | `logic-review` | "Find logic bugs in a single file or function via semi-formal execution tracing (Premises → Trace → Divergence → Trigger → Remedy)." |
| 1745 | `logistics-exception-management` | Triage freight delays, damage, shortages, loss and carrier disputes; prepare evidence, recovery options and communications with jurisdict... |
| 1746 | `lognorm` | "Work a site's SEO and AI-visibility (GEO) backlog through the hosted LogNorm MCP server: audits, fixes, content, AI-answer tracking." |
| 1747 | `logo-image-design` | 'Brand asset register: asset type, format, dimensions and aspect ratio, colour mode, background variant, clear space, approved and prohib... |
| 1748 | `logo-to-stickers` | "Turn a brand mark or existing IP into consistent, playful paper stickers with small visual stories and separate transparent images. Use ... |
| 1749 | `loki-logging` | Configure Grafana Loki for log aggregation and analysis. |
| 1750 | `loki-mode` | "Historical 2.35.x multi-agent workflow for turning a scoped PRD into reviewed implementation; includes experimental runner and benchmark... |
| 1751 | `long-tail-keyword-generator` | "Long-Tail Keyword Generator. Use when working with seed topic and optional audience or use case." |
| 1752 | `longbridge` | "Guide to using a separately installed Longbridge integration — real-time quotes, charts, fundamentals, portfolio analysis, options, and ... |
| 1753 | `longbridge-content` | "Latest news articles, regulatory filings, community discussion topics for listed stocks, and SEC EDGAR filing analysis (10-K/10-Q/8-K/pr... |
| 1754 | `longbridge-derivatives` | Curated upstream guidance for Longbridge Derivatives; use when the workflow matches the user goal. |
| 1755 | `longbridge-fundamentals` | "Financial statements, business segments, dividends, valuation multiples (PE/PB/PS), industry comparison, operating data, corporate actio... |
| 1756 | `longbridge-market-data` | "Real-time quotes, K-line charts, order book, trade ticks, intraday capital flow, market sentiment temperature, trading session schedule,... |
| 1757 | `longbridge-quant` | Curated upstream guidance for Longbridge Quant; use when the workflow matches the user goal. |
| 1758 | `longbridge-research` | Curated upstream guidance for Longbridge Research; use when the workflow matches the user goal. |
| 1759 | `lookdev` | "Human-in-the-loop web studio to tune AI-generated output by eye. Stand up a local interactive studio (sliders, pickers, drag handles) or... |
| 1760 | `lookdev-auto` | "Automated visual tuning: a vision or video model rates rendered variants in a loop. Render several labeled variants into one artifact, a... |
| 1761 | `looot` | "Search, price and run 2,500+ data API endpoints (work emails, company search, SERP, web pages) from one prepaid balance via the looot MC... |
| 1762 | `loop-library` | "Find, compare, adapt, and design bounded AI-agent feedback loops with explicit checks, stop rules, guardrails, and handoffs." |
| 1763 | `loopy` | "Discover, find, compare, audit, repair, adapt, craft, run, debrief, and prepare repeatable AI-agent loops for publication." |
| 1764 | `lore` | "Markdown project memory for AI agents. Use for decisions, architecture, conventions, monorepo scopes, `.lore/`, or `lore` commands; not ... |
| 1765 | `loss-aversion-designer` | "Compare gain and loss framing and describe credible costs of inaction when an offer needs urgency without fearmongering." |
| 1766 | `lovable-cleanup` | "Audits and strips Lovable scaffolding from Vite + React projects — removes lovable-tagger, swaps placeholder assets, prunes unused Radix... |
| 1767 | `lumify-odds` | "Lumify's hosted sports MCP/REST API for sportsbook odds, line-movement history, public betting splits, and player props across MLB, NFL,... |
| 1768 | `lurkapi-ad-research` | "Tear down the ads a brand or market runs in the Meta, Google, LinkedIn and TikTok ad libraries via LurkAPI: live ads, long-running winne... |
| 1769 | `m365-agents-dotnet` | Microsoft 365 Agents SDK for .NET. Build multichannel agents for Teams/M365/Copilot Studio with ASP.NET Core hosting, AgentApplication ro... |
| 1770 | `m365-agents-py` | Microsoft 365 Agents SDK for Python. Build multichannel agents for Teams/M365/Copilot Studio with aiohttp hosting, AgentApplication routi... |
| 1771 | `m365-agents-ts` | Microsoft 365 Agents SDK for TypeScript/Node.js. |
| 1772 | `m365-entra-attack` | Microsoft 365 / Entra ID red-team attack chain |
| 1773 | `mac-api-connection-diagnostics` | "Diagnose an API or website connection failure from a Mac with Kilobat's read-only JSON probes before changing application code or networ... |
| 1774 | `mac-mini-llm-lab` | Configure a Mac mini as a reliable local LLM server with remote access, observability, and power-safe operation. Use when building an alw... |
| 1775 | `machine-learning-ops-ml-pipeline` | "Design and implement a complete ML pipeline for: $ARGUMENTS" |
| 1776 | `macos-menubar-tuist-app` | Build, refactor, or review SwiftUI macOS menubar apps that use Tuist. |
| 1777 | `macos-reverse` | "Authorized macOS and Mach-O reverse engineering: codesign inspection, Objective-C/Swift recovery, endpoint-security surfaces, and Apple-... |
| 1778 | `macos-screen-recorder` | "macOS screen recorder that captures the main display PLUS system audio via ScreenCaptureKit — no BlackHole/loopback driver, no sudo, jus... |
| 1779 | `macos-spm-app-packaging` | Scaffold, build, sign, and package SwiftPM macOS apps without Xcode projects. |
| 1780 | `magic-animator` | AI-powered animation tool for creating motion in logos, UI, icons, and social media assets. |
| 1781 | `magic-ui-generator` | Utilizes Magic by 21st.dev to generate, compare, and integrate multiple production-ready UI component variations. |
| 1782 | `mailchimp-automation` | "Automate Mailchimp email marketing including campaigns, audiences, subscribers, segments, and analytics via Rube MCP (Composio). Always ... |
| 1783 | `mailtrap-managing-contacts` | Manage Mailtrap contacts, lists, segments, custom fields, imports, CRM syncs, and campaign audiences through the UI or API. |
| 1784 | `mailtrap-sending-emails` | Configure or troubleshoot Mailtrap live email sending with Email API, SMTP, transactional streams, bulk streams, or batches. |
| 1785 | `mailtrap-setting-up-sending-domain` | Add or verify a Mailtrap sending domain, troubleshoot DNS propagation, publish SPF/DKIM/DMARC records, and complete compliance. |
| 1786 | `mailtrap-testing-with-sandbox` | Capture outbound email in Mailtrap Email Sandbox for development, staging, CI, HTML inspection, spam checks, and fake inbox tests. |
| 1787 | `maintain-codex-wiki` | "Maintain a review-first engineering wiki with provenance, citation-aware queries, explicit capture and promotion, and deterministic chec... |
| 1788 | `make-automation` | "Automate Make (Integromat) tasks via Rube MCP (Composio): operations, enums, language and timezone lookups. Always search tools first fo... |
| 1789 | `make-ugc` | "Create original AI UGC-style product videos through Treg: research hooks, approve a licensed presenter and voice, generate clips, add ca... |
| 1790 | `makepad-2-0-animation` | Makepad 2.0 guidance for animation; use when building or debugging Makepad UI code. |
| 1791 | `makepad-2-0-dsl` | Makepad 2.0 guidance for dsl; use when building or debugging Makepad UI code. |
| 1792 | `makepad-2-0-events` | Makepad 2.0 guidance for events; use when building or debugging Makepad UI code. |
| 1793 | `makepad-2-0-layout` | Makepad 2.0 guidance for layout; use when building or debugging Makepad UI code. |
| 1794 | `makepad-2-0-widgets` | Makepad 2.0 guidance for widgets; use when building or debugging Makepad UI code. |
| 1795 | `makepad-animation` | \| CRITICAL: Use for Makepad animation system. Triggers on: makepad animation, makepad animator, makepad hover, makepad state, makepad tra... |
| 1796 | `makepad-basics` | \| CRITICAL: Use for Makepad getting started and app structure. Triggers on: makepad, makepad getting started, makepad tutorial, live_desi... |
| 1797 | `makepad-deployment` | \| CRITICAL: Use for Makepad packaging and deployment. Triggers on: deploy, package, APK, IPA, 打包, 部署, cargo-packager, cargo-makepad, WASM... |
| 1798 | `makepad-dsl` | \| CRITICAL: Use for Makepad DSL syntax and inheritance. Triggers on: makepad dsl, live_design, makepad inheritance, makepad prototype, "<... |
| 1799 | `makepad-event-action` | \| CRITICAL: Use for Makepad event and action handling. Triggers on: makepad event, makepad action, Event enum, ActionTrait, handle_event,... |
| 1800 | `makepad-font` | \| CRITICAL: Use for Makepad font and text rendering. Triggers on: makepad font, makepad text, makepad glyph, makepad typography, font atl... |
| 1801 | `makepad-layout` | \| CRITICAL: Use for Makepad layout system. Triggers on: makepad layout, makepad width, makepad height, makepad flex, makepad padding, mak... |
| 1802 | `makepad-platform` | \| CRITICAL: Use for Makepad cross-platform support. Triggers on: makepad platform, makepad os, makepad macos, makepad windows, makepad li... |
| 1803 | `makepad-reference` | "Guide to diagnosing Makepad build, widget, redraw and layout issues against the exact runtime revision." |
| 1804 | `makepad-shaders` | \| CRITICAL: Use for Makepad shader system. Triggers on: makepad shader, makepad draw_bg, Sdf2d, makepad pixel, makepad glsl, makepad sdf,... |
| 1805 | `makepad-skills` | "Makepad UI development skills for Rust apps: setup, patterns, shaders, packaging, and troubleshooting." |
| 1806 | `makepad-splash` | \| CRITICAL: Use for Makepad Splash scripting language. Triggers on: splash language, makepad script, makepad scripting, script!, cx.eval,... |
| 1807 | `makepad-widgets` | "Select and compose Makepad widgets, configure their properties and styling, and debug widget behavior against a pinned makepad-widgets v... |
| 1808 | `malware-analysis` | "Analyze suspected malware through static, dynamic, and behavioral techniques: IOC extraction, YARA/Sigma rule authoring, sandbox orchest... |
| 1809 | `malware-analyst` | Expert malware analyst specializing in defensive malware research, threat intelligence, and incident response. Masters sandbox analysis, ... |
| 1810 | `manage-skills` | Discover, list, create, edit, toggle, copy, move, and delete AI agent skills across 11 tools (Cursor, Claude, Agents, Windsurf, Copilot, ... |
| 1811 | `manifest` | "Install and configure the Manifest observability plugin for your agents. Use when setting up telemetry, configuring API keys, or trouble... |
| 1812 | `markdown-rendering` | "Open Markdown reliably in cmux panes and recover from blank rendered surfaces." |
| 1813 | `market-segments` | 'Exploring customer segments, audiences or new markets: 3-5 segments with their jobs, pains and product fit.' |
| 1814 | `market-sizing-analysis` | "Comprehensive market sizing methodologies for calculating Total Addressable Market (TAM), Serviceable Available Market (SAM), and Servic... |
| 1815 | `market-validator` | "Validate a product idea against real user complaints from Reddit, X, G2, Quora, Hacker News, Product Hunt and YouTube, then score demand... |
| 1816 | `marketing-ideas` | "Provide proven marketing strategies and growth ideas for SaaS and software products, prioritized using a marketing feasibility scoring s... |
| 1817 | `marketing-mindset` | "Use when a user asks how to win first customers, whether doing X will produce Y, how to write an ad or judge a marketing test — a market... |
| 1818 | `marketing-plan` | "When the user needs a comprehensive marketing plan for a client, a company they advise, or their own product." |
| 1819 | `marketing-psychology` | "Apply behavioral science and mental models to marketing decisions, prioritized using a psychological leverage and feasibility scoring sy... |
| 1820 | `marketplace-rbac-audit` | "Audit multi-role marketplace authorization across roles, resource ownership, tenant boundaries, and order-state transitions; use when ac... |
| 1821 | `markstream-angular` | "Integrate the alpha markstream-angular renderer into Angular 20+ applications with standalone components, signals, safe HTML defaults, a... |
| 1822 | `markstream-custom-components` | "Override Markstream node renderers and add trusted custom tags across Vue, React, Svelte, and Angular using scoped or renderer-local map... |
| 1823 | `markstream-install` | "Install and configure Markstream streaming Markdown renderers for Vue, React, Svelte, Angular, Nuxt, Next.js, and Vue 2 applications." |
| 1824 | `markstream-migration` | "Audit and migrate an existing Markdown renderer to Markstream while preserving custom renderers, security policy, streaming behavior, an... |
| 1825 | `markstream-nuxt` | "Integrate markstream-vue into Nuxt 3 or 4 with SSR-safe client boundaries, renderer modes, explicit CSS, and browser-only optional peers." |
| 1826 | `markstream-react` | "Integrate the beta markstream-react renderer into React 18+ or Next.js with correct client/server entrypoints, CSS, streaming state, and... |
| 1827 | `markstream-svelte` | "Integrate the beta markstream-svelte renderer into Svelte 5 or SvelteKit with runes, explicit CSS, smooth streaming, workers, and SSR-sa... |
| 1828 | `markstream-vue` | "Integrate markstream-vue into plain Vue 3 with renderer modes, code and DOM choices, streaming state, virtualization, optional peers, an... |
| 1829 | `markstream-vue2` | "Integrate markstream-vue2 into Vue 2.6 or 2.7 with correct Composition API decisions, CSS, streaming state, optional peers, and scoped o... |
| 1830 | `markstream-vue2-cli` | "Integrate markstream-vue2 into Vue CLI or Webpack 4 with export-map-safe CSS, CDN worker fallbacks, and conservative code-block defaults." |
| 1831 | `markstream-vue2-vite` | "Integrate markstream-vue2 into Vue 2 plus Vite with bundled worker imports, CSS ordering, Composition API compatibility, and safe stream... |
| 1832 | `marlin-bed-leveling` | "Calibrates Marlin 2.x 3D printer firmware bed leveling: Unified Bed Leveling (UBL), Bilinear ABL, M420 S1 post-homing, Z-probe offsets, ... |
| 1833 | `master-pitcher` | "Audit, draft or roast a pitch deck against a VC's 3-minute scan: 18 checks across 6 dimensions, a score out of 18, ranked fixes and plac... |
| 1834 | `matematico-tao` | "Analyze code complexity, dependency graphs, concurrency and invariants using explicit mathematical assumptions. Use for algorithm or arc... |
| 1835 | `mathguard` | "Math-heavy escalation for n >= 10^6 — Bloom, HyperLogLog, Count-Min, MinHash/LSH, FFT, JL projection, sweep line. Use when classical O(n... |
| 1836 | `matplotlib` | "Matplotlib is Python's foundational visualization library for creating static, animated, and interactive plots." |
| 1837 | `maxia` | Connect to MAXIA AI-to-AI marketplace on Solana. Discover, buy, sell AI services. Earn USDC. 13 MCP tools, A2A protocol, DeFi yields, sen... |
| 1838 | `mcd-secret-menu-lab` | "Plan McDonald's China recipe combinations using an authorized MCP connection for current store menus, prices and nutrition. Use for recr... |
| 1839 | `mcp-builder` | "Create MCP (Model Context Protocol) servers that enable LLMs to interact with external services through well-designed tools. The quality... |
| 1840 | `mcp-builder-ms` | "Use this skill when building MCP servers to integrate external APIs or services, whether in Python (FastMCP) or Node/TypeScript (MCP SDK)." |
| 1841 | `mcp-dependency-drift-audit` | "Statically audit MCP configs for mutable npm/npx package references before approval or CI, without executing discovered MCP servers." |
| 1842 | `mcp-server` | 'Before adding a remote MCP server or tool to a web product, adding OAuth to it, or listing it in a directory: ship it right the first ti... |
| 1843 | `mcp-server-security` | Secure Model Context Protocol (MCP) servers with transport encryption, tool authorization, input validation, and audit logging for safe A... |
| 1844 | `mcp-tool-developer` | "Build Model Context Protocol (MCP) servers and tools from scratch. Full-stack MCP development with TypeScript/Python, testing, deploymen... |
| 1845 | `md2video-audio` | "Convert Markdown documents into narrated MP4 videos with synchronized visuals and voice narration." |
| 1846 | `mdm-device-management` | Manage and secure company devices with MDM solutions |
| 1847 | `mdpr-skill` | "Review MDPR Markdown presentation workflows with semantic hints, visual checks, and deterministic renderer boundaries." |
| 1848 | `media-use` | "Resolve and prepare licensed media, voice, music, captions and sound for HyperFrames with explicit provider and cost boundaries." |
| 1849 | `meeting-distiller-pro` | Transform messy meeting notes and transcripts into structured action items, decisions, and follow-ups. Never lose a meeting insight again. |
| 1850 | `meeting-notes` | "Turns raw meeting notes into structured minutes: conclusion first, then decisions / action items / open questions; every action item mus... |
| 1851 | `meme-coin-audit` | Meme coin and token security audit |
| 1852 | `memory-forensics` | "Comprehensive techniques for acquiring, analyzing, and extracting artifacts from memory dumps for incident response and malware analysis." |
| 1853 | `memory-handoff` | "Portable session handoff across agent CLIs: read a project's handoff file at session start, rewrite it at session end, so the next sessi... |
| 1854 | `memory-safety-patterns` | "Cross-language patterns for memory-safe programming including RAII, ownership, smart pointers, and resource management." |
| 1855 | `memory-systems` | "Design short-term, long-term, and graph-based memory architectures. Use when building agents that must persist across sessions, needing ... |
| 1856 | `mental-health-analyzer` | 分析心理健康数据、识别心理模式、评估心理健康状况、提供个性化心理健康建议。支持与睡眠、运动、营养等其他健康数据的关联分析。 |
| 1857 | `mentorship-program` | 'Mentorship register: mentor and mentee pair, department, focus area, mentee goal, session counts, last and next session, overall rating,... |
| 1858 | `mercury-mcp` | "Cheatsheet for the Mercury (proton) MCP tools. Use when connected to the Mercury MCP server to look up which mercury_* tool to call for ... |
| 1859 | `mermaid-expert` | Create Mermaid diagrams for flowcharts, sequences, ERDs, and architectures. Masters syntax for all diagram types and styling. |
| 1860 | `mesh-memory` | "Self-hosted semantic memory for AI agents via MCP. Save worklogs, decisions, and notes, then recall them across sessions by meaning, not... |
| 1861 | `meta-description-optimizer` | "Meta Description Optimizer. Use when working with existing description and page content or summary." |
| 1862 | `meta-description-writer` | "Meta Description Writer. Use when working with page content or factual summary." |
| 1863 | `meta-tag-comparison-tool` | "Meta Tag Comparison Tool. Use when working with HTML or extracted metadata from two or more labeled pages." |
| 1864 | `meta-tag-generator` | "Meta Tag Generator. Use when working with page summary, URL and optional brand or social image." |
| 1865 | `metasploit-framework` | "⚠️ AUTHORIZED USE ONLY > This skill is for educational purposes or authorized security assessments only. > You must have explicit, writt... |
| 1866 | `meteora-dlmm-pool-screening` | Screen and rank Meteora DLMM pools for LP quality using public Meteora APIs (fee/TVL, bin step, organic score). Read-only: never deploys,... |
| 1867 | `micro-saas-launcher` | Expert in launching small, focused SaaS products fast - the indie hacker approach to building profitable software. Covers idea validation... |
| 1868 | `microservices-patterns` | "Master microservices architecture patterns including service boundaries, inter-service communication, data management, and resilience pa... |
| 1869 | `microsoft-azure-webjobs-extensions-authentication-events-dotnet` | Microsoft Entra Authentication Events SDK for .NET. Azure Functions triggers for custom authentication extensions. |
| 1870 | `microsoft-teams-automation` | "Automate Microsoft Teams tasks via Rube MCP (Composio): send messages, manage channels, create meetings, handle chats, and search messag... |
| 1871 | `mid-engagement-ir-detection` | Methodology for detecting client SOC patches, attacker activity, and security-state changes that occur DURING a red-team engagement |
| 1872 | `minecraft-bukkit-pro` | Master Minecraft server plugin development with Bukkit, Spigot, and Paper APIs. |
| 1873 | `minicut-film-studio` | "Install and use the official MiniCut film studio skill, pinned by commit, to make multi-shot AI short films with the paid MiniCut CLI." |
| 1874 | `minimalist-ui` | "Use when creating clean editorial interfaces with warm monochrome palettes, crisp borders, restrained motion, and flat bento layouts." |
| 1875 | `miro-automation` | "Automate Miro tasks via Rube MCP (Composio): boards, items, sticky notes, frames, sharing, connectors. Always search tools first for cur... |
| 1876 | `mirrord` | "Run a local process inside a live Kubernetes cluster's network, env and traffic with mirrord, so changes are tested against real service... |
| 1877 | `mise-configurator` | "Generate production-ready mise.toml setups for local development, CI/CD pipelines, and toolchain standardization." |
| 1878 | `mixpanel-automation` | "Automate Mixpanel tasks via Rube MCP (Composio): events, segmentation, funnels, cohorts, user profiles, JQL queries. Always search tools... |
| 1879 | `ml-engineer` | Build production ML systems with PyTorch 2.x, TensorFlow, and modern ML frameworks. Implements model serving, feature engineering, A/B te... |
| 1880 | `ml-pipeline-workflow` | "Complete end-to-end MLOps pipeline orchestration from data preparation through model deployment." |
| 1881 | `mlops-engineer` | Build comprehensive ML pipelines, experiment tracking, and model registries with MLflow, Kubeflow, and modern MLOps tools. |
| 1882 | `mmx-cli` | "Use mmx to generate text, images, video, speech, and music via the MiniMax AI platform. Use when the user wants to create media content,... |
| 1883 | `moatmri` | Analyze AI disruption pressure across a business, map competitive exposure, and produce a 90-day defensive action plan. |
| 1884 | `mobbin` | "Find real app screens, user flows and website sections on Mobbin through the Mobbin MCP server, to ground UI design and code in shipped ... |
| 1885 | `mobile-design` | "Design and review iOS, Android, React Native or Flutter interfaces for touch, accessibility, navigation, offline behavior and measured p... |
| 1886 | `mobile-developer` | Develop React Native, Flutter, or native mobile apps with modern architecture patterns. Masters cross-platform development, native integr... |
| 1887 | `mobile-friendly-test` | "Mobile-Friendly Test. Use when working with accessible page or supplied screenshots and HTML." |
| 1888 | `mobile-native` | "Improve mobile web behavior for touch, viewport sizing, safe areas, inputs, scrolling, and native-feeling interaction." |
| 1889 | `mobile-reverse` | "Authorized Android/iOS application reverse engineering and security testing: APK/IPA analysis, runtime instrumentation (Frida/Objection)... |
| 1890 | `mobile-security-coder` | Expert in secure mobile coding practices specializing in input validation, WebView security, and mobile-specific security patterns. |
| 1891 | `mobilebox-cloud-phones` | "Drive a Mobilebox cloud Android phone or iOS simulator over MCP or REST: create it, read the screen, tap and type, install an app, then ... |
| 1892 | `mock-hunter` | "Audit a live web page in five phases (catalog, click, trace, classify, report) to identify mock data, hardcoded values, LLM-generated me... |
| 1893 | `model-cost-compare` | "Starter: compare model costs for a described task — maps task shape to the cheapest adequate seat and shows the price spread" |
| 1894 | `model-registry-governance` | Establish model registry standards, governance controls, metadata schemas, approvals, and lifecycle policies for enterprise AI deployments. |
| 1895 | `model-serving-kubernetes` | Deploy ML models on Kubernetes with KServe (formerly KFServing) and NVIDIA Triton Inference Server. |
| 1896 | `model-supply-chain-security` | Secure the AI model supply chain with artifact signing, provenance attestation, SBOM workflows, dependency controls, and trusted model pr... |
| 1897 | `modellix` | "Integrate the Modellix API/CLI for async AI image, video, and speech generation or transcription (model run --wait, task download)." |
| 1898 | `modern-java-guidance` | "Guides agents to write Java 17/21+ and Spring Boot 3.x+ code with version detection and the mjg CLI scanner instead of Java 8 and Boot 2... |
| 1899 | `modern-javascript-patterns` | "Comprehensive guide for mastering modern JavaScript (ES6+) features, functional programming patterns, and best practices for writing cle... |
| 1900 | `moltnode-chain-reader` | "Read 31 blockchains over keyless JSON-RPC with MoltNode (balances, blocks, contract calls) and get Chord swap quotes with an unsigned tr... |
| 1901 | `molykit` | \| CRITICAL: Use for MolyKit AI chat toolkit. Triggers on: BotClient, OpenAI, SSE streaming, AI chat, molykit, PlatformSend, spawn(), Thre... |
| 1902 | `monday-automation` | "Automate Monday.com work management including boards, items, columns, groups, subitems, and updates via Rube MCP (Composio). Always sear... |
| 1903 | `monetization` | "Estrategia e implementacao de monetizacao para produtos digitais - Stripe, subscriptions, pricing experiments, freemium, upgrade flows, ... |
| 1904 | `mongodb` | Administer MongoDB databases. Configure replica sets, sharding, and backups. Use when managing MongoDB deployments. |
| 1905 | `monopoly` | MONOPOLY is a Senior System Design Engineer skill for architecting, reviewing, and scaling systems. Triggers on requests involving archit... |
| 1906 | `monorepo-architect` | "Expert in monorepo architecture, build systems, and dependency management at scale. Masters Nx, Turborepo, Bazel, and Lerna for efficien... |
| 1907 | `monorepo-management` | "Build efficient, scalable monorepos that enable code sharing, consistent tooling, and atomic changes across multiple packages and applic... |
| 1908 | `monte-carlo-analyze-root-cause` | Curated upstream guidance for Monte Carlo Analyze Root Cause; use when the workflow matches the user goal. |
| 1909 | `monte-carlo-asset-health` | Curated upstream guidance for Monte Carlo Asset Health; use when the workflow matches the user goal. |
| 1910 | `monte-carlo-context-detection` | Route data-related requests to the right Monte Carlo skill or workflow. USE WHEN alerts, incidents, data broken, stale, coverage gaps, da... |
| 1911 | `monte-carlo-monitor-creation` | "Guides creation of Monte Carlo monitors via MCP tools, producing monitors-as-code YAML for CI/CD deployment." |
| 1912 | `monte-carlo-monitoring-advisor` | Analyze data coverage, create monitors for warehouse tables and AI agents. Covers coverage gaps, use-case analysis, data monitor creation... |
| 1913 | `monte-carlo-performance-diagnosis` | "Diagnoses pipeline performance issues -- slow jobs, expensive queries, latency trends -- using Monte Carlo's cross-platform observabilit... |
| 1914 | `monte-carlo-prevent` | "Surfaces Monte Carlo data observability context (table health, alerts, lineage, blast radius) before SQL/dbt edits." |
| 1915 | `monte-carlo-push-ingestion` | "Review and adapt warehouse metadata, lineage and query-log collection templates for an explicitly authorized Monte Carlo destination." |
| 1916 | `monte-carlo-remediation` | Investigate and remediate data quality alerts using Monte Carlo MCP tools. Runs root cause analysis, assesses blast radius, discovers ava... |
| 1917 | `monte-carlo-storage-cost-analysis` | Analyze a warehouse for stale, unused, or redundant tables via the analyze_storage_costs MCP tool. Classifies waste patterns and table ca... |
| 1918 | `monte-carlo-validation-notebook` | "Generates SQL validation notebooks for dbt PR changes with before/after comparison queries." |
| 1919 | `monthly-closing-statements` | 'Monthly closing register: period dates, cash/bank/party/inventory/TDS reconciliation flags, profit, receivables, payables, working capit... |
| 1920 | `moodle-external-api-development` | "This skill guides you through creating custom external web service APIs for Moodle LMS, following Moodle's external API framework and co... |
| 1921 | `movie-coupon` | "Fetch movie ticket coupons from platforms like Taopiaopiao and Maoyan. Returns coupon links and QR code images for users to redeem via W... |
| 1922 | `moyu` | Anti-over-engineering guardrail that activates when an AI coding agent expands scope, adds abstractions, or changes files the user did no... |
| 1923 | `mtls-configuration` | "Configure mutual TLS (mTLS) for zero-trust service-to-service communication. Use when implementing zero-trust networking, certificate ma... |
| 1924 | `muapi-media` | "Generate images and videos with MuAPI's schema-driven asynchronous media API while protecting keys, polling, and output downloads." |
| 1925 | `multi-advisor` | "Conselho de especialistas — consulta multiplos agentes do ecossistema em paralelo para analise multi-perspectiva de qualquer topico. Ati... |
| 1926 | `multi-agent-architect` | "Design and optimize production-grade multi-agent systems with LangGraph, LangChain, and DeepAgents for complex AI workflows." |
| 1927 | `multi-agent-brainstorming` | "Simulate a structured peer-review process using multiple specialized agents to validate designs, surface hidden assumptions, and identif... |
| 1928 | `multi-agent-patterns` | This skill should be used when the user asks to "design multi-agent system", "implement supervisor pattern", "create swarm architecture",... |
| 1929 | `multi-agent-task-orchestrator` | "Route tasks to specialized AI agents with anti-duplication, quality gates, and 30-minute heartbeat monitoring" |
| 1930 | `multi-cloud-architecture` | "Decision framework and patterns for architecting applications across AWS, Azure, and GCP." |
| 1931 | `multi-platform-apps-multi-platform` | "Build and deploy the same feature consistently across web, mobile, and desktop platforms using API-first architecture and parallel imple... |
| 1932 | `multi-source-search` | "Cross-validate web research and produce an offline-checkable evidence ledger with explicit source diversity, confidence, conflicts, and ... |
| 1933 | `multi-tenant-llm-hosting` | Design secure, multi-tenant LLM hosting platforms with tenant isolation, quotas, billing attribution, noisy-neighbor protection, and per-... |
| 1934 | `music-for-robots` | Optional music-inspired creative exercise for multimodal agents. Ingests an unquantized acoustic MP3 composition by Michael Luchtan (Musi... |
| 1935 | `music-generation-studio` | "Install and use the official AI Music Generator package, pinned by digest, for paid hosted work on the Beatra service." |
| 1936 | `mysql` | Administer MySQL/MariaDB databases. Configure replication and optimize performance. Use when managing MySQL deployments. |
| 1937 | `n8n-agents` | Design n8n AI agents, chains, classifiers, extractors, tool calling, memory, RAG, structured output, and human-review flows. |
| 1938 | `n8n-binary-and-data` | Handle n8n files and binary data across uploads, downloads, transforms, multimodal inputs, agent tools, and chat surfaces. |
| 1939 | `n8n-code-javascript` | Write JavaScript code in n8n Code nodes. Use when writing JavaScript in n8n, using $input/$json/$node syntax, selecting the HTTP Request ... |
| 1940 | `n8n-code-python` | Write Python code in n8n Code nodes. Use when writing Python in n8n, using _input/_json/_node syntax, working with standard library, or n... |
| 1941 | `n8n-code-tool` | Write and debug JavaScript or Python for the AI-callable n8n Custom Code Tool, including schemas, sandbox limits, and return formats. |
| 1942 | `n8n-error-handling` | Design visible, structured, recoverable n8n failures using error outputs, retries, Error Trigger workflows, and HTTP error responses. |
| 1943 | `n8n-expression-syntax` | Validate n8n expression syntax and fix common errors. Use when writing n8n expressions, using {{}} syntax, accessing $json/$node variable... |
| 1944 | `n8n-mcp-tools-expert` | Expert guide for using n8n-mcp MCP tools effectively. Use when searching for nodes, validating configurations, accessing templates, manag... |
| 1945 | `n8n-multi-instance` | Select, verify, and safely switch n8n MCP instances across production, staging, teams, or clients, especially before credential writes. |
| 1946 | `n8n-node-configuration` | Operation-aware node configuration guidance. Use when configuring nodes, understanding property dependencies, determining required fields... |
| 1947 | `n8n-subworkflows` | Build reusable n8n sub-workflows with typed inputs, all-vs-each execution, discoverable naming, and agent-tool exposure. |
| 1948 | `n8n-validation-expert` | "Expert guide for interpreting and fixing n8n validation errors." |
| 1949 | `n8n-workflow-patterns` | "Proven architectural patterns for building n8n workflows." |
| 1950 | `nano-settlement-verify` | "Check that a Nano (XNO) payment settled before a seller serves a paid call: one inline read-only script asks a public node about a send ... |
| 1951 | `nanobanana-ppt-skills` | "AI-powered PPT generation with document analysis and styled images" |
| 1952 | `nap-consistency-checker` | "NAP Consistency Checker. Use when working with canonical business name, address and phone plus listing records." |
| 1953 | `native-data-fetching` | Use when implementing or debugging ANY network request, API call, or data fetching. Covers fetch API, React Query, SWR, error handling, c... |
| 1954 | `neon-ai-gateway` | "One API and one credential for frontier and open-source LLMs, built into your Neon branch and powered by Databricks." |
| 1955 | `neon-functions` | "Long-running, serverless Node.js HTTP functions deployed onto your Neon branch, with DATABASE_URL injected automatically and compute tha... |
| 1956 | `neon-object-storage` | "S3-compatible object storage that branches with your Neon project, so files and the database stay in sync across every branch." |
| 1957 | `neon-postgres` | "Guides and best practices for working with Neon Serverless Postgres. Covers setup, connection methods, branching, autoscaling, scale-to-... |
| 1958 | `neon-postgres-branches` | "Choose and create the right Neon branch type for testing and development. Use when users ask about Neon branching, migration testing wit... |
| 1959 | `neon-postgres-egress-optimizer` | "Diagnose and fix excessive Postgres egress (network data transfer) in a codebase." |
| 1960 | `nerdzao-elite` | "Software engineering and product design workflow and Senior Product Designer. Full workflow with planning, architecture, TDD, clean code... |
| 1961 | `nerdzao-elite-gemini-high` | "Modo Elite Coder + UX Pixel-Perfect otimizado especificamente para Gemini 3.1 Pro High. Workflow completo com foco em qualidade máxima e... |
| 1962 | `nestjs-expert` | "You are an expert in Nest.js with deep knowledge of enterprise-grade Node.js application architecture, dependency injection patterns, de... |
| 1963 | `netapi` | "Check domains and IPs against a free compromised feed, find newly registered lookalike domains, and get TLD stats and Top 1M ranks from ... |
| 1964 | `network-101` | "Configure and test common network services (HTTP, HTTPS, SNMP, SMB) for penetration testing lab environments. Enable hands-on practice w... |
| 1965 | `network-engineer` | Expert network engineer specializing in modern cloud networking, security architectures, and performance optimization. |
| 1966 | `networkx` | "NetworkX is a Python package for creating, manipulating, and analyzing complex networks and graphs." |
| 1967 | `neverapply` | "Find matching jobs, tailor resumes, prepare for interviews and apply to jobs with the user's approval through NeverApply's hosted MCP se... |
| 1968 | `new-rails-project` | Create a new Rails project |
| 1969 | `new-relic` | Configure New Relic observability platform for infrastructure and application monitoring. |
| 1970 | `newman-cicd-integration` | "Generate ready-to-use CI/CD pipeline configurations that install and run Newman for automated API testing." |
| 1971 | `news-sentiment-engine` | Multi-source RSS news aggregation with Claude-powered sentiment analysis and structured briefing output |
| 1972 | `nexrad-mosaic-access` | "Access official NOAA/NCEP MRMS radar and multisensor composites for a region and time; validate product, grid, domain, quality, timestam... |
| 1973 | `nexrad-mosaic-construction` | "Construct a quality-aware NEXRAD multi-radar mosaic from aligned single-site products with explicit coverage, beam geometry, quality wei... |
| 1974 | `nexrad-product-access` | "Discover and access NEXRAD data for a selected radar site, time, product, or Level II moment using completed archive volumes, real-time ... |
| 1975 | `nexrad-radar-visualization` | "Plot NEXRAD Level II/III site scans and decoded radar mosaics with correct radar geometry, map grids, units, quality masks, timestamps, ... |
| 1976 | `nextjs-app-router-patterns` | "Comprehensive patterns for Next.js 14+ App Router architecture, Server Components, and modern full-stack React development." |
| 1977 | `nextjs-best-practices` | "Next.js App Router principles. Server Components, data fetching, routing patterns." |
| 1978 | `nextjs-seo-indexing` | "Fix SEO indexing issues, crawl budget problems, and Search Console coverage errors for Next.js apps. Covers canonical tags, noindex audi... |
| 1979 | `nextjs-supabase-auth` | Expert integration of Supabase Auth with Next.js App Router |
| 1980 | `nfs-storage` | Configure NFS servers and clients. Implement network file sharing for Linux systems. Use when setting up shared storage. |
| 1981 | `nft-standards` | "Master ERC-721 and ERC-1155 NFT standards, metadata best practices, and advanced NFT features." |
| 1982 | `nika` | "Runs repeatable AI work as checked, budgeted workflow files." |
| 1983 | `nitrosend-email-platform-migration` | "Move contacts from MailerLite, Brevo, Kit, ActiveCampaign, HubSpot or any CSV export to Nitrosend, importing opt-outs first and only sub... |
| 1984 | `nitrosend-klaviyo-migration` | "Move email marketing from Klaviyo to Nitrosend: bring suppressed profiles across first, import subscribed profiles by list, then rebuild... |
| 1985 | `nitrosend-mailchimp-migration` | "Move a Mailchimp audience to Nitrosend without losing consent: import opt-outs first, connect Mailchimp to sync subscribed members, then... |
| 1986 | `nitrosend-shopify-email-marketing` | "Run Shopify email marketing in Nitrosend: connect the store with customer consent kept, segment on orders and store activity, and draft ... |
| 1987 | `no-free-work` | "Classify a client request against the agreed scope, then draft the reply and a priced change order. Use for scope creep, extra requests,... |
| 1988 | `no-obvious-questions` | "Filter every question before asking the user: skip ones answerable from context, tools, common sense or prior authorization; send the re... |
| 1989 | `noaa-radar-satellite-fetching` | "Retrieve NOAA NEXRAD and GOES products from public cloud archives using verified site, product, channel, sector, and scan-time selection." |
| 1990 | `nodejs-backend-patterns` | "Comprehensive guidance for building scalable, maintainable, and production-ready Node.js backend applications with modern frameworks, ar... |
| 1991 | `nodejs-best-practices` | "Node.js development principles and decision-making. Framework selection, async patterns, security, and architecture. Teaches thinking, n... |
| 1992 | `nosql-expert` | "Expert guidance for distributed NoSQL databases (Cassandra, DynamoDB). Focuses on mental models, query-first modeling, single-table desi... |
| 1993 | `not-a-vibe-coder` | Turns vague prompts into 8 structured planning files for brand new projects. DO NOT use on existing codebases. |
| 1994 | `not-human-search-mcp` | "Search AI-ready websites, inspect indexed site details, verify MCP endpoints, and discover tools and APIs using the Not Human Search MCP... |
| 1995 | `notebooklm` | "Interact with Google NotebookLM to query documentation with Gemini's source-grounded answers. Each question opens a fresh browser sessio... |
| 1996 | `notification-reminder-hub` | 'Notification register: title, type, priority, recipient and department, message, linked record, trigger module, scheduled and sent dates... |
| 1997 | `notion-automation` | "Automate Notion tasks via Rube MCP (Composio): pages, databases, blocks, comments, users. Always search tools first for current schemas." |
| 1998 | `notion-manual-import` | 'Notion Manual Import: the Notion step for any module - CSV, property mapping, import steps and verification for the field list the activ... |
| 1999 | `notion-template-business` | Expert in building and selling Notion templates as a business - not just making templates, but building a sustainable digital product bus... |
| 2000 | `nsfw-ai-spicyapi` | "Generate adult (18+) images, image-to-video clips and image edits through the SpicyAPI API, with a cost quote before every paid run and ... |
| 2001 | `nutrition-analyzer` | 分析营养数据、识别营养模式、评估营养状况，并提供个性化营养建议。支持与运动、睡眠、慢性病数据的关联分析。 |
| 2002 | `nx-workspace-patterns` | "Configure and optimize Nx monorepo workspaces. Use when setting up Nx, configuring project boundaries, optimizing build caching, or impl... |
| 2003 | `object-storage` | Configure object storage with S3, GCS, and MinIO. Implement lifecycle policies and access controls. Use when managing object storage. |
| 2004 | `objection-preemptor` | "Map customer objections and address them with evidence and choice-preserving language when a funnel, sales page, or pitch encounters rec... |
| 2005 | `observability-and-instrumentation` | "Instruments code so production behavior is visible and diagnosable. Use when adding logging, metrics, tracing, or alerting. Use when shi... |
| 2006 | `observability-cloud-planning` | 'Build a cloud, SLO, and incident-readiness register after intake. Use when an SME needs monitoring scope, alert ownership, cost limits, ... |
| 2007 | `observability-engineer` | Build production-ready monitoring, logging, and tracing systems. Implements comprehensive observability strategies, SLI/SLO management, a... |
| 2008 | `observability-monitoring-monitor-setup` | "Set up metrics, distributed tracing, log aggregation, and dashboards for application and infrastructure monitoring." |
| 2009 | `observability-monitoring-slo-implement` | "You are an SLO (Service Level Objective) expert specializing in implementing reliability standards and error budget-based engineering pr... |
| 2010 | `obsess` | "Perfectionist mode for one target: checked attempts on a UI detail or hot path, keeps the best version, stops on a budget. Only on expli... |
| 2011 | `obsidian-bases` | Create and edit Obsidian Bases (.base files) with views, filters, formulas, and summaries. Use when working with .base files, creating da... |
| 2012 | `obsidian-cli` | "Use the Obsidian CLI to read, create, search, and manage vault content, or to develop and debug Obsidian plugins and themes from the com... |
| 2013 | `obsidian-clipper-template-creator` | Guide for creating templates for the Obsidian Web Clipper. Use when you want to create a new clipping template, understand available vari... |
| 2014 | `obsidian-markdown` | Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other Obsidian-specific syntax. Use when wor... |
| 2015 | `obtain-coupons-all-in-one` | "All-in-one coupon fetcher supporting takeout (Meituan, Ele.me, JD), parcel/courier (SF, ZTO, YTO, etc.), travel (DiDi, Ctrip), and movie... |
| 2016 | `occupational-health-analyzer` | 分析职业健康数据、识别工作相关健康风险、评估职业健康状况、提供个性化职业健康建议。支持与睡眠、运动、心理健康等其他健康数据的关联分析。 |
| 2017 | `octopus-architecture` | "Review system architecture, simplify boundaries, or compare interface designs from repository evidence" |
| 2018 | `octopus-quick` | Quick execution for ad-hoc tasks without full workflow overhead — use for small, self-contained requests |
| 2019 | `octopus-research` | "Thorough research across multiple sources — use for complex topics needing broad synthesis" |
| 2020 | `octopus-security-audit` | OWASP compliance, vulnerability scanning, and adversarial red team testing — use for security reviews |
| 2021 | `octopus-ui-ux-design` | "Design UI/UX systems with style guides, palettes, typography, and component specs for new interfaces" |
| 2022 | `odoo-accounting-setup` | "Expert guide for configuring Odoo Accounting: chart of accounts, journals, fiscal positions, taxes, payment terms, and bank reconciliati... |
| 2023 | `odoo-automated-tests` | "Write and run Odoo automated tests using TransactionCase, HttpCase, and browser tour tests. Covers test data setup, mocking, and CI inte... |
| 2024 | `odoo-backup-strategy` | "Complete Odoo backup and restore strategy: database dumps, filestore backup, automated scheduling, cloud storage upload, and tested rest... |
| 2025 | `odoo-docker-deployment` | "Production-ready Docker and docker-compose setup for Odoo with PostgreSQL, persistent volumes, environment-based configuration, and Ngin... |
| 2026 | `odoo-ecommerce-configurator` | "Expert guide for Odoo eCommerce and Website: product catalog, payment providers, shipping methods, SEO, and order-to-fulfillment workflow." |
| 2027 | `odoo-edi-connector` | "Guide for implementing EDI (Electronic Data Interchange) with Odoo: X12, EDIFACT document mapping, partner onboarding, and automated ord... |
| 2028 | `odoo-hr-payroll-setup` | "Expert guide for Odoo HR and Payroll: salary structures, payslip rules, leave policies, employee contracts, and payroll journal entries." |
| 2029 | `odoo-inventory-optimizer` | "Expert guide for Odoo Inventory: stock valuation (FIFO/AVCO), reordering rules, putaway strategies, routes, and multi-warehouse configur... |
| 2030 | `odoo-l10n-compliance` | "Country-specific Odoo localization: tax configuration, e-invoicing (CFDI, FatturaPA, SAF-T), fiscal reporting, and country chart of acco... |
| 2031 | `odoo-manufacturing-advisor` | "Expert guide for Odoo Manufacturing: Bills of Materials (BoM), Work Centers, routings, MRP planning, and production order workflows." |
| 2032 | `odoo-migration-helper` | "Step-by-step guide for migrating Odoo custom modules between versions (v14→v15→v16→v17). Covers API changes, deprecated methods, and vie... |
| 2033 | `odoo-module-developer` | "Expert guide for creating custom Odoo modules. Covers __manifest__.py, model inheritance, ORM patterns, and module structure best practi... |
| 2034 | `odoo-orm-expert` | "Master Odoo ORM patterns: search, browse, create, write, domain filters, computed fields, and performance-safe query techniques." |
| 2035 | `odoo-performance-tuner` | "Expert guide for diagnosing and fixing Odoo performance issues: slow queries, worker configuration, memory limits, PostgreSQL tuning, an... |
| 2036 | `odoo-project-timesheet` | "Expert guide for Odoo Project and Timesheets: task stages, billable time tracking, timesheet approval, budget alerts, and invoicing from... |
| 2037 | `odoo-purchase-workflow` | "Expert guide for Odoo Purchase: RFQ → PO → Receipt → Vendor Bill workflow, purchase agreements, vendor price lists, and 3-way matching." |
| 2038 | `odoo-qweb-templates` | "Expert in Odoo QWeb templating for PDF reports, email templates, and website pages. Covers t-if, t-foreach, t-field, and report actions." |
| 2039 | `odoo-rpc-api` | "Expert on Odoo's external JSON-RPC and XML-RPC APIs. Covers authentication, model calls, record CRUD, and real-world integration example... |
| 2040 | `odoo-sales-crm-expert` | "Expert guide for Odoo Sales and CRM: pipeline stages, quotation templates, pricelists, sales teams, lead scoring, and forecasting." |
| 2041 | `odoo-security-rules` | "Expert in Odoo access control: ir.model.access.csv, record rules (ir.rule), groups, and multi-company security patterns." |
| 2042 | `odoo-shopify-integration` | "Connect Odoo with Shopify: sync products, inventory, orders, and customers using the Shopify API and Odoo's external API or connector mo... |
| 2043 | `odoo-upgrade-advisor` | "Step-by-step Odoo version upgrade advisor: pre-upgrade checklist, community vs enterprise upgrade path, OCA module compatibility, and po... |
| 2044 | `odoo-woocommerce-bridge` | "Sync Odoo with WooCommerce: products, inventory, orders, and customers via WooCommerce REST API and Odoo external API." |
| 2045 | `odoo-xml-views-builder` | "Expert at building Odoo XML views: Form, List, Kanban, Search, Calendar, and Graph. Generates correct XML for Odoo 14-17 with proper vis... |
| 2046 | `odw` | Dynamic multi-agent workflows — plan first, then orchestrate parallel agents with adversarial verification via the local odw daemon. Use ... |
| 2047 | `offboarding-exit` | 'Offboarding register: exit type, employee and manager, notice and final day, reason, handover owner, and done flags for knowledge transf... |
| 2048 | `offensive-osint` | Operational arsenal for authorized external red-team and bug-bounty recon. |
| 2049 | `offer-appointment` | 'Offer register: candidate, position, department, employment type, offered salary and currency, offer date and expiry, joining date, prob... |
| 2050 | `offers` | "When the user wants to design, construct, or improve an offer — the thing they actually sell — including value framing, bonus stacking, ... |
| 2051 | `office-productivity` | "Office productivity workflow covering document creation, spreadsheet automation, presentation generation, and integration with LibreOffi... |
| 2052 | `og-tag-generator` | "OG Tag Generator. Use when working with page URL, title, description and optional public image URL." |
| 2053 | `okr-system` | 'OKR register: objective, owner and level, department, quarter and year, up to three key results with progress percentages, parent OKR an... |
| 2054 | `okta-attack` | Okta-as-IdP red-team attack chain |
| 2055 | `ollama-stack` | Run local LLM workloads with Ollama, Open WebUI, and GPU-aware tuning for private development environments. |
| 2056 | `omentir-linkedin-outreach` | "Run LinkedIn prospecting and outreach through the Omentir MCP server: find people, score fit, draft messages, and check campaigns. Never... |
| 2057 | `omp-delegate` | Delegate coding tasks to Oh My Pi (`omp`) only when the user explicitly requests it, while the orchestrator retains review and landing re... |
| 2058 | `on-call-handoff-patterns` | "Effective patterns for on-call shift transitions, ensuring continuity, context transfer, and reliable incident response across shifts." |
| 2059 | `on-page-seo-audit-checker` | "On-Page SEO Audit Checker. Use when working with page URL or HTML and target reader task." |
| 2060 | `onboard` | "Decompose mixed project materials (code, docs, PDF/Excel/PPT) into a sourced overview and a goal-driven three-tier learning path, then t... |
| 2061 | `onboarding` | "When the user wants to optimize post-signup onboarding, user activation, first-run experience, or time-to-value." |
| 2062 | `onboarding-cro` | "You are an expert in user onboarding and activation. Your goal is to help users reach their \"aha moment\" as quickly as possible and es... |
| 2063 | `onboarding-playbook` | 'Onboarding checklist: step, phase and order, department, owner, linked SOP and required flag. Use for joiner onboarding.' |
| 2064 | `onboarding-psychologist` | "Design first-use and onboarding experiences that bring an early win, cut setup friction, build ownership and form habits through stable ... |
| 2065 | `one-drive-automation` | "Automate OneDrive file management, search, uploads, downloads, sharing, permissions, and folder operations via Rube MCP (Composio). Alwa... |
| 2066 | `oneroster-csv-validator` | "Validates 1EdTech / IMS Global OneRoster v1.1 and v1.2 CSV roster sets: manifest integrity, bulk vs delta strictness, foreign key refere... |
| 2067 | `ontoly-software-graph` | "Use Ontoly's deterministic Software Graph, MCP server, and agent skills for architecture review, request tracing, impact analysis, and d... |
| 2068 | `open-dynamic-workflows` | "Plan, orchestrate, and adversarially verify parallel AI coding agents with a dynamic multi-agent workflow engine." |
| 2069 | `open-source-marketing` | When the user wants to market an open source project authentically. Trigger phrases include "open source marketing," "OSS marketing," "Gi... |
| 2070 | `openapi-spec-generation` | "Generate and maintain OpenAPI 3.1 specifications from code, design-first specs, and validation patterns. Use when creating API documenta... |
| 2071 | `openapi-spec-generator` | "Generate complete, production-ready OpenAPI 3.x and Swagger 2.0 specifications from natural language descriptions, code, or partial specs." |
| 2072 | `openclaw-deployment-hardening` | Secure OpenClaw deployments with preflight hardening checks, CI/CD guardrails, container runtime restrictions, and post-deploy verification. |
| 2073 | `openclaw-github-repo-commander` | "7-stage super workflow for GitHub repo audit, cleanup, PR review, and competitor analysis" |
| 2074 | `openclaw-local-mac-mini` | Set up OpenClaw locally and run it reliably on a Mac mini for private, always-on local agent workflows. |
| 2075 | `openclaw-security-hardening` | Harden OpenClaw self-hosted environments with baseline host controls, auth tightening, secret handling, network segmentation, and safe up... |
| 2076 | `opencode-delegate` | Delegate coding tasks to the OpenCode CLI only when the user explicitly requests it, while the orchestrator retains review and landing re... |
| 2077 | `openhook` | "Creates and joins private Openhook channels so people and their AI agents can exchange messages. Use for an Openhook invite, collaborati... |
| 2078 | `openshift` | Manage Red Hat OpenShift clusters and deployments. |
| 2079 | `opentelemetry` | Instrument applications and infrastructure with OpenTelemetry for unified traces, metrics, and logs. |
| 2080 | `opentofu-migration` | Migrate from Terraform to OpenTofu with state compatibility, provider registry setup, and CI/CD pipeline updates. Use when adopting the o... |
| 2081 | `optim-agent` | "Guide agent-driven parameter optimization for configurable systems with measurable objectives. Use for HPO, inference tuning, simulation... |
| 2082 | `options-flow-analyzer` | Compare raw and explicitly filtered options put/call ratios with documented premium, delta and expiry assumptions |
| 2083 | `oral-health-analyzer` | 分析口腔健康数据、识别口腔问题模式、评估口腔健康状况、提供个性化口腔健康建议。支持与营养、慢性病、用药等其他健康数据的关联分析。 |
| 2084 | `orca-replay` | Answers questions about a past agent run from its recording rather than from memory, and replays or forks that run. Use when asked why an... |
| 2085 | `orchestrate` | "Coordinate focused subagents on substantial work, keep their ownership non-overlapping, and integrate verified results. Use for large-sc... |
| 2086 | `orchestrate-batch-refactor` | "Plan and execute large refactors with dependency-aware work packets and parallel analysis." |
| 2087 | `organic-growth-forecast-tool` | "Organic Growth Forecast Tool. Use when working with dated traffic history or baseline with explicit growth assumptions." |
| 2088 | `organization-design` | 'Org structure register: department, type, parent, head, location, approved against actual headcount, annual budget, cost centre code and... |
| 2089 | `os-scripting` | "Operating system and shell scripting troubleshooting workflow for Linux, macOS, and Windows. Covers bash scripting, system administratio... |
| 2090 | `osint-methodology` | Comprehensive OSINT methodology for external red-team operations and authorized attack-surface assessments. |
| 2091 | `oss-hunter` | "Automatically hunt for high-impact OSS contribution opportunities in trending repositories." |
| 2092 | `osterwalder-canvas-architect` | "Iterative consultant agent for building and validating logically consistent 9-block Business Model Canvases." |
| 2093 | `ot-ics` | "Authorized OT/ICS security assessment: Purdue-model zoning review, PLC/SCADA exposure, industrial protocol discovery, and passive-first ... |
| 2094 | `outlook-automation` | "Automate Outlook tasks via Rube MCP (Composio): emails, calendar, contacts, folders, attachments. Always search tools first for current ... |
| 2095 | `outlook-calendar-automation` | "Automate Outlook Calendar tasks via Rube MCP (Composio): create events, manage attendees, find meeting times, and handle invitations. Al... |
| 2096 | `outreach-email-template-generator` | "Outreach Email Template Generator. Use when working with recipient context, outreach purpose and genuine offer." |
| 2097 | `outreachagent` | "Operate reply-aware cold outbound email workflows for AI agents with inboxes, contacts, templates, pacing, approvals, webhooks, and deli... |
| 2098 | `outreachgenie-list-audit` | "Audit saved OutreachGenie prospect lists against an outreach flow for missing template values, text limits and incomplete collection, us... |
| 2099 | `page-cro` | Analyze and optimize individual pages for conversion performance. |
| 2100 | `page-speed-score-simulator` | "Page Speed Score Simulator. Use when working with performance report or explicit hypothetical performance inputs." |
| 2101 | `pagerduty-automation` | "Automate PagerDuty tasks via Rube MCP (Composio): manage incidents, services, schedules, escalation policies, and on-call rotations. Alw... |
| 2102 | `pagespeed-enhancer` | "Scan, audit, and fix web performance issues across all four Lighthouse/PageSpeed Insights pillars — Performance, Accessibility, Best Pra... |
| 2103 | `paid-ads` | "You are an expert performance marketer who verifies available authorized account access before taking action. Your goal is to help creat... |
| 2104 | `pakistan-payments-stack` | "Design and implement production-grade Pakistani payment integrations (JazzCash, Easypaisa, bank/PSP rails, optional Raast) for SaaS with... |
| 2105 | `pangolinfo-amazon-data-research` | "Plan and run read-only Amazon product, review, category, seller, and market research through Pangolinfo's documented MCP bridge." |
| 2106 | `papers-skill` | "Skill for academic research workflows: search Semantic Scholar (200M+ papers), inspect citations, download arXiv PDFs, and extract PDF t... |
| 2107 | `paragraph-keyword-optimizer` | "Paragraph Keyword Optimizer. Use when working with paragraph and target keyword." |
| 2108 | `parallel-agents` | "Multi-agent orchestration patterns. Use when multiple independent tasks can run with different domain expertise or when comprehensive an... |
| 2109 | `parallel-search-mcp` | "Search the public web and verify sources with Parallel's free Search MCP. Use when the user chooses Parallel or its connected tools for ... |
| 2110 | `parasite-and-pr` | Prepare review-ready press, community and social syndication drafts around a verified launch or benchmark, with source and privacy checks. |
| 2111 | `parcel-coupon` | "Call parcel/courier coupon API to fetch one-stop logistics service coupons, including smart shipping and smart price matching. Returns c... |
| 2112 | `party-ledger-reconciliation` | 'Party ledger reconciliation: party type, name and PAN/VAT, ledger against statement balance, difference and reason, duplicates, confirma... |
| 2113 | `party-planning` | "Estimate party food and drink quantities, select games, and draft hosting timelines using HostPartyPlay's published planning heuristics." |
| 2114 | `patch-diff-exploit` | "Locate vulnerability fixes in vendor patches, diff binaries across versions, and build N-day PoCs. Attack-side complement to binary-diff... |
| 2115 | `payment-accounting` | 'Payment voucher register: payment number and date, paid to and purpose, mode, gross amount, TDS rate and deducted, net paid, invoice all... |
| 2116 | `payment-integration` | Integrate Stripe, PayPal, and payment processors. Handles checkout flows, subscriptions, webhooks, and PCI compliance. Use PROACTIVELY wh... |
| 2117 | `payments-received` | 'Payments received log: reference, client and invoice, amount and currency, payment date and method, withholding tax, bank account, recei... |
| 2118 | `paypal-integration` | "Master PayPal payment integration including Express Checkout, IPN handling, recurring billing, and refund workflows." |
| 2119 | `payroll-finance` | 'Payroll register: employee, department and month, basic, DA, HRA and TA, bonus, deductions, net pay, pay period, payment date and method... |
| 2120 | `paywall-upgrade-cro` | "You are an expert in in-app paywalls and upgrade flows. Your goal is to convert free users to paid, or upgrade users to higher tiers, at... |
| 2121 | `pci-compliance` | "Review payment data flows and engineering control evidence for a scoped PCI assessment, without claiming certification." |
| 2122 | `pci-dss-compliance` | Implement PCI DSS requirements for payment card data. Configure cardholder data environment and security controls. Use when processing pa... |
| 2123 | `pdf-conversion-router` | Use when converting a PDF into another format such as Markdown, HTML, text, JSON, DOCX, or structured notes and the agent must choose the... |
| 2124 | `penetration-testing` | Perform basic penetration testing and security assessments. |
| 2125 | `pennylane` | "Write, simulate and train PennyLane quantum circuits: QNodes, devices, templates, measurements, autodiff with NumPy/JAX/PyTorch, gradien... |
| 2126 | `pentest-checklist` | "Provide a comprehensive checklist for planning, executing, and following up on penetration tests. Ensure thorough preparation, proper sc... |
| 2127 | `pentest-commands` | "Provide a comprehensive command reference for penetration testing tools including network scanning, exploitation, password cracking, and... |
| 2128 | `pentest-tools` | "Operate 20+ penetration-testing tools (Nmap, Nuclei, SQLMap, FFUF, Hashcat, and more) through structured workflows with consistent outpu... |
| 2129 | `people-data` | "Research LinkedIn professional profiles and public business-contact data, including email/phone lookup, people search, and YouTube chann... |
| 2130 | `people-directory` | 'Employee master record: name, employee id, department, job title, grade, manager, employment type, contact and emergency details, access... |
| 2131 | `performance-audit-static` | 'Only when a performance audit is asked for (ship-check asks by name; a release proposes, never runs it): static audit of N+1 queries, ov... |
| 2132 | `performance-engineer` | "Diagnose performance bottlenecks using profiling, traces, load tests, and observability; verify latency and capacity improvements." |
| 2133 | `performance-management` | 'Performance review register: review type, period, employee and reviewer, KPI, OKR and behaviour scores, overall rating, PIP and promotio... |
| 2134 | `performance-optimization` | Optimizes application performance. Use when performance requirements exist, when you suspect performance regressions, or when Core Web Vi... |
| 2135 | `performance-optimizer` | "Identifies and fixes performance bottlenecks in code, databases, and APIs. Measures before and after to prove improvements." |
| 2136 | `performance-profiling` | "Performance profiling principles. Measurement, analysis, and optimization techniques." |
| 2137 | `performance-testing-review-ai-review` | "Review performance-sensitive code changes with reproducible baselines, workload metrics, static analysis and evidence-backed findings." |
| 2138 | `performance-testing-review-multi-agent-review` | "Review a defined code diff from relevant correctness, authorization and performance perspectives; delegate only when authorized and repr... |
| 2139 | `performance-tuning` | Optimize Linux system performance. Configure kernel parameters, analyze bottlenecks, and tune resources. Use when improving system perfor... |
| 2140 | `permission-manager` | "Manage opencode permissions: review always-allow lists, suggest safe read-only commands, configure permission patterns" |
| 2141 | `perp-dex-costs` | "Before a perpetual futures trade, find which perp DEX is cheapest now for the size (fees plus slippage on the live book) and compare fun... |
| 2142 | `perq` | "Find verified free AI credits, free tiers, startup programs and student perks for AI APIs, GPUs and dev tools, each with the vendor's so... |
| 2143 | `personal-tool-builder` | Expert in building custom tools that solve your own problems first. The best products often start as personal tools - scratch your own it... |
| 2144 | `petty-cash-management` | 'Petty cash register: entry number, date and type, payee and purpose, cash in and out, running balance, cash limit flag, custodian, physi... |
| 2145 | `phase-gated-debugging` | "Use when debugging any bug. Enforces a 5-phase protocol where code edits are blocked until root cause is confirmed. Prevents premature f... |
| 2146 | `photopea-embedded-editor` | Embed Photopea in web apps using photopea.js. Covers embedding, file I/O, scripting, exporting, layers, text, filters, and selected Photo... |
| 2147 | `php-pro` | 'Write idiomatic PHP code with generators, iterators, SPL data structures, and modern OOP features. Use PROACTIVELY for high-performance ... |
| 2148 | `pi-custom-model` | "Register custom Pi Agent model slugs so saved OpenRouter variants resolve correctly." |
| 2149 | `pi-delegate` | Delegate coding tasks to the Pi coding agent CLI (`pi`) only when the user explicitly requests it, while the orchestrator retains review ... |
| 2150 | `pi-web-search` | "Give Pi Agents a safe web-search and fetch workflow using the installed pi-web-access package." |
| 2151 | `pick-ui-library` | "Choose a frontend library from Emil Kowalski’s curated list after checking the project’s existing stack and requirements." |
| 2152 | `pilot-protocol` | "Give an AI agent a permanent network address, encrypted P2P messaging, and an installable app store via Pilot Protocol" |
| 2153 | `piloterr-mcp` | "Get structured JSON from 391 Piloterr scraping endpoints (Amazon, LinkedIn, Zillow, Crunchbase, Google...) through Piloterr's MCP server... |
| 2154 | `pipecat-friday-agent` | "Build a low-latency, Iron Man-inspired tactical voice assistant (F.R.I.D.A.Y.) using Pipecat, Gemini, and OpenAI." |
| 2155 | `pipedrive-automation` | "Automate Pipedrive CRM operations including deals, contacts, organizations, activities, notes, and pipeline management via Rube MCP (Com... |
| 2156 | `pitch-psychologist` | "Structure pitches, decks, and talk tracks around audience beliefs, proof, and a clear decision when presentations need stronger progress... |
| 2157 | `pixeltable` | "Build Pixeltable apps for multimodal RAG, video and image search, audio transcription, agent memory, embeddings stored with the data, in... |
| 2158 | `placecall` | "Place real outbound phone calls to US businesses through the PlaceCall API: book, ask, get quotes, then read the outcome and transcript." |
| 2159 | `plaid-fintech` | Expert patterns for Plaid API integration including Link token flows, transactions sync, identity verification, Auth for ACH, balance che... |
| 2160 | `plan-ledger-tasks-yylo` | Create a concise Product Development Requirement and one or more implementation-sized YYLO Ledger tasks when the user explicitly asks to ... |
| 2161 | `plan-writing` | "Structured task planning with clear breakdowns, dependencies, and verification criteria. Use when implementing features, refactoring, or... |
| 2162 | `planetscale` | Operate MySQL-compatible databases on PlanetScale with branching workflows, safe migrations, and production rollouts. |
| 2163 | `planning-and-task-breakdown` | Breaks work into ordered tasks. Use when you have a spec or clear requirements and need to break work into implementable tasks. Use when ... |
| 2164 | `planning-with-files` | "Work like Manus: Use persistent markdown files as your \"working memory on disk.\"" |
| 2165 | `platform-engineering` | Build internal developer platforms (IDPs) with self-service infrastructure, golden paths, and developer portals using Backstage, Crosspla... |
| 2166 | `playwright-cli` | Automate browser interactions, test web pages and work with Playwright tests. |
| 2167 | `playwright-java` | "Scaffold, write, debug, and enhance enterprise-grade Playwright E2E tests in Java using Page Object Model, JUnit 5, Allure reporting, an... |
| 2168 | `playwright-skill` | "Write and run scoped Playwright browser automation, responsive checks, screenshots and login-flow tests with a local Node executor." |
| 2169 | `plotly` | Interactive visualization library. Use when you need hover info, zoom, pan, or web-embeddable charts. Best for dashboards, exploratory an... |
| 2170 | `podcast-generation` | "Generate real audio narratives from text content using Azure OpenAI's Realtime API." |
| 2171 | `podman` | Manage containers using Podman, the daemonless container engine. |
| 2172 | `poka-yoke` | "Mistake-proof code, config and process: make the wrong action impossible or self-announcing rather than documented." |
| 2173 | `polars` | Expression-based DataFrame library for Python and Rust. Use for eager or lazy tabular analytics, ETL, and pandas migration; streaming sup... |
| 2174 | `policy-acknowledgement` | 'Policy acknowledgement register: employee, policy and version, sent and due dates, acknowledged date and flag, days overdue, reminder se... |
| 2175 | `policy-as-code` | Implement policy as code with OPA, Sentinel, and Kyverno. Automate policy enforcement in CI/CD and infrastructure. Use when enforcing com... |
| 2176 | `policy-library` | 'Policy register: name, version, category, owner and approver, applies to, compliance framework, acknowledgement requirement, effective d... |
| 2177 | `polis-protocol` | "Coordinate multi-vendor AI agents as a self-improving team — a learning router assigns work by track record and citizens can amend the p... |
| 2178 | `polis-protocol-a-self-optimizing-city-of-agents` | "Polis Protocol: A Self-Optimizing City of Agents" |
| 2179 | `ponder` | "Run coverage-gated multi-pass code, architecture, security, UI, or product reviews where every file must be graded and 4 perspectives de... |
| 2180 | `popup-cro` | "Create and optimize popups, modals, overlays, slide-ins, and banners to increase conversions without harming user experience or brand tr... |
| 2181 | `posix-shell-pro` | Expert in strict POSIX sh scripting for maximum portability across Unix-like systems. Specializes in shell scripts that run on any POSIX-... |
| 2182 | `post` | "Make share-post image sets that look native: Xiaohongshu carousels, X images, covers, App Store poster layouts, real screenshots and fai... |
| 2183 | `postel-writing` | "Find posts going viral in the user's niche, write their own version in their voice for X (Twitter), LinkedIn, Bluesky or Mastodon, and s... |
| 2184 | `poster-design-studio` | "Install and use the official AI Poster Maker package, pinned by digest, for paid hosted work on the Beatra service." |
| 2185 | `postgres-best-practices` | "Postgres performance optimization and best practices from Supabase. Use this skill when writing, reviewing, or optimizing Postgres queri... |
| 2186 | `postgres-readonly-queries` | "Execute safe read-only SQL queries against PostgreSQL databases with multi-connection support and defense-in-depth write protection." |
| 2187 | `postgresql` | "Design a PostgreSQL-specific schema. Covers best-practices, data types, indexing, constraints, performance patterns, and advanced features" |
| 2188 | `postgresql-cli` | "PostgreSQL interactive terminal (psql) reference and usage guide." |
| 2189 | `postgresql-devsec` | Administer PostgreSQL databases. Configure replication, backups, and performance tuning. Use when managing PostgreSQL deployments. |
| 2190 | `postgresql-optimization` | "PostgreSQL database optimization workflow for query tuning, indexing strategies, performance analysis, and production database management." |
| 2191 | `posthog-automation` | "Automate PostHog tasks via Rube MCP (Composio): events, feature flags, projects, user profiles, annotations. Always search tools first f... |
| 2192 | `postman-collection-generator` | "Generate complete, import-ready Postman Collection v2.1 JSON files from natural language API descriptions or cURL commands." |
| 2193 | `postman-newman-automation` | "Generate Newman CLI commands, configuration files, Jenkins pipeline scripts, and shell automation for running Postman collections in CI/... |
| 2194 | `postman-openapi-converter` | "Convert OpenAPI 3.x or Swagger 2.0 specs (YAML or JSON) into complete, import-ready Postman Collection v2.1 JSON files." |
| 2195 | `postmark-automation` | "Automate Postmark email delivery tasks via Rube MCP (Composio): send templated emails, manage templates, monitor delivery stats and boun... |
| 2196 | `postmortem-writing` | "Comprehensive guide to writing effective, blameless postmortems that drive organizational learning and prevent incident recurrence." |
| 2197 | `power-user-cultivation` | "When the user wants to identify and nurture developer advocates, build champion programs, or turn active users into contributors and eva... |
| 2198 | `powershell-windows` | "PowerShell Windows patterns. Critical pitfalls, operator syntax, error handling." |
| 2199 | `ppl-personal-crm` | "Uses the ppl personal CRM over MCP to prepare for conversations, recall facts about people, log interactions and manage relationship fol... |
| 2200 | `pptx-deck-creation` | "Create editable, production-ready PPTX decks with narrative planning, explicit layout specs, asset guidance, and quality checks." |
| 2201 | `pr-merge-champion` | "Optimize pull requests for quick approval and merging by ensuring clean diffs, comprehensive self-reviews, and structured documentation." |
| 2202 | `pr-writer` | "Create pull requests following Sentry's engineering practices." |
| 2203 | `pre-boarding` | 'Pre-boarding checklist: task, employee and department, owner, category, joining and due dates, documents received, laptop, email and acc... |
| 2204 | `pre-release-review` | "Run a read-only pre-release review for deploy readiness, migrations, config, secrets, rollout order, rollback risk, and launch blockers." |
| 2205 | `pre-ship-gate` | "A ship gate that runs before any production deploy: checks the silent failure modes that make a deploy 'succeed' while prod stays broken... |
| 2206 | `premium-3d-website` | Guidelines for building premium 3D websites, focusing on custom WebGL shaders, post-processing, physics-based interactions, smooth animat... |
| 2207 | `presentation-deck` | 'Build an evidence-linked slide register after context-first intake. Use when an SME needs a presentation deck, speaker notes, or a struc... |
| 2208 | `price-psychology-strategist` | "Design pricing presentation, anchors, and tiers when an offer needs clearer value and fairness without misleading comparisons." |
| 2209 | `pricing` | "When the user wants help with pricing decisions, packaging, or monetization strategy." |
| 2210 | `pricing-strategy` | "Design pricing, packaging, and monetization strategies based on value, customer willingness to pay, and growth objectives." |
| 2211 | `prisma-expert` | "You are an expert in Prisma ORM with deep knowledge of schema design, migrations, query optimization, relations modeling, and database o... |
| 2212 | `privacy-by-design` | "Use when building apps that collect user data. Ensures privacy protections are built in from the start—data minimization, consent, encry... |
| 2213 | `privacy-mask` | "Mask, redact, anonymize and censor sensitive information (PII) in screenshots and images — phone numbers, emails, IDs, API keys, crypto ... |
| 2214 | `privilege-escalation-methods` | "Provide comprehensive techniques for escalating privileges from a low-privileged user to root/administrator access on compromised Linux ... |
| 2215 | `pro-launch` | "Build an app or product from 0 to 1, taste-first, with phase gates: references, naming, style frames, UI loop, launch video, GTM and shi... |
| 2216 | `pro-motion` | "Make a motion-graphics launch, brand or promo film audio first: plan the music, then render the film in code (canvas to MP4) cut to the ... |
| 2217 | `probation-tracker` | 'Probation register: employee, start and end dates, 30, 60 and 90-day review scores, overall score and confirmation letter. Use for proba... |
| 2218 | `product-analytics` | 'Adding analytics, session recordings, heatmaps, ''what did users do'', Clarity or PostHog: behaviour analytics without analytics cookies... |
| 2219 | `product-decision-agent` | "中文产品决策 Agent。用于需求优先级、Roadmap、增长、留存、运营、数据异常、A/B Test、项目延期和跨团队协作；先判断事实、阶段、核心阻塞与主导机制，再给出下一步、停止清单和切换条件。默认中文，不引用原文或讲历史。" |
| 2220 | `product-description-generator` | "Product Description Generator. Use when working with verified product features and intended buyer." |
| 2221 | `product-design` | "Design de produto nivel Apple — sistemas visuais, UX flows, acessibilidade, linguagem visual proprietaria, design tokens, prototipagem e... |
| 2222 | `product-design-harness` | Use when a product direction, feature, workflow, experiment, launch, feedback signal, automation, or scale decision needs judgment before... |
| 2223 | `product-engineering-competitor-analysis` | 'Competitive research or a competitive brief: competitors and substitutes, their strengths and weaknesses, where to differentiate.' |
| 2224 | `product-engineering-propose` | '''I have an idea'', ''is this worth building'', ''what next'': research it and propose what to build, with sources and key screens to re... |
| 2225 | `product-engineering-retro` | 'Build a session''s learnings into the setup: its friction, what went wrong and why, then an improved instruction, route, hook or script,... |
| 2226 | `product-engineering-start-here` | 'Where to start, and what comes next, along the product lifecycle: from a new idea, new evidence, an agreed change, a bug or a release to... |
| 2227 | `product-inventor` | "Product Inventor e Design Alchemist de nivel maximo — combina Product Thinking, Design Systems, UI Engineering, Psicologia Cognitiva, St... |
| 2228 | `product-manager` | "Guide product strategy, discovery, prioritization and metrics; upstream templates and formula collections are external prerequisites." |
| 2229 | `product-manager-toolkit` | "Essential tools and frameworks for modern product management, from discovery to delivery." |
| 2230 | `product-marketing` | "When the user wants to create or update their product marketing context document." |
| 2231 | `product-marketing-context` | "Create or update a reusable product marketing context document with positioning, audience, ICP, use cases, and messaging. Use at the sta... |
| 2232 | `product-photo-studio` | "Install and use the official AI Product Photography package, pinned by digest, for paid hosted work on the Beatra service." |
| 2233 | `production-audit` | "Audit a shipped repo for production-readiness gaps across RLS, webhooks, secrets, grants, Stripe idempotency, mobile UX, and deployment ... |
| 2234 | `production-code-audit` | "Audit an explicitly scoped codebase for evidenced security, correctness and performance issues; implement authorized targeted repairs an... |
| 2235 | `production-runtime-certification` | "Certify a deployed service with fresh evidence across source, CI, migrations, runtime health, readiness, and critical routes; use before... |
| 2236 | `production-scheduling` | Codified expertise for production scheduling, job sequencing, line balancing, changeover optimisation, and bottleneck resolution in discr... |
| 2237 | `professional-proofreader` | Use when a user asks to "proofread", "review and correct", "fix grammar", "improve readability while keeping my voice", and to proofread ... |
| 2238 | `programmatic-seo` | Design and evaluate programmatic SEO strategies for creating SEO-driven pages at scale using templates and structured data. |
| 2239 | `progressive-estimation` | "Estimate AI-assisted and hybrid human+agent development work with explicit PERT assumptions and calibration feedback loops" |
| 2240 | `progressive-web-app` | "Build Progressive Web Apps (PWAs) with offline support, installability, and caching strategies. Trigger whenever the user mentions PWA, ... |
| 2241 | `project-based-performance` | 'Project performance review: role, project and manager, delivery, quality and collaboration scores, overall score and feedback. Use for p... |
| 2242 | `project-brief` | "Project Detail Optimizer. Use when working with one sentence, rough notes or an existing project brief." |
| 2243 | `project-development` | "This skill covers the principles for identifying tasks suited to LLM processing, designing effective project architectures, and iteratin... |
| 2244 | `project-memory-log` | "Maintain one operation log and one deduplicated document catalog for long-running projects. Use when resuming project work or tracing du... |
| 2245 | `project-skill-audit` | Audit a project and recommend the highest-value skills to add or update. |
| 2246 | `project-state-governor` | "Govern evidence-backed canonical project state across sessions, branches, reviews, and research cycles without inventing product intent." |
| 2247 | `projection-patterns` | "Build read models and projections from event streams. Use when implementing CQRS read sides, building materialized views, or optimizing ... |
| 2248 | `projects-work-management` | 'Project register: owner, team, priority, progress percentage, milestones, deliverables and budget against actual cost. Use for project t... |
| 2249 | `prometheus-configuration` | "Complete guide to Prometheus setup, metric collection, scrape configuration, and recording rules." |
| 2250 | `prometheus-grafana` | Set up metrics collection and visualization with Prometheus and Grafana. |
| 2251 | `promotion-upgrade-requests` | 'Promotion register: current and requested role and grade, justification, OKR and behaviour scores, time in role, salary proposal and dec... |
| 2252 | `prompt-caching` | Caching strategies for LLM prompts including Anthropic prompt caching, response caching, and CAG (Cache Augmented Generation) |
| 2253 | `prompt-engineer` | "Transforms user prompts into optimized prompts using frameworks (RTF, RISEN, Chain of Thought, RODES, Chain of Density, RACE, RISE, STAR... |
| 2254 | `prompt-engineering` | "Expert guide on prompt engineering patterns, best practices, and optimization techniques. Use when user wants to improve prompts, learn ... |
| 2255 | `prompt-engineering-patterns` | "Master advanced prompt engineering techniques to maximize LLM performance, reliability, and controllability." |
| 2256 | `prompt-injection-defense` | Defend AI systems against prompt injection and indirect prompt attacks using input controls, tool permissions, output validation, and iso... |
| 2257 | `prompt-library` | "A comprehensive collection of battle-tested prompts inspired by [awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) ... |
| 2258 | `proof-kb` | "Maintain a source-linked knowledge base of first-hand SEO evidence and update pages that depend on superseded facts." |
| 2259 | `protect-mcp-governance` | "Agent governance skill for MCP tool calls — Cedar policy authoring, shadow-to-enforce rollout, and Ed25519 receipt verification." |
| 2260 | `protocol-reverse` | "Authorized reverse engineering of custom binary protocols, Protobuf/gRPC schemas, WebSocket frames, and PCAP-driven protocol recovery." |
| 2261 | `protocol-reverse-engineering` | "Comprehensive techniques for capturing, analyzing, and documenting network protocols for security research, interoperability, and debugg... |
| 2262 | `prototype` | Build a throwaway prototype to flesh out a design — a runnable terminal app for state/business-logic questions, or several radically diff... |
| 2263 | `provider-health` | "Starter: one-screen provider health summary — availability, auth method, version drift, and cost posture for every seatable provider" |
| 2264 | `public-relations` | "When the user wants help with public relations, earned media, press coverage, journalist outreach, or media strategy (not pull requests)." |
| 2265 | `pubmed-database` | Direct REST API access to PubMed. Advanced Boolean/MeSH queries, E-utilities API, batch processing, citation management. For Python workf... |
| 2266 | `punchtape` | Use a user-authorized punchtape zone to verify agreed project checks and record a machine verdict. |
| 2267 | `puppeteer-skill` | 'Generates Puppeteer scripts for browser automation, scraping, and PDF generation. Triggers on: "Puppeteer", "headless Chrome", "page.got... |
| 2268 | `purchase-accounting` | 'Purchase register: supplier, invoice, gross amount, VAT and TDS, net payable, ledger account and payment balance. Use for purchase accou... |
| 2269 | `push-skill-to-github` | "Commit and push skill changes to the configured skills repository after review and validation." |
| 2270 | `puzzle-activity-planner` | "Plan puzzle-based activities for classrooms, parties, and events with pre-configured generator links" |
| 2271 | `pwn-chain` | "Go from reverse engineering to a working exploit: stack/heap/kernel pwn workflows with pwntools, libc-database, ROP, and stabilization f... |
| 2272 | `pydantic-ai` | "Build production-ready AI agents with PydanticAI — type-safe tool use, structured outputs, dependency injection, and multi-model support." |
| 2273 | `pydantic-models-py` | "Create Pydantic models following the multi-model pattern for clean API contracts." |
| 2274 | `pypict-skill` | "Pairwise test generation" |
| 2275 | `pytest-skill` | "Generates production-grade pytest tests in Python with fixtures, parametrize, markers, mocking, and conftest patterns. Use when user men... |
| 2276 | `python-development` | "You are a Python project architecture expert specializing in scaffolding production-ready Python applications. Generate complete project... |
| 2277 | `python-development-python-scaffold` | "You are a Python project architecture expert specializing in scaffolding production-ready Python applications. Generate complete project... |
| 2278 | `python-fastapi-development` | "Python FastAPI backend development with async patterns, SQLAlchemy, Pydantic, authentication, and production API patterns." |
| 2279 | `python-packaging` | "Comprehensive guide to creating, structuring, and distributing Python packages using modern packaging tools, pyproject.toml, and publish... |
| 2280 | `python-patterns` | "Python development principles and decision-making. Framework selection, async patterns, type hints, project structure. Teaches thinking,... |
| 2281 | `python-performance-optimization` | "Profile and optimize Python code using cProfile, memory profilers, and performance best practices. Use when debugging slow Python code, ... |
| 2282 | `python-pptx-generator` | "Generate complete Python scripts that build polished PowerPoint decks with python-pptx and real slide content." |
| 2283 | `python-pro` | Master Python 3.12+ with modern features, async programming, performance optimization, and production-ready practices. Expert in the late... |
| 2284 | `python-testing-patterns` | "Implement comprehensive testing strategies with pytest, fixtures, mocking, and test-driven development. Use when writing Python tests, s... |
| 2285 | `qiskit` | "Build and transpile Qiskit circuits, test local simulators and prepare authorized hardware workloads with Sampler/Estimator primitives." |
| 2286 | `qoder-delegate` | Delegate coding tasks to the Qoder CLI (`qodercli`) only when the user explicitly requests it, while the orchestrator retains review and ... |
| 2287 | `qrx` | "Make branded, print-ready art QR codes to validate before use with QRX (qrx.codes). Use when a link needs a QR code that looks like artw... |
| 2288 | `quality-nonconformance` | Operational guidance for quality control, non-conformance investigation, root cause analysis, corrective action, and supplier quality man... |
| 2289 | `quant-analyst` | Build financial models, backtest trading strategies, and analyze market data. Implements risk metrics, portfolio optimization, and statis... |
| 2290 | `quit-sponsor` | "Helps an AI agent provide non-judgmental, evidence-informed quit-smoking support with user-consented tracking, craving check-ins, and es... |
| 2291 | `qurl-private-review` | "Share one local web app with an approved browser reviewer through qURL, check the app loads, and delete the share when the review ends." |
| 2292 | `radar-satellite-analysis` | "Interpret weather radar and satellite observations by validating product metadata and geometry, deriving storm and cloud structures, tra... |
| 2293 | `radare2` | "Drive the radare2 CLI for binary reconnaissance, disassembly, analysis, function locating, export, and lightweight patching (r2/rabin2/r... |
| 2294 | `radio-sdr` | "Authorized RF/SDR security research: signal identification, replay-feasibility study in shielded labs, and wireless protocol analysis wi... |
| 2295 | `radix-ui-design-system` | "Build accessible design systems with Radix UI primitives. Headless component customization, theming strategies, and compound component p... |
| 2296 | `rag-engineer` | Expert in building Retrieval-Augmented Generation systems. Masters embedding models, vector databases, chunking strategies, and retrieval... |
| 2297 | `rag-implementation` | "RAG (Retrieval-Augmented Generation) implementation workflow covering embedding selection, vector database setup, chunking strategies, a... |
| 2298 | `rag-infrastructure` | Build and operate Retrieval-Augmented Generation (RAG) infrastructure with vector stores, embedding pipelines, and hybrid search. |
| 2299 | `rag-observability-evals` | Monitor and evaluate RAG systems with retrieval quality metrics, groundedness checks, hallucination detection, and continuous regression ... |
| 2300 | `ralph-loop-yylo` | Execute exactly one explicitly assigned YYLO Ledger task through the Ralph loop to a validated queued commit. Use only when the user expl... |
| 2301 | `ranking-opportunity-finder` | "Ranking Opportunity Finder. Use when working with query/page performance export or dated ranking evidence." |
| 2302 | `ranking-progress-tracker` | "Ranking Progress Tracker. Use when working with dated keyword positions with engine, market and device." |
| 2303 | `rayden-code` | Generate React code with Rayden UI components using correct props, tokens, and premium layout patterns |
| 2304 | `rayden-use` | Build and maintain Rayden UI components and screens in Figma via Figma MCP with full design token enforcement |
| 2305 | `rclone-cli` | "Rclone command-line cloud storage manager reference and usage guide. Use this skill whenever the user mentions rclone, or any task invol... |
| 2306 | `re-create` | "Completely delete and rewrite a file or module from scratch when structural rot makes patching impossible." |
| 2307 | `rea-growth` | "Analyze a company’s public growth and content through Treg, distinguish observations from hypotheses, and produce an evidence-linked pla... |
| 2308 | `react-best-practices` | "Comprehensive performance optimization guide for React and Next.js applications, adapted from Vercel’s published guidance. Use when writ... |
| 2309 | `react-component-performance` | Diagnose slow React components and suggest targeted performance fixes. |
| 2310 | `react-flow-architect` | "Build production-ready ReactFlow applications with hierarchical navigation, performance optimization, and advanced state management." |
| 2311 | `react-flow-node-ts` | "Create React Flow node components following established patterns with proper TypeScript types and store integration." |
| 2312 | `react-modernization` | "Master React version upgrades, class to hooks migration, concurrent features adoption, and codemods for automated transformation." |
| 2313 | `react-native-architecture` | "Architecture and integration patterns for React Native development with Expo, including navigation, state management, native modules, an... |
| 2314 | `react-native-skills` | "Review React Native and Expo rendering, lists, animations, navigation and native UI against project versions and measured behavior." |
| 2315 | `react-nextjs-development` | "React and Next.js 14+ application development with App Router, Server Components, TypeScript, Tailwind CSS, and modern frontend patterns." |
| 2316 | `react-patterns` | "Modern React patterns and principles. Hooks, composition, performance, TypeScript best practices." |
| 2317 | `react-state-management` | "Master modern React state management with Redux Toolkit, Zustand, Jotai, and React Query. Use when setting up global state, managing ser... |
| 2318 | `react-ui-patterns` | "Modern React UI patterns for loading states, error handling, and data fetching. Use when building UI components, handling async data, or... |
| 2319 | `read-all-adrs` | "Read every ADR in a project before summarizing architectural context or decisions." |
| 2320 | `readability-enhancer` | "Readability Enhancer. Use when working with text and optional reader level." |
| 2321 | `readability-score-calculator` | "Readability Score Calculator. Use when working with text and language." |
| 2322 | `readme` | "You are an expert technical writer creating comprehensive project documentation. Write an accurate README sized to the project and task,... |
| 2323 | `recallmax` | "Prepare source-linked conversation handoffs and bounded document summaries, preserving decisions, uncertainty and task state within the ... |
| 2324 | `receipt-accounting` | 'Receipt register: payer, mode, gross amount received, invoice allocation, unapplied amount and TDS collected. Use for receipt and sales-... |
| 2325 | `receiving-code-review` | Use when receiving code review feedback, before implementing suggestions, especially if feedback seems unclear or technically questionabl... |
| 2326 | `recognition-rewards` | 'Recognition register: employee, reward type, category, visibility, message and points awarded. Use for employee recognition programs.' |
| 2327 | `recon-scope-triage` | Triage ASM/recon output for ownership before testing |
| 2328 | `recruit` | "Turn a job description into an evidence-linked candidate shortlist through Treg, with job-related ranking and optional authorized busine... |
| 2329 | `recruitment-pipeline` | 'Recruitment pipeline: candidate, position, stage, source, applied and interview dates, interview score, notice period and offer. Use for... |
| 2330 | `recsys-pipeline-architect` | "Designs composable recommendation, ranking, and feed pipelines using the six-stage Source→Hydrator→Filter→Scorer→Selector→SideEffect fra... |
| 2331 | `recursive-context-pruning-token-budgeting` | "Optimizes AI agent performance by pruning redundant context, managing token usage, and enforcing ultra-concise, direct-to-value responses." |
| 2332 | `red-team-tactics` | "Red team tactics principles based on MITRE ATT&CK. Attack phases, detection evasion, reporting." |
| 2333 | `red-team-tools` | "Implement proven methodologies and tool workflows from top security researchers for effective reconnaissance, vulnerability discovery, a... |
| 2334 | `reddit-automation` | "Automate Reddit tasks via Rube MCP (Composio): search subreddits, create posts, manage comments, and browse top content. Always search t... |
| 2335 | `reddit-serp` | Find relevant public Reddit threads in search or citation reports and draft transparent practitioner replies for user review. |
| 2336 | `redesign-existing-projects` | "Use when upgrading existing websites or apps by auditing generic UI patterns and applying premium design fixes without rewrites." |
| 2337 | `redirect-301-generator` | "301 Redirect Generator. Use when working with source-to-destination mapping and deployment platform." |
| 2338 | `redirect-checker` | "Redirect Checker. Use when working with URL or recorded response chain." |
| 2339 | `redis` | Configure Redis for caching and data storage. Set up clustering, persistence, and Sentinel. Use when implementing Redis caching or queues. |
| 2340 | `redis-cli` | "Redis command-line interface (redis-cli) reference and usage guide. Use this skill whenever the user mentions redis-cli, Redis CLI, or a... |
| 2341 | `redteam-mindset` | Red-team operator discipline |
| 2342 | `redteam-report-template` | Client-facing red-team deliverable format |
| 2343 | `reference-builder` | Creates exhaustive technical references and API documentation. Generates comprehensive parameter listings, configuration guides, and sear... |
| 2344 | `referral-program` | "You are an expert in viral growth and referral marketing using only referral data and tools actually available and authorized. Your goal... |
| 2345 | `rehabilitation-analyzer` | 分析康复训练数据、识别康复模式、评估康复进展，并提供个性化康复建议 |
| 2346 | `release-gate` | 'Before ''push it'', ''ship it'', a deploy, release or go-live, or calling a stage done: the gate, the owner''s preview, go/no-go, promot... |
| 2347 | `remote-gpu-trainer` | "Deploy, monitor, and debug long GPU jobs on RENTED/remote instances (AutoDL, RunPod, vast.ai, Lambda, Slurm, K8s): teardown/billing safe... |
| 2348 | `remote-work-tracker` | 'Remote work register: employee, location, week start, HQ versus remote days, core-hours compliance and manager approval. Use for hybrid ... |
| 2349 | `remotion` | Generate walkthrough videos from Stitch projects using Remotion with smooth transitions, zooming, and text overlays |
| 2350 | `remotion-best-practices` | "Best practices for Remotion - Video creation in React" |
| 2351 | `remotion-captions` | Transcribing, displaying and animating captions |
| 2352 | `remotion-create` | Create a new Remotion video |
| 2353 | `remotion-docs` | Search Remotion documentation |
| 2354 | `remotion-interactivity` | Structure Remotion markup for interactivity |
| 2355 | `remotion-render` | Export a Remotion video |
| 2356 | `remotion-to-hyperframes` | "Migrate Remotion or other animation code and footage into HyperFrames, recording editability and frame comparison limits." |
| 2357 | `remove-animations` | "Remove unnecessary interface motion while preserving final states, focus, layout, and animation-dependent behavior." |
| 2358 | `render-automation` | "Automate Render tasks via Rube MCP (Composio): services, deployments, projects. Always search tools first for current schemas." |
| 2359 | `renhua` | "Write Chinese social posts and product copy in a real person's voice, removing AI tells. Use for 小红书, X 帖子, 日记, 朋友圈, 产品介绍, 去 AI 味, 说人话." |
| 2360 | `repo-foundation` | "Implement features, fixes, modules, contract migrations, and resumed work while preserving user edits and authorized public contracts." |
| 2361 | `repo-maintainer` | "Audit and repair repository hygiene across artifacts, dependencies, CI, docs, Git state, and code-quality signals. Use for repository ma... |
| 2362 | `repo-native-refactor` | "Review diffs without editing, or perform evidence-based cleanup while preserving authorized behavior, public contracts, and domain owner... |
| 2363 | `report-writing` | Bug bounty report writing for H1/Bugcrowd/Intigriti/Immunefi |
| 2364 | `reports-analytics` | 'Report register: type, source modules, owner, audience, frequency, last and next run and report link. Use for reporting governance.' |
| 2365 | `repurpose-into-a-post` | "Turn an article, newsletter, transcript or video into a Twitter or LinkedIn post that stands on its own. Use when someone wants to repur... |
| 2366 | `requesting-code-review` | Use when completing tasks, implementing major features, or before merging to verify work meets requirements |
| 2367 | `requirements-writing` | "Write and review verifiable requirements using EARS patterns, quality checks, defect review, and traceability." |
| 2368 | `research-prompt` | "Turn vague research needs into one precise deep-research prompt with context and output criteria." |
| 2369 | `resolving-merge-conflicts` | Use when you need to resolve an in-progress git merge/rebase conflict. |
| 2370 | `restosignals` | "Find US restaurants and bars before they open, as scored leads fused from liquor-license, food-permit and business-filing records, via t... |
| 2371 | `resumable-implementation-contracts` | "Create repository-based execution contracts for multi-session implementation work, with stable task IDs, evidence, checkpoints, and exac... |
| 2372 | `returns-reverse-logistics` | Codified expertise for returns authorisation, receipt and inspection, disposition decisions, refund processing, fraud detection, and warr... |
| 2373 | `reverse-browser-automation` | "Automate browsers (Playwright) and Windows desktop applications (UI automation) for reverse-engineering evidence collection, UI-driven w... |
| 2374 | `reverse-engineer` | Expert reverse engineer specializing in binary analysis, disassembly, decompilation, and software analysis. Masters IDA Pro, Ghidra, rada... |
| 2375 | `reverse-engineer-anything` | Use REA to investigate shipped apps, binaries, packages, and runtimes; trace features with evidence, compare versions, or guide reconstru... |
| 2376 | `reverse-engineering` | "General reverse-engineering methodology for compiled, obfuscated, packed, or virtualized targets: GDB, Frida, angr, Unicorn, and Qiling ... |
| 2377 | `reverse-image-search` | "Reverse Image Search. Use when working with image or public image URL." |
| 2378 | `reverse-proxy` | Configure nginx and Traefik as reverse proxies. Implement SSL termination and routing. Use when setting up application gateways. |
| 2379 | `review-and-simplify-changes` | "Review a git diff or explicit file scope for reuse, code quality, efficiency, clarity, and standards issues, then optionally apply safe ... |
| 2380 | `review-animations` | "Review motion code against a craft, performance, accessibility, and interaction-quality standard with evidence." |
| 2381 | `review-multi-agent-orchestration` | "Use when a supervisor, swarm, graph, planner-worker system, or parallel agent workflow needs review for task boundaries, shared state, b... |
| 2382 | `review-response-generator` | "Review Response Generator. Use when working with review text and verified business context." |
| 2383 | `review-swarm` | "Parallel read-only multi-agent review of a current git diff or explicit file scope to find behavioral regressions, security or privacy r... |
| 2384 | `revops` | "Design and improve revenue operations, lead lifecycle rules, scoring, routing, handoffs, and CRM process automation. Use when marketing,... |
| 2385 | `rich-elicitation` | "Asks clarifying questions in multiple rounds before starting ambiguous tasks. Fires when 2+ task dimensions each have 3+ viable answers." |
| 2386 | `riffkit` | "Create short videos with Riffkit: Adapt a source formula, Swap approved footage, or generate from an idea. Use for UGC ads and localized... |
| 2387 | `risk-manager` | Monitor portfolio risk, R-multiples, and position limits. Creates hedging strategies, calculates expectancy, and analyzes proposed stop-l... |
| 2388 | `risk-metrics-calculation` | "Calculate portfolio risk metrics including VaR, CVaR, Sharpe, Sortino, and drawdown analysis. Use when measuring portfolio risk, impleme... |
| 2389 | `robius-app-architecture` | \| CRITICAL: Use for Robius app architecture patterns. Triggers on: Tokio, async, submit_async_request, 异步, 架构, SignalToUI, Cx::post_actio... |
| 2390 | `robius-event-action` | \| CRITICAL: Use for Robius event and action patterns. Triggers on: custom action, MatchEvent, post_action, cx.widget_action, handle_actio... |
| 2391 | `robius-matrix-integration` | \| CRITICAL: Use for Matrix SDK integration with Makepad. Triggers on: Matrix SDK, sliding sync, MatrixRequest, timeline, matrix-sdk, matr... |
| 2392 | `robius-state-management` | \| CRITICAL: Use for Robius state management patterns. Triggers on: AppState, persistence, theme switch, 状态管理, Scope::with_data, save stat... |
| 2393 | `robius-widget-patterns` | \| CRITICAL: Use for Robius widget patterns. Triggers on: apply_over, TextOrImage, modal, 可复用, 模态, collapsible, drag drop, reusable widget... |
| 2394 | `robot-framework-skill` | "Generates Robot Framework tests in keyword-driven syntax with Python. Supports SeleniumLibrary, RequestsLibrary, and custom keywords. Us... |
| 2395 | `robots-txt-creator` | "Robots.txt Creator. Use when working with site origin and desired crawl rules." |
| 2396 | `robots-txt-validator` | "Robots.txt Validator. Use when working with robots.txt text, crawler and URLs to test." |
| 2397 | `routerbase-model-gateway` | "Integrate RouterBase as an OpenAI-compatible model gateway for routing GPT, Claude, Gemini, media, audio, and embedding requests." |
| 2398 | `ruby-pro` | Write idiomatic Ruby code with metaprogramming, Rails patterns, and performance optimization. Specializes in Ruby on Rails, gem developme... |
| 2399 | `run-deep-swe` | "Run reproducible DeepSWE coding-agent benchmark evaluations through OpenRouter and mini-swe-agent." |
| 2400 | `runapi-cli` | Generate AI images, videos, and music/audio from agents using the RunAPI CLI. |
| 2401 | `runaway-guard` | "Cost-safety discipline for paid AI / inference APIs: treat $-cost as a third complexity dimension alongside time and space. Forces a wri... |
| 2402 | `runbook-creation` | Create operational runbooks and standard operating procedures. Document troubleshooting guides and recovery procedures. Use when document... |
| 2403 | `rust-async-patterns` | "Master Rust async programming with Tokio, async traits, error handling, and concurrent patterns. Use when building async Rust applicatio... |
| 2404 | `rust-pro` | Master Rust 1.75+ with modern async patterns, advanced type system features, and production-ready systems programming. |
| 2405 | `saas-authorization` | 'Adding sign-in, a role, a route that touches data, API tokens, a webhook or job, or ''is this secure'': who may do what in a multi-tenan... |
| 2406 | `saas-multi-tenant` | "Design and implement multi-tenant SaaS architectures with row-level security, tenant-scoped queries, shared-schema isolation, and safe c... |
| 2407 | `saas-mvp-launcher` | "Use when planning or building a SaaS MVP from scratch. Provides a structured roadmap covering tech stack, architecture, auth, payments, ... |
| 2408 | `saas-pricing-strategist` | Design, optimize, and test pricing strategies for SaaS products using data-driven frameworks, competitive analysis, and psychological pri... |
| 2409 | `saas-security-posture` | Audit and harden your SaaS tool stack |
| 2410 | `saga-orchestration` | "Patterns for managing distributed transactions and long-running business processes." |
| 2411 | `salary-benchmarking` | 'Salary benchmark register: role, department and grade against market and internal minimum, median and maximum. Use for compensation revi... |
| 2412 | `salary-wage-accounting` | 'Payroll register: gross, allowances, TDS and provident fund deductions, net pay, payment date and statutory reconciliation. Use for sala... |
| 2413 | `sales-accounting` | 'Sales register: customer, invoice, gross amount, discount, VAT and TDS, net receivable, credit terms and balance. Use for sales accounti... |
| 2414 | `sales-automator` | 'Draft cold emails, follow-ups, and proposal templates. Creates pricing pages, case studies, and sales scripts. Use PROACTIVELY for sales... |
| 2415 | `sales-enablement` | "Create sales collateral such as decks, one-pagers, objection docs, demo scripts, playbooks, and proposal templates. Use when a sales tea... |
| 2416 | `salesforce-automation` | "Automate Salesforce tasks via Rube MCP (Composio): leads, contacts, accounts, opportunities, SOQL queries. Always search tools first for... |
| 2417 | `salesforce-development` | Expert patterns for Salesforce platform development including Lightning Web Components (LWC), Apex triggers and classes, REST/Bulk APIs, ... |
| 2418 | `sam-altman` | "Persona fictícia inspirada em temas públicos associados a Sam Altman; sem representação, citações verificadas ou acesso interno." |
| 2419 | `same-idea-both-platforms` | "Write one idea as a Twitter post and a LinkedIn post that read as written separately, not pasted twice. Use when someone wants to cross-... |
| 2420 | `sandbase-mcp` | "Discover, inspect, and invoke 2,000+ AI models and APIs through SandBase's local MCP bridge with explicit schema and cost checks." |
| 2421 | `sankhya-dashboard-html-jsp-custom-best-pratices` | "This skill should be used when the user asks for patterns, best practices, creation, or fixing of Sankhya dashboards using HTML, JSP, Ja... |
| 2422 | `sast-configuration` | "Static Application Security Testing (SAST) tool setup, configuration, and custom rule creation for comprehensive security scanning acros... |
| 2423 | `sast-scanning` | Perform static application security testing with tools like Semgrep, CodeQL, and SonarQube. |
| 2424 | `satori` | "Use supportive, non-diagnostic reflection informed by Satori's philosophical and psychological lenses." |
| 2425 | `sbom-supply-chain` | Generate, sign, and verify SBOMs and provenance attestations to secure the software supply chain. Use when implementing SLSA controls, ar... |
| 2426 | `scala-pro` | Master enterprise-grade Scala development with functional programming, distributed systems, and big data processing. Expert in Apache Pek... |
| 2427 | `scanning-tools` | "Master essential security scanning tools for network discovery, vulnerability assessment, web application testing, wireless security, an... |
| 2428 | `scanpy` | "Scanpy is a scalable Python toolkit for analyzing single-cell RNA-seq data, built on AnnData. Apply this skill for complete single-cell ... |
| 2429 | `scarcity-urgency-psychologist` | "Design honest scarcity and urgency messaging when verified inventory, capacity, or deadlines justify a timely decision." |
| 2430 | `scarf-single-cell` | "Analyze single-cell RNA-seq at million-cell scale with Scarf: out-of-core Zarr stores on disk or object storage, provenance-tracked arti... |
| 2431 | `schema-markup` | Design, validate, and optimize schema.org structured data for eligibility, correctness, and measurable SEO impact. |
| 2432 | `schema-markup-generator` | "Generate and implement JSON-LD structured data for web apps, blogs, FAQs, and SaaS sites. Supports WebSite, SoftwareApplication, BlogPos... |
| 2433 | `scientific-writing` | "Draft and revise scientific manuscripts with evidence-based structure, citation verification, reporting guidelines and venue-specific fo... |
| 2434 | `scikit-learn` | Machine learning in Python with scikit-learn. Use for classification, regression, clustering, model evaluation, and ML pipelines. |
| 2435 | `score-eval` | "Use when scoring an evaluation diff against a supplied rubric and baseline fixture: retain evidence for detected/fixed findings and repo... |
| 2436 | `scrapely-scrape` | "Collect web data with ready-made Scrape.ly scrapers: Google Maps places, Amazon products, LinkedIn jobs, reviews, social posts. Use when... |
| 2437 | `scrapingbee-cli` | "Fetch web pages, crawl sites and get Google, Amazon, Walmart and YouTube data as JSON with the ScrapingBee CLI. Use when a task needs co... |
| 2438 | `screen-adverse-media` | Screen a person or organisation for adverse media coverage, PEP status, and sanctions exposure — corroboration-gated, returns "review" ne... |
| 2439 | `screen-reader-testing` | "Practical guide to testing web applications with screen readers for comprehensive accessibility validation." |
| 2440 | `screenshots` | "Generate marketing screenshots of your app using Playwright. Use when the user wants to create screenshots for Product Hunt, social medi... |
| 2441 | `screenstudio-alt` | "Open-source headless Screen Studio alternative: auto speed-up of idle, auto-zoom on click clusters, keystroke overlay chips, smoothed sy... |
| 2442 | `scribiz` | Summarize authorized video or audio with Scribiz transcripts, timestamps, chapters and on-screen text, or turn existing captions into dra... |
| 2443 | `scroll-3d-world` | "Build a scroll-scrubbed Three.js fly-through landing page: one continuous camera path through diorama scenes, with no AI video, no seams... |
| 2444 | `scroll-experience` | Expert in building immersive scroll-driven experiences - parallax storytelling, scroll animations, interactive narratives, and cinematic ... |
| 2445 | `sdk-dx` | "Design SDKs that developers love to use—APIs that feel native, error messages that guide, and experiences that reduce friction. This ski... |
| 2446 | `seaborn` | "Seaborn is a Python visualization library for creating publication-quality statistical graphics. Use this skill for dataset-oriented plo... |
| 2447 | `search-preview-simulator` | "Search Preview Simulator. Use when working with title, description and page URL." |
| 2448 | `search-specialist` | "Research questions with focused web searches, primary-source verification, and explicit evidence gaps." |
| 2449 | `second-deposit-igaming` | "Explore local casino deposit exports with heuristic signals and descriptive comparisons. Sensitive player data; contact lists and countr... |
| 2450 | `secrets-management` | "Secure secrets management practices for CI/CD pipelines using Vault, AWS Secrets Manager, and other tools." |
| 2451 | `security-and-hardening` | Hardens code against vulnerabilities. Use when handling user input, authentication, data storage, or external integrations. Use when buil... |
| 2452 | `security-arsenal` | Security payloads, bypass tables, wordlists, gf pattern names, always-rejected bug list, and conditionally-valid-with-chain table. |
| 2453 | `security-audit` | "Comprehensive security auditing workflow covering web application testing, API security, penetration testing, vulnerability scanning, an... |
| 2454 | `security-audit-static` | 'Only when a security audit is asked for (ship-check asks by name; a release proposes one, never runs it): a static audit of AI-built cod... |
| 2455 | `security-auditor` | Expert security auditor specializing in DevSecOps, comprehensive cybersecurity, and compliance frameworks. |
| 2456 | `security-automation` | Automate security workflows and remediation. Build security pipelines, automate compliance checks, and implement SOAR capabilities. Use w... |
| 2457 | `security-bluebook-builder` | "Build a minimal but real security policy for sensitive apps. The output is a single, coherent Blue Book document using MUST/SHOULD/CAN l... |
| 2458 | `security-compliance-compliance-check` | "You are a compliance expert specializing in regulatory requirements for software systems including GDPR, HIPAA, SOC2, PCI-DSS, and other... |
| 2459 | `security-requirement-extraction` | "Derive security requirements from threat models and business context. Use when translating threats into actionable requirements, creatin... |
| 2460 | `security-scanning-security-dependencies` | "You are a security expert specializing in dependency vulnerability analysis, SBOM generation, and supply chain security. Scan project de... |
| 2461 | `security-scanning-security-hardening` | "Coordinate multi-layer security scanning and hardening across application, infrastructure, and compliance controls." |
| 2462 | `security-scanning-security-sast` | 'Static Application Security Testing (SAST) for code vulnerability analysis across multiple languages and frameworks ' |
| 2463 | `seek-and-analyze-video` | "Seek and analyze video content using Memories.ai Large Visual Memory Model for persistent video intelligence" |
| 2464 | `segment-automation` | "Automate Segment tasks via Rube MCP (Composio): track events, identify users, manage groups, page views, aliases, batch operations. Alwa... |
| 2465 | `segment-cdp` | Expert patterns for Segment Customer Data Platform including Analytics.js, server-side tracking, tracking plans with Protocols, identity ... |
| 2466 | `selector` | "Select a specialized 100seotools skill from a plain-language SEO or project-documentation request. Use when the user needs help choosing... |
| 2467 | `selenium-skill` | "Generates production-grade Selenium WebDriver automation scripts and tests in Java, Python, JavaScript, C#, Ruby, or PHP. Supports local... |
| 2468 | `semantic-versioning` | Automate versioning and changelog generation using semantic versioning principles. |
| 2469 | `semgrep-rule-creator` | Creates custom Semgrep rules for detecting security vulnerabilities, bug patterns, and code patterns. Use when writing Semgrep rules or b... |
| 2470 | `semgrep-rule-variant-creator` | Creates language variants of existing Semgrep rules. Use when porting a Semgrep rule to specified target languages. Takes an existing rul... |
| 2471 | `sendblue-api` | "Send and receive iMessage, SMS, and RCS from application code via the Sendblue HTTP API — text, media, group messages, send styles, reac... |
| 2472 | `sendblue-cli` | "Send iMessage and SMS from the shell via the @sendblue/cli npm package — outbound sends, contact management, and account setup with no A... |
| 2473 | `sendblue-notify` | "Text the user's phone when a long-running task, agent turn, or scheduled job finishes — via @sendblue/cli for outbound, optionally wired... |
| 2474 | `sendgrid-automation` | "Automate SendGrid email delivery workflows including marketing campaigns (Single Sends), contact and list management, sender identity se... |
| 2475 | `senior-architect` | "Plan and review system architecture using explicit requirements, tradeoffs and evidence; bundled scripts are incomplete stubs." |
| 2476 | `senior-frontend` | Frontend development skill for React, Next.js, TypeScript, and Tailwind CSS applications. Use when building React components, optimizing ... |
| 2477 | `senior-fullstack` | "Coordinate full-stack implementation across interface, service, database and delivery boundaries using the existing project stack and ve... |
| 2478 | `sentry-automation` | "Automate Sentry tasks via Rube MCP (Composio): manage issues/events, configure alerts, track releases, monitor projects and teams. Alway... |
| 2479 | `seo` | "Run a broad SEO audit across technical SEO, on-page SEO, schema, sitemaps, content quality, AI search readiness, and GEO. Use as the umb... |
| 2480 | `seo-aeo-blog-writer` | "Writes search-intent-led long-form articles with answer-first structure, FAQ coverage, internal links, and conversion paths for SEO and ... |
| 2481 | `seo-aeo-content-cluster` | "Builds a topical authority map from business goals, search intent, existing content, and gaps, then prioritises foundational and support... |
| 2482 | `seo-aeo-content-quality-auditor` | "Audits a website, codebase, page, or content set for technical SEO, search intent, AEO, conversion paths, and publishing readiness, then... |
| 2483 | `seo-aeo-internal-linking` | "Maps internal link opportunities between pages with relevant anchor text, placement instructions, orphan-page detection, and cannibalisa... |
| 2484 | `seo-aeo-keyword-research` | "Researches and prioritises keywords from the site context and live search intent, including problem queries, question queries, difficult... |
| 2485 | `seo-aeo-landing-page-writer` | "Writes or improves conversion-focused landing pages for products, services, and offers with practical SEO and AEO structure." |
| 2486 | `seo-aeo-meta-description-generator` | "Writes title tags, meta descriptions, Open Graph tags, and Twitter Card tags aligned to page intent and conversion goals." |
| 2487 | `seo-aeo-orchestrator` | "Runs an audit-first SEO/AEO growth workflow from project discovery through implementation, foundational content, measurement setup, depl... |
| 2488 | `seo-aeo-schema-generator` | "Generates and validates implementation-ready JSON-LD structured data for relevant page types and rich-result eligibility." |
| 2489 | `seo-audit` | Diagnose and audit SEO issues affecting crawlability, indexation, rankings, and organic performance. |
| 2490 | `seo-authority-builder` | 'Analyzes content for E-E-A-T signals and suggests improvements to build authority and trust. Identifies missing credibility elements. Us... |
| 2491 | `seo-autopilot` | Run a user-invoked SEO maintenance pass with repository change checks, ranking history, competitor sitemap diffs and a reviewable backlog. |
| 2492 | `seo-blog-images` | Plan and verify blog covers, social previews and inline proof visuals with accurate alt text, responsive dimensions and optimized file si... |
| 2493 | `seo-cannibalization-detector` | Analyzes multiple provided pages to identify keyword overlap and potential cannibalization issues. Suggests differentiation strategies. U... |
| 2494 | `seo-checklist-generator` | "SEO Checklist Generator. Use when working with site type and current goal." |
| 2495 | `seo-competitor-pages` | Generate SEO-optimized competitor comparison and alternatives pages. Covers "X vs Y" layouts, "alternatives to X" pages, feature matrices... |
| 2496 | `seo-content` | Content quality and E-E-A-T analysis with AI citation readiness assessment. Use when user says "content quality", "E-E-A-T", "content ana... |
| 2497 | `seo-content-auditor` | Analyzes provided content for quality, E-E-A-T signals, and SEO best practices. Scores content and provides improvement recommendations b... |
| 2498 | `seo-content-checker` | "SEO Content Checker. Use when working with content and target query or reader task." |
| 2499 | `seo-content-planner` | 'Creates comprehensive content outlines and topic clusters for SEO. Plans content calendars and identifies topic gaps. Use PROACTIVELY fo... |
| 2500 | `seo-content-refresher` | Identifies outdated elements in provided content and suggests updates to maintain freshness. Finds statistics, dates, and examples that n... |
| 2501 | `seo-content-writer` | Writes SEO-optimized content based on provided keywords and topic briefs. Creates engaging, comprehensive content following best practice... |
| 2502 | `seo-dataforseo` | "Use DataForSEO for live SERPs, keyword metrics, backlinks, competitor analysis, on-page checks, and AI visibility data. Trigger when the... |
| 2503 | `seo-directory-backlinks` | 'Directory and backlink register: platform, domain, target URL, follow attribute, authority and spam scores, approval and NAP-match statu... |
| 2504 | `seo-drift` | "Snapshot a site's SEO state and detect ranking, indexation, metadata, canonical, robots, schema, and on-page regressions over time." |
| 2505 | `seo-forensic-incident-response` | "Investigate sudden drops in organic traffic or rankings and run a structured forensic SEO incident response with triage, root-cause anal... |
| 2506 | `seo-fundamentals` | Core principles of SEO including E-E-A-T, Core Web Vitals, technical foundations, content quality, and how modern search engines evaluate... |
| 2507 | `seo-geo` | "Optimize content for AI Overviews, ChatGPT, Perplexity, and other AI search systems. Use when improving GEO, AI citations, llms.txt read... |
| 2508 | `seo-health-score-calculator` | "SEO Health Score Calculator. Use when working with audit findings and a disclosed scoring rubric." |
| 2509 | `seo-hreflang` | Hreflang and international SEO audit, validation, and generation. Detects common mistakes, validates language/region codes, and generates... |
| 2510 | `seo-image-gen` | "Generate SEO-focused images such as OG cards, hero images, schema assets, product visuals, and infographics. Use when image generation i... |
| 2511 | `seo-images` | Image optimization analysis for SEO and performance. Checks alt text, file sizes, formats, responsive images, lazy loading, and CLS preve... |
| 2512 | `seo-keyword-strategist` | Analyzes keyword usage in provided content, calculates density, suggests semantic variations and related terms based on the topic. Preven... |
| 2513 | `seo-meta-optimizer` | Creates optimized meta titles, descriptions, and URL suggestions based on character limits and best practices. Generates compelling, keyw... |
| 2514 | `seo-page` | Deep single-page SEO analysis covering on-page elements, content quality, technical meta tags, schema, images, and performance. Use when ... |
| 2515 | `seo-plan` | Strategic SEO planning for new or existing websites. Industry-specific templates, competitive analysis, content strategy, and implementat... |
| 2516 | `seo-programmatic` | "Plan and audit programmatic SEO pages generated at scale from structured data. Use when designing templates, URL systems, internal linki... |
| 2517 | `seo-roast` | Review owned-site crawlability, page structure, authority and AI-search visibility, then prepare a prioritized revenue-oriented fix roadmap. |
| 2518 | `seo-schema` | Detect, validate, and generate Schema.org structured data. JSON-LD format preferred. Use when user says "schema", "structured data", "ric... |
| 2519 | `seo-sitemap` | Analyze existing XML sitemaps or generate new ones with industry templates. Validates format, URLs, and structure. Use when user says "si... |
| 2520 | `seo-snippet-hunter` | Formats content to be eligible for featured snippets and SERP features. Creates snippet-optimized content blocks based on best practices.... |
| 2521 | `seo-structure-architect` | Analyzes and optimizes content structure including header hierarchy, suggests schema markup, and internal linking opportunities. Creates ... |
| 2522 | `seo-technical` | "Audit technical SEO across crawlability, indexability, security, URLs, mobile, Core Web Vitals, structured data, JavaScript rendering, a... |
| 2523 | `seo-title-optimization` | Rewrite and audit SEO page titles, title tags, MDX frontmatter titles, H1 alignment, and bulk title improvements. Use when the user menti... |
| 2524 | `sequence-psychologist` | "Plan email nurture and multi-touch communication sequences when each message should build trust and prepare the next decision." |
| 2525 | `sequenzy-email-marketing` | "Operate Sequenzy email campaigns through an authorized CLI or MCP connection: inspect audiences, prepare drafts, schedule approved sends... |
| 2526 | `serply-search-mcp` | "Search Google, Bing, Google News and Google Scholar, and read public pages, with the Serply MCP server. Use when the user chooses Serply... |
| 2527 | `server-management` | "Server management principles and decision-making. Process management, monitoring strategy, and scaling decisions. Teaches thinking, not ... |
| 2528 | `service-mesh` | Implement Istio and Linkerd service meshes. Configure mTLS, traffic management, and observability. Use when managing microservices commun... |
| 2529 | `service-mesh-expert` | "Review Istio or Linkerd topology, traffic policies, mTLS, observability and multi-cluster operations within an authorized environment." |
| 2530 | `service-mesh-observability` | "Complete guide to observability patterns for Istio, Linkerd, and service mesh deployments." |
| 2531 | `session-handoff` | "Use when context approaches capacity, before /clear or /compact, when switching tasks, or when ending a coding session: produces a struc... |
| 2532 | `setup-help` | "Walk a user through setup or installation one step at a time with the remaining steps visible." |
| 2533 | `setup-matt-pocock-skills` | Configure this repo for the engineering skills — set up its issue tracker, triage label vocabulary, and domain doc layout. Run once befor... |
| 2534 | `sexual-health-analyzer` | Sexual Health Analyzer |
| 2535 | `sfxmint` | "Find and add free CC0 sound effects to an app, game or video by event, set or description over a keyless API or MCP; generate a missing ... |
| 2536 | `shadcn` | Manages shadcn/ui components and projects, providing context, documentation, and usage patterns for building modern design systems. |
| 2537 | `shader-programming-glsl` | "Expert guide for writing efficient GLSL shaders (Vertex/Fragment) for web and game engines, covering syntax, uniforms, and common effects." |
| 2538 | `shark` | "Pitch a business idea to a Shark Tank-style panel of Claude sub-agent investors who grill it, hear a founder agent answer, and each go I... |
| 2539 | `sharp-coder` | Two-layer performance skill combining disciplined THINK layer (surgical edits, simplicity) and terse SPEAK layer (caveman compression). T... |
| 2540 | `sharp-edges` | "Review misuse-prone security APIs, configuration defaults, cryptographic interfaces and authentication ergonomics; verify concrete failu... |
| 2541 | `shellcheck-configuration` | "Master ShellCheck static analysis configuration and usage for shell script quality. Use when setting up linting infrastructure, fixing c... |
| 2542 | `ship-check` | Assemble a ship-readiness review from existing evidence, with bounded static findings, test gaps, sign-off decisions and release artifacts. |
| 2543 | `shipping-and-launch` | Prepares production launches. Use when preparing to deploy to production. Use when you need a pre-launch checklist, when setting up monit... |
| 2544 | `shipping-artifacts` | 'Documenting an AI-built app for handoff, review or audit: the docs that make it reviewable (architecture, flows, permissions, variables,... |
| 2545 | `shipvela-publish` | "Publish an explicitly selected website through the user's connected Shipvela MCP account, track the exact deployment, and return its liv... |
| 2546 | `shodan-reconnaissance` | "Provide systematic methodologies for leveraging Shodan as a reconnaissance tool during penetration testing engagements." |
| 2547 | `shopify-apps` | Expert patterns for Shopify app development including Remix/React Router apps, embedded apps with App Bridge, webhook handling, GraphQL A... |
| 2548 | `shopify-automation` | "Automate Shopify tasks via Rube MCP (Composio): products, orders, customers, inventory, collections. Always search tools first for curre... |
| 2549 | `shopify-development` | Build Shopify apps, extensions, themes using GraphQL Admin API, Shopify CLI, Polaris UI, and Liquid. |
| 2550 | `shopify-firebase-app` | "Scaffold, extend and deploy Shopify embedded apps on Firebase with Nitrogen. Use for a Shopify app on Cloud Functions, Firestore and Hos... |
| 2551 | `shopify-review-triage` | "Turn public 1-3-star Shopify App Store review rows into a P0-P3 triage brief: incident risk, repeated friction, pricing confusion, featu... |
| 2552 | `short` | "Rewrite the previous response more briefly while preserving the substance." |
| 2553 | `show-the-change` | "Explain a specific project change to non-programmers, with evidence and practical checks." |
| 2554 | `signup-flow-cro` | "You are an expert in optimizing signup and registration flows. Your goal is to reduce friction, increase completion rates, and set users... |
| 2555 | `similarity-search-patterns` | "Implement efficient similarity search with vector databases. Use when building semantic search, implementing nearest neighbor queries, o... |
| 2556 | `simplify-code` | "Review a diff for clarity and safe simplifications, then optionally apply low-risk fixes." |
| 2557 | `since-cutoff` | "Find which APIs of a project's pinned Python dependencies changed after the model's training cutoff, where the code uses them, and write... |
| 2558 | `site-architecture` | "Plan or restructure website hierarchy, navigation, URL patterns, breadcrumbs, and internal linking. Use when mapping pages, sections, an... |
| 2559 | `site-comparison-report-generator` | "Site Comparison Report Generator. Use when working with two or more sites and the user's comparison goal." |
| 2560 | `sitemap-generator` | "XML Sitemap Generator. Use when working with canonical public page URLs and optional real modification dates." |
| 2561 | `skeleton-first` | "Prove a data/AI/agent workflow end to end on a tiny sample, find cheap wins, then scale in cost-gated steps within budget." |
| 2562 | `skill-agent-topology` | "Audit whether a multi-agent setup earns its coordination cost — use before adding an agent, or when a workflow feels slow or agents agre... |
| 2563 | `skill-audit` | "Audit codebases for quality, consistency, and broken patterns — use for pre-release or tech debt review" |
| 2564 | `skill-authoring` | "Principles for writing skills that behave the same way every run — use when adding, editing, or reviewing a skill in this plugin" |
| 2565 | `skill-check` | "Validate Claude Code skills against the agentskills specification. Catches structural, semantic, and naming issues before users do." |
| 2566 | `skill-code-review` | Expert multi-AI code review with inline PR comments — use for thorough quality and security analysis |
| 2567 | `skill-content-pipeline` | "Extract patterns and anatomy from URLs — use to reverse-engineer content strategies from live pages" |
| 2568 | `skill-context-detection` | "Auto-detect work context (Dev vs Knowledge) — use to tailor workflows based on current task type" |
| 2569 | `skill-copilot-provider` | GitHub Copilot CLI as optional zero-cost provider via copilot -p programmatic mode |
| 2570 | `skill-cost-projections` | "Project remaining workflow cost from per-phase averages — warns on budget ceiling overruns" |
| 2571 | `skill-council` | "Run a configurable multi-LLM council with personas, budget caps, synthesis, veto gates, and optional implementation handoff." |
| 2572 | `skill-coverage-audit` | "Trace codepaths in diffs, map against tests, auto-generate missing coverage — use before shipping PRs" |
| 2573 | `skill-creator` | "Create and review reusable skill drafts with bundled Python scaffolding, basic frontmatter validation and ZIP packaging helpers. Use for... |
| 2574 | `skill-creator-ms` | "Guide for creating effective skills for AI coding agents working with Azure SDKs and Microsoft Foundry services. Use when creating new s... |
| 2575 | `skill-debate` | Structured multi-provider AI debates between Claude and available advisors — use for critical decisions |
| 2576 | `skill-debug` | "Debug a reproducible symptom with a bounded feedback loop and original-scenario verification" |
| 2577 | `skill-decision-support` | Present options with trade-offs for informed decision-making — use when choosing between approaches |
| 2578 | `skill-deck` | Generate slide deck presentations from briefs — use when you need slides, pitch decks, or visual summaries |
| 2579 | `skill-design-lineage` | "Persist design documents with branch tracking, revision chains, and cross-session discovery" |
| 2580 | `skill-developer` | "Comprehensive guide for creating and managing skills in Claude Code with auto-activation system, using an illustrative custom hook archi... |
| 2581 | `skill-doc-delivery` | Convert markdown to DOCX, PPTX, XLSX, PDF office documents — use when you need exportable deliverables |
| 2582 | `skill-doc-sync` | "Post-ship doc sync across project markdown. Use when: sync docs, update docs, document changes, release notes." |
| 2583 | `skill-doctor` | "Environment diagnostics — check providers, auth, config, hooks, scheduler, and more" |
| 2584 | `skill-extract` | "Reverse-engineer design systems, tokens, and components from live products or screenshots" |
| 2585 | `skill-factory` | "Run a full build-and-ship pipeline from a spec — use for hands-off project generation" |
| 2586 | `skill-finish-branch` | "Wrap up a branch — run tests, create PR, merge or discard — use when implementation is done" |
| 2587 | `skill-gap-analysis` | 'Skill gap register: employee, skill area, current against required level, gap severity and recommended training. Use for capability plan... |
| 2588 | `skill-improver` | "Iteratively improve a Claude Code skill using the skill-reviewer agent until it meets quality standards. Use when improving a skill with... |
| 2589 | `skill-installer` | Validate and install explicitly selected local skill trees into a workspace, with full-tree Claude registration, backups and ZIP packaging. |
| 2590 | `skill-intake` | "Move incoming issues and pull requests through triage states until each is actionable or closed — use when the queue has piled up or a r... |
| 2591 | `skill-intent-contract` | "Use when starting a complex or ambiguous task that risks scope drift" |
| 2592 | `skill-issue` | "Find out why a coding-agent skill won't fire — grade each SKILL.md A–F on activation, simulate which skill a prompt triggers, and flag c... |
| 2593 | `skill-issues` | "Track project blockers, bugs, and gaps across sessions — use when issues pile up or need triage" |
| 2594 | `skill-iterative-loop` | "Run tasks in a loop until goals are met — use for iterative refinement, polling, or convergence" |
| 2595 | `skill-knowledge-work` | "Switch to Knowledge Work mode for research and writing — use when task is non-code focused" |
| 2596 | `skill-meta-prompt` | "Craft better prompts using proven optimization techniques — use when your prompt needs refinement" |
| 2597 | `skill-native-escalation-routing` | "Use when choosing native or multi-LLM handling for init, review, or security requests" |
| 2598 | `skill-optimizer` | "Diagnose and optimize Agent Skills (SKILL.md) with real session data and research-backed static analysis. Works with Claude Code, Codex,... |
| 2599 | `skill-parallel-agents` | Decompose large tasks across parallel agents — use for migrations, multi-file refactors, or batch work |
| 2600 | `skill-porter` | "Preview conservative tool-name translations and copy complete local skill bundles for manual adaptation to Google Antigravity." |
| 2601 | `skill-prd` | Write an AI-optimized PRD using multi-AI orchestration — use when scoping a new feature or product |
| 2602 | `skill-pressure-test` | "Interrogate a plan, decision, or design one question at a time until it holds — use to stress-test your own thinking before committing t... |
| 2603 | `skill-prototype` | "Prototype one risky assumption within a fixed budget, then keep or discard the result" |
| 2604 | `skill-rails-upgrade` | "Analyze Rails apps and provide upgrade assessments" |
| 2605 | `skill-refine` | "Score and improve an artifact with a frozen rubric, independent models, implemented edits, and bounded rescoring" |
| 2606 | `skill-resume` | "Pick up where you left off from a previous session — use after context resets, compaction, or new conversations" |
| 2607 | `skill-review-response` | "Use when a reviewer, CI bot, or another AI leaves feedback to address" |
| 2608 | `skill-rollback` | "Roll back to a previous checkpoint via git — use when a change went wrong and you need to revert" |
| 2609 | `skill-router` | "Use when the user is unsure which skill to use or where to start. Interviews the user with targeted questions and recommends the best sk... |
| 2610 | `skill-scanner` | "Scan agent skills for security issues before adoption. Detects prompt injection, malicious code, excessive permissions, secret exposure,... |
| 2611 | `skill-security-audit` | "Audit an Agent Skill, MCP server, connector, or desktop extension before installation by tracing code, dependencies, permissions, creden... |
| 2612 | `skill-security-framing` | URL validation and content sanitization for untrusted sources — use when handling external input safely |
| 2613 | `skill-seekers` | "Convert approved documentation, repositories, or PDFs into an agent skill using the Skill Seekers workflow, then review the generated co... |
| 2614 | `skill-sentinel` | Auditoria e evolucao do ecossistema de skills. Qualidade de codigo, seguranca, custos, gaps, duplicacoes, dependencias e relatorios de sa... |
| 2615 | `skill-ship` | "Package and finalize completed work for delivery — use when a feature is done and ready to ship" |
| 2616 | `skill-skill` | "Write, upgrade or audit a Claude skill so it changes what gets generated: forcing functions, triggerable descriptions, and a static audi... |
| 2617 | `skill-staged-review` | "Use when a PR or feature needs both specification and code-quality review" |
| 2618 | `skill-status` | "Show where you are in the workflow and what to do next — use for progress checks and orientation" |
| 2619 | `skill-suggester` | "Scan prompt history for recurring patterns and unmet needs, then propose new skills or command templates" |
| 2620 | `skill-task-management` | "Manage tasks with Claude Code native tools — use to track TODOs, delegate work, and monitor progress" |
| 2621 | `skill-tdd` | "Build a behavior change with observed red, minimal green, and measured test consolidation" |
| 2622 | `skill-thought-partner` | "Brainstorm creatively with pattern spotting and paradox hunting — use for ideation and exploration" |
| 2623 | `skill-verification-gate` | "Use when about to declare work complete, fixed, passing, or done" |
| 2624 | `skill-verify` | "Use when about to declare work complete, fixed, passing, or done" |
| 2625 | `skill-visual-feedback` | Process screenshot-based UI/UX feedback to fix visual issues — use when users share screenshots of bugs |
| 2626 | `skill-work-slicing` | "Break a plan or spec into vertical slices that each declare what blocks them — use when work is agreed but not yet cut into fileable pie... |
| 2627 | `skill-writer` | Create and improve agent skills following the Agent Skills specification. Use when asked to create, write, or update skills. |
| 2628 | `skill-writing-plans` | Create zero-context implementation plans with bite-sized tasks — use for multi-step feature planning |
| 2629 | `skin-health-analyzer` | Analyze skin health data, identify skin problem patterns, assess skin health status. Supports correlation analysis with nutrition, chroni... |
| 2630 | `skyvern-browser-automation` | "AI-powered browser automation — navigate sites, fill forms, extract structured data, log in with stored credentials, and build reusable ... |
| 2631 | `slack-automation` | "Automate Slack workspace operations including messaging, search, channel management, and reaction workflows through Composio's Slack too... |
| 2632 | `slack-bot-builder` | Build Slack apps using the Bolt framework across Python, JavaScript, and Java. Covers Block Kit for rich UIs, interactive components, sla... |
| 2633 | `slack-gif-creator` | "A toolkit providing utilities and knowledge for creating animated GIFs optimized for Slack." |
| 2634 | `sleep-analyzer` | 分析睡眠数据、识别睡眠模式、评估睡眠质量，并提供个性化睡眠改善建议。支持与其他健康数据的关联分析。 |
| 2635 | `slideops` | "Turn a repository into a cited HTML slide deck and detect the day it drifts from the code. Citations record file, lines, and hash; a std... |
| 2636 | `slideshow` | "Build live HyperFrames slide decks with fragments, branching hotspots and presenter notes." |
| 2637 | `slo-implementation` | "Framework for defining and implementing Service Level Indicators (SLIs), Service Level Objectives (SLOs), and error budgets." |
| 2638 | `smart-contract-formal-verification` | 'Foundry and Soroban formal invariant verification register: state transition rules, boundary invariant properties, and symbolic executio... |
| 2639 | `smart-contract-upgrade-governance` | 'Soroban WASM upgrade governance register: executable bytecode hash, timelocked migration delays, and multi-sig authorization quorum.' |
| 2640 | `smart-git-automation` | "Smart change detection, auto branch naming, and streamlined commit/PR workflow" |
| 2641 | `smartui-skill` | "Generates SmartUI visual regression test configurations for screenshot comparison on TestMu AI cloud. Framework-agnostic — works with Pl... |
| 2642 | `smtp-penetration-testing` | "Conduct comprehensive security assessments of SMTP (Simple Mail Transfer Protocol) servers to identify vulnerabilities including open re... |
| 2643 | `snowflake-development` | "Comprehensive Snowflake development assistant covering SQL best practices, data pipeline design (Dynamic Tables, Streams, Tasks, Snowpip... |
| 2644 | `soc2-compliance` | Implement SOC 2 Trust Services Criteria. Configure security, availability, and processing integrity controls. Use when preparing for a SO... |
| 2645 | `social-content` | "Help plan and draft social content; publishing capabilities depend on the actual connected account and tool permissions. Your goal is to... |
| 2646 | `social-media-setup` | 'Social media register: platforms and handles, post captions and hashtags, publishing cadence, approval status and profile checklist. Use... |
| 2647 | `social-metadata-hardening` | "Fix social sharing previews so URLs render as rich cards on Facebook, LinkedIn, X/Twitter, WhatsApp, Telegram, and more. Covers OG tags,... |
| 2648 | `social-orchestrator` | "Orquestrador unificado de canais sociais — coordena Instagram, Telegram e WhatsApp em um unico fluxo de trabalho. Publicacao cross-chann... |
| 2649 | `social-post-writer-seo` | "Social Media Strategist and Content Writer. Creates clear, engaging social media posts for Instagram, LinkedIn, and Facebook." |
| 2650 | `social-proof-architect` | "Select and place genuine testimonials, case studies, and other proof when an audience needs evidence at specific trust barriers." |
| 2651 | `socialclaw` | "Agent-first social media publishing skill — schedule and publish posts across the listed platforms (X, LinkedIn, Instagram, Facebook Pag... |
| 2652 | `software-architecture` | "Guide for quality focused software architecture. This skill should be used when users want to write code, design architecture, analyze c... |
| 2653 | `solidity-security` | "Master smart contract security best practices, vulnerability prevention, and secure Solidity development patterns." |
| 2654 | `solidping` | "Run SolidPing uptime monitoring through its hosted MCP server: list and diagnose checks, read results and incidents, create checks acros... |
| 2655 | `sop-company-wiki` | 'SOP and company wiki register: title, category, department, owner, version, priority and review dates. Use for process documentation.' |
| 2656 | `sops-encryption` | Encrypt files and configs with Mozilla SOPS. |
| 2657 | `soroban-contract-audit` | 'Soroban smart contract security audit register: authorization checks, panic pathways, integer overflows, and storage footprint verificat... |
| 2658 | `soroban-liquidity-pool` | 'Automated market maker liquidity pool register: constant-product invariant curves, swap fee tiers, and LP token shares for Soroban DeFi.' |
| 2659 | `soroban-oracle-data-feed-audit` | 'DeFi price oracle integration and safety audit register: heartbeat bounds, stale price threshold reversion, and TWAP medianizer validati... |
| 2660 | `soroban-storage-ttl-lifecycle` | 'Soroban ledger state rent and TTL extension register: live state tracking, bump thresholds, rent fee reserves, and archive boundaries.' |
| 2661 | `soroban-token-minter` | 'Soroban SEP-41 token contract architecture register: admin control, supply caps, metadata standard, and transfer event emissions on Stel... |
| 2662 | `soundza` | "Find, audition and add free sound effects, ambience or music to a game, video or app with Soundza, or generate a new sound effect from a... |
| 2663 | `source-document-filing` | 'Source document register: document type and number, party, amount, index key, storage location, retention period and verification. Use f... |
| 2664 | `source-driven-development` | Grounds every implementation decision in official documentation. Use when you want authoritative, source-cited code free from outdated pa... |
| 2665 | `spark-optimization` | "Optimize Apache Spark jobs with partitioning, caching, shuffle optimization, and memory tuning. Use when improving Spark performance, de... |
| 2666 | `spec-driven-development` | Creates specs before coding. Use when starting a new project, feature, or significant change and no specification exists yet. Use when re... |
| 2667 | `spec-driven-loop` | Freeze PRD, technical design, and acceptance criteria before medium-to-large Codex work; coordinate agents with explicit ownership, then ... |
| 2668 | `spec-to-code-compliance` | Verifies code implements exactly what documentation specifies for blockchain audits. Use when comparing code against whitepapers, finding... |
| 2669 | `speckit-updater` | SpecKit Safe Update |
| 2670 | `specstream-browser-sessions` | "Open, drive and release a hosted SpecStream browser session over CDP (Playwright, Puppeteer) or one REST action at a time, with domain l... |
| 2671 | `speed` | Launch RSVP speed reader for text |
| 2672 | `spline-3d-integration` | "Use when adding interactive 3D scenes from Spline.design to web projects, including React embedding and runtime control API." |
| 2673 | `spreadsheet-manual-build` | 'Spreadsheet Manual Build: an empty Excel workbook or CSV from a confirmed field list, formatted and validated. Use for an xlsx template ... |
| 2674 | `sql-injection-testing` | "Execute comprehensive SQL injection vulnerability assessments on web applications to identify database security flaws, demonstrate explo... |
| 2675 | `sql-optimization-patterns` | "Diagnose slow SQL with query plans, preserve query results, and verify indexing or query changes against representative data." |
| 2676 | `sql-pro` | Master modern SQL with cloud-native databases, OLTP/OLAP optimization, and advanced query techniques. Expert in performance tuning, data ... |
| 2677 | `sql-sentinel` | "Audit SQL for the cost & performance anti-patterns that burn warehouse credits. Scores warehouse health 0-100 and outputs a prioritized ... |
| 2678 | `sqlmap-database-pentesting` | "Provide systematic methodologies for automated SQL injection detection and exploitation using SQLMap." |
| 2679 | `square-automation` | "Automate Square tasks via Rube MCP (Composio): payments, orders, invoices, locations. Always search tools first for current schemas." |
| 2680 | `squirrel` | "Full-cycle AI coding skill: plans, builds, tests, lints, fixes bugs, and writes production-grade docs. Auto-detects project state and ad... |
| 2681 | `sre-dashboards` | Design and operationalize SRE dashboards that surface reliability, latency, error, saturation, and capacity signals across services. |
| 2682 | `sred-project-organizer` | Take a list of projects and their related documentation, and organize them into the SRED format for submission. |
| 2683 | `sred-work-summary` | Go back through the previous year of work and create a Notion doc that groups relevant links into projects that can then be documented as... |
| 2684 | `ssh-configuration` | Configure SSH servers and clients securely. Manage keys, tunnels, and config files. Use when setting up secure remote access. |
| 2685 | `ssh-penetration-testing` | "Conduct comprehensive SSH security assessments including enumeration, credential attacks, vulnerability exploitation, tunneling techniqu... |
| 2686 | `sshepherd` | "Zero-knowledge SSH ops CLI — server health checks, docker/systemd control, log tailing, Postgres introspection, and declarative deploys,... |
| 2687 | `ssl-tls-management` | Manage SSL/TLS certificates with Let's Encrypt and internal PKI. Configure secure HTTPS, certificate renewal, and cipher suites. Use when... |
| 2688 | `stability-ai` | Geracao de imagens via Stability AI (SD3.5, Ultra, Core). Text-to-image, img2img, inpainting, upscale, remove-bg, search-replace. 15 esti... |
| 2689 | `stageshow` | "Use when a user asks for a React product illustration, animated walkthrough, product demo, or cursor-led UI animation. Build from the re... |
| 2690 | `stakeholder-investor-reports` | 'Stakeholder report register: stakeholder, period, key metrics, preparer, approver, send date and report link. Use for investor and board... |
| 2691 | `startup-analyst` | Expert startup business analyst specializing in market sizing, financial modeling, competitive analysis, and strategic planning for early... |
| 2692 | `startup-business-analyst-business-case` | 'Generate comprehensive investor-ready business case document with market, solution, financials, and strategy ' |
| 2693 | `startup-business-analyst-financial-projections` | 'Create detailed 3-5 year financial model with revenue, costs, cash flow, and scenarios ' |
| 2694 | `startup-business-analyst-market-opportunity` | 'Generate comprehensive market opportunity analysis with TAM/SAM/SOM calculations ' |
| 2695 | `startup-financial-modeling` | "Build comprehensive 3-5 year financial models with revenue projections, cost structures, cash flow analysis, and scenario planning for e... |
| 2696 | `startup-it-troubleshooting` | Practical IT troubleshooting playbooks for small teams without dedicated IT staff. |
| 2697 | `startup-metrics-framework` | "Comprehensive guide to tracking, calculating, and optimizing key performance metrics for different startup business models from seed thr... |
| 2698 | `state-machine` | Renders every state of a component you choose on a throwaway page, with mock data and a switcher, so you can work on each state. |
| 2699 | `statsmodels` | "Statsmodels is Python's premier library for statistical modeling, providing tools for estimation, inference, and diagnostics across a wi... |
| 2700 | `stellar-anchor-integration` | 'Stellar anchor protocol compliance register: SEP-10 web authentication, SEP-24 interactive deposit and withdrawal, and KYC lifecycle.' |
| 2701 | `stellar-asset-clawback-compliance` | 'Regulated Stellar asset clawback architecture register: issuer authorization flags, claimable balance revocations, and regulatory audit ... |
| 2702 | `stellar-escrow-timelock` | 'Decentralized conditional escrow and timelock contract register: multi-signature release conditions, clawback expiry, and settlement tri... |
| 2703 | `stellar-multisig-threshold-coordinator` | 'Multi-signature signer and threshold coordination register: weight configurations, master key locks, and cosigner quorum thresholds for ... |
| 2704 | `steve-jobs` | "Agente que simula Steve Jobs — cofundador da Apple, CEO da Pixar, fundador da NeXT, o maior designer de produtos tecnologicos da histori... |
| 2705 | `stitch-design-taste` | "Use when generating Google Stitch DESIGN.md systems for premium typography, color, layout, motion intent, and anti-generic UI rules." |
| 2706 | `stitch-loop` | Teaches agents to iteratively build websites using Stitch with an autonomous baton-passing loop pattern |
| 2707 | `stitch-ui-design` | "Expert guidance for crafting effective prompts in Google Stitch, the AI-powered UI design tool by Google Labs. This skill helps create p... |
| 2708 | `story-bible-continuity` | 'Deterministic continuity check for long manuscripts against a story bible: name drift, age arithmetic, era anachronisms, unpaid foreshad... |
| 2709 | `stride-analysis-patterns` | "Apply STRIDE methodology to systematically identify threats. Use when analyzing system security, conducting threat modeling sessions, or... |
| 2710 | `stripe-automation` | "Automate Stripe tasks via Rube MCP (Composio): customers, charges, subscriptions, invoices, products, refunds. Always search tools first... |
| 2711 | `stripe-integration` | "Implement and verify Stripe checkout, subscriptions, webhooks and refunds with explicit server-side authorization and retry boundaries." |
| 2712 | `structured-data-validator` | "Structured Data Validator. Use when working with JSON-LD, Microdata or RDFa source." |
| 2713 | `styleseed-design-review` | "Reviews UI/frontend code and tells you exactly why it \"looks AI-generated\" — then how to fix it." |
| 2714 | `subagent-driven-development` | Use when executing implementation plans with independent tasks in the current session |
| 2715 | `subagent-orchestrator` | Coordinate quota-aware parallel subagents for large, multi-file Antigravity tasks. |
| 2716 | `subject-line-psychologist` | "Draft email subject lines and notification copy matched to audience and sequence position when earning attention requires clarity and tr... |
| 2717 | `suno-lyrics-to-song` | "Install and use the official Lyrics to Song package, pinned by digest, for paid hosted work on the Beatra service." |
| 2718 | `supabase` | "Use when doing ANY task involving Supabase." |
| 2719 | `supabase-automation` | "Automate Supabase database queries, table management, project administration, storage, edge functions, and SQL execution via Rube MCP (C... |
| 2720 | `supabase-edge-function-caller-auth` | "Audit and fix who can call each Supabase Edge Function: verify_jwt settings, withSupabase auth modes, role checks, webhook signatures an... |
| 2721 | `supabase-postgres-best-practices` | Postgres performance optimization and best practices from Supabase. Use this skill when writing, reviewing, or optimizing Postgres querie... |
| 2722 | `supabase-production` | 'A Supabase query, RPC or migration, ''db push'', ''supabase link'', RLS or grants, a Supabase error: server-only keys, deny-all RLS, mig... |
| 2723 | `super-code` | "Standing house style to enforce dense, correct, and idiomatic code on all coding tasks. Minimizes code bloat and agent operation overhead." |
| 2724 | `supercov` | "Measure line, branch and MC/DC coverage of a project's existing tests with the supercov CLI, then write small, focused tests for the cod... |
| 2725 | `superpowers-lab` | "Evaluate experimental Claude workflow skills in an isolated lab with reproducible tasks, observed results, and explicit adoption criteria." |
| 2726 | `supply-chain-attack-recon` | Authorized read-only review of public software supply-chain exposure |
| 2727 | `supply-chain-attack-response` | Detect, respond to, and prevent software supply chain attacks on package registries, container images, and CI/CD pipelines with lockfile ... |
| 2728 | `supply-chain-risk-auditor` | "Identifies dependencies at heightened risk of exploitation or takeover. Use when assessing supply chain attack surface, evaluating depen... |
| 2729 | `supply-chain-security` | "Software supply-chain security assessment: SBOM generation, SCA scanning, CI/CD pipeline review, container image audit, build integrity,... |
| 2730 | `survey-generator` | "Generate source-backed AI/ML survey paper artifacts with curated bibliographies and Fireworks/Kimi HTML rendering." |
| 2731 | `sveltekit` | "Build full-stack web applications with SvelteKit — file-based routing, SSR, SSG, API routes, and form actions in one framework." |
| 2732 | `swift-concurrency-expert` | Review and fix Swift concurrency issues such as actor isolation and Sendable violations. |
| 2733 | `swiftui-expert-skill` | "Write, review, and refactor SwiftUI for iOS or macOS, covering data flow, view composition, performance, identity, environment, localiza... |
| 2734 | `swiftui-liquid-glass` | Implement or review SwiftUI Liquid Glass APIs with correct fallbacks and modifier order. |
| 2735 | `swiftui-performance-audit` | Audit SwiftUI performance issues from code review and profiling evidence. |
| 2736 | `swiftui-ui-patterns` | Apply proven SwiftUI UI patterns for navigation, sheets, async state, and reusable screens. |
| 2737 | `swiftui-view-refactor` | Refactor SwiftUI views into smaller components with stable, explicit data flow. |
| 2738 | `sybil-glm53-offload-setup` | "Select, verify and benchmark a GLM-5.3-Flash EXL3 offload mode on a single supported Linux NVIDIA host." |
| 2739 | `sybil-inference-optimisation` | "Benchmark and tune local LLM serving against a measured ceiling with controlled comparisons, resource limits and quality gates." |
| 2740 | `sybil-local-studio-contribution-triage` | "Evaluate PR eligibility from pinned T3 Code policy and immutable submission evidence before any authorised moderation." |
| 2741 | `sybil-local-studio-test-t3-app` | "Verify a T3 Code web or desktop flow through its Browser panel against isolated checkout state." |
| 2742 | `sybil-local-studio-test-t3-mobile` | "Verify the native T3 Code client through its Device panel, an isolated backend and the returned target-specific controls." |
| 2743 | `sympy` | "SymPy is a Python library for symbolic mathematics that enables exact computation using mathematical symbols rather than numerical appro... |
| 2744 | `sync-lipsync` | "Lip-sync an existing video of a real person to new audio or a typed script with sync. labs through its hosted MCP server, quoting the co... |
| 2745 | `syncbook-discovery` | "Find reciprocal collaborators on Syncbook or prepare a private profile draft for human review using only explicitly supplied task facts." |
| 2746 | `sys-configure` | Configure Claude Octopus — redirects to /octo:setup interactive wizard |
| 2747 | `system-prompt-lookup` | Checks what a shipped AI product's system prompt and tool schema actually say, by reading a dated archive of captured prompts instead of ... |
| 2748 | `systematic-debugging` | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes |
| 2749 | `systemd-services` | Create and manage systemd services and timers. Configure service dependencies and resource limits. Use when managing system services. |
| 2750 | `systems-programming-rust-project` | "You are a Rust project architecture expert specializing in scaffolding production-ready Rust applications. Generate complete project str... |
| 2751 | `taasky` | "Negotiate terms with another person or their agent through the hosted Taasky MCP server: meeting times, prices, dates. The human confirm... |
| 2752 | `tailwind-design-system` | "Build production-ready design systems with Tailwind CSS, including design tokens, component variants, responsive patterns, and accessibi... |
| 2753 | `tailwind-patterns` | "Tailwind CSS v4 principles. CSS-first configuration, container queries, modern patterns, design token architecture." |
| 2754 | `taisly-social-media-posting` | "Use Taisly Agent Kit to prepare and publish approved short-form video posts across TikTok, Instagram Reels, YouTube Shorts, X, and Faceb... |
| 2755 | `takeout-coupon` | "Call takeout coupon API to fetch hidden coupon lists, red packets and aggregated redemption pages for platforms (Meituan, Taobao Flash/E... |
| 2756 | `talivia-agent-kit` | "Set up and verify Talivia revenue analytics through MCP, with explicit confirmation for website changes and payment attribution." |
| 2757 | `talking-avatar-video` | "Install and use the official Talking Avatar Video package, pinned by digest, for paid hosted work on the Beatra service." |
| 2758 | `tanstack-query-expert` | "Expert in TanStack Query (React Query) — asynchronous state management. Covers data fetching, stale time configuration, mutations, optim... |
| 2759 | `task-intelligence` | "Protocolo de Inteligência Pré-Tarefa — planeja a tarefa e consulta apenas agentes disponíveis, relevantes e autorizados quando o benefíc... |
| 2760 | `tastegate` | "Build or fix a frontend so it looks designed, not AI-generated, then prove it in a real browser: renders at phone and desktop width and ... |
| 2761 | `tavily-web` | "Web search, content extraction, crawling, and research capabilities using Tavily API. Use when you need to search the web for current in... |
| 2762 | `tax-register` | 'Tax register: sales and purchase tax, withholding deducted and received, net payable, filing due date and days remaining. Use for tax co... |
| 2763 | `tcm-constitution-analyzer` | 分析中医体质数据、识别体质类型、评估体质特征,并提供个性化养生建议。支持与营养、运动、睡眠等健康数据的关联分析。 |
| 2764 | `tdd` | Test-driven development. Use when the user wants to build features or fix bugs test-first, mentions "red-green-refactor", or wants integr... |
| 2765 | `tdd-orchestrator` | Master TDD orchestrator specializing in red-green-refactor discipline, multi-agent workflow coordination, and comprehensive test-driven d... |
| 2766 | `tdd-workflow` | "Test-Driven Development workflow principles. RED-GREEN-REFACTOR cycle." |
| 2767 | `tdd-workflows` | "Use when working with tdd workflows tdd cycle (Alias for tdd-workflows-tdd-cycle)" |
| 2768 | `tdd-workflows-tdd-cycle` | "Use when working with tdd workflows tdd cycle" |
| 2769 | `tdd-workflows-tdd-green` | "Implement the minimal code needed to make failing tests pass in the TDD green phase." |
| 2770 | `tdd-workflows-tdd-red` | "Generate failing tests for the TDD red phase to define expected behavior and edge cases." |
| 2771 | `tdd-workflows-tdd-refactor` | "Use when working with tdd workflows tdd refactor" |
| 2772 | `tds-booking-payment` | 'TDS register: payee PAN, payment nature, rate and amount deducted, deposit date and challan reference, return filing and ledger variance... |
| 2773 | `teach` | Teach the user a new skill or concept, within this workspace. |
| 2774 | `team-calendar` | 'Team calendar: event, type, date and time with time zone, attendees, organizer, location and source module. Use for shared scheduling.' |
| 2775 | `team-collaboration-issue` | "You are a GitHub issue resolution expert specializing in systematic bug investigation, feature implementation, and collaborative develop... |
| 2776 | `team-collaboration-standup-notes` | "You are an expert team communication specialist focused on async-first standup practices, AI-assisted note generation from commit histor... |
| 2777 | `team-composition-analysis` | "Design optimal team structures, hiring plans, compensation strategies, and equity allocation for early-stage startups from pre-seed thro... |
| 2778 | `teardown` | Creates technical illustrations of physical objects and of how things work, such as display pixels or interface layers, with coherent vie... |
| 2779 | `tech-writing-proofread` | "Proofreads English technical writing for typos, grammar, punctuation, terminology consistency, jargon, and structure; returns an itemize... |
| 2780 | `technical-change-tracker` | "Track code changes with structured JSON records, state machine enforcement, and AI session handoff for bot continuity" |
| 2781 | `technical-tutorials` | When the user wants to create step-by-step technical tutorials, quickstarts, or code walkthroughs. Trigger phrases include "tutorial," "q... |
| 2782 | `telegram` | Integracao completa com Telegram Bot API. Setup com BotFather, mensagens, webhooks, inline keyboards, grupos, canais. Boilerplates Node.j... |
| 2783 | `telegram-automation` | "Automate Telegram tasks via Rube MCP (Composio): send messages, manage chats, share photos/documents, and handle bot commands. Always se... |
| 2784 | `telegram-bot-builder` | Expert in building Telegram bots that solve real problems - from simple automation to complex AI-powered bots. Covers bot architecture, t... |
| 2785 | `telegram-bot-messaging` | "Send Telegram messages, files, and alerts via bot API; ask questions with inline buttons and wait for the answer. Supports multiple bots... |
| 2786 | `telegram-channel-ads` | "Vet and price ad posts in Telegram channels: reach benchmarks by size, topic and language, ad-network and channel-age checks, CPM and de... |
| 2787 | `telegram-mini-app` | Expert in building Telegram Mini Apps (TWA) - web apps that run inside Telegram with native-like experience. Covers the TON ecosystem, Te... |
| 2788 | `template-library` | 'Template register: name, type, owning module and department, owner, last updated and content link. Use for document template governance.' |
| 2789 | `temporal-golang-pro` | "Use when building durable distributed systems with Temporal Go SDK. Covers deterministic workflow rules, mTLS worker configs, and advanc... |
| 2790 | `temporal-python-pro` | Master Temporal workflow orchestration with Python SDK. Implements durable workflows, saga patterns, and distributed transactions. Covers... |
| 2791 | `temporal-python-testing` | "Comprehensive testing approaches for Temporal workflows using pytest, progressive disclosure resources for specific testing scenarios." |
| 2792 | `terraform-aws` | Provision AWS infrastructure with Terraform. Create modules, manage state, and implement IaC best practices. Use when deploying AWS resou... |
| 2793 | `terraform-aws-modules` | "Terraform module creation for AWS — reusable modules, state management, and HCL best practices. Use when building or reviewing Terraform... |
| 2794 | `terraform-azure` | Provision Azure infrastructure with Terraform. Configure providers, manage state, and deploy resources. Use when implementing IaC for Azure. |
| 2795 | `terraform-gcp` | Provision GCP infrastructure with Terraform. Configure providers and deploy Google Cloud resources. Use when implementing IaC for GCP. |
| 2796 | `terraform-infrastructure` | "Terraform infrastructure as code workflow for provisioning cloud resources, creating reusable modules, and managing infrastructure at sc... |
| 2797 | `terraform-module-library` | "Production-ready Terraform module patterns for AWS, Azure, and GCP infrastructure." |
| 2798 | `terraform-skill` | "Terraform infrastructure as code best practices" |
| 2799 | `terraform-specialist` | Expert Terraform/OpenTofu specialist mastering advanced IaC automation, state management, and enterprise infrastructure patterns. |
| 2800 | `test-automator` | Master AI-powered test automation with modern frameworks, self-healing tests, and comprehensive quality engineering. Build scalable testi... |
| 2801 | `test-driven-development` | Use when implementing any feature or bugfix, before writing implementation code |
| 2802 | `test-fixing` | "Systematically identify and fix all failing tests using smart grouping strategies. Use when explicitly asks to fix tests (\"fix these te... |
| 2803 | `test-framework-migration-skill` | "Migrates and converts test automation scripts between Selenium, Playwright, Puppeteer, and Cypress." |
| 2804 | `test-guard` | "Review generated or changed test code against universal testing rules before it ships or is presented for approval." |
| 2805 | `test-harness` | 'Writing or running tests, proving a fix, a red or flaky run, a fix that didn''t land, ''is it verified'', ''run the gate'': tests where ... |
| 2806 | `testdriver-e2e-testing` | "Build E2E tests with TestDriver.ai, the AI code reviewer that runs every pull request in a real desktop sandbox, finds bugs, and builds ... |
| 2807 | `testing-patterns` | "Jest testing patterns, factory functions, mocking strategies, and TDD workflow. Use when writing unit tests, creating test factories, or... |
| 2808 | `testing-qa` | "Comprehensive testing and QA workflow covering unit testing, integration testing, E2E testing, browser automation, and quality assurance." |
| 2809 | `testng-skill` | 'Generates TestNG tests in Java with groups, data providers, parallel execution, XML suite configuration, and listeners. Use when user me... |
| 2810 | `text-to-html-converter` | "Text to HTML Converter. Use when working with plain text and optional structure preferences." |
| 2811 | `text-translator` | "Text Translator. Use when working with source text and target language or locale." |
| 2812 | `textme` | "Text Claude from your phone — set up the njerschow/textme daemon so inbound iMessages drive a Claude Code session on your laptop, with v... |
| 2813 | `the-honoured-one` | "Forces the AI to fully load context and read relevant files before performing complex, multi-file tasks, architectural changes, or debug... |
| 2814 | `theme-factory` | "This skill provides a curated collection of professional font and color themes, each with carefully selected color palettes and font pai... |
| 2815 | `thick-client` | "Authorized security testing of desktop thick clients: local storage, update channels, IPC, traffic interception, and client-side trust-b... |
| 2816 | `threat-hunting` | "Blue-team threat hunting: detection engineering with Sigma/YARA, SIEM query design, and validation of incident detections against known ... |
| 2817 | `threat-intelligence` | "Authorized OSINT and cyber threat intelligence: enriching IOCs, campaigns, impersonation, scams, and threat-actor profiles from public s... |
| 2818 | `threat-mitigation-mapping` | "Map identified threats to appropriate security controls and mitigations. Use when prioritizing security investments, creating remediatio... |
| 2819 | `threat-modeling` | Conduct threat modeling using STRIDE methodology. Identify threats, assess risks, and design security controls. Use when designing secure... |
| 2820 | `threat-modeling-expert` | "Expert in threat modeling methodologies, security architecture review, and risk assessment. Masters STRIDE, PASTA, attack trees, and sec... |
| 2821 | `threejs-animation` | Three.js animation - keyframe animation, skeletal animation, morph targets, animation mixing. Use when animating objects, playing GLTF an... |
| 2822 | `threejs-fundamentals` | Three.js scene setup, cameras, renderer, Object3D hierarchy, coordinate systems. Use when setting up 3D scenes, creating cameras, configu... |
| 2823 | `threejs-geometry` | Three.js geometry creation - built-in shapes, BufferGeometry, custom geometry, instancing. Use when creating 3D shapes, working with vert... |
| 2824 | `threejs-interaction` | Three.js interaction - raycasting, controls, mouse/touch input, object selection. Use when handling user input, implementing click detect... |
| 2825 | `threejs-lighting` | Three.js lighting - light types, shadows, environment lighting. Use when adding lights, configuring shadows, setting up IBL, or optimizin... |
| 2826 | `threejs-loaders` | Three.js asset loading - GLTF, textures, images, models, async patterns. Use when loading 3D models, textures, HDR environments, or manag... |
| 2827 | `threejs-materials` | Three.js materials - PBR, basic, phong, shader materials, material properties. Use when styling meshes, working with textures, creating c... |
| 2828 | `threejs-postprocessing` | Three.js post-processing - EffectComposer, bloom, DOF, screen effects. Use when adding visual effects, color grading, blur, glow, or crea... |
| 2829 | `threejs-shaders` | Three.js shaders - GLSL, ShaderMaterial, uniforms, custom effects. Use when creating custom visual effects, modifying vertices, writing f... |
| 2830 | `threejs-skills` | "Create 3D scenes, interactive experiences, and visual effects using Three.js. Use when user requests 3D graphics, WebGL experiences, 3D ... |
| 2831 | `threejs-textures` | Three.js textures - texture types, UV mapping, environment maps, texture settings. Use when working with images, UV coordinates, cubemaps... |
| 2832 | `tiktok-automation` | "Automate TikTok tasks via Rube MCP (Composio): upload/publish videos, post photos, manage content, and view user profiles/stats. Always ... |
| 2833 | `time-ledger` | "Natural-language time tracking: parse what the user says they did into Activity/Minutes/Date rows in their own Notion database — asking ... |
| 2834 | `time-machine-recovery` | "Diagnose failed or stalled macOS Time Machine backups and recover space on local APFS destinations that remain full after backup deletion." |
| 2835 | `time-tracking` | 'Time entry register: employee, project, client, task, hours, billable flag, rate and amount, invoice and approver. Use for time tracking.' |
| 2836 | `title-meta-length-counter` | "Title & Meta Length Counter. Use when working with title and/or meta description." |
| 2837 | `tmux` | "Expert tmux session, window, and pane management for terminal multiplexing, persistent remote workflows, and shell scripting automation." |
| 2838 | `to-issues` | Break a plan, spec, or PRD into independently-grabbable issues on the project issue tracker using tracer-bullet vertical slices. |
| 2839 | `to-prd` | Turn the current conversation into a PRD and publish it to the project issue tracker — no interview, just synthesis of what you've alread... |
| 2840 | `todoist-automation` | "Automate Todoist task management, projects, sections, filtering, and bulk operations via Rube MCP (Composio). Always search tools first ... |
| 2841 | `tokenleak` | "Token-lean rules for coding agents: cut the context re-sent on every later call (big reads, noisy logs, re-reads, serial calls) without ... |
| 2842 | `tokenwise` | "Measurement-driven model router for Claude Code. Routes Haiku/Sonnet/Opus per task class, logs every routed task with real $ numbers, an... |
| 2843 | `tone-of-voice-analyzer` | "Tone of Voice Analyzer. Use when working with text and optional brand voice sample." |
| 2844 | `tool-design` | "Build tools that agents can use effectively, including architectural reduction patterns. Use when creating new tools for agent systems, ... |
| 2845 | `tool-use-guardian` | "Triage tool failures, validate responses and resume bounded workflows using replay-safe retries and explicit handling of unknown write o... |
| 2846 | `tools-page-seo-optimizer` | "Framework-agnostic SEO workflow for any site with multiple tool, product, or feature pages. Covers duplicate content, unique meta tags, ... |
| 2847 | `top-web-vulnerabilities` | "Provide an illustrative, overlapping reference for common web application vulnerability patterns organized by category. This skill enabl... |
| 2848 | `track-management` | Use this skill when creating, managing, or working with Conductor tracks - the logical work units for features, bugs, and refactors. Appl... |
| 2849 | `traderspy-market-briefing` | "Crypto market briefing from live TraderSpy data: majors, funding, open interest, top-trader lean, fresh AI signals and screener movers. ... |
| 2850 | `traderspy-market-screener` | "Scan the most-traded crypto futures pairs for up to 3 technical conditions in one TraderSpy call, compare coins, and backtest what follo... |
| 2851 | `traderspy-position-check` | "Health-check crypto futures positions the user describes, with TraderSpy data: liquidation and stop distance, multi-timeframe read, fund... |
| 2852 | `traderspy-smart-money` | "Track what top crypto futures traders hold on Binance, Hyperliquid, Bybit and OKX with TraderSpy: elite leaderboard, positions, trader p... |
| 2853 | `traderspy-technical-analysis` | "Read one crypto futures pair with TraderSpy: 19 indicators on up to 3 timeframes in one call, key levels, funding, open interest and pos... |
| 2854 | `traderspy-trading-signals` | "Fetch and explain TraderSpy's AI crypto futures signals: entry, take-profit ladder, stop, triggers, status against the live price, and h... |
| 2855 | `trading-ledger` | "A trading journal that captures the decision, not just the fill: thesis, plan, and emotion at the moment of entry, written to the user's... |
| 2856 | `traffic-potential-calculator` | "Traffic Potential Calculator. Use when working with search volume and explicit CTR assumptions for matching period and market." |
| 2857 | `train-sentence-transformers` | "Train or fine-tune SentenceTransformer, CrossEncoder, and SparseEncoder models for retrieval, similarity, clustering, classification, re... |
| 2858 | `transactional-email` | 'Adding transactional or alert email, choosing a provider, ''sent twice'', ''never arrived'': app email sent once, never lost, with one-c... |
| 2859 | `transformers-js` | "Use Transformers.js to run state-of-the-art machine learning models directly in JavaScript/TypeScript." |
| 2860 | `transitions-dev` | Production-ready CSS transitions for web apps. Use when implementing notification badges, dropdowns, modals, panel reveals, page transiti... |
| 2861 | `transitions-polish` | Polish and refine existing motion against the transitions.dev motion-token scale — duration, distance, scale, blur, and easing — plus the... |
| 2862 | `travel-health-analyzer` | 分析旅行健康数据、评估目的地健康风险、提供疫苗接种建议、生成多语言紧急医疗信息卡片。支持WHO/CDC数据集成的专业级旅行健康风险评估。 |
| 2863 | `travel-planner` | "旅行/行程规划需求时使用:规划去某地旅行、X天X城、带老人孩子、自驾、假期安排等。产出逐日行程表、预算估算(经济/舒适/奢华三档)、交通住宿建议、景点美食清单。必须先问预算,预算未确认只输出问题清单;事实数据带来源和查询日期。" |
| 2864 | `tree-ring-memory` | "Use Tree Ring Memory for local-first AI-agent memory lifecycle work: recall, evidence, audit, forgetting, and consolidation without tran... |
| 2865 | `treg` | "Use the Treg CLI or MCP catalog to discover, price and call authorized external tools with team-scoped credentials and a user-approved b... |
| 2866 | `trello-automation` | "Automate Trello boards, cards, and workflows via Rube MCP (Composio). Create cards, manage lists, assign members, and search across boar... |
| 2867 | `trending-keyword-visualizer` | "Trending Keyword Visualizer. Use when working with dated keyword interest or volume series with source." |
| 2868 | `triage` | Move issues and external PRs through a state machine of triage roles — categorise, verify, grill if needed, and write agent-ready briefs. |
| 2869 | `triage-validation` | Finding validation before writing any report |
| 2870 | `trigger-dev` | Trigger.dev expert for background jobs, AI workflows, and reliable async execution with excellent developer experience and TypeScript-fir... |
| 2871 | `trip-coupon` | "Call trip/travel coupon API to fetch travel coupons including DiDi ride-hailing gift packages and hotel coupon bundles. Returns coupon l... |
| 2872 | `trl-training` | Train and fine-tune transformer language models using TRL (Transformers Reinforcement Learning). Supports SFT, DPO, GRPO, KTO, RLOO and R... |
| 2873 | `trpc-fullstack` | "Build end-to-end type-safe APIs with tRPC — routers, procedures, middleware, subscriptions, and Next.js/React integration patterns." |
| 2874 | `trust-calibrator` | "Diagnose audience trust barriers and calibrate proof, certainty, and credibility signals when messaging overclaims or fails to reassure." |
| 2875 | `tune-monitor` | Analyze a Monte Carlo monitor and recommend config changes to reduce alert noise. Supports metric, custom SQL, validation, and table moni... |
| 2876 | `turborepo-caching` | "Configure Turborepo for efficient monorepo builds with local and remote caching. Use when setting up Turborepo, optimizing build pipelin... |
| 2877 | `turn-this-into-a-thread` | "Turn a long idea, transcript, article or draft into a Twitter thread where every tweet stands alone. Use when someone asks for a thread ... |
| 2878 | `tutorial-engineer` | Creates step-by-step tutorials and educational content from code. Transforms complex concepts into progressive learning experiences with ... |
| 2879 | `tweetapi` | "Look up public Twitter/X profiles, tweets, search results, lists, communities and Spaces with TweetAPI's REST API or hosted MCP server. ... |
| 2880 | `twilio-communications` | "Build communication features with Twilio: SMS messaging, voice calls, WhatsApp Business API, and user verification (2FA). Covers the ful... |
| 2881 | `twitter-automation` | "Automate Twitter/X tasks via Rube MCP (Composio): posts, search, users, bookmarks, lists, media. Always search tools first for current s... |
| 2882 | `typescript-advanced-types` | "Comprehensive guidance for mastering TypeScript's advanced type system including generics, conditional types, mapped types, template lit... |
| 2883 | `typescript-expert` | TypeScript and JavaScript expert with deep knowledge of type-level programming, performance optimization, monorepo management, migration ... |
| 2884 | `typescript-pro` | Master TypeScript with advanced types, generics, and strict type safety. Handles complex type systems, decorators, and enterprise-grade p... |
| 2885 | `ui-a11y` | Audit a component or page for accessibility issues and fix them |
| 2886 | `ui-component` | Generate a new UI component following the StyleSeed design conventions |
| 2887 | `ui-design` | 'Mandatory for any product''s screens, a builder''s too, and any mock, prototype or artifact that shows them: its design system, colour, ... |
| 2888 | `ui-diff` | "Compare UI screenshots between revisions, capture interactions, and draft a visual PR review. Use for visual regressions, component diff... |
| 2889 | `ui-from-screenshot` | "Turn a screenshot or mockup into matching UI with the project's own components, then compare the result side by side with the image and ... |
| 2890 | `ui-lint` | Quick automated lint — detects common design system violations in seconds |
| 2891 | `ui-motion` | "Apply a named StyleSeed motion to a component — either one of the 5 personality seeds (Spring/Silk/Snap/Float/Pulse × entrance/exit/hove... |
| 2892 | `ui-page` | Scaffold a new mobile page/screen using the StyleSeed layout patterns |
| 2893 | `ui-pattern` | Generate a composed UI pattern (card layout, list, form section, grid, etc.) using design system primitives |
| 2894 | `ui-review` | Review UI code for design system compliance, accessibility, and best practices |
| 2895 | `ui-score` | Score a UI file's design quality 0-100 against StyleSeed's design language — per-category breakdown, the worst offenders, and a prioritiz... |
| 2896 | `ui-setup` | Interactive setup wizard — guides you step-by-step to configure the design system for your project |
| 2897 | `ui-skills` | "Opinionated, evolving constraints to guide agents when building interfaces" |
| 2898 | `ui-skills-root` | Use before UI-related work to select the smallest useful UI Skills context through the ui-skills CLI. |
| 2899 | `ui-states` | "Design and build the UI states agents forget: first use, empty, loading, error, offline, no results, long content, permission denied and... |
| 2900 | `ui-tokens` | View, add, or modify design tokens in the StyleSeed design system |
| 2901 | `ui-update` | Update StyleSeed engine in your project — analyzes what's outdated and updates safely |
| 2902 | `ui-ux-designer` | Create interface designs, wireframes, and design systems. Masters user research, accessibility standards, and modern design tools. |
| 2903 | `ui-ux-pro-max` | "Comprehensive design guide for web and mobile applications. Use when designing new UI components or pages, choosing color palettes and t... |
| 2904 | `ui-visual-validator` | Rigorous visual validation expert specializing in UI testing, design system compliance, and accessibility verification. |
| 2905 | `uiverify-triage-visual-changes` | "Triage a UI Verify visual regression build from your coding agent over MCP: sort changed screenshots into regressions, intended changes ... |
| 2906 | `ultrafast` | "Make or edit videos as ultrafast JSON documents with the uf CLI or its MCP tools: write, check, look at frames, review, then export MP4,... |
| 2907 | `uncle-bob-craft` | "Use when performing code review, writing or refactoring code, or discussing architecture; complements clean-code and does not replace pr... |
| 2908 | `understand-customers` | Synthesize consented customer research into pains, buying objections, switching triggers and attributed customer language before drafting... |
| 2909 | `understand-project-yylo` | Inspect the current product architecture, dependencies, and validation loops before planning or implementing a requested change. |
| 2910 | `unified-ai-gateway` | Operate and evaluate Unified AI System through fifteen governed MCP tools, including provider-free prompt enhancement, while preserving f... |
| 2911 | `uniprot-database` | Direct REST API access to UniProt. Protein searches, FASTA retrieval, ID mapping, Swiss-Prot/TrEMBL. For Python workflows with multiple d... |
| 2912 | `unit-testing-test-generate` | "Generate comprehensive, maintainable unit tests across languages with strong coverage and edge case focus." |
| 2913 | `unity-ai-game-creator` | "Transform raw game ideas into complete Unity projects with AI-powered asset generation, scene blueprints, music/SFX prompts, and step-by... |
| 2914 | `unity-developer` | Build Unity games with optimized C# scripts, efficient rendering, and proper asset management. Masters Unity 6 LTS, URP/HDRP pipelines, a... |
| 2915 | `unity-ecs-patterns` | "Production patterns for Unity's Data-Oriented Technology Stack (DOTS) including Entity Component System, Job System, and Burst Compiler." |
| 2916 | `unpaid-intern` | "A free second brain for work in plain markdown files the user owns. Turns transcripts, docs, and tickets into briefings, meeting prep, d... |
| 2917 | `unpolish-ai-writing` | "Strip AI writing tells from a draft, then optionally add sparse seeded typos at researched human error rates. Use for deslop, imperfecti... |
| 2918 | `unreal-engine-cpp-pro` | "Expert guide for Unreal Engine 5.x C++ development, covering UObject hygiene, performance patterns, and best practices." |
| 2919 | `unship` | "Compare AI agent-made UI variants locally in a real app, then keep one and clean up unused temporary code." |
| 2920 | `unslop` | "Post-process AI-generated text through the unslop CLI to strip AI writing patterns before publishing" |
| 2921 | `unslop-commit` | "Rewrites commit messages so they sound like a careful human engineer wrote them. Strips AI/marketing slop (\"comprehensive solution\", \... |
| 2922 | `unslop-file` | "Humanize natural-language memory files (CLAUDE.md, todos, preferences, docs) by removing AI-isms and adding burstiness while preserving ... |
| 2923 | `unslop-review` | "Rewrites code review comments so they read like a human teammate wrote them. Cuts corporate-AI throat-clearing (\"I noticed...\", \"I wa... |
| 2924 | `unslop-seo` | Edit existing SEO and answer-engine content for plain language, accurate entities, cited claims and readable heading structure. |
| 2925 | `unslop-ui` | "Audit and redesign AI-generated interfaces with product-specific visual direction, structured design passes, and optional snapshots or s... |
| 2926 | `unslop-ui-audit` | "Use the Unslop UI design linter for static frontend diagnostics, contrast checks, and reviewing design presets." |
| 2927 | `unsloth-finetuning` | "Fine-tune and post-train LLMs with Unsloth Core on a single consumer GPU: VRAM sizing, LoRA/QLoRA, GRPO/DPO, chat-template correctness, ... |
| 2928 | `unsplash-integration` | Integration skill for searching and fetching high-quality, free-to-use professional photography from Unsplash. |
| 2929 | `untangle-codebase` | Untangle a whole codebase in one pass, so agents working in it read less per change, break less without noticing, and debug faster. |
| 2930 | `update-swiftui-apis` | "Scan Apple's SwiftUI documentation for deprecated APIs and update the SwiftUI Expert Skill with modern replacements." |
| 2931 | `upgrading-expo` | Guidelines for upgrading Expo SDK versions and fixing dependency issues |
| 2932 | `upstash-qstash` | Upstash QStash expert for serverless message queues, scheduled jobs, and reliable HTTP-based task delivery without managing infrastructure. |
| 2933 | `upstash-ratelimit` | "Add rate limiting to API routes, middleware, and edge functions with @upstash/ratelimit: sliding window, fixed window, and token bucket ... |
| 2934 | `upstash-redis` | "Use the @upstash/redis HTTP client for caching, sessions, counters, and Redis data structures from serverless and edge runtimes without ... |
| 2935 | `uptime-monitoring` | 'Publishing an app, adding /health or a cron job, ''set up monitoring'', ''is it down'': content checks, a second location, heartbeats, a... |
| 2936 | `url-slug-generator` | "URL Slug Generator. Use when working with page title and optional language or URL policy." |
| 2937 | `url-to-markdown` | "Fetch a public webpage as clean Markdown for an agent: read, summarize, quote, or cite the page while preserving its source URL." |
| 2938 | `us-property-data` | "Use when a task needs real U.S. residential property data: valuation, listings, price or tax history, schools, or a zillow.com URL." |
| 2939 | `us-watchlist-alerts` | "Free US stock watchlists, price alerts and daily briefs; no API key, NYSE-holiday aware. Informational only, never places trades." |
| 2940 | `usage-based-pricing` | "Design pricing models that developers understand, accept, and can predict. Trigger phrases: usage-based pricing, API pricing, metered bi... |
| 2941 | `usage-engineer` | "Cut wasted tokens in coding-agent sessions: compact long logs, stop identical retries, check stale project maps, and audit local Codex/O... |
| 2942 | `use-dom` | Use Expo DOM components to run web code in a webview on native and as-is on web. Migrate web code to native incrementally. |
| 2943 | `user-management` | Manage users, groups, and permissions on Linux systems. Configure sudo and access controls. Use when managing system access. |
| 2944 | `user-thoughts` | Persist user decisions and project constraints to mdbase across sessions. Use on explicit /user-thoughts or /ustht requests, or within pr... |
| 2945 | `using-agent-skills` | Meta-skill for discovering and invoking the right agent skill for the work at hand, applied at session start. |
| 2946 | `using-git-worktrees` | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - ensures an isolated... |
| 2947 | `using-lwc` | "Use when project decisions, code structure, research, incidents, or verified context must survive future coding-agent sessions through L... |
| 2948 | `using-n8n-mcp-skills` | Route n8n MCP workflow design, editing, validation, testing, deployment, credential, execution, and debugging tasks to specialist guidance. |
| 2949 | `using-neon` | "Neon is a serverless Postgres platform that separates compute and storage to offer autoscaling, branching, instant restore, and scale-to... |
| 2950 | `using-superpowers` | Use when starting any conversation - establishes how to find and use skills, requiring skill invocation before ANY response including cla... |
| 2951 | `uv-package-manager` | "Comprehensive guide to using uv, an extremely fast Python package installer and resolver written in Rust, for modern Python project mana... |
| 2952 | `ux-audit` | Audit screens for UX issues using Nielsen's heuristics and modern mobile UX best practices |
| 2953 | `ux-copy` | Generate UX microcopy (button labels, error messages, empty states, toasts) following a casual-but-polite voice and tone |
| 2954 | `ux-feedback` | Add appropriate user feedback states (loading, success, error, empty) to a component or page |
| 2955 | `ux-flow` | Design user flows and navigation structure following proven UX patterns |
| 2956 | `ux-persuasion-engineer` | "Audit decision friction and propose clear, accessible UX flows when layout, defaults, or sequencing obstruct informed action." |
| 2957 | `uxkin-research` | "Research how real products handle a screen, flow or visual style before designing it: search UXKIN's real iOS screens, user journeys and... |
| 2958 | `uxui-principles` | "Evaluate interfaces against 168 research-backed UX/UI principles, detect antipatterns, and inject UX context into AI coding sessions." |
| 2959 | `value-curve` | 'Comparing a product with competitors or choosing what to be best at: a value curve on one segment''s top needs, plus price.' |
| 2960 | `value-proposition` | 'Creating or testing a value proposition: the 6-part form (Who, Why, What before, How, What after, Alternatives).' |
| 2961 | `variant` | Builds multiple variants of a component you're working on and helps you iterate and pick one. |
| 2962 | `variant-analysis` | Find similar vulnerabilities and bugs across codebases using pattern-based analysis. Use when hunting bug variants, building CodeQL/Semgr... |
| 2963 | `varlock` | "Secure-by-default environment variable management for Claude Code sessions." |
| 2964 | `varlock-claude-skill` | "Secure environment variable management with explicit checks to reduce secret exposure in Claude sessions, terminals, logs, or git commits" |
| 2965 | `vector-database-engineer` | "Expert in vector databases, embedding strategies, and semantic search implementation. Masters Pinecone, Weaviate, Qdrant, Milvus, and pg... |
| 2966 | `vector-database-ops` | Deploy, manage, and optimize vector databases for AI applications. |
| 2967 | `vector-index-tuning` | "Optimize vector index performance for latency, recall, and memory. Use when tuning HNSW parameters, selecting quantization strategies, o... |
| 2968 | `veille-mcp` | "Check emails, domains, phone numbers and IPs for fraud signals, and validate EU VAT numbers and IBANs, through Veille's MCP server. Use ... |
| 2969 | `vendor-contractor-management` | 'Vendor register: name, type, services, contact, linked contract dates, payment terms and rating. Use for vendor and contractor management.' |
| 2970 | `vendor-management` | Implement vendor risk management programs. Assess third-party security and maintain vendor inventory. Use when managing supplier security. |
| 2971 | `vercel-ai-sdk-expert` | "Expert in the Vercel AI SDK. Covers Core API (generateText, streamText), UI hooks (useChat, useCompletion), tool calling, and streaming ... |
| 2972 | `vercel-automation` | "Automate Vercel tasks via Rube MCP (Composio): manage deployments, domains, DNS, env vars, projects, and teams. Always search tools firs... |
| 2973 | `vercel-cli-with-tokens` | "Deploy and manage projects on Vercel using token-based authentication. Use when working with Vercel CLI using access tokens rather than ... |
| 2974 | `vercel-deployment` | Expert knowledge for deploying to Vercel with Next.js |
| 2975 | `vercel-deployments` | Deploy frontend and full-stack apps on Vercel with previews, edge functions, environment promotion, and production guardrails. |
| 2976 | `vercel-optimize` | "Audit deployed Vercel apps for cost and performance issues using metrics, project config, code scans, and version-aware recommendations." |
| 2977 | `vercel-react-view-transitions` | "Guide React and Next.js view transitions, shared element animations, route transitions, transition types, and reduced-motion-safe UI sta... |
| 2978 | `vercel-vgpu` | "Build and profile WGSL shaders and WebGPU passes using the installed vgpu package and version-matched documentation." |
| 2979 | `verification-before-completion` | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands a... |
| 2980 | `verify-citations` | Verify citations and references in a document, report, or article against real sources. Use when the user asks to fact-check, verify refe... |
| 2981 | `verify-document` | Check whether a document (PDF or image) shows signs of tampering or forgery before you rely on it. Use when the user asks to verify a pay... |
| 2982 | `verl-rl-training` | Provides guidance for training LLMs with reinforcement learning using verl (Volcano Engine RL). Use when implementing RLHF, GRPO, PPO, or... |
| 2983 | `vexor` | "Vector-powered CLI for semantic file search with a Claude/Codex skill" |
| 2984 | `vexor-cli` | Semantic file discovery via `vexor`. Use whenever locating where something is implemented/loaded/defined in a medium or large repo, or wh... |
| 2985 | `vibe-abliteration` | "Run Heretic directional abliteration to reduce a model's refusals: set up, optimize, read the Pareto front, verify the export, then save... |
| 2986 | `vibe-code-auditor` | Audit rapidly generated or AI-produced code for structural flaws, fragility, and production risks. |
| 2987 | `vibe-code-cleanup` | "Safe production cleanup and hardening for vibe-coded fullstack apps (Next.js, React, Node.js, etc.). Removes dead imports, unused files,... |
| 2988 | `vibe-delegate` | Delegate coding tasks to the Mistral Vibe CLI (`vibe`) only when the user explicitly requests it, while the orchestrator retains review a... |
| 2989 | `vibe-shield` | "Audit Next.js, React, Express, Hono, Supabase SQL, Stripe webhooks, and SKILL.md or MCP configs across 92 static security and prompt-inj... |
| 2990 | `vibecode-production-qa-validator` | "13-phase production QA for fullstack Next.js apps: build verification, SEO tags, OG images, favicon, route regression, API auth, page sp... |
| 2991 | `vibers-code-review` | Human review workflow for AI-generated GitHub projects with spec-based feedback, security review, and follow-up PRs from the Vibers service. |
| 2992 | `viboscope` | "Psychological compatibility matching — find cofounders, collaborators, and friends with explicit consent and unverified provider scoring" |
| 2993 | `video-content-extractor` | "Extract key frames from MP4 videos at configurable intervals, run Tesseract OCR, and generate structured Markdown reports with video met... |
| 2994 | `video-router` | "Route a video-production brief to generation, deterministic composition, supplied-footage editing, or an automatic cross-modal plan befo... |
| 2995 | `videodb` | Video and audio perception, indexing, and editing. Ingest files/URLs/live streams, build visual/spoken indexes, search with timestamps, e... |
| 2996 | `videodb-skills` | "Upload, stream, search, edit, transcribe, and generate AI video and audio using the VideoDB SDK." |
| 2997 | `viral-generator-builder` | Expert in building shareable generator tools that go viral - name generators, quiz makers, avatar creators, personality tests, and calcul... |
| 2998 | `viral-video-teardown-remake` | "Install and use the official Viral Video Remake package, pinned by digest, for paid hosted work on the Beatra service." |
| 2999 | `visibility-index-calculator` | "Visibility Index Calculator. Use when working with keyword weights and rank-to-CTR mapping with rankings." |
| 3000 | `visual-emotion-engineer` | "Create a visual direction brief for color, typography, imagery, and hierarchy when design must support a defined emotion, culture, and a... |
| 3001 | `vitest-skill` | 'Generates Vitest tests in JavaScript/TypeScript with Vite-native speed. Jest-compatible API with ESM support and HMR. Use when user ment... |
| 3002 | `vizcom` | AI-powered product design tool for transforming sketches into full-fidelity 3D renders. |
| 3003 | `vllm-server` | Deploy and manage vLLM for high-throughput LLM inference. Configure continuous batching, tensor parallelism, quantization, and OpenAI-com... |
| 3004 | `vmware-vcenter-attack` | VMware vSphere / vCenter Server external attack matrix |
| 3005 | `voice-agents` | Voice agents represent the frontier of AI interaction - humans speaking naturally with AI systems. |
| 3006 | `voice-ai-development` | Expert in building voice AI applications - from real-time voice agents to voice-enabled apps. Covers OpenAI Realtime API, Vapi for voice ... |
| 3007 | `voice-ai-engine-development` | "Build real-time conversational AI voice engines using async worker pipelines, streaming transcription, LLM agents, and TTS synthesis wit... |
| 3008 | `voice-cloning-studio` | "Install and use the official AI Voice Cloning package, pinned by digest, for paid hosted work on the Beatra service." |
| 3009 | `voiceover-narration-studio` | "Install and use the official AI Voiceover Generator package, pinned by digest, for paid hosted work on the Beatra service." |
| 3010 | `vpn-setup` | Configure WireGuard, OpenVPN, and cloud VPNs. Implement secure remote access and site-to-site connectivity. Use when setting up secure ne... |
| 3011 | `vps-server-management` | "Manage authorized VPS hosts and server-side agents through cautious SSH and operations workflows." |
| 3012 | `vs-and-alternatives` | Draft evidence-backed comparison and alternative pages using sourced switching reasons, pricing scenarios and migration details. |
| 3013 | `vscode-extension-guide-en` | "Guide for VS Code extension development from scaffolding to Marketplace publication" |
| 3014 | `vulnerability-scanner` | "Advanced vulnerability analysis principles. OWASP 2025, Supply Chain Security, attack surface mapping, risk prioritization." |
| 3015 | `vulnerability-scanning` | Scan systems and dependencies for CVEs and security vulnerabilities. |
| 3016 | `waf-setup` | Deploy and tune Web Application Firewalls. Configure rules for OWASP Top 10 protection. Use when protecting web applications from common ... |
| 3017 | `warehouse` | "Plan and review read-only data warehouse analysis with explicit scope, privacy, provenance, and validation checks." |
| 3018 | `warp-delegate` | Delegate coding tasks to the Warp Agent CLI (`oz`) only when the user explicitly requests it, while the orchestrator retains review and l... |
| 3019 | `warren-buffett` | "Agente que simula Warren Buffett — o maior investidor do seculo XX e XXI, historicamente associado a Berkshire Hathaway, discipulo de Be... |
| 3020 | `watch-igaming` | "Reviews a video link or local screen recording from transcript and scene-change frames matched by timecode, then returns a review, QA ta... |
| 3021 | `wcag-audit-patterns` | "Comprehensive guide to auditing web content against WCAG 2.2 guidelines with actionable remediation strategies." |
| 3022 | `weather-data-lifecycle-management` | "Manage ownership, retention, and cleanup of downloaded weather data across one-shot jobs, interactive viewers, caches, failures, and can... |
| 3023 | `weather-data-reproducibility` | "Record and verify provenance manifests for weather-data inputs and derived artifacts, including object identity, selections, software ve... |
| 3024 | `weather-model-data-fetching` | "Retrieve numerical weather prediction data from public AWS S3 and HTTP archives using GRIB2 inventories, byte ranges, Herbie, provider f... |
| 3025 | `weather-model-run-discovery` | "Resolve the newest complete numerical weather prediction cycle and forecast objects across provider mirrors without downloading full pay... |
| 3026 | `weather-observation-fetching` | "Retrieve surface and upper-air weather observations from authoritative APIs and archives with station identity, time, units, and quality... |
| 3027 | `weather-pipeline-performance-diagnosis` | "Diagnose slow weather-data workflows by measuring discovery, transfer, parsing, scientific processing, and rendering separately before c... |
| 3028 | `weaviate` | "Search, query, inspect, create, and import data into Weaviate vector database collections using bundled adapted scripts and references." |
| 3029 | `weaviate-cookbooks` | "Build Weaviate AI apps from official cookbook blueprints for RAG, agentic RAG, data exploration, multimodal PDF search, async clients, a... |
| 3030 | `web-access` | "Use Treg for public web or platform data only when existing search, browser and connected tools cannot cover the task, with explicit cos... |
| 3031 | `web-artifacts-builder` | "Create React frontend artifacts and bundle a reviewed project into a shareable HTML file." |
| 3032 | `web-design-guidelines` | "Review files for compliance with Web Interface Guidelines." |
| 3033 | `web-design-system` | "Choose a design direction for a website from real sites and write it down as a DESIGN.md: colors with roles, type, spacing, radius, shad... |
| 3034 | `web-media-getter` | "One query across free image / video / GIF APIs (stock + historical/archival + GIF engines), returning normalized, license-tagged results... |
| 3035 | `web-performance-optimization` | "Optimize website and web application performance including loading speed, Core Web Vitals, bundle size, caching strategies, and runtime ... |
| 3036 | `web-project-brainstorming` | Masterclass framework for brainstorming web development projects and page designs. Outlines structural phases for concept, UX flow, styli... |
| 3037 | `web-review` | "Review a website or landing page and list what to fix, most important first: message, generic AI look, consistency, copy, mobile, access... |
| 3038 | `web-scraper` | Web scraping inteligente multi-estrategia. Extrai dados estruturados de paginas web (tabelas, listas, precos). Paginacao, monitoramento e... |
| 3039 | `web-security-testing` | "Web application security testing workflow for OWASP Top 10 vulnerabilities including injection, XSS, authentication flaws, and access co... |
| 3040 | `web2-recon` | Web2 recon pipeline |
| 3041 | `web3-audit` | Smart contract security audit |
| 3042 | `web3-rate-limiting-circuit-breaker` | 'On-chain and relayer rate-limiting circuit breaker register: throughput thresholds, emergency pause triggers, and multi-sig recovery.' |
| 3043 | `web3-testing` | "Master comprehensive testing strategies for smart contracts using Hardhat, Foundry, and advanced testing patterns." |
| 3044 | `web3-transaction-relayer-pool` | 'Gasless transaction relayer node pool register: fee sponsorship limits, nonce synchronization, and balance replenishment alerts.' |
| 3045 | `webapp-testing` | "To test local web applications, write native Python Playwright scripts." |
| 3046 | `webdriverio-skill` | 'Generates WebdriverIO (WDIO) automation tests in JavaScript or TypeScript. Supports local and TestMu AI cloud. Use when user mentions "W... |
| 3047 | `webflow-automation` | "Automate Webflow CMS collections, site publishing, page management, asset uploads, and ecommerce orders via Rube MCP (Composio). Always ... |
| 3048 | `webly` | "Publish a website or share files at a live URL in seconds with no account, then let the person claim it, edit it over Webly's MCP server... |
| 3049 | `wechat-cover-maker` | "Install and use the official WeChat Article Cover package, pinned by digest, for paid hosted work on the Beatra service." |
| 3050 | `wechat-official-account-strategist` | "Grow WeChat Official Accounts (微信公众号) with high-conversion content strategy, title formulas, article architecture, and Mini-Program inte... |
| 3051 | `weightloss-analyzer` | 分析减肥数据、计算代谢率、追踪能量缺口、管理减肥阶段 |
| 3052 | `wellally-tech` | "Integrate multiple digital health data sources, connect to [WellAlly.tech](https://www.wellally.tech/) knowledge base, providing data im... |
| 3053 | `wgm` | "Turns a rough request into working software via a governed build loop: align first, plan, then iterate one task at a time with determini... |
| 3054 | `what-could-break` | "Find what a change breaks outside its own diff, then prove the one fact that makes it safe by running real code. Use before any multi-fi... |
| 3055 | `whatsapp-automation` | "Automate WhatsApp Business tasks via Rube MCP (Composio): send messages, manage templates, upload media, and handle contacts. Always sea... |
| 3056 | `whatsapp-cloud-api` | Integracao com WhatsApp Business Cloud API (Meta). Mensagens, templates, webhooks HMAC-SHA256, automacao de atendimento. Boilerplates Nod... |
| 3057 | `why-did-this-post-flop` | "Diagnose why one Twitter or LinkedIn post underperformed: not seen, seen and skipped, or read and ignored. Use when someone asks why a p... |
| 3058 | `wifi-wireless` | "Authorized wireless security assessment: Wi-Fi capture, WPA handshake analysis, rogue AP detection research, and lab-only deauthenticati... |
| 3059 | `wiki-architect` | "You are a documentation architect that produces structured wiki catalogues and onboarding guides from codebases." |
| 3060 | `wiki-builder` | "Create and maintain reusable research wikis with source provenance, configurable structure, and local markdown outputs." |
| 3061 | `wiki-changelog` | "Generate structured changelogs from git history. Use when user asks \"what changed recently\", \"generate a changelog\", \"summarize com... |
| 3062 | `wiki-onboarding` | "Generate two complementary onboarding documents that together give any engineer — from newcomer to principal — a complete understanding ... |
| 3063 | `wiki-page-writer` | "You are a senior documentation engineer that generates comprehensive technical documentation pages with evidence-based depth." |
| 3064 | `wiki-qa` | "Answer repository questions grounded entirely in source code evidence. Use when user asks a question about the codebase, user wants to u... |
| 3065 | `wiki-researcher` | "You are an expert software engineer and systems analyst. Use when user asks \"how does X work\" with expectation of depth, user wants to... |
| 3066 | `wiki-vitepress` | "Transform generated wiki Markdown files into a polished VitePress static site with dark theme and interactive Mermaid diagrams. Use when... |
| 3067 | `wiki-yylo` | Use YYLO Ledger wiki Records as durable project knowledge. Search before creating, classify information correctly, and make revision-safe... |
| 3068 | `windows-ad` | "Authorized Active Directory and Windows identity attacks: Kerberos abuse, AD CS escalation, BloodHound path analysis, NTLM relay, and do... |
| 3069 | `windows-agent-shell` | 'A coding agent on Windows: Git Bash path rewriting, PowerShell quoting and encoding, CRLF. Use when output comes back garbled, or it wor... |
| 3070 | `windows-hardening` | Harden Windows servers per security baselines and CIS benchmarks. Configure Group Policy, Windows Defender, and security features. Use wh... |
| 3071 | `windows-privilege-escalation` | "Provide systematic methodologies for discovering and exploiting privilege escalation vulnerabilities on Windows systems during penetrati... |
| 3072 | `windows-server` | Administer Windows Server systems. Manage IIS, Active Directory, and PowerShell automation. Use when administering Windows infrastructure. |
| 3073 | `windows-shell-reliability` | "Reliable command execution on Windows: paths, encoding, and common binary pitfalls." |
| 3074 | `wireshark-analysis` | "Execute comprehensive network traffic analysis using Wireshark to capture, filter, and examine network packets for security investigatio... |
| 3075 | `wjttc-builder` | "PLAN and GENERATE WJTTC (Championship-Grade) test suites for any project. Analyzes the codebase, classifies components across the WJTTC ... |
| 3076 | `wjttc-tester` | "F1-inspired test EXECUTOR + reporter. Runs a test plan, finds and reproduces bugs, audits suite signal integrity, then files a WJTTC rep... |
| 3077 | `woo-guard` | "Review generated or changed WooCommerce extensions, payment and shipping integrations, checkout customizations, and order or product log... |
| 3078 | `word-count-structure-checker` | "Word Count & Structure Checker. Use when working with text or structured article." |
| 3079 | `wordpress` | "WordPress development workflow covering theme development, plugin creation, WooCommerce integration, performance optimization, and secur... |
| 3080 | `wordpress-centric-high-seo-optimized-blogwriting-skill` | "Generate clean, human-sounding, SEO-optimized WordPress blog posts with optional Yoast metadata, JSON-LD schema markup, and image SEO pl... |
| 3081 | `wordpress-penetration-testing` | "Assess WordPress installations for common vulnerabilities and installed core/plugin REST permission boundaries." |
| 3082 | `wordpress-plugin-development` | "WordPress plugin development workflow covering plugin architecture, hooks, admin interfaces, REST API, security best practices, and Word... |
| 3083 | `wordpress-theme-development` | "WordPress theme development workflow covering theme architecture, template hierarchy, custom post types, block editor support, responsiv... |
| 3084 | `wordpress-woocommerce-development` | "WooCommerce store development workflow covering store setup, payment integration, shipping configuration, customization, and WordPress 7... |
| 3085 | `work-humanizer` | '''Make this sound human'', ''less AI'': edit AI-sounding work writing so a careful person could have written it, without changing what i... |
| 3086 | `workflow-automation` | Workflow automation is the infrastructure that makes AI agents reliable. Without durable execution, a network hiccup during a 10-step pay... |
| 3087 | `workflow-orchestration-patterns` | "Master workflow orchestration architecture with Temporal, covering fundamental design decisions, resilience patterns, and best practices... |
| 3088 | `workflow-patterns` | Use this skill when implementing tasks according to Conductor's TDD workflow, handling phase checkpoints, managing git commits for tasks,... |
| 3089 | `workflow-yylo` | Create and maintain validated YYLO Ledger workflow Records while keeping storage, execution, and run evidence as separate explicit bounda... |
| 3090 | `workorai` | "WorkorAI talent-marketplace skill: candidates search jobs and manage applications; employers run the job lifecycle and get ranked candid... |
| 3091 | `worktable-mcp` | "Find, cite and update Docs, Records, HTML Docs, annotations and threads in a Worktable workspace through Worktable's MCP server. Use whe... |
| 3092 | `wp-guard` | "Review generated or changed WordPress plugins, themes, and blocks for security, internationalization, performance, and API correctness." |
| 3093 | `wp-site-health-auditor` | "Turns a WordPress Site Health report into a risk-tiered, backup-first fix plan with exact WP-CLI/PHP snippets. Use for site health, reco... |
| 3094 | `wrike-automation` | "Automate Wrike project management via Rube MCP (Composio): create tasks/folders, manage projects, assign work, and track progress. Alway... |
| 3095 | `write-design-md` | "Write or update a project's DESIGN.md from the colors, type, spacing and components it really uses, with rules agents follow so new scre... |
| 3096 | `write-in-my-voice` | "Draft a Twitter or LinkedIn post that sounds like the person asking, from posts they already wrote. Use when someone asks for a post or ... |
| 3097 | `write-kaggle-benchmarks` | Write, push, run, publish, and manage Kaggle Benchmark tasks using the kaggle CLI and the kaggle-benchmarks Python SDK. Use when the user... |
| 3098 | `write-swift` | "Write and review modern Swift with value types, concurrency, protocols, API design, memory management, and testing." |
| 3099 | `writer` | "Document creation, format conversion (ODT/DOCX/PDF), mail merge, and automation with LibreOffice Writer." |
| 3100 | `writing-great-skills` | Reference for writing and editing skills well — the vocabulary and principles that make a skill predictable. |
| 3101 | `writing-guidelines` | Curated upstream guidance for Writing Guidelines; use when the workflow matches the user goal. |
| 3102 | `writing-plans` | Use when you have a spec or requirements for a multi-step task, before touching code |
| 3103 | `writing-skills` | Use when creating new skills, editing existing skills, or verifying skills work before deployment |
| 3104 | `x-article-publisher-skill` | "Publish articles to X/Twitter" |
| 3105 | `x-twitter-scraper` | "Use Xquik for X data workflows: tweet search, user lookup, follower export, media downloads, monitors, webhooks, REST API, MCP, SDK setu... |
| 3106 | `x402-express-wrapper` | Wrapper oficial de M2MCent (Node.js) para inyectar muros de pago x402 en APIs o servidores Model Context Protocol (MCP). Usar al construi... |
| 3107 | `xiaohongshu-content-strategist` | "Create viral Xiaohongshu (小红书) content with platform-native strategy, save-rate optimization, trending formats, and search SEO for China... |
| 3108 | `xml-sitemap-visualizer` | "XML Sitemap Visualizer. Use when working with XML sitemap or sitemap index." |
| 3109 | `xss-html-injection` | "Execute comprehensive client-side injection vulnerability assessments on web applications to identify XSS and HTML injection flaws, demo... |
| 3110 | `xvary-stock-research` | "Thesis-driven equity analysis from public SEC EDGAR and market data; /analyze, /score, /compare workflows with bundled Python tools (Cla... |
| 3111 | `yann-lecun` | "Persona fictícia inspirada em temas públicos associados a Yann LeCun, para diálogo criativo sobre redes neurais e aprendizagem preditiva." |
| 3112 | `yann-lecun-debate` | "Sub-skill de debates e posições de Yann LeCun. Cobre críticas técnicas detalhadas aos LLMs, rivalidades intelectuais (LeCun vs Hinton, S... |
| 3113 | `yann-lecun-filosofia` | "Sub-skill filosófica e pedagógica de Yann LeCun." |
| 3114 | `yann-lecun-tecnico` | "Sub-skill técnica de Yann LeCun. Cobre CNNs, LeNet, backpropagation, JEPA (I-JEPA, V-JEPA, MC-JEPA), AMI (Advanced Machinery of Intellig... |
| 3115 | `yao-meta-skill` | Create, refactor, evaluate, and package agent skills from workflows, prompts, transcripts, docs, or notes. Use for skill creation, reusab... |
| 3116 | `yes-md` | "6-layer AI governance: safety gates, evidence-based debugging, anti-slack detection, and machine-enforced hooks. Makes AI safe, thorough... |
| 3117 | `yield-intelligence` | Passive income portfolio analysis — activate when user asks about dividend yields, Treasury rates, REIT income, monthly passive income go... |
| 3118 | `youtube-automation` | "Automate YouTube tasks via Rube MCP (Composio): upload videos, manage playlists, search content, get analytics, and handle comments. Alw... |
| 3119 | `youtube-full` | "Fetch YouTube transcripts, search videos, browse channels, and extract playlists via TranscriptAPI — no yt-dlp, no Google API key, works... |
| 3120 | `youtube-notetaker` | "Turn YouTube talks into local study notes with slides, transcripts, editable annotations, and a markdown-backed viewer." |
| 3121 | `youtube-seo` | Use an authorized recording or transcript to draft YouTube titles, timestamped chapters, launch posts and verified video structured data. |
| 3122 | `youtube-seo-optimizer` | Generate complete YouTube & podcast SEO packages with live-researched keywords — titles, descriptions, tags, hashtags, chapters, and audi... |
| 3123 | `youtube-summarizer` | "Extract transcripts from YouTube videos and generate comprehensive, detailed summaries using intelligent analysis frameworks" |
| 3124 | `youtube-transcript` | "Fetch YouTube transcripts through DeepAPI or local fallback tooling and save clean text output." |
| 3125 | `youtube-transcript-skills` | "Fetch YouTube video transcripts, search videos/channels, browse channels, and extract playlists via the getyoutubetranscript.com API; ve... |
| 3126 | `zambo` | "Connect an agent to Zambo: 153 tools behind one remote MCP endpoint, cross-AI handover, memory, and a verifiable AER-1 receipt for every... |
| 3127 | `zapier-make-patterns` | No-code automation democratizes workflow building. Zapier and Make (formerly Integromat) let non-developers automate business processes w... |
| 3128 | `zcode-delegate` | Delegate coding tasks to the Z.AI ZCode CLI only when the user explicitly requests it, while the orchestrator retains review and landing ... |
| 3129 | `zendesk-automation` | "Automate Zendesk tasks via Rube MCP (Composio): tickets, users, organizations, replies. Always search tools first for current schemas." |
| 3130 | `zero-trust` | Implement zero-trust network architecture. Configure identity-based access, micro-segmentation, and continuous verification. Use when imp... |
| 3131 | `zeroize-audit` | "Detects missing zeroization of sensitive data in source code and identifies zeroization removed by compiler optimizations, with assembly... |
| 3132 | `zhongcao-cover-maker` | "Install and use the official Xiaohongshu Cover Maker package, pinned by digest, for paid hosted work on the Beatra service." |
| 3133 | `zhongcao-note-copywriter` | "Install and use the official Xiaohongshu Copywriter package, pinned by digest, for paid hosted work on the Beatra service." |
| 3134 | `zipai-optimizer` | "Ultra-dense token optimizer skill for prompt caching, log pruning, AST-based inspection, and minified JSON payloads." |
| 3135 | `zk-proof-verification-pipeline` | 'Zero-knowledge cryptographic verification pipeline register: proving system, circuit verification keys, public inputs, and gas costs.' |
| 3136 | `zod-validation-expert` | "Expert in Zod — TypeScript-first schema validation. Covers parsing, custom errors, refinements, type inference, and integration with Rea... |
| 3137 | `zoho-crm-automation` | "Automate Zoho CRM tasks via Rube MCP (Composio): create/update records, search contacts, manage leads, and convert leads. Always search ... |
| 3138 | `zoom-automation` | "Automate Zoom meeting creation, management, recordings, webinars, and participant tracking via Rube MCP (Composio). Always search tools ... |
| 3139 | `zustand-store-ts` | "Create Zustand stores following established patterns with proper TypeScript types and middleware." |
