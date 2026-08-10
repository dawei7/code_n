## General

**Model each croak as five ordered stages**

Every valid frog sound must pass through:

```text
c -> r -> o -> a -> k
```

Characters from different frogs may interleave, but an `r` must belong to a frog that previously emitted `c`, an `o` must continue a frog waiting after `r`, and so on. This can be validated by counting how many frogs currently wait at each stage.

The dictionary:

```python
idx = {c: i for i, c in enumerate('croak')}
```

maps `c`, `r`, `o`, `a`, and `k` to indices zero through four. `map(idx.get, croakOfFrogs)` then turns the input into that stage-index stream.

The constraints guarantee that every character is one of these five letters. Without that guarantee, `idx.get` could produce `None` and would need an explicit invalid-character check.

**A fast necessary length check**

Every completed croak has exactly five characters. A mixture of complete croaks must therefore have total length divisible by five:

```python
if len(croakOfFrogs) % 5 != 0:
    return -1
```

Divisibility is necessary but not sufficient. A string can contain the correct total counts and still present letters in an impossible order, so the stage scan remains essential.

**What the stage counts mean**

`cnt = [0] * 5` stores how many observed occurrences currently belong to each latest stage. For indices zero through three, `cnt[i]` can be viewed as frogs that have emitted the corresponding character and are waiting for the next one.

When stage `i` arrives, the code first increments `cnt[i]`. For every noninitial stage, it must also consume one waiting frog from `cnt[i - 1]`. This transfers a croak from the previous stage to the current stage.

The completed `k` count at `cnt[4]` is allowed to accumulate because no later character needs to consume it. Active concurrency is tracked separately.

**Starting a new croak**

When `i == 0`, the character is `c`. It begins a new active croak:

```python
x += 1
ans = max(ans, x)
```

`x` is the number of frogs currently partway through a croak. Every new `c` requires some frog to start or restart a sound. If a previously used frog has already finished, it is available, which is reflected by that completed croak having decreased `x` earlier.

`ans` records the maximum number simultaneously active at any prefix. That peak is the minimum number of distinct frogs needed.

**Advancing a noninitial character**

For `r`, `o`, `a`, or `k`, a frog must be waiting at the immediately preceding stage:

```python
if cnt[i - 1] == 0:
    return -1
```

If none exists, the character cannot be assigned to any valid ongoing croak. For example, an `o` cannot skip directly after `c`; it specifically needs an unmatched `r`.

When a predecessor exists, `cnt[i - 1] -= 1` consumes one. The already-executed `cnt[i] += 1` records its arrival at the new stage.

If `i == 4`, the character is `k` and that frog has completed its sound, so `x -= 1`. The same physical frog can handle a later `c`, which will increase `x` again but need not increase the historical maximum `ans`.

**Trace overlapping sounds**

For `"crcoakroak"`, the active counts evolve as follows:

| Character | Meaning | Active `x` | Peak `ans` |
|---|---|---:|---:|
| `c` | frog 1 starts | 1 | 1 |
| `r` | frog 1 advances | 1 | 1 |
| `c` | frog 2 starts | 2 | 2 |
| `o` | one frog advances | 2 | 2 |
| `a` | that frog advances | 2 | 2 |
| `k` | that frog finishes | 1 | 2 |
| `r,o,a,k` | the remaining frog finishes | 0 | 2 |

At one point two croaks are unfinished, so one frog cannot produce the observed interleaving. Two frogs suffice, making the peak both a lower bound and an achievable count.

**Why the peak active count is minimal**

At any input prefix with `x` unfinished croaks, those croaks must belong to `x` different frogs because a single frog cannot be at two positions of its sound simultaneously. Thus every valid assignment needs at least the maximum observed `x` frogs.

The stage-transfer process also gives a schedule using exactly that many. A new `c` can be assigned to any idle frog, or to a new frog if all currently counted frogs are busy. Every later character continues one frog waiting at its preceding stage. A `k` makes that frog idle. This assignment never needs more than the peak, so `ans` is attainable and minimal.

**Final completeness check**

Even if every observed transition was locally possible, the input is invalid when one or more croaks never reach `k`. At the end, such frogs remain active, so `x > 0`.

The return:

```python
return -1 if x else ans
```

rejects incomplete suffixes and otherwise returns the concurrency peak. Together with transition validation, `x == 0` means every started croak finished in order.

**Why the stage invariant proves validity**

Before each character, counts zero through three represent exactly the unfinished croaks waiting after each prefix of `"croak"`. A `c` creates a valid new one-stage prefix. Any later character is accepted only by extending a croak at the immediately preceding valid prefix. Therefore, no accepted assignment violates order. If the scan ends with no active croaks, those prefixes have all extended to full `"croak"` sequences, so the input is a valid interleaving.

## Complexity detail

Let $n$ be the string length. The algorithm performs one divisibility check and one left-to-right scan. Dictionary lookup, counter updates, and comparisons are constant time for each character, so total time is $O(n)$.

The dictionary always has five entries and `cnt` always has five integers. `ans`, `x`, and the current stage use constant storage. Thus auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Explicit five counters:** Separate variables for frogs after `c`, `r`, `o`, and `a` avoid indexing but duplicate transition code. The array expresses the same state uniformly.
- **Track a state per frog:** Assign characters to individual frog objects. It can work but may require searching for a frog at the needed stage, while aggregate counts contain all necessary information.
- **Repeatedly remove `"croak"` subsequences:** Extracting one frog at a time can become quadratic and makes minimum concurrency harder to derive.
- **Length divisible by five:** This alone does not prove validity; `"croakcrook"` has ten characters but contains an impossible stage order.
- **Sequential croaks:** `"croakcroak"` reaches active count one, returns to zero, and reuses the same frog.
- **Fully overlapping starts:** A prefix with several `c` characters raises the active count and therefore the required number of frogs.
- **Character without predecessor:** An initial `r` or an `o` with no waiting `r` immediately returns -1.
- **Incomplete final croak:** A suffix such as `"cro"` leaves `x` positive and is rejected at the end.
- **Single complete croak:** All five transfers succeed, the peak is one, and final active count is zero.
- **Tied stage populations:** Counts may contain several frogs at the same stage; any one can consume the next matching character because frogs are indistinguishable for counting.
