## General

**What a positive entry reveals**

Two suffixes have a positive common-prefix length exactly when their first characters are equal. Therefore `lcp[i][j] > 0` partitions positions into character-equality groups. Process positions from left to right. When position $i$ has no assigned character, give its entire positive-entry group the next unused letter. The first unassigned group contains the smallest index at which any choice remains, so assigning `a`, then `b`, and so on produces the lexicographically smallest possible candidate.

Only 26 lowercase letters are available. Encountering a 27th group proves that no valid result exists.

**Why construction must be followed by validation**

Positive versus zero entries reveal only whether two starting characters match; they do not prove the claimed prefix lengths. For any actual string, the complete recurrence is

$$
L(i,j) =
\begin{cases}
0, & \text{if the characters at } i \text{ and } j \text{ differ},\\
1 + L(i+1,j+1), & \text{if they match},
\end{cases}
$$

where the continuation term is zero once either suffix ends. Scan the matrix from bottom right to top left and compare every supplied entry with this recurrence. The continuation value is already present at `lcp[i + 1][j + 1]`, so no second matrix is needed. A mismatch catches incorrect diagonals, asymmetry, non-transitive equality claims, impossible lengths, and every other inconsistency.

If all entries agree, the constructed string generates exactly the requested matrix. Its left-to-right earliest-letter assignment also proves that no valid string can be lexicographically smaller.

## Complexity detail

There are $n^2$ matrix entries. Group construction inspects at most $n^2$ entries, and validation performs constant work per entry, for $O(n^2)$ time. The output character array uses $O(n)$ additional space; the given LCP matrix is input storage and is not duplicated.

## Alternatives and edge cases

- **Union-find grouping:** Unite every pair with a positive LCP value, order components by their smallest index, and label them greedily. This is valid but adds parent and rank machinery without avoiding the mandatory quadratic validation.
- **Rebuilding a produced LCP matrix:** Dynamic programming can generate the candidate's complete matrix and compare it with the input. It keeps the same $O(n^2)$ time but consumes an unnecessary $O(n^2)$ auxiliary matrix.
- **Pairwise suffix comparison:** Directly compare characters for every pair of suffixes. It is straightforward but can revisit the same suffix tails and grow to $O(n^3)$ time.
- **Single position:** The only valid matrix is `[[1]]`, whose smallest string is `"a"`.
- **More than 26 equality groups:** A lowercase English result cannot represent them, so the answer is empty.
- **Invalid diagonal or recurrence:** Each diagonal must equal the remaining suffix length, and matching positions must extend the next diagonal pair by exactly one; validation rejects any violation.
