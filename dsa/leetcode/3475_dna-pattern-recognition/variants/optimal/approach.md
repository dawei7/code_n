## General

**Project four independent Boolean indicators for every sample.** This query does not filter out any row. It selects the original `sample_id`, `dna_sequence`, and `species`, then evaluates four pattern expressions. MySQL returns the truth value of each expression as zero or one, giving the requested indicator columns.

Because the schema states that DNA sequences use `A`, `T`, `G`, and `C`, the literal uppercase patterns directly match the declared representation.

**Detect a start codon only at the beginning.** The expression

`dna_sequence LIKE 'ATG%' AS has_start`

requires the first three characters to be `ATG`. In a `LIKE` pattern, the literal prefix must match at position zero, and `%` then accepts any suffix, including an empty one. A sequence containing `ATG` only in the middle does not pass because no leading wildcard appears.

For example, `ATGCT...` produces one, while `CGTATG...` produces zero even though it contains the same three letters later.

**Detect one of three stop codons at the end.** The regular expression

`TAA$|TAG$|TGA$`

has three alternatives. The dollar sign anchors each alternative to the end of the sequence. Therefore, a match is found only when the final three characters are `TAA`, `TAG`, or `TGA`. Merely containing one of these triples earlier is not enough.

Writing the end anchor in every alternative avoids ambiguity. The expression is logically equivalent to a grouped form such as `(TAA|TAG|TGA)$`.

**Find the repeated `ATAT` motif anywhere.** The expression

`dna_sequence LIKE '%ATAT%' AS has_atat`

places `%` on both sides, allowing any prefix and suffix. It returns one when `ATAT` occurs at least once, including at the beginning or end. Overlapping occurrences do not need separate treatment because the result is only a presence indicator.

**Recognize a run of at least three G characters.** The regular expression

`GGG+`

means two literal `G` characters followed by one or more additional `G` characters. The `+` quantifier applies only to the immediately preceding third `G`, so the minimum accepted run length is three. It also accepts `GGGG`, `GGGGG`, and longer runs. With no start or end anchor, the run may occur anywhere in the sequence.

This is subtly different from interpreting `+` as applying to the whole text `GGG`. In standard regular-expression grouping, repeating the whole triple would require `(GGG)+`. The ungrouped source pattern correctly expresses “at least three consecutive Gs.”

**Each condition is evaluated independently.** One sample may satisfy several patterns. `ATGGGGTCATCATAA` starts with `ATG`, ends with `TAA`, and contains a run of four Gs, so its projected indicators are $1,1,0,1$. No branch excludes evaluation of another column.

A sample matching none of them is still returned with four zeros. This follows from using expressions in `SELECT` rather than placing them in a `WHERE` clause.

**Order the complete result by sample ID.** `ORDER BY 1` refers to the first selected column, `sample_id`. Ascending order is SQL's default, so the output is ordered by unique sample ID as required. The ordinal notation is concise; the unique key ensures deterministic ordering.

**Why the query is correct.** The leading-literal `LIKE` accepts exactly sequences beginning with the start codon. The end-anchored alternation accepts exactly the three declared stop suffixes. The double-wildcard `LIKE` accepts exactly sequences containing the motif, and `GGG+` accepts exactly sequences with a contiguous G run of length at least three. Since all rows are selected and each Boolean is aliased to the requested output name, the query produces one correctly annotated row per sample, then orders those rows by ID.

The output retains the original DNA text and species without transformation. Pattern evaluation is observational only.

## Complexity detail

Let $S$ be the total number of characters across all DNA sequences and let $r$ be the number of sample rows. Each of the four fixed patterns can scan a sequence in time linear in its length in the ordinary engine model. Four constant-many scans still total $O(S)$.

Ordering all returned rows by `sample_id` costs $O(r\log r)$ in a general execution plan. If the optimizer reads through the unique-key index in order, it may avoid a separate sort, but the conservative logical bound is $O(S+r\log r)$, matching the manifest.

The query returns $r$ rows and may require $O(r)$ sort-key or result workspace, matching the manifest's space statement. Exact temporary memory is controlled by the database engine and chosen plan; the SQL text itself declares no growing procedural structure.

All patterns are fixed and contain no nested ambiguous repetition, so there is no reason to expect pathological exponential backtracking from these particular expressions.

## Alternatives and edge cases

- **Put pattern conditions in `WHERE`:** That would remove nonmatching samples, but the required output includes every sample with zero indicators.
- **Use `LIKE '%ATG%'` for `has_start`:** A leading wildcard would incorrectly accept `ATG` in the middle.
- **Omit the stop-codon end anchors:** Sequences containing `TAA`, `TAG`, or `TGA` internally would be false positives.
- **Anchor only the final alternative:** A pattern such as `TAA|TAG|TGA$` leaves the first two alternatives unanchored; the source correctly anchors all three.
- **Use `LIKE '%GGG%'`:** This also detects at least three consecutive Gs and is simpler, while `GGG+` explicitly accepts arbitrary longer runs.
- **Exactly two Gs:** `GGG+` cannot match because at least three G characters are required.
- **Four or more Gs:** The `+` consumes the additional Gs and still returns one.
- **Overlapping `ATAT` motifs:** Presence remains one regardless of how many overlapping matches occur.
- **Short sequences:** A sequence shorter than three cannot match start or stop codons, and one shorter than four cannot match `ATAT`; the expressions naturally return zero.
- **Multiple simultaneous patterns:** Columns are independent, so any combination of zeros and ones is possible.
- **Case sensitivity:** The schema declares uppercase DNA characters. If mixed-case data were allowed under a case-insensitive collation, explicit binary or case-sensitive matching might be needed.
- **`NULL` DNA sequence:** Pattern expressions evaluate to SQL null rather than zero; the reference schema does not specify null rows, so the query follows the declared data model.
- **`ORDER BY 1` maintainability:** It is correct while `sample_id` is the first selected column, though naming the column directly can be clearer during later query edits.
