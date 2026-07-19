## General
**Measure the relative cost of city A:** For each person, `aCost - bCost` is the change in total cost if that person is sent to A instead of B. A smaller difference means choosing A is more favorable relative to choosing B.

**Choose exactly half by that difference:** Sort the people in ascending order of `aCost - bCost`. Send the first $N/2$ people to A and the remaining people to B. Summing the corresponding entries produces a balanced schedule by construction.

**Why this greedy split is optimal:** Suppose a proposed balanced assignment sends person `i` to B and person `j` to A even though `i` has a smaller difference. Swapping their cities changes the cost by
$$
(\texttt{aCost}_i-\texttt{bCost}_i)-(\texttt{aCost}_j-\texttt{bCost}_j) \le 0.
$$
The swap preserves the city counts and never increases the total. Repeating it removes every inversion, yielding exactly the sorted split, so no balanced assignment can be cheaper.

## Complexity detail
Sorting $N$ cost pairs takes $O(N\log N)$ time. A sorted copy stores $N$ references and uses $O(N)$ auxiliary space; the two summations take $O(N)$ additional time.

## Alternatives and edge cases
- **Start with everyone in city B:** Add every B cost, then apply the $N/2$ smallest values of `aCost - bCost`. This is the same greedy argument written as savings.
- **Dynamic programming by people and A slots:** Track the minimum cost after each prefix and number sent to A. It takes $O(N^2)$ time and $O(N)$ space, which is unnecessary for two cities.
- **Quadratic selection:** Repeatedly search for the next smallest difference. It remains correct but takes $O(N^2)$ time.
- **Equal differences:** Tied people are interchangeable because swapping them changes the total by zero.
- **Everyone prefers one city:** Exactly half must still go to each city; absolute preference does not override the balance constraint.
- **Minimum input:** With two people, compare the only two balanced assignments.
