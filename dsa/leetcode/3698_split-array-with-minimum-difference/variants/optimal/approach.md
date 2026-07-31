## General

The indices that can end a strictly increasing prefix form one contiguous range. Starting from index `0`, advance while each adjacent pair satisfies `nums[i] < nums[i + 1]`; let `increasing_end` be the final reachable index. A left part ending after that point is invalid.

Likewise, the valid starting indices of strictly decreasing suffixes form a contiguous range ending at the array's right boundary. Scan leftward while `nums[i - 1] > nums[i]` and record the earliest `decreasing_start`. A right part beginning before that point is invalid.

**Intersect the two boundary conditions.** A split after index $i$ is valid exactly when $i\le\texttt{increasing\_end}$ and $i+1\ge\texttt{decreasing\_start}$. These conditions are necessary by construction. They are sufficient because they select a prefix contained in the verified increasing run and a suffix contained in the verified decreasing run.

Compute the total array sum once and maintain the prefix sum while scanning split indices. For a left sum $L$ and total $T$, the absolute difference is $\lvert L-(T-L)\rvert=\lvert2L-T\rvert$. Minimize it over the valid boundary interval; if that interval contains no legal split between two nonempty parts, return `-1`.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. The two boundary scans, total sum, and split scan each take $O(n)$ time. Only indices, sums, and the current answer are retained, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Validate both subarrays for every split:** Rechecking monotonicity and recomputing sums repeats overlapping work and can take $O(n^2)$ time.
- **Prefix/suffix Boolean arrays:** Precomputing validity and sums gives $O(n)$ time but consumes $O(n)$ space that the boundary structure makes unnecessary.
- **Singleton parts:** A one-element subarray is both strictly increasing and strictly decreasing, so splits next to either endpoint may be valid.
- **Equal adjacent values:** Equality violates both strict conditions wherever that adjacent pair lies inside a candidate part.
- **Relation across the split:** No ordering condition compares `nums[i]` with `nums[i + 1]`; each belongs to a different subarray.
- **No overlap:** When no boundary satisfies both run limits, the required sentinel is `-1`.
