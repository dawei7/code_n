## General

**Track purchased chairs and currently free chairs**

The exact source uses two counters:

- `cnt` is the total number of chairs that have ever been needed and therefore must be available initially;
- `left` is the number of those chairs currently free.

The room starts empty with no purchased capacity, so both are zero.

When a person enters:

- if `left > 0`, one free chair is reused and `left` decreases;
- otherwise, every existing chair is occupied, so one additional chair is necessary and `cnt` increases.

When a person leaves, their chair becomes free, so `left` increases.

`cnt` never decreases. It records the maximum capacity required over the whole event sequence, which is the minimum number that must have been supplied from the beginning.

**Connection to maximum occupancy**

At every prefix,

$$
\text{current occupants}=\texttt{cnt}-\texttt{left}.
$$

Whenever occupancy rises without exceeding earlier maximum, a free chair is consumed. Whenever it would exceed all prior occupancy, no free chair exists and `cnt` grows by one. Therefore, final `cnt` equals maximum simultaneous occupancy.

The manifest describes explicitly simulating occupancy and recording its maximum. The exact code implements the equivalent resource-reuse viewpoint.

**Example**

For `"ELELEEL"`:

- first E finds no free chair, so `cnt=1`;
- L makes `left=1`;
- next E consumes it;
- alternating events repeat;
- the second consecutive E eventually finds no free chair and raises `cnt` to 2.

No later prefix needs more, so two chairs suffice.

For seven E events, no chair is ever freed. Every entry increments `cnt` and the result is 7.

**Why allocating only on demand is optimal**

The simulation constructs a feasible reuse assignment: each entry either takes a chair freed by an earlier departure or receives a newly counted chair. Thus `cnt` chairs are enough.

Whenever `cnt` increases to $c$, that entering person arrives while the previous $c-1$ chairs are all occupied. Any valid room must have at least $c$ chairs at that instant. Final `cnt` is therefore also a lower bound. Being both sufficient and necessary proves minimality.

**State invariant after every event**

After a valid event prefix, `cnt` equals the largest occupancy reached in that prefix, `left` equals `cnt` minus current occupancy, and every currently present person has one chair.

For a leave, occupancy drops by one while capacity is unchanged, so free chairs rise by one. For an entry with a free chair, occupancy rises and free chairs fall, still not exceeding the established maximum. For an entry without a free chair, current occupancy equals capacity; increasing both occupancy and `cnt` by one establishes a new maximum and leaves zero free chairs.

This induction connects the resource simulation to the mathematical peak-prefix count and proves that no chair is double-assigned.

**Alternative prefix-balance formula**

If E contributes $+1$ and L contributes $-1$, current occupancy after a prefix is their cumulative sum. The required chair count is the maximum of those prefix sums. The exact variables encode the same quantity indirectly: `cnt - left` is the current prefix sum, while `cnt` is its historical maximum.

The validity guarantee also implies every prefix sum is nonnegative. That is the arithmetic form of “nobody leaves an empty room.”

**Why free chairs may outnumber current occupants**

After a busy period, several people can leave. `left` then grows while `cnt` remains the earlier peak. Those free chairs are real capacity ready for later entrants; discarding the count on leave would make the method purchase the same chair again.

**Valid sequence guarantee**

The statement guarantees exits are valid, so a leave never occurs when no person is present. The exact code does not explicitly verify this. With malformed input beginning in `'L'`, it would create a free chair that had never been counted, breaking the interpretation. Correctness relies on the guarantee.

**Why c other than E means leave**

The branch uses `else` rather than `elif c == "L"`. This is safe because the alphabet contains only `'E'` and `'L'`. Any unexpected character would be treated as a leave outside the contract.

## Complexity detail

Let $n$ be the event-string length.

The loop processes each event once with constant work, so time is $O(n)$.

Only `cnt`, `left`, and the current character are stored. Auxiliary space is $O(1)$.

The output is one integer, and the input string is unchanged.

The best case and worst case both scan the full string because the final capacity cannot be known until all events are considered.

## Alternatives and edge cases

- **Occupancy plus maximum:** Add one on E, subtract one on L, and update a peak variable. It matches the manifest and is algebraically equivalent.
- **Stack of chairs:** Explicitly store free chair identifiers, but identities never matter and would use unnecessary space.
- **Count E minus L prefixes:** Maximum prefix balance directly gives the answer.
- **All entries:** Every event needs a new chair, so result is string length.
- **Perfect alternation starting with E:** One chair is repeatedly reused.
- **Consecutive entries:** Each beyond currently free capacity raises `cnt`.
- **Consecutive valid leaves:** They accumulate several reusable chairs.
- **Room empty at end:** Final occupancy may be zero while `cnt` retains peak capacity.
- **Valid-sequence guarantee:** It prevents `left` from representing nonexistent chairs.
- **Single event E:** One chair is necessary.
- **Only E/L alphabet:** It makes the source's `else` branch safe.
- **No early return:** A later burst of entries may exceed every earlier capacity.
