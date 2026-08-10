## General

**Translate the placement rule directly into counting**

Every integer ball number from `lowLimit` through `highLimit` appears exactly once. Its destination box is determined only by the sum of its decimal digits. Therefore the problem can be solved by visiting every ball, computing that sum, and increasing the counter for the corresponding box.

The exact solution stores the counters in `cnt = [0] * 50`. Index `s` represents box number `s`, and `cnt[s]` records how many processed balls have digit sum `s`. Index zero is allocated even though positive ball numbers never have digit sum zero; keeping it makes the digit sum itself usable as an array index without an offset.

After all balls are processed, `max(cnt)` returns the largest occupancy. The identity of the winning box is irrelevant, and ties need no special treatment because the requested answer is only the number of balls in a most-populated box.

**Compute one digit sum with repeated division**

For each loop value `x`, the solution initializes `y = 0`. The expression `x % 10` extracts the current last decimal digit. Adding that digit to `y` accumulates the digit sum. Integer division `x //= 10` discards the digit just processed.

For example, beginning with `x = 321`:

- The remainder is one, so `y` becomes one and `x` becomes 32.
- The remainder is two, so `y` becomes three and `x` becomes 3.
- The remainder is three, so `y` becomes six and `x` becomes zero.

The `while x` loop then stops, and `cnt[6]` is incremented. This exactly implements the placement rule for ball 321.

At every iteration of the inner loop, `y` equals the sum of digits already removed, while the current `x` contains exactly the not-yet-processed leading digits. When `x` reaches zero, no digits remain, so `y` is the complete digit sum. This invariant explains why no decimal digit is omitted or counted twice.

**Why changing x does not skip ball numbers**

The code deliberately reduces `x` to zero while finding its digits. In some loop styles, mutating the loop variable could make the next number incorrect. Python's `for x in range(lowLimit, highLimit + 1)` obtains each next value from the independent `range` iterator, however. At the beginning of the next outer iteration, Python assigns the next integer to `x` regardless of how the preceding iteration changed it.

Thus the digit extraction destroys only the temporary integer bound to `x`. It does not modify `lowLimit`, `highLimit`, the `range` object, or any future ball number.

**Why an array of fifty counters is sufficient**

The upper limit is at most $10^5$. Any number below $100000$ has at most five digits, so its digit sum is at most $9+9+9+9+9=45$. The only six-digit value permitted is $100000$, whose digit sum is one. Therefore every reachable box number is safely below 50.

The array has a few intentionally unused positions. This is preferable to a boundary-sized structure that is harder to read, and it still consumes constant memory under the stated constraints. No box with an infinite label range needs to be physically represented because the input's number of decimal digits bounds every possible digit sum.

**Trace the first example**

For balls one through nine, each ball enters the box with the same number because it has one digit. Ball ten has digit sum one and therefore joins ball one in box one. The counters for boxes two through nine remain one, while `cnt[1]` becomes two. The maximum counter is consequently two.

The second and third examples show that the winning box need not be unique and need not have a one-digit ball number associated with it. The counter array naturally handles both facts: every digit sum updates its own index, and `max` ignores which index first attains the maximum.

**Why the final maximum is correct**

After processing any prefix of the inclusive number range, `cnt[b]` equals the number of processed ball labels whose digit sum is $b$. This is initially true because all counters are zero. Processing the next label computes its exact digit sum $s$ and increments only `cnt[s]`, so the statement remains true by induction.

When the outer loop ends, the processed prefix is the entire range. Consequently every counter is the occupancy of its corresponding box. The maximum array element is therefore exactly the greatest number of balls in any box, which is the requested result.

## Complexity detail

Let $R = \texttt{highLimit}-\texttt{lowLimit}+1$ be the number of balls, and let $D$ be the maximum number of decimal digits in a ball label. The outer loop runs $R$ times. Repeated division processes at most $D$ digits per label, so the total time is $O(RD)$, matching the manifest. The final scan of 50 counters is constant time under the fixed constraints and does not change that bound.

The exact source allocates exactly 50 integer counters and a constant number of scalar variables. Under the stated limit, its auxiliary space is therefore $O(1)$. If the same array-counting idea were generalized to arbitrary $D$-digit numbers, the maximum digit sum would be $9D$, so a suitably sized counter array would use $O(D)$ space; that is the generalized bound recorded in the manifest.

Because $D$ is at most six for this problem, it is also valid to regard $O(RD)$ as $O(R)$ under the fixed constraint. Keeping $D$ explicit better explains the work performed by the inner loop.

## Alternatives and edge cases

- **Hash map of box counts:** A dictionary avoids choosing an array bound and generalizes easily, but has hashing overhead and is unnecessary when the digit-sum range is tiny.
- **Convert each number to a string:** Summing converted digit characters is readable, yet allocates or processes string representations and retains the same $O(RD)$ time.
- **Incremental digit-sum updates:** One can update the sum from one number to the next using carry behavior, potentially reducing repeated division, but the carry logic is substantially easier to get wrong.
- **Digit dynamic programming:** Counting box occupancies without enumerating every label is possible for much larger numeric ranges, but is excessive for `highLimit <= 100000`.
- **Inclusive upper endpoint:** `range(lowLimit, highLimit + 1)` includes `highLimit`; omitting the plus one would lose the final ball.
- **Single-ball range:** Exactly one counter becomes one, so the maximum is one.
- **Tied boxes:** `max(cnt)` returns the shared occupancy, which is all the problem asks for.
- **Ball number ten:** The zero digit contributes nothing, leaving digit sum one.
- **Ball number 100000:** Despite having six digits, its sum is only one and fits comfortably in the counter array.
- **Largest five-digit sum:** `99999` maps to box 45, still below index 50.
- **Unused counter zero:** It remains zero because all labels are positive, but causes no issue in the maximum.
- **Mutated loop variable:** Python's range iterator supplies the next label independently, so reducing `x` inside the body is safe.
- **No explicit winning-box variable:** Tracking only counters and taking their maximum is sufficient because box identity is not returned.
