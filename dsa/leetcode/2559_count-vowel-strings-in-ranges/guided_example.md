# Guided Example: Count Vowel Strings in Ranges

## 1. The question hiding inside each query

We are given a 0-indexed list of lowercase words and a list of index ranges. For a range `[l, r]` the task is not to describe the words: it is to report *how many* of the words at indices $l, l+1, \dots, r$ both begin and end with a vowel, where the vowel set is fixed to `a`, `e`, `i`, `o`, `u`.

Two structural facts about that sentence decide the whole method. First, qualification is a property of one word in isolation — it never depends on neighbouring words — so it can be evaluated once per index and frozen into a 0/1 label. Second, each query asks for a count over a **contiguous index interval**, which is precisely the shape a prefix sum answers with a single subtraction. The work therefore splits into one classification pass and one accumulation pass; after that, no query ever looks at a word again.

Name the labels explicitly. Let

$$
b_i = \begin{cases} 1 & \text{if } \texttt{words[i]} \text{ starts and ends with a vowel} \\ 0 & \text{otherwise} \end{cases}
$$

The required output for a query `[l, r]` is then the plain interval sum $\sum_{i=l}^{r} b_i$.

## 2. Reducing a word to one bit

The endpoint test reads exactly two characters of `words[i]`: the first character `words[i][0]` and the last character `words[i][-1]`. Every interior character is irrelevant, which is why the bound on word length never influences the running time — the test costs the same for a one-letter word and a forty-letter word.

A word qualifies only when **both** lookups land in the vowel set $\{a, e, i, o, u\}$. The word length matters for one reason only: when a word has length $1$, its first and last characters are the *same* character, so a single-letter vowel such as `"e"` satisfies both halves of the test at once, while a single-letter consonant such as `"z"` fails both. Nothing in the rule excludes that case, and the contract explicitly allows a length of one, so the collapse must be handled by the ordinary test rather than by a special branch.

## 3. Worked instance: the first official sample

Take `words = ["aba", "bcb", "ece", "aa", "e"]` with `queries = [[0,2], [1,4], [1,1]]`; the required result is `[2, 3, 0]`.

Classifying each index once:

| Index $i$ | Word `words[i]` | First character | Last character | Both in the vowel set? | Label $b_i$ |
|---|---|---|---|---|---|
| 0 | `"aba"` | `a` | `a` | yes; the interior `b` is irrelevant | 1 |
| 1 | `"bcb"` | `b` | `b` | no; `b` is not a vowel | 0 |
| 2 | `"ece"` | `e` | `e` | yes; the interior `c` is irrelevant | 1 |
| 3 | `"aa"` | `a` | `a` | yes | 1 |
| 4 | `"e"` | `e` | `e` | yes; the only letter serves as both endpoints | 1 |

The label row is `1 0 1 1 1`, so four of the five words qualify. Index 1 is the interesting negative: `"bcb"` looks vowel-rich in its interior, but only endpoints are consulted, and both of its endpoints are consonants.

## 4. Turning labels into a prefix table

Define the prefix array by accumulating labels from the left:

$$
P_k = \sum_{i=0}^{k-1} b_i \quad \text{for } 0 \le k \le n
$$

so $P_0 = 0$ (the empty prefix) and $P_n$ equals the total number of qualifying words.

| Prefix entry | $P_0$ | $P_1$ | $P_2$ | $P_3$ | $P_4$ | $P_5$ |
|---|---|---|---|---|---|---|
| Labels included | none | $b_0$ | $b_0, b_1$ | $b_0 \dots b_2$ | $b_0 \dots b_3$ | $b_0 \dots b_4$ |
| Value | 0 | 1 | 1 | 2 | 3 | 4 |
| Formed by | the empty prefix | $P_0 + b_0$ | $P_1 + b_1$ | $P_2 + b_2$ | $P_3 + b_3$ | $P_4 + b_4$ |

The value at $P_2$ staying equal to $P_1$ is the signature of the zero label at index 1: a non-qualifying word contributes nothing and leaves the running total flat.

## 5. Answering all three queries

Because $P$ stores running totals, a range sum telescopes into two table lookups:

$$
\sum_{i=l}^{r} b_i = P_{r+1} - P_l
$$

| Query | $l$ | $r$ | Left term | Right term | Difference | Required output |
|---|---|---|---|---|---|---|
| `[0,2]` | 0 | 2 | $P_0 = 0$ | $P_3 = 2$ | 2 | 2 |
| `[1,4]` | 1 | 4 | $P_1 = 1$ | $P_5 = 4$ | 3 | 3 |
| `[1,1]` | 1 | 1 | $P_1 = 1$ | $P_2 = 1$ | 0 | 0 |

Every value matches the required result. The third query is the instructive one: it covers the single non-qualifying index, and it is answered by subtracting two equal prefix values, producing $0$ without any word being re-inspected.

## 6. Why the subtraction is valid

The whole method rests on one invariant, maintained by construction of the prefix array:

> **Invariant.** For every $k$ with $0 \le k \le n$, the entry $P_k$ equals the number of qualifying words among indices $0, 1, \dots, k-1$.

The base case $k = 0$ counts the empty index set, which is $0$. Each induction step appends the single label $b_k$ to the already-counted set, giving $P_{k+1} = P_k + b_k$; because that rule is applied at every step, the invariant holds for all $n+1$ entries.

Now split the queried interval into two nested prefixes. The indices $0 \dots r$ are the disjoint union of $0 \dots l-1$ and $l \dots r$, so counting is additive:

$$
\underbrace{\sum_{i=0}^{r} b_i}_{P_{r+1}} = \underbrace{\sum_{i=0}^{l-1} b_i}_{P_l} + \sum_{i=l}^{r} b_i
$$

