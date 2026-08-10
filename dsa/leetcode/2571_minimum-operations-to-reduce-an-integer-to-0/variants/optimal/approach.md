## General

**Think in binary runs of ones**

Subtracting a set power of two clears one isolated one bit in a single operation. For example, binary `100100` can be reduced by subtracting the two represented powers separately.

A consecutive run of several one bits offers a better description. A run from bit $a$ through bit $b$ has value

$$
2^a+2^{a+1}+\cdots+2^b=2^{b+1}-2^a.
$$

Instead of subtracting every set bit, add $2^a$ once and subtract $2^{b+1}$ once. The whole run is handled in two operations. For a long run this is much cheaper.

The main complication is that carrying into the zero above a run may join with a higher run. The solution scans from least significant bit to most significant bit and keeps this carry possibility alive.

**Meaning of `cnt` while scanning**

The loop examines the current least-significant bit with `n & 1`, then discards that bit with `n >>= 1`.

When a one is seen, `cnt` increases. It represents the length or accumulated status of the current consecutive block of ones in the transformed binary number, including a carry created from a lower run.

Nothing is charged immediately because the correct choice depends on what follows. A single one followed by zero is best cleared directly in one operation. Multiple consecutive ones may be better rounded upward through a carry, especially if the bit above the zero connects to more ones.

**What happens at a zero boundary**

When the current bit is zero and `cnt == 0`, there is no pending run, so the scan simply continues.

When `cnt == 1`, the pending block is an isolated one. The code increments `ans` once and sets `cnt = 0`. This corresponds to subtracting that one power of two. Carrying it upward would also require operations and offers no advantage at an empty boundary.

When `cnt > 1`, a multi-one run has ended. The code increments `ans` once for adding the power at the bottom of that run. Algebraically, this clears all run bits and creates one carried bit in the zero position immediately above them. It therefore assigns `cnt = 1` rather than zero.

That carried one is processed together with subsequent higher bits. If the next original bit is zero, the next loop boundary charges one operation to clear the carried singleton. If the next original bit is one, `cnt` becomes at least two, meaning the carry has merged into a higher run. This delayed decision is how the algorithm captures improvements spanning nearby runs.

The assignment is written compactly as

`cnt = 0 if cnt == 1 else 1`.

**Finish a run that reaches above the highest original bit**

After all original bits have been shifted away, `cnt` may still be nonzero.

If `cnt == 1`, one isolated highest bit remains and costs one subtraction, so `ans` increases by one.

If `cnt > 1`, the number ends in a top run of multiple ones. Add the power at the run's bottom to round it into one power above the top, then subtract that new power. This costs two operations, so `ans` increases by two.

No further carry interaction is possible because there are no higher original bits.

**Trace `n = 39`**

$39$ is binary `100111`. Scanning from the right first sees a run of three ones, so `cnt` becomes three. The following zero ends that run. One operation adds $2^0$, conceptually changing the low `111` into a carry at bit $3$; `ans` becomes one and `cnt` becomes one.

The next bit is zero, so the carried singleton is cleared with one operation, corresponding to subtracting $2^3$. The highest original one is then seen and, at loop end, costs one more subtraction of $2^5$.

The three operations match $39+1=40$, $40-8=32$, and $32-32=0$.

**Why the local choices are optimal**

An isolated one requires at least one operation because its coefficient must change from one to zero; subtracting its own power achieves that lower bound.

For a run of length at least two, clearing bits separately costs at least two operations, while the add-at-bottom and subtract-above representation costs exactly two before considering possible merging. Keeping the carry cannot be worse than resolving the run independently, and it may be better when it joins higher ones.

The scan performs precisely these optimal canonical choices from low to high. Operations on higher powers cannot selectively repair lower processed bits without introducing a carry captured by the same representation. Thus the algorithm constructs a minimum-weight signed-binary expression for $n$, where each positive or negative power corresponds to one allowed operation.

## Complexity detail

Each loop iteration shifts `n` right by one bit. A positive integer has $\lfloor\log_2 n\rfloor+1$ bits, so the loop takes $O(\log n)$ time. Every iteration performs constant work.

Only `ans`, `cnt`, and the shrinking integer `n` are stored, giving $O(1)$ auxiliary space. Reassigning the local integer does not affect any caller-owned object.

## Alternatives and edge cases

- **Breadth-first search over integer states:** BFS can find shortest paths for small bounds but explores many values and obscures the binary structure.
- **Subtract every set bit:** This uses the ordinary popcount operations but is suboptimal for long runs such as `1111`, which can be handled in two operations.
- **Recursive nearest-power choice:** Repeatedly moving toward a nearest power of two can work, but tie and carry cases require careful memoization or proof.
- **Power of two:** There is one isolated set bit, so the answer is one.
- **All-one binary number:** A number such as `1111` rounds up once and subtracts the new power once, giving two operations.
- **Two consecutive ones:** Clearing separately and rounding upward both cost two; retaining the carry is no worse and can merge with higher bits.
- **Separated isolated ones:** Each zero boundary resolves one pending singleton, matching the number of such bits.
- **Carry meets a higher one:** Keeping `cnt = 1` lets the next one extend the run instead of prematurely paying to clear both.
- **Positive-input guarantee:** The loop begins with at least one set bit; zero would correctly require no operations but is outside the contract.
- **Input rebinding:** Right shifts change only the local name `n` because Python integers are immutable.
