# Guided Example: Counter

## 1. What the Contract Actually Fixes

A factory operation receives one integer start value and hands back a function. That returned function is the real object of study: its first invocation must produce the start value itself, and every later invocation must produce exactly one more than the value it produced on the preceding invocation. Invoking it $m$ times therefore emits

$$n,\; n+1,\; n+2,\; \dots,\; n+m-1 .$$

Two facts are fixed by the statement and one is left open. Fixed: the first emitted value is the start value `n` itself, never `n + 1`; and the step between consecutive emissions is exactly $1$, never a quantity derived from the input. Open: how many invocations will occur, because the schedule arrives beside the start value and its length $m$ may be anything from $0$ up to the documented limit. The method must produce the progression lazily, one value per invocation, rather than preparing a fixed list of answers up front.

The instance traced here starts at `n = -2` with five scheduled invocations, so five values are owed. The negative start is deliberate: a progression that begins below zero and then crosses it exercises the register arithmetic without adding any special case for sign.

| Part of the input | Value for this instance | What it fixes |
|---|---|---|
| Start value `n` | `-2` | the first emitted value, and the origin of the progression |
| Invocation schedule | `["call","call","call","call","call"]` | that exactly $m = 5$ invocations occur, in this order |
| Required output | `[-2,-1,0,1,2]` | that the $k$-th emitted value equals $n + (k - 1)$ |

## 2. Why No Stateless Function Can Work

A function that kept nothing between invocations would derive its answer from the same untouched input every time. With start value `-2` it would emit `-2` on all five invocations, giving `[-2,-2,-2,-2,-2]`, whereas the contract requires `[-2,-1,0,1,2]`. That design is already wrong at the second invocation, and the gap between the two answers is exactly the information the method must carry: one integer register holding the value the next invocation owes the caller.

This is the whole algorithmic content of the problem. There is no search, no ordering decision, and no optimisation. There is one piece of private state and a two-phase discipline that every invocation follows without exception:

1. **Emit:** report the value the register currently holds.
2. **Advance:** replace the register's contents with that value plus one, so the next invocation owes a larger number.

The register lives between invocations rather than inside them. In language terms the returned function is a closure over the register: it keeps referring to that storage, so the storage survives each call and is never rebuilt. The register is written once, when the factory runs; nothing afterwards may re-initialise it.

```mermaid
accTitle: Counter register state machine
accDescr: The factory initialises one private register, and each invocation emits the stored value before advancing the register by one, so invocations repeat the emit-then-advance cycle indefinitely.
flowchart TD
    A["Factory runs with start value n"] --> B["Private register is set to n"]
    B --> C["An invocation arrives"]
    C --> D["Emit the value the register currently holds"]
    D --> E["Store that value plus one in the register"]
    E --> C
```

The order of those two phases is the entire correctness argument of the next section, and it is also the most common way a submitted design breaks.

## 3. Step-by-Step Execution of the Chosen Instance

Write $s_k$ for the register's contents immediately before the $k$-th invocation. The single initialisation gives $s_1 = n$, and the two-phase discipline gives the recurrence

$$s_{k+1} = s_k + 1 \quad \text{for every } k \ge 1, \qquad \text{emitted value at invocation } k = s_k .$$

Unrolling it yields the closed form $s_k = n + (k - 1)$, which is exactly the progression the contract demands. The trace walks the five invocations and checks each emission against that form.

| Invocation $k$ | Register before, $s_k$ | Value emitted | Register after, $s_{k+1}$ | Required $n + (k - 1)$ |
|---|---|---|---|---|
| 1 | $-2$ | `-2` | $-1$ | $-2 + 0 = -2$ |
| 2 | $-1$ | `-1` | $0$ | $-2 + 1 = -1$ |
| 3 | $0$ | `0` | $1$ | $-2 + 2 = 0$ |
| 4 | $1$ | `1` | $2$ | $-2 + 3 = 1$ |
| 5 | $2$ | `2` | $3$ | $-2 + 4 = 2$ |

The emitted column equals `[-2,-1,0,1,2]`, the required output, and no value is produced twice. The third invocation emits `0`, a legitimate emission that a design treating zero as "no value yet" would silently drop. The crossing from `-1` through `0` to `1` needs no branch. After the fifth invocation the register holds $3$, which the schedule never observes: the answer is the sequence of reads, not the final register contents.

## 4. The Invariant and Why the Reasoning Is Correct

**Invariant.** Immediately before the $k$-th invocation, the private register holds $s_k = n + (k - 1)$, where $n$ is the start value captured by the factory.

**Base case.** The factory performs exactly one write, setting the register to `n`, and returns before any invocation can occur. Nothing has advanced it, so the register holds $n = n + (1 - 1)$ before the first invocation, and the invariant holds at $k = 1$.

**Inductive step.** Assume $s_k = n + (k - 1)$ at some invocation $k$. The emit phase reports the register unchanged, so the value handed to the caller is $n + (k - 1)$, precisely the value the contract requires at position $k$. The advance phase stores $s_{k+1} = s_k + 1 = n + (k - 1) + 1 = n + k = n + ((k + 1) - 1)$, which is the invariant at $k + 1$.

