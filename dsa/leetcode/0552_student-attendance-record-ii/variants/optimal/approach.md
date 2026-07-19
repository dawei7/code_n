## General
**Keep only information that constrains the next day**

Whether another character may be appended depends on two facts: whether an absence has already appeared and how many consecutive late days end the current prefix. This creates six states `(absences, late_streak)`, with absences in `{0, 1}` and the streak in `{0, 1, 2}`.

**Start from the empty eligible record**

Before processing a day, state `(0, 0)` has count one and every other state has count zero. Each iteration builds a fresh six-state table for records one day longer.

**Apply the three legal transitions**

Appending `P` preserves the absence count and resets the late streak to zero. Appending `A` is allowed only from a zero-absence state, changes the absence count to one, and resets the streak. Appending `L` preserves absences and increases the streak only when it is below two.

**Reduce every accumulated count**

Several predecessor states can enter the same next state. Add their counts modulo `1,000,000,007` so values remain bounded without changing the required modular result.

**Why the state totals count every valid record once**

Each eligible prefix has exactly one absence count and one trailing-late length, so it belongs to exactly one state. The transitions append each possible legal next character and reject precisely the moves that would create a second absence or third consecutive late day. Induction over the processed length therefore establishes a one-to-one correspondence between generated transitions and eligible records. Summing all six states after `n` days gives the answer.

## Complexity detail
Each of the `n` days updates six states with at most three constant-time transitions, so time is $O(n)$. Only the current and next six counts are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Six-by-six matrix exponentiation:** applies the same finite-state transitions in $O(\log n)$ time, but is more complex and unnecessary for the given bound.
- **Memoized recursion:** has $O(n)$ states and time but uses $O(n)$ call-stack and cache space.
- **Enumerate all records:** explores $3^{n}$ strings and becomes infeasible quickly.
- **Recompute every prefix length independently:** remains correct but repeats transitions and takes $O(n^2)$ time.
- **One day:** all three characters `P`, `A`, and `L` are eligible.
- **Second absence:** no transition enters an absence count of two.
- **Third late day:** no transition leaves a late streak of two by appending `L`.
- **Modulo arithmetic:** must be applied during accumulation, not only after exponentially large exact counts are formed.
