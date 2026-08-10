## General

**The special positions reached by repeated acceleration**

The car begins at position 0 with speed 1. After one `A` command it moves 1; after another it moves 2; after another it moves 4. After `k` consecutive accelerations, its position is

$$
1+2+4+\cdots+2^{k-1}=2^k-1,
$$

and its speed is `2^k`.

Positions of the form `2^k - 1` are therefore easy: exactly `k` accelerations reach them. No shorter command sequence can travel that far because reversals do not move the car and interrupt the doubling progress. The DP treats these positions as direct base patterns.

**Define a distance-only dynamic program**

Let `dp[i]` be the minimum number of instructions needed to reach positive position `i` starting from position 0 with speed 1. The final speed does not matter.

The array is filled from `i = 1` through `target`. Every recurrence term for `dp[i]` refers only to a smaller positive distance, so its optimal value is already available.

For a current distance `i`, `k = i.bit_length()` is the unique integer satisfying

$$
2^{k-1}\le i<2^k.
$$

Thus,

$$
2^{k-1}-1<i\le 2^k-1.
$$

After `k-1` accelerations, the car is still before `i`. After `k` accelerations, it reaches or passes `i`. An optimal path can be organized around these two nearby acceleration landmarks.

**Exact hit with only accelerations**

If `i == 2**k - 1`, the car reaches `i` after exactly `k` accelerations. The code sets `dp[i] = k` and continues to the next distance.

This case is separated because the overshoot gap would be zero, and no reversal is necessary. Adding one would make the candidate longer than the obvious all-`A` sequence.

**Strategy one: pass the target, reverse, and return**

When `i < 2^k - 1`, one option is:

1. issue `k` accelerations, reaching `F = 2^k - 1`;
2. issue one `R`, resetting the speed to `-1`;
3. travel backward by the gap `F-i` using an optimal instruction pattern.

The gap is

$$
F-i=2^k-1-i.
$$

After the reversal, the car faces toward the target from the right. Reflecting the number line turns this into the same subproblem as traveling a positive distance `F-i` from rest state speed 1. The car's absolute position and direction are different, but the instruction rules are symmetric under reflection.

The command count is therefore

$$
k+1+\texttt{dp}[2^k-1-i].
$$

This is the initial value assigned to `dp[i]`. The gap is smaller than `i` because `i \ge 2^{k-1}`, so its DP entry has already been computed.

For target 6, `k = 3` and `F = 7`. Three accelerations reach 7, one reversal faces left, and `dp[1] = 1` supplies one acceleration back to 6. The total is 5, corresponding to `"AAARA"`.

**Strategy two: reverse before the target, back up, then face forward**

Overshooting is not always optimal. The alternative begins with only `k-1` accelerations, reaching

$$
P=2^{k-1}-1
$$

with positive speed `2^{k-1}`. Since `P < i`, the target remains ahead.

The car now issues `R`, resetting its speed to `-1`, then performs `j` backward accelerations. Those `j` commands move a total distance

$$
1+2+\cdots+2^{j-1}=2^j-1
$$

to the left. Its new position is

$$
P-(2^j-1)=2^{k-1}-2^j.
$$

A second `R` resets the negative speed to `+1`. The car is again facing the target, and the remaining forward distance is

$$
i-\left(2^{k-1}-2^j\right).
$$

The DP already knows the shortest way to cover that smaller distance. The number of commands used before the subproblem is:

- `k-1` forward accelerations;
- one first reversal;
- `j` backward accelerations;
- one second reversal.

Their total is

$$
(k-1)+1+j+1=k-1+j+2.
$$

This produces the exact candidate in the code:

`dp[i - (2 ** (k - 1) - 2**j)] + k - 1 + j + 2`.

The loop tries `j` from 0 through `k-2`. When `j = 0`, there is no backward `A`; the two reversals simply discard the large speed and reset it to `+1` before continuing. When `j = k-1`, backing up would return to position zero and make the remaining distance equal to `i` itself, so it would not be a smaller DP subproblem. Larger `j` values go even farther backward and cannot improve this normalized pattern. Therefore, `range(k - 1)` covers the useful choices.

**Why these patterns cover an optimal solution**

Before the first reversal, an optimal sequence begins with some number of accelerations; reversing earlier without first moving can be removed or normalized. Around target `i`, the relevant longest initial acceleration run either reaches the first landmark at or beyond `i` using `k` accelerations, or stops at the preceding landmark using `k-1` accelerations.

With `k` accelerations, the car has reached the target exactly or overshot it, leading to the first strategy. With `k-1` accelerations, it is short of the target; it may reverse, travel backward for some `j` accelerations, reverse again, and then solve the smaller remaining distance, leading to the second strategy.

Any later instructions after the normalized reversals form a translated and possibly reflected copy of the original start-state problem, because `R` resets speed magnitude to 1. That is exactly why a distance-only `dp` value can complete the sequence.

The recurrence takes the minimum over the overshoot candidate and every useful undershoot/backtrack candidate. Each candidate is a valid instruction sequence, and the structural argument places an optimal sequence in one of these families. Hence, `dp[i]` is optimal.

**Why bottom-up order works**

The overshoot gap `2^k-1-i` is less than `i`. In an undershoot candidate, the temporary forward position `2^{k-1}-2^j` is positive for `j <= k-2`, so subtracting it from `i` also gives a distance strictly between 0 and `i`. All referenced table entries were filled in earlier iterations.

Starting with `dp[0] = 0` supplied by the zero-initialized list, the loop therefore builds correct answers in increasing distance order and finally returns `dp[target]`.

## Complexity detail

Let `T = target`. The outer loop computes `T` entries. For distance `i`, `k = O(\log i)` and the inner loop tries `k-1` possible backward acceleration counts. Every candidate uses constant-time arithmetic and table access.

The total time is

$$
O\left(\sum_{i=1}^{T}\log i\right)=O(T\log T).
$$

The `dp` list contains `T+1` integers, so auxiliary space is `O(T)`. The solution is iterative and uses no recursion stack. All other variables require constant space.

The `bit_length` operation obtains `k` directly from the binary magnitude of `i`, avoiding a separate loop to find the surrounding powers of two.

## Alternatives and edge cases

- **Breadth-first search over position and speed:** BFS directly finds the shortest instruction sequence and is conceptually simple, but it must bound and store many `(position, speed)` states. The distance DP exploits the powers-of-two structure and uses `O(T)` space.

- **Memoized recursive DP:** The same overshoot and undershoot recurrence can be evaluated top-down. Bottom-up order makes the “all subdistances are smaller” property explicit and avoids recursion overhead.

- **Greedy always overshoot:** Reaching `2^k-1` and coming back is sometimes best, but not always. Trying the early-reversal family is necessary for optimality.

- **Exact Mersenne position:** When `i = 2^k-1`, `k` accelerations are optimal and no reversal should be added.

- **`target = 1`:** Its bit length is 1, it equals `2^1-1`, and the answer is one `A`.

- **Zero backward accelerations:** `j = 0` deliberately permits two consecutive reversals to reset a large positive speed to `+1` without changing position.

- **Exclude `j = k-1`:** That choice returns to position zero, so the remaining DP distance would still be `i` and would create a self-dependency rather than progress.

- **Negative positions allowed:** The derivation can tolerate going left, but the normalized useful undershoot positions in the loop remain positive. Reflection symmetry handles backward completion after overshooting.

- **Final speed:** Only reaching the target position matters. The DP does not constrain the speed at arrival.

- **Integer arithmetic:** Every landmark and remaining distance is integral. Powers of two and bit length describe the acceleration dynamics exactly without floating-point calculations.
