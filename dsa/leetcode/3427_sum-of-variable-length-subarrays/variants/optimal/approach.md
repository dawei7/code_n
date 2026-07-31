## General

Each required quantity is a range sum. Build a prefix array with `prefix[0] = 0`, where `prefix[j]` equals the sum of the first $j$ values. Then the inclusive range from `start` through `i` has sum `prefix[i + 1] - prefix[start]`.

For every index `i`, compute `start = max(0, i - nums[i])` exactly as defined by the contract and add that constant-time range query to the answer. The prefix construction accounts for each input value once, and the second scan accounts for each endpoint once, so all required subarrays are included exactly once without repeatedly traversing their overlapping elements.

## Complexity detail

Let $n$ be the length of `nums`. Constructing the prefix array and evaluating all $n$ queries take $O(n)$ time. The prefix array uses $O(n)$ auxiliary space. The maximum legal total fits comfortably in a Python integer.

## Alternatives and edge cases

- **Directly sum every slice:** This mirrors the definition and is correct, but overlapping windows can make it $O(n^2)$.
- **Maintain one sliding window:** Consecutive endpoints can request unrelated start positions, so there is no single monotone window to update.
- **Single element:** Its start is clamped to `0`, and that value is the complete answer.
- **Value larger than its index:** The start clamps to `0`, so the subarray contains the entire prefix through `i`.
- **Overlapping subarrays:** Repeated contributions are intentional because every endpoint defines a separate subarray.
