## General

**Intervals remain the right subproblems despite shifting**

Removing a subarray makes surviving elements move together, which may seem to destroy original indices. Interval dynamic programming handles this by asking only about elements originally between two boundaries.

`f[i][j]` is the minimum number of moves needed to remove all values from original inclusive interval `arr[i:j+1]`. Removals inside the interval may create new adjacencies, and the recurrence accounts for them.

**Base cases**

A one-element interval is itself a palindrome, so `f[i][i] = 1`.

For two adjacent values:

- if they are equal, the pair is a palindrome and needs one move;
- otherwise, each must be removed separately, needing two moves.

The source handles this length-two case explicitly because the later endpoint-merging recurrence refers to a nonempty interior.

**Always-valid split transitions**

For any cut position `k` between `i` and `j - 1`, one valid strategy is:

1. remove interval `[i,k]` optimally;
2. remove interval `[k+1,j]` optimally.

This costs `f[i][k] + f[k + 1][j]`. Trying every `k` covers every possible way to separate the work into two independent original intervals.

The variable `t` keeps the minimum among these split costs and the special equal-endpoint candidate.

**Why equal endpoints can be removed without an extra move**

If `arr[i] == arr[j]` and the interval has at least three elements, the code initializes:

`t = f[i + 1][j - 1]`.

At first this may look one move too small: after removing the interior, do the endpoints not still need removal? The key is to merge the equal endpoints into the final interior move.

Take an optimal sequence that removes the interior. Just before its last move, the remaining interior elements selected by that move form a palindrome \(P\). The two untouched equal endpoints now surround that remaining interior. If their value is \(x\), then \(xPx\) is also a palindrome. Expand the final interior removal to include both endpoints. The number of moves remains exactly the interior count.

For `[1,2,1]`, the interior `[2]` takes one move. Expanding that move removes `[1,2,1]` as one palindrome. For `[1,3,4,1]`, the equal endpoints may still help even if the entire original interval is not visibly palindromic after other removals.

**Why interval lengths are processed in the correct order**

The outer loop moves `i` from right to left, and the inner loop moves `j` from `i + 1` rightward. Every needed state is smaller:

- `f[i + 1][j - 1]` lies in a later row;
- `f[i][k]` has a smaller right endpoint already completed in the current row;
- `f[k + 1][j]` has a larger left endpoint completed in an earlier outer iteration.

Thus every recurrence reads finalized values.

**Why the recurrence is complete**

An optimal removal schedule for `[i,j]` either uses the equal endpoints together in one move at some stage or does not.

If they are used together, they must be equal, and restricting the schedule to the interior shows that the equal-endpoint merge candidate captures the possible saving.

If they are not removed together, the sequence can be separated across a boundary between groups whose removals do not rely on pairing those two endpoints. One of the tested split positions captures its total cost. Taking the minimum over the merge and all splits therefore finds an optimal schedule.

Another practical view is that split transitions alone can remove anything, while the equal-endpoint transition captures exactly the useful cross-boundary interaction created by shifting.

**Following `[1,3,4,1,5]`**

For interval `[1,3,4,1]`, matching endpoints allow the interior cost for `[3,4]`, which is two. One realization removes 4, then removes `[1,3,1]`, for two moves.

The final 5 can be removed in a separate move through a split, bringing the whole array’s optimum to three.

**Sentinel infinity**

When endpoints differ, the merge is illegal. The source initializes `t = inf` so the split loop must supply the result. Since every interval can always be removed as singletons, at least one finite split exists.

## Complexity detail

Let \(n=\lvert\texttt{arr}\rvert\). There are \(O(n^2)\) interval states. Each state may try \(O(n)\) split points, so time complexity is \(O(n^3)\).

The \(n\)-by-\(n\) table uses \(O(n^2)\) auxiliary space. Loop variables and `inf` use constant additional space. The input is not modified.

## Alternatives and edge cases

- **Top-down memoization:** Use the same interval recurrence recursively. It computes only reached states but still has \(O(n^3)\) worst-case time and \(O(n^2)\) cache space.
- **Remove singletons greedily:** This is always valid but can miss large savings created when equal values become adjacent.
- **Whole array already palindromic:** Repeated endpoint merging propagates a result of one.
- **One element:** The diagonal base case returns one.
- **Two equal elements:** The explicit length-two base returns one.
- **Two different elements:** Neither can join the other in a palindromic pair, so the base returns two.
- **Equal values becoming adjacent later:** This is the core reason ordinary substring checks are insufficient; interval DP models adjacency after interior removals.
- **Repeated values:** Multiple split and merge possibilities are compared, so no pairing is chosen greedily.
- **Required infinity import:** Standalone Python code needs `inf` from `math` or another sufficiently large sentinel.
- **Nonempty input:** The return `f[0][n - 1]` assumes at least one element, which the contract guarantees.
