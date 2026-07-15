# Handshakes That Don't Cross

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1259 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/handshakes-that-dont-cross/) |

## Problem Description

### Goal

An even number of people sit around a circle. Every person must shake hands with exactly one other person, producing a perfect pairing. Draw each handshake as a straight segment between the two participants.

Count how many different complete pairing arrangements can be drawn without any two handshake segments crossing inside the circle. Return the count modulo $10^9+7$. People occupy distinct positions, so pairings that connect different position pairs are different arrangements even when they have the same geometric shape after rotation.

### Function Contract

**Inputs**

- `numPeople`: an even integer between `2` and `1000`.
- Let $p=\texttt{numPeople}/2$ be the number of handshake pairs.

**Return value**

- Return the number of noncrossing perfect pairings modulo $10^9+7$.

### Examples

**Example 1**

- Input: `numPeople = 2`
- Output: `1`

**Example 2**

- Input: `numPeople = 4`
- Output: `2`

**Example 3**

- Input: `numPeople = 6`
- Output: `5`

### Required Complexity

- **Time:** $O(p\log M)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Fix one distinguished person. If that person shakes hands with another position, their segment divides the remaining circle into two independent arcs. A noncrossing arrangement is possible only when each arc contains an even number of people, because everyone within an arc must pair internally.

**Catalan recurrence from the first handshake**

Let `dp[k]` count noncrossing arrangements for `k` pairs, with `dp[0] = 1` for the empty interior. When the distinguished person leaves `i` complete pairs on one side of their handshake, the other side contains `k - 1 - i` pairs. The two sides can be arranged independently, contributing `dp[i] * dp[k - 1 - i]` possibilities.

Summing over $0 \le i < k$ gives the Catalan recurrence

$$
\textit{dp}[k]=\sum_{i=0}^{k-1}\textit{dp}[i]\,\textit{dp}[k-1-i].
$$

Every noncrossing pairing has one unique partner for the distinguished person and therefore appears in exactly one split. Conversely, combining any two valid subarrangements across a split cannot introduce a crossing because they lie on opposite sides of the fixed segment.

**Evaluate successive Catalan numbers directly**

Rather than summing every earlier split for every state, use the equivalent ratio

$$
C_{k+1}=C_k\frac{2(2k+1)}{k+2}.
$$

Division modulo the prime $M=10^9+7$ is multiplication by $(k+2)^{M-2}\bmod M$, using Fermat's little theorem. Starting from $C_0=1$, apply this update for $k=0$ through $p-1$. All denominators are smaller than $M$, so each has an inverse.

#### Complexity detail

There are $p$ updates. Each modular inverse is computed by binary exponentiation in $O(\log M)$ time, giving $O(p\log M)$ total time. Only the current Catalan value and loop counters are retained, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Naive recursive splitting:** It follows the same proof but recomputes identical pair counts exponentially many times without memoization.
- **Quadratic Catalan DP:** Directly evaluating every split is straightforward and uses $O(p^2)$ time, which is slower under the app runner's full boundary case.
- **Factorial formula:** $C_p=\frac{1}{p+1}\binom{2p}{p}$ can be evaluated with factorial tables and modular inverses, but uses $O(p)$ storage.
- **Two people:** The sole possible handshake is noncrossing, matching the base transition from `dp[0]`.
- **Modulo arithmetic:** Reduce every multiplication so implementations with fixed-width integers do not overflow.

</details>
