### 1. Description

There is a biker going on a road trip. The road trip consists of $n + 1$ points at various altitudes. The biker starts his trip on point `0` with altitude equal `0`.

You are given an integer array `gain` of length `n` where $\text{gain}[i]$ is the **net gain in altitude** between points `i`​​​​​​ and $i + 1$ for all ($0 \le i < n)$. Return *the **highest altitude** of a point.*

### 2. Function Contract

**Inputs**

- `gain`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $gain = [-5,1,5,0,-7]$
- **Output:** `1`
- **Explanation:** The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

#### Example 2

- **Input:** $gain = [-4,-3,-2,-1,4,3,2]$
- **Output:** `0`
- **Explanation:** The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

### 4. Constraints

- $n = \text{gain.length}$

- $1 \le n \le 100$

- $-100 \le \text{gain}[i] \le 100$
