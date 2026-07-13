# Decode Ways

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 91 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/decode-ways/) |

## Problem Description
### Goal
Letters are encoded by the integers `1` through `26`, mapping in order from `A` through `Z`. Given a nonempty decimal digit string, split it into one- or two-digit codes and decode every part using that mapping.

Return the number of complete valid decodings. Different split boundaries count as different ways even when prefixes overlap. A zero has no standalone letter and is valid only inside `10` or `20`; leading zeroes and pairs above `26` invalidate the affected split. Return zero when no full decoding exists.

### Function Contract
**Inputs**

- `s`: a nonempty string of decimal digits

**Return value**

The number of valid complete decodings.

### Examples
**Example 1**

- Input: `s = "12"`
- Output: `2`

**Example 2**

- Input: `s = "226"`
- Output: `3`

**Example 3**

- Input: `s = "06"`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Partition decodings by a one- or two-digit final code**

For each prefix ending at position `i`, a one-digit final code is legal only when `s[i] != "0"`; it extends every decoding of the preceding prefix. A two-digit final code is legal only when the pair lies from `10` through `26`; it extends every decoding ending two positions earlier. These ending categories are disjoint.

**The empty-prefix count anchors two-digit codes at the start**

Initialize the empty-prefix count to `1`: there is one way to decode no characters, which lets a valid first pair such as `"12"` contribute correctly. The first-character count is zero for `"0"` and one otherwise. For each later position, compute the new count from only those two prior prefix counts, then shift them forward.

**Zeroes contribute only through valid pairs**

Before processing position `i`, the two variables equal the decoding counts for prefix lengths $i - 1$ and `i`. Appending a legal one- or two-digit token creates disjoint decoding sets from those prefixes. A zero contributes nothing through the single-digit branch; only `10` or `20` can carry a positive count through it.

**Trace both branching and zero restrictions**

For `226`, prefix `22` has two decodings: $2 | 2$ and `22`. At `6`, a single `6` extends both, while `26` extends the decoding of the first `2`, totaling three. For `2101`, the zero forces `10`; the later `01` is illegal, but the final `1` can stand alone after the forced pair, leaving one decoding.

**The final code partitions all decodings**

Every complete decoding ends with either one digit representing `1..9` or two digits representing `10..26`. Removing that final code leaves a valid decoding of the prefix one or two positions earlier, respectively.

The two categories are disjoint because their final code lengths differ, and they exhaust the allowed alphabet encodings. Adding only the predecessor counts whose final digits form a legal code therefore counts every decoding once, while leading zeroes, isolated zeroes, and pairs above 26 contribute nothing.

#### Complexity detail

Each digit is processed once, giving $O(n)$ time. Two previous counts and one current count use $O(1)$ space.

#### Alternatives and edge cases

- **Unmemoized recursion:** repeats suffix states exponentially.
- **DP array:** has the same linear time but stores $O(n)$ counts unnecessarily.
- **Greedy tokenization:** cannot choose locally between one- and two-digit codes without losing valid alternatives.
- A leading zero returns zero immediately through initialization. Pairs such as `30`, `06`, and `27` are not legal two-digit codes.
- The count can be zero partway through and later cannot revive unless a legal token connects to a prefix with a nonzero prior count.

</details>
