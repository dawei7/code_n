## General

**Turn each scoring section into one yes-or-no choice**

Bob does not receive more points for placing more arrows into a section after he has already beaten Alice there. For section `i`, Alice has `aliceArrows[i]` arrows. Bob loses or ties that section when he uses at most that many arrows, and he wins it only when he uses at least one more. Therefore, if Bob decides to win section `i`, the cheapest useful allocation is exactly `aliceArrows[i] + 1` arrows. That decision costs that many arrows and earns exactly `i` points.

This observation removes an enormous number of meaningless allocations. Instead of asking how many arrows to place in every section, the solution first asks only which sections Bob should win. Every section has two relevant states:

- do not deliberately win it, spending no arrows on it during the search and gaining no points from it; or
- win it with the minimum required number of arrows, spending `aliceArrows[i] + 1` and gaining `i` points.

There are `s = len(aliceArrows)` sections. A bitmask from `0` through `2^s - 1` can represent every possible subset of sections. Bit `i` is `1` precisely when the subset proposes winning section `i`. Enumerating masks is practical because this problem always has only twelve scoring sections, even though the explanation keeps `s` as a useful general symbol.

**Evaluate one mask**

For every nonempty `mask`, the inner loop visits all entries of `aliceArrows`. When `mask >> i & 1` is true, section `i` belongs to the proposed winning set. The solution then adds `i` to `s`, the score of this proposal, and adds `x + 1` to `cnt`, where `x` is `aliceArrows[i]`. Thus, `cnt` is not an arbitrary allocation: it is the smallest total number of arrows that can win exactly all selected sections.

The mask is feasible when `cnt <= numArrows`. If its score `s` is strictly larger than the best score `mx` found so far, the code remembers both the score and the mask by assigning `mx = s` and `st = mask`. The strict comparison is intentional. The problem permits any maximum-scoring allocation, so there is no need to replace an earlier best subset with a later subset that has the same score.

The code uses the name `s` both conceptually for the number of sections in the complexity discussion and locally for the score accumulated for one mask. In the Python function, `m = len(aliceArrows)` is the actual section count, while the local `s` is reset to zero for each mask. Keeping those roles separate makes the loops easier to understand.

**Why minimum winning costs are sufficient**

Suppose an allocation wins section `i` using more than `aliceArrows[i] + 1` arrows. Removing the excess arrows does not change whether Bob wins the section and does not change its point value. Those arrows can therefore be left unused until the final construction step. Consequently, every optimal score has at least one representation among the masks using the minimum winning cost for each selected section.

Conversely, every mask with `cnt <= numArrows` can be turned into a legal allocation. Give each selected section its recorded minimum winning amount. This wins every selected section and consumes `cnt` arrows. The remaining `numArrows - cnt` arrows can be placed somewhere without undoing any victory. This establishes a direct connection between feasible masks and achievable scores: no achievable optimal score is omitted, and every score considered feasible can actually be produced.

Since the loop examines all subsets, it eventually examines a mask corresponding to an optimal set of scoring sections. The stored value `mx` can never exceed the true optimum because it comes only from a feasible allocation. It also cannot finish below the optimum because the optimal subset is among the enumerated masks and would update `mx` unless an equally good subset was already stored. Therefore, `st` identifies a maximum-scoring choice of sections.

**Reconstruct the actual arrow allocation**

The search stores only a bitmask, but the method must return a list whose entries add up to exactly `numArrows`. It begins reconstruction with `ans = [0] * m`. For every selected bit `i` in `st`, it assigns `ans[i] = aliceArrows[i] + 1` and subtracts that amount from the local `numArrows` variable. After this loop, each selected positive-value section is definitely won, every unselected section still has zero arrows, and `numArrows` now means “arrows still unassigned,” rather than the original total.

The final statement `ans[0] += numArrows` puts all leftovers into section `0`. This is a particularly safe disposal location because section `0` is worth zero points. Extra arrows there cannot remove any already won section, and whether they cause Bob to tie, lose, or win section `0` has no effect on his score. The returned entries now sum to the original arrow count exactly.

