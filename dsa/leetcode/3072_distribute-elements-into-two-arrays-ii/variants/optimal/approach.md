## General

**Turn large values into compact ranks.** The values can be as large as $10^9$, but only their relative order matters to `greaterCount`. Sort the distinct values and map them to ranks from $1$ through $m$, where $m$ is the number of distinct values. Equal values receive the same rank, which is essential because the comparison is strictly greater.

**Maintain one frequency structure per destination.** A Fenwick tree stores how many values of each rank have been appended to its array. A prefix query through the current value's rank counts elements less than or equal to that value. Therefore, if an array currently has length $L$, its required count is

$$
\operatorname{greaterCount}(\texttt{arr}, x) = L - \operatorname{prefixCount}(\operatorname{rank}(x)).
$$

Both the prefix query and the insertion of a new rank take logarithmic time.

**Apply the decision hierarchy exactly.** Seed `arr1` with `nums[0]` and `arr2` with `nums[1]`, inserting those values into their respective trees. For every remaining value, query both greater counts before modifying either structure. Choose `arr1` when its count is larger. If the counts tie, choose `arr1` exactly when its length is no larger than `arr2`; this combines the shorter-array rule with the final `arr1` tie-break. Otherwise choose `arr2`. Append the value and update only the chosen tree.

At every iteration, each Fenwick tree contains precisely the frequencies of the values already appended to its corresponding array. The prefix identity therefore produces the exact strictly-greater counts required by the rule. Since the algorithm then follows all three comparison and tie-breaking levels without changing either array's append order, every placement matches the prescribed process; concatenating the two arrays gives the required result.

## Complexity detail

Let $n$ be the length of `nums`. Sorting the distinct values for coordinate compression takes $O(n \log n)$ time. Each of the $n$ values is queried or inserted a constant number of times at $O(\log n)$ per operation, so the total time is $O(n \log n)$. The rank map, two Fenwick trees, and two destination arrays use $O(n)$ space in total.

## Alternatives and edge cases

- **Segment tree:** A segment tree supports the same frequency queries and insertions in $O(\log n)$ time, but uses a larger structure and more implementation machinery than a Fenwick tree.
- **Sorted destination arrays:** Binary search can find each greater count, but inserting into a Python list can shift $O(n)$ elements, making the complete process $O(n^2)$.
- **Direct scanning:** Counting greater elements by scanning both destination arrays is easy to express but takes $O(n^2)$ time in the worst case and cannot handle $n=10^5$.
- **Strict comparison:** The prefix query includes the current rank, so subtracting it from the array length excludes equal values and counts only values that are strictly greater.
- **Count tie before length tie:** Array lengths matter only when the greater counts are equal; a shorter array must not override a larger greater count.
- **Complete tie:** When both counts and lengths match, the value goes to `arr1`, represented by the condition `len(first) <= len(second)`.
- **Duplicate values:** Coordinate compression maps duplicates to one rank while the Fenwick frequency preserves their multiplicity.
- **Output order:** The final answer is `arr1 + arr2`; sorting the destination arrays to support queries would destroy their required append order unless separate output arrays were retained.
