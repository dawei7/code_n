## General

The temporary string `t` is a stack: characters enter from the front of `s` and can leave only from the end of `t`. Before reading the input, count how many copies of every letter remain in `s`.

Move characters from `s` to the stack one at a time, decrementing the moved character's remaining count. Maintain the smallest letter still present in the unread suffix. The stack top is safe to print whenever it is no greater than that smallest unread letter. Printing a larger top while a smaller unread letter exists would make the result lexicographically worse; retaining a top that is already no larger cannot improve the next output position.

Pop every safe top before consuming another input character. Each choice therefore writes the smallest character that can legally occupy the next output position. Once no unread characters remain, every stack character is safe and is printed in reverse stack order.

## Complexity detail

Each of the $n$ characters is counted once, pushed once, and popped once. The pointer to the smallest remaining letter advances at most 26 times, so total time is $O(n)$. The stack and written output require $O(n)$ space, while the frequency array has constant size.

## Alternatives and edge cases

- **Recompute the unread minimum:** Scanning the remaining suffix after every push is correct but takes $O(n^2)$ time.
- **Suffix-minimum array:** Precomputing the smallest character for every suffix also gives $O(n)$ time, using an additional $O(n)$ array.
- **Single character:** It is pushed and immediately printed.
- **Increasing input:** Every new stack top can be printed immediately.
- **Decreasing input:** All characters remain stacked until the smallest final character arrives.
- **Repeated characters:** Equality is safe; a stack top equal to the smallest unread letter may be printed now.
- **Exhausted input:** The sentinel state makes every remaining stack top printable.
