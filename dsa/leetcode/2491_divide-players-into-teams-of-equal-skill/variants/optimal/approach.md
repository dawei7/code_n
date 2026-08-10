## General

**Sorting reveals the only possible partner pattern**

Every team must contain two players, and every team must have the same total skill. After sorting `skill` in nondecreasing order, the smallest remaining skill is at the left end and the largest is at the right end.

If a valid division exists, those two extremes must be paired. To see why, suppose the smallest value $a$ were paired with some value $b$ smaller than the current maximum $d$. The maximum would need a partner $c$ that is at least $a$. Then

$$
d+c \ge d+a > b+a,
$$

so the maximum's team would have a larger sum than the smallest player's team. That contradicts the equal-sum requirement.

Therefore, pair the smallest with the largest, remove them, and repeat the same argument on the remaining sorted interval. This forces symmetric pairs from the two ends.

**Establish the required sum from the first pair**

The code sorts the list in place and defines

`t = skill[0] + skill[-1]`.

Since the extreme pair is forced in any valid division, its sum must be the common team sum. Every later symmetric pair must equal `t`. There is no need to guess or search for another target.

Pointers `i` and `j` begin at the first and last indices. While `i<j`, the method checks the current extreme pair. If its sum differs from `t`, no valid equal-sum division exists and it immediately returns `-1`.

If the sum matches, the pair's chemistry `skill[i]*skill[j]` is added to `ans`. Both pointers then move inward, ensuring each player is used exactly once.

Because the input length is even, the pointers meet between elements after exactly $n/2$ pairs. There is never an unpaired middle player.

**Why a failed symmetric pair proves impossibility**

The sorted-extremes argument applies at every stage, not only to the original minimum and maximum. Once outer pairs are fixed and removed, the remaining players still need to form teams with the same target `t`. Their smallest and largest remaining values must pair with each other.

If their sum is smaller than `t`, the smallest cannot obtain a larger partner because the current largest is already the largest available. If their sum is larger, the largest cannot obtain a smaller partner because the current smallest is already the smallest available. Either way, rearranging interior players cannot repair the mismatch.

Thus the early `-1` is logically conclusive.

**Why successful scanning constructs a valid division**

If every checked pair sums to `t`, the algorithm has partitioned all indices into disjoint pairs. Every player appears once because each pointer position is consumed once, and all pair sums are equal by the checks. This is exactly a valid team division.

The chemistry sum is computed at the same time. For each constructed team, its two skills are multiplied once and added. Hence `ans` is the requested total chemistry for that valid division.

Although duplicate skill values can make player identities interchangeable, they do not affect the chemistry result. Symmetric pairing still supplies a valid partition whenever one exists.

**Trace the sample**

Sorting `[3,2,5,1,3,4]` gives `[1,2,3,3,4,5]`. The target is $1+5=6$.

The pairs are $(1,5)$, $(2,4)$, and $(3,3)$. Each sum is six. Their products are 5, 8, and 9, so the method returns $5+8+9=22$.

For `[1,1,2,3]`, sorting gives the same sequence. The target from extremes is four, but the next pair is $(1,2)$ with sum three. Since those are the remaining extremes, no rearrangement can make both team sums four, and the method returns `-1`.

**Input mutation**

`skill.sort()` changes the caller-provided list. This is harmless under the challenge contract because only the returned chemistry is observed, but it is a practical detail worth stating in an interview. If the original order had to be preserved, sorting a copy would require explicit additional storage.

## Complexity detail

Let $n$ be the number of players. Python's sort takes $O(n\log n)$ time in the worst case. The two-pointer scan performs $n/2$ iterations, which is $O(n)$. Sorting dominates, so total time is $O(n\log n)$.

Python's in-place Timsort can use $O(n)$ auxiliary memory in the worst case. The pointers and accumulator use $O(1)$ additional space beyond the sort's workspace. This matches the manifest's $O(n)$ space bound.

The maximum chemistry sum can exceed 32-bit range: up to $n/2$ products may each be as large as $10^6$. Python integers handle this safely.

## Alternatives and edge cases

- **Frequency table:** Since skills are at most 1000, pair complementary values by counts in $O(n+U)$ time and $O(U)$ space, where $U=1000$. It avoids comparison sorting but requires careful handling of equal complements.
- **Hash-map counts:** Determine the common sum from total skill divided by the number of teams, then consume complements. It offers expected linear time but has more bookkeeping.
- **Two players:** They always form the sole team, and their product is returned.
- **Duplicate skills:** They represent different players and must be consumed with their full multiplicity.
- **Equal-skill pair:** When both endpoints have the same value, there must be an even number of remaining copies to pair.
- **Even length:** It guarantees no player remains after pointers move inward.
- **First target pair:** The global minimum and maximum are forced partners in any valid solution.
- **Early mismatch:** A failed remaining-extremes sum cannot be repaired by a different pairing.
- **Large chemistry:** Use a sufficiently wide integer type in fixed-width languages.
- **Mutation:** The exact implementation sorts the input list in place.
