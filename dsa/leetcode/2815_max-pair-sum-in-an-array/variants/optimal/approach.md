## General

**Test the defining condition for every pair.** A pair is valid when the largest decimal digit of its two numbers is equal. Among valid pairs, the task asks for the maximum sum. The exact solution uses exhaustive pair enumeration: it considers every pair of distinct indices exactly once, checks the digit condition when the pair could improve the answer, and retains the greatest valid sum.

This differs from the ten-bucket technique described in the Optimal manifest. The source does not group numbers or keep a best prior value per largest digit.

**Generate unique unordered index pairs.** The outer loop uses `enumerate(nums)`, giving index `i` and value `x`. The inner loop iterates over `nums[i + 1:]`, which contains only values to the right of `i`.

For any two distinct indices $p<q$, the pair is visited when `i = p` and `y` is the copied suffix element originating at $q$. It is not visited with the reverse ordering because the inner slice never includes earlier positions. Therefore, every legal pair of array positions is considered once, even when the two stored numeric values are equal.

**Compute the candidate sum first.** `v = x + y` is the score of the current pair. The condition begins with `ans < v`. Python's `and` short-circuits, so if this sum cannot exceed the best already found, the code does not spend time finding either largest digit.

Skipping the digit check in that case is safe. Even if the pair were valid, its sum would not improve `ans`. The task needs only the maximum value, not a list or count of all valid pairs.

**Find a number's largest decimal digit through text.** `str(x)` converts a positive integer into its ordinary decimal representation. `max(str(x))` returns the lexicographically greatest character. For characters `"0"` through `"9"`, Unicode code-point order agrees with numeric digit order, so the greatest character represents the largest decimal digit.

For example, `str(2536)` is `"2536"` and its maximum character is `"6"`. If both numbers produce the same maximum character, the pair satisfies the rule. Positivity matters: there is no minus-sign character to interfere, and the constraints guarantee positive numbers.

**Update only for a valid improvement.** The assignment `ans = v` occurs only when both conditions are true: the sum is strictly larger than the current answer and the largest digits match. Starting `ans` at negative one gives the required sentinel when no pair is valid, since all valid pair sums are positive and would replace it.

If two valid pairs have the same maximum sum, the later pair does not update because the comparison is strict. This is fine because only the numeric maximum is returned; the identity of the pair is irrelevant.

**Why exhaustive enumeration is correct.** Every candidate answer must come from two distinct array indices. The nested loops visit every such unordered pair exactly once. For each visited pair whose sum could beat the current best, the largest-digit comparison accepts it exactly when the problem accepts it. `ans` is therefore the maximum valid sum among all pairs processed so far.

That statement is a loop invariant. It begins true because no pairs have been processed and negative one represents “none.” Processing another pair either leaves the maximum unchanged or replaces it with a larger valid sum. When enumeration ends, the processed set is the complete pair set, so `ans` is the required result.

**Repeated values remain separate items.** Slicing yields numeric values rather than indices, but each suffix position is still iterated separately. If two identical numbers occur at different indices, the pair between them is valid and is examined. The algorithm does not mistakenly deduplicate the input.

**The exact source repeatedly recalculates digit maxima.** A number used in many pairs is converted to a string and scanned many times, unless short-circuiting skips some checks. This is correct but inefficient compared with precomputing one digit key per input or using ten buckets. The small constraint `n <= 100` makes the brute-force method practical.

**Slicing is also real work.** For every outer index, `nums[i + 1:]` creates a new list of references. These suffix copies total a quadratic number of references over the whole run and give the exact implementation linear peak temporary list space. An index-based inner loop would avoid those copies without changing pair enumeration.

## Complexity detail

Let $n$ be the number of values and let $D$ be the maximum number of decimal digits in a value, equivalently $D=O(\log V)$ for maximum value $V$. There are $n(n-1)/2=O(n^2)$ pairs.

When the short-circuit first condition passes, converting each number to text and finding its maximum takes $O(D)$ time. In the worst case this happens for $O(n^2)$ pairs, so pair checking costs $O(n^2D)=O(n^2\log V)$ time. The repeated suffix slices also perform $O(n^2)$ total reference copying, which is dominated when retaining the digit factor and equal when $D$ is bounded.

Under the given `nums[i] <= 10^4`, each number has at most five digits, so $D$ is a small constant and time simplifies to $O(n^2)$. It is useful to state both the general and constraint-specific views.

At peak, the current suffix slice contains $O(n)$ references. Temporary decimal strings contain $O(D)$ characters. Thus exact auxiliary space is $O(n+D)$, which is $O(n)$ under the constraints. This differs from the manifest's $O(1)$ claim because the manifest describes a bucket algorithm and the exact loop uses slicing. If the inner loop used indices instead of a slice, its auxiliary space would fall to $O(D)$, or $O(1)$ under the bounded digit length.

## Alternatives and edge cases

- **Ten largest-digit buckets:** Scan each number once, compute its largest digit, combine it with the best prior value in that digit's bucket, and update the bucket maximum. This takes $O(n\log V)$ time and $O(1)$ space because there are ten buckets, matching the manifest.
- **Precompute digit keys:** Store each number's largest digit once, then enumerate pairs in $O(n^2)$ time without repeated string scanning. It uses $O(n)$ extra space.
- **Arithmetic digit extraction:** Repeatedly use remainder ten and integer division rather than converting to text. It has $O(\log V)$ work per number and handles the numeric intent directly.
- **No valid pair:** `ans` remains negative one, exactly the required return value.
- **Duplicate numeric values:** Different indices form a legal pair; the enumeration includes them separately.
- **Largest digit appears multiple times:** `max` still returns that digit once as the comparison key, which is all the condition requires.
- **Number containing zero:** Zero can be one of its digits, but a larger character wins unless the number itself were zero; inputs are at least one.
- **Value ten thousand:** Its decimal characters are one followed by zeros, so its largest digit is one.
- **Equal valid sums:** Keeping the first maximum is sufficient because the output contains no pair identity.
- **Short-circuit order:** Digit maxima are skipped only when the sum cannot improve `ans`. Reversing the logic carelessly could skip a larger candidate before validating it.
- **Positive inputs:** They ensure every valid sum exceeds the negative-one sentinel and prevent a minus sign from entering the string comparison.
- **Input preservation:** Sorting is not used; slices copy references, and `nums` remains unchanged.
- **Manifest mismatch:** The claimed bucket complexity belongs to the faster alternative, not the exact exhaustive source, whose real worst-case pair count is quadratic.
