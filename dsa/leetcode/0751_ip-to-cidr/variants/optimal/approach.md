## General
**Treat an IPv4 address as a 32-bit integer**

Shift the four octets into one unsigned integer. Consecutive IPv4 addresses then become consecutive integers, and a CIDR block of size $2^{k}$ is valid at `current` exactly when `current` is divisible by $2^{k}$.

**Choose the largest legal block at the current boundary**

The lowest set bit of `current`, computed as `current & - current`, is the largest power-of-two block aligned there. The block also cannot exceed the number of addresses remaining, so cap it by the greatest power of two no larger than `remaining`. For address zero, every power of two is aligned; treat its alignment allowance as $2^{32}$.

Convert a chosen size $2^{k}$ to prefix length $32 - k$, emit the dotted address with that prefix, advance by the block size, and repeat.

**Why taking the largest block is optimal**

Any exact cover must begin at the current first uncovered address. A first block larger than the chosen one is either misaligned or extends beyond the remaining interval, so it is illegal. Replacing the chosen block with smaller aligned blocks requires at least two blocks to cover the same initial range and cannot improve the suffix. Therefore some minimum cover uses the greedy block first; applying the same argument after advancing proves the entire list minimum.

## Complexity detail
The dyadic decomposition of an interval uses $O(\log n)$ blocks. Each iteration performs constant-time 32-bit arithmetic and formatting, so time is $O(\log n)$. The returned block list uses $O(\log n)$ space, while auxiliary state apart from the output is $O(1)$.

## Alternatives and edge cases
- **Emit every address as `/32` and merge siblings:** This can produce the same minimum cover, but it first performs $O(n)$ work and storage.
- **Increase the prefix until a block fits:** Trying block sizes one by one is correct but less direct than using the low bit and remaining count.
- **Unaligned starting address:** Alignment may force one or more small blocks before a larger block becomes available.
- **Address `0.0.0.0`:** Its low bit is numerically zero, so handle it as aligned to the full $2^{32}$ address space.
- **One requested address:** Emit the start address with prefix `/32`.
- **Octet boundary crossing:** Integer addition naturally carries from one octet into the next.
- **Exact coverage:** Cap every block by `remaining`; alignment alone does not prevent overshooting the requested suffix.
