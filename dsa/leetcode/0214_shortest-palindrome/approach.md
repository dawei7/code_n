## General

**Reduce the construction problem to one palindromic prefix**

The original string `s` must remain intact as the suffix of the answer because
characters may be added only in front. Suppose the longest prefix of `s` that
is already a palindrome has length `idx`. Split the string into
`p = s[:idx]` and `t = s[idx:]`. Since `p` is a palindrome, prepending the
reverse of `t` produces

$$
\operatorname{reverse}(t) + p + t.
$$

The left and right copies of `t` mirror each other, and the middle `p` mirrors
itself, so this entire string is a palindrome. In code, that construction is
`s[idx:][::-1] + s`.

Using the longest palindromic prefix is what makes the result shortest. Any
characters of `s` outside the chosen prefix must be mirrored by newly prepended
characters. A shorter palindromic prefix leaves a longer suffix `t` and thus
requires more additions. Conversely, if some construction added fewer than
`len(t)` characters, a longer initial portion of `s` would have to occupy the
self-mirroring center, implying a palindromic prefix longer than the one chosen.

The real task is therefore to find the greatest prefix length that is
palindromic.

**Compare a prefix with its own reverse using two rolling hashes**

The exact solution scans `s` once and maintains two polynomial hashes for the
prefix ending at the current character. Each lowercase character is mapped to
an integer from 1 through 26 with `ord(c) - ord('a') + 1`. Mapping `a` to 1
rather than 0 prevents leading `a` characters from disappearing algebraically.

Let the mapped values of a length-$k$ prefix be
$v_0, v_1, \ldots, v_{k-1}$ and let the base be $b=131$. Before applying the
modulus, `prefix` represents

$$
v_0b^{k-1} + v_1b^{k-2} + \cdots + v_{k-2}b + v_{k-1},
$$

while `suffix` represents

$$
v_0 + v_1b + \cdots + v_{k-2}b^{k-2} + v_{k-1}b^{k-1}.
$$

The second expression is the first expression with character order reversed.
If the prefix is a palindrome, its value sequence reads the same in both
directions, so these two polynomial values are equal.

Both hashes are stored modulo `10**9 + 7` to keep numbers bounded. The variable
`mul` holds the next power of 131 needed by the reverse-direction hash. It
starts at 1, which is $131^0$.

**How each character updates the three values**

For each character value `v`, the statement conceptually represented by
`prefix = (prefix * base + v) % mod` shifts every existing coefficient one
power higher and places `v` at power zero. This is the ordinary left-to-right
polynomial hash update.

The update `suffix = (suffix + v * mul) % mod` places the new character at the
highest power used so far. Then `mul = (mul * base) % mod` advances the power
for the next iteration. Thus, after processing index `i`, both hashes describe
exactly `s[:i + 1]`, but in opposite reading directions.

Whenever `prefix == suffix`, the source assigns `idx = i + 1`. The `+1`
converts the zero-based ending index into a prefix length, which is also the
slice boundary required later. Because scanning proceeds from left to right,
every later equality overwrites an earlier one, leaving `idx` at the longest
hash-matching prefix.

**Trace a short non-palindrome**

For `s = "abcd"`, the one-character prefix `a` has identical forward and
reverse hashes, so `idx` becomes 1. At prefix `ab`, the forward coefficients
are `1 * 131 + 2`, while the reverse coefficients are
`1 + 2 * 131`; they differ. The longer prefixes also do not match, so `idx`
remains 1.

The unmirrored suffix is `s[1:] = "bcd"`. Reversing it gives `"dcb"`, and the
method returns `"dcb" + "abcd" = "dcbabcd"`. The central `a` is the longest
palindromic prefix, and the remaining characters appear in mirrored order on
both sides.

For `s = "aacecaaa"`, hash equality is last observed at prefix length 7,
corresponding to `"aacecaa"`. The remaining suffix is one `a`, so exactly that
character is prepended to obtain `"aaacecaaa"`.

**Already-palindromic and empty inputs avoid extra construction**

