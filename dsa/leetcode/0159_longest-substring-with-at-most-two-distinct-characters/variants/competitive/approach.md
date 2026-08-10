## General

**Represent the window with a fixed frequency table**

The competitive source maintains an inclusive window `s[start:i + 1]`.
`visited[k]` is the number of occurrences in that window whose character code
is `k`. The table has 256 entries, and `ord(char)` converts a one-character
string to its integer code.

`distinct_count` records how many table entries are positive. Keeping this
scalar avoids scanning all 256 entries after every update. `longest` stores the
maximum valid window length found so far.

The Reference restricts input to English letters. Their character codes fit
inside `[0,255]`, so every `ord(char)` is a valid table index. For arbitrary
Unicode text, this representation could raise `IndexError`; a dictionary would
be the appropriate generalization.

**Extend the right side and detect a new type**

The `for` loop supplies the next index `i` and character `char`. Before
incrementing its table entry, the source checks whether that count is zero.
If so, this character did not previously occur in the current window, and
`distinct_count` increases by one.

Then the frequency is incremented. This order matters: checking afterward
would no longer distinguish a newly introduced type from an existing one.

The previous iteration left at most two types. Adding one character can produce
at most three, so a single condition—`distinct_count > 2`—identifies whether
repair is needed.

**Shrink until one type disappears completely**

While there are more than two distinct characters, the source decrements the
frequency of `s[start]`. If that frequency becomes zero, the window no longer
contains that character and `distinct_count` decreases. Then `start` advances
one index.

Removing a character occurrence and removing a character type are not the same
event. If the left side contains several copies of the same letter, the count
remains positive through several iterations and the window still has three
types. The loop correctly continues until one type is absent.

Once the count returns to two, `i - start + 1` is the length of the current
valid substring. `longest` keeps the larger of its old value and this length.

**Why no candidate can be missed**

For each fixed `i`, the shrinking loop stops at the first `start` that restores
validity. Any later start produces a shorter substring ending at the same
position. Thus the measured window is the longest valid one ending at `i`.

Every substring has some right endpoint. When the algorithm reaches that
endpoint, its maintained window is at least as long as any other valid window
ending there. Comparing all these lengths is enough to find the global maximum.

The left boundary never decreases. Once a prefix has been removed to satisfy
the constraint, adding more characters on the right cannot make that discarded
prefix useful again. Across the entire algorithm, each index enters the window
once and leaves at most once.

**Trace the frequency changes**

For `"eceba"`, the first three characters create frequencies `e:2` and `c:1`,
so `longest` reaches three.

Adding `b` changes its count from zero to one and raises `distinct_count` to
three. Removing the first `e` leaves `e:1`, so the count is still three.
Removing `c` changes its frequency to zero; `distinct_count` becomes two and
the window begins at the second `e`.

Adding `a` again creates a third type. Removing that `e` makes its count zero,
leaving the valid window `"ba"`. The recorded maximum remains three.

For `"ccaabbb"`, introducing `b` forces both leading `c` occurrences out.
Once the `c` frequency reaches zero, the window contains only `a` and `b` and
can grow to `"aabbb"` of length five.

**Maintain exact state**

After the repair loop:

- every `visited` entry equals its frequency in `s[start:i + 1]`;
- `distinct_count` equals the number of positive entries and is at most two;
- the current window is the longest valid one ending at `i`;
- `longest` is the best length among all processed endpoints.

The insertion code preserves frequency accuracy, the removal code updates both
frequencies and the distinct scalar exactly when a type disappears, and the
maximum update preserves the final claim. These facts prove the returned value.

## Complexity detail

Let $n$ be `len(s)`. The right endpoint advances $n$ times. `start` advances at
most $n$ times total, even though its work is written inside a `while` loop.
Every table lookup and arithmetic operation is constant time. Total time is
$O(n)$.

The frequency table always has 256 integer slots, independent of $n$, and all
other state is scalar. Auxiliary space is $O(256)=O(1)$. This matches the
manifest under the English-letter contract.

The list comprehension that creates `visited` performs 256 initializations;
that is a fixed constant rather than input-dependent work.

## Alternatives and edge cases

- **Sparse `Counter`:** Tracks only characters present in the current window and naturally supports Unicode, with expected constant-time hash operations.
- **Rightmost-position map:** With at most three entries, evict the character whose final occurrence is farthest left and jump `start` directly.
- **Enumerate all substrings:** Correct but can require quadratic time before counting work.
- **Empty string outside the stated lower bound:** The loop would return zero gracefully.
- **Single repeated letter:** `distinct_count` stays one and the entire string is measured.
- **Alternating two letters:** No shrinking occurs; the complete string is valid.
- **Third distinct letter:** The loop may remove many occurrences before a frequency becomes zero.
- **Character-code assumption:** The 256-entry array is safe for English letters but not for general Unicode input.
- **At most versus exactly two:** Windows containing one distinct character are valid and must be considered.
- **Contiguous requirement:** Advancing `start` removes a prefix; the algorithm never skips characters inside its substring.
