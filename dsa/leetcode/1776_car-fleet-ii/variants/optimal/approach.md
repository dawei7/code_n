## General

**Process cars from front to back in reverse index order**

Positions are strictly increasing, so larger indices are farther along the road. A car can collide only with a car or fleet ahead of it.

The exact solution scans from right to left. When processing car `i`, collision behavior for every relevant car ahead has already been computed in `ans`.

`stk` holds candidate indices ahead that may be the next fleet car `i` reaches. Candidates that cannot be car `i`'s first collision are popped.

**Compute catch time only when i is faster**

For candidate car `j` ahead, car `i` can catch it while both keep their current speeds only if:

`cars[i][1] > cars[j][1]`.

The initial distance is `position[j] - position[i]`, and the relative closing speed is `speed[i] - speed[j]`. Their hypothetical collision time is:

$$
t=
\frac{\text{position}_j-\text{position}_i}
{\text{speed}_i-\text{speed}_j}.
$$

The source computes this with true division, producing a floating-point answer.

If `i` is no faster than `j`, it cannot catch `j` before `j` changes into some fleet. Candidate `j` is popped so the algorithm can consider the slower fleet or car structure farther ahead that `j` may eventually join.

**Check whether j still exists at time t**

Even when `i` is faster than `j`, the calculated `t` is valid only if `j` has not already collided with its own next car before that time.

`ans[j] == -1` means `j` never collides ahead, so it continues at its initial speed indefinitely and is a valid target.

Otherwise `ans[j]` is the time when `j` joins another fleet. If `t <= ans[j]`, car `i` catches `j` no later than that event. The collision time is valid, so the source stores `ans[i] = t` and stops popping.

If `t > ans[j]`, candidate `j` changes speed and position behavior before `i` would reach it as an independent car. The hypothetical time is obsolete. The algorithm pops `j` and considers the next candidate representing the fleet ahead.

Equality is accepted: if `i` reaches `j` at the exact moment `j` hits its next fleet, all meet simultaneously and `t` is still car `i`'s first collision time.

**Why popped candidates can never become the first collision**

A candidate is removed for one of two reasons:

- Car `i` cannot catch it at its current speed.
- Car `i` would catch it only after it has already merged into a fleet ahead.

In either case, `i` cannot collide first with that candidate as a separate car. Its future is governed by a fleet farther ahead, so retaining the index would only repeat an invalid comparison.

This monotonic elimination is what makes the stack linear rather than scanning every car ahead for every `i`.

**Why a surviving top is the next collision**

Stack order preserves cars or fleet representatives ahead in the relevant road order. After invalid nearer candidates are removed, the first top satisfying the speed and timing conditions is reachable before it disappears.

No skipped candidate can be an earlier valid collision because each was proven unreachable in its independent lifetime. Therefore assigning its catch time to `ans[i]` is correct.

If the stack empties, no fleet ahead can be caught and `ans[i]` remains minus one.

**Trace the first example**

The rightmost car at position seven has no car ahead, so its answer stays minus one and its index enters the stack.

Car at position four has speed three versus speed two ahead. Catch time is three seconds, and the front car never collides, so answer is three.

Car at position two has speed one. It cannot catch the faster car immediately ahead and ultimately does not catch a fleet, so its answer remains minus one.

Car at position one has speed two and catches the position-two car, which travels at speed one indefinitely, after one second. The result matches `[1,-1,3,-1]`.

**Stack amortization**

Every car index is appended exactly once. Once popped, it never returns. Although one iteration may pop many entries, the total number of pops across the complete scan is at most $n$.

That global accounting is essential: the nested while loop does not imply quadratic time.

**Why the returned array is correct**

When `ans[i]` is set, the stored time is the physical catch time for a candidate that remains independent until that moment, and all nearer invalid candidates have been eliminated. It is therefore car `i`'s first collision.

When no candidate survives, every potential car ahead is unreachable before joining a fleet or is too fast, so minus one is correct. Right-to-left processing supplies already-correct future collision times for every validity comparison.

## Complexity detail

Let $n$ be the number of cars. Each index is pushed once and popped at most once. All arithmetic and answer checks per push or pop are constant time, so total time is $O(n)$.

The stack and answer list each hold at most $n$ entries, giving $O(n)$ space, matching the manifest. Other variables are scalar.

Floating-point division is performed only for candidates where the rear car is faster. Accepted tolerance accommodates ordinary binary floating-point representation.

## Alternatives and edge cases

- **Simulate continuous motion events:** A priority queue can process fleet collisions but requires complex invalidation and is slower than the monotonic stack.
- **Check every car ahead:** It can take $O(n^2)$ time.
- **Equal speeds:** The rear car cannot close the distance, so the candidate is popped.
- **Rear car slower:** It cannot catch the candidate before that candidate changes fleet state.
- **Front candidate never collides:** Any positive catch time from a faster rear car is valid.
- **Candidate collides earlier:** A hypothetical later catch is discarded by `t > ans[j]`.
- **Simultaneous fleet collision:** `t == ans[j]` is accepted.
- **Rightmost car:** It has no target and always remains minus one.
- **Several cascading fleets:** Repeated pops skip cars that disappear before they could be reached.
- **Strict position ordering:** It guarantees positive distances for indices ahead.
- **Slowest fleet speed:** Considering farther surviving candidates models the speed inherited after intermediate collisions.
- **One car:** The stack starts empty for it and answer is `[-1]`.
- **Answer initialization:** Minus one distinguishes never colliding from every nonnegative time.
- **Input preservation:** Cars are read in place and never reordered or modified.
