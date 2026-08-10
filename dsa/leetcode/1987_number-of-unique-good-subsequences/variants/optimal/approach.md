## General

**Separate subsequences by their final character**

Every good subsequence other than the special string `"0"` must begin with one. The source tracks unique such strings in two conceptual groups:

- `f` is the number ending in one;
- `g` is the number ending in zero.

Only the counts are stored, not the strings themselves. Grouping by last character is enough to update distinct subsequences without retaining an exponential set.

The variable `ans` is named like a running total, but during the loop it serves only as a Boolean-style flag for whether a zero has appeared. It becomes one on any zero and never needs to exceed one, because all occurrences of the standalone subsequence `"0"` represent the same unique string.

**Process a new one**

When the current character is one, every previously known good string that starts with one can have this character appended. Appending one to the `f + g` distinct prior strings yields distinct strings ending in one. The standalone string `"1"` is another possibility.

The update is therefore

`f = f + g + 1`

modulo $10^9+7$.

This assignment replaces the old ending-one count rather than adding to it separately. Every previously known string ending in one is already represented among the new construction set: remove its final one to obtain a possibly empty subsequence that existed before the current position. Processing the later equal character regenerates that same string. Replacement is the standard way the recurrence removes duplicates caused by repeated characters.

`g` does not change because a newly processed one cannot create a new string ending in zero.

**Process a new zero**

Appending zero to every previously known string that begins with one creates `f + g` distinct good strings ending in zero. Their prefixes differ, so their appended results differ.

The update

`g = g + f`

again replaces the old conceptual set with all strings obtainable by ending at the current zero. Previously known ending-zero strings are regenerated through an earlier valid prefix in the same last-character deduplication logic.

The method does not add a standalone zero to `g`, because `g` is reserved for strings that start with one. Instead, `ans = 1` records the one exceptional valid string `"0"`.

Leading-zero strings such as `"00"` and `"01"` are never introduced: a zero is appended only to strings already beginning in one, and the standalone zero is never extended through these states.

**Trace `"101"`**

Start with `f=0`, `g=0`, and zero flag `ans=0`.

The first one gives `f=1`, representing `"1"`.

The zero gives `g=1`, representing `"10"`, and sets the standalone-zero flag.

The final one updates `f` to `1 + 1 + 1 = 3`, representing unique strings `"1"`, `"11"`, and `"101"`. `g` still represents `"10"`. Adding the special `"0"` gives five unique good subsequences.

**Trace repeated ones**

For `"11"`, the first one sets `f=1`. The second sets `f=2`, representing `"1"` and `"11"`. It does not produce two copies of `"1"` even though either input occurrence can form it, because the recurrence counts distinct strings rather than index selections.

**Why the recurrence is correct**

After each processed prefix, assume `f` and `g` count exactly the unique nonzero-leading good strings ending in their named character. Appending the current character to every prior nonzero-leading string, plus the singleton when the character is one, describes all valid strings whose chosen last occurrence is current.

Using the current occurrence regenerates all older strings ending in the same character, so replacement deduplicates them while including every genuinely new extension. The other ending-character group remains unchanged. A zero separately records the sole valid leading-zero exception.

By induction, after the full scan, the three categories are disjoint and exhaustive: strings ending one, nontrivial strings ending zero but starting one, and standalone zero. Their sum is the required number.

**Modulo placement**

Each `f` or `g` update is reduced immediately. Addition and later recurrence use only modular arithmetic, so the final residue is unchanged. The zero flag is already only zero or one. The final expression reduces `ans + f + g` once more.

## Complexity detail

Let $N$ be the binary string length. The loop reads each character once and performs constant arithmetic, so time is $O(N)$. This is optimal because an unseen character could change whether `"0"` or additional subsequences exist.

Only `f`, `g`, `ans`, the modulus, and the loop character are stored. Auxiliary space is $O(1)$, independent of the exponentially large conceptual set of subsequences.

## Alternatives and edge cases

- **Generate every subsequence:** There are $2^N$ index selections and many duplicates, making enumeration infeasible for $N=10^5$.
- **Store all distinct strings in a set:** Correct only for tiny input and consumes exponential total string space.
- **General distinct-subsequence DP:** One can track last occurrences, but the two-character and leading-zero structure permits this smaller recurrence.
- **All zeroes:** `f` and `g` stay zero, while the standalone-zero flag makes the answer one.
- **All ones:** The unique good strings are one through $N$ repeated ones, and `f` grows to $N$.
- **Single zero:** The answer is one.
- **Single one:** The answer is one.
- **Leading zeros before the first one:** They contribute only the unique standalone `"0"` and cannot prefix other good strings.
- **Repeated characters:** Replacement-style updates prevent counting the same resulting string multiple times.
- **Zero after a valid prefix:** It can extend every nonzero-leading state and contributes to `g`.
- **Modulo:** Counts are reduced at every growing-state update.
- **Input preservation:** The solution scans the immutable string without constructing subsequences.
