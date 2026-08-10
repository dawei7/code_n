## General

**What self-contained really requires.** A substring `s[i:j + 1]` is self-contained when every occurrence in the complete string of every character appearing inside the substring also lies between `i` and `j`. It must also be a proper substring, so its length must be smaller than `len(s)`.

This can be expressed with global first and last occurrences. If a character `c` appears inside a candidate, then:

$$
\texttt{first[c]}\ge i
\quad\text{and}\quad
\texttt{last[c]}\le j.
$$

The exact source builds both maps in one pass. `first[c]` is written only the first time `c` appears, while `last[c]` is overwritten at every occurrence and ends at the final position.

**A valid candidate can start only at a global first occurrence.** Consider the first character of a self-contained substring, `s[i]`. If the same character appeared before `i`, then it would occur both inside and outside the substring, violating the definition. Therefore, `i` must equal the global first occurrence of `s[i]`.

The outer loop uses `for c, i in first.items()`, so it tries exactly these necessary starting positions. There are at most 26 because the input contains lowercase English letters.

This reduction is powerful: the method does not need to try all $n$ possible starts independently. Starts that are not first occurrences can never succeed.

**Track how far the candidate is forced to extend.** For a chosen start character `c`, `mx` begins as `last[c]`. Any self-contained substring starting at `i` and containing `c` must reach at least that far, or another occurrence of `c` would remain outside on the right.

The inner scan moves `j` right from `i`. For each encountered character `s[j]`, it reads that character's global first and last positions as `a` and `b`.

If `a < i`, the character already appeared before the candidate start. Since the current substring now contains it, that earlier occurrence is permanently outside. Extending farther right can never include an index before `i`, so no candidate with this start can be self-contained. The source correctly breaks the scan.

Otherwise, all occurrences on the left are safe, but the candidate must include the character's final occurrence. The update `mx = max(mx, b)` records the farthest right endpoint forced by every character encountered so far.

**Closure occurs when the scan catches the requirement.** When `j == mx`, every character seen from `i` through `j` has:

- no occurrence before `i`, because the scan would have broken;
- no occurrence after `j`, because its last occurrence is at most `mx=j`.

Thus `s[i:j + 1]` is self-contained. The source checks `j - i + 1 < n` before recording it, enforcing the rule `t != s`.

The scan does not stop after finding one closed substring. Continuing can encounter a new character whose first occurrence is still at or after `i` and whose last occurrence forces a later endpoint. That may produce a longer self-contained substring with the same start. Since the task asks for the longest, every later closure is worth considering.

**Trace for `"abacd"`.** First occurrences are `a:0`, `b:1`, `c:3`, and `d:4`. Start at `i=0` for `a`. Its last occurrence is 2, so `mx=2`. Scanning index 1 encounters `b` with last 1; `mx` stays 2. At index 2, `j==mx`, so `"aba"` is closed.

Continuing to index 3 encounters `c`, whose last is 3. Now `j==mx` again and `"abac"` is self-contained with length four. At index 4, the interval would become the entire string, so the length check refuses it. The answer remains four.

For `"abab"`, start zero eventually closes only at index three, which is the whole string and is forbidden. Starting at `b`'s first occurrence index one encounters `a`, whose first occurrence is before the start, so that scan breaks. No proper self-contained substring exists and -1 remains.

**Why all valid substrings are considered.** Take any valid proper substring. Its start is the first global occurrence of its first character, so the outer loop selects that start. During its inner scan, no contained character has a first occurrence before the start, so the loop does not break before the substring's end. Every contained character's last occurrence is within the substring, so at its endpoint the maintained `mx` is at most that endpoint. Because the endpoint itself has been scanned and `mx` never trails below necessary last occurrences, closure is recognized. Its length is therefore offered to `ans`.

Every recorded closure also satisfies both first- and last-occurrence conditions and the proper-substring check. The maximum recorded length is exactly the answer.

## Complexity detail

The first/last map construction takes $O(n)$ time. The outer loop has at most 26 iterations, and each inner loop scans at most $n$ positions. Total time is $O(26n)=O(n)$ under the fixed lowercase alphabet.

This is linear asymptotically but may inspect the same string position for several candidate starting characters. If the alphabet were unbounded with $A$ distinct characters, the more general bound would be $O(An)$.

The two dictionaries hold at most 26 entries, so auxiliary space is $O(26)=O(1)$ relative to input length. The local manifest's $O(n)$ time and $O(1)$ space accurately describe this fixed-alphabet implementation.

## Alternatives and edge cases

- **Partition-label intervals:** Build closed intervals from first and last occurrences and merge dependencies. It can express the same closure idea but needs care to consider the longest proper union.
- **Try every substring:** Checking outside occurrences for all $O(n^2)$ candidates is far slower.
- **Prefix frequency counts:** They can test one candidate quickly but still leave too many candidate boundaries without the first-occurrence reduction.
- **Whole string only:** It is explicitly forbidden, so the length check must reject it even though it is always occurrence-closed.
- **No proper candidate:** `ans` stays -1.
- **One unique character at an interior position:** Its one-character substring is self-contained and can be recorded.
- **Character seen before the start:** `a < i` makes the entire start impossible, so breaking is stronger and safer than merely skipping one endpoint.
- **Character whose last occurrence is later:** `mx` extends the required boundary to include it.
- **Nested dependencies:** Newly included characters can extend `mx` repeatedly; scanning until closure resolves the chain.
- **Multiple closures for one start:** The scan continues because a later closure can be longer.
- **Repeated start character:** Initial `mx = last[c]` guarantees every copy is included.
- **Lowercase alphabet:** The constant 26 is what turns the outer-times-inner work into $O(n)$.
- **Dictionary iteration order:** It follows first insertion order in Python, but answer correctness does not depend on candidate order.
- **Length at least two for input:** The full-string exclusion can therefore still leave meaningful proper candidates.
- **No input mutation:** The source only records positions and scans `s`.
