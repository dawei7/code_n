## General

**A suffix flip changes only the current effective bit**

Process target positions from left to right. Once position `i` is fixed, every later operation must start after `i`; otherwise, it would flip that position again and destroy the match.

Therefore, at each position there is a forced decision: if the current effective bit already equals the target bit, do nothing. If it differs, a flip must start exactly here. Starting later cannot repair this position, and starting earlier is no longer allowed if the previous prefix is to remain correct.

This greedy decision is both necessary and sufficient.

**Representing all previous flips by parity**

The initial source bit at every position is zero. Every suffix flip started at an earlier or equal index affects the current position. Applying an even number of flips leaves zero; applying an odd number changes it to one.

`ans` is the number of flips chosen so far, so `ans & 1` is the effective current source bit before deciding at this position.

The target character `v` is converted with `int(v)`. The expression

`(ans & 1) ^ int(v)`

is one exactly when the current effective bit and desired bit differ. XOR of equal bits is zero; XOR of different bits is one.

When they differ, `ans += 1` starts a suffix flip at this position. That immediately fixes the current bit and toggles the effective state for every later position.

**A transition-based viewpoint**

The initial effective value before the string is zero. A new flip is needed every time the desired target value differs from the effective value established by prior flips.

After a flip, that effective value becomes the current target bit. Thus the answer is the number of value transitions when the target is imagined with a leading zero.

For `target = 101`, values move from initial zero to one, then to zero, then to one. There are three transitions, so three flips are necessary.

For an all-zero target, there is no transition from the initial zero and the answer remains zero.

**Why the left-to-right greedy choice is optimal**

Suppose position `i` is the first mismatch. Any operation capable of changing it must start at an index no greater than `i`. Starting below `i` would miss it. Starting before `i` would also flip some already-correct earlier position.

The only feasible first operation that preserves the fixed prefix is therefore a suffix flip beginning at `i`. The algorithm performs exactly that forced operation.

If there is no mismatch, flipping here would make the current position wrong and require another later-impossible repair of that same position. Doing nothing is forced.

By induction over positions, the algorithm uses the unique necessary choice at each boundary and hence the minimum possible number.

**Why no actual string is maintained**

A suffix flip can cover up to $N$ positions. Physically toggling those characters for every operation could cost quadratic time.

Only the parity of flips affecting the unprocessed suffix matters. `ans & 1` summarizes that state in one bit, while `ans` itself also stores the final count.

**Tracing target 10111**

At the first character, effective zero differs from one, so flip count becomes one and future effective value is one. At the next character, desired zero differs, so count becomes two and effective value returns to zero.

The next desired one causes a third flip. The remaining desired ones match the odd flip parity, so no more operations are needed. The result is three.

Every increment therefore corresponds to one unavoidable boundary in the target.

## Complexity detail

Let $N$ be target length. The loop examines each character once and performs constant-time bit and integer operations. Time is $O(N)$.

Only `ans` and the current character are stored, so auxiliary space is $O(1)$, matching the manifest. The algorithm never constructs the initial zero string or a modified target copy.

Python integer conversion is constant for the one-character strings zero and one. The answer is at most $N$, because at most one forced flip is started per position.

## Alternatives and edge cases

- **Count explicit transitions:** Prefix the target conceptually with zero and count adjacent unequal bits. This is the same algorithm in a different expression.
- **Simulate the full string:** Toggling each suffix can cost $O(N^2)$ time.
- **Maintain a Boolean flipped flag:** Toggle it on each mismatch and increment a separate count. It is equivalent to using answer parity.
- **All zeros:** No operations are required.
- **All ones:** One flip at index zero creates the target.
- **Alternating bits:** Every position differs from the prior effective value, so answer equals string length.
- **Single zero:** It already matches the initial state.
- **Single one:** One suffix flip at zero is necessary.
- **Previous prefix:** Starting a later suffix never changes earlier fixed positions, which is why the greedy invariant holds.
- **No competitive variant:** This package's manifest exposes only the Optimal branch, and the approach follows that exact source.
