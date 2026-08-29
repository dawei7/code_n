## General

**A toggle is parity, not a full history**

Every bulb begins off. Toggling one bulb twice returns it to off:

`off -> on -> off`.

Three toggles leave it on again. Therefore the final state depends only on whether its occurrence count in `bulbs` is odd or even:

- even count means off;
- odd count means on.

The order of toggles for different bulbs does not affect this conclusion because each operation changes only its named bulb.

**Use one fixed state slot per bulb number**

There are exactly 100 bulbs, numbered 1 through 100. The source creates:

`st = [0] * 101`.

Index `b` directly represents bulb `b`. Index 0 is unused, making the array indices align with the one-based bulb labels.

A zero means off and a one means on.

For every toggle number `x`, the source executes:

`st[x] ^= 1`.

XOR with 1 flips a binary state:

$$
0\mathbin{\mathrm{xor}}1=1,
\qquad
1\mathbin{\mathrm{xor}}1=0.
$$

This exactly simulates the operation without branches.

**Why the state equals occurrence parity**

Initially every `st[b]` is zero, matching zero occurrences.

Each occurrence of bulb `b` flips `st[b]` and changes the occurrence count's parity from even to odd or odd to even. By induction, after every processed operation:

$$
\texttt{st}[b]=C(b)\bmod2.
$$

When all operations are processed, a stored one identifies exactly an odd-count bulb, which is exactly a bulb left on.

**Produce sorted output by scanning indices**

The return comprehension uses:

`[i for i, x in enumerate(st) if x]`.

`enumerate` visits indices 0, 1, 2, and so on through 100. Selecting indices whose state is one automatically produces ascending numeric order.

Index 0 cannot appear because it is initialized to zero and valid input never toggles it.

No explicit sort is required.

**Trace the first example**

For `[10,30,20,10]`:

- the first 10 changes `st[10]` from 0 to 1;
- 30 changes `st[30]` to 1;
- 20 changes `st[20]` to 1;
- the second 10 changes `st[10]` back to 0.

The final scan encounters on bulbs 20 and 30 in that order, returning `[20,30]`.

For `[100,100]`, the first occurrence turns bulb 100 on and the second turns it off. No state is one, so the comprehension returns an empty list.

**Why counting full frequencies is unnecessary**

The final condition needs only frequency modulo 2. Storing a potentially larger count and taking modulo later would work, but each XOR update performs that reduction immediately.

The fixed state array also avoids hashing overhead and guarantees that output order follows the bulb labels.

**The fixed universe makes both storage and ordering simple**

In a problem with arbitrary bulb identifiers, an array indexed by identifier could waste unbounded space. Here the universe is permanently limited to 1 through 100. Reserving 101 slots is therefore a true constant, not an $O(\max(\texttt{bulbs}))$ structure that grows with input values.

This same representation solves two tasks at once. Direct access makes each toggle constant time, while numeric array order supplies the requested sorted result. A hash set would also represent odd parity, but its iteration order would not provide the contractual ascending order.

The source stores integers rather than physical strings such as `"on"` and `"off"`. This lets XOR express the state transition algebraically and makes the parity invariant visible in the data itself.

## Complexity detail

Let $N=\lvert\texttt{bulbs}\rvert$. Processing the operations costs $O(N)$. Scanning the fixed 101 slots costs $O(101)$, which is $O(1)$ with respect to $N$. Total time is $O(N+100)=O(N)$ under the fixed domain.

The state array always contains 101 integers, regardless of input length, so auxiliary space is $O(1)$. The output can contain at most 100 bulb numbers and is also bounded by the fixed domain.

## Alternatives and edge cases

- **Toggle membership in a set:** Add an absent bulb and remove a present bulb, then sort the set. This uses up to 100 entries and adds an $O(B\log B)$ final sort for $B$ on bulbs.
- **Counter frequencies:** Count every bulb and filter odd values. It stores more information than needed and still requires ordering the keys.
- **Boolean negation:** `st[x] = not st[x]` also flips state, though it changes entries from integers to booleans; XOR keeps the explicit parity representation.
- **Every bulb toggled an even number of times:** All states return to zero and the result is `[]`.
- **Repeated odd count:** Any odd number of toggles leaves the same final on state as one toggle.
- **Bulb one and bulb 100:** Direct indexing includes both valid boundary labels.
- **Unused index zero:** It remains off and is filtered from the enumerated result.
- **Already sorted requirement:** Scanning the fixed state array from low to high satisfies it without sorting.
- **Single toggle:** That bulb alone is returned.
- **Input length at most 100:** The fixed-domain method remains valid even if the same bulb appears many times.
