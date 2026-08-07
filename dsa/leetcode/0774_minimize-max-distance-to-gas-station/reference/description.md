### 1. Description

You are given an integer array `stations` that represents the positions of the gas stations on the **x-axis**. You are also given an integer `k`.

You should add `k` new gas stations. You can add the stations anywhere on the **x-axis**, and not necessarily on an integer position.

Let `penalty()` be the maximum distance between **adjacent** gas stations after adding the `k` new stations.

Return *the smallest possible value of* `penalty()`. Answers within $10^{-6}$ of the actual answer will be accepted.

### 2. Function Contract

**Inputs**

- `stations`: a strictly increasing list of integer gas-station positions on the x-axis.
- `k`: the exact number of new gas stations to add.

New stations may be placed at arbitrary real-valued positions. Once the existing and new stations are ordered by position, only distances between adjacent stations contribute to `penalty()`.

**Return value**

- The smallest possible maximum adjacent-station distance after all `k` additions, returned as a floating-point value accurate within $10^{-6}$.

### 3. Examples

#### Example 1

- **Input:** $stations = [1,2,3,4,5,6,7,8,9,10], k = 9$
- **Output:** `0.50000`
#### Example 2

- **Input:** $stations = [23,24,36,39,46,56,57,65,84,98], k = 1$
- **Output:** `14.00000`

### 4. Constraints

- $10 \le \text{stations.length} \le 2000$

- $0 \le \text{stations}[i] \le 10^{8}$

- `stations` is sorted in a **strictly increasing** order.

- $1 \le k \le 10^{6}$