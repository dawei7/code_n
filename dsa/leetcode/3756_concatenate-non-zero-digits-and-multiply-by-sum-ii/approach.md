## General

**Build three prefix summaries**

For every source prefix ending before index `i`:

- `sum_d[i]` is the sum of its decimal digits. Zeros contribute nothing, so this is also the sum of retained nonzero digits.
- `cnt_n0[i]` is the number of nonzero digits.
- `p[i]` is the integer formed by concatenating its nonzero digits, stored modulo `MOD`.

When digit `d` is nonzero, concatenation updates as `p*10+d` and the count rises. When `d` is zero, `p` and the count remain unchanged. The digit sum always adds `d`.

These invariants are built in one left-to-right pass.

Inductively, suppose `p[i]` is the filtered value of `s[:i]` modulo `MOD`. A zero leaves that sequence unchanged. A nonzero digit appends one decimal symbol, whose numeric recurrence is old value times ten plus the digit. Thus every prefix entry has the claimed meaning.

**Remove the filtered prefix before a query**

For inclusive query `[l,r]`, let:

$$
n_0=\texttt{cnt\_n0}[r+1]-\texttt{cnt\_n0}[l]
$$

be the number of retained query digits, and

$$
sd=\texttt{sum\_d}[r+1]-\texttt{sum\_d}[l]
$$

be their sum.

Let `A` be the filtered nonzero-digit sequence before `l` and `B` the filtered sequence inside the query. The filtered prefix through `r` is their concatenation:

$$
A\Vert B=A\cdot10^{|B|}+B.
$$

Therefore

$$
B=p[r+1]-p[l]\cdot10^{n_0}\pmod{MOD}.
$$

The global `pow10` table supplies `10^{n_0} mod MOD` in constant time.

The code stores this residue as `x` and appends `x*sd mod MOD`.

For example, suppose the filtered prefix before `l` is 12 and the query's filtered digits form 34. Then the filtered prefix through `r` is `12*10²+34=1234`. Subtracting `12*10²` isolates 34. Zeros in the original substring never enter the exponent because `n0` counts only retained digits.

**Why zeros need no special query correction**

Zeros neither extend the filtered decimal value nor add to the digit sum or nonzero count. Prefix subtraction automatically ignores them wherever they appear.

If a query contains only zeros, `n0=0`, the two filtered prefix values are equal, `sd=0`, and the product is zero.

For `"10203004"` over the full range, the filtered prefix value is 1234 and digit sum ten. For substring `"020"`, removing the preceding filtered prefix with one decimal shift isolates two, and its digit sum is two.

Digit sums are stored without taking the modulus, but their maximum is only nine times the string length. Multiplying by the modular value and reducing at the end is equivalent to reducing the sum earlier.

**Modular subtraction may be negative temporarily**

Python computes

`x = p[r+1] - p[l] * pow10[n0] % mod`.

Because only the product term is explicitly reduced first, `x` may be negative. The final `x*sd % mod` still yields the correct nonnegative residue: modular multiplication and Python's final modulo normalize any congruent representative.

**Why every query is constant work**

All information depending on substring length or contents is encoded in prefix differences and one power lookup. The source never scans query characters, so overlapping queries reuse preprocessing completely.

Every query uses the original prefix arrays; no removal is applied to `s` itself. This preserves indices for subsequent queries exactly as the contract requires.

## Complexity detail

Let `m=len(s)` and `q=len(queries)`. Per method call, building three prefix arrays takes $O(m)$ time, and each query takes $O(1)$, for $O(m+q)$ time.

Local prefix storage is $O(m)$ and the output is $O(q)$.

At module import, the exact source also builds `pow10` through fixed maximum `100000` in $O(MAX)$ time and space. Thus total loaded implementation storage is $O(MAX+m)$, while the manifest's $O(m)$ describes per-call package-local working space after shared precomputation. This distinction matters when accounting for the exact Python module rather than amortized calls.

## Alternatives and edge cases

- **Scan each query substring:** This can require $O(mq)$ total work. Prefix summaries make queries constant time.
- **Use ordinary source length in the power:** Removed zeros do not occupy digits in `B`; the exponent must be the nonzero count.
- **Prefix only digit sums:** The concatenated value requires its own modular prefix recurrence.
- **Construct enormous integers exactly:** Query values can have $10^5$ digits. Modular prefixes avoid materializing them.
- **All-zero query:** Both filtered value and sum are zero.
- **Single nonzero digit:** The result is its square.
- **Leading or trailing zeros in a query:** They disappear and do not change the exponent.
- **Negative intermediate `x`:** The final modulo normalizes it correctly.
- **Full-string query:** `p[0]=0`, so the prefix-removal formula returns the complete filtered value.
- **Module-level table cost:** It is one-time shared work, not recreated for every method call.
- **Independent queries:** Prefix arrays remain immutable; one query never changes indices for another.
- **Repeated nonzero digits:** Concatenation is positional, so duplicates are appended separately and `cnt_n0` counts both.
- **Digit-sum prefix:** Ordinary subtraction works because digit sums are additive, unlike concatenated values which require the power adjustment.
