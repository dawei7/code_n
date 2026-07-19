## General
Build a frequency table for the first `k` elements. The number of keys in that table is exactly the number of distinct values in the first window, because a key exists precisely when its value has a positive frequency.

Slide the window one position at a time. Decrement the count of the element leaving on the left and remove its key if the count reaches zero. Then increment the count of the element entering on the right. Record the table size after both updates.

At every step, the table begins with the previous window's exact multiplicities. Removing its leftmost element and adding the new rightmost element changes that multiset into exactly the next window. Removing zero-count keys preserves the equivalence between table keys and distinct values, so every recorded size is the required count.

## Complexity detail
The first window takes $O(k)$ time to build. Each of the remaining $n-k$ elements causes a constant expected number of hash-table operations, for $O(n)$ total time. At most `k` distinct values can occur in one window, so the frequency table uses $O(k)$ space; the required output is not counted as auxiliary space.

## Alternatives and edge cases
- **Rebuild a set for every window:** Direct and correct, but costs $O((n-k+1)k)$ time.
- **Fixed value-frequency array:** The value bound permits an array of size $10^5+1$, trading predictable access for space independent of `k`.
- **Window length one:** Every result is 1 because each one-element window has one distinct value.
- **Window equals the array:** Return exactly one count.
- **All values equal:** The frequency may change while the distinct count remains 1.
- **Outgoing last occurrence:** Delete its key only when its frequency becomes zero.
- **Incoming existing value:** Incrementing an existing key must not increase the distinct count.
- **Repeated windows:** Equal adjacent answers are still separate output entries.
