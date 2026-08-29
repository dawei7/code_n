## General

**Process the earliest unresolved bit first.** Each operation flips exactly three consecutive positions. Scan the array from left to right. When the scan reaches index `i`, every position before `i` has already been conceptually fixed to $1$. Any new operation starting before `i` would touch one of those fixed positions and undo earlier work. Any operation starting after `i` cannot touch `i`. Therefore, among the operations that remain useful, the only operation capable of changing the current bit is the length-three flip beginning exactly at `i`.

That observation makes the choice forced rather than merely greedy:

- if the current value at `i` is $1$, do not flip at `i`, because a flip would turn it into $0$ and no later operation could repair it;
- if the current value at `i` is $0$, a successful solution must flip starting at `i`;
- if `i + 2` lies outside the array, that forced flip does not exist, so the transformation is impossible.

There is no advantage to applying the same triplet twice. Flipping twice restores all three bits to their previous states and costs two operations. Thus each starting position is used either zero or one time, exactly as the scan decides.

**Notice the source's deliberate omitted assignment.** A literal triplet flip at `i` would toggle `nums[i]`, `nums[i + 1]`, and `nums[i + 2]`. The exact solution only executes

`nums[i + 1] ^= 1` and `nums[i + 2] ^= 1`.

It does not write `nums[i] ^= 1`. This is intentional. The branch runs only when the local value `x` is zero, and the forced operation conceptually changes that current zero to one. Once the scan leaves index `i`, no future decision needs to read it again. Physically storing that known final value would have no effect on the count or on any future bit, so the code omits the write.

This means the array held in memory is not a complete simulation of the board after all counted operations. Processed zeros may remain zero in `nums` even though the conceptual operation made them one. Only the unprocessed suffix is maintained accurately, and that is all the algorithm requires.

**Why `x` still sees earlier flips correctly.** Python's `enumerate(nums)` retrieves the element at the current index as iteration progresses. Earlier decisions may already have toggled that position when it was one or two places ahead. By the time iteration reaches `i`, the local variable `x` therefore contains the current value after every previously chosen triplet that affects `i`. Omitting writes to already processed centers does not interfere with this, because a center is never part of a future triplet.

When a zero is found and a complete triplet is available, the code toggles the two future positions, increments `ans`, and treats the current position as finalized. When a one is found, it simply advances.

**An invariant that mirrors the implementation.** Just before index `i` is examined:

1. every index smaller than `i` is conceptually $1$ after the operations counted so far;
2. every value from `i` onward stored in `nums` equals its real value after those operations;
3. the decisions for starts smaller than `i` are forced in every successful solution.

The invariant is true initially. If the current stored value is one, skipping preserves it and no future start can change it. If it is zero, flipping at `i` is forced; the conceptual current bit becomes one, and explicitly toggling the next two cells keeps the still-unprocessed suffix accurate. Thus the invariant advances by one position.

If the scan reaches a zero among the final two indices, `i + 2 >= len(nums)`. Starts before `i` are already forced and fixed, while no legal start at or after `i` covers that zero. Returning $-1$ is therefore not an early guess: it proves no operation sequence exists. If the scan finishes, every position is conceptually one.

**Why the count is minimum.** At every zero encountered, all successful solutions must use the triplet beginning there. At every one encountered, successful solutions must not use it after earlier decisions have been normalized to at most one flip per start. The algorithm neither misses a necessary operation nor performs an optional one. Its count is consequently the unique necessary count whenever a solution exists.

For `nums = [0,1,1,1,0,0]`, index $0$ is zero, so the first flip is forced. The code leaves stored index $0$ alone and toggles positions $1$ and $2$, making the relevant stored suffix look like `[0,0,1,1,0,0]`. At index $1$, the current zero forces another flip, which toggles positions $2$ and $3$. Index $2$ is then one and is skipped. Index $3$ becomes zero and forces the final triplet covering positions $3,4,5$. The count is three, and the conceptual final array is all ones.

For `[0,1,1,1]`, the forced flip at index $0$ makes the unprocessed suffix values at indices $1$ and $2$ equal to zero. The forced flip at index $1$ would need index $3$ and index $4$, but index $4$ does not exist. No alternative first decision was available, so $-1$ is correct.

## Complexity detail

Let $n$ be the length of `nums`. The loop examines every index at most once. Each iteration performs a comparison, a bound check only when needed, and at most two XOR assignments. These are constant-time operations, so the total time is $O(n)$. This is optimal in the worst case because a late bit can determine whether the result is possible, requiring inspection of the input.

The solution uses only `ans`, the loop index, and the current value in addition to the input list. It allocates no data structure whose size grows with $n$, so auxiliary space is $O(1)$. The list is modified in place, although—as described above—it is only a faithful representation of the unprocessed suffix, not the actual final all-one array.

## Alternatives and edge cases

- **Flip all three cells explicitly:** Toggle `nums[i]` as well as the next two. This is easier to view as a literal simulation and has the same $O(n)$ time and $O(1)$ space, but the current-cell write is unnecessary once its index is finalized.
- **Track active-flip parity:** A small queue or parity mechanism can compute each effective bit without mutating the array. For fixed window length three it remains $O(n)$ time and $O(1)$ space, but it is more machinery than the exact in-place suffix update.
- **Breadth-first search over arrays:** Treating every binary array as a state can find a shortest sequence for tiny $n$, but there are $2^n$ states. The forced leftmost decision eliminates the need for state search.
- **Try every subset of triplet starts:** Each start only matters by parity, but enumerating all $2^{n-2}$ choices is exponential. The scan determines those parities uniquely.
- **Final two positions:** They cannot be the start of a length-three operation. If either is zero when reached, returning $-1$ is mandatory.
- **Length exactly three:** A zero at index $0$ forces the only operation. After its effects reach indices $1$ and $2$, the scan either finishes successfully or detects impossibility there.
- **Already all ones:** No branch is taken, `ans` remains zero, and the input stays unchanged.
- **Overlapping flips:** They are handled automatically because each forced operation toggles the next two stored values before those indices are read.
- **Repeated flip at one start:** Two identical flips cancel. Removing such pairs always reduces the operation count, so a minimum sequence never needs a start more than once.
- **Input mutation is partial:** The method changes future cells but deliberately leaves a processed zero unchanged in storage. Callers must not expect `nums` to contain the resulting all-one array, even when the returned count is valid.
- **Binary-domain dependence:** XOR with one toggles correctly only because every value is guaranteed to be either zero or one.
