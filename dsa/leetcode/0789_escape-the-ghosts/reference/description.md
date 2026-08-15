### 1. Description

You are playing a simplified PAC-MAN game on an infinite 2-D grid. You start at the point `[0, 0]`, and you are given a destination point $target = [x_{target}, y_{target}]$ that you are trying to get to. There are several ghosts on the map with their starting positions given as a 2D array `ghosts`, where $\text{ghosts}[i] = [x_{i}, y_{i}]$ represents the starting position of the $$i^{\text{th}}$$ ghost. All inputs are **integral coordinates**.

Each turn, you and all the ghosts may independently choose to either **move 1 unit** in any of the four cardinal directions: north, east, south, or west, or **stay still**. All actions happen **simultaneously**.

You escape if and only if you can reach the target **before** any ghost reaches you. If you reach any square (including the target) at the **same time** as a ghost, it **does not** count as an escape.

Return `true`* if it is possible to escape regardless of how the ghosts move, otherwise return *`false`*.*

### 2. Function Contract

**Inputs**

- `ghosts`: Input parameter (`List[List[int]]`).
- `target`: Input parameter (`List[int]`).

**Return value**

- Returns `bool`.

### 3. Examples

#### Example 1

- **Input:** $ghosts = [[1,0],[0,3]], target = [0,1]$
- **Output:** `true`
- **Explanation:** You can reach the destination (0, 1) after 1 turn, while the ghosts located at (1, 0) and (0, 3) cannot catch up with you.

#### Example 2

- **Input:** $ghosts = [[1,0]], target = [2,0]$
- **Output:** `false`
- **Explanation:** You need to reach the destination (2, 0), but the ghost at (1, 0) lies between you and the destination.

#### Example 3

- **Input:** $ghosts = [[2,0]], target = [1,0]$
- **Output:** `false`
- **Explanation:** The ghost can reach the target at the same time as you.

### 4. Constraints

- $1 \le \text{ghosts.length} \le 100$

- $\text{ghosts}[i].length = 2$

- $-10^{4} \le x_{i}, y_{i} \le 10^{4}$

- There can be **multiple ghosts** in the same location.

- $\text{target.length} = 2$

- $-10^{4} \le x_{target}, y_{target} \le 10^{4}$
