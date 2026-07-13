# Chalkboard XOR Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 810 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Bit Manipulation, Brainteaser, Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/chalkboard-xor-game/) |

## Problem Description

### Goal

Integers are written on a chalkboard. Alice and Bob alternate erasing exactly one number, with Alice moving first. If a player begins a turn when the XOR of all remaining numbers is `0`, that player wins immediately.

Otherwise the player must erase one number, but loses if that erasure makes the XOR of the remaining numbers equal to `0`. The XOR of an empty board is `0`. Return `True` exactly when Alice can win assuming both players choose moves optimally, and `False` otherwise.

### Function Contract

**Inputs**

- `nums`: a nonempty list of nonnegative integers initially written on the chalkboard.

**Return value**

- `True` if Alice has a winning strategy under optimal play; otherwise, `False`.

### Examples

**Example 1**

- Input: `nums = [1,1,2]`
- Output: `False`
- Explanation: The XOR is nonzero and the list length is odd, so every move gives Bob a winning position.

**Example 2**

- Input: `nums = [0,1]`
- Output: `True`
- Explanation: The XOR is nonzero, but an even number of entries guarantees Alice a safe move.

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `True`
- Explanation: The initial XOR is zero, so Alice wins before removing anything.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Identify the immediately winning state**

Compute the XOR `X` of all entries. If `X` is zero at the start of Alice's turn, the game rule gives her an immediate win.

**Characterize a dangerous removal**

If `X` is nonzero, removing a value `v` leaves XOR `X xor v`. This becomes zero exactly when $v = X$; that move lets the opponent begin with zero XOR and win immediately.

When the number of entries is even, not every entry can equal `X`: an even number of identical `X` values would XOR to zero, contradicting $X \ne 0$. Therefore, at least one safe value different from `X` can be removed. The opponent then receives an odd-length, nonzero-XOR position.

For an odd-length position with nonzero XOR, removing `X` loses immediately, while removing any other value leaves the opponent an even-length nonzero-XOR position, which has the safe-move property above. Thus every move from the odd position loses. With the one-element case as the base, this parity argument shows that nonzero-XOR positions are winning exactly at even length.

#### Complexity detail

XOR all `n` values once and inspect the length parity, taking $O(n)$ time. The running XOR is one scalar, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Explicit minimax:** Explore every remaining subset and memoize whose turn can win; it is correct but requires $O(n \cdot 2^n)$ work.
- **Frequency reasoning:** Counts can explain XOR cancellation, but the complete decision still reduces to total XOR and length parity.
- **Nim interpretation:** Superficial similarity to Nim can be misleading because a move removes an entire listed value and the zero-XOR state wins immediately.
- **Initial XOR zero:** Alice wins regardless of whether the length is odd or even.
- **Single nonzero value:** Its only removal gives the opponent an empty, zero-XOR board, so Alice loses.
- **Single zero:** Alice wins immediately.
- **Even nonzero position:** A safe move must exist by the XOR contradiction argument.

</details>
