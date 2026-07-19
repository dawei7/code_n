## General
**Align storage with 1-based account numbers**

Store a sentinel before the initial balances, making the list index equal to
the public account number. An account is valid exactly when it lies from `1`
through `N`. This avoids repeating index subtraction and gives direct constant-
time balance access.

**Validate every condition before mutation**

A deposit checks only its destination account. A withdrawal checks its account
and available balance. A transfer must validate both accounts and sufficient
source funds before changing either entry. Performing all checks first makes a
failed operation atomic: it cannot debit a valid source before discovering an
invalid destination.

**Apply the corresponding balance updates**

After validation, deposit adds to one entry, withdrawal subtracts from one
entry, and transfer subtracts from the source and adds the same amount to the
destination. These updates exactly implement each transaction. Balances never
become negative because every outgoing operation checks available funds, and
rejected operations preserve the preceding state, so every later result is
based on precisely the valid transaction history.

## Complexity detail
Constructing the 1-based balance list takes $O(N)$ time and space. Each account
validation, lookup, comparison, and update uses a constant number of direct
array operations, so every transaction takes $O(1)$ time. The stored balances
occupy $O(N)$ space.

## Alternatives and edge cases
- **Dictionary by account number:** A hash map also gives expected $O(1)$
  operations but adds overhead when valid account numbers are dense.
- **Linear account records:** Searching a list of account-number/balance pairs
  for every transaction is correct but costs $O(N)$ per call.
- Account `0` and every account above `N` are invalid.
- Transferring to an invalid destination must not debit a valid source.
- An outgoing amount exactly equal to the source balance is valid.
- A zero-money transaction is valid when all referenced accounts exist.
- Transferring from an account to itself is valid and leaves its balance
  unchanged.
- Balances can grow beyond $10^{12}$ after deposits, so fixed-width
  implementations need a wide integer type.
