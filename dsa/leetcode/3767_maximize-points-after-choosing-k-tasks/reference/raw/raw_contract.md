## Function Contract

**Inputs**

- `technique1`: Points earned by using technique 1 on each task.
- `technique2`: Points earned by using technique 2 on the corresponding tasks.
- `k`: The inclusive lower bound on how many tasks must use technique 1.

The arrays have the same nonzero length. Choices are independent across indices except for the global technique-1 quota. Let $N$ be their common length and let $K = \texttt{k}$.

**Return value**

Return the greatest possible sum of the selected point values. More than `k` tasks may—and should—use technique 1 whenever doing so increases the total.
