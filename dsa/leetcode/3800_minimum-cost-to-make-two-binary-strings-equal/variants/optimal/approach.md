## General

**Classify mismatches by orientation**

Matching positions need no operation. Every mismatch has one of two forms:

- type zero: `s[i]='0'` and `t[i]='1'`;
- type one: `s[i]='1'` and `t[i]='0'`.

`diff[0]` and `diff[1]` count these orientations. Positions within one orientation are interchangeable for cost purposes because every allowed swap may choose arbitrary distinct indices.

The scan calls `int(c1)` only after detecting inequality. Source bit zero therefore identifies `(0,1)` and source bit one identifies `(1,0)`.

Let `mn=min(diff)`, `mx=max(diff)`, and $B=mn+mx$.

**Understand what each operation does to mismatches**

A flip at a mismatched position fixes that one mismatch for `flipCost`.

Swapping within one string between one mismatch of each orientation fixes both. In `s`, for example, the two source bits are zero and one; exchanging them makes both agree with their respective `t` bits. This costs `swapCost`.

A cross swap at one mismatched index does not fix it. It changes `(0,1)` into `(1,0)` or vice versa, converting its orientation for `crossCost`. At a matching position, a cross swap changes nothing.

These effects reduce the problem to deciding how many opposite pairs to swap, how many dominant-orientation mismatches to convert, and how many leftovers to flip.

**Candidate one: flip everything**

The initial

`ans = (diff[0]+diff[1])*flipCost`

repairs each mismatch independently. This candidate is necessary when swaps or cross conversions are expensive.

**Candidate two: pair existing opposite orientations**

There are `mn` immediately available opposite-orientation pairs. Swapping each pair fixes two mismatches. The dominant group has `mx-mn` leftovers, each fixed by a flip.

The cost is

`mn*swapCost + (mx-mn)*flipCost`.

The source takes the minimum with the all-flip candidate, thereby also deciding whether an opposite pair is better handled by one swap or two flips.

No positional distance appears in `swapCost`, so any two opposite mismatches can be paired; their concrete indices are unnecessary.

**Candidate three: convert dominant mismatches until pairing is maximized**

Set `avg = (mx+mn)//2`, the maximum number of pairs after accounting for parity.

Initially only `mn` opposite pairs exist. Converting `avg-mn` dominant mismatches with cross swaps increases the minority count and decreases the dominant count by the same amount.

After conversion:

- when $B$ is even, both orientations have `avg` members;
- when $B$ is odd, they form `avg` pairs with one dominant mismatch left.

The source cost is

`(avg-mn)*crossCost + avg*swapCost + (B-2*avg)*flipCost`.

The final coefficient is zero for even $B$ and one for odd $B$.

**Why only endpoint conversion counts matter**

Suppose `q` dominant mismatches are converted, where `0<=q<=avg-mn`. Pairing then fixes `mn+q` opposite pairs, and remaining mismatches are flipped. The total cost is a linear function of `q`:

$$
q\cdot\texttt{crossCost}
+(mn+q)\cdot\texttt{swapCost}
+(mx-mn-2q)\cdot\texttt{flipCost}.
$$

A linear function over an integer interval reaches its minimum at an endpoint unless all points tie. Endpoint `q=0` is candidate two; endpoint `q=avg-mn` is candidate three.

Likewise, deciding how many existing opposite pairs use swaps rather than two flips is linear, so candidate one and candidate two cover its endpoints. No mixed interior strategy can beat all three source candidates.

**Trace an imbalanced case**

If mismatch counts are five and one, then `mn=1`, `mx=5`, and `avg=3`.

Candidate three cross-converts two dominant mismatches, leaving three of each orientation. Three ordinary swaps then fix all six mismatches. Its cost is `2*crossCost+3*swapCost`.

Without conversions, one ordinary swap fixes the existing opposite pair and four flips fix the remainder.

**Already-equal strings**

Both counts are zero. Every candidate evaluates to zero, so no special branch is required.

## Complexity detail

The source scans the $N$ character pairs once, doing constant work per position. All later arithmetic is constant. Total time is $O(N)$.

`diff` has two counters and all other state is scalar, so auxiliary space is $O(1)$. Neither input string is modified.

## Alternatives and edge cases

- **Shortest path over full strings:** The state space is exponential; orientation counts capture everything relevant.
- **Cross swap as a direct repair:** It only reverses mismatch orientation and must be followed by pairing or flipping.
- **Swap two same-orientation mismatches:** Within-string swapping equal source bits changes nothing.
- **Use only swaps:** An odd total mismatch count necessarily leaves one mismatch for a flip.
- **Use only flips:** Always feasible but not always cheapest.
- **Balanced orientations:** `avg=mn`, so candidate three needs no cross conversions.
- **One mismatch:** Only a flip can finish; formulas return `flipCost`.
- **Odd total mismatches:** Candidate three includes exactly one leftover flip.
- **Cross cost very high:** Candidate one or two wins.
- **Swap cost above two flips:** The all-flip candidate prevents overpaying.
- **Equal strings:** Answer is zero.
- **Arbitrary swap indices:** Counts suffice because swaps are not adjacency-restricted.
- **Input preservation:** The method counts orientations without constructing modified strings.
- **No adjacency restriction:** Arbitrary distinct indices validate count-based pairing.
- **Large costs:** Python integers safely hold count-price products.
