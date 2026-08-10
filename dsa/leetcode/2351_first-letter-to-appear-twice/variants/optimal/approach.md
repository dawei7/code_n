## General

**The answer is determined at a second occurrence**

A letter “appears twice” at the position where its running frequency first reaches two. The requested letter is the one whose second occurrence has the smallest index.

Scanning `s` from left to right encounters positions in exactly that priority order. The first character whose count becomes two must therefore be the answer.

**Maintain running frequencies**

`cnt = Counter()` begins as an empty frequency mapping. For each character `c`, the method increments `cnt[c]`.

Immediately after the increment:

- count one means this is the first occurrence;
- count two means this is the second occurrence;
- a larger count would mean the second occurrence happened earlier.

The method returns as soon as `cnt[c] == 2`.

Because it returns at the earliest second occurrence in the scan, no character can later qualify earlier.

The Counter represents information about the processed prefix, not about the complete string. That distinction is what makes it useful for ordering. At index `i`, `cnt[c]` answers how many copies of `c` have actually appeared no later than `i`. A final frequency table built after the scan could say that both `a` and `c` repeat, but it would not by itself reveal whether `a`'s second copy or `c`'s second copy occurred first. Updating and testing immediately preserves that temporal fact.

**Why the first appearance does not decide anything**

The order of first occurrences is irrelevant. A letter seen early may not repeat until much later, while another letter first seen later can receive its second occurrence sooner.

For `"abccbaacz"`, `a` is first at index zero, but its second occurrence is index five. `c` first appears at index two and repeats at index three, so the scan returns `c` when that second copy is processed.

**Why checking equality with two is precise**

Checking `cnt[c] >= 2` would also return at the same first qualifying moment. The exact equality makes the event explicit: return exactly when the running frequency transitions from one to two.

No character can reach count three before the method should already have returned at its count-two position. The input guarantee ensures some repeated character exists, so execution always returns inside the loop.


Suppose the method returns character `c` at index `i`. Its frequency in prefix `s[0..i]` is two, so `i` is `c`'s second occurrence.

For every earlier position `j < i`, the method did not return. Therefore the character processed at `j` had frequency other than two after its increment; no letter completed its second occurrence earlier.

Thus `c` has the earliest second-occurrence index and is exactly the requested result.

Conversely, let `c` be the problem's answer and `i` its second occurrence. Before `i`, no letter has appeared twice by definition. At `i`, incrementing `cnt[c]` changes it to two, so the method returns `c`. It cannot return another letter first.

**The fixed alphabet bounds storage**

The input uses only 26 lowercase English letters. The Counter can hold at most 26 keys regardless of string length. That makes its auxiliary space constant under this domain.

Although the manifest summary mentions a 26-bit mask, the exact source uses a Counter. A bit mask would record only seen/not-seen state; the Counter records full frequencies even though only the transition to two matters.

## Complexity detail

Let `n` be the string length. The scan may return early, but in the worst case the first second occurrence is near the end, so time is `O(n)`.

The Counter stores at most 26 entries, giving `O(1)` auxiliary space under the lowercase-English constraint. With an unbounded alphabet, it would be `O(u)` for `u` distinct characters seen.

The immutable input string is not modified. The returned value is one character.

## Alternatives and edge cases

- **26-bit seen mask:** Test the bit for each character; if already set, return it, otherwise set it. This matches the manifest summary and uses one integer.
- **Boolean array of length 26:** It expresses first-seen state without full counts and remains constant-space.
- **Set of seen letters:** If `c in seen`, return it; otherwise insert it. This is simpler than a Counter for the exact need.
- **Compute all frequencies first:** Final counts do not reveal which second occurrence came earliest; scan order must be retained.
- **Return the first character with final count at least two:** Iterating unique characters by first appearance can give the wrong answer because second-occurrence order differs.
- **Immediate pair such as `"aa"`:** The second character raises the count to two and is returned.
- **Only one repeated letter:** Its second occurrence is necessarily the answer.
- **Several repeated letters:** The left-to-right early return selects the smallest second-occurrence index.
- **A letter appearing many times:** It triggers on its second copy; later copies are never reached after return.
- **First repeated letter may not be first distinct letter:** Only second-occurrence position matters.
- **Guaranteed repetition:** The function has no fallback return because valid input always triggers the condition.
- **Lowercase alphabet:** At most 26 Counter keys exist.
- **Input preservation:** Counting does not modify `s`.
- **Counter availability:** The exact source relies on `Counter`, conventionally from `collections`.
