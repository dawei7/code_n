## General

**Reduce the license plate to required letter counts**

Digits and spaces in `licensePlate` do not matter. Letters are case-insensitive, and repeated letters create repeated requirements.

The exact solution builds

`cnt = Counter(c.lower() for c in licensePlate if c.isalpha())`.

Each alphabetic character is converted to lowercase before counting. If the plate contains two copies of `s`, `cnt["s"]` is two; a candidate with only one `s` cannot complete it.

Under the input contract, alphabetic characters are English letters. The 26-letter alphabet keeps the count structure constant-sized.

**Test whether a word covers the multiset**

For a candidate word `w`, `t = Counter(w)` records its lowercase letter frequencies. Candidate words are already guaranteed lowercase.

The condition

`all(v <= t[c] for c, v in cnt.items())`

checks every required letter. A candidate may contain extra letters or extra copies; only shortages matter.

This is multiset containment, not ordinary set containment. Checking only whether each distinct letter appears would incorrectly accept a word with too few repetitions.

**Keep the shortest eligible word**

`ans` begins as `None`. Whenever a completing word is found, it becomes the current best.

Before counting a later word, the solution skips it when

`ans and len(w) >= len(ans)`.

If `w` is longer, it cannot improve the objective. If it has equal length, the earlier current answer must win the tie, so it also must not replace `ans`. This early skip both preserves the first-occurrence rule and avoids constructing an unnecessary counter.

Only a strictly shorter word is tested after an answer exists.

**Why input-order scanning resolves ties**

Words are processed from first to last. The first completing word of some length becomes the answer unless a strictly shorter completing word appears later. Once the best length is known, equal-length later words are ignored.

Therefore, after the scan, `ans` is the earliest word among all completing words of minimum length.

**Trace `"1s3 PSt"`**

Filtering digits and the space, then lowercasing, gives requirements:

- `s` twice
- `p` once
- `t` once

`"step"` has only one `s` and fails. `"steps"` has both copies plus `p` and `t`, so it becomes the answer. Words missing the second `s` fail even if they contain every distinct required letter.

**Trace a tie**

For plate `"1s3 456"`, only one `s` is required. Suppose `"pest"`, `"stew"`, and `"show"` all complete the plate and have length four.

`"pest"` is the first such word and becomes `ans`. The other length-four words satisfy `len(w) >= len(ans)` and are skipped, preserving `"pest"` as required.

**Why a later shorter word can still replace the answer**

The early condition skips only lengths greater than or equal to the current best. A shorter word proceeds to the counter check. If it completes the plate, it replaces `ans` because shorter length has priority over input position.

Input order is a tiebreaker only after minimum length is fixed.

**Why the method is correct**

The plate counter exactly represents every relevant letter and multiplicity after ignoring case, digits, and spaces. A word passes the `all` test exactly when its counter contains at least those counts, so eligibility is exact.

During the left-to-right scan, `ans` is always the earliest completing word of the smallest completing length seen so far. A longer or equal candidate cannot improve this invariant, while a shorter completing candidate correctly replaces it. The existence guarantee ensures `ans` is a string by the end. Thus the returned word satisfies both shortest length and earliest tie position.

## Complexity detail

Let `C` be the total number of characters in the license plate and all words. Building the plate counter is linear in plate length. Each word that is not skipped is counted in time proportional to its length, and checking requirements examines at most 26 letters.

Across the complete input, time is `O(C)`. Early length skips can reduce actual work but do not worsen the bound.

Both counters contain at most 26 lowercase English-letter keys, so their auxiliary size is `O(1)` with respect to input length. `ans` stores a reference to an existing word. If the alphabet were unbounded, the counter space would instead depend on the number of distinct characters.

## Alternatives and edge cases

- **Fixed 26-element arrays:** Convert letters to indices and compare counts. This avoids hash maps and has the same linear time and constant alphabet space.

- **Sort plate letters and candidate letters:** A two-pointer containment check can work, but sorting every word adds unnecessary logarithmic factors.

- **Use sets instead of counters:** This loses multiplicity and fails when a plate letter appears more than once.

- **Normalize digits as characters:** Digits and spaces must be ignored entirely, not required in candidates.

- **Uppercase plate letters:** Lowercasing before counting makes them match lowercase candidate letters.

- **Equal-length completing words:** The first one remains because later equal lengths are skipped.

- **Later shorter completing word:** It is still tested and replaces the longer current answer.

- **Extra candidate letters:** They are harmless; every required count only needs to be met or exceeded.

- **Guaranteed answer:** The exact source returns `ans` directly. Under the contract it cannot remain `None`.

- **Very short license requirement:** Even a single required letter uses the same multiset logic and tie handling.
