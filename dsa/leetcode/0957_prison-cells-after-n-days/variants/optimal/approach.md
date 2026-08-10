## General

**A huge day count hides a tiny state space**

There are eight binary cells, so only `2^8 = 256` complete states exist. After one day, both endpoints are always zero because they lack two neighbors. From then on, only six interior bits vary, giving at most `2^6 = 64` reachable states.

The transition is deterministic: the same state always produces the same next state. A sufficiently long simulation must repeat a state and enter a cycle. Once its length is known, billions of days can be skipped with a remainder.

**Use immutable state keys**

The input list becomes `state = tuple(cells)`. Tuples are hashable dictionary keys, unlike mutable lists.

Dictionary `seen` maps each state to the remaining `n` when it was encountered. The code counts days downward rather than storing elapsed days.

**Detect and measure a cycle**

At each loop start, if `state` exists in `seen`, cycle length is:

`seen[state] - n`.

For example, if the same state was seen with twenty days remaining and returns with six remaining, fourteen transitions separate equal states. Evolution will now repeat every fourteen days.

The assignment `n %= cycle_length` discards all complete cycles. Each full cycle begins and ends at the same state, so removing it cannot change the final result.

The current state is then recorded with its possibly reduced remaining-day count.

**Why zero remaining days is checked next**

If modulo reduction makes `n == 0`, the current state is already final. The loop breaks before applying another transition.

Otherwise, `n -= 1` consumes exactly one day and the next state is formed. This order prevents an off-by-one error when the remaining days contain an exact number of cycles.

**Compute every new cell from the old tuple**

The new first and last cells are explicitly zero.

For interior indices one through six:

`int(state[index - 1] == state[index + 1])`

produces one when both neighbors agree and zero when they differ. Equality covers both occupied-occupied and vacant-vacant.

The cell's own previous value is irrelevant. Building a new tuple guarantees simultaneous updates; no newly computed cell can affect another cell on the same day.

**Why the dictionary values use remaining days**

Many cycle detectors store the elapsed day index. This solution stores remaining days, which decrease by one per ordinary transition.

For repeated state `s`, the earlier remaining count is larger. Subtracting the current count gives exactly the number of transitions between occurrences, hence a positive cycle length.

After fast-forwarding, overwriting `seen[state]` is harmless. The same deterministic cycle remains, and the reduced `n` is now smaller than one full cycle.

**A conceptual large-day example**

Suppose a state repeats every fourteen days and there are one billion days remaining. Any whole multiple of fourteen returns to that same state. Only `1,000,000,000 % 14` transitions affect the final position inside the cycle.

The algorithm replaces the huge count by this small remainder and simulates only those steps.


Before detecting a cycle, the loop applies the exact rule once per decremented day.

At a repeated state, deterministic evolution guarantees the sequence between occurrences will repeat forever. Removing whole copies of that cycle preserves both current state and eventual final state. The loop stops exactly when no transitions remain.

Converting the final tuple back to a list returns the required format.

**Why initial endpoint values are preserved**

The input endpoints may initially be zero or one. They must not be normalized before day one because they are genuine neighbors of interior cells one and six during that first transition. The computed next state then forces both endpoints to zero. Consequently, day zero is handled exactly as supplied, while every later state belongs to the smaller six-variable interior universe used in the cycle bound.

## Complexity detail

With exactly eight cells, at most 256 states can appear, and after the first transition at most 64 endpoint-zero states are possible. Every transition examines six interior positions.

Time and auxiliary space are therefore `O(1)` with respect to input day count `n`. They are bounded by the fixed state universe rather than by up to one billion days.

If cell count were variable `C`, state count could be exponential in `C`, but the contract fixes `C = 8`.

## Alternatives and edge cases

- **Simulate every day:** Correct for small `n` but infeasible near one billion.
- **Hard-code a fourteen-day cycle:** This problem has a familiar short cycle, but general detection is clearer and self-verifying.
- **Bitmask state:** Eight bits can encode the cells compactly while preserving the same cycle logic.
- **In-place left-to-right update:** Incorrect because new values would influence other cells during the same day.
- **Endpoint cells:** They become zero on every transition.
- **Equal occupied neighbors:** The new interior value is one.
- **Equal vacant neighbors:** It is also one.
- **Different neighbors:** The new value is zero.
- **Cycle remainder zero:** Break without applying an extra day.
- **Input preservation:** Tuple conversion leaves the caller's list unchanged and the function returns a new list.