Section `0` is also present in the bitmask search, but selecting it contributes zero to `s` while consuming arrows. Because an update requires `s > mx`, adding only section `0` can never improve the stored answer. A mask containing section `0` is likewise never preferable to the same positive-scoring choices without it. The final leftover assignment handles this zero-point section without needing to select it during optimization.

The enumeration begins at mask `1` rather than mask `0`. The empty subset is already represented by the initial values `st = 0` and `mx = 0`. If Bob cannot afford to win any positive-scoring section, no candidate produces a score greater than zero, `st` remains zero, and reconstruction simply places every arrow in `ans[0]`. That is legal and achieves the maximum possible score of zero.

## Complexity detail

Let `s` be the number of scoring sections. There are `2^s` possible masks. The code skips the empty mask but still examines `2^s - 1` masks, which has the same asymptotic size. For each mask, it scans all `s` sections to compute the required arrows and score. The search therefore takes `O(2^s \cdot s)` time.

Reconstruction performs one additional scan of `s` positions, which takes `O(s)` time and is dominated by the subset enumeration. In the actual problem `s = 12`, so at most 4095 nonempty masks are checked, each across twelve positions. The exponential form is important for explaining the technique, while the fixed small dimension explains why it is fast enough here.

The returned `ans` list occupies `O(s)` space. Apart from that required output, the method stores only a few integers such as `st`, `mx`, `cnt`, and the loop variables, so its auxiliary working space is `O(1)`. Counting the output, as the variant manifest does, the total space complexity is `O(s)`. No list of all masks and no dynamic-programming table is retained.

Python integers can represent the total arrow counts without overflow. In a fixed-width language, the given constraints should still be checked before choosing the type used for accumulated arrow costs, even though this particular twelve-section problem keeps the maximum comfortably bounded.

## Alternatives and edge cases

- **Backtracking over win-or-skip choices:** A depth-first search can make the same two decisions for each section and track arrows and score along the recursion. It has the same exponential worst-case work, and pruning unaffordable branches can reduce practical work, but the bitmask version is shorter and makes exhaustive coverage especially explicit.
- **Zero-one knapsack by arrow budget:** Treat each section as an item with weight `aliceArrows[i] + 1` and value `i`. A budget-indexed dynamic program can find the maximum score, but its cost depends on `numArrows` and reconstruction needs additional state. With only twelve sections, enumerating `2^12` subsets is simpler and independent of a potentially larger arrow budget.
- **Greedily choosing the best score-to-arrow ratio:** Ranking sections by `i / (aliceArrows[i] + 1)` is not reliable for a zero-one choice problem. A locally attractive ratio can consume arrows that would enable a better combination of other sections, so only a method that considers combinations can guarantee the optimum.
- **Spending extra arrows while evaluating a subset:** Excess arrows never increase a section's points. Using the minimum winning cost during comparison is essential because it gives every proposed subset its fairest feasibility test; leftovers are handled only after the best subset is known.
- **No affordable positive-scoring section:** The initialized empty choice remains optimal. The result places all arrows in section `0` and returns a valid allocation whose score is zero.
- **Armor-like “at most” reasoning does not apply here:** Bob must allocate exactly all `numArrows`, not merely at most that number. The reconstruction's final addition to `ans[0]` is what turns the minimum-cost winning plan into an exact-total allocation.
- **Ties do not score:** Bob needs strictly more arrows than Alice in a section. This is why the cost is `aliceArrows[i] + 1`, not `aliceArrows[i]`.
- **Several optimal answers:** The strict `s > mx` update preserves the first maximum-scoring mask encountered. The problem explicitly accepts any maximum-scoring allocation, so no tie-breaking rule is required.
- **All arrows left after reconstruction:** Assigning them to index `0` may change the outcome of the zero-point section, but it cannot change the numeric score and cannot invalidate any selected victory.
- **Fixed twelve-section domain:** The exponential algorithm is appropriate because the number of sections is tiny and fixed. It would not scale to an input with hundreds of independently selectable sections; a different constraint structure would then demand dynamic programming, meet-in-the-middle search, or another optimization method.
