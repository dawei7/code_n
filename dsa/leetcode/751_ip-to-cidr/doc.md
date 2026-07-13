# IP to CIDR

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 751 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/ip-to-cidr/) |

## Problem Description

### Goal

Given a starting IPv4 address `ip` and a positive count `n`, consider exactly `n` consecutive addresses beginning with `ip`. Represent that complete address range using CIDR blocks.

Return the smallest possible list of CIDR blocks whose union covers every requested address and no address before the start or after the end. Each block must be correctly aligned for its prefix length, and the returned blocks should follow address order without gaps or overlaps outside the target range.

### Function Contract

**Inputs**

- `ip`: the first IPv4 address in dotted-decimal notation.
- `n`: the positive number of consecutive addresses to cover.

**Return value**

- A minimum-length list of CIDR strings whose disjoint ranges cover exactly the requested addresses.

### Examples

**Example 1**

- Input: `ip = "255.0.0.7"`, `n = 10`
- Output: `["255.0.0.7/32", "255.0.0.8/29", "255.0.0.16/32"]`
- Explanation: The middle block covers eight aligned addresses, while the two boundary addresses require singleton blocks.

**Example 2**

- Input: `ip = "0.0.0.0"`, `n = 4`
- Output: `["0.0.0.0/30"]`
- Explanation: The start is aligned to a four-address block, so one prefix covers the entire range.

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(\log n)$

<details>
<summary>Approach</summary>

#### General

**Treat an IPv4 address as a 32-bit integer**

Shift the four octets into one unsigned integer. Consecutive IPv4 addresses then become consecutive integers, and a CIDR block of size $2^{k}$ is valid at `current` exactly when `current` is divisible by $2^{k}$.

**Choose the largest legal block at the current boundary**

The lowest set bit of `current`, computed as `current & - current`, is the largest power-of-two block aligned there. The block also cannot exceed the number of addresses remaining, so cap it by the greatest power of two no larger than `remaining`. For address zero, every power of two is aligned; treat its alignment allowance as $2^{32}$.

Convert a chosen size $2^{k}$ to prefix length $32 - k$, emit the dotted address with that prefix, advance by the block size, and repeat.

**Why taking the largest block is optimal**

Any exact cover must begin at the current first uncovered address. A first block larger than the chosen one is either misaligned or extends beyond the remaining interval, so it is illegal. Replacing the chosen block with smaller aligned blocks requires at least two blocks to cover the same initial range and cannot improve the suffix. Therefore some minimum cover uses the greedy block first; applying the same argument after advancing proves the entire list minimum.

#### Complexity detail

The dyadic decomposition of an interval uses $O(\log n)$ blocks. Each iteration performs constant-time 32-bit arithmetic and formatting, so time is $O(\log n)$. The returned block list uses $O(\log n)$ space, while auxiliary state apart from the output is $O(1)$.

#### Alternatives and edge cases

- **Emit every address as `/32` and merge siblings:** This can produce the same minimum cover, but it first performs $O(n)$ work and storage.
- **Increase the prefix until a block fits:** Trying block sizes one by one is correct but less direct than using the low bit and remaining count.
- **Unaligned starting address:** Alignment may force one or more small blocks before a larger block becomes available.
- **Address `0.0.0.0`:** Its low bit is numerically zero, so handle it as aligned to the full $2^{32}$ address space.
- **One requested address:** Emit the start address with prefix `/32`.
- **Octet boundary crossing:** Integer addition naturally carries from one octet into the next.
- **Exact coverage:** Cap every block by `remaining`; alignment alone does not prevent overshooting the requested suffix.

</details>
