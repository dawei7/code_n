# Most Expensive Item That Can Not Be Bought

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2979 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/most-expensive-item-that-can-not-be-bought/) |

## Problem Description
### Goal
The market contains an item at every positive integer price. Alice has an
unlimited supply of coins in two denominations, `primeOne` and `primeTwo`,
which are distinct prime numbers.

An item can be bought when its price is a nonnegative integer combination of
the two denominations; either coin may be used any number of times, including
zero. Return the greatest positive price that cannot be formed in this way.

### Function Contract
**Inputs**

- `primeOne`: the first prime coin denomination
- `primeTwo`: the distinct second prime coin denomination

Both primes are greater than `1` and less than $10^4$, and their product is
less than $10^5$.

**Return value**

The largest positive integer not representable as
$x\cdot\texttt{primeOne}+y\cdot\texttt{primeTwo}$ for nonnegative integers
$x$ and $y$.

### Examples
**Example 1**

- Input: `primeOne = 2`, `primeTwo = 5`
- Output: `3`
- Explanation: Prices `1` and `3` are impossible, while every larger price is representable.

**Example 2**

- Input: `primeOne = 5`, `primeTwo = 7`
- Output: `23`
- Explanation: `23` is impossible and every greater integer is a combination of `5` and `7`.
