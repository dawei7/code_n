## General

**Parse one letter-number group at a time**

The valid input alternates a lowercase letter with a positive decimal frequency, but a frequency may contain several digits.

Pointer `i` always points to the next letter. Pointer `j = i + 1` begins at its first digit. While characters are digits, the code builds the number with

`x = x * 10 + int(compressed[j])`.

Multiplying the existing prefix by ten shifts its decimal digits left, and adding the new digit appends it. For digits `'1'`, `'0'`, this produces 1 then 10.

When `j` reaches the next letter or end of string, `x` is the complete frequency belonging to `compressed[i]`. It is added to `cnt[letter]`, and `i = j` starts the next group.

**Combine repeated letters**

The same character may appear in several input groups. `Counter` accumulation adds their frequencies instead of overwriting them.

For `"a3c9b2c1"`, counts become $a:3$, $b:2$, and $c:10$.

The output requires each character once, in alphabetical order. The generator formats each counter item as `f"{k}{v}"`. Sorting these strings sorts by their first character. Since counter keys are distinct lowercase letters, later digits cannot affect the ordering between two items. Joining produces `"a3b2c10"`.


The parser invariant is that all characters before `i` have been divided into complete valid groups and their frequencies added exactly once to `cnt`.

The inner loop consumes precisely the maximal digit sequence after the current letter, reconstructing its numeric value. Adding it preserves the invariant, and the next `i` points to the next group. Valid-input guarantees prevent a missing frequency.

After parsing, `cnt[c]` equals the sum of all input frequencies for character $c$, which is its total decompressed multiplicity. Formatting one entry per key meets uniqueness, and alphabetical sorting meets ordering. The output therefore represents the same decompressed string multiset in the required better form.

**Why decompression is unnecessary**

Frequencies can reach $10^4$ per group and many groups may repeat. Expanding characters would create a much larger string only to count it again. Adding encoded counts directly preserves all needed information.

The problem explicitly permits character order to change, so aggregating by letter does not need to retain group positions.

**A detailed parser trace**

For `"a12b3a8"`, `i=0` points to `a`. The digit loop sees 1 and makes `x=1`, then sees 2 and makes `x=12`. It stops at `b` and adds 12 to `cnt["a"]`. The next group adds 3 to `b`. The final group adds another 8 to `a`, producing total 20.

Advancing `i` directly to `j` is important: `j` already points at the next letter, so no delimiter is required and no digit is reread.

The source never assumes frequency has one digit. It also never mistakes a digit for a new group because only the outer pointer position is interpreted as a letter; all subsequent consecutive digits belong to that letter.

**Output size and canonical form**

One output group is produced per distinct letter, so the result has at most 26 groups. Its frequency may be larger than any individual input frequency because repeated groups are summed. Decimal formatting naturally uses as many digits as needed.

Alphabetical order plus one group per character makes the representation canonical: two valid compressed inputs describing the same letter totals produce exactly the same better-compressed output.

**Exact data-structure note**

The manifest describes a fixed 26-slot table. The exact code uses a sparse `Counter`. With only lowercase English letters, both have constant alphabet-bounded size. The sparse form stores only letters that appear.

## Complexity detail

Let $n$ be compressed input length and $u\le26$ the number of distinct letters.

Each input character is examined a constant number of times during parsing, for $O(n)$ time. Formatting and sorting $u$ outputs costs $O(u\log u)$ plus output length. Because $u\le26$, this is constant with respect to $n$, so total time is $O(n)$.

The counter uses $O(u)$ space, constant under the fixed alphabet. Formatted parts and returned string use space proportional to output length, at most $O(n)$ plus growth from summed decimal digits; with constraints it remains linear.

Excluding output, auxiliary space is $O(1)$ under the alphabet bound.

The input string is not modified.

## Alternatives and edge cases

- **Fixed 26-element integer array:** Matches the manifest exactly and can emit indices in order without sorting.
- **Regular-expression parsing:** It can extract letter-number groups but adds engine overhead and hides the simple state machine.
- **Decompress then recount:** Potentially enormous and unnecessary.
- **Multi-digit frequency:** The multiply-by-ten recurrence parses it correctly.
- **Repeated letter groups:** Counts are added, not replaced.
- **Already better-compressed input:** Parsing and emission reproduce the same logical representation.
- **Input order not alphabetical:** Final sorting corrects it.
- **Frequency crossing a digit boundary:** Values such as 9 plus 1 become output count 10 normally.
- **No leading zeros:** The guarantee makes numeric reconstruction canonical, though the parser would still compute their numeric value.
- **One group:** It is returned in the same letter-count form.
- **Sorting formatted strings:** Safe because each begins with a unique one-character lowercase key.
- **Valid compression guarantee:** Every letter is followed by at least one digit, so `x` is never left zero for a group.
