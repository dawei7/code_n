## General

Two values are almost equal when zero swaps suffice or one swap of two digit positions in either number makes them equal. The solution processes values in sorted order, generates every number reachable from the current value by at most one swap, and counts how many earlier original values match those results.

Sorting is more than a performance convenience. A swap can move zero to the front, and converting the resulting digit string back to an integer removes that leading zero. For example, swapping `"30"` produces `"03"`, interpreted as three. Processing the larger value thirty after three lets the generated result find the earlier shorter integer.

For current integer `x`, set `vis` begins with `x` itself, representing the allowed zero-operation case. `s = list(str(x))` exposes its decimal digits.

The nested loops choose every pair of positions `i < j`. They swap those two characters, convert the complete sequence with `int("".join(s))`, and add the result to `vis`. The swap is immediately undone before trying the next pair.

A set is essential. Swapping equal digits may leave the number unchanged, and different position pairs can produce the same integer, especially after leading zeros disappear. Each earlier array occurrence must contribute at most once for the current index, so duplicate transformation results must be removed.

`cnt` maps each original value already processed to its frequency. The expression `sum(cnt[y] for y in vis)`, with the comprehension's local variable, counts every earlier index whose value equals one reachable result. Then `cnt[x] += 1` makes the current original value available to later indices.

The original source writes the generator variable as `x` too. In Python 3, comprehension variables have their own scope, so this does not replace the outer current `x` before `cnt[x] += 1`.

**Why generating swaps only from the current number is enough.** Let earlier value be $a$ and current sorted value be $b$, so $a\le b$. If swapping $b$ makes $a$, the algorithm finds it directly. If swapping $a$ makes $b$, the same transposition applied to $b$ reverses the swap and makes $a$, provided their displayed lengths match. A swap on the shorter $a$ cannot create additional digits, so a larger resulting $b$ has the same length. The only length-changing representation case comes from a leading zero after swapping the larger number, which is exactly why sorting places that larger source second.

For `[3,12,30,17,21]`, sorting places three before thirty. Current thirty generates three via leading zero and finds one earlier count. Current twenty-one can generate twelve and finds the other pair.

For five copies of one, `vis` contains one for every occurrence. Before processing the $j$-th copy, `cnt[1]` equals the number of earlier copies, so contributions sum to $0+1+2+3+4=10$.

The array is sorted in place, so its original order is not preserved. Pair counting is unaffected because the property depends on values and every unordered pair of indices is counted once in some processing order.

## Complexity detail

Let $n$ be the number of values and $d$ the maximum number of decimal digits. Sorting takes $O(n\log n)$. Each value has $O(d^2)$ digit pairs. Creating a joined string and converting it to an integer takes $O(d)$ time, giving $O(nd^3)$ transformation time in the direct string implementation.

Summing over at most $O(d^2)$ distinct results per value adds $O(nd^2)$ expected dictionary work. Total expected time is $O(n\log n+nd^3)$.

The frequency map stores up to $n$ distinct originals. `vis` stores at most $O(d^2)$ results and the digit list uses $O(d)$ space. Including the in-place sort's Python implementation workspace can add up to $O(n)$ references. The stated auxiliary bound $O(n+d^2)$ is appropriate.

## Alternatives and edge cases

- **Compare every pair directly:** Generate swaps or compare digit mismatch positions for all $O(n^2)$ pairs. This fits $n=100$ but repeats transformation work.
- **Canonical signatures:** Grouping by sorted digits is insufficient because arbitrary permutations may require more than one swap. The exact operation distance must be respected.
- **Generate from both numbers:** This duplicates work. Sorted processing plus inverse-swap reasoning makes one-sided generation sufficient.
- **Do not sort:** Leading-zero transformations can make a longer number equal a shorter one only in one direction. Without sorting, generating only from the current number could miss such a pair.
- **Equal numbers:** Zero operations are allowed, and initializing `vis` with `x` counts them.
- **Repeated digits:** Swapping identical digits produces the same value; `vis` prevents double counting.
- **Leading zero result:** `int` removes it, allowing pairs such as three and thirty.
- **Different digit multisets:** No swap can change digits, so no generated result matches.
- **Three-cycle permutation:** Values like 123 and 231 require more than one transposition and are correctly not generated from each other.
- **Input mutation:** `nums.sort()` changes caller-visible order. A preservation requirement would require sorting a copy and add explicit $O(n)$ storage.
- **Positive integers:** There is no minus sign in the digit list. Supporting negatives would require separate sign handling.
