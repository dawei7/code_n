## General

Let `k` be the total number of ones in the array. Any final group containing all ones must occupy exactly `k` consecutive circular positions: there are only `k` ones available, so a larger block is unnecessary and a smaller block cannot contain them all.

This turns the problem into choosing the best circular window of length `k`.

**Relate a window’s contents to its swap cost**

Suppose a particular length-$k$ window already contains $c$ ones. Its other $k-c$ positions contain zeros. Because the entire array contains $k$ ones, exactly $k-c$ ones lie outside this window.

Each zero inside can be swapped with one of those outside ones. After $k-c$ swaps, all $k$ positions in the window are ones. Fewer swaps cannot work because every zero currently inside must be replaced. Therefore the precise cost of choosing that window is

$$
k-c.
$$

Minimizing swaps is consequently equivalent to maximizing the number of ones already present in a circular length-$k$ window.

**Initialize the first candidate**

The code computes `k = nums.count(1)`. It then obtains the one count in the ordinary prefix window covering indexes $0$ through $k-1$:

`mx = cnt = sum(nums[:k])`

Here, `cnt` is the number of ones in the current window, while `mx` is the greatest window count seen so far. Since values are binary, summing a slice counts its ones.

The slice is used only once for initialization. Its length is at most $n$, after which the window is updated in constant time per movement.

**Slide across the circular boundary**

The loop `for i in range(k, n + k)` performs $n$ window movements. At each step, index `i` is the new rightmost position entering the window. It may be beyond the physical end of the list, so `i % n` wraps it back to the corresponding circular index.

The position leaving the window is $i-k$. The source writes it as `(i - k + n) % n`. Adding $n$ before taking the remainder keeps the intention explicit and produces the same circular index. The update first adds `nums[i % n]` and then subtracts `nums[(i - k + n) % n]`.

Adding the entrant and removing the leaver preserves a length-$k$ window and changes its count in $O(1)$ time. Then `mx = max(mx, cnt)` retains the best concentration of ones.

Starting from window $0$ through $k-1$, the first update produces the window starting at index $1$. Subsequent updates consider starts $2,3,\ldots,n-1$, including every window that crosses from the array’s end to its beginning. The final movement reaches the start-$0$ window again. That duplicate is harmless; all distinct circular starting positions have already been considered.

For `[1,1,0,0,1]`, $k=3$. The circular window containing indexes $4,0,1$ contains three ones, even though it is split across the displayed ends. Modular indexing discovers that window and sets `mx` to three, giving zero swaps.

**Convert the best window back to swaps**

Once every circular window has been examined, `mx` is the maximum number of ones that can already lie in the selected group. Its number of zeros is `k - mx`, so the final result is returned by `k - mx`.

This value is achievable by swapping each internal zero with an external one. It is also a lower bound for that chosen window because each internal zero must change. Since `mx` was maximal over every possible group location, no other window requires fewer swaps.

**Why arbitrary swaps make the count sufficient**

A swap may exchange any two distinct positions; the positions do not have to be adjacent. Therefore moving an outside one into an inside zero costs exactly one operation, regardless of their distance around the circle. If only adjacent swaps were allowed, distances and ordering would matter, and this window-count formula would not solve the problem.

## Complexity detail

Let $n$ be the array length. `nums.count(1)` scans $n$ entries. Creating and summing `nums[:k]` touches $k \le n$ entries. The sliding loop performs exactly $n$ iterations, each with constant-time arithmetic, indexing, and comparisons. Total time is $O(n)$.

The slice `nums[:k]` is a newly allocated Python list of up to $n$ elements. Therefore the exact implementation’s peak auxiliary space is $O(k)$, which is $O(n)$ in the worst case, despite the manifest’s $O(1)$ claim. All sliding-window state after initialization is constant-sized, and the slice becomes disposable after `sum` finishes, but peak-space analysis still counts that temporary allocation.

A constant-space implementation could compute the initial count with an index loop or an iterator expression instead of slicing. That would preserve the algorithm and $O(n)$ time, but it is not the exact stored source.

## Alternatives and edge cases

- **Constant-space initialization:** Replace `sum(nums[:k])` with a loop over the first `k` indexes or an iterator-based sum. The sliding logic remains the same while peak auxiliary space becomes $O(1)$.
- **Duplicate the array:** Sliding over `nums + nums` makes circular windows visually simple, but creates an $O(n)$ copied list. The exact solution uses modular indexes and avoids that full duplication.
- **Recount every window:** Summing each length-$k$ window independently costs $O(nk)$ in the worst case. Removing one value and adding one value reduces the total to linear time.
- **Try actual swaps greedily:** Choosing which outside one to swap is irrelevant because swaps may use arbitrary positions. Counting internal zeros proves both the cost and feasibility.
- **No ones:** Then `k = 0`, the initial slice is empty, and each loop update adds and subtracts the same element. `mx` remains zero and the method returns zero, as there is nothing to group.
- **Exactly one one:** Every circular window has length one. A window at that one already contains it, so `mx = 1` and the answer is zero.
- **All ones:** Here `k = n`. Every length-$n$ circular window is the entire array, `mx = n`, and no swaps are required.
- **Array length one:** Whether the sole value is zero or one, the answer is zero. The modulo divisor `n` remains valid because $n \ge 1$.
- **Group crosses the boundary:** Modular indexing includes windows whose suffix lies at the end and whose remainder lies at the beginning, which is essential for Example 3.
- **Tied best windows:** Only the maximum count matters; the method need not remember which window achieved it.
- **Duplicate final window:** The $n$ movements revisit the initial circular window. This affects neither correctness nor the $O(n)$ bound.
- **Arbitrary-position swap definition:** The formula `k - cnt` would understate the cost if only adjacent exchanges were allowed. It is correct specifically because any two distinct positions may be swapped.
- **Input preservation:** The method reads `nums` and creates one slice but never assigns into the original list.
