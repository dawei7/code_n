## General

**A valid move is bounded by opposite non-enemy markers**

Array values mean:

- `1` is one of your forts;
- `0` is an enemy fort;
- `-1` is an empty position that can be the destination.

To move legally, one endpoint must be `1` and the other `-1`, while every position strictly between them must be zero. The number captured is exactly the length of that consecutive zero run.

The army may move left or right, so endpoint order can be either `1,...,-1` or `-1,...,1`.

**Only consecutive nonzero boundaries matter**

Ignore zeroes temporarily and look at the nonzero markers in array order. A valid move can occur only between two consecutive such markers.

If another `1` or `-1` lay between the chosen endpoints, then an intermediate position would not be an enemy fort, violating the rule that every crossed position is zero.

Conversely, the interval between consecutive nonzero markers contains only zeroes by definition. It is valid exactly when the marker values are opposite.

The algorithm scans precisely these consecutive boundary pairs.

**Start at a nonzero boundary and skip its zero run**

At index `i`, the condition `if forts[i]` is true for both 1 and $-1$, and false for zero.

When `forts[i]` is nonzero, `j` advances while `forts[j]==0`. At loop end:

- either `j==n` and the zero run reaches the array boundary with no destination marker;
- or `j` is the next nonzero marker after `i`.

The number of zeroes strictly between them is `j-i-1`.

**Check that the markers are opposite**

Allowed nonzero values are only 1 and $-1$. They are opposite exactly when their sum is zero:

`forts[i]+forts[j]==0`.

This compact condition accepts both directions:

- $1+(-1)=0$;
- $(-1)+1=0$.

It rejects two owned forts and two empty positions.

For an opposite pair, `ans` is updated with the zero-run length. Keeping a maximum considers every legal army move and retains the greatest number of captured enemy forts.

**Advance without repeating work**

After processing the run, `i=j`. If `j` is a nonzero marker, it becomes the left boundary for the next run. If `j==n`, the outer loop ends.

When `forts[i]==0`, the guarded scan is skipped and `i` advances by one through `j=i+1`. This is how leading zeroes are passed until the first real boundary appears.

Across the entire method, a zero inside a run is advanced over once by the inner loop. The jump `i=j` prevents rescanning that run in the outer loop.

**Trace the first sample**

For `[1,0,0,-1,0,0,0,0,1]`:

- boundary 1 at index 0 and boundary $-1$ at index 3 enclose two zeroes, so capture count two;
- boundary $-1$ at index 3 and boundary 1 at index 8 enclose four zeroes, so capture count four.

The maximum is four.

Although the second interval is written left-to-right as empty-to-owned, it represents moving the army from index 8 leftward to index 3. The sum-zero test handles this without reversing the array.

**Why trailing or leading enemy forts cannot be captured alone**

A run of zeroes at an array end has only one nonzero boundary, so it cannot have both a starting owned fort and an empty destination. The scan either walks past leading zeroes or reaches `j==n` for trailing zeroes and does not update the answer.

**Adjacent opposite markers**

If `1` and `-1` are adjacent, the interval contains zero enemy forts. The candidate length is zero. Such a movement is legal but does not improve the initialized answer zero.


Every valid move's endpoints are consecutive nonzero markers, and the scan inspects that pair when `i` reaches the first endpoint. Their opposite values pass the sum test, and the exact number of intervening zeroes is considered.

Every candidate accepted by the scan has opposite required endpoint types and only zeroes in between, so it describes a legal move. Taking the maximum over exactly all legal intervals returns the desired capture count.

If no such interval exists or there is no owned fort, `ans` is never raised and zero is returned.

## Complexity detail

Let $n$ be the array length. Although there is a nested `while`, indices move only forward. Every position is passed a constant number of times, so total time is $O(n)$ rather than $O(n^2)$.

Only `n`, `i`, `j`, and `ans` are stored. Auxiliary space is $O(1)$.

The maximum answer is at most $n-2$ and easily fits ordinary integer types.

## Alternatives and edge cases

- **Track last nonzero index:** In one simple `for` loop, compare each new nonzero marker with the previous one and measure their gap.
- **Brute-force endpoint pairs:** It repeats zero-run checks and can cost $O(n^2)$.
- **No owned fort:** No move can begin, so return zero.
- **No empty position:** No legal destination exists.
- **Leading or trailing zeroes:** They lack two bounding markers and cannot form a move.
- **Same-type boundaries:** `1...1` and `-1...-1` are invalid.
- **Opposite adjacent boundaries:** They capture zero enemy forts.
- **Movement direction:** Both leftward and rightward moves are accepted by the same sum-zero test.
- **Consecutive nonzero requirement:** Any intervening marker would violate the all-zero interior rule.
- **Nested-loop appearance:** Forward jumps ensure linear total work.
