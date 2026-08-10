## General

**Translate the requirement into an existence test**

For each candidate word `s`, the question is not how many times it occurs or where it begins. It only asks whether at least one different array element contains `s` as a contiguous substring. That is an existential condition:

$$
\text{keep } s \iff \text{there exists an index } j \ne i \text{ such that } s \text{ is contained in } \texttt{words}[j].
$$

The stored solution expresses that definition almost word for word. The outer loop visits every word together with its index:

```python
for i, s in enumerate(words):
```

Keeping `i` is necessary because the candidate must occur in another word. Every string is trivially a substring of itself, so a search that includes the same array position would incorrectly accept every input.

**How the inner generator checks all possible containers**

For the current candidate, this expression examines the array again:

```python
any(i != j and s in t for j, t in enumerate(words))
```

Each generated Boolean combines two requirements:

- `i != j` ensures that `t` comes from a different array position.
- `s in t` uses Python's substring operation, which is true only when all characters of `s` occur contiguously and in order somewhere within `t`.

The word “substring” is stricter than “subsequence.” For example, `"ace"` is a subsequence of `"abcde"` but not a substring because its letters are separated. Python's `in` operation performs the required contiguous search.

The `and` operator short-circuits from left to right. When `i == j`, Python does not even evaluate `s in t`. This avoids counting the candidate's occurrence in itself and skips an unnecessary search.

**Why `any` matches the problem exactly**

`any` returns true as soon as the generator produces its first true value. Once one other word contains `s`, no further evidence can change whether `s` belongs in the answer. The early exit saves work when a match occurs near the beginning of the list.

If every different word fails the substring check, the generator is exhausted and `any` returns false. The candidate is then omitted. Thus the condition has exactly the two outcomes required by the contract.

When the condition is true, `ans.append(s)` stores the original string. The algorithm appends at most once for each outer-loop position, even if several different words contain it. The input guarantee that all words are unique further means the returned list cannot contain duplicate string values.

**A trace on the first example**

For `words = ["mass", "as", "hero", "superhero"]`:

| Candidate | Relevant comparisons | Decision |
|---|---|---|
| `"mass"` | It is not contained in `"as"`, `"hero"`, or `"superhero"` | omit |
| `"as"` | `"as" in "mass"` is true | append |
| `"hero"` | `"hero" in "superhero"` is true | append |
| `"superhero"` | No other word is long enough to contain it | omit |

The result is `["as", "hero"]`. It follows input order because the outer loop follows input order, although the contract allows any order.

**Length is an implicit rejection test**

A longer string cannot be contained in a shorter string. The code does not write an explicit `len(s) <= len(t)` condition because Python's substring operation already returns false when the candidate is longer. Omitting the redundant test keeps the expression compact without changing behavior.

Likewise, the code does not manually enumerate starting positions. Conceptually, for candidate length $a$ and container length $b$, a substring search tries positions from zero through $b-a$ and looks for a complete character match. The built-in operation owns that low-level work.

**Why the result is correct**

Consider any word appended to `ans`. It was appended only because `any` found some pair index `j` with `j \ne i` and `s in words[j]`. Therefore, it is a substring of another input word and must be included.

Conversely, consider any input word that is a substring of another word. When the outer loop reaches its index `i`, the generator eventually examines the containing word's different index `j`. Both parts of the conjunction are true, so `any` returns true and the word is appended. Therefore, every required word is included.

Together, these directions show that `ans` contains exactly the requested words. The index inequality prevents false positives from self-matching, and appending outside the inner generator prevents repeated output for multiple containers.

## Complexity detail

Let $n$ be the number of words and let $L$ be the maximum word length. The outer loop has $n$ iterations. In the worst case, `any` examines all $n$ possible container positions for every candidate, giving $O(n^2)$ pair checks.

A straightforward substring test may examine $O(L)$ starting positions and compare up to $O(L)$ characters at each one, for $O(L^2)$ worst-case work per pair. Under that general model, the complete bound is $O(n^2L^2)$, matching the manifest. Python's built-in string search uses optimized implementation techniques and is often closer to linear in the two string lengths, but the approach does not depend on a particular runtime's optimization for correctness.

The generator consumed by `any` is lazy, so it does not build a list of all pair results. Apart from the output, the loops retain only a few indices and string references. The answer can contain up to $n$ word references, so the stored solution's total additional list storage is $O(n)$. If output storage is excluded, auxiliary working space is $O(1)$.

Early termination can make real execution smaller: a candidate whose first different comparison matches performs only one substring search. The worst-case bound still applies when no candidate matches or when each match occurs at the final comparison.

## Alternatives and edge cases

- **Explicit nested loops:** Two ordinary loops plus `break` implement exactly the same method and may be easier for a beginner to debug. The generator with `any` is a concise version of that control flow.
- **Knuth-Morris-Pratt search:** Building an LPS table for each candidate makes each pairwise substring search linear in the text length. It improves the character-comparison bound but adds preprocessing code and state for the short maximum word length of 30.
- **Suffix trie:** Inserting every suffix of every word allows candidates to be queried through trie paths. It avoids checking every pair directly but can use $O(nL^2)$ nodes in the worst case and is substantially more complex.
- **Sort by length:** Processing shorter words first and comparing them only with longer words can skip impossible pairs. The uniqueness guarantee means equal-length distinct words cannot contain one another.
- **Concatenate with separators:** Searching for each word in a combined string is dangerous unless boundaries and the word's own occurrence are handled carefully. A match spanning a separator must never count.
- **Only one input word:** The generator sees only the same index, which fails `i != j`, so `any` is false and the answer is empty.
- **Candidate longer than container:** `s in t` safely returns false; no explicit length guard is required.
- **Candidate equal to another word:** The constraints say all strings are unique. Without that guarantee, equal strings at different indices would correctly count as one being a substring of another position.
- **Several containing words:** `any` stops at the first successful one, and the candidate is appended only once.
- **Substring at an edge:** Matches at position zero or ending at the final character are ordinary valid substring matches and are recognized by `in`.
- **Character order without contiguity:** Merely finding the same letters in order is insufficient. The use of `s in t` enforces adjacency.
