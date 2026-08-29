## General

**Reduce the distance to an outer-occurrence span**

Place the three distinct selected indices in increasing order `i<j<k`. The absolute values then simplify:

$$
|i-j|+|j-k|+|k-i|
=(j-i)+(k-j)+(k-i)
=2(k-i).
$$

The middle occurrence establishes that three copies exist, but its exact position disappears from the final expression. Minimizing distance means finding three equal-value occurrences whose first-to-third span is smallest.

**Collect sorted positions for each value**

During one left-to-right scan, `g[x]` receives every index where value `x` occurs. Appending in enumeration order makes each occurrence list sorted automatically, with no separate sorting cost.

This grouping prevents comparisons between unequal values. Every three positions from one list form a good tuple, while positions from different lists never do.

**Why consecutive occurrence windows suffice**

Let one value's positions be

$$
p_0<p_1<\cdots<p_{t-1}.
$$

Suppose a selected triple uses list positions `a<b<c`. Because three positions are required, `c>=a+2`. For the same first occurrence `p_a`, the earliest possible third occurrence is `p_{a+2}`, and

$$
p_{a+2}-p_a\le p_c-p_a.
$$

Thus the consecutive triple beginning at `a` has no larger distance than the arbitrary triple. If a global optimum skipped an occurrence, a consecutive window exists that matches or improves it.

The source checks every `h` from zero through `len(ls)-3` and evaluates the outer positions `ls[h]` and `ls[h+2]`. It need not read `ls[h+1]` because list ordering guarantees it is the distinct middle occurrence.

For example, occurrences `[1,4,5,9,12]` create windows with outer spans four, five, and seven: `(1,4,5)`, `(4,5,9)`, and `(5,9,12)`. A skipped triple such as `(1,5,9)` has span eight and cannot beat the window starting at one. The smallest window distance is twice four, or eight.

**Why all candidates are valid and complete**

Every evaluated pair of outer positions belongs to a list containing the intervening occurrence at `h+1`, so it defines three distinct equal-valued indices. Multiplying the span by two gives the original distance exactly.

The consecutive-window lemma shows that every arbitrary good tuple has an evaluated window with no greater distance. Therefore the smallest evaluated value is the global minimum.

The infinity sentinel distinguishes “no candidate yet” from a real distance. If every occurrence list has length below three, no inner iteration executes and the method returns `-1`. Any finite update proves a good tuple exists.

For positions `[0,2,3,10]`, the source checks spans three and eight, corresponding to distances six and sixteen. A nonconsecutive triple such as `[0,2,10]` has span ten and cannot improve the consecutive windows.

**Why this scales to the larger constraint**

The “II” version allows `10^5` elements, so cubic endpoint enumeration is impossible. Occurrence lists compress the relevant comparisons: an index is stored once, and each adjacent length-three window is processed once.

The manifest summary mentions tracking the latest two indices, which could be implemented in a streaming manner. The exact source instead stores full occurrence lists and scans them afterward. Both ideas evaluate the same consecutive triples, but this document follows the actual list-based code.

Storing full lists also makes the separation of concerns clear: the first pass groups and orders occurrences, and the second pass evaluates geometry. No list is sorted afterward because insertion order already follows increasing array indices.

## Complexity detail

Let `n` be the array length. The first scan performs one expected constant-time dictionary lookup and one append per index, totaling expected $O(n)$ time.

If list lengths are `t_1,t_2,\ldots`, then

$$
\sum t_i=n.
$$

Each list contributes at most `t_i-2` windows, so the total window count is $O(n)$. Overall expected time is $O(n)$.

The dictionary and lists store each input index exactly once, using $O(n)$ auxiliary space. The infinity sentinel and loop variables use constant additional space.

## Alternatives and edge cases

- **Cubic triplet enumeration:** It directly tests the definition but is infeasible at `n=10^5`.
- **Successor array:** Linking each occurrence to its next occurrence also permits checking the next two positions in $O(n)$ time. The exact source uses grouped lists instead.
- **Keep only the latest two positions online:** On seeing a third occurrence, evaluate its span with the occurrence two steps back. This reduces stored history per value but is not the shown implementation.
- **Evaluate nonconsecutive triples:** They cannot beat a consecutive window because moving the third occurrence earlier or first later shrinks the span.
- **Value appears fewer than three times:** It contributes no candidate.
- **Value appears exactly three times:** Its sole triple is checked.
- **Dense equal run:** Three adjacent indices yield distance four, the smallest possible for distinct integer indices.
- **Ties between values:** Only the distance is returned, so equal minima need no tie-breaking.
- **Order of tuple components:** Absolute pairwise distance is symmetric; sorting indices for analysis changes nothing.
- **Large answer:** The maximum finite distance is below `2n`, but the infinity sentinel cleanly handles absence.
- **Hash behavior:** Dictionary grouping gives expected linear time; values themselves need no bounded-array indexing.
