## General

**Store inventory in the contract's denomination order**

The ATM has exactly five denominations. `self.d = [20, 50, 100, 200, 500]` stores their values, and `self.cnt` stores available counts at matching indices. `self.m` is five.

This parallel layout means index zero always refers to twenty-dollar notes and index four to five-hundred-dollar notes. Returned withdrawal arrays must use the same order.

The constructor initializes every count to zero, matching an empty ATM.

**Deposit is component-wise addition**

`deposit` enumerates the five supplied counts and adds each to the corresponding inventory slot:

`self.cnt[i] += x`.

Deposits never replace existing notes; they accumulate. Zero entries leave a denomination unchanged. Because the input order is guaranteed, no denomination lookup is needed.

**Withdrawal must obey mandated greedy priority**

This is not a general “find any combination of notes” problem. The ATM is required to try larger denominations first, even when that choice later makes the request fail.

`reversed(range(self.m))` visits indices four down to zero, corresponding to values `500, 200, 100, 50, 20`. For denomination `self.d[i]`, the machine could use at most `amount // self.d[i]` notes without exceeding the current remainder, but it may own fewer. Therefore, it selects

`min(amount // self.d[i], self.cnt[i])`.

That count is stored in `ans[i]`, and its value is subtracted from `amount`.

Taking the maximum possible count at every denomination exactly implements “prioritizes using banknotes of larger values.” The algorithm must not backtrack to replace a selected large note with smaller ones.

**Stage the withdrawal before changing inventory**

During the greedy pass, `ans` records a proposed combination, but `self.cnt` remains untouched. If the remaining `amount` is positive after all five denominations, the greedy policy could not form the request. The method returns `[-1]` immediately.

Because no inventory count was decremented during planning, a failed withdrawal is atomic: the ATM contains exactly the same notes afterward.

If the remainder is zero, the plan succeeded. Only then does the second loop subtract every `ans[i]` from `self.cnt[i]` and return the five-element plan.

This two-phase design avoids the need to roll back partially selected notes.

**Why the selected plan follows the policy**

At denomination `v`, all larger denominations have already been fixed. The mandated policy requires using as many `v` notes as possible without exceeding the current remainder or inventory. The `min` expression is precisely that number.

Inductively, after every iteration, the plan agrees with the required greedy decision for every denomination processed so far. When the pass ends, `ans` is the unique count vector produced by this deterministic priority rule, apart from indistinguishable physical notes of the same value.

If its remainder is zero, the note values sum to the requested original amount and counts never exceed inventory. If not, the policy says rejection is correct even if a different non-greedy combination exists.

**Trace the intentional rejection**

Suppose the ATM has one `500` note and three `200` notes and the request is `600`. It must take the `500` note first, leaving `100`. With no usable notes to make that remainder, it rejects.

Three `200` notes could total `600`, but choosing them would violate the larger-first rule. The exact implementation correctly returns `[-1]` and retains all notes.

**Persistent object state**

`self.cnt` survives across method calls. Successful withdrawals reduce it, failed withdrawals do not, and deposits increase it. The denomination list never changes.

Large note counts are safe in Python integers. The fixed five-entry structures do not grow with the number of calls.

## Complexity detail

Each deposit visits exactly five positions. Each withdrawal performs one five-denomination planning pass and, on success, one five-position commit pass. Every individual operation is therefore `O(1)` time because the denomination count is fixed.

Across `Q` total method calls, total time is `O(Q)`, matching the manifest. The ATM stores two five-element lists and a few scalars, so persistent and auxiliary space are `O(1)`.

The returned successful list always has five entries; failure returns the one-entry sentinel `[-1]` exactly as required.

## Alternatives and edge cases

- **General coin-change search:** It could find a combination that succeeds when greedy fails, but that would violate the ATM's mandated behavior.
- **Backtracking after a greedy dead end:** The `600` example explicitly forbids replacing the selected `500` with three `200` notes.
- **Mutate inventory during planning:** This requires rollback on failure and risks corrupting state. Staging `ans` keeps failure atomic.
- **Deposit zero notes:** The corresponding inventory counts remain unchanged.
- **Withdraw more value than total inventory:** A positive remainder remains and the call returns `[-1]` without modification.
- **Exact large-note match:** The greedy pass uses that note and succeeds immediately for the remaining lower denominations.
- **Insufficient low denominations after large selection:** The request fails even if a smaller-note alternative existed before selecting the large note.
- **Successful withdrawal:** Every used count is subtracted exactly once during commit.
- **Repeated calls:** Each sees the state left by all prior successful operations and deposits.
- **Denomination order:** Internal storage and returned arrays are ascending even though withdrawal processing is descending.
- **Amount not divisible by any available combination:** The nonzero remainder detects failure.
- **Fixed denomination count:** Constant-time claims rely on exactly five supported values.
