## General

**Process customers in their fixed queue order**

Change collected from a later customer cannot help an earlier transaction. The simulation must therefore process `bills` from left to right, maintaining only bills already received and not returned as change.

Only five- and ten-dollar bills are useful for future change:

- a five-dollar bill can help change a ten or twenty;
- a ten-dollar bill can help change a twenty;
- a twenty-dollar bill is larger than every required change and is never useful.

Variables `five` and `ten` track available counts. Twenty-dollar bills need not be stored.

**Customer pays five**

A five-dollar payment requires no change. The stand keeps it:

`five += 1`.

These bills are especially valuable because every ten-dollar customer requires one.

**Customer pays ten**

The customer needs five dollars change. The only possible bill is one five.

The source:

- increments `ten` because it receives the ten;
- decrements `five` for the change.

If no five was available, `five` becomes negative and the common failure check returns false.

The received ten cannot be used as change in the same transaction because the customer needs only five.

**Customer pays twenty**

The required change is fifteen. There are two possible combinations:

- one ten and one five;
- three fives.

The greedy rule uses a ten whenever available:

`if ten: ten -= 1; five -= 1`.

Otherwise, it uses:

`five -= 3`.

After either choice, a negative `five` means change was impossible.

**Why prefer one ten plus one five**

Both combinations give fifteen, but using a ten preserves two additional five-dollar bills.

Five-dollar bills are strictly more flexible:

- a future ten-dollar payment can be changed only with a five;
- a future twenty can use fives or a ten-plus-five;
- ten-dollar bills cannot replace a missing five for a ten-dollar customer.

Therefore, whenever a ten is available, spending it cannot make the future worse than spending three fives. It preserves the more universally needed denomination.

This exchange argument proves the greedy choice: if any successful plan used three fives while retaining a ten, replace that change with the ten and one five. The current customer still receives fifteen, and the stand has two more fives afterward, never reducing future possibilities.

**Why checking only `five < 0` is sufficient**

`ten` decreases only inside `if ten`, so it never becomes negative.

For a ten-dollar customer, the only possible shortage is a missing five. For a twenty-dollar customer, either branch also fails only by requiring more fives than available after any verified ten use.

Thus, the common negative-five test detects every impossible transaction.

**Trace the successful example**

For `[5,5,5,10,20]`:

- first three customers build `five=3`;
- the ten-dollar customer leaves `five=2,ten=1`;
- the twenty-dollar customer receives one ten and one five, leaving `five=1,ten=0`.

No count becomes negative, so every customer received correct change.

For `[5,5,10,10,20]`, the two ten-dollar customers consume both fives. At the twenty, tens exist but no five accompanies one; decrement makes `five=-1`, so the function returns false.

**Why successful simulation is sufficient**

At every step, the maintained counts describe actual bills held after a valid sequence of prior transactions. The greedy twenty-dollar exchange is future-optimal, so failing under it means no alternative change choice could have preserved more useful resources.

If the scan ends, every transaction was completed in queue order, proving the returned true.

The maintained counts also form a precise invariant: before each customer, `five` and `ten` equal the usable bills left after serving exactly the preceding customers with the greedy rule. Every branch first accounts for the received payment where relevant and then subtracts the chosen change. A negative five count is therefore not merely an arithmetic warning; it proves the current transaction demands a bill that the stand does not possess.

## Complexity detail

Let `n = len(bills)`. The loop visits each customer once and performs constant arithmetic and comparisons, so time is `O(n)`.

Only two counters and loop variables are stored, giving `O(1)` auxiliary space.

Bill values themselves do not affect complexity because the set of denominations is fixed by the contract.

## Alternatives and edge cases

- **Backtracking over change choices:** Only twenty-dollar payments offer two combinations, but the greedy exchange proof makes branching unnecessary.

- **Use three fives before a ten:** This can strand future ten-dollar customers and is never better.

- **First customer pays ten or twenty:** No five exists, the count becomes negative, and false is returned.

- **All customers pay five:** Counts only increase and the answer is true.

- **Twenty with ten but no five:** Ten-plus-five is impossible, and three fives are also impossible; false.

- **Twenty with no ten but three fives:** The fallback combination succeeds.

- **Twenty with both choices available:** Ten-plus-five preserves more fives.

- **Twenty-dollar bills held:** They are ignored because no future required change is at least twenty.

- **Queue order:** Transactions cannot be rearranged to borrow change from later customers.

- **Immediate failure:** Once a customer cannot receive change, later bills cannot repair that past transaction.

- **Input immutability:** The bill array is read in order and not modified.
