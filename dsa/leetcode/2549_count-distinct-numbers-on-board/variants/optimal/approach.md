## General

**For `n>1`, every number from 2 through `n` eventually appears**

Start with `n` on the board. For any current number `x>=3`, choose:

$$
i=x-1.
$$

Then:

$$
x\bmod(x-1)=1,
$$

because $x=1\cdot(x-1)+1$.

Therefore, presence of `x` causes `x-1` to be added on the next day. Beginning from `n`, this creates the descending chain:

$$
n,\ n-1,\ n-2,\ldots,2.
$$

So all `n-1` integers in interval `[2,n]` appear after at most `n-2` days.

**Why one never appears**

For every integer `x`:

$$
x\bmod1=0,
$$

not one. The procedure can never add `i=1` from any board value.

When `n>1`, the final board therefore contains exactly 2 through `n` and excludes one.

**Why no value above `n` can appear**

The rule considers candidate `i` only in range `1<=i<=n`, where `n` is the original input bound. No operation can place a number outside that range.

Combined with the descending-chain inclusion and exclusion of one, this proves the final set exactly.

**The special case `n=1`**

Initially, number one is already on the board. The only candidate is also one, and `1%1=0`, so no new number is added.

The board retains its initial number forever and has one distinct value.

This is why the formula uses:

`max(1,n-1)`

rather than always returning `n-1`, which would give zero for `n=1`.

**Check `n=2`**

The board starts with 2. Candidates 1 and 2 give remainders zero, so nothing new is added. The final count is one.

Both `n-1` and `max(1,n-1)` correctly return one.

**Why a billion days are more than enough**

For `n<=100`, the guaranteed descending chain reaches 2 within at most 98 daily transitions. Once all values 2 through `n` are present, no value outside that already complete possible set can be added.

The board stabilizes long before $10^9$ days. Simulating the stated duration is unnecessary.

**Persistence matters**

Numbers remain on the board. When `x-1` is added, `x` is not removed. The descending process accumulates the entire interval rather than leaving only the latest number.

This persistence is why the final count is `n-1` rather than one for `n>2`.

**Other modulo relationships are irrelevant to the count**

A number may add several candidates in one day, possibly causing values to appear earlier than the simple chain predicts. That cannot expand the final set beyond `[2,n]` or remove any chain value.

The chain is an inclusion proof, not a claim that it is the only way values appear.

**Formal induction on the descending chain**

Base case: `n` is present initially.

Inductive step: assume some `x` with $3\le x\le n$ is present. The daily procedure examines that persistent `x` and candidate `i=x-1`, which lies in the permitted range. Since the remainder is one, `x-1` is placed on the board and remains there.

By induction, every integer from `n` down through two appears. This reasoning does not require each value to be added on a separate day; simultaneous extra additions only make the conclusion arrive sooner.

**Why stabilization is permanent**

Once board set is $\{2,3,\ldots,n\}$, any candidate newly considered still lies from one through `n`. Candidate one never qualifies, while every other candidate is already present. Future days can add nothing new.

The state is a fixed point of the process, so the billion-day result equals this early stabilized count.

**Another small example**

For `n=6`, chain witnesses are:

$$
6\bmod5=1,\quad
5\bmod4=1,\quad
4\bmod3=1,\quad
3\bmod2=1.
$$

The final board contains 2, 3, 4, 5, and 6: five values, which is `n-1`.


For `n>1`, induction using `x%(x-1)=1` puts every integer down to two on the board. Candidate limits prevent values above `n`, and modulo one prevents adding one. The final set has `n-1` elements.

For `n=1`, the initial board contains one element forever. The returned maximum formula handles both cases exactly.

## Complexity detail

The method evaluates one subtraction and one maximum operation, independent of `n` and day count. Time is $O(1)$.

It stores no growing collection or simulation state. Auxiliary space is $O(1)$.

The proof replaces a potentially enormous day-by-day process with a closed form.

## Alternatives and edge cases

- **Board simulation:** It would eventually stabilize for `n<=100` but is unnecessary and obscures the invariant.
- **`n=1`:** Initial one remains, so return one.
- **`n=2`:** Only two remains, also giving one.
- **`n>2`:** Final set is exactly `\{2,\ldots,n\}`.
- **Candidate one:** It never satisfies remainder one.
- **Candidate above `n`:** The rule never considers it.
- **Multiple additions per day:** They can accelerate stabilization but not change the final set.
- **Persistence:** Previously placed values are never removed.
- **Billion-day count:** It has no effect after early stabilization.
- **Closed form:** `max(1,n-1)` unifies both input regimes.
