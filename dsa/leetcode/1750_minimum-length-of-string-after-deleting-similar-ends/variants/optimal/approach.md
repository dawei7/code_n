## General

**Represent deletions with two boundaries**

Only a prefix and suffix of the current string can be deleted. After any number of operations, the characters that remain therefore form one contiguous interval of the original string.

The exact solution stores that interval with `i` as its leftmost index and `j` as its rightmost index. Initially they are zero and `len(s) - 1`, so the whole string remains. Moving `i` right simulates deleting prefix characters; moving `j` left simulates deleting suffix characters. The source never constructs new strings, which avoids repeated copying.

An operation is possible only when at least two characters remain and the boundary characters agree. That rule becomes the outer condition:

`while i < j and s[i] == s[j]`.

If the characters differ, no legal prefix and suffix can share a character, because every non-empty prefix begins with `s[i]` and every non-empty suffix ends with `s[j]`.

**Delete maximal equal runs at both ends**

Suppose the current boundary character is `c`. A legal operation can remove any non-empty prefix made only of `c` and any non-empty suffix made only of `c`. For minimizing length, there is no benefit in deliberately retaining a boundary `c` from either maximal run. Removing more characters of the already-matched boundary symbol cannot prevent a future operation that would otherwise be possible; any retained `c` would still sit at the same end and would need removal before a different boundary character could be exposed.

The first inner loop advances `i` while the next character is the same:

`while i + 1 < j and s[i] == s[i + 1]`.

The condition `i + 1 < j` leaves the right boundary separate while the maximal left run is identified. It prevents the prefix scan from crossing the suffix position.

The second inner loop moves `j` left while the preceding character matches:

`while i < j - 1 and s[j - 1] == s[j]`.

It similarly collects the maximal right run without crossing the current left boundary.

After those loops, `i` points at the last character of the deletable left run and `j` points at the first character of the deletable right run. The parallel update `i, j = i + 1, j - 1` removes those final boundary characters as well. Thus the whole matching run on each side disappears in one outer iteration.

**Why the loops compare adjacent characters instead of storing c**

The source does not assign a separate variable for the matched symbol. During the left scan, `s[i] == s[i + 1]` keeps advancing through a chain of equal adjacent characters. Equality is transitive, so every traversed character equals the original boundary symbol.

The same reasoning applies on the right. The outer condition already established that the original left and right symbols match, so the two removed runs use the same character as required by the operation.

**Handle a remaining string made entirely of one character**

If every remaining character equals the common boundary symbol, the left scan may advance almost all the way to `j`. The guarded conditions keep the pointers from invalidly crossing during the inner loops, and the final update can then make `i > j`.

For `"aaaa"`, the left scan advances through the first three characters while `j` stays on the last. The final update removes the left prefix and right suffix, leaving crossed pointers. This models deleting all four characters with non-intersecting groups.

For `"aaa"`, an analogous operation can take two characters as one end and one as the other. Prefix and suffix lengths do not need to match, so an empty result is valid.

**Trace the third example**

For `"aabccabba"`, both ends are `a`. The left scan consumes the leading run `"aa"` and the right side consumes its trailing `"a"`, exposing the interval `"bccabb"`.

The new endpoints are both `b`. The left run has one `b` and the right run has two, so all three boundary `b` characters are removed. The remaining interval is `"cca"`.

Its endpoints differ, so the outer loop stops. Three indices remain, which is the minimum length shown in the example.

**Why greedy maximal deletion is optimal**

Whenever the endpoints differ, no operation exists, so stopping is forced. Whenever they match on character `c`, any valid next operation can delete only some positive number of leading `c` characters and some positive number of trailing `c` characters.

Deleting the maximal runs immediately reaches at least as far inward as any smaller legal choice. A smaller choice would leave `c` at one or both boundaries. Before exposing a different symbol, those leftovers would also have to be deleted using `c` at both ends. Combining those repeated deletions is equivalent to the maximal removal, provided characters remain; when all remaining characters are `c`, maximal removal already achieves the smallest possible length zero.

Therefore the greedy step never sacrifices a better future. Repeating it until endpoints differ or the interval vanishes yields the minimum attainable length.

**Compute the remaining length safely**

For a non-empty inclusive interval from `i` through `j`, length is `j - i + 1`. If all characters are deleted, the pointers cross and that expression can be zero or negative depending on how they moved.

The return statement `max(0, j - i + 1)` converts every crossed-pointer state to length zero while preserving the ordinary inclusive length for a non-empty interval.

## Complexity detail

Let $n$ be the string length. Pointer `i` only moves right and pointer `j` only moves left. Every inner-loop iteration permanently removes a character from future consideration, and the outer update removes boundary characters. Although loops are nested syntactically, no character is processed more than a constant number of times. Total time is $O(n)$.

The algorithm stores only two integer indices and uses the original immutable string for comparisons. Its auxiliary space is $O(1)$, matching the manifest. It does not allocate slices, mutable character arrays, or recursive frames.

Early termination can make runtime much smaller when the original endpoints differ, but the all-removable and deeply layered cases still require linear work.

## Alternatives and edge cases

- **Repeated string slicing:** Delete prefixes and suffixes by constructing a new string each time. It is intuitive but can copy $O(n)$ characters repeatedly and degrade toward $O(n^2)$ time.
- **Recursive two-pointer helper:** It follows the same greedy logic but may use $O(n)$ call-stack space and can exceed Python's recursion limit.
- **Run-length encoding:** Compress consecutive characters, then remove matching end runs. It works but allocates $O(n)$ storage that direct pointers avoid.
- **Different initial endpoints:** No operation is possible, so the original length is returned.
- **One-character string:** `i < j` is false, and length one remains because prefix and suffix may not intersect.
- **Two equal characters:** Both are removed by one iteration, producing zero.
- **Two different characters:** Neither can be removed, producing two.
- **All one character:** Unequal prefix and suffix lengths may cover the entire interval, so the answer is zero.
- **Matching runs of different lengths:** The rules require equal characters, not equal lengths; both maximal runs can be deleted.
- **Nested matching layers:** Each outer iteration exposes the next pair of boundary runs and handles it independently.
- **Pointer crossing:** `max(0, ...)` prevents a negative reported length.
- **Non-intersection:** Inner-loop guards keep identified prefix and suffix regions separate until the final legal removal.
- **No input mutation:** Index movement represents deletion without changing `s`.
- **Alphabet size three:** The logic relies only on equality and would work for any character alphabet.
