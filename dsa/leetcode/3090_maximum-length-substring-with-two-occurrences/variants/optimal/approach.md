## General

**Turn the condition into a window invariant.** A substring is valid when no character appears more than twice inside it. The goal is not to count valid substrings but to find the maximum length, so it is natural to maintain one longest possible valid window ending at each right endpoint.

The exact source uses two indices:

- `j` is the right endpoint currently being added;
- `i` is the left endpoint of the maintained window.

`cnt` records the frequency of each character in the inclusive substring `s[i:j + 1]`. Before the next character is added, every stored frequency is at most two.

**Expand by one character.** For each pair `(j, c)` from `enumerate(s)`, the code increments `cnt[c]`. This creates the only possible violation. Every other character had count at most two before the expansion and its count did not change. Therefore, the algorithm needs to inspect only `cnt[c]`, not scan all 26 letters after every step.

If `cnt[c] <= 2`, the expanded window remains valid immediately. If it becomes three, the window contains one too many copies of the newly added character.

**Shrink only as much as necessary.** While `cnt[c] > 2`, the source removes the character at `s[i]` from the frequency map and advances `i`. Characters different from `c` may be removed during this process, but that cannot create a new violation because their counts only decrease. Eventually the oldest included occurrence of `c` is removed, its count returns to two, and the loop stops.

Stopping at that exact moment is important. Moving `i` farther would keep the window valid, but it would make it needlessly shorter. After the loop, `s[i:j + 1]` is the longest valid substring that ends at `j`: any earlier left boundary would still include the third occurrence of `c` that forced the shrink.

**Why recording this length finds the global answer.** Every substring has some right endpoint. When the scan reaches that endpoint, the maintained window is the longest valid substring ending there. Any other valid substring ending at the same position starts at or after `i` and cannot be longer. Thus `j - i + 1` is the best candidate for this endpoint, and taking the maximum over all endpoints covers the globally longest valid substring.

This is also why `i` never needs to move backward. Once a prefix position has been excluded to repair a three-copy violation, adding more characters later cannot make that old position useful again: reintroducing it would only add characters and could recreate violations. The one-direction movement is the source of the linear running time.

**A detailed trace.** Consider `s = "bcbbac"`.

- At `j = 0`, the window is `"b"` and its length is one.
- Adding `c` gives `"bc"`; both counts are one.
- Adding the second `b` gives `"bcb"`; `b` occurs twice, so the window is valid.
- Adding the third `b` gives `"bcbb"`; `cnt["b"]` is three. The loop removes the leftmost `b`, advances `i`, and leaves `"cbb"` with two `b` characters.
- Adding `a` gives `"cbba"`, still valid.
- Adding the final `c` gives `"cbbac"`, where `c` occurs twice and `b` occurs twice.

The source records the best length after each repair, so it never counts the temporarily invalid `"bcbb"` but does count the valid windows that follow.

**Why a frequency map is needed.** With an ordinary sum or count, removing the leftmost element is easy. Character validity, however, is per letter. The `Counter` keeps those independent counts, allowing the source to know exactly when the extra copy of `c` has left the window. It is not sufficient to store only the most recently seen index, because two occurrences are allowed and the third occurrence determines the new boundary.

**The limit two is built into the code.** Unlike a general “at most $k$ occurrences” routine, this method compares directly with the literal `2`. There is no input parameter controlling the limit. That direct comparison matches this problem's fixed rule and makes the state especially small.

**Why the window is valid after every iteration.** Before adding `c`, all characters satisfy the limit. Adding it affects only its own count. The loop ends only when that count is again at most two, while every other count has stayed equal or decreased. Therefore, all counts meet the rule at the exact point where the answer is updated.

## Complexity detail

Let $n$ be the length of `s`. The right endpoint `j` advances exactly $n$ times. The left endpoint `i` also advances at most $n$ times across the entire run, even though its increments occur inside a `while` loop. Each increment, decrement, comparison, and maximum update is expected $O(1)$ with Python's hash-backed `Counter`.

The total time is therefore $O(n)$ expected, not $O(n^2)$. Amortized analysis is the key: the inner loop cannot repeatedly revisit an index after `i` passes it.

The input contains lowercase English letters, so `cnt` has at most 26 relevant entries. Auxiliary space is consequently $O(26)=O(1)$ relative to $n$. If the alphabet were unbounded, the more general statement would be $O(A)$ space, where $A$ is the number of distinct characters encountered.

## Alternatives and edge cases

- **Track occurrence queues:** Store the last three indices for each character and move the left boundary past the oldest when a third copy appears. This can also be linear but is more bookkeeping than the frequency window.
- **Enumerate every start:** Extending substrings from each starting position is straightforward but can take $O(n^2)$ time.
- **Last-two-position method:** Keeping the two newest positions per character can update `i` directly when a third copy arrives, avoiding the shrink loop while preserving $O(n)$ time.
- **One-character string:** Its only substring has length one and is valid.
- **Two equal characters:** Both may stay because the limit is inclusive.
- **Three equal characters:** The maximum valid length is two; each new copy forces the left boundary past the oldest.
- **All distinct characters:** The window never shrinks, so the answer is the entire string length.
- **Violation source:** Only the character just added can exceed two; all other counts were valid and are unchanged.
- **Characters removed during shrinking:** Counts of unrelated characters may fall, but lower counts can never invalidate the window.
- **Minimal shrink:** The loop stops as soon as the new character has count two, preserving the longest valid suffix ending at `j`.
- **Counter entries reaching zero:** They may remain stored with value zero. This does not affect correctness and the lowercase alphabet bounds the map size.
- **No empty answer:** The problem supplies a nonempty string, and every one-character substring is valid, so `ans` initialized to zero is updated to at least one.
- **Strictly more than two:** A count of exactly two is allowed; the condition uses `> 2`, not `>= 2`.
- **Expected hash behavior:** Python dictionary operations are expected constant time; adversarial hash-collision concerns are outside the ordinary complexity model for these single-character keys.
- **Why no final cleanup is required:** The answer is updated during the scan, and the maintained window is valid after every iteration.
- **Monotone pointers:** Neither index retreats, which is the central reason the nested-looking loops remain linear.
