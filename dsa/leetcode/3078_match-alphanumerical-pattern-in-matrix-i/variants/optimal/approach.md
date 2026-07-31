## General

Let the board dimensions be $R \times C$ and the pattern dimensions be $p \times q$.

**Search in the required result order.** Visit every top-left position where the $p \times q$ pattern fits, with rows increasing first and columns increasing within each row. The first valid placement is therefore automatically the answer with the smallest row and then the smallest column.

**Validate fixed digits directly.** At a pattern cell containing a decimal digit, the corresponding board value must equal that digit. A fixed digit does not participate in the letter-to-digit injectivity map: a letter is allowed to receive the same numeric value as a literal digit elsewhere.

**Maintain both directions for letters.** For letter cells, store `symbol_to_digit` so repeated occurrences of one letter must see the same board value. Also store `digit_to_symbol` so two distinct letters cannot receive the same value. Whenever either direction contradicts an established assignment, reject the current placement immediately. If every cell passes, the placement satisfies all literal, consistency, and distinct-letter requirements.

The two maps are sufficient in both directions. Any accepted placement obeys every rule by construction. Conversely, a valid placement never contradicts a fixed digit or either stored mapping, so the scan reaches its end and accepts it. Since candidate positions are examined in row-major order, the first accepted placement is exactly the requested coordinate pair.

## Complexity detail

There are at most $(R-p+1)(C-q+1)$ candidate placements, and validating one examines $pq$ cells. The tighter running time is $O((R-p+1)(C-q+1)pq)$, which is $O(RCpq)$.

Only mappings for lowercase letters and digits are needed. Their domains are bounded by the fixed alphabet and the ten board digits, so the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Pairwise cell comparisons:** Comparing every pair of pattern cells can verify equality relationships without maps, but costs $O((pq)^2)$ per placement instead of $O(pq)$.
- **Canonicalized signatures:** Converting each candidate and the pattern into first-occurrence signatures can express the letter structure, but fixed digit cells still require separate handling and temporary storage.
- **Letter versus literal digit:** A letter may map to the same numeric value as a fixed digit; injectivity applies between distinct letters, not between a letter and a literal symbol.
- **Repeated letter:** All of its cells must contain the same board digit.
- **Distinct letters:** They must map to distinct board digits, even if each letter appears only once.
- **Pattern does not fit:** Return `[-1, -1]` immediately when $p>R$ or $q>C$.
- **Multiple matches:** Row-major traversal makes the first match the required smallest coordinate pair.
- **All-literal pattern:** No letter maps are needed; every cell must match its fixed digit exactly.
