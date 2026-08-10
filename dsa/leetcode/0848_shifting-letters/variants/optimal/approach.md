## General

**Determine which operations affect one position**

Operation `i` shifts the prefix ending at `i`. Therefore, character position `p` is affected by every operation whose index is at least `p`:

$$
\text{total shift at }p
=\sum_{i=p}^{n-1}\texttt{shifts}[i].
$$

These are suffix sums of the `shifts` array. Computing each sum independently would be quadratic. Scanning positions from right to left lets one running total represent the needed suffix.

**Maintain the suffix total**

Variable `t` begins at zero. At index `i` moving from `n-1` down to zero, the statement:

`t += shifts[i]`

makes `t` equal to `shifts[i] + shifts[i+1] + ... + shifts[n-1]`.

That is exactly the total number of single-letter shifts applied to `s[i]`.

The rightmost character is affected only by the final whole-string operation. One position to the left is affected by the last two operations, and so on. Reverse traversal matches this nesting.

**Convert a letter to a zero-based alphabet index**

`ord(s[i]) - ord("a")` maps:

- `a` to 0;
- `b` to 1;
- ...
- `z` to 25.

Adding `t` applies all shifts numerically.

**Wrap around with modulo 26**

The alphabet repeats after 26 shifts. The expression:

`(original_index + t) % 26`

returns the final index from 0 through 25 regardless of how large `t` becomes.

`ascii_lowercase[j]` maps that index back to its letter.

For `z` with one shift, the numeric value is `25+1=26`; modulo 26 gives zero, which maps to `a`.

**Why converting the string to a list matters**

Python strings are immutable, so individual positions cannot be assigned. `s = list(s)` creates a mutable character list.

Each reverse iteration replaces one entry with its final letter. `"".join(s)` builds the returned string after all positions are complete.

The local variable name `s` is rebound to the list, but the original input string object remains unchanged.

**Trace `"abc"` with `[3,5,9]`**

Start from the right:

- At index 2, `t=9`. Letter `c` has index 2, so `(2+9)%26=11`, letter `l`.
- At index 1, `t=9+5=14`. Letter `b` has index 1, so final index 15, letter `p`.
- At index 0, `t=14+3=17`. Letter `a` has index 0, so final index 17, letter `r`.

Joining yields `"rpl"`, the same result as applying the prefix shifts one operation at a time.

**Why additions can be reordered**

Shifting a letter by `a` and then by `b` is equivalent to shifting by `a+b`. Modulo 26 addition is associative and commutative, so the order of contributing operations does not change the final character.

The algorithm may accumulate the total first and apply it once rather than materializing every intermediate string.

**Why every operation is accounted for exactly once**

At position `i`, running total `t` includes all operation indices from `i` onward, precisely those prefixes long enough to contain position `i`. It excludes earlier operation indices, whose prefixes end before `i`.

Thus, no relevant shift is missing and no irrelevant shift is added. Converting through modulo 26 gives the exact final character at every index.

The reverse-loop invariant can be stated precisely: immediately after adding `shifts[i]`, `t` equals the total of all operations whose prefixes contain index `i`. After writing the final character, moving to `i-1` requires adding exactly one newly relevant operation, namely operation `i-1`; every operation already in `t` also affects the longer prefix position `i-1`. This inductive relationship is why one scalar replaces an entire suffix-sum table.

## Complexity detail

Let `n = len(s)`. Converting the string to a list, scanning all positions once, and joining the result each take `O(n)` time. Total time is `O(n)`.

The mutable character list and returned string use `O(n)` space. The running total and index variables use `O(1)` additional working space.

Python integers can hold the potentially large suffix sum. Applying modulo only during character conversion is correct; `t` could also be reduced modulo 26 after each addition to keep it small.

## Alternatives and edge cases

- **Apply every prefix operation directly:** It can touch `O(n^2)` total characters.

- **Build a separate suffix-sum array:** It gives `O(n)` time but uses another length-`n` numeric array. The running total needs only one scalar beyond the output list.

- **Reduce `t` modulo 26 each step:** This produces identical letters and may keep integers bounded in fixed-width languages.

- **Zero shift:** It changes nothing but is safely included in the sum.

- **Shift by a multiple of 26:** Modulo maps the letter back to itself.

- **Very large shift values:** Only their remainder modulo 26 matters for letters.

- **One-character string:** Its only operation affects its only character.

- **Rightmost position:** Only `shifts[n-1]` affects it.

- **Leftmost position:** Every shift operation affects it, so it receives the total array sum.

- **Wrap from `z` to `a`:** Modulo 26 handles it automatically.

- **Lowercase guarantee:** `ascii_lowercase` indexing and subtraction from `ord("a")` are valid for every character.

- **Input string immutability:** A new list and final string are created; `shifts` is only read.
