## General

Two views of the state are needed: the current number stored at each index,
and an efficient way to obtain the smallest index for a number. Keep the first
view in a hash map. For the second, keep a min-heap of candidate indices for
each number.

**Invalidate old assignments lazily**

On `change(index, number)`, update the current-assignment map and push `index`
onto `number`'s heap. If that exact assignment already exists, do nothing.
There is no need to search and remove the index from its former heap.

On `find(number)`, repeatedly inspect the heap minimum. If the assignment map
still maps that index to `number`, it is the smallest valid index. Otherwise
pop the stale entry and continue. Return `-1` if the heap empties or never
existed.

Every valid assignment is inserted into its number's heap. Any candidate below
the returned top has been proven stale against the authoritative assignment
map, while the top itself is current. It is therefore exactly the smallest
matching index. Each stale entry is popped at most once, so deferred cleanup
does not accumulate repeated work.

## Complexity detail

Let $q$ be the total number of operations. A change performs at most one heap
push in $O(\log q)$ time. A find may pop stale entries, but across the full
trace there are at most $q$ such pops; its amortized cost is $O(\log q)$.
The complete trace takes $O(q\log q)$ time and uses $O(q)$ space.

## Alternatives and edge cases

- **Ordered set per number:** A balanced tree supports eager deletion and
  minimum lookup with the same asymptotic bounds, but Python has no built-in
  ordered set.
- **Scan every assignment:** Keeping only the index map is simple and correct,
  but each `find` can take $O(q)$ time and a trace can become quadratic.
- **Repeated identical change:** Skipping it avoids duplicate live heap entries.
- **Replacing the minimum:** The next `find` removes the stale old minimum and
  exposes the next current index.
- **Absent number:** A missing or fully stale heap produces `-1`.
