## General

**Separate frequency counting from category selection**

The task asks for two independent maxima:

- the largest frequency among vowels `a,e,i,o,u`;
- the largest frequency among all other lowercase letters.

It does not ask which letters attain those maxima, and ties may be resolved arbitrarily. Therefore, first count every distinct character, then update one of two running maxima based on its category.

The source uses:

`cnt = Counter(s)`.

After this pass, `cnt[c]` is the exact number of occurrences of letter `c`.

**Maintain one maximum for each category**

`a` stores the greatest vowel frequency seen so far, and `b` stores the greatest consonant frequency. Both begin at zero.

For every `(character,frequency)` pair:

- if `character in "aeiou"`, update `a = max(a,frequency)`;
- otherwise, update `b = max(b,frequency)`.

The input contains only lowercase English letters, so every non-vowel is a consonant for this problem. There are no digits, spaces, punctuation marks, or uppercase characters requiring another category.

**Why zero initialization handles missing categories**

If the string has no vowels, no loop iteration updates `a`, so it remains zero. That is exactly the rule for a missing category.

The same applies to `b` when every character is a vowel. No separate boolean or postprocessing condition is needed.

**Why ties need no special logic**

Suppose two vowels both occur three times. Updating with `max` leaves `a=3` regardless of which vowel is visited first. The output needs only the frequency, not a chosen letter.

Counter iteration order therefore cannot affect the result.

**A trace for successes**

`Counter("successes")` contains frequencies including:

- `s:4`;
- `c:2`;
- `u:1`;
- `e:2`.

The vowel branch raises `a` first to one and then two. The consonant branch raises `b` to four. Returning `a+b` gives six.


After processing any subset of counter entries:

- `a` is the maximum frequency among processed vowels, or zero if none;
- `b` is the maximum frequency among processed consonants, or zero if none.

Each next entry belongs to exactly one category, and taking the maximum updates precisely that category's invariant. After all entries, the two values are the requested maxima. Their sum is therefore the required answer.

**Why raw string scanning could also work**

The source first aggregates counts, then finds maxima. Updating maxima directly while frequencies are still growing would require revisiting a category's current maximum carefully, but a 26-slot count array could support the same two-stage idea.

Counter makes the code concise and stores only letters that occur.

**Do not confuse the maximum frequency with the category size**

For a category, the algorithm is looking for one letter with the greatest count. If vowel counts are `a:3`, `e:2`, and `i:2`, the required vowel contribution is three, not seven and not the number three of distinct vowel letters. The same distinction applies to consonants.

This is why `a` and `b` are updated with `max` rather than addition. `Counter` has already performed the only additions that belong in the solution: combining repeated occurrences of the same character. Once those per-letter totals exist, letters compete inside their category instead of being combined.

**Why examining only present characters is complete**

The loop visits `cnt.items()` rather than all 26 letters. Any absent letter has frequency zero. It cannot improve a positive maximum, and if an entire category is absent, that category's initialized maximum already remains zero. Thus omitting absent letters is equivalent to explicitly comparing their zero counts.

Every present lowercase letter belongs to exactly one branch, because the five vowels and the consonant complement partition the alphabet. No frequency is skipped or considered twice.

**A useful sanity bound**

Each maximum is at most `len(s)`, but the two winning letters are from disjoint categories. Their occurrences are disjoint positions in the string, so:

`0 <= a + b <= len(s)`.

This gives a quick way to detect an implementation that accidentally adds category totals or double-counts one character.

## Complexity detail

Let `n = len(s)`. Building the Counter scans `n` characters, taking `O(n)` expected time. The second loop visits at most 26 distinct lowercase letters, which is `O(1)` under the fixed alphabet. Total time is `O(n)`.

The Counter stores at most 26 entries. Because the alphabet size is a fixed problem constant, auxiliary space is `O(1)`, matching the manifest. If generalized to an unbounded alphabet, the same implementation would use `O(U)` for `U` distinct characters.

Membership testing in the five-character vowel string is constant time.

## Alternatives and edge cases

- **Use a 26-element frequency array:** This avoids hashing and also gives `O(n)` time and fixed space.
- **Sort the characters:** Frequencies can be grouped after sorting, but `O(n log n)` work is unnecessary.
- **Track only the globally most frequent letter:** The answer requires one maximum from each category, not merely the overall maximum.
- **Sum all vowel and consonant counts:** The task asks for maximum individual-letter frequencies, not category totals.
- **No vowels:** `a` remains zero and only the consonant maximum contributes.
- **No consonants:** `b` remains zero and only the vowel maximum contributes.
- **One-character string:** Its category maximum is one and the other is zero.
- **Tied vowels:** Any tied letter is acceptable; the stored frequency is the same.
- **Tied consonants:** The same reasoning applies.
- **All letters identical:** That letter's full string length becomes its category maximum.
- **Lowercase guarantee:** The membership string lists every vowel relevant to the input domain.
- **Counter order:** Explicit maximum operations make iteration order irrelevant.
- **Fixed alphabet complexity:** Storing up to 26 counts is conventionally `O(1)` rather than `O(n)`.