Rearranging isolates the term we want, which is exactly $P_{r+1} - P_l$. That is the correctness argument in full: the difference recovers the count of the requested window and nothing outside it, and the derivation used only additivity of counting over disjoint sets.

Two consequences matter because they are what make the queries cheap. The prefix array is **non-decreasing** ($b_i \ge 0$ implies $P_{k+1} \ge P_k$), so every answer lies between $0$ and $r - l + 1$; and because each query touches only two cells, the query stage has no dependence on how long the window is.

## 7. Boundary behaviour the sample does not show

The chosen instance contains a single-letter word at index 4, but it does not exhibit the other endpoint failures. Exercising them separately:

| Boundary instance | Word | First character | Last character | Label | What it teaches |
|---|---|---|---|---|---|
| Single vowel | `"u"` | `u` | `u` | 1 | One character fills both endpoint roles, so a length-one word can qualify |
| Single consonant | `"z"` | `z` | `z` | 0 | The same collapse occurs, but the shared character is outside the vowel set |
| Vowel start, consonant end | `"owl"` | `o` | `l` | 0 | Matching one endpoint is not sufficient; the rule is a conjunction |
| Consonant start, vowel end | `"ab"` | `a` | `b` | 0 | The mirror failure; a leading `a` alone proves nothing |
| Long word tested only at its ends | a word starting `a` and ending `u` | `a` | `u` | 1 | Interior length never changes the label |
| Window of one index | `[1,1]` | — | — | read from $P$ | Inclusive bounds make $l = r$ a legal, non-empty window answered by $P_{r+1} - P_r$ |
| Window spanning the entire array | `[0, n-1]` | — | — | read from $P$ | The answer is $P_n - P_0 = P_n$, the global count |

The last two rows are why the prefix array is built with $n+1$ entries rather than $n$: the index $r+1$ must be addressable even when $r$ is the final index, and the index $l$ must be addressable even when $l$ is $0$.

## 8. Other correct methods and their trade-offs

| Method | Preprocessing | Per query | Total cost | Assessment |
|---|---|---|---|---|
| Rescan the queried slice | none | $O(r - l + 1)$ | $O(nq)$ in the worst case | Correct, but with both $n$ and $q$ up to $10^5$ it can perform $10^{10}$ steps |
| Prefix-sum array | $O(n)$ | $O(1)$ | $O(n + q)$ | The method derived above; minimal per-query work and simple state |
| Sorted list of qualifying indices, then two binary searches | $O(n)$ | $O(\log n)$ | $O(n + q \log n)$ | Correct: count stored indices inside `[l, r]` by locating the first index at least $l$ and the first index greater than $r$ |
| Fenwick tree over the labels | $O(n)$ | $O(\log n)$ | $O(n + q \log n)$ | Correct, and it additionally supports point updates — a capability this problem never requests |
| Precomputed table of every window count | $O(n^2)$ | $O(1)$ | $O(n^2)$ time and memory | Constant per query in theory, impossible in practice for $n = 10^5$ |

The binary-search variant is the closest competitor and is a legitimate answer, but it pays a logarithmic factor per query to preserve information — the sorted index list — that the output never uses. The problem asks only *how many*, never *which*, so answers can be stored as plain counts and the prefix array dominates.

## 9. Traps this instance exposes

- **Reading the range as half-open.** `[l, r]` is inclusive at both ends. Treating it as the half-open interval $[l, r)$ silently drops the word at index $r$. The correct prefix indices are $l$ and $r+1$.
- **Testing only one endpoint.** `"owl"` and `"ab"` both look vowel-adjacent but fail. The rule is a conjunction, so accepting either endpoint over-counts.
- **Forgetting that a length-one word has one character in both roles.** Rejecting a word whose first and last characters coincide, or special-casing short words, loses `"e"` and `"u"` from the count.
- **Confusing the label array with the answer.** $b_i$ answers a single-index question, while the output is a window aggregate. Emitting labels, or prefix entries, instead of differences is a different and wrong output shape.
- **Recomputing the classification inside the query loop.** That discards the entire benefit of the preprocessing pass and degrades the method toward the $O(nq)$ rescan.
- **Widening the vowel set or ignoring case.** The stated set is exactly `a`, `e`, `i`, `o`, `u`, and the input is guaranteed to be lowercase; adding `y` or folding case changes results for words the contract deliberately excludes.
- **Assuming the prefix array starts at the first word's label.** Without the leading $P_0 = 0$ entry there is no way to express a window that starts at index $0$ as a difference, so `[0,2]` becomes unspeakable in the prefix language.

## 10. Time and auxiliary space

Let $n$ be the number of words, $q$ the number of queries, and $L$ the maximum word length.

- **Classification.** Each of the $n$ words is examined at two fixed character positions. Reading a character by position is constant time, so this pass costs $O(n)$ and does not depend on $L$ at all.
- **Prefix construction.** Every entry is one addition over the previous entry: $O(n)$.
- **Query answering.** Each query performs two array reads and one subtraction: $O(1)$ per query, so $O(q)$ overall.
- **Total time complexity.** $O(n) + O(n) + O(q) = O(n + q)$, linear in the input size and comfortably inside the limits $n, q \le 10^5$.
- **Auxiliary space complexity.** A label array and a prefix array cost $O(n)$ integers each, and the returned list costs $O(q)$ integers, so auxiliary space is $O(n + q)$. The returned list is required by the contract; the only avoidable structure is the prefix array, and it is exactly what buys constant-time queries.

The trade is the classic one for range queries on a static array: spend one linear pass of time and memory up front so that every later query collapses to a subtraction.
