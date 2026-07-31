## General

An alternating subarray is determined by the directions of its adjacent comparisons. Write **up** for `<` and **down** for `>`. Equality cannot extend a run. Once a comparison has one direction, the next comparison must have the opposite direction.

For every index `i`, keep four directional lengths:

- `left_up[i]` and `left_down[i]` are the maximum alternating lengths ending at `i` whose final comparison is respectively up or down.
- `right_up[i]` and `right_down[i]` are the maximum alternating lengths starting at `i` whose first comparison is respectively up or down.

Initialize every state to `1`. Besides representing a one-element alternating subarray, that neutral value lets either direction start a new run. During the left-to-right pass, if `nums[i - 1] < nums[i]`, then an up comparison may extend only a run ending down, so `left_up[i] = left_down[i - 1] + 1`. The greater-than case is symmetric. Equal values leave both states at `1`. A right-to-left pass constructs the starting states by the same reasoning.

The maximum left state already covers every solution that removes nothing. Removing the first or last element cannot improve on this maximum: any subarray available after such a boundary removal was already a subarray of the original array. It therefore remains to examine every interior removed index `r`.

Deleting `nums[r]` creates one new bridge comparison between `nums[r - 1]` and `nums[r + 1]`:

- If `nums[r - 1] < nums[r + 1]`, the bridge is up. Any comparison immediately before or after it must be down, so the best joined length is `left_down[r - 1] + right_down[r + 1]`.
- If `nums[r - 1] > nums[r + 1]`, the bridge is down, giving `left_up[r - 1] + right_up[r + 1]`.
- If the two bridge values are equal, no alternating subarray can cross the removed position.

Each directional state is the longest valid portion with the exact direction needed beside the bridge; states of length `1` correctly cover a missing comparison at either boundary. Thus each candidate is the longest alternating subarray crossing that particular deletion. Taking the maximum over no deletion and every interior deletion covers every permitted choice.

## Complexity detail

The three passes each examine $N$ positions a constant number of times, so the running time is $O(N)$. The four directional arrays use $O(N)$ auxiliary space.

The benchmark defines size as $N$, the number of array values. The accepted implementation and an independent sign-run implementation both scale linearly, while the slower control tries every possible removal and rescans the resulting array, taking $O(N^2)$ time.

## Alternatives and edge cases

- **Try every removal and rescan:** Building or logically skipping each possible removed index and then finding the best alternating run is straightforward and correct, but it takes $O(N^2)$ time.
- **Comparison-sign runs:** Prefix and suffix lengths over the sign sequence provide an equivalent $O(N)$ formulation, as long as the bridge sign is checked against both neighboring signs.
- **No removal:** An already alternating array may be the optimum, so the maximum ordinary run must be included explicitly.
- **Equal adjacent values:** Equality is neither up nor down and restarts every directional run.
- **Equal bridge values:** If `nums[r - 1] == nums[r + 1]`, deleting `nums[r]` cannot join the two sides into one alternating subarray.
- **Repeated bridge direction:** A strict bridge still cannot join a side whose adjacent comparison has the same direction; that side contributes only its boundary element.
- **Boundary removal:** Removing index `0` or `N - 1` creates no bridge and cannot reveal a subarray that was not already selectable without removal.
- **Two-element input:** Unequal values give length `2`; equal values give length `1`.
