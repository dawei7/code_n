# cOde(n)

A 2D grid-based game for learning Python algorithms through a realistic Computer Science BSc Algorithms and Data Structures course. Write solutions in your editor, run them, and see your algorithms visualized with real complexity measurement.

**Similar to "The Farmer Was Replaced" — but for algorithms, entirely in Python.**

## Backstory

In `cOde(n)`, the main figure is the student name chosen by the player. That student is working through a Computer Science BSc course in Algorithms and Data Structures: lectures, lab sheets, quiet study sessions, failing tests, corrected assumptions, and steady practice.

The story stays grounded and pure. There is no fantasy violence, romance, or shock content; the focus is the ordinary pressure and satisfaction of learning core algorithms well. Each level is a lab exercise where the student turns Python code into visible operations and learns why complexity matters.

## How It Works

1. You see a challenge with data displayed on a 2D grid
2. You write a `solve()` function using tracked data structures
3. Every operation (read, write, compare, swap) is counted
4. Your solution must be **correct** AND within the **complexity threshold**
5. The threshold is based on operation count — not speed — so the actual O() class matters

## Quick Start

```bash
# See the challenge tree and available levels
python main.py

# Open the Pygame navigator
python main.py nav

# Get info about a challenge
python main.py info intro_01

# Write your solution in solutions/<challenge_id>.py
python main.py nav

# Run your solution against a challenge
python run_challenge.py intro_01

# Run with graphics and choose speed in the Pygame window
python run_challenge.py intro_01 --pygame

# Or skip the chooser with a preset
python run_challenge.py intro_01 --pygame --speed step
python run_challenge.py intro_01 --pygame --speed very-slow
python run_challenge.py intro_01 --pygame --speed fast

# Use a larger input to test scalability
python run_challenge.py search_02 my_solution.py --n 256
```

## Explore Before Running

The Pygame navigator has three actions for each unlocked challenge:

| Button        | Purpose                                                                        |
| ------------- | ------------------------------------------------------------------------------ |
| `Explore`     | Preview the task, sample input visualization, and an example solution pattern. |
| `Run`         | Run your saved solution with the visual debugger.                              |
| `Open Script` | Open or create your solution file in your editor.                              |

The challenge description stays visible in both `Explore` and `Run` views so the task goal is always in front of the student.

## Pygame Learning Controls

When a challenge runs with `--pygame`, `cOde(n)` shows an algorithm debugger view:

| Control                 | Action                           |
| ----------------------- | -------------------------------- |
| `Space` / `P`           | Pause or resume replay           |
| `Enter` / `Right Arrow` | Execute one operation and pause  |
| `M`                     | Toggle step-by-step mode         |
| `S`                     | Stop at the current step         |
| `R`                     | Replay from the beginning        |
| `+` / `-`               | Adjust replay speed              |
| Click a grid/list cell  | Toggle a watchpoint on that cell |
| `Esc` / `Q`             | Close the graphics window        |

The side panel also has clickable controls for Play/Pause, Next, Replay, Manual/Auto mode, Stop, Slower, and Faster.

The speed chooser includes `step`, `crawl`, `very-slow`, `slow`, `normal`, `fast`, `turbo`, and `instant`. In `step` mode, every `Space`, `Enter`, or `Right Arrow` press executes exactly one recorded operation.

The side panel shows operation counts, complexity, the current operation, local variable values from your `solve()` function, and the final return value. List operations such as `swap`, indexed assignment, `append`, `insert`, and `pop` update the visible array while the replay runs.

Click a visible cell to add a watchpoint. Replay pauses when a read, write, compare, or swap touches that cell. This is useful when you want to follow one list index or grid coordinate through an algorithm.

For source-line replay stops, add this comment to a line in your solution:

```python
# code_n: breakpoint
```

When the visual replay reaches that recorded source line, it pauses and labels the variables panel as a breakpoint line. VS Code's red-dot breakpoints still belong to the VS Code debugger; the packaged game cannot reliably read them directly.

## Windows Distribution

Recommended player distribution: build a portable Windows app folder.

```bat
build_windows_exe.bat
```

This creates:

```text
dist\cOde(n)\cOde(n).exe
```

Zip and distribute the whole `dist\cOde(n)` folder. Players can double-click `cOde(n).exe`; they do not need to install Python, Pygame, or any pip packages.

