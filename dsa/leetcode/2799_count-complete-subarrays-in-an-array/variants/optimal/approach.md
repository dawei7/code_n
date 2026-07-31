## General

**Turn equal distinct counts into set coverage**

Let $k$ be the number of distinct values in the whole array. A subarray cannot introduce a value absent from `nums`, so a window with $k$ distinct values necessarily contains every required value. Compute $k$ once, then maintain a frequency map for a window `[left, right]`.

Move `right` from left to right and increment the incoming value's frequency. Once the map contains $k$ keys, the current window is complete. Every extension ending at `right`, `right + 1`, through `n - 1` remains complete because adding elements cannot remove a required value. Thus this one window start contributes `n - right` complete subarrays.

**Enumerate every valid start without enumerating every end**

After adding that contribution, remove `nums[left]` and advance `left`. If its frequency reaches zero, delete the key. Continue shrinking while all $k$ keys remain. Each iteration counts a different left endpoint, paired with every valid right extension, so no subarray is duplicated.

When shrinking removes a required value, the window is no longer complete. Advancing `right` resumes until coverage is restored. The left and right pointers only move forward, and the frequency map exactly represents their current window. Therefore every complete subarray is counted when its earliest complete right boundary is reached, and incomplete subarrays are never counted.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$ and let $k$ be the number of distinct values in `nums`. Each element enters the window once and leaves it at most once, giving $O(n)$ expected time under standard hash-map behavior. The whole-array set and window frequency map store at most $k$ keys, so the auxiliary space is $O(k)$.

The three legal benchmark tiers use all-distinct arrays. The sliding window remains linear, while a correct enumeration that grows a distinct set for every left endpoint performs $n(n+1)/2$ insertions and fails only the scaling verdict.

## Alternatives and edge cases

- **Enumerate every subarray:** Growing a set for every left endpoint is correct but takes $O(n^2)$ time even when set insertion is expected constant time.
- **Exactly-$k$ via two at-most counts:** Counting subarrays with at most $k$ distinct values minus those with at most $k-1$ is also linear, but it runs two window passes and is less direct here because no subarray can exceed the whole array's $k$ values.
- **Frequency array:** Since values are at most $2000$, an indexed count array can replace the hash map at the cost of fixed domain-sized storage.
- With one distinct value, every non-empty subarray is complete, producing $n(n+1)/2$.
- With all values distinct, only the entire array is complete.
- Repeated occurrences must keep a key present until its frequency actually becomes zero.
- The answer counts index intervals, so equal-looking subarrays at different positions are distinct choices.
