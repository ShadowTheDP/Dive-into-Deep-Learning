# Dive into Deep Learning

## Purpose

This repository is for learning D2L concepts and practicing deep learning
knowledge in small, runnable experiments.

The project is a personal D2L learning workspace, not a production ML codebase.
Its main job is to help you study one chapter at a time while keeping the work
organized enough that a human or AI agent can continue it correctly.

## What "Correct Work" Means Here

Human collaborators and AI agents should treat this repo as a study-and-lab
workspace.

Correct ways to work on this project:

- Study D2L chapter by chapter.
- Give each chapter a dedicated chapter path.
- At minimum, each chapter should have one clearly named source file.
- If a chapter grows beyond one file, place it in a dedicated folder such as
  `ch02_preliminaries/`.
- Put generated artifacts in `output/`.
- Prefer readable practice code over premature abstraction.
- Preserve the repo as a learning record, not just a dump of results.

Avoid:

- Mixing generated outputs with source files.
- Writing directly outside this repository when working on D2L tasks.
- Hiding core logic only inside notebooks or temporary scratch files.
- Changing the meaning of an existing chapter folder without updating this
  README.
- Turning this repo into a generic utilities repo unrelated to D2L study.

## Structure Rules

Use these structure rules unless there is a strong reason to do otherwise:

- One chapter, one dedicated chapter path.
- Preferred naming pattern for chapter folders:
  - `ch01_intro/`
  - `ch02_preliminaries/`
  - `ch03_linear-networks/`
- Inside a chapter path, keep at least one main chapter file with a clear name.
- If you introduce notes or notebooks later, keep them inside the relevant
  chapter folder or a clearly named `notebooks/` directory.
- Keep all generated files under `output/`, not beside the source file that
  created them.

## Environment

Current expected environment:

- Conda environment name: `d2l_ai`
- Python 3.9 is the currently documented baseline in this repo
- Main libraries: `torch`, `numpy`, `jax`, `d2l`

Activate:

```powershell
conda activate d2l_ai
```

Practical rule:

- Prefer using the existing `d2l_ai` Conda environment first.
- If the environment changes later, update this README or add an explicit
  environment manifest.

Note:
This repo currently does not include a full `requirements.txt` or
`environment.yml`, so the existing environment is still the source of truth.

## First Useful Commands

Verify the environment:

```powershell
python verify_env.py
```

Run the chapter 2 data manipulation example:

```powershell
python ch02_preliminaries/data_manipulation.py
```

Run the chapter 2 playground:

```powershell
python ch02_preliminaries/playground.py
```

Run the tensor lab:

```powershell
python tensor_lab.py
```

## Inputs

Typical inputs for this repo are:

- D2L chapter exercise scripts
- Small experiment files
- Notes that support D2L learning
- Optional notebooks for chapter-specific exploration

When starting a new chapter, create a clearly named chapter path first, then
place the chapter files inside it.

## Outputs

Put generated files under:

```text
output/
```

If a chapter becomes a mini-project, prefer:

```text
output/ch02_preliminaries/
output/ch03_linear-networks/
```

Generated output should stay local unless there is a clear reason to track it.

## File Map

Top-level files and folders:

- `.gitignore`
  - Ignore rules for local environments, temp data, outputs, and IDE files.
- `README.md`
  - This project working guide and AI-agent rule source of truth.
- `Changing Description.txt`
  - The single official project change log. Update it after completed work,
    especially before pushing to GitHub.
- `tensor_lab.py`
  - Quick tensor or accelerator sanity-check script.
- `verify_env.py`
  - Environment verification script for `torch`, `numpy`, `jax`, and `d2l`.
- `ch02_preliminaries/`
  - Current chapter-specific practice folder for D2L chapter 2 work.
- `output/`
  - Generated artifacts for this repo.

Files inside `ch02_preliminaries/`:

- `data_manipulation.py`
  - Runnable practice script for tensor and data manipulation concepts.
- `playground.py`
  - Interactive-style sandbox script for tensor shapes and reduction behavior.

## Working Rules for AI Agents

If you are an AI agent working in this repo:

1. Read this README first.
2. Treat this README as the single source of truth for project rules.
3. Stay inside `Project/Dive-into-Deep-Learning/` unless a human explicitly
   asks you to touch something else.
4. Preserve the chapter-oriented structure.
5. Create or update one dedicated chapter path per D2L chapter.
6. Ensure each chapter has at least one clearly named source file.
7. Put outputs in `output/`, not beside source scripts.
8. Prefer repo-relative paths in scripts, notes, and instructions.
9. Do not add large datasets, checkpoints, or model artifacts casually.
10. Do not silently replace the learning style of the repo with a production
   architecture.
11. Update `Changing Description.txt` after meaningful completed work,
    especially before push.
12. If you change the workflow or structure, update this README in the same
    task.

## Before Push Checklist

Before pushing to GitHub, check:

- The code you changed still runs.
- Generated files are in `output/`, not mixed into source folders.
- No local environment folders were added accidentally.
- No large local artifacts were staged by mistake.
- `Changing Description.txt` was updated to reflect the completed work if the
  change is worth preserving in project history.
- README updates were included if the workflow or structure changed.
- You did not leave behind scratch-only files with unclear names.

## Current Gaps

- No reproducible environment manifest is checked in yet.
- Some existing console text appears to have encoding issues and may need a
  later UTF-8 cleanup pass.
- The current repo has chapter 2 practice files, but future chapters still need
  a consistent expansion pattern as the learning work grows.
