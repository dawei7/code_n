## General

**Think in current-string positions, not original positions**

The distance rule is evaluated after every deletion. If characters disappear, later characters move left, so two equal characters that were originally farther than `k` apart may eventually become close. An algorithm that stores only original indices would miss that change.

The source instead builds the final string in `ans`. At every moment, `ans` contains only characters that have survived processing so far. Therefore `len(ans)` is exactly the index at which the next input character would appear in the currently compacted string. This is why the line `cur = len(ans)` is the central detail: `cur` is a current-string position even though the outer loop reads the original string from left to right.

The dictionary `last` maps a character to the index of its most recent retained occurrence in `ans`. When the next character `c` arrives, the source checks whether

`cur - last[c] <= k`.

If so, the new right occurrence merges into the retained left occurrence, which means the new occurrence is deleted. The implementation performs that deletion simply by not appending `c`. If no retained equal occurrence is close enough, it appends `c` and records its new compacted index.

**Why the most recent equal occurrence is sufficient**

Suppose `ans` is already stable: no two equal retained characters are within distance `k`. For any character `c`, consecutive retained occurrences of `c` must therefore be more than `k` positions apart.

The next input character would be placed at the right end, at index `cur`. If it is not close to the most recent retained `c`, it cannot be close to any earlier `c` because every earlier occurrence has an even smaller index and therefore a greater distance from `cur`. If it is close to the most recent retained `c`, no second retained `c` can also be close: two retained occurrences inside the last `k` positions would themselves be at distance at most `k`, contradicting the stability of `ans`.

Thus there is at most one eligible equal left partner for the new character, and `last[c]` identifies it. No scan over all earlier positions is needed.

**Why prefix compaction agrees with the required merge order**

The problem describes repeated operations on the whole current string and specifies smallest left index first, then smallest right index. The source appears to use a different schedule because it resolves a character as soon as that character is encountered. These schedules produce the same survivors.

First, every merge deletes only its right character. A character already retained in a processed prefix can never be deleted because of a character appended later: if they merge, the later character is the right endpoint and is the one removed. Operations wholly inside a prefix may delete prefix characters, but performing those internal deletions before examining a later suffix is safe. A deletion in the suffix cannot change which prefix character is the right endpoint of a pair wholly inside that prefix, while a prefix deletion merely compacts all later positions in exactly the way represented by `len(ans)`.

This permits an induction over input prefixes. Before reading a new character, assume `ans` is the stable result of the processed prefix. Appending the new character introduces no pair between two old survivors because the prefix was already stable. Any new eligible pair must use the appended character as its right endpoint. The preceding argument shows that there is at most one such pair and that its left endpoint is `last[c]`. If it is close, the specified process eventually deletes the new right character; skipping it produces the same stable prefix. If it is not close, no merge is possible and appending it preserves stability.

The priority rule cannot change this conclusion. If other deletions in the full string are scheduled before or after a merge involving the new suffix, they never cause a later character to delete an earlier survivor. They only remove right endpoints and compact the positions, which the prefix construction already incorporates. Therefore processing prefixes eagerly is a valid way to compute the deterministic final string.

**Loop invariant**

Immediately before each outer-loop iteration:

- `ans` is the fully merged stable result for the original characters already processed;
- its list indices are their current indices after all corresponding deletions;
- `last[c]` is the current index of the rightmost retained `c` for every character present; and
- any two equal characters in `ans` are more than `k` positions apart.

If the next `c` is close to `last[c]`, skipping it models deletion of the right endpoint and changes none of the retained positions, so every statement remains true. Otherwise appending it creates no close equal pair, and recording `last[c] = cur` restores the dictionary statement. The invariant begins with an empty list and proves that the joined list is stable and contains exactly the required survivors after all characters are processed.

For `s = "aabca"` and `k=2`, the first `a` is appended at index zero. The second would occupy index one, so its distance from the retained `a` is one and it is skipped. The next characters `b` and `c` occupy compacted indices one and two. The final `a` would now occupy index three; its distance from index zero is three, so it is retained. Joining `ans` gives `"abca"`.

For `s = "yybyzybz"` and `k=2`, the second `y` is skipped. That deletion causes the next relevant `y` to be considered at compacted index two rather than original index three. It is now exactly distance two from the first `y` and is skipped as well. This demonstrates why `len(ans)`, rather than the original loop index, is required.

## Complexity detail

Let `N` be the length of `s`. The outer loop visits every input character once. Dictionary membership, lookup, and update are expected `O(1)` operations, and list append is amortized `O(1)`. Joining the retained characters takes `O(N)` time in the worst case. The exact source therefore runs in expected `O(N)` time.

This differs materially from the manifest, which advertises `O(N^2)` and describes recomputing nearest successors after each deletion. That description does not match the protected source. No repeated rescan occurs: compacted indices and the latest retained position make one pass sufficient.

The `ans` list can retain all `N` characters, and the returned string can also have length `N`, so overall space is `O(N)`. The `last` dictionary has at most 26 entries because the input alphabet is the lowercase English letters, making it `O(1)` under the stated contract. Excluding the required output but including the mutable construction buffer, auxiliary space is still `O(N)`. The manifest's `O(N)` space bound does match the implementation.

## Alternatives and edge cases

- **Literal repeated simulation:** Search the current string for the priority pair, delete its right endpoint, and restart. This follows the statement directly but repeatedly scans and shifts a mutable sequence; depending on the data structure and search strategy, it can take quadratic or even cubic time.
- **Original-index distance:** Comparing original loop indices is incorrect because earlier deletions shorten the current string. The source's `len(ans)` is the exact current index after all skipped characters have been removed.
- **Track every occurrence per character:** A list or deque of retained positions is unnecessary. Stability guarantees that if the newest retained equal character is too far away, every older one is farther; if it is close, no other retained equal occurrence can also be close.
- **Stack without per-character lookup:** Scanning backward through `ans` for an equal character can degrade to `O(N^2)`. The dictionary locates the only relevant retained occurrence directly.
- **Repeated equal characters:** A run such as `"aaaa"` with positive `k` keeps only its first character. Every later `a` would appear immediately after the retained one in the compacted string and is deleted.
- **Cascading closeness:** Deleting intervening characters can bring later equal characters within range. Because deleted characters are never appended, later `cur` values automatically reflect every cascade.
- **Exactly distance `k`:** The pair is eligible because the rule says at most `k`. The source correctly uses `<= k` rather than a strict comparison.
- **No equal characters:** Every character is appended, `ans` remains the original string, and the final join returns it unchanged.
- **`k` at least the string length:** Every later occurrence of a character is within range of its first surviving occurrence after compaction, so the result contains only the first occurrence of each distinct letter.
- **Dictionary indices after skips:** Skipping a new right character does not shift any character already in `ans`, so stored indices remain valid. The construction never physically deletes an element from the middle of `ans`.
- **Priority ties:** Once the processed prefix is stable, a new rightmost character has at most one close equal survivor. The smallest-left and smallest-right tie rules therefore do not require an explicit comparison in the one-pass representation.
- **Empty result:** The input is nonempty and merges always preserve the left endpoint, so at least the first input character survives. The returned string cannot be empty under this contract.
