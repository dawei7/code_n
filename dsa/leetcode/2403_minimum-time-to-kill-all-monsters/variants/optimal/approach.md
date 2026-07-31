## General

**A chosen order fixes every waiting time.** Immediately after a kill, mana is
zero. If $c$ monsters have already been defeated, gain is $c+1$. Defeating a
remaining monster of power $p$ next therefore requires exactly

$$
\left\lceil\frac{p}{c+1}\right\rceil
$$

additional days. Waiting longer than this before the kill cannot help a later
monster because mana is reset, so an optimal schedule kills each chosen
monster on the first sufficient day.

**The killed subset contains all relevant history.** Encode defeated monsters
in a bitmask. For a mask with $c$ set bits, the next gain is always $c+1$
regardless of the order that produced the mask. Let `minimum_days[mask]` be
the least elapsed time to reach that exact killed set.

**Choose the next monster.** From each mask, try every unset monster bit. Add
`(power[i] + gain - 1) // gain`, the integer form of the ceiling, and minimize
the destination state. The empty mask begins at zero days; the full mask is
the answer.

Every monster order corresponds to one path from the empty mask to the full
mask, and each transition contributes exactly that order's necessary waiting
time. Conversely, each DP path is a legal kill order. Minimizing all incoming
paths to every subset and then the full subset therefore finds the globally
minimum schedule.

## Complexity detail

There are $2^n$ masks. Across all masks, each of the $n$ monster bits is unset
in exactly half the masks, so there are $n2^{n-1}$ transitions. Time is
$O(n2^n)$. The dynamic-programming array contains one value per mask and uses
$O(2^n)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate permutations:** Evaluating all $n!$ kill orders is correct but
  repeats equivalent killed subsets and grows much faster.
- **Memoized recursion:** The same subset recurrence can be evaluated
  top-down; it has identical asymptotic bounds but adds recursion overhead.
- **Greedy by smallest power:** Killing an easy monster raises gain quickly,
  but a locally smallest power need not minimize later ceiling costs.
- **Greedy by largest power:** Spending low gain on the hardest monster can
  waste many days and is likewise not generally optimal.
- **Ceiling division:** A monster whose power is not divisible by gain needs
  one additional whole day; ordinary floor division would undercount.
- **Duplicate powers:** Monsters remain distinct bits even when their powers
  match, because every kill separately increases gain.
- **Single monster:** Gain never changes before its kill, so the answer equals
  its power.
- **Large result:** Power values up to $10^9$ require 64-bit result storage in
  fixed-width languages.