By induction the invariant holds at every invocation, so every emitted value equals the required $n + (k - 1)$ and the method is sound. It is also complete: each invocation emits one value and advances the register once, so $m$ invocations emit exactly $m$ values and no required position is skipped.

Two properties follow from where the register lives rather than from its arithmetic.

- **Irreversibility.** The register is only replaced by its own successor, so the emitted sequence is strictly increasing with common difference $1$ and no value can repeat.
- **Privacy.** The register belongs to one factory run, so two counters created with different start values cannot interfere; a register kept in a shared location passes a single-counter test and fails as soon as two counters coexist.

## 5. Traps Exposed by This Instance

| Trap | What the defective handling produces | What this instance demonstrates |
|---|---|---|
| Advancing before emitting | the emissions are shifted by one, giving `[-1,0,1,2,3]` | the required first value `-2` never appears, and a sixth value `3` appears in a five-invocation run |
| Recomputing the answer from `n` on each invocation | every invocation emits `-2`, giving `[-2,-2,-2,-2,-2]` | the schedule asks for five distinct values, so a stateless answer is wrong from the second invocation onward |
| Keeping the register in a shared location | a second counter continues from the first counter's leftover value | the leftover $3$ in this trace would become another counter's first emission instead of its own start value |
| Special-casing negative start values | a branch that moves toward zero for negatives and away from zero for positives | `-2` advances to `-1` and then past zero to `1`, so the step is $+1$ for every sign |
| Assuming emitted values stay inside the documented start range | clamping or rejecting values above the largest start value | a start value of `1000` with three invocations owes `[1000,1001,1002]` |

The first two rows are the decisive ones and are the same defect seen twice: a method that never carries the register forward, and one that carries it forward at the wrong moment. Both return a plausible list of integers of the right length, which is why the trace is checked value by value rather than by counting elements.

## 6. Boundary Instances and Their Expected Outputs

The documented limits bound the start value and the number of invocations, not the values emitted.

| Start value `n` | Invocation schedule | Required output | What the instance establishes |
|---|---|---|---|
| `0` | one invocation | `[0]` | zero is a legitimate emission and must not be suppressed as a missing result |
| `-1000` | two invocations | `[-1000,-999]` | the lowest documented start value advances normally, with no floor at zero |
| `1000` | three invocations | `[1000,1001,1002]` | emissions are not confined to the documented start range |
| `95` | ten invocations | `[95,96,97,98,99,100,101,102,103,104]` | the register is never reset between invocations, and the emissions stay in order |
| `7` | no invocations | `[]` | an uninvoked counter emits nothing at all |

With no invocations the register is initialised and never read, so the answer is the empty list, not a one-element list. With at most $1000$ invocations from a start of at most $1000$, the largest possible emission is $1000 + 999 = 1999$ and the smallest is $-1000$, so no overflow reasoning is needed anywhere in the method.

## 7. Alternative Designs and Why They Are Eliminated

| Design | Auxiliary space | Verdict |
|---|---|---|
| Stateless recomputation from the start value | $O(1)$ | unsound: it emits the start value on every invocation instead of advancing |
| Remember only how many invocations have occurred | $O(1)$ | sound and equivalent: the $k$-th emission is $n + (k - 1)$, so the same invariant is carried by a differently labelled register |
| Remember every value already emitted | $O(m)$ | sound but wasteful: a single integer already determines the next value, and the stored history is never read again |
| Keep the register outside the returned function | $O(1)$ | sound for one counter only; counters created later would inherit a stranger's position rather than their own start value |
| Precompute the whole progression before the first invocation | $O(m)$ | impossible in general: the number of invocations is unknown to the factory, which has already returned before any invocation occurs |

The second row is the only genuinely interchangeable alternative, because storing the next value and storing the invocation count are two encodings of the same information related by $s = n + (k - 1)$. One integer is also necessary rather than merely sufficient: the value owed at invocation $k$ depends on the previous emission alone, and $k$ itself is unknown until the invocation arrives.

## 8. Time and Auxiliary Space Complexity

Every invocation performs a fixed amount of work regardless of the start value, the invocation index, or the schedule length.

| Phase | Work performed | Cost |
|---|---|---|
| Emit | the stored integer is reported to the caller | $O(1)$ |
| Advance | one integer addition and one store into the register | $O(1)$ |
| Total for one invocation | both phases together | $O(1)$ |

With $m$ invocations the total running time is $O(m)$, and that is optimal rather than merely acceptable: the output contains $m$ values and each must be produced by its own invocation, so no method can beat one unit of work per emitted value. For the traced instance $m = 5$, and the trace above is exactly five emit-and-advance pairs.

Auxiliary space is $O(1)$: the only storage the method owns is the single register, whose size does not depend on $m$. The emitted values are output rather than auxiliary storage, so the result list never counts against working memory. Writing $T$ for time and $S$ for auxiliary space,

$$T(m) = O(m), \qquad S(m) = O(1).$$

The limits $0 \le m \le 1000$ keep both bounds small in practice, but their shape is the real result: memory stays constant precisely because the register is the only information that must survive an invocation boundary.