For source-code distribution instead, players can double-click:

```bat
setup_and_play.bat
```

That creates `.venv`, installs `requirements.txt`, and starts the Pygame navigator.

## Challenge Tree

Challenges are organized in a tree with 4 paths. You unlock the next level only after completing its prerequisites.

```
                    ┌─── Sorting ──────────────────────────────────┐
                    │  Bubble → Selection → Insertion → Merge/Quick → Heap │
                    │                                                       │
 Hello Grid ───────┼─── Searching ────────────────────────────────┐
 (intro_01)        │  Linear → Binary → BFS Grid / DFS Grid → A* │
                    │                                              │
                    ├─── Graphs ───────────────────────────────────┐
                    │  Representation → BFS/DFS → Dijkstra → MST  │
                    │                                              │
                    └─── Dynamic Programming ──────────────────────┐
                       Fibonacci → Stairs → Knapsack / LCS → Matrix│
```

## Writing Solutions

Your script must import tracked structures from `code_n.api` and define a `solve` function. The arguments depend on the challenge:

```python
from code_n.api import TrackedGrid, TrackedList

# Sorting challenges
def solve(data: TrackedList, n: int) -> TrackedList:
    # sort data in-place using data.compare(i, j) and data.swap(i, j)
    return data

# Searching challenges
def solve(data: TrackedList, target: int, n: int) -> int:
    # return the index of target, or -1
    return index

# Grid challenges
def solve(grid: TrackedGrid, start: tuple, goal: tuple, size: int) -> int:
    # return shortest path length
    return distance

# DP challenges
def solve(n: int) -> int:
    # return the computed value
    return answer
```

## Tracked Data Structures

Use these instead of raw Python lists — every operation is counted:

| Structure      | Operations                                                                       |
| -------------- | -------------------------------------------------------------------------------- |
| `TrackedList`  | `data[i]` (read), `data[i] = x` (write), `data.compare(i, j)`, `data.swap(i, j)` |
| `TrackedGrid`  | `grid.get(x, y)`, `grid.set(x, y, val)`, `grid.compare(...)`, `grid.swap(...)`   |
| `TrackedQueue` | `enqueue()`, `dequeue()`, `peek()`                                               |
| `TrackedStack` | `push()`, `pop()`, `peek()`                                                      |
| `TrackedSet`   | `add()`, `contains()`, `remove()`                                                |

## Complexity Thresholds

Each challenge has a maximum allowed complexity class. Your operation count must stay within the limit:

| Class      | Operations allowed (approx.) |
| ---------- | ---------------------------- |
| O(1)       | ≤ 10                         |
| O(log n)   | ≤ 3·log₂(n) + 10             |
| O(n)       | ≤ 3n + 10                    |
| O(n log n) | ≤ 2n·log₂(n) + 10            |
| O(n²)      | ≤ 2n² + 10                   |

## Project Structure

```
code_n/
├── main.py                  # Game menu & challenge tree display
├── run_challenge.py         # Challenge runner (validates & scores)
├── code_n/                  # Core engine
│   ├── grid.py              # 2D grid with cell types
│   ├── renderer.py          # ANSI terminal rendering
│   ├── counter.py           # Operation counter & complexity classifier
│   ├── tracked.py           # Tracked data structures (TrackedList, etc.)
│   ├── challenge.py         # Challenge base class
│   ├── tree.py              # Challenge tree & unlock logic
│   ├── progress.py          # Save/load player progress
│   └── api.py               # Public API for player scripts
├── challenges/              # Challenge implementations
│   ├── intro.py             # Intro challenges
│   ├── sorting.py           # Sorting algorithm challenges
│   ├── searching.py         # Search algorithm challenges
│   ├── graphs.py            # Graph algorithm challenges
│   ├── dynamic.py           # Dynamic programming challenges
│   └── registry.py          # Challenge ID → class mapping
├── player_scripts/          # Example solutions & templates
│   ├── template.py          # Empty template to copy
│   ├── solve_intro_01.py    # Example: find max
│   ├── solve_sort_01.py     # Example: bubble sort
│   ├── solve_search_02.py   # Example: binary search
│   └── solve_dp_01.py       # Example: fibonacci
└── progress.json            # Your save file (auto-generated)
```
