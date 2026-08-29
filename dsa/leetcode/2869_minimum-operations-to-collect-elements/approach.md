## General

**Operations force a right-to-left order.** One operation removes the last array element and puts it in the collection. There is no choice about which position is removed next: the collection receives `nums[n-1]`, then `nums[n-2]`, and so on. The only decision is when to stop. The earliest stopping time at which all values `1,2,...,k` have appeared is automatically the minimum number of operations.

The solution simulates precisely this forced suffix scan. Array `is_added` has length `k`. Required value `v` maps to Boolean position `v - 1`, so indices `0..k-1` represent values `1..k`. Variable `count` records how many distinct required values have been seen.

**Why count distinct values rather than occurrences.** Collecting the same required number twice gives no additional progress: the goal is to possess every value at least once. When current `nums[i]` is at most `k` and its Boolean entry is still false, the source marks it true and increments `count`. If that entry was already true, the occurrence is ignored.

Values above `k` are also ignored for progress because they are not members of the required set. Importantly, “ignored” does not mean their removal costs no operation. The loop still moves past their index. When the algorithm eventually returns `n - i`, that distance includes every removed suffix element, useful or not.

**The stopping condition.** Once `count == k`, all $k$ distinct required values have been observed. The current scan began at index `n-1` and has reached index `i` inclusively, so the number removed is

$$
(n-1)-i+1=n-i.
$$

The function returns that value immediately. Stopping earlier would omit at least one required value because `count` had not yet reached $k$. Continuing longer would add operations without being necessary. Therefore this first return is minimal.
Before processing index `i`, each true entry `is_added[v-1]` means value `v` appears somewhere in the already removed suffix `nums[i+1..n-1]`, and `count` is exactly the number of true entries. Processing `nums[i]` preserves that statement: an irrelevant or duplicate value changes nothing, while a first occurrence of a required value changes exactly its corresponding false entry and increases the true-entry count by one.

When the return occurs, the invariant proves the collection contains every value from one through $k$. If the loop has not returned earlier, the invariant also proves at least one value was missing from every shorter removed suffix. This establishes both feasibility and minimality.

**Trace `[3,1,5,4,2]` with `k = 2`.** Remove `2` first; it is required and new, so `count` becomes one. Values `4` and `5` are above `k` and do not change progress, though they consume the second and third operations. Removing `1` marks the other required value, making `count = 2`. Its index is one in an array of length five, so `n - i = 4` operations are returned.

The code uses a Boolean list instead of a hash set because required values occupy the compact known range `1..k`. This gives direct constant-time membership and avoids storing unrelated collected values.

**Reliance on the input guarantee.** The statement promises that collecting `1..k` is possible. Under that contract, the loop must reach `count == k` and return an integer. The function has no explicit return after the loop; if called with invalid data missing a required value, Python would return `None`. That behavior is acceptable only because the legal input guarantee rules the case out.

## Complexity detail

In the worst case, the necessary value farthest to the left is at index zero, so the loop examines all $n$ elements. Every iteration performs constant-time comparisons and a Boolean-array access. Time is $O(n)$.

The Boolean list has exactly $k$ entries, so auxiliary space is $O(k)$. All other variables use constant space. Since $k\le n$, this is also $O(n)$ in the broad worst case, but $O(k)$ states the tighter dependence. The input is not modified; the loop only simulates removals by reading in reverse.

## Alternatives and edge cases

- **Hash set:** Store required values seen in a set and stop when its size is $k$. This is correct but uses hashing where a compact Boolean array gives simpler direct indexing.
- **Physically popping elements:** Repeated `nums.pop()` also follows the operation order but unnecessarily mutates the input. Reverse indexing computes the same count.
- **Irrelevant values above `k`:** They do not change `count` but still contribute to the returned operation total.
- **Duplicate required values:** Only the first encountered copy changes progress; subsequent copies are skipped.
- **`k = 1`:** The scan stops at the first value one encountered from the right.
- **Required value at index zero:** Every element must be removed, and `n - 0` correctly returns `n`.
- **Immediate completion:** If the final $k$ relevant removals already cover all required values, the function stops without scanning unused prefix elements.
- **Invalid input outside the contract:** Missing required values would fall through with `None`; a defensive general-purpose version should return a sentinel or raise an error.
