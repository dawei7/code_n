## Examples

**Example 1**

- **Input:** `t = 100`, `calls = [{"t": 20, "inputs": [1]}]`
- **Output:** `[{"t": 20, "inputs": [1]}]`
- **Explanation:** Initial call at t=20 executes `fn([1])` immediately. No further calls arrive within 100ms.

**Example 2**

- **Input:** `t = 50`, `calls = [{"t": 50, "inputs": [1]}, {"t": 75, "inputs": [2]}]`
- **Output:** `[{"t": 50, "inputs": [1]}, {"t": 100, "inputs": [2]}]`
- **Explanation:** Call 1 at t=50 executes `fn([1])` immediately. Call 2 at t=75 arrives during the 50ms window and is buffered. At t=100 (50ms after t=50), the trailing execution `fn([2])` fires.

**Example 3**

- **Input:** `t = 70`, `calls = [{"t": 50, "inputs": [1]}, {"t": 75, "inputs": [2]}, {"t": 90, "inputs": [8]}, {"t": 140, "inputs": [5, 7]}, {"t": 300, "inputs": [9, 4]}]`
- **Output:** `[{"t": 50, "inputs": [1]}, {"t": 120, "inputs": [8]}, {"t": 190, "inputs": [5, 7]}, {"t": 300, "inputs": [9, 4]}]`
- **Explanation:**
  - t=50: `fn([1])` executes immediately (window 50-120).
  - t=75 & t=90: `[2]` is overwritten by `[8]`.
  - t=120: Window ends, trailing `fn([8])` executes (new window 120-190).
  - t=140: `[5, 7]` buffered.
  - t=190: Window ends, trailing `fn([5, 7])` executes.
  - t=300: Window is idle, `fn([9, 4])` executes immediately.
