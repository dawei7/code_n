## General

Although the class is named `MyHashSet`, the exact implementation does not compress keys with a hash function and does not need collision handling. It uses direct addressing: every legal key has its own dedicated array position.

The source restricts keys to the inclusive range from `0` through `1,000,000`. That finite, reasonably sized universe makes a Boolean presence table possible.

**Direct-address representation**

The constructor allocates:

`self.data = [False] * 1000001`.

Index `key` represents that exact key.

- `data[key] == False` means the key is absent.
- `data[key] == True` means the key is present.

There is a one-to-one mapping between legal keys and indices. Key zero uses index zero, and key one million uses the last index. The array length includes both endpoints, which explains the extra one.

**Why this is set behavior**

A set stores only membership, not occurrence counts.

`add(key)` assigns `True`. Adding the same key repeatedly leaves the same Boolean value, so duplicates never accumulate.

`remove(key)` assigns `False`. Removing a key that is already absent also leaves `False`, satisfying the requirement to do nothing observable.

`contains(key)` returns the Boolean stored at that index.

Every operation directly establishes or reads the representation invariant; there is no search.

**The representation invariant**

After any sequence of operations:

> For every legal key `x`, `data[x]` is true if and only if the most recent relevant update among `add(x)` and `remove(x)` was an addition, or `x` was added and never removed.

Initially every entry is false, matching an empty set.

An operation on key `x` changes only `data[x]`. Because each other key `y` has a different index, its membership remains unchanged. This independence is the main simplicity of direct addressing.

**Why there are no collisions**

Traditional hashing maps a large key universe into a smaller bucket array, so two keys may share a bucket. This implementation uses identity as the address:

$$
\operatorname{address}(key)=key.
$$

Distinct legal integers have distinct addresses. No linked lists, probing, secondary hashes, or equality searches are needed.

It is still a valid implementation of the HashSet interface, even though its internal technique is more specifically called a direct-address table.

**A complete operation trace**

Start with all entries false.

- `add(1)` sets `data[1]` to true.
- `add(2)` sets `data[2]` to true without changing index one.
- `contains(1)` reads true.
- `contains(3)` reads its untouched false entry.
- A second `add(2)` writes true over true; the set still has one logical key `2`.
- `remove(2)` writes false.
- `contains(2)` now returns false.
- Another `remove(2)` would leave false and cause no error.

This matches all required semantics with single array accesses.

**Why Boolean storage is enough**

The class never needs to remember when a key was inserted, how often it was added, or any associated value. Membership has exactly two states, so one Boolean per possible key contains all required information.

A counter would introduce incorrect multiset behavior if repeated additions required repeated removals. A set deliberately treats repeated addition as idempotent.

**Why bounds matter**

Direct indexing is safe because every operation receives `0 <= key <= 10^6`. A negative key in Python would index from the end, and a key above the maximum would raise an error. The exact code performs no defensive check because the source contract excludes both cases.

The fixed key ceiling also determines the memory cost. This design would be wasteful or impossible for arbitrary 64-bit integers or strings.

**Why the implementation is correct**

The constructor establishes false membership for every key. `add` makes the selected key present, `remove` makes it absent, and `contains` returns exactly that state. Operations on one key cannot affect another because their indices differ.

By induction over any operation sequence, the Boolean table always matches the abstract set, so all returned membership answers are correct.

## Complexity detail

Let

$$
U=1{,}000{,}001
$$

be the size of the legal key universe, and let `q` be the number of later operations.

Constructing the Boolean list writes `U` initial entries, taking

$$
O(U)
$$

time and `O(U)` space.

Each `add`, `remove`, or `contains` performs one indexed access or assignment, so each operation takes `O(1)` worst-case time. Across `q` operations, operation time is `O(q)`, and including initialization total time is `O(U+q)`.

Persistent space remains

$$
O(U),
$$

regardless of how many keys are actually present. There is no per-operation auxiliary allocation.

## Alternatives and edge cases

- **Separate chaining:** Hash keys into a smaller bucket array and store colliding keys in lists. This uses space closer to the number of inserted keys but has bucket-search costs.

- **Open addressing:** Probe alternative slots after collisions. It can be compact but requires careful deletion markers and resizing.

- **Bitset:** Store one bit rather than a full Python Boolean reference per key. The logical design is identical and memory can be much smaller in a low-level representation.

- **Key zero:** It maps naturally to `data[0]`; no sentinel conflict exists because storage is Boolean.

- **Maximum key:** Index `1,000,000` is valid because the list length is `1,000,001`.

- **Repeated addition:** Writing true again does not create duplicates.

- **Removing an absent key:** Writing false over false has no observable effect.

- **Contains does not mutate:** It only reads one entry.

- **Empty set:** Immediately after construction, every membership query returns false.

- **Sparse usage:** Even one inserted key still pays for the full universe-sized array; this is the direct-address tradeoff.

- **Contract violations:** Negative or oversized keys are not handled and could access the wrong slot or raise an exception.

- **No built-in hash table:** A plain indexed list satisfies the restriction without using `set` or `dict`.
