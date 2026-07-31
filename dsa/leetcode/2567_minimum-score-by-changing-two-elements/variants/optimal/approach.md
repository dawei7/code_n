## General

**Make the low score zero.** Because $n \ge 3$, at least one element is not among the two changed positions. Set both changed values equal to any unchanged value. The resulting array contains a duplicate, so its minimum pairwise absolute difference is $0$, the smallest possible low score. The optimization therefore reduces to minimizing the high score, which is simply the final maximum minus the final minimum.

**Only extreme values matter.** Imagine the values in sorted order. Any changed value can be placed inside the range of the unchanged values without expanding that range. Thus the task is equivalent to selecting two original extremes to neutralize. There are only three distributions: change the two largest values, change one smallest and one largest value, or change the two smallest values.

If `smallest` contains the three least values in ascending order and `largest` contains the three greatest values in descending order, the remaining ranges for those choices are respectively:

$$
\begin{aligned}
&\texttt{largest[2]} - \texttt{smallest[0]},\\
&\texttt{largest[1]} - \texttt{smallest[1]},\\
&\texttt{largest[0]} - \texttt{smallest[2]}.
\end{aligned}
$$

Every other choice leaves both a smaller minimum and a larger maximum than one of these boundary choices, so it cannot improve the range. Take the minimum of the three candidates. Fixed-size heaps find the required six boundary values in one pass without sorting the full array.

## Complexity detail

Let $n$ be the length of `nums`. Selecting the three smallest and three largest values with fixed-size heaps takes $O(n \log 3) = O(n)$ time. Each heap and result list has exactly three elements, so the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Sort the complete array:** Sorting makes the three candidate ranges immediately visible and takes $O(n \log n)$ time, but all interior ordering is unnecessary.
- **Enumerate changed pairs:** Trying every pair of positions and recomputing the remaining range is correct but polynomially slower.
- **Exactly three elements:** Either two positions can be changed to match the remaining value, so all three candidate ranges are zero.
- **Duplicate values:** Existing duplicates already make the low score zero; the same three range candidates still determine how much the high score can shrink.
- **All values equal:** Every candidate range is zero, and changing two positions to the same value preserves that score.
- **Changed values:** Once the unchanged range is chosen, place both changed values at any value inside it, preferably equal to an unchanged entry, so neither the low nor high score increases.
