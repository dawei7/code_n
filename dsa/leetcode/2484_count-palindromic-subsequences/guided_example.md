# Guided Example: Count Palindromic Subsequences

## 1. What a length-five palindromic subsequence really is

The instance traced here is the official first example, `s = "103301"`, whose expected
answer is $2$; the string has $n = 6$ positions. A subsequence of length $5$ is a choice of
five positions

$$
i < j < k < l < m
$$

together with the digits found there. It is palindromic exactly when reading those digits
forwards and backwards gives the same sequence, which for five characters means

$$
s_i = s_m, \qquad s_j = s_l, \qquad s_k \ \text{unconstrained}.
$$

So a length-five palindromic subsequence has the shape $a\,b\,x\,b\,a$: the first and last
digits must agree, the second and fourth must agree, and the middle digit is free. The
problem counts **index tuples**, not distinct strings — two different choices of positions
that happen to spell the same characters are two subsequences. The official explanation of
this instance confirms that reading: the six length-five subsequences contain the value
`"10301"` twice, and both are counted, giving the answer $2$.

| Position in the tuple | Role in the shape $a\,b\,x\,b\,a$ | Constraint | Interacts with |
|:---:|:---|:---|:---|
| $i$ | first digit $a$ | $s_i = a$ | must equal $s_m$ |
| $j$ | second digit $b$ | $s_j = b$ | must equal $s_l$ |
| $k$ | centre digit $x$ | no constraint on its value | separates the two halves |
| $l$ | fourth digit $b$ | $s_l = b$ | must equal $s_j$ |
| $m$ | fifth digit $a$ | $s_m = a$ | must equal $s_i$ |

The centre position $k$ plays a special role: it is the only position that is not matched
with any other, and the two sides of the tuple are otherwise completely independent. That
independence is the entire mechanism of the solution.

## 2. Grouping by the centre index

Fix the centre position $k$ with $1 \le k \le n$ in one-based indexing. Every length-five
palindromic subsequence has exactly one centre, so classifying subsequences by their centre
partitions them: nothing is counted twice and nothing is missed. Once $k$ is fixed, the
remaining choices split into two independent halves:

- the **left pair** $(i, j)$ with $i < j < k$, contributing the ordered digit pair
  $(s_i, s_j) = (a, b)$;
- the **right pair** $(l, m)$ with $k < l < m$, which must contribute the ordered digit pair
  $(s_l, s_m) = (b, a)$ — the same two digits in the opposite order.

For a fixed centre $k$ and a fixed ordered digit pair $(a, b)$, every left pair of type
$(a, b)$ can be combined with every right pair of type $(b, a)$, and each such combination
is a different index tuple. The choices do not interfere because the left pair uses indices
below $k$ and the right pair uses indices above $k$. The number of subsequences centred at
$k$ is therefore the product of the two counts, and the answer is

$$
\text{answer} = \sum_{k=1}^{n} \sum_{a=0}^{9} \sum_{b=0}^{9}
L_k(a,b) \cdot R_k(b,a) \pmod{10^{9}+7},
$$

where $L_k(a,b)$ counts pairs $i < j < k$ with digits $(a,b)$ and $R_k(a,b)$ counts pairs
$k < l < m$ with digits $(a,b)$. Only $10 \times 10 = 100$ ordered digit pairs exist, so
each centre needs only a hundred product terms, no matter how long the string is.

## 3. Worked trace on `"103301"`

The instance has the six one-based positions shown below, and the centre at $k = 6$ has an
empty right side, while the centre at $k = 1$ has an empty left side. Both contribute
nothing, because a pair cannot be formed from fewer than two positions.

| Centre $k$ | Digit $s_k$ | Left positions | Nonzero left pair counts $L_k(a,b)$ | Right positions | Nonzero right pair counts $R_k(a,b)$ | Subsequences centred here | Running total |
|:---:|:---:|:---|:---|:---|:---:|:---:|:---:|
| 1 | `1` | none | none | 2–6 | $(0,1)\!:\!2$, $(0,3)\!:\!2$, $(0,0)\!:\!1$, $(3,3)\!:\!1$, $(3,0)\!:\!2$, $(3,1)\!:\!2$ | 0 | 0 |
| 2 | `0` | 1 | none | 3–6 | $(3,0)\!:\!2$, $(3,1)\!:\!2$, $(3,3)\!:\!1$, $(0,1)\!:\!1$ | 0 | 0 |
| 3 | `3` | 1–2 | $(1,0)\!:\!1$ | 4–6 | $(3,0)\!:\!1$, $(3,1)\!:\!1$, $(0,1)\!:\!1$ | 1 | 1 |
| 4 | `3` | 1–3 | $(1,0)\!:\!1$, $(1,3)\!:\!1$, $(0,3)\!:\!1$ | 5–6 | $(0,1)\!:\!1$ | 1 | 2 |
| 5 | `0` | 1–4 | $(1,0)\!:\!1$, $(1,3)\!:\!2$, $(0,3)\!:\!2$, $(3,3)\!:\!1$ | 6 | none | 0 | 2 |
| 6 | `1` | 1–5 | $(1,0)\!:\!2$, $(1,3)\!:\!2$, $(0,3)\!:\!2$, $(0,0)\!:\!1$, $(3,3)\!:\!1$, $(3,0)\!:\!2$ | none | none | 0 | 2 |

