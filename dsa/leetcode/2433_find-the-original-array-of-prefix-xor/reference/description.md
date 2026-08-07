## Description

You are given an **integer** array `pref` of size `n`. Find and return *the array *`arr`* of size *`n`* that satisfies*:

- $\text{pref}[i] = \text{arr}[0] ^ \text{arr}[1] ^ ... ^ \text{arr}[i]$.

Note that $^$ denotes the **bitwise-xor** operation.

It can be proven that the answer is **unique**.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** $pref = [5,2,0,3,1]$
- **Output:** `[5,7,2,3,2]`
- **Explanation:** From the array [5,7,2,3,2] we have the following:
- pref[0] = 5.
- pref[1] = 5 ^ 7 = 2.
- pref[2] = 5 ^ 7 ^ 2 = 0.
- pref[3] = 5 ^ 7 ^ 2 ^ 3 = 3.
- pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.
#### Example 2

- **Input:** $pref = [13]$
- **Output:** `[13]`
- **Explanation:** We have pref[0] = arr[0] = 13.
### Constraints

- $1 \le \text{pref.length} \le 10^{5}$

- $0 \le \text{pref}[i] \le 10^{6}$