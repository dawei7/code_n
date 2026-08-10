## General

**Store every encountered chain value**

The competitive method uses dictionary `lookup` as a visited-state set. A key
is present when that integer has already been transformed. Its stored value is
always `True` and is never otherwise inspected, so a Python `set` would express
the intent more directly.

The outer loop continues only while current `n` is not 1 and is absent from the
dictionary. It records the current state, computes its digit-square successor,
and repeats.

**Compute the successor through decimal text**

Helper `nextNumber` converts the positive integer to `str(n)`. Iterating that
string visits each decimal digit from left to right. `int(char)` converts one
digit character back to its numeric value, `**2` squares it, and accumulator
`new` sums the squares.

Digit order is irrelevant because addition is commutative. Numerical `divmod`
would avoid creating a string, but the textual version follows the definition
closely and is easy for a beginner to read.

The Reference guarantees positive input, so the string contains digits only.
Negative input would include `'-'`, which `int(char)` could not convert in this
per-character loop; that domain is intentionally excluded.

**Trace 19 step by step**

Dictionary starts empty. The loop records 19, and `nextNumber` calculates
$1^2 + 9^2 = 82$. It records 82 and obtains 68, records 68 and obtains 100,
then records 100 and obtains 1.

The next condition sees `n == 1`, stops, and returns true. The dictionary is
used only to guard against cycles; it does not contribute to the numeric sums.

**Detect an unhappy number through repetition**

For an unhappy input, deterministic digit-square transitions eventually enter
a cycle. The first trip around that cycle records every member. When the chain
returns to its entry point, `n in lookup` becomes true, so the loop stops.

Because current `n` is not 1, the final expression returns false. There is no
need to find where the cycle began or how long it is; one repeated state proves
the future will repeat forever.

**Why eventual repetition is guaranteed**

A $d$-digit integer maps to at most $81d$. Under the maximum signed 32-bit
input, $d \le 10$, so the first successor is no greater than 810. Values in
that small region continue mapping within another bounded region.

There are finitely many possible states there. Since each state has exactly one
successor, the chain must either encounter 1 or revisit a state. It cannot keep
creating larger distinct values indefinitely.

**Why all true results and false results are justified**

Returning true happens only after the actual transition sequence reaches 1,
which is the definition of happiness.

Returning false happens only after detecting a repeated non-1 integer. The next
value from that integer is always the same, so the repeated suffix forms a
cycle. If that cycle contained 1, the loop would have stopped at 1 before the
repeat test caused a false return. The cycle therefore excludes 1.

**Complexity comments need the cost of each transition**

The source comment says time and space are $O(k)$ where $k$ is the number of
steps. That counts transitions but treats converting and scanning each integer
as constant. The first transition scans $O(\log n)$ decimal digits, and each
dictionary key is an integer whose representation also has a size.

For the fixed 32-bit contract, all representations are bounded and the chain
after one step enters a small constant domain. For arbitrary-size integers, a
more precise analysis includes digit-processing cost rather than only the
number of states.

**The exact variant does not match constant-state manifest wording**

The manifest summary describes Floyd's slow and fast pointers, and its space
bound is $O(1)$. The competitive source instead retains a dictionary of all
visited values. Fixed 32-bit bounds can make the maximum dictionary size a
large constant in a strict asymptotic convention, but the implementation is
still structurally history-based and uses more state as the chain grows.

This distinction matters pedagogically: the dictionary method detects a cycle
by memory, while Floyd detects it by different traversal speeds.

**Repeated-call considerations**

If many inputs are tested, one could cache known happy and unhappy states across
calls or hardcode the known non-happy cycle. The exact method creates a fresh
dictionary per call, so no result leaks across invocations and memory is
released afterward.

## Complexity detail

Let $d = O(\log n)$ be the initial decimal digit count. The first string
conversion and digit scan cost $O(d)$. The sequence then enters a bounded region
for the 32-bit domain, so total time is $O(\log n)$ in the manifest model.

The dictionary stores one entry per distinct visited state, which is $O(k)$ in
the source's chain-length notation. Under the fixed input range, $k$ is bounded
by a constant; under a generalized model, this is not the same implementation
as Floyd's $O(1)$ auxiliary state. Each string conversion also uses temporary
space proportional to the current digit count.

## Alternatives and edge cases

- **Visited set:** Store keys without redundant `True` values; same cycle-detection logic and asymptotic behavior.
- **Floyd's algorithm:** Uses two evolving values and no history collection, genuinely matching the manifest summary.
- **Numeric digit extraction:** Repeated `divmod(..., 10)` avoids allocating a decimal string.
- **Hardcoded cycle member:** Stop at 4 or 1 after proving all unhappy chains enter the known cycle.
- **Input 1:** Loop does not run and returns true.
- **Happy multi-step input:** Stops as soon as successor becomes 1.
- **Unhappy input:** Stops at the first repeated state, not after infinite work.
- **Positive-only domain:** Required by the per-character conversion's digit assumption.
- **Zeros in decimal text:** Convert to digit zero and add nothing.
- **Fresh dictionary:** Each call is independent but repeated calls do not share useful classification cache.
