# cOde(n) Continuation Notes

Date saved: 2026-05-30

This file is a handoff note for continuing work on cOde(n) without needing the full chat history.

## Project Purpose

cOde(n) is a Python and Pygame algorithm-learning game inspired by the workflow of writing scripts in an editor, running them, and seeing the code operate on a simple 2D grid/list visualization. Players solve challenges by editing files in `solutions/`, then running visual replays that count real operations and estimate complexity classes.

The backstory is grounded and pure: the player chooses the name of a Computer Science BSc student taking Algorithms and Data Structures. The story focuses on lectures, lab sheets, careful debugging, and learning complexity through measured Python operations.

## Workspace

- Root: `c:\dawei7\code_n`
- Venv: `.venv`
- Python used so far: 3.12.8
- Pygame used so far: 2.6.1
- Internal Python package/import name: `code_n`
- Packaged executable: `dist/cOde(n)/cOde(n).exe`
- Source of truth is the root source tree, not files inside `dist/`.

If the current editor is open on `dist/cOde(n)/solutions/*.py` or the old `dist/AlgoMaster/solutions/*.py`, remember that this is a packaged copy. The normal development solution files are in root `solutions/`.

## Common Commands

Run the navigator from source:

```bash
c:/dawei7/code_n/.venv/Scripts/python.exe main.py nav
```

Run a saved challenge solution:

```bash
c:/dawei7/code_n/.venv/Scripts/python.exe run_challenge.py intro_01 --no-animate --n 8 --seed 1
```

Run with Pygame graphics:

```bash
c:/dawei7/code_n/.venv/Scripts/python.exe run_challenge.py intro_01 --pygame
```

Run with a specific visual speed:

```bash
c:/dawei7/code_n/.venv/Scripts/python.exe run_challenge.py intro_01 --pygame --speed step
c:/dawei7/code_n/.venv/Scripts/python.exe run_challenge.py intro_01 --pygame --speed very-slow
c:/dawei7/code_n/.venv/Scripts/python.exe run_challenge.py intro_01 --pygame --speed fast
```

Compile-check edited Python files:

```bash
c:/dawei7/code_n/.venv/Scripts/python.exe -m py_compile code_n/pygame_renderer.py code_n/execution_trace.py run_challenge.py main.py
```

Rebuild the portable Windows app:

```bash
powershell -NoProfile -Command "Get-Process 'cOde(n)','AlgoMaster' -ErrorAction SilentlyContinue | Stop-Process -Force; Start-Sleep -Milliseconds 500; if (Test-Path 'dist/cOde(n)') { Remove-Item 'dist/cOde(n)' -Recurse -Force }; if (Test-Path 'dist/AlgoMaster') { Remove-Item 'dist/AlgoMaster' -Recurse -Force }"
c:/dawei7/code_n/.venv/Scripts/python.exe build_windows_exe.py
```

Smoke-test rebuilt exe:

```bash
"dist/cOde(n)/cOde(n).exe" --run-challenge intro_01 --no-animate --n 8 --seed 1
```

## Current Implemented Features

- Challenge tree with locked/unlocked progression.
- Player-chosen protagonist name stored in `progress.json` as `player_name`.
- Grounded Computer Science BSc Algorithms and Data Structures backstory in `code_n/branding.py`, README, CLI, and navigator.
- Root `solutions/` folder where player scripts are created and loaded.
- Pygame challenge navigator.
- Navigator buttons ordered `Explore`, `Run`, and `Open Script`.
- Explore view shows the task description, generated sample visualization, setup summary, and example solution pattern.
- Challenge descriptions are visible in both Explore and Run/debugger views.
- VS Code opening through `code` or `code.cmd`, with Notepad fallback.
- Packaged Windows distribution through PyInstaller.
- Dynamic import support for packaged player scripts through hidden imports and `play.py` bundling.
- Operation counting for reads, writes, compares, swaps, calls.
- Complexity classification based on operation count, not wall-clock speed.
- Pygame visual replay of tracked list/grid operations.
- Side panel showing operation counts, current operation, locals from `solve()`, and return value.
- Live list mutation visualization for swap, write, append, insert, and pop.
- Replay controls: clickable Play/Pause, Next, Replay, Manual/Auto, Stop, Slower, and Faster buttons plus keyboard shortcuts.
- Speed presets: `step`, `crawl`, `very-slow`, `slow`, `normal`, `fast`, `turbo`, `instant`.
- Clickable cell watchpoints: clicking a visible list/grid cell toggles a watchpoint; replay pauses when an operation touches it.
- Source-line replay breakpoints using inline comments in player scripts.

