## General

**Classify strings by how many ones they contain**

A binary string of length $N$ can contain zero, one, two, and so on through $N$ ones. That gives $N+1$ possible one-count classes.

The input contains only $N$ strings. Even if every input string belongs to a different class, at most $N$ of the $N+1$ classes can be present. By the pigeonhole principle, at least one count $i$ from zero through $N$ is missing.

If the method constructs any length-$N$ string containing exactly $i$ ones, that string cannot equal an input string. Equal binary strings necessarily have equal numbers of ones, while no input has that chosen count.

This is the central idea of the exact source. It differs from the familiar diagonal-bit construction, although both guarantee a missing string.

**Store present counts in a bit mask**

`mask` is an integer used as a compact set. Bit $k$ is one exactly when an input string with $k$ ones has been observed.

For each string `x`, `x.count("1")` scans its characters and returns its number of ones. The expression `1 << count` creates an integer whose only set bit is at that position. Bitwise OR,

`mask |= 1 << x.count("1")`,

records the class without disturbing any class recorded earlier. Several strings with the same one count simply set the same bit again.

For example, if the input one counts are one and two, bits one and two become set. Bit zero is clear, so a string with no ones is guaranteed absent.

**Find the first missing class**

`count(0)` supplies the infinite sequence 0, 1, 2, and so forth. For each candidate `i`, the expression `mask >> i & 1` extracts bit $i$.

The source then XORs that bit with one. For a bit value of zero, `0 ^ 1` is one and the condition succeeds. For a set bit, `1 ^ 1` is zero and the search continues. In plain language, the condition asks whether class $i$ has not appeared.

Although the iterator is unbounded syntactically, the proof guarantees a missing class among 0 through $N$. The loop therefore returns after at most $N+1$ checks and never reaches an impossible one-count larger than the string length.

**Construct a representative of that class**

For the missing count `i`, the method returns

`"1" * i + "0" * (len(nums) - i)`.

The first part contributes exactly $i$ ones. The second contributes $N-i$ zeroes. Their concatenation has length $N$ and exactly $i$ ones, so it is a valid binary string in the missing class.

The positions of the ones do not matter. All that matters for the nonmembership proof is the count. Putting all ones first is simply the easiest canonical representative to build.

For `nums = ["01", "10"]`, both inputs contain one one. The mask records only class one. The first missing class is zero, and the source returns `"00"`, which is a valid answer even if an example shows a different valid output.

**Why the answer is certainly absent**

Suppose, for contradiction, that the constructed string equals some `nums[j]`. Equal strings have the same character at every position and therefore the same number of ones. The output has exactly $i$ ones, so `nums[j]` would also have $i$ ones.

But the mask search chose $i$ only because no input string had that count. This contradiction proves the constructed string is not in the array.

The argument does not need the input strings to be checked individually against the output. Once a missing count is known, an entire class of strings is certified absent.

**Relationship to the number of possible strings**

There are $2^N$ total binary strings and only $N$ forbidden strings, so a missing answer exists for many reasons. This method uses the much smaller set of $N+1$ possible Hamming weights, where "Hamming weight" means number of one bits.

The uniqueness guarantee for input strings is consistent with the problem, but this particular proof would still find a missing weight even if duplicate rows consumed some of the $N$ positions. Duplicates could only reduce the number of represented classes.

**Exact cost rather than the manifest label**

The outer loop visits $N$ strings, but `x.count("1")` reads all $N$ characters of each string. Thus the concrete input-processing work is $N\cdot N$, not linear in the number of rows alone.

The manifest's $O(N)$ time matches diagonal construction, which inspects one character per row. It does not match this Hamming-weight implementation. The exact source has $O(N^2)$ time when $N$ denotes both the number of strings and their length.

## Complexity detail

Let $N=\texttt{len(nums)}$, which is also every string's length. Counting ones in all strings takes $O(N^2)$ time. Testing at most $N+1$ mask bits and building the $N$-character result take $O(N)$ additional time. Total exact time is $O(N^2)$.

The integer mask needs $O(N)$ bits, and the returned string needs $O(N)$ space. Excluding output, this is $O(N)$ bit space, often described as $O(1)$ machine words only under the small constraint $N\le16$. The manifest's $O(N)$ space is a safe bound.

## Alternatives and edge cases

- **Cantor diagonal construction:** Flip `nums[i][i]` for every $i$. It gives $O(N)$ time and an immediate per-row difference proof.
- **Hash set plus enumeration:** Generate candidates until one is absent, but candidate construction and membership storage are unnecessary here.
- **Integer-set search:** Convert inputs to integers and test $0$ through $N$; conversion still reads $O(N^2)$ input characters.
- **Missing class zero:** Return the all-zero string.
- **Missing class $N$:** Return the all-one string; the zero suffix has length zero.
- **Several missing counts:** Returning the smallest is valid because any missing class works.
- **Many strings share a one count:** One mask bit represents them all, leaving even more classes absent.
- **Input order:** It has no effect because bitwise OR records only presence.
- **One input string:** There are two weight classes, so the loop finds the other one.
- **No direct membership test:** The missing-weight proof makes one unnecessary.
- **Infinite-looking iterator:** `count(0)` terminates through the guaranteed return by index $N$ at the latest.
- **Output format:** Repeating strings produces exactly $N$ characters containing only zero and one.
- **Input preservation:** Counting characters does not modify the strings or list.