If the full string produces equal hashes, the final update sets `idx = n`.
The conditional return then returns `s` itself instead of creating an empty
suffix slice, reversing it, and concatenating. For the empty string, the loop
does not execute, but both `idx` and `n` are zero, so the same branch correctly
returns the empty string.

**The exact source is randomized-style hashing, not the manifest's KMP**

The current manifest summary says this branch uses a KMP prefix function, but
the exact solution contains no prefix table. It uses one modular rolling hash.
This distinction affects the guarantee.

Every real palindromic prefix makes the two hashes equal, so the method does
not miss a palindrome because of hashing. However, modular hash equality does
not prove that two strings are equal: different coefficient sequences can
have the same remainder modulo `10**9 + 7`. Such a collision could cause the
code to treat a non-palindromic prefix as palindromic. If the colliding prefix
is the last equality seen, the returned construction may be non-palindromic or
not shortest.

The large prime modulus and base 131 make accidental collisions unlikely on
ordinary judge data, but the algorithm is probabilistic rather than
collision-free. A KMP prefix-function implementation gives deterministic
$O(n)$ behavior and matches the manifest summary. Since this document must
teach the executable optimal source, it explains the rolling hash and states
its collision caveat instead of presenting KMP as though that were the code.

Subject to the no-collision assumption, equality occurs exactly at
palindromic prefixes. The scan retains the longest one, and the reverse-suffix
construction derived above then proves both palindromicity and minimality.

## Complexity detail

Let $n$ be `len(s)`. The loop performs one constant number of modular
arithmetic operations per character, taking $O(n)$ time. Extracting the suffix,
reversing it, and concatenating it with `s` also take $O(n)$ time in the worst
case. Total time is $O(n)$.

The hash state—`prefix`, `suffix`, `mul`, `idx`, `base`, and `mod`—uses
$O(1)$ auxiliary space. Python's suffix slice, reversed slice, and returned
string require $O(n)$ memory, so the exact end-to-end implementation uses
$O(n)$ space, matching the manifest. If the mandatory returned string is
excluded from auxiliary-space accounting, temporary slicing still reaches
$O(n)$ when a long suffix must be prepended.

## Alternatives and edge cases

- **KMP prefix function:** Build `s + separator + reversed(s)` and use the final prefix-function value as the longest palindromic-prefix length. It is deterministic, runs in $O(n)$ time and $O(n)$ space, and is the technique named by the current manifest even though the exact source instead hashes.
- **Double rolling hash plus verification:** Two independent moduli make collision probability much smaller; directly verifying the final candidate prefix removes the immediate false positive, though finding a fallback after a failed verification needs care to preserve linear time.
- **Manacher's algorithm:** It deterministically finds all palindrome radii in $O(n)$ time and can select the longest one touching index 0. It is more intricate than necessary for this prefix-only goal.
- **Check prefixes from longest to shortest:** Compare each prefix with its reversal and stop at the first palindrome. It is simple but repeated slicing and comparison can take $O(n^2)$ time at the maximum length $5 \cdot 10^4$.
- **Empty string:** The scan has no iterations, `idx == n == 0`, and the method returns `""` without indexing any character.
- **One character:** Its two hashes match immediately, so the method returns the original one-character palindrome.
- **The whole string is a palindrome:** The last iteration sets `idx` to $n$, and no characters are added.
- **Only the first character is palindromic:** Every nonempty string has at least a one-character palindromic prefix. Reversing all characters after index 0 produces the required answer, as in `"abcd"`.
- **Repeated characters:** A string such as `"aaaa"` updates `idx` at every position and is returned unchanged. Repetition is handled by coefficients, not by a special case.
- **Separator choice:** The exact rolling-hash source does not concatenate strings and therefore needs no separator. A KMP alternative must use a delimiter outside the lowercase input alphabet to prevent a match from crossing the boundary incorrectly.
- **Hash collision:** This is a semantic edge case, not merely a performance issue. One modular equality can be a false positive; applications requiring unconditional correctness should prefer deterministic KMP or Manacher rather than relying on the accepted-source probability.
- **Input preservation:** Strings are immutable in Python. The method creates new strings for the suffix and result but never changes `s`.
