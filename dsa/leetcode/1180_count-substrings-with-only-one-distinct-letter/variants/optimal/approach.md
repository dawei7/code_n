## General

A qualifying substring must be contiguous, nonempty, and contain only one distinct letter. Therefore, it cannot cross a position where the character changes. This makes each maximal run of equal characters an independent counting region.

For example, `"aaaba"` splits into the runs `"aaa"`, `"b"`, and `"a"`. Every one-letter-only substring lies completely inside one of those runs. A substring that crosses from `"a"` to `"b"` contains at least two distinct letters and is invalid. Once the maximal runs are identified, the problem becomes: how many nonempty substrings does a run of length $L$ contain?

**Counting one equal-character run**

Inside a run, every position contains the same letter, so every nonempty contiguous interval is valid. There are $L$ substrings of length one, $L-1$ substrings of length two, and so on, down to one substring of length $L$. Their total is

$$
L+(L-1)+\cdots+1=\frac{L(L+1)}{2}.
$$

Another beginner-friendly way to see the same formula is to count by starting position. From the run’s first position, a valid substring may end at any of $L$ positions. From the second position, it has $L-1$ choices. This continues until the last position has one choice. Both views count every interval once.

**How the two pointers discover maximal runs**

The code begins with `i = 0`. This variable is the first index of the next run that has not yet been counted. While `i < n`, it sets `j = i` and advances `j` while two conditions hold: `j` is still inside the string, and `s[j] == s[i]`. Because `s[i]` is the run’s character, the inner loop moves across exactly the consecutive copies of that character.

When the inner loop stops, `j` is the exclusive end of the run. Either `j == n`, meaning the run reaches the end of the string, or `s[j]` differs from `s[i]`, meaning a new run begins at `j`. The run occupies the half-open interval from `i` through `j` and has length `j - i`. Here “through `j`” means up to but not including `j`; the half-open form avoids adding or subtracting one when measuring the length.

The solution adds

`(1 + j - i) * (j - i) // 2`

to `ans`. If $L=j-i$, this is exactly $(L+1)L/2$. The division is performed after multiplication. One of two consecutive integers $L$ and $L+1$ is always even, so the product is divisible by two and integer division loses nothing.

Finally, `i = j` moves the outer pointer directly to the first character of the next run. No character from the completed run is reconsidered by a later outer iteration.

**Following the example from start to finish**

For `s = "aaaba"`, the first run starts at zero. The inner pointer advances to three, so $L=3$ and the solution adds $3 \cdot 4 / 2=6$. Those six occurrences are three length-one substrings, two length-two substrings, and one length-three substring.

The next run is the single `"b"` at index three. Its length is one, so it contributes one. The last `"a"` is another separate length-one run and contributes one. It must not be combined with the earlier `"a"` characters because the `"b"` between them prevents a contiguous substring from using both regions. The final answer is $6+1+1=8$.

For a string of ten identical letters, there is one run of length ten, so the answer is $10 \cdot 11 / 2=55$. The algorithm obtains that result without constructing any of the 55 substrings.

**Why the sum over runs is exact**

Every substring counted inside a run is valid because all of its characters equal the run’s character. Conversely, take any valid substring. Since it has one distinct letter, it cannot cross a boundary between two different adjacent characters. It must therefore lie wholly within exactly one maximal run. The run formula counts that interval once according to its start and end positions.

The maximal runs are disjoint and together cover the whole string. The outer loop processes each run once, and `ans` accumulates its exact number of valid intervals. Thus no qualifying occurrence is omitted, no invalid interval is included, and identical substring text at different positions is correctly counted as separate occurrences.

## Complexity detail

Let $n$ be the length of `s`. Although the solution contains a loop inside another loop, it is not quadratic. Within a run, `j` advances across each character once. After the run is counted, `i` jumps to that same exclusive endpoint. Across the entire execution, the inner-loop pointer performs $n$ successful character visits in total, plus a constant amount of boundary work per run.

The total time complexity is therefore $O(n)$. Computing the arithmetic formula for a run is constant-time under the usual unit-cost integer model.

The algorithm stores only `n`, the two indices, the accumulator, and temporary arithmetic values. It does not create substrings, arrays, maps, or run records. Its auxiliary-space complexity is $O(1)$.

The answer can be as large as $n(n+1)/2$. Python integers grow automatically. In a fixed-width language, the result and the multiplication should use a sufficiently wide integer type before dividing by two.

## Alternatives and edge cases

- **Ending-at-this-index dynamic programming:** Track the number of valid substrings ending at the current character. Increase that number when the character matches its predecessor; otherwise reset it to one. Adding these values also gives $O(n)$ time and $O(1)$ space.
- **Enumerate all substrings:** Generating intervals and checking their distinct letters is unnecessarily expensive, taking at least quadratic time and potentially cubic work with repeated scans.
- **Single-character string:** One maximal run of length one contributes $1 \cdot 2 / 2=1$, so the only substring is counted.
- **All characters equal:** The inner loop reaches `n` once, and the formula counts all $n(n+1)/2$ nonempty substrings.
- **Every adjacent character differs:** Every run has length one. Each contributes one, so the answer is exactly $n$.
- **Same letter in separated runs:** Runs such as the two `"a"` regions in `"aba"` must remain separate. Contiguity prevents combining them across the different middle character.
- **Exclusive run endpoint:** When the inner loop ends, `j` is not part of the completed run. The correct length is `j - i`, and setting `i = j` starts precisely at the unprocessed character.
- **Occurrence counting rather than distinct text:** Two equal substrings at different index intervals both count. The run formula naturally counts intervals, not unique string values.
