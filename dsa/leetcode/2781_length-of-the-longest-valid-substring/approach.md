## General

**Maintain the longest valid suffix ending at each position**

The exact solution scans `word` from left to right. After processing right endpoint `j`, variable `i` is the earliest starting index such that `word[i:j + 1]` contains no forbidden substring. The current valid window length is therefore `j - i + 1`.

When one new character at `j` is appended, every substring that existed entirely before `j` was already handled at the previous step. The only newly created forbidden occurrence could be a substring that ends exactly at `j`. This observation reduces the work from examining every substring inside the window to examining only suffixes ending at the new character.

**Store forbidden strings for direct membership tests**

`s = set(forbidden)` converts the list into a hash set. A candidate suffix can then be tested with expected constant-time membership after its string contents are hashed.

The critical constraint is that every forbidden string has length at most ten. Therefore, at each endpoint, only the last ten possible suffix lengths can matter. A longer suffix cannot itself equal any member of `forbidden`.

**Decode the inner loop's bounds**

For endpoint `j`, the loop is:

`for k in range(j, max(j - 10, i - 1), -1)`.

It considers starts `k` in descending order:

- `k = j` gives suffix length one;
- `k = j - 1` gives length two;
- and so on through at most length ten;
- it never goes below the current valid start `i`.

Python's stop bound is exclusive. If `j - 10` is the maximum bound, the last included start is `j - 9`, producing length ten. If `i - 1` is larger, the last included start is `i`. Thus the code checks exactly the relevant suffixes that lie inside the current window.

**Why shortest suffixes are checked first**

As `k` decreases, `word[k:j + 1]` becomes longer and starts farther left. If several forbidden strings end at `j`, restoring validity requires moving `i` beyond the occurrence with the largest start index. The loop begins with that largest possible `k` and moves left.

At the first match, it sets `i = k + 1` and breaks. Any later, longer matching suffix would begin at a smaller `k` and would require moving `i` less far. The first match therefore imposes the strongest boundary update.

For example, if both `"b"` and `"ab"` are forbidden and the current text ends in `"ab"`, the one-character suffix `"b"` is found first. Moving past that `b` also removes the longer occurrence, and it gives the earliest valid start after excluding both.

**Why old forbidden occurrences stay excluded**

Before adding `word[j]`, the prior window `word[i:j]` is valid by the maintained invariant. Any forbidden occurrence ending before `j` either lies before `i` or was the reason `i` moved right earlier. Since `i` never decreases, such an occurrence cannot re-enter the active window.

After appending the new character, checking all possible forbidden suffixes ending at `j` covers every new threat. If none is found, the old `i` remains valid. If one is found at `k`, moving to `k + 1` excludes it and every other match ending at `j`, while old occurrences remain excluded as well.

**A walkthrough**

For `word = "cbaaaabc"` and forbidden set `{"aaa", "cb"}`:

- At `j = 0`, `"c"` is allowed, so the window length is one.
- At `j = 1`, suffix `"b"` is allowed but `"cb"` is forbidden. The boundary moves from zero to one, leaving `"b"`.
- As the run of `a` characters grows, suffixes of length one and two remain allowed.
- When an `"aaa"` suffix appears, its start `k` causes `i = k + 1`, removing the first character of that forbidden triple from the window.

At every endpoint, `ans` records the maximum valid window length, eventually reaching four for `"aabc"`.

**Why the window is the longest valid one for its endpoint**

After processing `j`, the active window is valid by the suffix argument. It is also impossible to choose an earlier start than `i`. Every time `i` moved to `k + 1`, a forbidden occurrence began at `k` and ended at the then-current endpoint. Any future window starting at or before `k` would still contain that occurrence. Therefore the boundary never moves farther than necessary but can never safely move back.

All substrings ending at `j` and starting at or after `i` are valid because they are contained in the valid active window. The longest of them starts at `i`, giving length `j - i + 1`.

**Why the global maximum is correct**

Every substring has one right endpoint. At each endpoint, the method computes the longest valid substring ending there. Taking the maximum of those lengths considers a candidate at every possible ending position. Hence it finds the overall longest valid substring.

The empty substring mentioned in the definition never needs explicit handling because `word` is nonempty and a positive-length valid character may or may not exist. If every single character is forbidden, boundary updates make each current length zero and `ans` remains zero.

## Complexity detail

Let `n` be `word.length` and let `S` be the total number of characters across the forbidden list. Building the set takes expected `O(S)` time and `O(S)` space.

For each of `n` endpoints, the inner loop checks at most ten suffixes. Each slice has length at most ten, so slicing and hashing are constant under this fixed constraint. The scan is `O(n)`, making total expected time `O(n + S)`.

The set owns `O(S)` string data. Temporary slices are at most ten characters and only a constant number are live at once, so scan auxiliary space is `O(1)` beyond the set. Total auxiliary space is `O(S)`.

If the maximum forbidden length were a variable `L` rather than the fixed ten, Python slicing and hashing could make the scan `O(nL^2)` in a direct accounting. The stated bound relies on `L <= 10`.

## Alternatives and edge cases

- **Check every substring:** Enumerating all starts and ends is quadratic before membership costs and ignores the ten-character maximum.
- **Trie of reversed forbidden strings:** Walking backward through a trie avoids substring slicing and generalizes well when the maximum forbidden length is larger.
- **Aho–Corasick automaton:** It finds all forbidden occurrences in linear text time but is much more machinery than the fixed length-ten bound requires.
- **Forbidden string of length one:** When that character appears, `i` becomes `j + 1` and the current valid length is zero.
- **Several forbidden suffixes end together:** Checking starts from largest to smallest and breaking on the first match applies the strongest necessary boundary.
- **Forbidden occurrence starts before `i`:** It is already outside the active window, so the loop deliberately does not inspect it.
- **No forbidden string appears:** `i` stays zero and the answer becomes the whole word length.
- **Repeated forbidden entries:** Converting to a set removes duplicates without changing membership semantics.
- **Overlapping occurrences:** Monotonic boundary movement excludes each occurrence as soon as its endpoint is processed.
- **All characters individually forbidden:** Every active window becomes empty and the method returns zero.
- **Maximum-length forbidden string:** The exclusive bound still includes the suffix of length ten.
- **Input preservation:** The algorithm slices and reads `word` but never modifies it.
