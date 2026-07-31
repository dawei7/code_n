## General

A partial curry must remember both the arguments already supplied and their order. Copying the complete accumulated array whenever another call arrives is simple, but one-argument calls then copy prefixes of lengths $1, 2, \ldots, n$, producing quadratic work. Instead, store every call's argument array as one immutable node whose `previous` link points to the earlier state.

The initial returned function has no node and a collected count of zero. Each call creates one node containing only its new arguments and adds their length to the count. Empty calls create empty chunks but do not advance the arity. If the total remains below `fn.length`, return another closure over that new node and count.

**Flatten only at the completing call**

Once the count reaches the declared arity, follow `previous` links to collect the chunks from newest to oldest. Traverse that chunk list backward and append each chunk into one final argument array, restoring the original call order and the order within every call. Invoke `fn` once with that array.

Every supplied argument belongs to exactly one node. Reversing the node traversal restores the chronological batch order, so the flattened sequence is identical to concatenating `inputs` from left to right. The arity check delays evaluation until that sequence is complete. For a zero-parameter function, the first empty call already satisfies the check and invokes `fn` with no arguments.

Because nodes are immutable, two functions returned from the same partial curry can be extended independently: neither continuation mutates or replaces the shared prefix.

## Complexity detail

Let $n$ be the total number of arguments and $p$ the number of curry calls. Creating nodes and recording new argument batches takes $O(n + p)$ time across the sequence. The completing call visits $p$ chunks and copies $n$ values once, so the total remains $O(n + p)$. The linked nodes, retained batches, temporary chunk list, and final argument array require $O(n + p)$ space.

## Alternatives and edge cases

- **Copy accumulated arguments after every call:** Spreading `[...args, ...nextArgs]` is correct and naturally supports branching, but one argument per call causes $O(n^2)$ total copying.
- **One mutable accumulator:** Appending into a shared array achieves linear work for one call chain, but extending the same partial curry along two branches makes those branches interfere.
- **Bind parameters repeatedly:** Successive `bind` calls can express partial application, but managing completion and zero-argument calls is less direct and still creates chained wrappers.
- **Empty argument batches:** Preserve the current count and ordering; return another curry unless zero arity is already complete.
- **Zero arity:** The returned function must call `fn` when invoked as `curried()` rather than returning another function forever.
- **Argument order:** Retain order both between batches and within each batch; a linked structure must be reversed during final flattening.
- **Reusable partial curries:** Treat each state as immutable so separate continuations can safely share a prefix.
