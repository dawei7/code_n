## General

**Only consecutive ones need to be compared**

Suppose the indices of ones are:

$$
p_1<p_2<\cdots<p_r.
$$

If every consecutive pair has at least $k$ zeros between it, then any nonconsecutive pair is even farther apart and also satisfies the condition. Therefore, the scan only needs to remember the index of the most recently seen one.

The variable `j` holds that index.

**Initialize so the first one always passes**

```python
j = -inf
```

uses negative infinity as a sentinel meaning no earlier one exists. When the first one appears at finite index `i`, the calculated distance `i - j - 1` is positive infinity, so it cannot be less than finite `k`.

This avoids a separate Boolean flag or special branch for the first one. After the first one, `j` becomes an ordinary integer index.

**Scan every array position once**

```python
for i, x in enumerate(nums):
```

provides the zero-based index and binary value. The condition `if x` is true exactly when `x == 1` under the input guarantee.

Zeros need no direct action. They contribute to the gap automatically through the difference between one indices.

**Derive the number of positions between two ones**

If the previous one is at `j` and the current one at `i`, their index difference is `i-j`. Removing the two endpoint positions leaves:

$$
i-j-1
$$

array places strictly between them.

The code checks:

```python
if i - j - 1 < k:
    return False
```

If fewer than `k` positions separate the ones, the requirement is violated and no later input can repair that pair. Returning immediately is safe.

If the pair passes, `j = i` makes the current one the predecessor for the next one.

**Trace the first example**

For `[1,0,0,0,1,0,0,1]` with `k = 2`:

- The first one is at index 0 and passes the infinity sentinel.
- The next one is at index 4. There are $4-0-1=3$ places between them, at least two.
- The final one is at index 7. There are $7-4-1=2$ places between them, exactly the allowed minimum.

The scan finishes and returns true.

For `[1,0,0,1,0,1]`, the final pair is at indices 3 and 5, leaving $5-3-1=1$ place. Since one is below two, the method returns false.

**Why zero `k` is handled naturally**

When `k = 0`, every pair of distinct one positions has at least zero positions between it. The expression `i-j-1` is never negative for increasing distinct indices, so the comparison with zero never fails. No explicit special case is needed.

Adjacent ones have zero places between them and are valid only when `k = 0`.

**Why the algorithm is correct**

Whenever a one is processed, `j` is the immediately preceding one index because it was updated on every earlier one and never on zero. The code therefore checks the exact number of positions between each consecutive pair.

If it returns false, that pair violates the requirement, so the whole array is invalid. If the scan returns true, every consecutive pair has at least $k$ positions between it. Any nonconsecutive pair spans one or more of these gaps plus intervening one positions and is farther apart, so all pairs satisfy the rule.

**Nonempty array and no-one cases**

The array is nonempty, but it may contain no ones. Then `j` remains negative infinity and no pair exists to violate the requirement, so true is correct.

With exactly one one, there is likewise no pairwise spacing constraint, and the sentinel lets it pass.

**Why storing the previous index is enough**

The index formulation compresses an arbitrarily long zero run into one subtraction. There is no counter to reset incorrectly and no need to inspect earlier one positions after a newer one appears. Once the gap from `j` to `i` has passed, `i` is closer to every future one than `j` is. If a future one is far enough from `i`, it is automatically farther from `j`; if it is too close, the immediately consecutive pair already proves failure. This dominance is why updating `j = i` loses no relevant spacing information.

## Complexity detail

Let $n$ be the array length. The loop visits each element at most once and performs constant work. It can stop early on a violation, while worst-case time is $O(n)$.

Only the previous index `j` and current loop variables are stored, so auxiliary space is $O(1)$, matching the manifest.

## Alternatives and edge cases

- **Count zeros since the last one:** Reset a counter to zero after each one and increment it on zeros. This is equivalent and avoids using infinity.
- **Store every one index:** Compare adjacent stored positions afterward. It is correct but uses $O(n)$ space unnecessarily.
- **Convert to a large integer:** Bit tricks can count zeros between set bits, but conversion is less direct and fixed-width languages may overflow.
- **First one:** It has no predecessor, so it must never cause failure.
- **No ones:** The condition is vacuously true.
- **One one:** There is no pair to compare, so true is returned.
- **Adjacent ones:** They have zero positions between them and pass only for `k = 0`.
- **Exactly `k` zeros:** The strict `< k` test accepts equality.
- **Trailing zeros:** They do not matter because spacing is required only between ones.
- **Early return:** Once one violating pair is found, later values cannot make that already-observed gap larger.
