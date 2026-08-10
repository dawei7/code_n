## General

**Only total apple count matters.** Apples from one pack may be split across boxes, so pack boundaries impose no restriction. The required capacity is simply:

$$
S=\sum_i\texttt{apple}[i].
$$

A selected set of boxes is feasible exactly when its total capacity is at least $S$.

**Choose largest capacities first.** `capacity.sort(reverse=True)` orders boxes from most to least useful. The loop subtracts capacities from remaining apple count `s`. The first prefix whose cumulative capacity reaches the total gives the returned number of boxes.

For example, total apples 6 and capacities 5, 4, 3, 2, 1 use 5 first, leaving one, then 4, reaching or exceeding capacity with two boxes.

**Why largest-first minimizes the count.** For any fixed number $r$, the sum of the $r$ largest capacities is at least the capacity sum of every other $r$-box selection. Therefore:

- if the largest $r$ boxes cannot hold all apples, no selection of $r$ boxes can;
- when the largest $r$ boxes first can hold them, a feasible $r$-box selection exists.

The first successful prefix is thus both necessary and sufficient, proving minimality.

This is an exchange argument as well: if a selected set contains a smaller box while a larger unselected box exists, swapping them cannot reduce total capacity. Repeating exchanges transforms an optimal set into the sorted prefix.

**Subtracting remaining demand is equivalent to accumulating capacity.** The source initializes `s = sum(apple)`, then performs `s -= c`. Condition `s <= 0` means selected capacity is at least original apple total. Overshooting is allowed because unused box space is harmless.

**Why there is no fallback return.** The reference guarantees redistribution is possible using available boxes. Therefore some prefix—at worst all boxes—makes `s <= 0` and returns. Without that guarantee, the Python method could reach the end and implicitly return `None`.

**Input mutation.** Sorting occurs in place, so the caller's `capacity` list is permanently rearranged descending. `apple` is only read.

**A trace of the second example.** Apple total is 15. Sorted capacities are 7, 4, 2, 2. Remaining demand becomes 8, 4, 2, then 0, so all four boxes are required. The three largest total only 13, proving no three-box choice works.

**No assignment construction is needed.** Because individual apples may be redistributed arbitrarily, aggregate capacity proves a packing exists. There are no indivisible packs that could fail to fit despite enough total space.

## Complexity detail

Let $N$ be pack count and $M$ box count. Summing apples costs $O(N)$. Sorting capacities costs $O(M\log M)$, and the prefix scan costs $O(M)$. Total time is $O(N+M\log M)$.

Python's in-place sort may use $O(M)$ temporary workspace in the worst case. Other variables are constant-sized. The manifest's $O(M)$ space allowance accurately covers sorting workspace.

The output is one integer.

## Alternatives and edge cases

- **Max-heap of capacities:** Heapify and pop largest boxes until enough capacity. It reaches $O(N+M+R\log M)$ but sorting is simpler when only one query is needed.
- **Try all box subsets:** It is exponential and unnecessary because only capacity sums matter.
- **Sort ascending and scan backward:** It is equivalent but slightly less direct than descending order.
- **One box holds everything:** The first subtraction reaches nonpositive and returns one.
- **Exact total capacity:** Equality is sufficient, so `s <= 0` correctly stops at zero.
- **Capacity overshoot:** Extra unused space is allowed.
- **Need every box:** The guarantee ensures the final prefix succeeds and returns $M$.
- **Splittable packs:** This is essential to reducing the problem to total capacity.
- **Impossible input outside contract:** The source would implicitly return `None`.
- **Input mutation:** `capacity` ends sorted descending after the method returns.
- **Why pack count does not affect box count directly:** Ten small packs and one large pack with the same total apples are interchangeable because every pack may be split. Only their summed demand enters the algorithm.
- **Largest-prefix dominance:** For each $r$, no other $r$ boxes have greater total capacity than the descending prefix. This establishes impossibility for every smaller count, not just feasibility of the returned count.
- **Positive capacities:** Every selected box strictly reduces remaining demand, so progress is monotone and the first success cannot later be invalidated.
- **Return uses one-based enumeration:** `enumerate(capacity,1)` makes `i` equal the number of boxes consumed, avoiding a separate `i+1` conversion.
- **Sorting tie capacities:** Equal-size boxes may exchange order without changing prefix sums or the returned count.
- **No partial box restriction:** Selecting a box does not require filling it completely. The final chosen box may have unused space after `s` becomes negative.
- **Minimum one box:** Apple counts are positive, so zero boxes can never satisfy the demand; one-based scanning begins at the smallest meaningful answer.
- **Apple array remains unchanged:** Only `sum(apple)` is read, so pack counts and order remain available to the caller after execution.
- **Box identities:** Only capacity affects feasibility, so the method need not retain original box indices.
