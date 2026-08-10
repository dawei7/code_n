## General

**Why the answer should be built left to right**

To minimize a decimal string lexicographically, the earliest output position has priority over every later position. At each position, the greedy goal is to place the smallest digit that can be moved there using the remaining adjacent-swap budget.

Moving a digit left by one current position costs one adjacent swap. Once a digit is selected, it is removed from the remaining sequence and appended to the answer. The difficulty is calculating a digit's current position efficiently after earlier removals have shifted the sequence.

The stored solution combines ten queues with a Binary Indexed Tree, also called a Fenwick tree.

**Queues of original positions**

`pos[d]` is a deque containing the one-based original indices of every occurrence of digit `d`, in increasing order. The setup loop reads `num` with indices starting at one and appends each index to the corresponding digit queue.

When considering digit `d`, only `pos[d][0]` matters. Among identical digits, the earliest remaining occurrence is never more expensive to move left than a later one. Choosing a later equal digit cannot improve the output character and would cross the earlier equal digit unnecessarily.

After selecting an occurrence, `popleft` removes it from its digit queue in constant time.

**What the Binary Indexed Tree records**

The tree contains one at every original index already selected for the output and zero elsewhere. `update(j, 1)` marks a selected original position. `query(x)` returns how many selected positions are at most `x`.

The low-bit operation `x & -x` isolates the least significant set bit. Updates move upward through Fenwick responsibility ranges by adding that low bit. Queries move toward zero by subtracting it. Both operations visit $O(\log n)$ indices.

After `i-1` output digits have been selected, `tree.query(n)` equals `i-1`. For a candidate at original index `j`, `tree.query(j)` counts selected original positions no later than `j`. The difference `tree.query(n) - tree.query(j)` counts selected positions originally after `j`.

**Deriving the exact distance formula**

The source computes

`dist = tree.query(n) - tree.query(j) + j - i`.

Substitute the fact that total selected positions equal `i-1`:

$$
dist
=
(i-1-query(j))+j-i
=
j-1-query(j).
$$

Because candidate `j` is not yet selected, `query(j)` counts removed positions originally before it. Thus `j-query(j)` is its one-based rank among remaining digits, and `j-1-query(j)` is the number of remaining digits before it. That is exactly the adjacent swaps needed to bring it to the front of the remaining sequence, which is output position `i`.

The less-simplified stored expression accounts explicitly for earlier selections on both sides of `j` while reaching the same cost.

**Choosing the next digit**

For each output position, the inner loop tries digits from zero through nine. If a digit queue is nonempty, it calculates the cost of its earliest occurrence. The first digit with `dist <= k` is the smallest feasible next character.

The code subtracts the cost, removes that position from its queue, appends the digit, marks the position in the tree, and breaks to advance the output position.

A feasible digit always exists. The first digit in the current remaining sequence costs zero, so when its value is reached in the zero-through-nine scan, it can be selected even if the budget is exhausted.

**Why the greedy choice is globally correct**

Suppose the algorithm chooses digit `a` for the next position. Every smaller digit's earliest occurrence costs more than the remaining budget, and later occurrences of the same smaller digit cost no less. Therefore, no valid sequence of at most the remaining swaps can place a smaller character here.

Any competing answer that begins with a larger digit is lexicographically worse regardless of its suffix. Among answers beginning with `a`, using the earliest occurrence minimizes the swaps spent and leaves at least as much flexibility for the suffix. Repeating this exchange reasoning at every output position proves the completed string is the smallest reachable one.

Leading zeros are allowed in the result, so zero is correctly tried first.

## Complexity detail

Let $n$ be the number of digits. Building the ten position queues takes $O(n)$ time and space.

There are $n$ output positions and at most ten candidate digits are checked at each. A checked nonempty queue performs two Fenwick queries, and a selected digit performs one update. Each costs $O(\log n)$, while ten is constant. Total time is $O(n\log n)$.

The Fenwick array uses $O(n)$ space, all deques together store $n$ positions, and the answer stores $n$ characters. Total auxiliary space is $O(n)$, matching the manifest.

## Alternatives and edge cases

- **Direct list simulation:** Repeatedly locate and remove a feasible digit from a list. Shifting elements can make total time quadratic.
- **Segment tree:** It can count removed positions and update them in $O(\log n)$, matching the asymptotic time with more implementation overhead.
- **Budget large enough to sort fully:** The greedy process chooses digits in ascending order, including duplicates, once every needed move is affordable.
- **Budget too small for a smaller digit:** The algorithm skips it for the current position but may choose it later after intervening digits are removed.
- **Repeated digit:** Only the earliest remaining occurrence is considered because it is the cheapest identical choice.
- **Leading zero output:** It is explicitly permitted, so zero receives normal greedy priority.
- **One digit:** Its cost is zero and the original string is returned.
- **k remains unused:** “At most” k swaps allows the algorithm to stop spending when the string cannot be improved.
- **One-based indexing:** Fenwick operations and stored positions consistently use indices one through n.
- **Required imports:** `defaultdict`, `deque`, and their supporting environment must be available.
