## General

**Combine fast key lookup with fast recency updates**

An LRU cache must answer two independent questions quickly:

- given a key, where is its stored value?
- among all stored keys, which one was used least recently?

A hash map answers the first in expected constant time but does not maintain usage order. A linked list maintains order, but searching it by key would be linear. The solution combines them:

- `cache` maps each key directly to its `Node`;
- a doubly linked list orders those nodes by recency.

The node immediately after `head` is the most recently used. The node immediately before `tail` is the least recently used.

**Why two sentinel nodes simplify the list**

`head` and `tail` are permanent dummy nodes. Initially, `head.next` is `tail` and `tail.prev` is `head`.

Real cache nodes always live strictly between them. Therefore:

- every real node has a predecessor and successor;
- insertion at the most-recent end never needs an empty-list branch;
- eviction always removes `tail.prev`;
- removing the only real node uses the same pointer assignments as removing a middle node.

The sentinel key and value defaults have no semantic meaning and are never entered into `cache`.

**Understand the two pointer helpers**

`remove_node(node)` reconnects the node’s neighbors:

- `node.prev.next = node.next`;
- `node.next.prev = node.prev`.

Because the list is doubly linked and the caller already has the node reference, no search is needed.

`add_to_head(node)` inserts immediately after the head sentinel. It first points the node toward the old first real node and back to `head`, then updates both surrounding links to point at the inserted node.

After this helper, that node is the most recently used.

The helpers do not modify the dictionary or `size`; they handle only recency-list topology. Their callers are responsible for keeping all structures synchronized.

**A successful `get` is a use**

If a key is absent, `get` returns `-1` and changes no recency information.

If present, the map provides its node directly. The source removes that node from its old list position and reinserts it after `head`. This promotion records the access as the newest use. It then returns `node.val`.

Promoting even an already most-recent node is safe: removal joins `head` to the former second node, and insertion restores the accessed node after `head`.

**Updating an existing key is also a use**

For an existing key, `put` retrieves its node, removes it, changes `node.val`, and adds the same object at the most-recent position.

No new dictionary entry or list node is needed, and `size` stays unchanged. Updating must refresh recency because the operation has just used that key.

**Insert and evict in a synchronized transaction**

For a new key, the method creates a node, stores it in the map, inserts it after `head`, and increments `size`.

If that makes `size > capacity`, `tail.prev` is the least recently used real node. The method removes its key from `cache`, unlinks the node, and decrements `size`.

Both map deletion and list removal are essential. Leaving the dictionary entry would allow later access to an evicted node; leaving the list node would corrupt ordering and consume capacity invisibly.

The constructor guarantees positive capacity, so after an overflowing insertion there is always a real node at `tail.prev` to evict.

**State invariants after every public operation**

The implementation maintains:

- the dictionary contains exactly the real list nodes;
- dictionary keys equal their nodes’ `key` fields;
- the number of real nodes equals `size` and never exceeds `capacity`;
- list order from `head.next` to `tail.prev` is most recent to least recent;
- every real node’s forward and backward links agree.

`get` changes only order, existing-key `put` changes a value and order, and new-key `put` changes membership before restoring the capacity bound.

In the example with capacity two, keys one and two are inserted with two most recent. `get(1)` promotes one, making two least recent. Inserting three evicts two. Later, inserting four after accessing nothing newer than one evicts one. The remaining order correctly reflects four as newest and three as older.

## Complexity detail

Let $C$ be the configured capacity.

Dictionary lookup, insertion, and deletion are expected $O(1)$. Each linked-list helper changes a fixed number of pointers. `get` and `put` therefore run in expected $O(1)$ time per operation, as required.

At most $C$ real nodes and $C$ dictionary entries exist, plus two sentinels and scalar fields. Space is $O(C)$.

The word “average” in the contract matters because Python dictionary operations are expected constant time rather than worst-case constant under adversarial collision behavior.

## Alternatives and edge cases

- **Ordered dictionary:** Maintain least-to-most recent insertion order, moving accessed keys to the end and popping the first on overflow. It is concise but delegates the core data-structure work to a library.
- **Plain dictionary with timestamps:** Updating timestamps is easy, but finding the minimum timestamp by scanning makes eviction $O(C)$ unless another ordered structure is added.
- **Array or list as recency queue:** Locating and removing an arbitrary accessed key costs $O(C)$.
- **Capacity one:** Each new distinct insertion evicts the only previous real node; sentinels avoid special pointer cases.
- **Repeated `get`:** Each successful access keeps that key at the most-recent end.
- **Existing-key `put`:** It updates in place and must not increment `size` or evict another key.
- **Stored value `-1`:** Constraints make values nonnegative, so `-1` is an unambiguous miss signal.
- **Eviction order:** `tail.prev`, not `head.next`, is least recent in this source’s orientation.
- **Node/map consistency:** Removing from only one structure would break later operations; membership changes must update both.
- **Thread safety:** No synchronization is present. Concurrent operations could interleave pointer and dictionary changes and violate invariants.
