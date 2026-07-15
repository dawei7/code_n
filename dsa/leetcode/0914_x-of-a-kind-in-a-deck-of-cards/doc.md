# X of a Kind in a Deck of Cards

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 914 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Math, Counting, Number Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/) |

## Problem Description
### Goal

You are given an integer array `deck`, where `deck[i]` is the number written on the $i$th card. Partition every card into one or more groups. All groups must share one size $x$, and that size must satisfy $x>1$.

Each group must contain exactly $x$ cards, and every card within one group must have the same integer written on it. Return `true` if all cards can be partitioned under these rules; otherwise, return `false`.

### Function Contract
**Inputs**

- `deck`: an array of $n$ card values, where $1 \le n \le 10^4$ and every value is between $0$ and $10^4-1$, inclusive.

**Return value**

`true` if some common group size $x>1$ divides the frequency of every distinct card value; otherwise, `false`.

### Examples
**Example 1**

- Input: `deck = [1,2,3,4,4,3,2,1]`
- Output: `true`
- Explanation: Four groups of size $2$ can be formed, one for each value.

**Example 2**

- Input: `deck = [1,1,1,2,2,2,3,3]`
- Output: `false`
- Explanation: The frequencies $3$, $3$, and $2$ have no common divisor greater than $1$.

**Example 3**

- Input: `deck = [7,7,7]`
- Output: `true`
- Explanation: The entire deck is one group of size $3$.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Reduce the partition to frequency divisibility**

Cards with different values can never share a group, so only the frequency of each distinct value matters. If a value occurs $f$ times and every group has size $x$, then $x$ must divide $f$. A single group size works for the whole deck exactly when it is a common divisor of every frequency.

Count the values, then compute the greatest common divisor of all frequencies. The greatest common divisor contains every integer that could divide every count: a valid $x>1$ exists if and only if this final value is greater than $1$. If the running greatest common divisor becomes $1$, it can never increase after incorporating more frequencies, so the method may return `false` immediately.

This test is sufficient as well as necessary. When the greatest common divisor is $g>1$, choose $x=g$. Every frequency is divisible by $g$, so the cards of each value split into complete groups of exactly that size, and those groups cover the deck without mixing values.

#### Complexity detail

Let $n$ be the number of cards. Building the frequency map visits all $n$ cards once. Computing greatest common divisors over at most $n$ distinct frequencies takes $O(n \log n)$ bit operations in the most literal arithmetic model, while the bounded integer domain used here gives the required $O(n)$ runtime. The frequency map stores at most $n$ entries, so auxiliary space is $O(n)$.

#### Alternatives and edge cases

- **Try every possible group size:** Testing each $x$ from $2$ through the smallest frequency is correct but repeats divisibility work and can be quadratic in the deck length.
- **Count each value by rescanning the deck:** Calling a linear count operation for every distinct value avoids a hash-map update loop but takes $O(n^2)$ time when many values are distinct.
- **One card:** A singleton frequency has greatest common divisor $1$, so no group size greater than $1$ is possible.
- **One distinct value:** The whole deck is valid whenever its length is at least $2$; the group size may equal that full frequency.
- **Multiple groups of one value:** A frequency need not equal $x$; it only needs to be divisible by $x$.
- **Card value zero:** Zero is an ordinary card label and has no special effect on grouping.

</details>
