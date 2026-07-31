## General

Let $f$ be the largest frequency of any value and let $n$ be the array length. The maximum greatness is exactly $n-f$, so only the largest frequency must be counted.

**Why more than $n-f$ wins are impossible**

Choose a value $x$ that appears $f$ times. Split the original positions into the $L$ values below $x$, the $f$ copies of $x$, and the $G$ values above $x$. At most all $L$ positions below $x$ can win. Any winning position whose original value is at least $x$ must receive one of the $G$ permutation values strictly above $x$, so there can be at most $G$ additional wins. Thus every arrangement has at most $L+G=n-f$ wins.

**Why the bound can always be reached**

Conceptually sort the values as $a_0 \leq \dots \leq a_{n-1}$ and shift them left by $f$ positions. For every $0 \leq i < n-f$, assign $a_{i+f}$ to the position holding $a_i$. These two values must be different: equality would place at least $f+1$ copies of the same value between indices $i$ and $i+f$, contradicting the definition of $f$. Therefore all first $n-f$ comparisons are strict wins, and the remaining $f$ assignments may lose.

The construction proves attainability, but building it is unnecessary. A single frequency-table pass finds $f$ and returns $n-f$ directly.

## Complexity detail

The algorithm scans all $n$ values once and performs expected-constant-time hash-map updates, giving $O(n)$ expected time. In the worst case all values are distinct, so the frequency table uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Sorting and two pointers:** Greedily match each smallest target with the smallest unused strictly larger value in $O(n \log n)$ time; it produces the same count but does unnecessary ordering work.
- **Explicit permutation search:** Trying arrangements is factorial and infeasible even for modest input sizes.
- **All equal:** The maximum frequency is $n$, so no strict comparison can win.
- **All distinct:** The maximum frequency is one, and a cyclic shift achieves $n-1$ wins.
- **Tied maximum frequencies:** Only the common maximum count matters; choosing any value with frequency $f$ gives the same bound.
- **Strict comparison:** Equal values never contribute, which is exactly why multiplicity controls the unavoidable losses.
