## General

An ordered partition is determined by choosing which indexed elements enter the first group; every other element enters the second. There are therefore $2^n$ assignments before applying the sum requirements.

If the total array sum is below $2k$, the two groups cannot both reach `k`, so the answer is zero. Otherwise, call a group bad when its sum is strictly less than `k`. The two groups cannot both be bad, because their combined sum is at least $2k$. This makes complementary counting especially simple: count assignments whose first group is bad, double that count for the symmetric case where the second group is bad, and subtract from $2^n$.

Count bad first groups with 0/1 knapsack. Let `ways_by_sum[s]` be the number of subsets of processed indices whose values sum exactly to `s`, retaining only states $0 \le s < k$. Initialize the empty subset at sum zero. For each value, update subtotals downward so that the current index is used at most once. Values at least `k` require no update because adding one can never create a retained bad sum.

After all elements, summing the DP states counts every indexed subset with sum below `k`. Each corresponds to exactly one ordered assignment with a bad first group. Since the two bad orientations are disjoint when the total is at least $2k$, the required result is $2^n - 2B$ modulo $10^9 + 7$, where $B$ is that DP sum.

## Complexity detail

Let $n$ be the length of `nums`. There are `k` retained subtotal states, and each of the $n$ values updates at most all of them, so the time complexity is $O(nk)$. The one-dimensional DP array uses $O(k)$ auxiliary space. Modular reduction keeps every stored count bounded.

## Alternatives and edge cases

- **Enumerate all assignments:** Evaluating every subset directly is conceptually simple but takes $O(2^n)$ time and cannot support $n$ up to $1000$.
- **Two-dimensional knapsack:** A table indexed by both processed elements and subtotal is correct but uses $O(nk)$ space; descending updates compress it to one row.
- If the total sum is less than $2k$, no great partition exists regardless of individual values.
- Equal values at different indices are separate choices and must contribute separately to the DP counts.
- A one-element array always returns zero because positive `k` requires both groups to contain positive sum.