## Pygame Debugger Controls

| Control                                      | Action                                      |
| -------------------------------------------- | ------------------------------------------- |
| `Space`, `Enter`, `Right Arrow` in step mode | Execute exactly one operation               |
| `Space` or `P` in normal mode                | Pause or resume replay                      |
| `Enter` or `Right Arrow` in normal mode      | Execute one operation and pause             |
| `M`                                          | Toggle step-by-step mode                    |
| `S`                                          | Stop at the current step                    |
| `R`                                          | Replay from the beginning                   |
| `+` / `-`                                    | Adjust replay speed                         |
| Side-panel buttons                           | Play/pause, step, replay, stop, mode, speed |
| Click a visible cell                         | Toggle a watchpoint for that coordinate     |
| `Esc` / `Q`                                  | Close the graphics window                   |

Inline source breakpoint marker:

```python
# code_n: breakpoint
```

Put that comment on a line in a solution script. The replay will pause when the execution trace reaches that recorded line. VS Code red-dot breakpoints are not directly read by the packaged game because they belong to the VS Code debugger session, not the running Python process.

## Important Files

- `code_n/pygame_renderer.py`: Pygame replay/debugger, speed picker, step mode, watchpoints, visual operations.
- `code_n/execution_trace.py`: `sys.settrace` capture of player locals, return values, and inline source breakpoints.
- `code_n/navigation.py`: Pygame challenge navigator, run/open buttons, packaged/source process launch, log output.
- `code_n/challenge.py`: Challenge run lifecycle; builds `VisualRunResult` and invokes the renderer.
- `code_n/tracked.py`: Player-facing tracked data structures and operation logging.
- `code_n/counter.py`: Operation records, stats, complexity classification, thresholds.
- `code_n/solutions.py`: Frozen-aware path handling for `solutions/`.
- `code_n/progress.py`: Frozen-aware progress path.
- `run_challenge.py`: CLI challenge runner, `--pygame`, `--speed`, solution loading.
- `play.py`: Packaged launcher and `--run-challenge` bridge.
- `build_windows_exe.py`: PyInstaller build script and hidden imports.
- `README.md`: User-facing docs. It was changed by the user or a formatter after the previous turn, so read it before editing.

## Recent Fixes And Lessons

- Fixed packaged navigator crash caused by `ChallengeNavigator` using `self.GRID_LINE` before the constant existed.
- Added `GRID_LINE = (64, 73, 89)` in `code_n/navigation.py`.
- Avoid using `os.startfile` on `.py` files as an editor fallback because it can execute scripts and open/close a console unexpectedly.
- The Pygame side panel reserves a footer for pass/fail messages; keep variable and return-value text clipped above it to avoid overlap.
- The navigator details panel reserves bottom zones for Run/Open buttons and controls; keep description text clipped above those zones to avoid overlap.
- Packaged Windows output can use cp1252; keep challenge completion messages ASCII and let `play.py` replace unsupported stdout/stderr characters to avoid PyInstaller error dialogs after closing Pygame.
- In `--pygame` runs, missing scripts, scripts without `solve`, load errors, solution exceptions, and verifier exceptions are shown as failed Pygame result panels instead of PyInstaller tracebacks. Non-Pygame runs still raise tracebacks for debugging.
- Rebuilding the packaged app on Windows may fail if an old `cOde(n).exe` or legacy `AlgoMaster.exe` is still running. Stop it before deleting `dist/cOde(n)`.
- PyInstaller needs hidden imports for dynamically loaded player scripts, especially `code_n.api`, `code_n.counter`, `code_n.execution_trace`, `code_n.grid`, `code_n.pygame_renderer`, and `code_n.tracked`.

## Last Verified State

After renaming the internal package to `code_n`:

```text
all source Python files py_compile ok
source intro_01 challenge run ok
source sort_01 example player script run ok
code_n imports and the old package name is no longer importable
no old lowercase package text refs in source/docs/build spec/dist text files
PyInstaller rebuild ok
dist/cOde(n)/cOde(n).exe --run-challenge intro_01 --no-animate --n 8 --seed 1 ok
```

## Potential Next Work

- Add a small watchpoint list panel with remove buttons.
- Add per-line source display next to variables so breakpoints feel closer to a real debugger.
- Add more challenges for sorting, searching, graphs, and dynamic programming.
- Add automated Pygame screenshot tests if browser/playwright or screenshot tooling is available.
- Consider a lightweight in-game editor only if the original requirement changes; the current design intentionally keeps players writing scripts in their own editor.
