## General

**Turn marking into a pairing problem**

Every operation consumes two previously unused indices. Within a pair, one value must be at most half the other:

$$
2\cdot\textit{small}\le\textit{large}.
$$

The objective is therefore to form as many disjoint valid small-large pairs as possible. If $p$ pairs are formed, exactly $2p$ indices are marked.

Sorting removes the importance of original positions because the condition depends only on values and any two distinct indices may be paired. It also makes it possible to greedily reserve small values for the left role and large values for the right role.

**Why only half the array can supply pairs**

No solution can contain more than $\lfloor n/2\rfloor$ pairs because each pair uses two indices. The code divides the sorted array conceptually into:

- a lower candidate region beginning at index $0$;
- an upper candidate region beginning at `(n + 1) // 2`.

The upper region contains exactly $\lfloor n/2\rfloor$ values. For even $n$, the two regions have equal length. For odd $n$, the lower region has one extra middle value, which may remain unmarked.

Any maximum pairing can be rearranged so that the smaller member of each pair comes from the lower region and the larger member comes from the upper region. If a supposedly small member lies in the upper half while some lower-half value is unused or used as a large member, replacing it with the no-larger lower value cannot break `2 * small <= large`. This exchange pushes small roles downward and large roles upward.

**The two-pointer greedy scan**

Pointer `i` identifies the smallest lower-region value not yet matched. The loop visits upper-region values `x` in ascending order.

If `2 * nums[i] <= x`, the pair is valid. The algorithm commits to it and increments `i`. The current upper value is consumed by the loop automatically, while the pointer moves to the next small candidate.

If the condition fails, `x` is too small even for the smallest unmatched lower value. It is therefore too small for every later lower candidate, because those values are at least `nums[i]`. The current `x` can never participate as the large side of a future pair, so skipping it loses nothing.

Notice that `i` does not advance on failure. A later, larger upper value may still match that same smallest candidate.

**Why matching immediately is safe**

Suppose current upper value $x$ can match the smallest remaining lower value $a$. Could saving $x$ for another value produce more pairs? Any later lower value $b$ satisfies $b\ge a$, so it is at least as difficult to match. Pairing $x$ with $a$ uses the weakest available large value for the easiest-to-match remaining small value.

If an optimal solution instead pairs $x$ with $b$ and pairs $a$ with some later upper value $y\ge x$, swap the two lower partners. Pair $(a,x)$ is valid because the greedy test succeeded. Pair $(b,y)$ remains valid because it was no harder for $y$ than the original arrangement after ordering; more generally, the sorted greedy matching theorem says assigning the earliest feasible large value to the earliest unmatched small value maximizes cardinality.

If $x$ was unused in an optimal solution, adding $(a,x)$ either increases the count or can replace the large member used with $a$ without reducing it. Thus accepting a feasible pair cannot lower the best achievable number of later pairs.

**Why every skipped value is hopeless**

When `2 * nums[i] > x`, $x$ fails against the smallest unmatched lower candidate. All other unmatched candidates are greater than or equal to that one, so doubling them produces an even larger requirement. No valid remaining pair can use $x$ as its large member.

It also cannot be repurposed as a small member in this construction because the lower half already contains enough no-larger candidates to support the maximum possible number of pairs. Moving an upper-half value into the small role would only make matching harder.

**Trace an example**

For `nums = [9,2,5,4]`, sorting produces `[2,4,5,9]`. The upper scan is `[5,9]`:

- smallest unmatched lower value is $2$; $2\cdot2\le5$, so pair $(2,5)$ and move `i` to one;
- next lower value is $4$; $2\cdot4\le9$, so pair $(4,9)$ and move `i` to two.

Two pairs mark four indices, which is the theoretical maximum for four elements.

For sorted `[6,7,8]`, the upper scan contains only $8$. It cannot match $6$ because $12>8$, so no pair exists and the answer is zero.

**Why the return value is twice `i`**

`i` starts at zero and increases exactly once per successful match. It therefore equals the number of disjoint pairs formed. Every pair marks two distinct indices, so `i * 2` is the number of marked indices.

The code sorts `nums` in place, changing the caller's order. It never needs to remember actual original indices because the output asks only for the maximum count.

## Complexity detail

Let $n$ be the array length. Sorting costs $O(n\log n)$ time. The upper-half slice and loop contain $\lfloor n/2\rfloor$ elements, so scanning is $O(n)$. Total time is $O(n\log n)$.

In Python, `nums[(n + 1) // 2:]` creates a new list containing the upper half, using $O(n)$ space. Timsort may also use $O(n)$ temporary memory. Thus the manifest's $O(n)$ space bound accurately covers the exact implementation. The sort mutates the input.

## Alternatives and edge cases

- **Binary search the number of pairs:** One can test whether $p$ pairs are possible and binary-search $p$, but the direct two-pointer scan finds the maximum in one pass after sorting.
- **Try every pairing:** Matching combinations grow exponentially and are unnecessary due to sorted monotonicity.
- **Pair adjacent sorted values:** Adjacent values may be too close in magnitude; small candidates need access to the large upper tail.
- **Odd length:** At most $n-1$ indices can be marked, and the lower candidate region intentionally has one extra value.
- **One element:** The upper slice is empty, `i` stays zero, and no index is marked.
- **Duplicate values:** Occurrences are distinct indices, but equal positive values cannot pair with each other because doubling one exceeds the other.
- **Very large values:** The condition may require wider arithmetic in fixed-width languages; Python integers do not overflow.
- **All pairs feasible:** `i` reaches $\lfloor n/2\rfloor$, and the answer is the largest even number not exceeding $n$.
- **Input mutation:** Sort a copy if the original order must be preserved.
