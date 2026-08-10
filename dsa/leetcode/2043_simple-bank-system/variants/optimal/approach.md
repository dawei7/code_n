## General

**Map one-based account numbers to list indices**

Accounts are numbered from one through `n`, while Python lists are indexed from zero. Account `a` therefore has balance at `self.balance[a - 1]`.

The constructor stores `self.n = len(balance)` so every operation can validate the upper account boundary in constant time. It also stores the supplied list itself as `self.balance`.

This is a reference, not a copy. Successful transactions update the same list object that the caller passed to the constructor.

**Validate before changing state**

A failed transaction must return false and leave every balance unchanged. Each method performs all of its rejection checks before its first mutation.

The input contract guarantees account arguments are at least one, so the exact source checks only whether an account is greater than `n`. Under the contract, this completely validates the range. If zero or a negative account were supplied outside the contract, Python negative indexing could access an unintended account; the implementation relies on the stated lower-bound guarantee.

**Transfer between two accounts**

`transfer(account1, account2, money)` has three failure conditions:

- `account1` does not exist;
- `account2` does not exist;
- the source account balance is smaller than `money`.

The compound `or` condition short-circuits from left to right. If an account is too large, Python does not proceed to an unsafe balance lookup for that account.

When all conditions pass, the method subtracts `money` from `account1 - 1` and adds the same amount to `account2 - 1`, then returns true.

The total money across all accounts is unchanged by a transfer because the debit and credit are equal.

**Why the transfer is atomic at method level**

Both account validations and the sufficient-funds check occur before the debit. Therefore a missing destination cannot cause money to be removed from the source, and insufficient funds cannot cause a partial credit.

After validation, ordinary single-threaded execution applies the two list assignments consecutively. The challenge does not define concurrent calls, persistent storage failures, or external transaction rollback, so this method-level validation is the required atomic behavior.

**Deposit**

`deposit(account, money)` needs only to verify that the account exists. A deposit does not remove funds from another account, so there is no balance sufficiency condition.

On success it adds `money` to the indexed balance and returns true. On an invalid account it returns false without mutation.

**Withdraw**

`withdraw(account, money)` checks both account existence and whether the current balance is at least `money`. Equality is allowed: withdrawing an account's entire balance leaves zero.

On success it subtracts the amount and returns true. On failure it returns false without changing the list.

**Trace the example**

Starting balances are `[10,100,20,50,30]`. Withdrawing ten from account three is valid because its balance is twenty, leaving ten.

Transferring twenty from account five to account one changes their balances from thirty and ten to ten and thirty. Depositing twenty back into account five restores its balance to thirty.

Attempting to transfer fifteen from account three fails because that account now holds only ten. Neither account three nor account four changes. Attempting to withdraw from account ten fails the account-bound check because only five accounts exist.

**Representation invariant**

After every completed operation, `self.balance[i]` is the current balance of account `i+1`. Balances never become negative because both operations that subtract money first verify sufficient funds.

Deposits increase exactly one balance. Withdrawals decrease exactly one. Transfers preserve the total while moving the requested amount between exactly two indexed accounts.

The constructor establishes the mapping, and each successful method preserves it. Failed methods perform no mutation, so they preserve it as well.

**Same-account and zero-money operations**

If `account1 == account2` and the balance is sufficient, transfer subtracts and then adds the same amount to the same list entry. It returns true and leaves the balance unchanged. This is a valid transaction under the given rules.

The constraints allow `money=0`. Every existing account has enough funds for zero, so zero deposits, withdrawals, and valid-account transfers return true without changing balances.

**Large balances**

Repeated deposits can make an account exceed the original input bound. Python integers grow as needed, so arithmetic does not overflow a fixed 64-bit container in this implementation.

## Complexity detail

Each method performs a fixed number of comparisons, list accesses, and arithmetic assignments. `transfer`, `deposit`, and `withdraw` each run in $O(1)$ time per call.

The bank object retains a balance list of $N$ entries and one integer count, so its represented state is $O(N)$. Because the constructor stores the caller's list by reference rather than copying it, it does not allocate another $O(N)$ list at initialization; nevertheless, the persistent bank state it owns conceptually contains $N$ balances. Each operation uses $O(1)$ additional space.

## Alternatives and edge cases

- **Copy the input list:** `self.balance = balance.copy()` would isolate bank state from caller mutations but differs from the exact source.
- **Dictionary by account number:** Supports sparse identifiers, but consecutive one-through-$n$ accounts make a list simpler and faster.
- **Helper validation method:** Can centralize `1 <= account <= n` checks; the source relies on the contractual lower bound.
- **Nonexistent source account:** Transfer returns false before indexing its balance.
- **Nonexistent destination account:** Transfer returns false before any debit.
- **Insufficient funds:** Transfer and withdrawal return false without partial changes.
- **Exact available balance:** The operation succeeds and may leave zero.
- **Same source and destination:** A sufficiently funded transfer succeeds with no net balance change.
- **Zero money:** Valid existing-account operations succeed and leave state unchanged.
- **Large accumulated balance:** Python integer arithmetic avoids overflow.
- **External mutation:** Because the original list is retained by reference, caller changes to that list also affect bank state.
- **Account zero outside the contract:** The source would use negative indexing; correctness depends on the guaranteed positive account numbers.
- **No concurrency model:** The implementation provides sequential in-memory transaction semantics only.
