## General

**Lexicographic order is decided at the first differing position**

Every answer must use exactly the same multiset of letters as `s`, but its order may change. To be strictly greater than `target`, the result must have some first position where it differs from `target`, and its letter at that position must be larger. Everything after that decisive position can then be made as small as possible.

This leads to the structure of the desired result:

1. Match a prefix of `target` exactly.
2. At one pivot position, use an available letter strictly larger than `target[pivot]`.
3. Arrange every remaining letter in ascending order.

For a fixed pivot and fixed matching prefix, the smallest valid pivot letter is best. Once the pivot is larger, the suffix cannot affect the greater-than relationship, so sorting the suffix ascending makes the complete result lexicographically smallest for that pivot.

The only difficult part is selecting the pivot. A later pivot preserves a longer prefix equal to `target` and is therefore lexicographically smaller than any solution forced to differ earlier. The solution first tries to push the exact match as far right as possible, then backtracks only when no larger pivot letter is available.

**Represent the unused letters by frequencies**

The array `counts` has 26 entries. Entry zero counts `'a'`, entry one counts `'b'`, and so forth. Scanning `s` fills this array, preserving duplicate multiplicities exactly.

The list `prefix` contains letters already committed to equal the corresponding positions of `target`. Whenever a letter is appended to `prefix`, one copy is removed from `counts`. Therefore, at every point:

- `prefix` uses real letters from `s`.
- `counts` describes exactly the letters of `s` that remain unused.
- The concatenation of `prefix` and all letters represented by `counts` has the same multiset as `s`.

This invariant prevents both losing a duplicate and using a letter too many times.

**Match the target for as long as the multiset allows**

Starting at `position = 0`, the first loop examines `target[position]`. If an unused copy exists, it appends that character to `prefix`, decrements its count, and moves to the next position.

Matching the target character is always the smallest possible choice that does not make the result smaller at this position. Choosing a smaller character would make the whole permutation lexicographically smaller than `target` immediately and could never be repaired by a later suffix. Choosing a larger character would make a valid pivot now, but if an exact match can be continued and a valid pivot can be placed later, that later difference produces a smaller overall answer.

The loop stops in one of two situations:

- `position < n` and no unused copy of `target[position]` exists.
- `position == n`, meaning the letters of `s` can reproduce all of `target` exactly.

In the second situation, equality is not enough because the result must be strictly greater. The algorithm must backtrack to change some earlier matched letter into a larger one.

**Try to place the decisive larger letter**

When `position < n`, the code scans letter indices from one greater than the current target letter through 25. This is an ascending scan, so the first available letter is the smallest unused letter strictly greater than `target[position]`.

After selecting that index, the code consumes one copy and builds `suffix` by emitting all remaining letters from `'a'` through `'z'` according to their counts. The returned string is

`prefix + chosen_larger_letter + sorted_suffix`.

This candidate is a valid permutation because every consumed and emitted count comes from `s`. It is strictly greater than `target` because `prefix` matches through `position - 1` and the chosen letter is greater at `position`. It is the smallest candidate for this pivot because both the chosen greater letter and the suffix are as small as possible.

For `s = "abc"` and `target = "bba"`, the algorithm first matches `'b'`. No second `'b'` remains, so `position` is one and `prefix` is `"b"`. Among unused letters greater than target letter `'b'`, `'c'` is the smallest. The only remaining letter `'a'` forms the sorted suffix, producing `"bca"`.

For `s = "leet"` and `target = "code"`, no `'c'` is available at position zero. The smallest available letter greater than `'c'` is `'e'`, and the remaining letters sort to `"elt"`. The result is `"eelt"`.

**Backtrack when the current pivot cannot be made larger**

If no unused letter is greater than `target[position]`, no answer can keep the current matched prefix and first differ at this position. The solution then moves the pivot one position left:

1. If `prefix` is empty, there is no earlier position to reconsider, so no answer exists.
2. Otherwise, decrement `position`.
3. Pop the last matched letter from `prefix`.
4. Restore that letter's count because it is unused again.
5. Repeat the search for a letter greater than `target[position]`.

Restoring the popped letter is essential. It may itself be a possible pivot letter at an earlier position or belong in the final suffix.

