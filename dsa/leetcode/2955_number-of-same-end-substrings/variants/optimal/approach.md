## General

A substring is determined by its start and end indices. It is same-end when the characters at those two positions are equal.

For one character appearing $x$ times inside a query range:

- each occurrence forms a length-one same-end substring;
- every pair of distinct occurrences chooses a unique longer substring whose endpoints contain that character.

The count for that character is

$$
x+\binom{x}{2}
=
\frac{x(x+1)}2.
$$

The source answers range occurrence counts with per-character prefix arrays.

**Build prefix counts**

`cs = set(s)` contains only characters that actually appear. For every such character $c$, `cnt[c]` is an array of length $n+1$.

Prefix convention is:

$$
\texttt{cnt}[c][i]
=
\text{number of occurrences of }c\text{ in }\texttt{s}[0..i-1].
$$

All counts at prefix zero start at zero.

For each one-based prefix endpoint `i` corresponding to current character `a`:

1. Copy every character's count from prefix `i - 1` to `i`.
2. Increment `cnt[a][i]`.

After this update, all prefix arrays satisfy the definition.

Using only `set(s)` rather than all 26 letters saves constants. Characters absent from the entire string cannot contribute to any query.

**Count occurrences in an inclusive query**

For query `[l, r]`, the number of occurrences of character $c$ is

`x = cnt[c][r + 1] - cnt[c][l]`.

Prefix `r+1` includes positions through $r$, while prefix `l` includes positions before $l$. Their difference is exactly the inclusive range.

**Why `t` starts as the range length**

The source initializes

`t = r - l + 1`.

This counts all one-character substrings. Every position is same-end with itself, regardless of its character.

Then, for each $c$, it adds

`x * (x - 1) // 2`,

the number of pairs of distinct occurrences. Combining the initial singles across all characters with these pair terms is equivalent to summing $x(x+1)/2$ per character.

**Why occurrence pairs correspond one-to-one with substrings**

Choose two occurrences of the same character at positions $p<q$ inside the query range. They define exactly one substring `s[p..q]`, and its ends match.

Conversely, every same-end substring of length greater than one supplies exactly one pair of distinct equal-character endpoint occurrences. Interior characters do not affect qualification.

Therefore adding one for every equal-character pair counts all longer same-end substrings exactly once.

For a range containing character counts $a:3$, $b:2$, and $c:1$, singles contribute six. Pair terms contribute $\binom32+\binom22+\binom12=3+1+0$, for total ten.

**Answer each query independently**

The prefix tables are reusable. Each query loops over at most 26 present characters, calculates their range counts, and appends one result. Query order is preserved in `ans`.

## Complexity detail

Let $D=|\texttt{set}(s)|\le26$, $N=|s|$, and $Q$ be query count.

Building the tables takes $O(DN)$ time because the source copies all $D$ character counts at each position. Each query takes $O(D)$. Since $D$ is bounded by the fixed alphabet, total time simplifies to $O(N+Q)$.

The prefix arrays store $(N+1)D$ integers, using $O(DN)=O(N)$ space for fixed $D$. The returned answer uses $O(Q)$ output space.

## Alternatives and edge cases

- **Position lists plus binary search:** Store sorted indices per character and use two bisects per query, giving $O(\log N)$ per character per query with less dense storage.
- **Scan each query substring:** Counting characters directly costs up to $O(NQ)$ time.
- **All characters distinct in a range:** Only length-one substrings qualify, so result equals range length.
- **All characters equal:** Every substring is same-end, giving $L(L+1)/2$ for range length $L$.
- **Single-position query:** `t` starts at one and all pair terms are zero.
- **Inclusive right endpoint:** Use prefix index `r + 1`; using `r` would omit the final character.
- **Characters absent from a range:** Their $x$ is zero and pair contribution is zero.
- **Characters absent globally:** They have no prefix array and no possible contribution.
- **Set iteration order:** It is arbitrary but irrelevant because contributions are added commutatively.
- **Integer arithmetic:** The pair formula uses exact floor division after an always-even product.
- **Output order:** Results are appended in the same order as input queries.
- **Why interior content is irrelevant:** Once endpoints match, any characters between them are allowed; no additional substring scan or condition is needed.
- **Pair formula avoids double counting:** `C(x,2)` chooses an unordered earlier/later occurrence pair once. Ordered pairs would count each longer substring twice.
- **Prefix copying cost:** The exact source explicitly carries every present character's count to each next column rather than copying a whole dictionary, producing the stated $DN$ work.
- **Range length equals total singles:** `r-l+1` is also the sum of all per-character occurrence counts in the query, which proves the initial `t` accounts for every one-character substring exactly once.
- **Large answers:** A query spanning one repeated-character string has $N(N+1)/2$ results, so fixed-width implementations should use a sufficiently wide integer.
