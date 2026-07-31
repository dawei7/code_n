## General

**Choose a hub before counting the team**

Fix employee $i$ as the team member who must interact with everyone else. Another interval $[s_j,e_j]$ overlaps the hub interval $[s_i,e_i]$ exactly when

$$
s_j \le e_i
\quad\text{and}\quad
e_j \ge s_i.
$$

Every employee satisfying both inequalities can be included: the definition requires interaction with the hub, not interaction among every pair of teammates. The largest valid team centered at $i$ therefore contains all intervals overlapping $i$, including the hub itself.

**Count overlaps from independently sorted endpoints**

Sort all start times and all end times into two separate arrays. For hub $i$:

- `bisect_right(sorted_starts, endTime[i])` counts intervals beginning no later than the hub ends;
- `bisect_left(sorted_ends, startTime[i])` counts intervals ending strictly before the hub starts.

Every interval in the second group is also in the first count because its start is smaller than its end, which is smaller than the hub's start and hence no greater than the hub's end. Subtracting the second count from the first leaves exactly the intervals satisfying both overlap inequalities.

Using a right insertion boundary for starts includes `startTime[j] == endTime[i]`. Using a left insertion boundary for ends excludes only `endTime[j] < startTime[i]`, retaining `endTime[j] == startTime[i]`. These choices preserve the source's closed-interval rule.

Evaluate this count for every original paired interval and return the maximum. For any chosen hub, the computed employees form a valid team, so every candidate count is attainable. Conversely, every valid team has a hub, and all of its members appear in that hub's computed overlap set; its size cannot exceed the corresponding count. The maximum computed value is therefore exactly optimal.

## Complexity detail

Let $n$ be the number of employees. Sorting the two endpoint arrays takes $O(n\log n)$ time. Two binary searches for each of $n$ hubs add another $O(n\log n)$ time, so the total is $O(n\log n)$. The sorted copies use $O(n)$ auxiliary space.

The benchmark defines size as $n$ and uses disjoint intervals in a deliberately permuted order. The accepted method sorts and performs two searches per hub. A correct method that compares every possible hub with every employee performs $\Theta(n^2)$ overlap checks on all three tiers.

## Alternatives and edge cases

- **Pairwise overlap scan:** Testing all $n$ intervals for each candidate hub directly implements the definition but takes $O(n^2)$ time.
- **Event sweep:** An offline sweep can derive each interval's overlap count in $O(n\log n)$ time as well, but the two sorted endpoint lists express the inclusive boundaries more directly.
- **Maximum simultaneous attendance:** Counting the largest set present at one common time solves a stricter problem. A long hub interval may overlap several mutually disjoint teammates, so a valid team need not have a universal shared time point.
- **Endpoint contact:** Closed intervals overlap when one's end equals another's start. Strict binary-search boundaries would incorrectly discard these teams.
- **Self membership:** Each hub overlaps its own interval and belongs to its team, so every answer is at least one.
- **Duplicate intervals:** Repeated starts, ends, or entire intervals represent distinct employees and must each contribute to the count.
- **Preserve pairing:** The independently sorted arrays are used only for aggregate counts. Candidate hubs must still iterate over the original paired `startTime[i]` and `endTime[i]` values.
- **Input order:** No ordering is guaranteed, and permuting employees cannot change the answer.
