## General
**Aggregate by table and food.** Scan every order once. Insert its food name into a set and increment a nested counter keyed first by the numeric table number and then by the food name. The customer name is irrelevant to the aggregation.

Sort the distinct foods lexicographically to form the header. Sort the counter's table keys numerically, not as strings, so table `"10"` follows `"5"`. For each table, emit its original decimal representation followed by the count for every sorted food, using zero when that pair never occurred.

Every order increments exactly one cell, so the counter contains the required multiplicities. Sorting the two independent dimensions establishes the mandated row and column order, and visiting every header food for every table fills all absent combinations with zero. Therefore the emitted matrix matches the display-table definition.

## Complexity detail
Reading the $N$ orders takes $O(N)$ time. Sorting the $F$ foods and $T$ tables costs $O(F\log F + T\log T)$, and materializing the table costs $O(TF)$. The counters store at most $N$ populated pairs, while the returned matrix contains $O(TF)$ cells, giving $O(N+TF)$ total space including output.

## Alternatives and edge cases
- **Rescan all orders per cell:** For each table-food pair, count matching records directly. It is correct but can take $O(NTF)$ time.
- **Sort orders first:** Sorting by table and food can support a grouped scan, but a hash counter is simpler and still needs the final full matrix.
- **Numeric table order:** Convert table strings to integers for sorting; lexicographical order would place `"10"` before `"2"`.
- **Missing pair:** Emit `"0"`, not an absent cell or numeric zero.
- **Repeated identical orders:** Count every record independently, even when customer, table, and food all match.
- **Single order:** The result still contains a two-cell header and one table row.
