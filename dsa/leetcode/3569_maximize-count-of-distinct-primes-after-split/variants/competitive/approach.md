## General
**Competitive Approach — Maximize Count of Distinct Primes After Split**

The solution employs Two-Pointer technique iterating from opposing ends or maintaining a sliding window bound. It utilizes Hash Map / Dictionary for $O(1)$ average lookup and frequency tracking to maintain optimal runtime bounds. Key implementation techniques include Bitwise manipulation (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates.

**Why This Approach Was Chosen:**
Sourced from `kamyu104/LeetCode-Solutions`. This implementation focuses on raw computational throughput in method `linear_sieve_of_eratosthenes`. It minimizes object instantiation overhead, avoids redundant memory passes, and leverages compact iteration loops.

## Complexity detail
- **Time Complexity**: $O(U log log U + (n + q) log(n + q))$ — Operation count proportional to input scale.
- **Space Complexity**: $O(U + n + q)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Micro-Optimization:** Eliminates unnecessary function calls and temporary allocations to maximize execution speed.
- **Low Constant Factor:** Uses tight loop bounds and direct indexing for optimal judge performance.
