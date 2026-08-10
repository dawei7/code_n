## General

**Model the generator as a paused state machine**

The generator represents a cursor moving around a circular array. It does not precompute a sequence because the sequence may be infinite and each movement depends on the caller's next input. The only persistent algorithmic state is `index`, the current array position, and `jump`, the value sent into the generator when execution resumes.

JavaScript generators alternate between running and suspended states. A `yield` expression does two jobs at different times:

1. When execution reaches `yield arr[index]`, it sends the current array value to the caller and pauses.
2. When the caller later invokes `next(someJump)`, that argument becomes the result of the suspended `yield` expression, so it is assigned to `jump`.

Understanding that two-part behavior explains the compact exact code.

**The first call is initialization, not a movement**

The function first sets `index = startIndex` and executes `let jump = yield arr[index]`. Therefore, the first `next()` returns the array element at the supplied start index. No jump has yet been applied.

A subtle JavaScript rule is that an argument passed to the very first `next(argument)` cannot become the result of a previous `yield` because the generator has not reached one yet. That argument is ignored. The intended protocol is consequently:

- create the generator;
- call `next()` to receive the starting value;
- call `next(jump)` for every subsequent movement.

After the first yield, each resume supplies the jump that should move away from the position whose value was just observed.

**Turning an arbitrary signed jump into a valid circular index**

Inside the infinite loop, the next position is computed as

`((index + jump) % arr.length + arr.length) % arr.length`.

For a positive total, ordinary remainder already produces a number from zero through `arr.length - 1`. Large positive jumps also work because remainder removes complete laps around the array. For example, in an array of length five, moving forward by twelve is equivalent to moving forward by two.

Negative jumps require extra care in JavaScript. JavaScript's `%` is a remainder operator, and a negative dividend can produce a negative result. An index such as `-2` is not the desired wraparound position. The first remainder reduces the magnitude, adding `arr.length` shifts any negative remainder into the non-negative range, and the second remainder handles the case where the first result was already non-negative and the addition reached the array length. The final result always satisfies

$$
0 \le \text{index} < \text{arr.length}.
$$

This double-modulo normalization works for forward jumps, backward jumps, zero, and jumps spanning many cycles.

**One resume performs exactly one move**

After normalization, the generator reaches `jump = yield arr[index]`. It returns the value at the new position and pauses again. On the next call, the newly supplied argument replaces `jump` and the loop repeats.

Consider `arr = [10, 20, 30, 40]` and `startIndex = 1`. The first `next()` yields `20`. Sending `2` computes index three and yields `40`. Sending `-5` then computes

`((3 - 5) % 4 + 4) % 4 = 2`,

so the next value is `30`. The calculation uses the current index, not the original start index. That is why `index` must remain inside the generator frame between calls.

**Why the generator never finishes**

The `while (true)` loop contains a yield on every iteration, so it is infinite but cooperative. It does not consume CPU continuously: each iteration stops at `yield` and no further work occurs until the caller asks for another value. This gives an unbounded logical sequence with constant physical storage.

The exact implementation retains the array reference rather than a copy. If outside code mutates an element after generator creation, a later visit observes the new value. If outside code changes the array's length, even the wraparound modulus changes. The problem normally treats the provided array as stable; cloning it would create different semantics and additional space.

**Why the produced sequence is correct**

Initially, `index` is exactly `startIndex`, so the first yielded value is correct. Assume a yielded value came from the current valid position `index`. When the caller supplies a jump, the normalization computes the unique array index congruent to `index + jump` modulo the array length. That is precisely the result of moving the requested number of circular steps. The generator then yields the element at that index and stores the index for the next movement. By repeating this reasoning after every suspension, every returned value follows the requested circular walk.

## Complexity detail

Let `n` be `arr.length`. Creating the generator object is `O(1)`; its body does not execute until the first `next` call. The first `next()` performs `O(1)` work and returns the starting value. Every later `next(jump)` performs a fixed number of arithmetic operations, one array access, and one suspension, so it also takes `O(1)` time regardless of `n` or the magnitude of `jump`. Arithmetic is treated as constant-time JavaScript number arithmetic under the problem's numeric model.

After `q` yielded values, the algorithm has done `O(q)` total work. There is no up-front `O(n)` traversal and no dependency on how many complete circles the jumps represent, because modulo collapses them in constant time.

The generator frame stores `index`, `jump`, and a reference to `arr`, which is `O(1)` auxiliary space. It does not copy the input and does not retain previously returned values. The caller's input array itself occupies `O(n)`, but that is input storage rather than additional algorithmic space. The JavaScript generator object and suspension machinery are constant-sized for this fixed function.

## Alternatives and edge cases

- **Repeated step-by-step movement:** Incrementing or decrementing the cursor once per unit of `jump` is intuitive, but a huge jump would cost `O(|jump|)`. Modular arithmetic reaches the identical position in constant time.
- **Single remainder expression:** Writing `(index + jump) % arr.length` fails for negative totals in JavaScript because it may return a negative remainder. The two-remainder normalization is necessary.
- **Precompute an infinite sequence:** This is impossible in finite memory and cannot accommodate future jumps that have not been supplied. A generator naturally computes only the next requested state.
- **Return an iterator object manually:** A custom object with a `next` method can implement the same state machine, but the generator syntax directly expresses suspension and input through `yield`.
- **First `next` receives an argument:** JavaScript ignores that argument because no `yield` is waiting to receive it. The first result is still `arr[startIndex]`.
- **Zero jump:** The normalized index remains unchanged, so the same current value is yielded again.
- **Jump equal to a multiple of the length:** Complete laps cancel under modulo, leaving the cursor at the same index.
- **Large positive or negative jump:** The number of laps does not affect running time; normalization selects the congruent valid index directly.
- **One-element array:** Every normalized index is zero, so every call yields the sole element regardless of the jump.
- **External array mutation:** The generator holds the original reference. Later element changes are visible, and changing the length changes circular behavior; callers should keep the array stable when they need a fixed sequence.
- **Empty array:** The described operation assumes a usable circular array. With length zero, modulo by zero and `arr[index]` cannot define a valid walk, so such input must be excluded by the contract.
- **Infinite loop concern:** The loop is safe because every iteration reaches `yield`. It advances only once per caller request rather than running without pause.
