## General

**Only increments are allowed, so choose the smallest legal value at every position.** Let the final adjusted array be `a`. At index `i`, strict increase requires `a[i] > a[i - 1]`. Because values are integers, the smallest value satisfying that relationship is `a[i - 1] + 1`. The value also cannot be below the original `nums[i]`, since the allowed operation increments but never decrements. Therefore the smallest feasible final value is

`a[i] = max(nums[i], a[i - 1] + 1)`.

This one recurrence contains the entire greedy strategy. If the original value is already large enough, keep it unchanged. Otherwise, raise it only to one more than the preceding adjusted value. Raising it any further would spend extra operations immediately and would also make the requirement on later elements harder, never easier.

**What `mx` means.** The implementation does not build a separate adjusted array. After processing a value, `mx` is the final adjusted value chosen for that position. Before processing the next value `v`, `mx + 1` is therefore the minimum integer that would be strictly greater than its adjusted predecessor.

The code initializes `mx = 0`. This acts as a conceptual value just before index zero. Since the constraints guarantee every `nums[i]` is at least one, the first value always satisfies `v >= mx + 1`. It is left unchanged, exactly as it should be: there is no predecessor constraint on the first real element. If negative or zero inputs were allowed, this particular initialization would need separate first-element handling, but those values are outside the stated domain.

**Count only the forced increments.** For each original value `v`, the expression

`max(0, mx + 1 - v)`

computes the number of increments needed at this index. If `v` already exceeds `mx`, then `mx + 1 - v` is zero or negative and no operation is needed. Otherwise, the difference is exactly how far `v` must be raised to reach `mx + 1`. The code adds this amount to `ans`.

Next it updates the adjusted value with

`mx = max(mx + 1, v)`.

These two lines describe the same decision from two viewpoints. The first records its cost; the second records its resulting value. If an increment was necessary, the new `mx` is `mx + 1` from the previous iteration. If no increment was necessary, the new `mx` is the untouched `v`.

**A detailed trace.** Consider `nums = [1, 5, 2, 4, 1]`.

- For one, the conceptual threshold is one. No increment is needed, `ans` remains zero, and `mx` becomes one.
- For five, the threshold is two. Five is already larger, so the cost stays zero and `mx` becomes five.
- For two, the threshold is six. Four increments are forced, changing this position to six. Now `ans = 4` and `mx = 6`.
- For four, the threshold is seven. Three more increments change it to seven. Now `ans = 7` and `mx = 7`.
- For one, the threshold is eight. Seven more increments change it to eight. The final total is fourteen.

The implicitly constructed result is `[1, 5, 6, 7, 8]`. Every adjacent pair is strictly increasing, and every change is an allowed increment.

For `[1, 1, 1]`, the recurrence keeps the first one, raises the second to two for one operation, and raises the third to three for two more operations. The total is three. The sample describes those increments in a different order, but operation order does not affect the total required increase at each index.

**Why a local choice gives a global optimum.** The crucial asymmetry is that earlier values cannot be decreased. Once the optimal adjusted prefix ends at value `mx`, the current element has a hard lower bound of `mx + 1`. No choices made in the future can reduce that bound. Therefore every valid solution must spend at least `max(0, mx + 1 - v)` operations on the current value.

The algorithm spends exactly that lower bound and chooses the smallest feasible current result. This also gives the future the easiest possible predecessor: any larger choice would force every later adjusted value to be at least as large, potentially adding more operations. Thus the greedy choice is both locally unavoidable and globally safest.

This can be stated as a prefix property. After each iteration, `ans` is the minimum number of increments needed to make the processed prefix strictly increasing, and `mx` is the smallest possible final value among all minimum-cost ways to do so. The property is true for the first element, which remains unchanged. For the next element, any valid extension must reach at least `mx + 1` and at least `v`. Choosing their maximum pays the least possible added cost and produces the least possible new endpoint. By induction, the property holds for the whole array, so the returned total is minimal.

**Why modifying earlier elements cannot help.** When a current value is too small, it may be tempting to revisit its predecessor. The only allowed change to that predecessor is another increment, which raises the threshold for the current value and makes the situation worse. Decrementing the predecessor could help, but decrement operations are forbidden. This is why a left-to-right pass can finalize each position permanently.

**The input array remains unchanged.** Although the problem describes increment operations, the implementation only calculates how many would be necessary. It stores the current adjusted endpoint in `mx` and never writes into `nums`. This is enough because future decisions depend only on the previous adjusted value, not on the entire adjusted prefix.

## Complexity detail

Let `n = nums.length`. The loop visits each value exactly once. Every iteration performs a constant number of arithmetic operations and comparisons, so the running time is `O(n)`.

The implementation uses two scalar integers, `ans` and `mx`, regardless of input length. It does not copy or mutate the array and uses no recursion, so its auxiliary space is `O(1)`. Python integers can grow to hold the total automatically; in a fixed-width language, the maximum possible accumulated increment count should be checked when selecting the numeric type.

## Alternatives and edge cases

- **Mutate the array in place:** Setting `nums[i] = max(nums[i], nums[i - 1] + 1)` and adding the difference expresses the same greedy recurrence. It remains `O(n)` time and `O(1)` auxiliary space but changes the caller’s input.
- **Construct a separate adjusted array:** This can make the resulting sequence visible for teaching or reconstruction, but it uses `O(n)` additional space even though only the last adjusted value affects the next decision.
- **Repeated one-by-one simulation:** Literally incrementing a value until it clears its predecessor produces the same answer but may take time proportional to the answer, which can be far larger than `n`. Computing the difference performs all forced increments at once.
- **Already strictly increasing:** Every difference term is zero, each value becomes the new `mx` unchanged, and the answer is zero.
- **Single element:** The first value is unconstrained by a predecessor, so it is unchanged and the returned total is zero.
- **All values equal:** The final values become consecutive integers beginning at the original first value. Later positions require progressively more increments.
- **A large value followed by small values:** The large value must remain because decrements are unavailable; it raises the minimum threshold for every following position, which the recurrence captures.
- **Large gaps:** If `v > mx + 1`, the algorithm keeps the gap. Reducing `v` would be illegal, and increasing it would waste operations.
- **Strict versus non-decreasing:** The required threshold is `mx + 1`, not `mx`. Using `mx` would permit equal adjacent values and solve a different problem.
- **Positive-input assumption:** Initializing `mx` to zero is correct because every input value is at least one. A generalized version allowing arbitrary integers should initialize from the first array value instead.
- **No integer overflow in Python:** `ans` and `mx` expand as needed. Implementations with bounded integers should use a sufficiently wide type for the accumulated answer.
