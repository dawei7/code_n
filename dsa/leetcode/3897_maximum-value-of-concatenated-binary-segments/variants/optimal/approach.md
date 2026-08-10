## General

Segment $i$ has the fixed binary form

$$
1^{x_i}0^{y_i},
$$

where $x_i=\texttt{nums1}[i]$ and $y_i=\texttt{nums0}[i]$. Bits inside a segment cannot be rearranged; only whole segments may change order.

Every possible concatenation has the same total length $L$. Among equal-length binary strings, the numerically larger value is exactly the lexicographically larger string: at the first differing position, a `1` contributes a larger highest remaining power of two than a `0` can recover from all lower positions. The ordering problem can therefore be solved by deciding which segment should appear first at the earliest possible disagreement.

The source derives a simple sort key for the restricted shape “some ones followed by some zeros,” sorts all segments, and only then evaluates the chosen binary string modulo $10^9+7$.

**The pairwise ordering principle**

For two segment strings $A$ and $B$, placing $A$ first is at least as good as placing $B$ first precisely when

$$
A+B\ge_{\mathrm{lex}}B+A.
$$

If a proposed global order contains adjacent segments in the worse orientation, swapping those two improves the concatenation while leaving every other bit in place. Therefore an order consistent with the pairwise dominance rule is globally maximal.

For arbitrary strings, implementations often sort using a custom comparator for $A+B$ versus $B+A$. Here, the segments' special structure lets the source replace that comparator with a tuple key.

**Pure-one segments must come first**

When $y=0$, the segment is made entirely of ones. The constraints ensure $x>0$ because a segment cannot be empty.

Take a pure-one segment $A=1^a$ and any segment $B$ that contains a zero. In $A+B$, all $a$ leading ones appear before that zero-containing segment. In $B+A$, the first zero belonging to $B$ arrives before the added pure ones from $A$. At that first difference, $A+B$ has `1` while $B+A` has `0`, so $A$ must precede $B$.

All pure-one segments concatenate to one uninterrupted run of ones. Their internal order does not change the final string. The source assigns them key category 0 and uses `-x` as a deterministic secondary key, placing longer ones first even though ties among this category are value-equivalent.

**Mixed segments come next**

A mixed segment has $x>0$ and $y>0$, so it begins with ones and ends with zeros. Compare

$$
A=1^x0^y
\quad\text{and}\quad
B=1^u0^v.
$$

If $x>u$, then in $A+B$ the first run of ones continues after the point where $B+A$ has already reached $B$'s first zero. Therefore $A+B$ is larger, and the segment with more leading ones must come first.

If $x=u$, both concatenations share the same initial run of ones and then enter a zero run. Now the segment with fewer zeros should come first. If $y<v$, then $A+B$ reaches the leading ones of $B$ while $B+A$ is still inside its longer zero run. The next differing bit is `1` in $A+B$ and `0` in $B+A`.

Thus mixed segments are ordered by:

1. decreasing $x$; and
2. for equal $x$, increasing $y$.

The source represents that with key category 1 followed by `-x` and `y`.

**Pure-zero segments must come last**

When $x=0$, the segment is $0^y$. Compare it with any segment that has at least one leading one. Putting the one-starting segment first makes the concatenation begin with `1`, whereas putting the pure-zero segment first makes it begin with `0`. The one-starting segment is unconditionally better.

All pure-zero segments therefore follow pure-one and mixed segments. Their relative order is irrelevant because they merge into one trailing run of zeros. The source assigns category 2 and uses `y` only as a deterministic tie order.

The complete key is consequently:

- category 0 for $y=0$;
- category 1 for $x>0$ and $y>0$; and
- category 2 for $x=0$.

Within the only category where order affects the answer, the key is exactly $(-x,y)$.

**Why sorting by this key is globally optimal**

The three category rules satisfy every cross-category pairwise comparison: pure ones dominate mixed segments, every segment containing a one dominates pure zeros, and pure ones also dominate pure zeros.

Within mixed segments, decreasing leading-one count and then increasing zero count is exactly the result of comparing both possible concatenations. Therefore whenever two adjacent segments are out of key order, swapping them cannot decrease the binary string and strictly increases it when their order matters.

