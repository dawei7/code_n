# Legacy cOde(n) code (Pygame era)

This directory contains the old command-line and Pygame-based launcher
that cOde(n) shipped with before the 2026-06-07 web rebuild.

The rebuild moved cOde(n) to a server-client architecture:

- **Backend:** FastAPI (in `../server/`) wrapping the engine
- **Frontend:** React + Tailwind (in `../web/`)
- **Desktop wrapper:** Electron (in `../electron/`)

The Python engine itself (`../code_n/`, `../challenges/`,
`../optimal_solutions/`) is **untouched** by the rebuild. It is the
asset that the new web frontend and Electron app both talk to.

## Files in this directory

| File | Origin | Notes |
| --- | --- | --- |
| `main.py` | repo root | Old CLI menu (challenge tree, subcommands) |
| `run_challenge.py` | repo root | Old CLI runner (`--pygame`, `--speed`, `--list`, `--diff`) |
| `play.py` | repo root | Old double-click launcher used by the packaged exe |
| `build_windows_exe.py` | repo root | Old PyInstaller build for `cOde(n).exe` |

## What is NOT in this directory (still in place)

- `code_n/pygame_renderer.py` — the Pygame debugger/replay window
- `code_n/navigation.py` — the Pygame challenge navigator (the "hub")
- `code_n/renderer.py` — the terminal ANSI renderer

These three files are **still in their original location** because the
existing test suite (`tests/test_pygame_renderer_*.py` and
`tests/test_renderer_*.py`) imports them, and we want the 142-test
engine baseline to stay green through the rebuild.

They have a `# DEPRECATED: see legacy/README.md` comment at the top.
The follow-up sprint that deletes the Pygame tests can also move
the renderer sources here and remove the deprecation comment.

## How to run the legacy build (still works)

The old build is still functional as a fallback:

```bash
cd "c:/dawei7/code_n"
.venv/Scripts/python.exe main.py                                          # CLI menu
.venv/Scripts/python.exe run_challenge.py --pygame intro_01 --n 8 --seed 1
.venv/Scripts/python.exe build_windows_exe.py                             # rebuild old exe
```

The Pygame exe is preserved at `dist/cOde(n)/cOde(n).exe` (gitignored).

## Why a web rebuild

Pygame limits the visual elements and slows iteration on UI/UX
(typography, theming, animations, code editor quality). The new
web stack gives us Monaco for a real Python editor, Tailwind for
modern theming, CSS transitions for smooth cell highlights, and an
architecture that doesn't box us into a single rendering technology.

The engine is the same. The challenges are the same. The progression
is the same. Only the presentation layer changed.
