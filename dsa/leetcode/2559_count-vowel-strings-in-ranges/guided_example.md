# Guided Example: Count Vowel Strings in Ranges

## 1. One Representative Instance

Every entry of `words` either *qualifies* or does not: it qualifies when the vowel
letters `'a'`, `'e'`, `'i'`, `'o'`, `'u'` are both the first character and the last
character of the string. Each query `[l, r]` then asks how many qualifying entries
sit in the inclusive index range from `l` to `r`, and the answers must be returned
in the same order as the queries.

The instance traced here is the authored sample

```text
words   = ["aba", "bcb", "ece", "aa", "e"]
queries = [[0, 2], [1, 4], [1, 1]]
```

whose required output is `[2, 3, 0]`. It carries every idea the method needs: a
word rejected on its first letter, words accepted through matching vowel endpoints,
a single-letter word where first and last character coincide, and a query whose
range contains no qualifying entry at all.

| Query position | Query $[l_i, r_i]$ | Required `ans[i]` | Qualifying indices inside the range |
|:---:|:---:|:---:|:---|
| 0 | `[0, 2]` | 2 | 0, 2 |
| 1 | `[1, 4]` | 3 | 2, 3, 4 |
| 2 | `[1, 1]` | 0 | none |

## 2. Qualification Is a Property of Two Characters

A string qualifies only when *both* endpoint characters belong to the vowel set
$V = \{\texttt{a}, \texttt{e}, \texttt{i}, \texttt{o}, \texttt{u}\}$. Contents
between the endpoints are irrelevant, which matters because the maximum word
length is $40$ while only two characters decide the outcome. For an index $i$ write

$$
q(i) = [\, \texttt{words[i][0]} \in V \ \text{and}\ \texttt{words[i][-1]} \in V \,],
$$

the Iverson bracket of the qualification predicate, so $q(i) \in \{0, 1\}$.

| Index $i$ | `words[i]` | First character | Last character | Both vowels? | $q(i)$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | `"aba"` | `a` | `a` | yes | 1 |
| 1 | `"bcb"` | `b` | `b` | no, first letter | 0 |
| 2 | `"ece"` | `e` | `e` | yes | 1 |
| 3 | `"aa"` | `a` | `a` | yes | 1 |
| 4 | `"e"` | `e` | `e` | yes | 1 |

For the single-letter word `"e"` the first and last characters are the *same*
position, and it satisfies both endpoint tests, so it qualifies. For `"bcb"` the
last character is irrelevant once the first fails; a predicate that tested the
endpoints with "or" instead of "and" would wrongly accept it.

## 3. Turning a Property into a Range-Counting Structure

What a query needs is not the property of one word but a *count over an interval*.
Define the prefix count

$$
C(t) = \sum_{i=0}^{t} q(i), \qquad C(-1) = 0 .
$$

Two facts make this the right object. First, $C$ is non-decreasing and rises by at
most one per step, because every added term is $0$ or $1$. Second, and this is the
whole method, the number of qualifying indices in the inclusive interval $[l, r]$
is a difference of two prefix counts:

$$
\#\{i : l \le i \le r,\ q(i) = 1\} = C(r) - C(l - 1).
$$

The subtraction removes exactly the qualifying entries before `l` and leaves
exactly the qualifying entries inside the interval, and the inclusive boundary is
handled by using $C(l-1)$ rather than $C(l)$.

| Boundary $t$ | −1 | 0 | 1 | 2 | 3 | 4 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $q(t)$ | — | 1 | 0 | 1 | 1 | 1 |
| $C(t)$ | 0 | 1 | 1 | 2 | 3 | 4 |

The same numbers have a second reading. Collect the indices with $q(i) = 1$ into a
list. Because they are appended in increasing index order, the list
$Q = [0, 2, 3, 4]$ is automatically sorted, and the count of qualifying entries at
or below a boundary `t` is the number of elements of $Q$ that are at most `t`:

- $C(r)$ counts elements of $Q$ that are $\le r$;
- $C(l-1)$ counts elements of $Q$ that are $< l$.

Both counts are positions inside a sorted array, so they can be obtained by binary
search instead of by materialising the whole prefix array: a "last position at or
below `r`" search and a "first position not below `l`" search. The difference of
those two positions is the answer.

## 4. Executing Each Query

With $Q = [0, 2, 3, 4]$ the binary-search positions are read directly.

| Query | `l` | `r` | Count of $Q$ elements $< l$ | Count of $Q$ elements $\le r$ | Difference | Required |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 0 | 2 | 0 (nothing is below 0) | 2 (elements 0 and 2) | 2 | 2 |
| 1 | 1 | 4 | 1 (element 0 is below 1) | 4 (all four elements) | 3 | 3 |
| 2 | 1 | 1 | 1 (element 0 is below 1) | 1 (element 0 alone is at most 1) | 0 | 0 |

The third query is the informative one. Its range `[1, 1]` refers to the word
`"bcb"`, which does not qualify, so the two search positions coincide and the
difference is $0$. A method that counted the *length* of the range instead of the
qualifying entries inside it would answer `1` here.

## 5. Why the Reasoning Is Correct

**The prefix-invariant.** After the prefix of `words` up to index $i$ has been
scanned, $C(i)$ equals the number of qualifying entries among `words[0]` through
`words[i]`. The invariant holds at $i = -1$ with $C(-1) = 0$. Scanning index
$i+1$ adds $q(i+1) \in \{0,1\}$ to $C(i)$, so the count grows exactly when the new
word qualifies, which maintains the invariant. When the scan reaches the last
index, $C$ is fully determined by `words` alone, independently of the queries.

