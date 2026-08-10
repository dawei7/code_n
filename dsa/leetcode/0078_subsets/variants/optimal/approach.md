## General

**Every element creates one binary decision**

A subset either contains `nums[i]` or it does not. There is no third possibility, and because the input elements are unique, choosing the same membership decisions always identifies the same subset. The recursion explores these two choices for indices from zero through `len(nums) - 1`.

`dfs(i)` means that decisions for indices before `i` have already been made, and the mutable list `t` contains exactly the elements included by those decisions. The source first explores exclusion by calling `dfs(i + 1)` without changing `t`. It then appends `nums[i]`, explores inclusion with another `dfs(i + 1)`, and pops the element to restore the parent state.

Exploring exclusion first affects only output order. The contract accepts any order, so the algorithm could reverse these branches without changing the set of answers.

**The recursion tree is the power set**

At depth zero there is one undecided path. After the first element there are two paths: absent or present. After two elements there are four membership patterns, and after `n` elements there are $2^n$ leaves. Each root-to-leaf path is a length-`n` binary pattern whose zero/one choices specify a subset.

For `nums = [1, 2, 3]`, the all-exclude path reaches `[]`. A path excluding 1, including 2, and including 3 reaches `[2, 3]`. The all-include path reaches `[1, 2, 3]`. Every possible membership pattern occurs exactly once.

This tree explains why exponential work cannot be avoided: the required output itself contains $2^n$ different lists.

**Record only at a complete decision path**

When `i == len(nums)`, every input position has a decided membership state. The current `t` is therefore one complete subset, including possibly the empty subset. The source appends `t[:]`, a copy, and returns.

The copy is essential. All calls share and mutate the same working list. If the algorithm appended `t` directly, stored entries would refer to that one object and later appends or pops would change earlier answers. Slicing creates an independent list whose contents remain fixed.

Unlike combinations of a fixed size, there is no success condition based on `len(t)`. Every length from zero to `n` is valid, so the only leaf condition is that all elements have been considered.

**Why append, recurse, and pop restore the invariant**

Before `dfs(i)`, `t` describes choices for the prefix `nums[:i]`. The exclusion call sees the same prefix selection and moves on, so it generates all subsets whose `i`th element is absent.

After that call returns, appending `nums[i]` creates the correct state for all subsets whose `i`th element is present. The inclusion call explores them. Finally, `pop()` removes exactly the value appended by this level and restores `t` to its entry state before control returns to the parent.

This restoration is what allows one list to represent many different paths safely. Each recursive level owns one possible append and is responsible for undoing it.

**A correctness invariant**

On entry to `dfs(i)`, `t` contains exactly the chosen elements from the first `i` input positions, in their original relative order. The call must emit every subset that agrees with these existing choices and makes arbitrary choices for positions `i` onward.

At `i == n`, only one such subset remains, namely a copy of `t`. Otherwise, all responsible subsets split into two disjoint categories based on whether they contain `nums[i]`. The first recursive call emits exactly the exclusion category, and the second emits exactly the inclusion category. Since the categories are exhaustive and disjoint, the call fulfills its responsibility without duplicates.

Starting from empty `t` at index zero assigns responsibility for the entire power set. This proves completeness, uniqueness, and absence of invalid elements.

**Input order and uniqueness**

The algorithm does not sort `nums`. Every emitted subset lists selected values in their original input order. That is a perfectly valid representation because subsets are not required to be internally sorted.

The guarantee that all input values are unique is important for the “no duplicate subsets” claim. Distinct membership patterns on distinct values produce distinct subsets. If equal input values were allowed, different index decisions could yield equal value lists, and this source contains no duplicate-skipping logic.

**Trace the backtracking state**

For `[1, 2]`, exclusion-first traversal reaches `[]`, then includes 2 to record `[2]`. It returns to the level for 1 with `t` restored to empty, includes 1, then records `[1]` and `[1, 2]` through the two choices for 2. The four leaves correspond exactly to the four subsets.

The restoration between the two top-level branches explains why 2 does not remain accidentally selected when the recursion begins the branch containing 1.

## Complexity detail

There are $2^n$ output subsets. Copying a leaf list can cost up to $O(n)$, and across the complete power set each input value appears in exactly half the subsets, for $n2^{n-1}$ stored elements. Total time is $\Theta(n2^n)$, matching the manifest's $O(n\cdot2^n)$ bound.

The recursion depth is `n`, and `t` stores at most `n` values. Excluding the returned power set, auxiliary space is $O(n)$, matching the manifest. The output itself necessarily occupies $\Theta(n2^n)$ element slots across its lists.

## Alternatives and edge cases

- **Cascading iteration:** Start with `[[]]`; for each value, copy every existing subset and append that value. It produces the same doubling pattern without recursion.
- **Bitmask enumeration:** Treat integers from zero through $2^n-1$ as membership patterns. It is compact and directly exposes the one-bit-per-element correspondence.
- **Backtrack and append at every node:** Record `t` immediately, then loop over possible next indices. This visits one node per subset and avoids explicit exclude calls.
- **Input of length one:** The two leaves are the empty subset and the singleton.
- **Empty subset:** The all-exclude path records it automatically.
- **Full subset:** The all-include path records every input element.
- **Negative values:** Membership decisions depend on positions, not numeric magnitude or sign.
- **Original order:** Selected elements retain input order because indices only increase.
- **Unique-element guarantee:** It ensures distinct decision patterns yield distinct value subsets.
- **Copying:** `t[:]` is mandatory because `t` is later mutated by backtracking.
- **Any output order:** Exclusion-first DFS order is acceptable and needs no sorting.
- **Maximum length ten:** At most 1024 subsets are generated, but the general complexity remains exponential.
- **Input preservation:** The source never sorts or modifies `nums`.
