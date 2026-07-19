## General
**Using the fixed three-digit universe**

There are only $450$ even integers from `100` through `998`. Count the available copies of each digit from `0` through `9`, then inspect those candidate numbers in increasing order. This avoids choosing among as many as $100$ input positions.

**Testing one candidate by multiplicity**

Split a candidate into its hundreds, tens, and ones digits and count how many copies of each value it requires. The candidate is constructible exactly when every required count is no greater than the corresponding available count. Starting enumeration at `100` excludes leading zeroes, and stepping by two guarantees an even ones digit.

**Why the output is unique and sorted**

Each three-digit even integer is visited exactly once, so equal input positions cannot duplicate it. Any valid constructible number belongs to the enumerated range and passes its exact multiplicity test, while every accepted candidate can be assigned to that many distinct occurrences in the input. Ascending enumeration directly produces the required order.

## Complexity detail
Counting the $n$ input digits takes $O(n)$ time. Checking the fixed set of $450$ candidates performs constant work independent of $n$, so the total remains $O(n)$. Ten counters and constant-size candidate data use $O(1)$ auxiliary space; the output is also bounded by $450$ integers.

## Alternatives and edge cases
- **Three index loops:** Enumerating ordered triples of distinct positions and deduplicating their numbers is correct but takes $O(n^3)$ time.
- **Backtracking over digit counts:** Choosing hundreds, tens, and even ones values directly is also constant after the $O(n)$ count pass, but needs explicit restoration and duplicate handling.
- **Permutation library:** Materializing all length-three permutations repeats equal-valued arrangements and still scales cubically with input length.
- Zero may appear in the tens or ones position but never in the hundreds position.
- Forming a number such as `222` requires three separate copies of digit `2`.
- If no even digit is available for the ones position, the result is empty.
