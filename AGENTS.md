# Dive-into-Deep-Learning AGENTS

## Read Order

1. `README.md`
2. `docs/agent/current-state.md`
3. `Changing Description.txt` only when historical detail is needed
4. The target chapter file or folder

## Scope

- Stay inside `Project/Dive-into-Deep-Learning/` unless explicitly asked to
  pull material from `Project-source/`.
- Preserve the chapter-oriented learning structure.
- Prefer small runnable scripts over framework-heavy abstractions.

## Default Ignore Paths

- `output/`
- `__pycache__/`
- environment caches or local notebooks not under active work

## Preferred Plugins

- `Everything MCP` for file discovery
- `QMD` for local notes and handoff docs
- `GitHub MCP` for repo history or remote review
- `Context7` for library docs

## Validation

Use the narrowest command that proves the task:

- `python verify_env.py`
- `python tensor_lab.py`
- `python ch02_preliminaries/data_manipulation.py`
- task-specific chapter commands as needed

## Structure Direction

- Keep the current flat chapter-root approach while the repo is still small.
- Do not introduce a larger `chapters/` migration until there is a real need
  from additional chapter growth.
- Keep generated artifacts in `output/`.
