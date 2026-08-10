## General

**Separate unavoidable losses from one affordability reserve**

A transaction `[a,b]` changes money by `b-a`. If `a>b`, it permanently loses `a-b` money. If `a<=b`, it does not reduce money overall, though the user must still temporarily afford its cost `a`.

Let:

$$
S=\sum \max(0,a-b)
$$

over all transactions. This is the total net loss that can occur. The first source line computes exactly `S`.

Starting money must cover these losses plus enough remaining reserve to afford whichever transaction becomes hardest at the worst point of an arbitrary order.

**The bottleneck contribution is `min(cost, cashback)`**

For a losing transaction `a>b`, the loop considers `S+b`. Here `b = min(a,b)`.

For a non-losing transaction `a<=b`, it considers `S+a`. Here `a = min(a,b)`.

Thus, the returned expression is conceptually:

$$
S+\max_i\min(\texttt{cost}_i,\texttt{cashback}_i).
$$

The code writes the two cases explicitly to make their different affordability arguments visible.

**Why a losing transaction creates lower bound `S+b`**

Choose one losing transaction `[a,b]` and imagine an adversarial order that performs every *other* losing transaction before it, while postponing non-losing transactions that might add money.

The loss before this chosen transaction is:

$$
S-(a-b).
$$

If starting money is `M`, affordability requires:

$$
M-\bigl(S-(a-b)\bigr)\ge a.
$$

Rearranging gives:

$$
M\ge S+b.
$$

Therefore, every losing transaction's cashback can define a necessary reserve after all other losses.

**Why a non-losing transaction creates lower bound `S+a`**

For a transaction `a<=b`, imagine all losing transactions happen first. They consume total `S`. Before the non-losing transaction, the money can be as low as `M-S`, and it must still be at least cost `a`:

$$
M-S\ge a
\quad\Longrightarrow\quad
M\ge S+a.
$$

Taking the maximum of all these necessary bounds gives a global lower bound.

**Why that bound is sufficient for every order**

Let:

$$
X=\max_i\min(a_i,b_i)
$$

and start with `M = S + X`. Consider any arbitrary execution order. Non-losing transactions can only increase or preserve money, so for a lower-bound analysis they may be ignored. Let `L` be losses already suffered.

If the next transaction is non-losing `a<=b`, then `L<=S`. Current money is at least:

$$
M-L\ge S+X-S=X\ge a,
$$

because its minimum is `a` and `X` is the maximum of all minima.

If the next transaction is losing `a>b`, its own loss `a-b` has not happened yet, so:

$$
L\le S-(a-b).
$$

Current money is at least:

$$
S+X-\bigl(S-(a-b)\bigr)=X+a-b.
$$

For this transaction, `X>=b`, so this is at least `a`. The transaction is affordable.

Thus, `S+X` completes every transaction in every order. Combined with the lower bound, it is minimal.

**Trace the first example**

Transactions `[2,1]`, `[5,0]`, and `[4,2]` have losses one, five, and two, so `S=8`.

Their losing-case candidates are `8+1=9`, `8+0=8`, and `8+2=10`. The maximum is ten. Starting with less can fail when the transaction with cashback two is placed after the other losses; ten always works.

**Why cashback from profitable transactions is not counted as guaranteed help**

The requirement says *regardless of order*. An adversarial order may postpone every profitable transaction until after losses and an affordability bottleneck. Their gains cannot safely reduce required initial money.

The formula does not ignore their cost, however. For a non-losing transaction, that cost appears as the `S+a` reserve candidate.

**Total loss and temporary affordability are different needs**

The quantity `S` alone describes how much money may disappear after all losing transactions, but it does not guarantee that an expensive transaction can be started along the way. Conversely, keeping only the largest cost ignores money already consumed by earlier losses. The formula adds these two logically different obligations: `S` funds all irreversible decreases, while `X` is the largest residual balance that an adversarial position in the order can require. The proof above shows that `min(a,b)` is exactly the residual contribution for each transaction, not an arbitrary estimate.

## Complexity detail

Let $n$ be the number of transactions. Computing `S` scans the array once. The second loop scans it again and performs constant arithmetic and comparisons. Total time is $O(n)$.

Only `S`, `ans`, and current transaction values are stored. Auxiliary space is $O(1)$.

Sums may reach about $10^{14}$, so fixed-width implementations need 64-bit arithmetic. Python integers expand automatically.

## Alternatives and edge cases

- **One-pass accumulation:** Total loss and maximum `min(a,b)` can be accumulated together, then added. It has the same bounds.
- **Sort transactions:** Ordering is irrelevant to computing the worst-order guarantee; sorting adds unnecessary $O(n\log n)$ work.
- **All transactions non-losing:** `S=0`, and answer is the largest cost because an adversary may place that transaction first.
- **All transactions losing:** Answer is total loss plus the largest cashback.
- **Zero cost:** It is immediately affordable and may contribute zero as its minimum.
- **Zero cashback:** A losing transaction contributes no reserve beyond total loss.
- **Cost equals cashback:** It is non-losing and may require its full cost as reserve.
- **Profitable cashback:** Its future gain cannot be assumed before the transaction under arbitrary order.
- **Large total:** Use a wide integer type outside Python.
