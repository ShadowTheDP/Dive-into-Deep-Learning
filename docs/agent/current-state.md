# Current State

## Objective

Stabilize the repo as a low-friction D2L learning workspace with a clear agent
entry path and low context overhead.

## Current Structure

- `README.md` remains the durable project rules document.
- `AGENTS.md` now handles agent routing and plugin selection.
- `ch02_preliminaries/` is the active chapter work area.
- `output/` remains the local generated-artifact location.

## Current Decisions

- Do not perform a premature directory migration yet.
- Keep one chapter path per chapter.
- Keep validation script entrypoints at the repo root for now.

## Next Likely Improvements

- Add new chapter folders as D2L work expands.
- Introduce a deeper structure only when multiple chapter roots make the repo
  harder to navigate.
- Keep `Changing Description.txt` as human-readable history, not the primary
  agent handoff document.