Repeatedly removing inversions leads to the source's sorted order. Since no improving adjacent swap remains, and each pair is in its dominant orientation, the concatenation is lexicographically and numerically maximal.

**Evaluating without constructing the enormous binary string**

Let $L$ be the total number of bits. The source stores powers

$$
p[q]=2^q\bmod(10^9+7)
$$

for $q=0,1,\ldots,L-1$.

It sets `b = L - 1`, the exponent belonging to the first bit of an $L$-bit binary string. For each sorted segment:

- every one bit contributes `p[b]` to `ans`, after which `b` decreases;
- zero bits contribute nothing, so the source skips them together by subtracting `cnt0` from `b`.

For example, a final string `"1110"` has one bits at exponents 3, 2, and 1. The source adds

$$
2^3+2^2+2^1=14
$$

and skips the last zero at exponent 0.

Modulo reduction is applied to powers and to the accumulating sum. This is valid because modular addition and multiplication preserve the residue of the already chosen maximum integer. Importantly, the modulus is not used to choose the order: maximizing residues would be unrelated to maximizing the original integer.

The loop decrements its local `cnt1` values while emitting ones. Those integers came from tuple unpacking, so the stored `pairs` tuples and the input arrays are not modified.

## Complexity detail

Let $N$ be the number of segments and

$$
L=\sum_{i=0}^{N-1}
\left(\texttt{nums1}[i]+\texttt{nums0}[i]\right)
$$

be the total bit count.

Creating `pairs` and computing $L$ cost $O(N)$ time. Sorting the segment tuples costs $O(N\log N)$ time.

Building the power array performs $L-1$ modular multiplications, costing $O(L)$ time. The evaluation loop iterates once per one bit and performs one constant-time skip per segment's zero run. Its cost is $O(L+N)$, customarily simplified to $O(L)$ because every nonempty segment contributes at least one bit and hence $N\le L$.

The total running time is

$$
O(N\log N+L).
$$

The `pairs` list uses $O(N)$ space, and the power array `p` uses $O(L)$ space. Python sorting may also require $O(N)$ temporary storage. The exact auxiliary-space bound is therefore

$$
O(N+L),
$$

which simplifies to $O(L)$ under $N\le L$.

This is more precise than the Optimal manifest's $O(N)$ space claim. The checked-in implementation explicitly allocates one modular power for every bit position, and $L$ is not generally $O(N)$ when a segment may contain up to $2\cdot10^4$ bits. A different evaluator using fast exponentiation per run could avoid the $O(L)$ power table, but that is not the source being documented.

The array `p` is always nonempty because every segment has positive length and $N\ge1$. Thus `b = L - 1` is a valid initial exponent.

## Alternatives and edge cases

- **Generic concatenation comparator:** Sorting by whether `A+B > B+A` works for arbitrary binary strings, but the source's tuple key is simpler and faster to compare because every segment has form $1^x0^y$.
- **Run-based modular evaluation:** Append a run of $c$ bits using powers of two and a geometric-sum formula, potentially avoiding one iteration and one stored power per bit; it requires careful modular exponentiation.
- **Construct the full string:** Joining all sorted segments and parsing it is conceptually simple, but materializes $L$ characters and may exceed practical integer-conversion limits.
- **Pure-one segment:** It belongs before every segment containing a zero. Its order relative to other pure-one segments does not affect the final string.
- **Pure-zero segment:** It belongs after every segment containing a one. All pure-zero segments merge into equivalent trailing zeros.
- **Equal leading-one counts among mixed segments:** The segment with fewer following zeros goes first because it exposes the next segment's one bits sooner.
- **Identical segments:** Either order produces the same concatenation, and Python's stable sort preserves their input order without affecting the value.
- **One segment:** Sorting changes nothing; the evaluator simply computes that segment's binary value modulo the constant.
- **Very long zero runs:** They add no numerical term, so the source advances the exponent in one subtraction rather than looping over every zero.
- **Very long one runs:** The source does loop once per one, which is covered by the $O(L)$ total-length bound.
- **Modulo and maximization:** Segment order must maximize the full equal-length binary string first. Comparing values after reduction modulo $10^9+7$ could select the wrong order.
- **Space-manifest mismatch:** The actual power table contains $L$ entries, so this implementation uses $O(N+L)$ auxiliary space rather than only $O(N)$.
