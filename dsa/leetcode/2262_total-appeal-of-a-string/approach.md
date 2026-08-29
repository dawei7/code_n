## General

**Group substrings by where they end**

Listing every substring and building a distinct-character set for each one repeats enormous amounts of work. The solution instead processes `s` from left to right and groups substrings by their ending index.

At index `i`, exactly `i + 1` substrings end there: they start at positions zero through `i`. The variable `t` represents the sum of the appeals of all those ending-at-`i` substrings. The variable `ans` accumulates these per-ending sums. Since every non-empty substring has exactly one ending index, adding each `t` to `ans` counts every substring's appeal exactly once.

The remaining question is how to update `t` when a new character is appended.

**Extend all previous substrings with the current character**

Suppose the current character `c` is at index `i`. Every substring that ended at `i - 1` can be extended with `c`, and there is also the new one-character substring `s[i:i + 1]`. Appending `c` increases a particular substring's appeal by one only when that substring did not already contain `c`. If it did contain `c`, its set of distinct characters is unchanged.

The array `pos` stores the most recent index of each lowercase letter. After converting `c` to an integer from zero to 25, `pos[c]` is the last position at which this same letter appeared, or minus one if it has never appeared.

Let that previous position be `p`. A substring ending at `i` contains no earlier `c` precisely when its start lies after `p`. The allowed start positions are

$$
p + 1, p + 2, \ldots, i.
$$

There are `i - p` of them. For each of these substrings, the current `c` contributes one new distinct character. For every substring starting at or before `p`, an older `c` is already present, so the appeal does not increase.

This gives the update

`t += i - pos[c]`.

**Why the minus-one initialization handles first occurrences**

Every entry of `pos` starts at minus one. If `c` has never appeared and is now at index `i`, then the increment is `i - (-1) = i + 1`. That is exactly the number of substrings ending at `i`. All of them contain `c` for the first time, so all of their appeals increase by one.

This sentinel removes the need for a special first-occurrence branch. The same formula works for both unseen and repeated letters.

**Preserve the old position until after the contribution**

The line `pos[c] = i` occurs only after `t` and `ans` have been updated. The calculation needs the previous occurrence, not the current one. If the position were overwritten first, `i - pos[c]` would be zero, and the current character would contribute nothing even to the one-character substring.

Once the current contribution is counted, storing `i` prepares the array for the next copy of this letter.

**Trace the running total for** `"abbca"`

The state evolves as follows:

- At index zero, `'a'` was last at minus one. The increment is one, so `t = 1` and `ans = 1`.
- At index one, `'b'` was last at minus one. The increment is two, so `t = 3` and `ans = 4`.
- At index two, `'b'` was last at one. Only the substring `"b"` starting at index two gains a new distinct letter, so the increment is one. Now `t = 4` and `ans = 8`.
- At index three, `'c'` is new. All four substrings ending there gain `'c'`, so `t = 8` and `ans = 16`.
- At index four, the previous `'a'` was at zero. The starts one through four produce four substrings that did not already contain `'a'`, so `t = 12` and `ans = 28`.

The final value 28 agrees with summing appeals by explicitly listing the substrings, but the algorithm never constructs any of them.

**Why** `t` **has the claimed meaning**

Before processing index `i`, `t` is the total appeal of all substrings ending at `i - 1`. Extending those substrings preserves all distinct characters already present. The new character adds exactly one to the `i - p` extensions whose starting positions are after its last occurrence. The count also includes start `i`, which represents the newly created one-character substring. Therefore, adding `i - p` transforms `t` into the total appeal of every substring ending at `i`.

This inductive statement begins correctly at index zero: the only substring is one character long, and the minus-one formula sets `t` to one.

**Why summing** `t` **produces the global answer**

After the update for index `i`, `t` contains the appeal sum of one disjoint group: all substrings whose right endpoint is `i`. The groups for different indices do not overlap because a substring cannot have two different endpoints, and together they include all non-empty substrings. Adding `t` once per index therefore produces exactly the total appeal requested.

Another way to view the formula is by contributions. Each occurrence of a letter becomes the representative occurrence of that letter for substrings that start after the preceding copy and end at or after the current index. The running `t` method accumulates those contributions online rather than calculating their entire future influence at once.

**Why the alphabet array is enough**

The source guarantees lowercase English letters. Subtracting `ord('a')` from `ord(c)` maps them contiguously to zero through 25, so a fixed 26-entry array can store all latest positions. A dictionary would also work, but it would add hashing overhead without supporting any additional needed characters.

## Complexity detail

Let `n` be the length of `s`. The loop visits each character once and performs constant-time arithmetic plus two fixed-array accesses. The total running time is `O(n)`.

The `pos` array always has exactly 26 entries, independent of `n`. Apart from it, the method stores only counters and the current character index. Auxiliary space is therefore `O(1)` under the fixed lowercase-English alphabet.

The answer can be much larger than `n` because there are `n(n+1)/2` substrings. Python integers expand automatically. In a fixed-width language, a 64-bit integer should be used for `t` and `ans`; a 32-bit total is not sufficient for the maximum input length.

No substring, set, or prefix table is allocated, and the input string is immutable.

## Alternatives and edge cases

- **Enumerate substrings and build a set:** Constructing every substring and recounting distinct letters can take cubic time, which is infeasible for `n = 10^5`.
- **Extend a set for each starting index:** This avoids rescanning each substring internally but still examines `O(n^2)` start-end pairs.
- **Count each occurrence's future contribution:** For a character at index `i` with previous occurrence `p`, its direct contribution is `(i - p)(n - i)`. Summing that formula is another valid linear-time view; the exact solution instead maintains totals by ending index.
- **Dictionary of last positions:** It generalizes to arbitrary alphabets but offers no asymptotic benefit for the guaranteed 26 lowercase letters.
- **All characters equal:** The increment is always one after the first position, so `t` equals the number of substrings ending there times appeal one, and the total becomes `n(n+1)/2`.
- **All characters different:** At index `i`, every ending substring gains the new character, so the increment is `i + 1`.
- **A character reappears immediately:** If its previous position is `i - 1`, only the one-character substring beginning at `i` gains that character, and the increment is one.
- **A character reappears after a gap:** Exactly the starts after its preceding occurrence gain it; the gap length `i - pos[c]` counts those starts.
- **Single-character string:** The initialized last position is minus one, making `t = 1` and `ans = 1`.
- **Position-update order:** `pos[c]` must be read before it is replaced by `i`, or every increment would incorrectly be zero.
- **Repeated substring contents:** Each occurrence is still a different substring by index and must contribute separately; grouping by ending index correctly includes every occurrence.
- **Distinctness inside a substring:** The formula adds a character only when the chosen start excludes its previous occurrence, precisely matching set distinctness.
- **Large result:** Use wide integer arithmetic outside Python even though the character positions themselves fit in ordinary integers.
- **Fixed alphabet:** The `O(1)` space statement depends on the guarantee of lowercase English letters.
- **Input preservation:** The method reads characters only and performs no string reconstruction or mutation.
