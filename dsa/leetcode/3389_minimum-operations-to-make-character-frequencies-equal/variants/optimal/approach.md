## General

**Choose the common positive frequency.** In a good string, every alphabet frequency is either zero or one shared positive value $k$. It is sufficient to try $1 \le k \le F$, where $F$ is the largest original frequency: choosing a value above $F$ only adds insertions, and lowering it to $F$ cannot make any chosen character more expensive. Deleting every character gives an initial upper bound of $n$.

For a letter with frequency $a$, handling it without a change to the next letter costs

$$
\min\bigl(a,\lvert a-k\rvert\bigr),
$$

corresponding to removing that letter entirely or making its frequency $k$ with insertions/deletions.

**Price an adjacent pair.** Suppose adjacent letters have frequencies $a$ and $b$, with chosen goals $x,y \in \{0,k\}$. Editing them independently costs $\lvert a-x\rvert+\lvert b-y\rvert$. If the first has surplus and the second has deficit, changing one first-letter occurrence into the next letter replaces one deletion plus one insertion with one operation. The saving is

$$
\min\bigl(\max(a-x,0),\max(y-b,0)\bigr).
$$

Take the best of the four goal pairs. It is never necessary for an optimal plan to use changes across two consecutive alphabet boundaries: forwarding a character twice costs two operations, exactly the same as deleting it at the source and inserting it at the final letter. Therefore useful change edges can be selected as disjoint adjacent pairs.

For fixed $k$, run a prefix DP over the 26 letters. From each alphabet position, either pay its individual cost and advance one letter, or pay the best adjacent-pair cost and advance two. This considers every valid set of non-overlapping useful changes. Minimize the completed DP value over all $k$.

The pair formula realizes the maximum possible one-operation savings for its chosen goals; no additional transfer can help after either the surplus or deficit is exhausted. The non-overlap observation converts every optimal plan into a tiling by single letters and adjacent pairs, exactly the choices made by the DP. Trying every possible $k$ therefore finds a globally optimal good frequency vector and edit plan.

## Complexity detail

Let $n=\lvert s\rvert$, let $\sigma=26$, and let $F$ be the maximum character frequency. Counting takes $O(n)$ time. There are $F \le n$ target values, and each performs constant work for every alphabet letter, so the total is $O(n+\sigma F)=O(n)$ for the fixed lowercase alphabet. The frequency and DP arrays use $O(\sigma)=O(1)$ auxiliary space.

The benchmark defines `size` as $n$ and uses single-letter strings of lengths 24, 60, and 120, making $F=n$. The reference counts once and then performs constant alphabet work per target. A correct slower baseline counts each alphabet letter with a separate full-string scan for every target, taking $O(\sigma nF)=O(n^2)$ time for fixed $\sigma$ on these tiers.

## Alternatives and edge cases

- **Edit every frequency independently:** This misses the saving from changing a surplus letter into its deficient successor.
- **Greedily transfer every available surplus:** The best goal for either letter may be zero rather than $k$, and using one boundary can change which neighboring boundary should be used.
- **Carry characters through several letters:** Two successive changes offer no advantage over one deletion and one insertion, so such chains are unnecessary.
- **Enumerate targets above the current maximum:** They require only additional insertions compared with target $F$ and cannot improve the answer.
- **Already good input:** Choosing its existing frequency leaves each present letter at $k$ and every absent letter at zero, yielding zero operations.
- **Remove a rare character:** Setting one frequency to zero can be cheaper than raising it to the common target, as in `"acab"`.
- **Letter `'z'`:** It has no outgoing change edge and is handled only individually or as the second member of the `'y'`/`'z'` pair.