The algorithm backtracks from right to left. The first position at which it can place a larger letter is the rightmost feasible pivot. Any solution with an earlier pivot differs from `target` sooner. At that earlier first difference it must also be greater, while the found solution still matches `target` there, so the found solution is lexicographically smaller regardless of later characters.

**Why the returned candidate is globally smallest**

Any strictly greater permutation has a unique first differing position `p`. Before `p` it exactly matches `target`, at `p` it uses a greater letter, and after `p` its remaining letters can be arranged arbitrarily.

The forward phase builds the longest target prefix available. The backtracking phase considers potential pivot positions from right to left, skipping a position only when no unused greater letter can work there. It therefore finds the greatest feasible `p`. At that `p` it chooses the smallest feasible greater letter and sorts the suffix. These three choices—latest pivot, smallest greater pivot letter, and smallest suffix—are the lexicographic priorities in their exact order. Hence no other qualifying permutation can be smaller.

If backtracking empties `prefix` and no greater letter can be placed at position zero, even the most favorable first character is not greater than `target[0]`. Since every later difference is irrelevant after a smaller first character and exact matching is unavailable or cannot lead to a later pivot, no qualifying permutation exists, so returning `""` is correct.

## Complexity detail

Let `n` be the common length. Building `counts` takes $O(n)$ time. The forward matching phase advances `position` at most `n` times. During backtracking, each previously matched position is popped at most once. At every attempted pivot, the code scans at most 26 alphabet entries, a fixed constant, so all pivot searches take $O(26n)=O(n)$ time.

The sorted suffix is constructed only once, immediately before returning, and emits exactly the remaining letters, taking $O(n)$ time. Joining the prefix and suffix also takes $O(n)$. The total time complexity is $O(n)$.

The 26-entry count array is $O(1)$ with respect to `n`. The prefix list can contain `n` characters, and constructing the suffix and result requires linear output storage, so the auxiliary space complexity is $O(n)$. The algorithm never enumerates permutations, whose count could be factorial.

## Alternatives and edge cases

- **Generate and sort all distinct permutations:** This directly follows the definition but can require up to $n!$ candidates and is infeasible even far below `n = 300`. Frequency-guided pivot selection constructs only the single best candidate.
- **Take the next permutation of a sorted copy of `s` repeatedly:** Advancing until passing `target` can still traverse exponentially many permutations. The exact method jumps directly to the latest feasible pivot.
- **Choose a larger letter at the earliest opportunity:** That makes a valid answer but not necessarily the smallest one. Preserving an equal prefix for more positions has higher lexicographic priority than optimizing any suffix.
- **Use the largest feasible pivot letter:** Once the pivot position is fixed, a larger chosen letter only makes the result worse. The ascending alphabet scan correctly takes the first available greater letter.
- **Leave the suffix in original `s` order:** The original positions are irrelevant because any permutation is allowed. Sorting the remaining multiset ascending gives the minimum suffix.
- **Duplicate letters:** Counts preserve multiplicity, and consuming or restoring one copy changes only one array entry. A target character can be matched only as many times as `s` supplies it.
- **`s` can equal `target` exactly:** Equality is not strictly greater. Reaching `position == n` causes backtracking, which searches for the nearest possible increase; if none exists, the result is empty.
- **Target is smaller at the first position:** If the smallest available letter greater than `target[0]` can be chosen immediately, the remaining letters are sorted and returned without unnecessary matching.
- **All permutations are at most the target:** Backtracking eventually reaches position zero, finds no greater available letter, and returns `""`. For example, if `target` is the greatest permutation of `s`, no strict successor exists.
- **Target contains a letter unavailable during matching:** This is not automatically failure. An available larger letter at that position can create the answer, as `"eelt"` versus `"code"` demonstrates.
- **A smaller available letter at the failed position:** Choosing it would make the result smaller than `target` at the first difference, so the code correctly ignores it and either chooses a greater letter or backtracks.
- **Length one:** The sole permutation is `s`. The algorithm returns it only if its character is greater than `target`; equality or a smaller character yields `""`.
- **Restoring on backtrack:** Without adding the popped target character back to `counts`, later pivot attempts would operate on an incomplete multiset and could falsely report failure or build a non-permutation.
