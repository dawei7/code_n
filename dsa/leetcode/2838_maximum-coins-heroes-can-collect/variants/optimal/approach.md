## General

**Turn each answer into a power threshold**

For a hero with power $h$, every eligible monster satisfies $\texttt{monsters[j]} \le h$. Because every coin reward is positive and fighting does not reduce health, there is never a reason to skip an eligible monster. The answer is therefore the sum of all rewards whose associated monster power lies at or below one threshold.

Computing that sum independently for every hero repeats the same comparisons. Instead, pair each monster power with its reward and sort those pairs by power. Also sort `(hero power, original index)` pairs. The original index is retained because the returned answers must follow the input order rather than sorted power order.

**Sweep increasing hero powers**

Maintain `monster_index` at the first monster pair not yet consumed and `collected` as the sum of rewards before that pointer. For the current hero power, advance the pointer while the next monster power is no greater than the hero's power, adding each reward exactly once. Store the resulting total at that hero's original index.

When the next hero is processed, its power is at least the preceding hero's power. Every monster already included remains defeatable, so the pointer and sum never need to move backward. Monsters newly crossed by the threshold are added exactly once. Thus, after the inner loop, `collected` contains precisely the reward of every monster the current hero can defeat. Assigning that value through the saved original index proves every output entry is correct and properly ordered.

Duplicate hero powers naturally receive the same total. Duplicate monster powers are adjacent after sorting and are all included when that power first becomes reachable.

## Complexity detail

Let $n$ be the number of heroes and $m$ the number of monsters. Sorting the heroes costs $O(n\log n)$ and sorting the monster-reward pairs costs $O(m\log m)$. The sweep advances each pointer only forward, adding $O(n+m)$ work, so the total time is $O(n\log n+m\log m)$. The sorted pairs, sorted hero records, and output use $O(n+m)$ space.

The benchmark defines `size` as $n+m$ and keeps $n=m$. It permutes both power orders so the sorting terms remain exercised. The optimal sweep processes each sorted record once, while the calibration alternative scans all $m$ monsters independently for every hero and therefore requires $O(nm)$ time. That slower implementation completes all three legal tiers and returns identical outputs, but fails the scaling verdict.

## Alternatives and edge cases

- **Prefix sums plus binary search:** Sort monsters, build cumulative rewards, and binary-search the last defeatable power for each hero. This also runs in $O(m\log m+n\log m)$ time and uses $O(m+n)$ space.
- **Independent monster scan:** Test every monster for every hero and sum eligible rewards. It is correct but needs $O(nm)$ time at the maximum constraints.
- **Power-to-reward map:** Aggregating equal monster powers first can reduce duplicate records, but those distinct powers still need sorting or an ordered structure.
- **No defeatable monsters:** If the smallest monster is stronger than a hero, the untouched running total correctly contributes zero.
- **Every monster defeatable:** A sufficiently powerful hero receives the sum of all rewards.
- **Equal thresholds:** The comparison is inclusive, so monsters with power exactly equal to the hero's power must be counted.
- **Duplicate powers:** Every monster is a separate reward source even when several monsters share one power.
- **Duplicate heroes:** Heroes act independently and may collect the same monster rewards, so equal hero powers yield equal totals.
- **Large totals:** Up to $10^5$ rewards of $10^9$ coins may be summed, requiring an integer representation that safely holds values above 32-bit range.
