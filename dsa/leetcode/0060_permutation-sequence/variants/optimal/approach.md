## General

**Lexicographic permutations come in equal factorial-sized blocks**

With $n$ distinct ordered digits, fixing the first digit leaves $n-1$ digits that can be arranged in $(n-1)!$ ways. Therefore, the sorted permutation list begins with a block of $(n-1)!$ permutations starting with 1, then an equally sized block starting with 2, and so on.

After the first digit is chosen, the same structure repeats among the remaining digits. Fixing the second position leaves $n-2$ digits and creates blocks of $(n-2)!$. The algorithm uses these nested blocks to jump directly to rank `k` rather than generate `k-1` earlier permutations.

**Keep `k` one-based and subtract skipped blocks**

This source does not change `k` to a zero-based index. At position `i`, `k` is the one-based rank within the permutations sharing the already selected prefix.

For each unused candidate digit in increasing order, `fact` is the number of complete permutations under that choice. If `k > fact`, the requested permutation is not in this candidate's block, so the code subtracts `fact` and considers the next unused digit. If `k <= fact`, the target lies inside the current block; that digit is appended and marked visited.

The strict comparison matters. When `k == fact`, the requested permutation is the final member of the current block, not the first member of the next block. Using `>=` would shift boundary ranks incorrectly.

**How the factorial is computed for each position**

At output position `i`, there will be `n - i - 1` digits after the chosen one. Their number of arrangements is

$$
(n-i-1)!.
$$

The inner multiplication loop starts `fact = 1` and multiplies integers from 1 through `n - i - 1`, producing exactly that factorial. On the final position, the range is empty and `fact` stays 1, correctly representing $0! = 1$.

The source recomputes this factorial at every position rather than carrying it forward. This is simple and remains fast for $n \le 9$, though it contributes to the quadratic running time.

**Visited digits preserve the remaining ordered set**

`vis[j]` says whether digit `j` is already in the output prefix. The candidate loop always runs from 1 through `n`, skipping visited digits. Thus the unvisited candidates are considered in increasing numeric order, matching lexicographic order.

When a block is selected, the source appends `str(j)` and marks the digit. It then breaks so exactly one digit fills the current position. Since `n <= 9`, every digit has one character, and concatenating their string forms produces the expected permutation representation without separators.

**Trace for `n = 4`, `k = 9`**

At the first position, each candidate block has $3! = 6$ permutations. Rank 9 is beyond the block beginning with 1, so subtract 6 and obtain rank 3 inside the remaining blocks. The next unused digit 2 is selected, giving prefix `"2"`.

At the second position, each block has $2! = 2$ permutations. Rank 3 skips the block using 1, leaving rank 1, so digit 3 is selected and the prefix becomes `"23"`.

At the third position, each block has $1! = 1$ permutation. Rank 1 selects the smallest unused digit 1. The final digit is 4, producing `"2314"`.

**The rank invariant**

Before choosing position `i`, `ans` is the fixed prefix of the desired permutation, `vis` marks exactly its digits, and `k` is the one-based rank of the target among all suffix arrangements compatible with that prefix.

Every unused candidate owns exactly `fact` consecutive suffix arrangements. Subtracting a skipped block changes the rank to its correct position among later candidates. Selecting the first block containing `k` fixes the target's next digit without changing its within-block rank. This restores the invariant for the next position.

After $n$ selections, no suffix positions remain. The only compatible arrangement is the constructed string, so it is exactly the original $k$th permutation.

**Why a digit is always selected**

The contract guarantees the original rank lies between 1 and $n!$. Each selection narrows it to a valid rank among the remaining factorial number of arrangements. The total sizes of all candidate blocks equal that count, so one block must contain `k`; the candidate loop always reaches an `else` branch.

## Complexity detail

There are $n$ output positions. Recomputing factorials across all positions uses a triangular number of multiplications, $O(n^2)$. Scanning digits 1 through $n$ at every position is also $O(n^2)$. Joining $n$ one-character pieces is $O(n)$, so total time is $O(n^2)$, matching the manifest.

The visited array and answer-piece list each use $O(n)$ space. Other variables are scalar, so auxiliary space is $O(n)$, matching the manifest. The returned string itself has length $n$.

## Alternatives and edge cases

- **Zero-based factorial digits:** Subtract one from `k`, divide by the current factorial to select a remaining-list index, then use the remainder. This avoids repeated block subtraction but removing a list element still costs linear time.
- **Carry the factorial forward:** Compute `(n-1)!` once and divide by the number of remaining positions after each choice. It removes the repeated factorial loop while keeping overall $O(n^2)$ list selection unless a stronger data structure is used.
- **Generate permutations in order:** Stop at the $k$th leaf. This may take $\Theta(k n)$ work and is infeasible near $n!$.
- **Order-statistics tree:** Select and delete the required unused digit in logarithmic time, reducing selection overhead at the cost of a complex data structure.
- **`k = 1`:** No block is skipped, so digits are selected in increasing order.
- **`k = n!`:** Every position skips as many earlier blocks as possible, producing descending digits.
- **`n = 1`:** `fact` remains $0! = 1$, digit 1 is selected, and `"1"` is returned.
- **Factorial boundary:** The use of `k > fact` keeps `k == fact` in the current block.
- **Input values:** `n` and `k` are integers passed by value; caller state is not mutated.
