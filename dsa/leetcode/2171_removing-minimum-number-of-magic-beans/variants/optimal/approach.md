## General

**Maximize what remains instead of minimizing what leaves**

The original total number of beans is fixed. If a plan leaves $K$ beans, it
removes the original total minus $K$. Minimizing removals is therefore
equivalent to maximizing retained beans.

Suppose the common positive amount is $x$. Every bag with fewer than $x$ beans
must be emptied because beans cannot be added. Every bag with at least $x$
beans can retain exactly $x$; retaining fewer would either empty it or violate
the common amount.

**An optimal amount equals an existing bag count**

For any chosen nonempty set of retained bags, $x$ cannot exceed its smallest
original count. Raising $x$ to exactly that smallest count keeps the same bags
feasible and never decreases the retained total. Consequently, some optimal
common amount is one of the values already in `beans`.

Sort the counts. If the value at index $i$ is selected as $x$, every earlier
bag is too small and must be emptied, while all $n-i$ bags in the suffix can
retain $x$. The retained total is

$$
\texttt{ordered[i]}\,(n-i).
$$

Evaluate that product at every index and keep its maximum.

**Recover the minimum removal count**

Each evaluated suffix describes an achievable plan: empty the prefix and
reduce every suffix bag to the candidate value. The previous argument shows
that every optimum has a candidate among these sorted values. Subtracting the
largest achievable retained total from the original total therefore gives the
minimum possible removals.

## Complexity detail

Sorting $n$ bag counts takes $O(n\log n)$ time, and the candidate scan takes
$O(n)$ time. The sorted copy uses $O(n)$ auxiliary space.

The benchmark defines `size` as the number of bags $n$. Its tiers contain
distinct, unsorted values, so all candidate amounts remain relevant. A correct
method that scans every bag separately for every distinct target takes
$O(n^2)$ time on the same inputs.

## Alternatives and edge cases

- **Enumerate every target with a full rescan:** Directly computes each
  candidate's removal cost and is a useful oracle, but takes $O(n^2)$ time
  when counts are distinct.
- **Frequency table over the bounded values:** Counts and suffix totals over
  the $10^5$ possible amounts can solve the problem without comparison
  sorting, but its fixed-domain work and larger table are less direct.
- A single bag requires no removal.
- Equal bag counts already satisfy the requirement with zero removals.
- Emptying every bag is legal but never better than retaining at least one
  positive bag.
- Several equal candidate counts may describe the same retained plan; checking
  each duplicate does not change the maximum.
- The total may exceed 32-bit integer range because both the bag count and
  number of bags can reach $10^5$.
