## General

**Represent friends with zero-based indices**

The statement numbers friends from 1 through $n$, but Python arrays use indices zero through $n-1$.

The solution represents friend 1 by index zero. Array `vis` records whether each indexed friend has ever received the ball.

Only when building the returned list does the code convert an unvisited index `i` back to the problem's number `i + 1`.

**Track the current holder and turn multiplier**

Variable `i` is the index of the friend currently holding the ball. It starts at zero because friend 1 receives the ball initially.

Variable `p` is the current turn number and starts at one. On turn `p`, the ball moves `p * k` clockwise steps.

After calculating the next holder, `p` increments so the following pass uses the next multiple of `k`.

**Mark receipt before making the pass**

The loop condition is `while not vis[i]`. Entering the loop proves the current friend has not previously received the ball.

The code immediately sets `vis[i] = True`. This counts the initial possession by friend 1 and every later arrival.

It then calculates where that friend passes the ball. On the next condition check, the game stops if the destination was already marked.

This ordering matches the rule that the game finishes when someone receives the ball for the second time. That repeated recipient is not newly marked because it was already present.

**Use modular arithmetic for the circle**

Moving `p * k` steps clockwise from index `i` gives:

`i = (i + p * k) % n`.

Adding performs the clockwise movement on an unwrapped number line. Taking remainder modulo $n$ wraps index $n$ back to zero and supports movements longer than one full circle.

For example, with five friends, moving six steps from index one reaches:

$$
(1+6)\bmod 5=2,
$$

which is friend 3.

**Trace `n = 5` and `k = 2`**

Initially `i=0`, representing friend 1, and `p=1`.

- Mark friend 1. Move $1\cdot2$ steps to index 2, friend 3.
- Mark friend 3. Move $2\cdot2$ steps to index 1, friend 2.
- Mark friend 2. Move $3\cdot2$ steps to index 2, friend 3 again.

The next loop test finds `vis[2]` true and stops. Friends 4 and 5 were never marked, so the answer is `[4, 5]`.

**Trace a movement equal to the circle size**

For `n = 4` and `k = 4`, friend 1 is marked first.

The next index is:

$$
(0+1\cdot4)\bmod4=0.
$$

Friend 1 receives the ball again immediately. The loop ends, and friends 2, 3, and 4 are losers.

**Why the loop must terminate**

There are only $n$ friends. Each successful loop iteration marks one previously unvisited friend.

After at most $n$ such iterations, the next holder must be among the finite set already seen. The condition then fails. No separate turn limit is required.

This also proves the simulation performs at most linear work.

**Build losers in ascending order automatically**

The result comprehension scans indices with `range(n)`, which is increasing.

For every unvisited index, it appends `i + 1`. Therefore the output is already in ascending friend-number order and needs no sort.

Visited order may be irregular, but it has no influence on result order.

**The simulation invariant**

Before each loop test:

- `i` is the friend who has just received the ball;
- `p` is the number of the pass that this friend would make if it is their first receipt;
- `vis[j]` is true exactly for friends who received the ball earlier in the game.

If `vis[i]` is already true, the stopping event has occurred. Otherwise marking `i` and applying the modular pass produces the exact next state and increments the pass number.

By induction, the simulation follows every game transition until precisely the first repeated recipient.

**Why a set or Boolean array is necessary**

The game stops based on history, not merely the current position. A current index alone cannot reveal whether that friend appeared earlier.

The Boolean array supports constant-time membership checks and later exposes every loser. Since friend labels form a dense range, it is simpler than a hash set.


Every loop iteration corresponds to one first-time ball receipt and applies the rule's exact distance for the current turn. The loop ends exactly when the current recipient is repeated.

Consequently, `vis` is true exactly for all friends who received the ball at least once during the complete game. The final comprehension returns exactly the complement of that set, which is the definition of the losers.

## Complexity detail

At most $n$ friends can be marked before a repeat, so the simulation takes $O(n)$ time. Scanning `vis` to build the output takes another $O(n)$, leaving total time $O(n)$.

The visited array uses $O(n)$ space. The output can also contain $O(n)$ friend numbers. Variables `i` and `p` use $O(1)$ additional space.

## Alternatives and edge cases

- **Hash set of recipients:** Also supports $O(1)$ expected membership checks, but the dense Boolean array is simpler and helps enumerate losers.
- **Search prior positions after every move:** Avoids extra visited storage but can take $O(n^2)$ time.
- **Attempt a closed-form cycle analysis:** Possible number theory may characterize visits, but direct simulation is clearer within $n \le 50$.
- **One friend:** Friend 1 is marked, receives the ball again after wrapping, and there are no losers.
- **`k = n`:** The first pass returns to the current friend immediately.
- **Pass longer than one circle:** Modulo handles any multiple without repeated stepping.
- **Initial possession:** Friend 1 must be marked before the first pass.
- **Repeated recipient:** It was already marked from its first receipt and is not a loser.
- **Ascending output:** Scanning indices in order removes the need to sort.
- **One-based versus zero-based labels:** Convert only at output; modulo arithmetic stays zero-based.
- **Turn counter placement:** Increment after using `p` so the first pass is exactly `k` steps.
