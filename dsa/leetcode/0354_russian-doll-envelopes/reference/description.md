### 1. Description

You are given a 2D array of integers `envelopes` where $\text{envelopes}[i] = [w_{i}, h_{i}]$ represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return *the maximum number of envelopes you can Russian doll (i.e., put one inside the other)*.

### 2. Function Contract

**Inputs**

- `envelopes`: The array of `[width,height]` envelope dimensions.

**Return value**

Return the maximum length of a chain in which both dimensions increase strictly from each inner envelope to the next outer envelope.

### 3. Note

You cannot rotate an envelope.

### 4. Examples

#### Example 1

- **Input:** $envelopes = [[5,4],[6,4],[6,7],[2,3]]$
- **Output:** `3`
- **Explanation:** The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

#### Example 2

- **Input:** $envelopes = [[1,1],[1,1],[1,1]]$
- **Output:** `1`

### 5. Constraints

- $1 \le \text{envelopes.length} \le 10^{5}$

- $\text{envelopes}[i].length = 2$

- $1 \le w_{i}, h_{i} \le 10^{5}$
