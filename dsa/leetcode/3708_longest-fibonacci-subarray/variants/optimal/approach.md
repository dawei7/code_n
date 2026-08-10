## General

The condition is local: once two preceding values are known, the current value either continues the Fibonacci relation or breaks it. Because the requested sequence must be a **subarray**, only one current contiguous run needs to be tracked.

The exact source uses:

- `f` for the length of the longest Fibonacci subarray ending at the current position;
- `ans` for the longest such length seen anywhere.

Both begin at two:

`ans = f = 2`.

This initialization follows the note that every length-one or length-two subarray is automatically Fibonacci. The input length is at least three, so a length-two baseline always exists.

**Testing whether the current value extends the run**

Starting at index two, the source checks:

`nums[i] == nums[i - 1] + nums[i - 2]`.

If this equality holds, the current element satisfies the required recurrence relative to the immediately preceding two elements.

The previous run counted by `f` ends at `i - 1` and includes `nums[i-2]` whenever its length is at least two. Appending `nums[i]` therefore extends that same contiguous Fibonacci subarray by one:

`f = f + 1`.

The new run length may be the largest so far, so:

`ans = max(ans, f)`.

For `[5, 2, 7, 9, 16]`:

- $7=5+2$, so the run grows to three;
- $9=2+7$, so it grows to four;
- $16=7+9$, so it grows to five.

The entire array is counted.

**Resetting after a failed recurrence**

If the current value does not equal the sum of the previous two, no Fibonacci subarray of length at least three can end at `i` while including those immediately preceding positions.

However, the pair:

`nums[i - 1], nums[i]`

is always a valid Fibonacci subarray of length two because no recurrence must be checked until a third term exists. That pair is also the only possible starting base for a longer Fibonacci subarray that may continue at `i + 1`.

The correct reset is therefore:

`f = 2`,

not zero or one.

For `[1, 1, 1, 1, 2, 3, 5, 1]`, the early triples of ones fail because $1\ne1+1$. Each failure resets the ending run to two. At index four, $2=1+1$ begins a length-three run using indices two through four; the following values extend it to length five.

**Meaning of `f` after every iteration**

After processing index `i`, `f` equals the greatest length of a Fibonacci subarray whose right endpoint is exactly `i`.

If the recurrence succeeds, any valid length-three-or-more subarray ending at `i` must extend a valid subarray ending at `i - 1`, and the longest such extension has length old `f + 1`.

If the recurrence fails, no length-three candidate ending at `i` is valid, while the final pair remains valid, making two the exact maximum.

This local state is sufficient because a future extension depends only on the most recent two array values and the current run length. Older failed runs cannot jump across a break; that would violate contiguity.

**Why `ans` captures runs ending earlier**

`f` is reset when a run breaks, so it cannot by itself remember an earlier maximum. `ans` is updated whenever a run grows and never decreases.

Every Fibonacci subarray has some right endpoint. When the scan reaches that endpoint, `f` equals at least its length, and `ans` records the maximum over all such ending positions. The initial value two already covers the case where no triple satisfies the recurrence.

**Subarray versus subsequence**

The method always compares adjacent indices `i-2`, `i-1`, and `i`. It never skips an element. This is essential: a Fibonacci subsequence problem would require searching nonadjacent choices and a much larger dynamic program.

## Complexity detail

Let $n$ be `len(nums)`.

The loop visits indices two through $n-1$ once. Each iteration performs one addition, one equality comparison, and constant state updates. Total running time is $O(n)$.

Only `n`, `ans`, `f`, and the loop index are stored beyond the input. Auxiliary space is $O(1)$.

The input array is not modified. Python integers safely compute a sum up to $2\cdot10^9$ under the given value bounds.

## Alternatives and edge cases

- **Check every subarray:** Extending from every left boundary repeats the same recurrence checks and can take $O(n^2)$ time.
- **Dynamic-programming array:** Storing the ending length for every index also works in $O(n)$ time but wastes $O(n)$ space because only the previous length is needed.
- **Treat it as a subsequence problem:** Skipping elements solves a different problem and can report a length that is not contiguous.
- **No valid triple:** The answer remains two, matching the note that every pair is Fibonacci.
- **Entire array valid:** `f` increases on every iteration and `ans` reaches $n$.
- **Break followed by a new run:** Resetting to two preserves the final pair as the seed for the next possible recurrence.
- **Equal values:** Equality alone neither helps nor hurts; the third value must equal their sum.
- **Large values:** Only exact integer addition and comparison are used, with no floating-point behavior.
- **Minimum allowed length:** For a three-element input, one recurrence test decides whether the answer is three or two.
- **Positive-value guarantee:** The rolling argument depends on the recurrence and contiguity, not positivity, though positivity is part of the contract.
