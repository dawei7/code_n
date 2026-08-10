## General

A valid chosen substring needs only two endpoint conditions:

- its first and last characters are equal;
- its length is at least four.

The characters between the endpoints can be anything. The objective is to choose as many pairwise non-intersecting valid intervals as possible.

This is an interval-scheduling problem in which intervals do not need to be generated explicitly. The source scans possible right endpoints from left to right. As soon as any valid interval can end at the current index, it selects one, counts it, and starts fresh after that endpoint. Choosing the earliest possible finishing interval leaves the largest suffix for future choices, which is the standard optimal greedy rule for maximizing the number of disjoint intervals.

**What the dictionary represents**

`first_position` stores the earliest occurrence of each character since the end of the last selected substring. More precisely, for each recorded character `c`, `first_position[c]` is its smallest available index in the currently uncommitted suffix.

When a character is absent, `setdefault(character, index)` records its current index. When it is already present but too close to form a length-four substring, `setdefault` leaves the earlier index unchanged.

Keeping the earliest occurrence is always best for detecting feasibility. At a fixed ending index, the earliest matching start gives the longest possible substring. If even that earliest occurrence is fewer than three indices away, every later matching occurrence is also too close. If it is at least three indices away, a valid substring exists.

**Why the distance threshold is three**

An inclusive substring from index `start` through index `end` has length

`end - start + 1`.

Requiring length at least four is equivalent to

`end - start >= 3`.

That is exactly the source condition

`index - first_position[character] >= 3`.

The separate membership test ensures there is an earlier available occurrence with the same character.

**Selecting immediately at the earliest valid end**

The scan processes indices in increasing order. If the condition succeeds at `index`, then the substring beginning at `first_position[character]` and ending at `index` is valid. The source increments `selected` immediately.

This `index` is the earliest finishing position of **any** valid substring in the current available suffix. If some valid substring had ended earlier, then when the scan visited that earlier endpoint, its matching starting character would have been stored at least three positions behind and the code would already have selected it.

That earliest-finish property is the heart of the proof.

**Why earliest finish maximizes the count**

Consider an optimal collection of non-intersecting valid substrings in the current suffix, and let its first substring end at `e_opt`. Let the greedy substring end at `e_greedy`. Because greedy selects the first index at which any valid interval can finish,

$$
e_{\text{greedy}} \le e_{\text{opt}}.
$$

Replace the optimal collection’s first substring with the greedy one. Every later substring in the optimal collection begins after `e_opt`, and therefore also begins after `e_greedy`. The replacement creates no intersection and does not remove any later choice. So there exists an optimal solution whose first selection is the greedy selection.

After that selection, the same argument applies independently to the remaining suffix. Repeating the exchange proves that every greedy choice can be part of an optimal collection, and the final count is maximum.

The greedy interval’s start need not be the latest possible matching start. Choosing the earliest stored start may make the selected interval longer, but all positions through the same ending index become unavailable regardless. Future opportunities depend on the end, not on how far left the chosen interval began. The algorithm optimizes the finishing point, which is the relevant boundary.

**Why clearing all stored positions is necessary**

After selecting a substring ending at `index`, the source assigns

`first_position = {}`.

Every stored occurrence lies at or before `index`. Reusing any of them as the start of a later substring would make that later interval intersect the just-selected interval. They must all be discarded, not only the occurrence of the selected endpoint character.

The current ending character is also not inserted into the new dictionary. Substrings are inclusive, so using the same index as the next start would make two selected substrings share that character position. “Non-intersecting” forbids that. The next available start can only appear at `index + 1` or later.

**Why an early repeated character remains stored**

Suppose `'a'` first appears at index `0` and again at index `2`. The distance two is too short, so no selection occurs. `setdefault` retains index zero rather than replacing it with index two. If another `'a'` appears at index three, the retained occurrence proves that `word[0:4]` has length four and is valid. Replacing the stored position at index two would miss that opportunity.

**Tracing the first example**

For `word = "abcdeafdef"`, the dictionary first records the positions of `a`, `b`, `c`, `d`, and `e`. At index five, `a` repeats with distance five from index zero, so `"abcdea"` is selected and the dictionary is cleared.

The new suffix starts at index six. `f` is stored at six, `d` at seven, and `e` at eight. At index nine, `f` repeats with distance three, so `"fdef"` is selected. The final count is two.

No earlier-ending valid substring existed in either available suffix, so each choice leaves as much room as possible for the next.

## Complexity detail

The loop visits each of the `n` characters once. Dictionary membership, lookup, `setdefault`, assignment, and clearing are constant-time expected operations.

Moreover, `word` contains only lowercase English letters, so `first_position` has at most 26 entries. Replacing it with a new empty dictionary is constant-time with respect to `n`; the old dictionary also contains at most 26 entries. Total time is `O(n)`.

The dictionary holds at most one position for each of 26 letters, and all other state is scalar. Thus auxiliary space is `O(1)` under the fixed-alphabet constraint, matching the manifest. For a generalized unbounded alphabet, the more precise bound would be `O(\min(n,\sigma))` where `\sigma` is the number of distinct characters.

## Alternatives and edge cases

- **Generate every valid interval and run interval scheduling:** Enumerating all equal-character endpoint pairs could create `O(n^2)` intervals before sorting or selecting them. The source detects the earliest finishing interval online using only earliest positions.
- **Dynamic programming by prefix:** A DP can decide whether to take a valid substring ending at each index, but naively considering all matching starts is quadratic. The greedy exchange argument makes that extra state unnecessary.
- **Store the latest occurrence:** This can miss valid length-four substrings. If the earliest matching start is far enough away but the latest is too close, replacing the earliest position destroys the evidence that a valid interval exists.
- **Choose a later-ending interval:** It can only shorten the suffix available for future non-intersecting substrings and never increases the contribution of the current interval, since every selected substring is worth exactly one.
- **String shorter than four:** No endpoint distance can reach three, so the method returns zero.
- **Exactly four equal-endpoint characters:** A four-character string such as `"abca"` satisfies distance three and is selected once.
- **All characters equal:** The scan selects positions `[0,3]`, clears state, then can select `[4,7]`, and so on, yielding the maximum number of disjoint blocks of length four.
- **Repeated characters too close:** Retaining the earliest occurrence lets a later repetition eventually reach the threshold; close repeats do not reset the start.
- **Touching at an endpoint:** Intervals sharing one index intersect. Clearing without re-adding the current endpoint correctly forbids such reuse.
- **Adjacent selected substrings:** One interval may end at `e` and the next may start at `e+1`; they share no position and are allowed.
- **Several valid intervals ending together:** Their future effect is identical because they share the same end. Choosing the one beginning at the stored earliest occurrence remains optimal.
- **Unused possible starts inside a selected interval:** Clearing them is mandatory because every one overlaps the chosen interval, even if it could have paired with a future character.
- **No input mutation:** The algorithm records indices and a count but never changes `word`.
- **Fixed lowercase alphabet:** The constant-space conclusion relies on the stated 26-character alphabet. The linear-time greedy logic itself works for a larger hashable alphabet, with correspondingly larger dictionary space.
