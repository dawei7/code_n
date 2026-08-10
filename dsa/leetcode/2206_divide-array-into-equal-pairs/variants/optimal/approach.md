## General

Equal pairs can be formed independently for each distinct value. If a value occurs $v$ times, those occurrences can be divided into equal pairs exactly when $v$ is even.

The exact solution counts every value and verifies that every frequency has even parity.

**Why only frequencies matter**

Pair positions are not required to be adjacent, and pairs may be arranged in any order. For one value `x`, any two of its occurrences form a valid pair.

Occurrences of another value cannot help pair a leftover `x` because the two elements in a pair must be equal. Therefore each value class is an independent pairing problem.

**Count all occurrences**

`Counter(nums)` creates one mapping entry per distinct integer. Its value is the number of array positions containing that integer.

Every input position contributes once to exactly one frequency. No information needed for equality pairing is lost by discarding original order.

For `[3,2,3,2,2,2]`, the counter records two threes and four twos.

**Test even parity**

`v % 2 == 0` is true when frequency `v` can be split into groups of size two without a remainder.

The generator applies this test to every Counter value. `all` returns true only if every generated condition is true and stops early at the first odd count.

If all counts are even, value `x` with count $2q$ forms $q$ equal pairs. Doing this for every distinct value uses every element exactly once.

**Why an odd frequency makes pairing impossible**

Suppose some value appears $2q+1$ times. At most $q$ equal pairs can be formed from $2q$ of those occurrences, leaving one unpaired.

It cannot join a different value, so no arrangement of the global pairs can use every element. A single odd frequency is sufficient to return false.

Because the total array length is even, odd frequencies would occur in an even number of value classes, but that fact does not rescue them; each leftover still lacks an equal partner.

**Why even frequencies are sufficient**

For each distinct value with frequency $2q$, arbitrarily partition its occurrences into $q$ groups of two.

These groups are disjoint within the value class, and different classes use disjoint array positions. Their union covers all positions and every group contains equal elements.

Thus the parity condition is both necessary and sufficient, and the boolean returned by `all` exactly answers the problem.

One constructive way to imagine this partition is to list the indices of each value in any order and pair the first with the second, the third with the fourth, and so on. An even list ends exactly after a complete pair. This shows that the frequency test is not merely a numeric shortcut: it corresponds to an explicit valid division of the original positions.

**Why the requested number of pairs appears automatically**

The array contains $2n$ elements. When all elements are partitioned into groups of two, the number of groups is automatically

$$
\frac{2n}{2}=n.
$$

The algorithm does not need to count pairs explicitly after verifying complete coverage.

**Understand short-circuiting**

`all` may stop before reading every Counter frequency if it finds an odd one. That is safe because the final answer is already forced false.

When the result is true, it necessarily inspects every distinct value and confirms all of them.

## Complexity detail

Let $m$ be the number of array elements and $v$ the number of distinct values. Building the Counter takes expected $O(m)$ time, and checking its frequencies takes $O(v)$. Since $v\le m$, total expected time is $O(m)$.

The Counter stores $O(v)$ entries. The generator used by `all` has constant iterator state, so auxiliary space is $O(v)$, matching the manifest.

Under the fixed value bound one through 500, a 501-entry frequency array would make space $O(1)$ with respect to input length, but the exact source uses a Counter.

## Alternatives and edge cases

- **Toggle a hash set:** Add a value on its first unmatched occurrence and remove it on the next. The array is pairable exactly when the final set is empty.
- **Fixed parity array:** Toggle one boolean per value from one through 500, using constant domain space.
- **Sort and compare adjacent pairs:** Sorting groups equal values but costs $O(m\log m)$ time and may mutate the input.
- **XOR all elements:** A zero XOR does not prove every value has even frequency because bit patterns from different values can cancel.
- **One pair:** Two equal elements return true; two different elements produce two odd frequencies and return false.
- **Value appearing four times:** It forms two pairs and passes the parity test.
- **Several odd counts:** `all` stops at the first because one is already enough for impossibility.
- **Even total length:** Guaranteed by the contract, but individual value counts still require checking.
- **Pair order irrelevant:** Frequency grouping can choose any occurrence pairing.
- **Input preservation:** Counter construction reads but does not reorder or mutate `nums`.
- **Expected hash behavior:** Counter operations are expected constant time.
- **No explicit pair construction:** The existence proof is sufficient because only a boolean is returned.