Only the centres at positions $3$ and $4$ contribute, and each contributes exactly one
subsequence. The product calculation below shows why, and also shows which left pairs die
for lack of a mirror image.

| Centre $k$ | Left pair $(a,b)$ | Count $L_k(a,b)$ | Required right pair $(b,a)$ | Count $R_k(b,a)$ | Product |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 3 | $(1,0)$ | 1 | $(0,1)$ | 1 | 1 |
| 4 | $(1,0)$ | 1 | $(0,1)$ | 1 | 1 |
| 4 | $(1,3)$ | 1 | $(3,1)$ | 0 | 0 |
| 4 | $(0,3)$ | 1 | $(3,0)$ | 0 | 0 |

The two surviving tuples are $(1,2,3,5,6)$ and $(1,2,4,5,6)$ in one-based positions. Both
read `"1"`, `"0"`, `"3"`, `"0"`, `"1"`, that is `"10301"`, and both are valid palindromic
subsequences of length $5$. The answer is $2$, matching the expected output. The two tuples
differ only in whether the centre is the first or the second `3`; the values are identical
but the index sets are not, and the count is over index sets.

## 4. Sweeping the centre instead of rebuilding the pair counts

The pair counts of section 2 can be maintained incrementally rather than recomputed for each
centre. Moving the centre from $k$ to $k+1$ changes the two sides in a precise way: the old
centre position $k$ joins the left side, and position $k+1$ leaves the right side.

- The left side gains every pair that **ends** at position $k$, namely $(i, k)$ for all
  $i < k$.
- The right side loses every pair that **starts** at position $k+1$, namely
  $(k+1, m)$ for all $m > k+1$.

| Centre moves | Digit entering the left side | Left pairs gained | Digit leaving the right side | Right pairs lost |
|:---:|:---:|:---|:---:|:---|
| $1 \to 2$ | `1` at position 1 | none, there is no earlier position | `0` at position 2 | $(0,3)$ twice, $(0,0)$ once, $(0,1)$ once |
| $2 \to 3$ | `0` at position 2 | $(1,0)$ once | `3` at position 3 | $(3,3)$ once, $(3,0)$ once, $(3,1)$ once |
| $3 \to 4$ | `3` at position 3 | $(1,3)$ once, $(0,3)$ once | `3` at position 4 | $(3,0)$ once, $(3,1)$ once |
| $4 \to 5$ | `3` at position 4 | $(1,3)$ once, $(0,3)$ once, $(3,3)$ once | `0` at position 5 | $(0,1)$ once |
| $5 \to 6$ | `0` at position 5 | $(1,0)$ once, $(0,0)$ once, $(3,0)$ twice | `1` at position 6 | none, there is no later position |

Checking the arithmetic against the centre table confirms the sweep: after the first two
moves the left pair counts are exactly $(1,0)\!:\!1$, which is the centre-$3$ row, and after
the third move they are $(1,0)\!:\!1$, $(1,3)\!:\!1$, $(0,3)\!:\!1$, which is the centre-$4$
row. The right counts shrink in the same way. Because a sweep keeps only the $100$ pair
counts of each side, no table indexed by position is ever needed — that is the memory-saving
form of the same computation.

## 5. Why the counting is correct

The invariant that makes the formula exact is:

> For every centre position $k$, the product $L_k(a,b) \cdot R_k(b,a)$ equals the number of
> length-five palindromic subsequences whose centre is $k$ and whose outer two digit values
> are $a$ and inner two digit values are $b$, and summing over $k$ and $(a,b)$ counts every
> such subsequence exactly once.

Two facts establish it. First, **every** palindromic subsequence of length five has a unique
third position, so assigning it to the centre $k$ is a well-defined partition of the whole
set; no tuple is assigned to two centres and no tuple is left unassigned. Second, once $k$ is
fixed, a tuple is completely described by its left pair and its right pair. The palindromic
condition reduces to $s_i = s_m$ and $s_j = s_l$, which is precisely the statement that the
left pair $(a,b)$ and the right pair $(b,a)$ match; the centre digit itself places no
restriction. Counting combinations is therefore a product: if $L_k(a,b)$ left pairs and
$R_k(b,a)$ right pairs share the centre $k$, all $L_k(a,b) \cdot R_k(b,a)$ combinations are
distinct index tuples — the left pair alone distinguishes them within the left side and the
right pair alone distinguishes them within the right side — and all of them are valid.

The partition argument also shows where a naive value-based count would go wrong. If the
answer were "the number of distinct palindromic strings", the duplicate `"10301"` in this
instance would count once and the answer would be $1$. Counting index tuples is what makes
the product form correct, and it is also why the algorithm never needs to know which string
a pair spells — only how many pairs of each digit type exist.

## 6. Boundary and trap analysis

