## General

**Split the string into maximal equal-character runs**

A homogenous substring cannot cross a position where the character changes. Therefore every valid substring lies entirely inside one maximal consecutive run of a single character.

The exact solution scans these runs with two indices. `i` is the first index of the current run. `j` starts at `i` and advances while `j < n` and `s[j] == s[i]`. When that inner loop ends, the half-open interval `[i, j)` is the complete maximal run beginning at `i`.

The run length is `cnt = j - i`. After counting its substrings, assigning `i = j` moves directly to the first unprocessed character, which begins the next run.

**Count substrings inside one run**

For a run of length $c$, any choice of a start and an end within the run creates a homogenous substring because every character is equal.

Count by substring length:

- There are $c$ substrings of length one.
- There are $c-1$ substrings of length two.
- This continues down to one substring of length $c$.

The total is:

$$
c+(c-1)+\cdots+1
=
\frac{c(c+1)}{2}.
$$

The source computes exactly this triangular number as:

`(1 + cnt) * cnt // 2`.

The product is always even because one of two consecutive integers `cnt` and `cnt + 1` is even, so integer division loses no fractional part.

**Why runs can be counted independently**

Every homogenous substring belongs to exactly one maximal run. It cannot include characters from two different runs because crossing their boundary would include at least two distinct characters.

Within a run, every contiguous substring is homogenous. Therefore summing the triangular count of each run includes every valid substring once and includes no invalid substring.

Even when two separate runs contain the same letter, they remain independent. For example, the two `a` runs in `"abbcccaa"` are separated by other characters, so no contiguous all-`a` substring can combine them.

**Trace the sample string**

`"abbcccaa"` decomposes into runs:

- `"a"` of length one, contributing one.
- `"bb"` of length two, contributing three.
- `"ccc"` of length three, contributing six.
- `"aa"` of length two, contributing three.

The sum is $1+3+6+3=13$. This matches the example's grouping by substring contents while also counting different positions as distinct occurrences.

For `"zzzzz"`, there is one run of length five. Its triangular count is `6 * 5 // 2 = 15`.

**Understand positional occurrences**

Substrings are identified by their start and end positions, not only by their text. In a run `"bbb"`, the one-character substring `"b"` occurs at three different positions, so all three count. The two-character text `"bb"` occurs at two positions, and `"bbb"` occurs once.

The triangular formula counts these positional choices automatically.

**Apply the modulus safely**

After adding one run's contribution, the solution executes:

`ans %= mod`

where `mod = 10**9 + 7`. Modular addition satisfies:

$$
(a+b)\bmod M
=
\bigl((a\bmod M)+(b\bmod M)\bigr)\bmod M.
$$

Therefore reducing after every run produces the same final remainder as computing the complete potentially large count and reducing once.

Python integers do not overflow, but periodic reduction keeps `ans` bounded. The triangular contribution is computed before the reduction and is also safe in Python.

**Pointer invariant and termination**

At the start of each outer iteration, every index before `i` has been assigned to exactly one processed maximal run, and index `i` begins the next unprocessed run.

The inner loop advances `j` through every character equal to `s[i]` and stops at the string end or the first different character. Thus `[i, j)` is maximal. Setting `i = j` preserves the invariant.

Because each run contains at least one character, `j > i` and `i` strictly increases. Eventually `i == n`, so the scan terminates after covering the full string.

**Why the final answer is correct**

The scan partitions the string into disjoint maximal runs. For each length `cnt`, the formula counts all and only contiguous choices inside that run. No homogenous substring crosses a run boundary, so none are omitted by independent counting.

Adding the contributions and taking the required modulus therefore returns exactly the number of homogenous substrings modulo $10^9+7$.

## Complexity detail

Let $n$ be the string length. Although an inner loop appears inside an outer loop, `j` advances across each character only as part of its one run, and `i` jumps to `j` afterward. Across the whole method, every character is examined a constant number of times. Time complexity is $O(n)$.

The solution stores only `mod`, `i`, `j`, `n`, `cnt`, and `ans`. No run list or substring is created, so auxiliary space is $O(1)$, matching the manifest.

The number of runs ranges from one to $n$, but run information is processed and discarded one at a time.

## Alternatives and edge cases

- **Ending-streak counting:** Maintain the current equal-character streak and add its length at every position. It is also $O(n)$ time and $O(1)$ space.
- **Run-length array:** First store all run lengths, then sum their triangular values. It is correct but uses up to $O(n)$ extra space.
- **Enumerate substrings:** Checking all $O(n^2)$ intervals is far too slow for $n=100000$.
- **Count only distinct texts:** This is incorrect because identical substring text at different positions counts multiple times.
- **Single character:** One run of length one contributes one.
- **All characters equal:** One triangular number gives $n(n+1)/2$.
- **All adjacent characters different:** Every run has length one, so the answer is $n$.
- **Repeated letter in separated runs:** Runs cannot be merged across different intervening characters.
- **Maximum run ending at n:** The condition `j < n` prevents out-of-range access and still records the final run.
- **Half-open interval:** `j - i` is the exact run length because `j` is the first excluded index.
- **Integer division:** The product of consecutive integers is even, so `// 2` is exact.
- **Modulo placement:** Reducing after each run preserves the final modular sum.
- **No substring allocation:** Counting by lengths avoids slicing, copying, or comparing candidate strings.
- **Lowercase alphabet:** Only equality matters; the method would work for any character set.
- **Empty string:** The official constraint excludes it, so no special return branch is required.
