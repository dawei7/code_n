## General

**Use the promise about the original set**

Before the error, the collection contains every integer from one through `n` exactly once. After the error, one value appears twice and one different value disappears. This guarantee is much stronger than merely saying that the array contains arbitrary repeated numbers. It lets us recover both answers by comparing three sums.

The exact solution computes:

- `s1`: the expected sum of all integers from one through `n`;
- `s2`: the sum of the distinct values that actually occur;
- `s`: the sum of every array element, including the second copy of the duplicate.

Each difference isolates one unknown.

**Compute the expected perfect-set sum**

The well-known arithmetic-series formula gives:

`s1 = n * (n + 1) // 2`.

The implementation writes the factors as `(1 + n) * n // 2`, which is the same calculation. This is the sum the array would have if no replacement error had occurred.

Integer division is exact here because one of two consecutive integers `n` and `n + 1` is even. Python integers also grow as needed, so the multiplication cannot overflow. In a fixed-width language, the factors may need a wider type or division before multiplication.

**Why the set sum removes exactly the extra copy**

Calling `set(nums)` keeps one occurrence of every value and discards repeated occurrences. Under the problem guarantee, every number except the missing one occurs at least once, and the duplicate is the only number occurring more than once. Therefore, the set contains:

`{1, 2, ..., n}` with only the missing value absent.

The duplicate still appears once in this set, which is correct because it belonged to the original perfect set. Only its erroneous second occurrence is removed.

If the missing value is `m` and the duplicate is `d`, then the distinct-value sum is:

`s2 = s1 - m`.

Rearranging immediately gives `m = s1 - s2`. That is why the second returned component is `s1 - s2`.

**Why the ordinary array sum reveals the duplicate**

The full array contains the same distinct values represented by `s2` plus one extra copy of `d`. Thus:

`s = s2 + d`.

Rearranging gives `d = s - s2`. That is the first returned component, matching the required order: duplicate first, missing second.

Another way to view the full sum is `s = s1 - m + d`, but this equation alone contains two unknowns. The set sum supplies the second independent fact needed to separate them.

**Walk through the first example**

For `nums = [1, 2, 2, 4]`, the length is four:

- `s1 = 1 + 2 + 3 + 4 = 10`;
- `set(nums) = {1, 2, 4}`, so `s2 = 7`;
- the full array sum is `s = 9`.

The duplicate is `s - s2 = 9 - 7 = 2`. The missing value is `s1 - s2 = 10 - 7 = 3`. The returned array is therefore `[2, 3]`.

Notice how the two differences ask different questions. Full sum minus distinct sum asks, “Which value was counted one extra time?” Expected sum minus distinct sum asks, “Which expected value never appeared?”

**Why the calculation is correct**

Let `E` be the perfect set of values from one through `n`. Let `m` be the unique missing value and `d` the unique duplicated value. The set of values occurring in `nums` is exactly `E` without `m`. Therefore, its sum is the expected sum minus `m`, and `s1 - s2` must equal `m`.

The array contains exactly the elements of that distinct set plus one additional `d`. Therefore, its sum is the distinct sum plus `d`, and `s - s2` must equal `d`.

These arguments use every source guarantee: the values are within one through `n`, exactly one is missing, and exactly one is duplicated. Under those conditions, both differences are uniquely determined and the method returns the required ordered pair.

**Why no explicit search is needed**

The code never loops over every candidate from one through `n` to test its frequency. The aggregate sums encode the needed information. Python's built-in `sum` and set construction still traverse the input, but each traversal is linear and direct.

The input list itself is not modified. This can be desirable when callers may need the original data afterward, though the set used to preserve nonmutation has a memory cost.

## Complexity detail

Let `n` be the length of `nums`.

Computing the arithmetic-series sum takes constant time. Constructing `set(nums)` examines `n` elements, and summing its at most `n` distinct elements takes linear time. Computing `sum(nums)` also examines `n` elements. These linear passes occur sequentially, so total running time is `O(n)` under expected constant-time hash insertion.

The exact Python source creates a set containing `n - 1` distinct integers. Consequently, its auxiliary-space complexity is `O(n)`. The manifest advertises `O(1)` space, but that bound does not describe this literal set-based implementation. A sign-marking or XOR-based implementation can achieve constant auxiliary space, with different tradeoffs described below.

The expression `sum(set(nums))` creates the set temporarily, keeps it alive while summing it, and then permits it to be released. Its peak size is still linear even though it is not assigned to a named variable.

Python integer arithmetic prevents overflow for the sums. Under a fixed-width arithmetic model, the expected and actual sums can reach quadratic magnitude in `n`, so a sufficiently wide integer type is required.

## Alternatives and edge cases

- **In-place sign marking:** Use each value as an index and negate the element at that position. Encountering an already negative slot identifies the duplicate, and the one positive slot later identifies the missing value. This gives `O(n)` time and `O(1)` auxiliary space, but mutates `nums` and requires careful absolute-value handling.

- **XOR partitioning:** XOR all array values with one through `n` to obtain the XOR of the two unknowns, split values by a differing bit, and recover two candidates. A final membership check distinguishes duplicate from missing. It achieves `O(n)` time and `O(1)` space without arithmetic overflow, but is less intuitive.

- **Sum and sum-of-squares equations:** The differences of sums and squared sums form two equations for the missing and duplicate values. This uses constant space but is more error-prone and can overflow fixed-width types quickly.

- **Frequency array or hash map:** Counting occurrences makes the answer explicit and remains `O(n)` time, but uses `O(n)` storage. The exact set method stores only membership, then extracts both answers from sums.

- **Sorting:** Adjacent equal values reveal the duplicate, while a gap reveals the missing value. It costs `O(n log n)` time and may mutate the input.

- **Missing value is one:** The expected sum still exceeds the distinct sum by one. No boundary-specific initialization is required.

- **Missing value is `n`:** The same formula detects it even though there is no internal gap in a sorted order.

- **Duplicate appears next to itself or far apart:** Set construction ignores positions, so adjacency has no effect.

- **Smallest valid array:** For `[1, 1]`, the expected sum is three, the distinct sum is one, and the full sum is two. The method returns `[1, 2]`.

- **Input mutation:** The exact implementation leaves `nums` unchanged. Do not claim the same property for the sign-marking alternative unless all signs are restored afterward.

- **Invalid data with multiple errors:** The two differences would still produce numbers, but they would not necessarily identify all problems. Correctness depends on the exact one-duplicate, one-missing guarantee.

- **Hash behavior:** Set operations are expected `O(1)` per element in Python. Adversarial collision behavior can weaken that theoretical assumption, though integer hashing is well behaved for this constrained input.