**Additivity over a split.** For any $l \le r$, the indices $0, \dots, r$ partition
into $0, \dots, l-1$ and $l, \dots, r$. Counting is additive over a partition, so
$C(r) = C(l-1) + \#\{i \in [l, r] : q(i) = 1\}$, which rearranges to the query
formula. This is why the inclusive endpoints require $l-1$: the entry at index `l`
must remain inside the counted part.

**Well-definedness of the sorted-list reading.** The list $Q$ is built by scanning
indices in increasing order and keeping those with $q(i) = 1$, so it is strictly
increasing. Therefore the number of its elements $\le r$ is a valid "insertion
position after equals" and the number of its elements $< l$ is a valid "insertion
position before equals"; taking the difference of these two positions counts
exactly the elements lying in $[l, r]$. The structure is a faithful
re-encoding of $C$, not an approximation of it, and each query is answered in
$O(\log n)$ without touching the words again.

| Query shape | $C(l-1)$ | $C(r)$ | Result | Reading |
|:---|:---:|:---:|:---:|:---|
| Range starts at `0` | 0 | any | $C(r)$ | No correction is needed at the left edge |
| Range of a single index | $C(l-1)$ | $C(l)$ | $q(l)$ | A single-index query just reports the predicate |
| Full array | 0 | $C(n-1)$ | total qualifying | The whole list is counted |
| Range with no qualifying entries | equal values | equal values | 0 | Both searches land on the same position |

## 6. Boundary Behaviour and the Traps This Instance Exposes

| Instance | Required output | What it tests |
|:---|:---|:---|
| `words = ["u"]`, `queries = [[0, 0]]` | `[1]` | A one-letter word where first and last position coincide |
| `words = ["ab", "ba", "bc"]`, `queries = [[0, 2], [0, 0], [1, 1]]` | `[0, 0, 0]` | One vowel endpoint is not enough; `"ba"` fails on its last letter |
| `words = ["a", "b", "e"]`, `queries = [[0, 2], [0, 1], [1, 2]]` | `[2, 1, 1]` | Inclusive boundaries: the entries at both `l` and `r` are counted |
| `words = ["aa", "bb", "ee", "cc"]`, `queries = [[0, 3], [0, 3], [1, 2], [2, 2]]` | `[2, 2, 1, 1]` | Repeated and overlapping queries are answered independently, in order |
| `words = ["apple", "owl", "ice"]`, `queries = [[0, 2], [1, 1]]` | `[2, 0]` | `"owl"` starts with a vowel but ends with a consonant |
| Long word of 40 characters, both endpoints vowels | 1 | Interior letters never matter; only the two endpoints are examined |

The traps worth naming:

- **Testing containment instead of endpoints.** Asking whether a word contains a
  vowel accepts `"bcb"` never, but accepts `"owl"` — which the statement rejects
  because its last character is `l`.
- **Assuming two distinct characters.** `"e"` and `"u"` are legal words of length
  one, and both endpoints coincide; a method that inspected a "second character"
  would be wrong or unsafe at the boundary.
- **Mixing up the two boundary searches.** Counting elements $< l$ is required on
  the left and elements $\le r$ on the right. Using $> l$ on the left drops a
  qualifying word that sits exactly at `l`; using $< r$ on the right drops one that
  sits exactly at `r`.
- **Reusing a stale per-query scan.** Answering each query by scanning its range
  is correct but costs $O(r - l + 1)$ per query; with up to $10^{5}$ queries over
  up to $10^{5}$ words that is far too slow, which is exactly what the shared
  prefix structure removes.
- **Reordering the answers.** The output array is indexed by query position, while
  the structure is indexed by word position. Sorting or grouping queries is a valid
  optimisation only if each answer is written back to its original slot.
- **Treating `y` as a vowel.** The note fixes the vowel set at `a`, `e`, `i`, `o`,
  `u`; habits from English orthography are not part of the contract. The
  constraints also guarantee lowercase input only.

## 7. Alternatives and Their Trade-offs

| Alternative | Preprocessing | Cost per query | Total | Trade-off |
|:---|:---:|:---:|:---:|:---|
| Direct scan of the queried range | none | $O(r - l + 1)$ | $O(nq)$ worst case | No structure at all; hopeless at the stated limits |
| Full prefix-count array | $O(n)$ | $O(1)$ | $O(n + q)$ | Fastest queries, but materialises $n + 1$ counters that must be precomputed before any query is answered |
| Sorted list of qualifying indices | $O(n)$ | $O(\log n)$ | $O(n + q \log n)$ | Stores only the qualifying positions, so its size adapts to how many words qualify; queries pay a logarithmic search |
| Offline sort of queries with a running scan | $O(q \log q)$ | amortised $O(1)$ | $O(n + q \log q)$ | Avoids binary search entirely but must restore the original query order before returning |

All four compute the same predicate counts; they differ only in when the counting
work happens. The sorted-index form is attractive when few words qualify, because
its storage is proportional to the number of qualifying entries rather than to the
number of words.

## 8. Time and Auxiliary Space

Let $n$ be the length of `words` and $q$ the number of queries. Inspecting the two
endpoint characters of a word is constant work, because indexing the first and last
character of a string does not depend on the word length; the constraint
$\sum \lvert \texttt{words[i]} \rvert \le 3 \cdot 10^{5}$ is therefore never paid in
full by this method.

- **Time:** $O(n + q \log n)$. Building the qualification structure scans `words`
  once, and each query performs two binary searches over a sorted list of at most
  $n$ positions, each costing $O(\log n)$. The prefix-array variant reaches
  $O(n + q)$ at the cost of $O(n)$ counters.
- **Space:** $O(n)$ auxiliary space in the worst case for the sorted list of
  qualifying indices, plus $O(q)$ for the returned answer array. If instead each
  query is answered directly from a prefix array, that array also needs $O(n)$
  integers, which is the same bound with a larger constant.