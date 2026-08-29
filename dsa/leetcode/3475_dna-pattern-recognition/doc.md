# DNA Pattern Recognition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3475 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/dna-pattern-recognition/) |

## Problem Description

### Goal

The `Samples` table records DNA samples. Each row has a unique sample identifier, a DNA sequence made from the characters `A`, `T`, `G`, and `C`, and the species from which the sample was collected.

For every sample, report four indicators. `has_start` is `1` exactly when the sequence starts with the start codon `ATG`. `has_stop` is `1` exactly when it ends with one of the stop codons `TAA`, `TAG`, or `TGA`. `has_atat` records whether the motif `ATAT` occurs anywhere, and `has_ggg` records whether at least three consecutive `G` characters occur anywhere. An absent pattern contributes `0`; the four checks are independent, so one sequence may satisfy any combination of them.

Return every input row together with these indicators, ordered by `sample_id` in ascending order.

### Function Contract

**Input table**

`Samples`

| Column | Type | Meaning |
|---|---|---|
| `sample_id` | int | Unique sample identifier |
| `dna_sequence` | varchar | DNA sequence containing `A`, `T`, `G`, and `C` |
| `species` | varchar | Species from which the sample was collected |

Let $r$ be the number of rows and let

$$
S = \sum_{x \in \texttt{Samples}} \lvert x.\texttt{dna\_sequence} \rvert.
$$

**Return value**

Return `sample_id`, `dna_sequence`, `species`, `has_start`, `has_stop`, `has_atat`, and `has_ggg` for every sample. Each pattern column contains `1` when its condition holds and `0` otherwise. Sort the result by ascending `sample_id`.

### Examples

#### Example 1

Input table `Samples`:

| sample_id | dna_sequence | species |
|---:|---|---|
| 1 | `ATGCTAGCTAGCTAA` | Human |
| 2 | `GGGTCAATCATC` | Human |
| 3 | `ATATATCGTAGCTA` | Human |
| 4 | `ATGGGGTCATCATAA` | Mouse |
| 5 | `TCAGTCAGTCAG` | Mouse |
| 6 | `ATATCGCGCTAG` | Zebrafish |
| 7 | `CGTATGCGTCGTA` | Zebrafish |

- **Output:** 

| sample_id | dna_sequence | species | has_start | has_stop | has_atat | has_ggg |
|---:|---|---|---:|---:|---:|---:|
| 1 | `ATGCTAGCTAGCTAA` | Human | 1 | 1 | 0 | 0 |
| 2 | `GGGTCAATCATC` | Human | 0 | 0 | 0 | 1 |
| 3 | `ATATATCGTAGCTA` | Human | 0 | 0 | 1 | 0 |
| 4 | `ATGGGGTCATCATAA` | Mouse | 1 | 1 | 0 | 1 |
| 5 | `TCAGTCAGTCAG` | Mouse | 0 | 0 | 0 | 0 |
| 6 | `ATATCGCGCTAG` | Zebrafish | 0 | 1 | 1 | 0 |
| 7 | `CGTATGCGTCGTA` | Zebrafish | 0 | 0 | 0 | 0 |

For example, sample 4 both begins with `ATG`, ends with `TAA`, and contains the run `GGGG`; sample 5 satisfies none of the four conditions.
