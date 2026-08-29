### 1. Description

You are given an `m x n` matrix of characters `boxGrid` representing a side-view of a box. Each cell of the box is one of the following:

- A stone `'#'`

- A stationary obstacle `'*'`

- Empty `'.'`

The box is rotated **90 degrees clockwise**, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity **does not** affect the obstacles' positions, and the inertia from the box's rotation **does not **affect the stones' horizontal positions.

It is **guaranteed** that each stone in `boxGrid` rests on an obstacle, another stone, or the bottom of the box.

Return *an *`n x m`* matrix representing the box after the rotation described above*.

### 2. Function Contract

**Inputs**

- `boxGrid`: Input parameter (`List[List[str]]`).

**Return value**

- Returns `List[List[str]]`.

### 3. Examples

#### Example 1

![](images/rotatingtheboxleetcodewithstones.png)

- **Input:** `boxGrid = [["#",".","#"]]`
- **Output:** `[["."],`
["#"],
["#"]]

#### Example 2

![](images/rotatingtheboxleetcode2withstones.png)

- **Input:** $boxGrid = [["#",".","*","."],$
["#","#","*","."]]
- **Output:** `[["#","."],`
["#","#"],
["*","*"],
[".","."]]

#### Example 3

![](images/rotatingtheboxleetcode3withstone.png)

- **Input:** $boxGrid = [["#","#","*",".","*","."],$
["#","#","#","*",".","."],
["#","#","#",".","#","."]]
- **Output:** `[[".","#","#"],`
[".","#","#"],
["#","#","*"],
["#","*","."],
["#",".","*"],
["#",".","."]]

### 4. Constraints

- $m = \text{boxGrid.length}$

- $n = \text{boxGrid}[i].length$

- $1 \le m, n \le 500$

- $\text{boxGrid}[i][j]$ is either `'#'`, `'*'`, or `'.'`.