| Situation | Instance | Trap | What actually happens | Outcome |
|:---|:---|:---|:---|:---|
| Fewer than five positions | `"1234"`, `"111"`, `"1"` | expect a small positive count | there is no index tuple with five distinct positions | `0` |
| Exactly five positions | `"01210"` | expect several centres to contribute | only $k = 3$ has two positions on each side, and the single tuple is the whole string | `1` |
| All digits identical, length seven | `"0000000"` | try to count digit patterns instead of positions | all $\binom{7}{5} = 21$ index tuples are palindromic and all spell `"00000"` | `21` |
| All digits identical, length six | `"000000"` | expect a power of two or a Fibonacci-style value | the count is the binomial coefficient $\binom{6}{5} = 6$: choose the five positions | `6` |
| Two uniform blocks | `"9999900000"` | expect mixed palindromes spanning both blocks | a palindrome needs its two inner positions on opposite sides of the centre; the `9`s all precede the `0`s, so only `"99999"` and `"00000"` survive | `2` |
| Repeated inner/outer pairs | `"001100"` | count the two occurrences of `"00100"` once | the two tuples $(1,2,3,5,6)$ and $(1,2,4,5,6)$ are different index sets | `2` |
| Nested mirrored values | `"123454321"` | assume only the outermost symmetric choices count | several layered pairs around different centres are valid; the count is $14$ | `14` |
| Duplicated values from distinct indices | `"103301"` | deduplicate identical subsequence strings | the same string `"10301"` arises from two index tuples and both count | `2` |
| Large answers | any long string | let products overflow or skip the modulus | each product is bounded by about $5 \cdot 10^{7} \cdot 5 \cdot 10^{7}$, and the running sum is reduced modulo $10^{9}+7$ after each term | reduced value |

The first and the second-to-last rows pull in opposite directions and together define the
problem. Too few positions makes the answer zero regardless of how many matching digits
exist; many positions with repeated digits inflate the answer far beyond the number of
distinct strings, because subsequences are counted by position.

## 7. Alternatives and why the centre-product method is preferred

| Approach | Idea | Cost | Failure mode or tradeoff |
|:---|:---|:---|:---|
| Enumerate all five-position tuples | take every set of five positions and test the palindrome condition directly | $\binom{n}{5}$ tuples | infeasible: for $n = 10^{4}$ this is about $8 \cdot 10^{17}$ tuples |
| Enumerate all length-five subsequences by value | generate the $\binom{n}{5}$ digit strings and deduplicate them | exponential in practice | wrong as well as slow: the problem counts positions, and deduplication would discard exactly the duplicates that must be counted |
| General palindromic-subsequence dynamic programming | count palindromic subsequences of every length by interval recursion, then read off length five | $O(n^{2})$ states and transitions | correct but far heavier than needed; it tracks all lengths and all interval boundaries, while only length five with a fixed centre structure matters here |
| Centre-product with per-position pair tables | store $L_k$ and $R_k$ for every position as tables of $100$ pair counts | $O(100n)$ time, $O(100n)$ space | the method used here when the tables are materialised: simple to verify, and the $O(100n)$ memory is acceptable for $n = 10^{4}$ |
| Centre-product with a moving sweep | keep one $100$-entry left table and one $100$-entry right table, gaining pairs that end at the old centre and losing pairs that start at the new one | $O(100n)$ time, $O(100)$ space | the same counting identity with constant memory; it needs care in the update order so that the pair ending at the old centre is added only after that centre has been scored |

## 8. Complexity: time and auxiliary space

Let $n$ be the length of `s` and let $A = 10$ be the number of distinct digits, so the number
of ordered digit pairs is $A^{2} = 100$.

**Time.** For each centre position, the formula needs the $100$ products
$L_k(a,b) \cdot R_k(b,a)$ and their sum, which is a constant amount of work per centre, so
the scoring pass is $O(100n) = O(n)$. Building the pair counts is the only other cost. A
single pass over the string can accumulate all pair counts that end at each position: when
position $p$ with digit $d$ is visited, the pairs ending there are $(c, d)$ for each digit
$c$, so the counts for those pairs increase by the number of earlier occurrences of $c$ —
again $A$ operations per position, hence $O(100n)$. Maintaining both the prefix pair counts
and the suffix pair counts therefore costs $O(100n)$ time in total. Since $A = 10$ is fixed
by the alphabet, the whole method is linear in $n$: $O(100n)$ with the explicit constant.
The sweep of section 4 replaces the two position-indexed tables with constant-size updates
at each of the $n$ steps, so it does not change the time bound.

**Auxiliary space.** The materialised version stores, for each of the $n$ centres, two
$10 \times 10$ tables of counts — one for the pairs entirely to its left and one for the
pairs entirely to its right. That is $O(100n)$ integers, which at $n = 10^{4}$ is on the
order of a million small counters: linear in $n$, and the dominant memory cost of the
method. The sweep version keeps only the current left and right $10 \times 10$ tables plus
the digit-occurrence counters used to update them, which is $O(100)$ space, constant in $n$.
Either way, no structure proportional to the number of subsequences is ever built, which is
essential because that number can be as large as $\binom{10^{4}}{5}$ before reduction.