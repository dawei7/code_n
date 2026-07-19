# Product of Two Run-Length Encoded Arrays

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/product-of-two-run-length-encoded-arrays/) |
| Frontend ID | 1868 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

A run-length encoding represents an integer array as pairs `[value, frequency]`. Each pair expands to `frequency` consecutive copies of `value`, and adjacent pairs never store the same value. Two such encodings, `encoded1` and `encoded2`, represent arrays of equal decoded length.

Multiply the two decoded arrays element by element, then return the run-length encoding of that product array. The returned encoding must also be compressed: if consecutive product positions have the same value, they belong to one pair whose frequency covers the whole run. Process the encodings directly rather than materializing the potentially much longer decoded arrays.

### Function Contract

**Inputs**

- `encoded1`: a nonempty list of `[value, frequency]` pairs with positive values and frequencies; adjacent values differ.
- `encoded2`: another valid encoding whose decoded length equals that of `encoded1`.
- Let $M = \lvert\texttt{encoded1}\rvert$ and $N = \lvert\texttt{encoded2}\rvert$.

**Return value**

- Return the run-length encoding of the elementwise product of the two decoded arrays.
- Every returned frequency is positive, and adjacent returned pairs must have different product values.

### Examples

**Example 1**

- Input: `encoded1 = [[1,3],[2,3]]`, `encoded2 = [[6,3],[3,3]]`
- Output: `[[6,6]]`

Both aligned run products equal `6`, so they merge into one six-element run.

**Example 2**

- Input: `encoded1 = [[1,3],[2,1],[3,2]]`, `encoded2 = [[2,3],[3,3]]`
- Output: `[[2,3],[6,1],[9,2]]`

The run boundaries differ, but the pointers consume only the overlap at each step.

**Example 3**

- Input: `encoded1 = [[4,5]]`, `encoded2 = [[2,2],[3,3]]`
- Output: `[[8,2],[12,3]]`

One long run may overlap several runs from the other encoding.

### Required Complexity

- **Time:** $O(M + N)$
- **Space:** $O(M + N)$

<details>
<summary>Approach</summary>

#### General

**View the current runs as two remaining intervals**

Keep one pointer in each encoding and track the unconsumed frequency of both current runs. Their decoded positions overlap for the smaller remaining frequency. Every position in that overlap has the same product, so append exactly one product run for that many positions.

**Advance every exhausted boundary**

Subtract the overlap length from both remaining frequencies. Advance a pointer whenever its current frequency reaches zero; when both reach zero together, advance both. Each iteration therefore consumes at least one complete input run, so the number of iterations is at most $M+N-1$.

**Preserve canonical compression**

The same product can arise on both sides of an input boundary. Before appending, compare the product with the last output value. Equal values extend the last frequency; different values start a new output pair. Every decoded position is covered once, in order, and receives the product of its two source values, while this merge rule guarantees that the returned encoding has no adjacent equal values.

#### Complexity detail

Each input pointer advances monotonically and visits every run once, giving $O(M+N)$ time. The output contains at most $M+N-1$ runs, so including the returned data the space use is $O(M+N)$. Apart from that output, the pointer and remaining-frequency state is $O(1)$. These bounds are independent of the decoded array length.

#### Alternatives and edge cases

- **Decode, multiply, and re-encode:** This is straightforward but costs time and memory proportional to the decoded length, which may be far larger than $M+N$.
- **Queue of expanded values:** Streaming expanded values avoids two full arrays but still performs one operation per decoded element.
- **Coincident boundaries:** When both remaining frequencies reach zero, both pointers must advance.
- **Unequal run boundaries:** Consume only the smaller remaining frequency; the other run continues into the next overlap.
- **Equal neighboring products:** Merge them even when the underlying input values changed.
- **One run against many:** The longer run remains active while the opposite pointer advances several times.
- **Large frequencies:** Never loop once per represented element.

</details>
