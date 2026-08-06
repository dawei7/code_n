## Description

Table: `Samples`

```

+----------------+---------+
| Column Name    | Type    | 
+----------------+---------+
| sample_id      | int     |
| dna_sequence   | varchar |
| species        | varchar |
+----------------+---------+
sample_id is the unique key for this table.
Each row contains a DNA sequence represented as a string of characters (A, T, G, C) and the species it was collected from.

```

Biologists are studying basic patterns in DNA sequences. Write a solution to identify `sample_id` with the following patterns:

<ul>
	<li>Sequences that **start** with **ATG** (a common **start codon**)</li>
	<li>Sequences that **end** with either **TAA**, **TAG**, or **TGA** (**stop codons**)</li>
	<li>Sequences containing the motif **ATAT** (a simple repeated pattern)</li>
	<li>Sequences that have **at least** `3` **consecutive** **G** (like **GGG** or **GGGG**)</li>
</ul>

Return *the result table ordered by **sample_id in **ascending** order*.

The result format is in the following example.
