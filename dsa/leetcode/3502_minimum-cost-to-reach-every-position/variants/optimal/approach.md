## General

**One paid jump can unlock a suffix of target positions.** You begin behind everyone at position $n$. Swapping with person $j$ in front costs `cost[j]` and moves you to position $j$.

After that swap, every position with index greater than or equal to $j$ lies behind your new position in the line's movement model. People behind you can swap for free, so you can reach any target position $i\ge j$ without paying again.

Therefore, to reach target $i$, it is sufficient to choose one paid swap with any person $j$ satisfying $0\le j\le i$, then use free swaps to move back to $i$. The cost of that strategy is `cost[j]`.

**The answer is a prefix minimum.** Among all valid paid entry positions for target $i$, choose the cheapest:

$$
\texttt{answer}[i]
=
\min_{0\le j\le i}\texttt{cost}[j].
$$

The source scans from left to right and stores this running minimum in `mi`.

It initializes `mi = cost[0]`. At index `i` with current price `c`, update

`mi = min(mi, c)`.

After that assignment, `mi` equals the smallest cost among indices zero through $i$. Writing `ans[i] = mi` records exactly the formula above.

For `cost = [5,3,4,1,3,2]`, running minima are $5,3,3,1,1,1$. To reach position two, paying person one costs three and person two can then swap from behind for free. To reach position five, paying person three costs one and free swaps cover the rest.

For strictly increasing `[1,2,4,6,7]`, person zero is always the cheapest eligible paid swap. Once position zero is reached for cost one, every requested position can be reached through free behind swaps, so every answer is one.

**Why multiple paid swaps cannot improve the result.** All costs are positive. Any route reaching $i$ must at some point perform a paid swap with a person in front far enough to enter position $j\le i$; before that, you cannot obtain the free-behind access needed for $i$.

That one payment already costs at least the prefix minimum. Additional paid swaps add nonnegative cost and cannot reduce what was paid. Conversely, the prefix-minimum person provides a one-payment construction. Thus one paid swap is always optimal.

**Why indices after \(i\) are not candidates.** Paying a person at $j>i$ leaves target $i$ still in front rather than behind, so reaching $i$ would require another paid swap. Directly paying some eligible prefix person is no more expensive than retaining that extra positive payment in an optimal route. The minimum can be restricted to $j\le i$.
Before processing index $i$, `mi` is the minimum cost through $i-1$. Taking the minimum with `cost[i]` extends it to the prefix through $i$. The reachability argument proves that this prefix minimum is both a lower bound on any strategy and attainable by paying its corresponding person followed by free swaps. Therefore, every written answer is optimal.

The output positions are independent questions about the original line. The method computes costs but does not simulate or persist swaps from one answer to the next.

## Complexity detail

The loop visits each of the $n$ prices once and performs a constant-time comparison and assignment. Time complexity is $O(n)$.

The returned `ans` array contains $n$ required outputs, so total result storage is $O(n)$, matching the manifest. Excluding required output, the algorithm uses only scalar `mi`, index, and current cost, so auxiliary working space is $O(1)$.

The $O(n)$ time is optimal because every `cost[i]` can become a new prefix minimum and alter answers from that position onward.

## Alternatives and edge cases

- **Simulate swaps for every target:** This repeats line-state work and can become quadratic, while reachability depends only on one cheapest prefix payment.
- **Dynamic programming over positions:** The transition collapses to a running minimum; a full table is unnecessary.
- **Use suffix minima:** A person after target $i$ does not directly unlock $i$ for free, so the relevant range is the prefix.
- **Add several swap costs:** One paid jump followed by free behind swaps is always sufficient; positive extra payments cannot help.
- **First position:** Only person zero is an eligible one-payment choice, so answer zero is `cost[0]`.
- **New cheaper cost:** Once encountered, it becomes the answer for that and every later position unless an even cheaper value appears.
- **Strictly increasing costs:** The first value remains every prefix minimum.
- **Strictly decreasing costs:** Each current position's own cost becomes its answer.
- **Duplicate minimum costs:** Any occurrence attaining the same prefix minimum yields an equally cheap route.
- **Single-element array:** The loop writes the only cost, which is the sole possible paid swap.
- **Positive-cost guarantee:** It supports the argument that extra paid swaps cannot reduce total cost.
- **Independent outputs:** The source does not mutate `cost` or share a performed swap sequence between targets.
