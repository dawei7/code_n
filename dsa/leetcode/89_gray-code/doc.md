# Gray Code

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 89 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Backtracking, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/gray-code/) |

## Problem Description
### Goal
For a positive bit width `n`, consider every integer representable by exactly `n` binary bits, from `0` through $2^{n} - 1$. Arrange all of them in one sequence beginning with zero.

Consecutive values must differ in exactly one bit, and the final value must also differ from the initial zero in exactly one bit, making the ordering cyclic. Return any sequence satisfying these properties, with every value appearing once; more than one Gray-code cycle may be valid.

### Function Contract
**Inputs**

- `n`: the positive bit width

**Return value**

A valid list of all $2^{n}$ integers; more than one ordering may be correct.

### Examples
**Example 1**

- Input: `n = 2`
- Output: `[0,1,3,2]`

**Example 2**

- Input: `n = 1`
- Output: `[0,1]`

**Example 3**

- Input: `n = 3`
- Output: one valid cycle such as `[0,1,3,2,6,7,5,4]`

### Required Complexity

- **Time:** $O(2^n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Map each binary rank directly to its reflected Gray code**

For each integer rank `i` from `0` through $2^{n} - 1$, emit:

```text
gray(i) = i ^ (i >> 1)
```

At each bit position, this records whether two adjacent bits of the binary rank differ. The transform produces the same order as recursively reflecting the previous Gray-code list and prefixing a new high bit, but computes each output independently.

**Consecutive ranks collapse to one changed Gray bit**

Suppose rank `i` ends with `t` binary ones. Incrementing it flips those `t` low bits to zero and flips the next bit to one, so $i \oplus (i + 1)$ is a run of $t + 1$ low one-bits. Applying the Gray transform to both ranks makes adjacent changes cancel pairwise; their Gray values differ only at bit `t`.

Equivalently, $\operatorname{gray}(i) \oplus \operatorname{gray}(i + 1)$ is a power of two. A power of two has exactly one set bit, which is precisely the one-bit adjacency condition.

**Trace the complete two-bit cycle**

For ranks 0, 1, 2, and 3, the transform yields 0, 1, 3, and 2. In binary these are `00, 01, 11, 10`; every adjacent pair and the closing pair differ in one bit.

**Bijection and circular closure**

The transform is invertible: recover the highest binary bit from the highest Gray bit, then recover each lower binary bit by XORing the preceding recovered bit with the current Gray bit. It is therefore a bijection, so all $2^{n}$ values appear exactly once.

The consecutive-rank argument proves adjacency throughout the list. The final binary rank is `11...1`; XORing it with its right shift yields `10...0`, which differs from initial Gray value zero in exactly the high bit. Thus the output also closes into a valid cycle.

#### Complexity detail

Exactly $2^{n}$ required outputs are computed in constant time each, giving $O(2^n)$ time. Excluding the returned list, only the loop rank uses $O(1)$ space.

#### Alternatives and edge cases

- **Reflect and prefix:** builds each Gray-code level from the previous one and has the same output complexity.
- **Backtracking over one-bit neighbors:** can find a cycle but needs visited state and far more search machinery.
- **Ordinary binary order:** covers all values but often flips several bits between neighbors.
- $n = 1$ produces `[0,1]`, whose closing edge also changes one bit. If a generalized contract permits $n = 0$, the natural sequence contains only `[0]`.
- Output storage contains $2^{n}$ integers and is excluded from the stated $O(1)$ auxiliary-space bound.

</details>
