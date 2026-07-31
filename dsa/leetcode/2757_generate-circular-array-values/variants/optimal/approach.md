## General

A generator preserves local variables whenever it suspends at `yield`. Store only the current index, initially `startIndex`, and yield `arr[index]`. The value passed to the next `next(jump)` call becomes the result of that suspended yield expression, giving the jump needed for the following state transition.

**Normalize signed jumps**

Add the jump to the saved index and reduce it modulo the array length. JavaScript's remainder operator may return a negative number, so use

`((index + jump) % n + n) % n`

to place the result in $[0,n-1]$ for either jump direction and for any number of complete wraps.

After normalization, yield `arr[index]` and assign the next resumed input back to `jump`. Before every yield, `index` equals the starting index plus the sum of all previously supplied jumps modulo the array length. The update preserves this statement for the next call, proving every yielded element is the required circular destination.

## Complexity detail

Creating the generator and each call to `next()` use $O(1)$ time. One suspended index, one jump, and fixed generator control state require $O(1)$ auxiliary space. A harness requesting and storing $q$ values necessarily spends $O(q)$ total time and output space, but the required lazy generator operation remains constant per advance.

One generator advance must produce one value, establishing an $Omega(1)$ lower bound. The fixed modular update and indexed read match that bound, so the package uses an asymptotic-optimality certificate instead of timing a bounded schedule of at most 100 jumps.

## Alternatives and edge cases

- **Move one position per unit jump:** This is correct but costs $O(\lvert\texttt{jump}\rvert)$ per advance and repeats unnecessary full cycles.
- **Precompute repeated arrays:** The jump sequence is supplied lazily and may be signed, so a finite expanded array does not replace stateful modular movement.
- **Use one raw remainder:** In JavaScript, a negative dividend can produce a negative remainder and therefore an invalid array index.
- The first `next()` call receives no jump and must yield the starting value before any movement.
- A zero jump yields the same element again.
- Jumps equal to any multiple of the array length leave the index unchanged.
- A one-element array always yields its sole value.
- Generator state must persist across the maximum 100 requested advances.
