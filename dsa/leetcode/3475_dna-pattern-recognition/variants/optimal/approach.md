## General

**Keep the four biological tests independent.** Every input row must remain in the result, so this is a projection rather than a filtering query. Each output flag is a `CASE` expression that maps one pattern predicate to `1` and its negation to `0`.

SQL `LIKE` expresses all four predicates directly. `ATG%` anchors `ATG` at the beginning. The three stop codons need separate suffix patterns—`%TAA`, `%TAG`, and `%TGA`—joined with `OR`, because any one of them is sufficient. `%ATAT%` finds the motif at any position, including overlapping occurrences, while `%GGG%` recognizes a run of at least three consecutive `G` characters; a longer run necessarily contains `GGG` as a substring.

The query projects the original `sample_id`, `dna_sequence`, and `species` beside those four expressions. Since the expressions neither join nor group rows, each sample produces exactly one output row. Finishing with `ORDER BY sample_id` establishes the required ascending order rather than relying on storage order.

## Complexity detail

Let $r$ be the number of rows and let

$$
S = \sum_{x \in \texttt{Samples}} \lvert x.\texttt{dna_sequence} \rvert.
$$

The pattern checks scan at most a constant number of times across each sequence, for $O(S)$ total matching work. Sorting the $r$ output rows costs $O(r\log r)$, so the overall time bound is $O(S+r\log r)$. The database may keep up to $O(r)$ rows or sort keys in temporary storage for the order operation; the `CASE` expressions themselves use constant space per row.

## Alternatives and edge cases

- **Regular expressions:** Anchored expressions can encode the same conditions, but `LIKE` is clearer for these fixed literal prefixes, suffixes, and substrings.
- **Filtering with `WHERE`:** Filtering would incorrectly discard samples that match no pattern; those rows must appear with four zero flags.
- **One combined condition:** The four flags are separate outputs, so combining the predicates loses which patterns each sequence satisfies.
- **Stop codon in the middle:** `TAA`, `TAG`, or `TGA` counts only at the end; a leading `%` and no trailing `%` enforce that suffix rule.
- **Start codon in the middle:** `ATG` after the first character does not set `has_start`; `ATG%` has no leading wildcard.
- **Long `G` runs:** `GGGG` and longer runs qualify because each contains the required `GGG` substring.
- **Overlapping motifs:** A sequence such as `ATATAT` contains `ATAT`; only presence matters, not the number of occurrences.
- **Several matches at once:** A sequence can independently receive multiple `1` values, including all four.
- **Input order:** The final `ORDER BY sample_id` is required even when the fixture happens to arrive sorted.
