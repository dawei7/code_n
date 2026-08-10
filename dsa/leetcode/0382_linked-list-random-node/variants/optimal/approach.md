## General

**The obstacle presented by a linked list**

Uniform random selection is easy from an array: generate a uniform index and read that position. A singly linked list does not provide constant-time indexed access, and the follow-up asks for a method that still works when the length is unknown and the list is too large to copy.

The exact solution uses reservoir sampling with a reservoir of size one. It stores only the original `head` in the constructor. Every call to `getRandom()` walks through the list once while continually maintaining one candidate answer. After the walk, every node—not merely every distinct value—has exactly the same probability of being that candidate.

This distinction matters when values repeat. If three different nodes contain the same value, each node receives its own equal chance, so that value’s total probability is three times the probability of a value appearing in one node. The contract speaks about random nodes and returns their values; it does not require distinct values to be equally likely.

**The reservoir invariant**

After processing the first $i$ nodes, the variable `ans` is the value of one of those nodes, and each of the $i$ processed nodes has probability exactly $1/i$ of being represented.

The algorithm begins each call with `n = ans = 0` and `head = self.head`. For every node:

1. Increment `n`, so `n` is the number of nodes seen including the current one.
2. Generate `x = random.randint(1, n)`, uniformly from the inclusive integers `1` through `n`.
3. If `n == x`, replace `ans` with the current node’s value.
4. Move to `head.next`.

The equality `n == x` occurs with probability $1/n$. Therefore the current node replaces the reservoir with exactly the probability needed to give it a fair chance among all `n` nodes seen so far.

There is nothing special about choosing the endpoint `n`; testing `x == 1` would produce the same probability. The exact code’s condition is simply one of the `n` equally likely random outcomes.

**Why the first node initializes the answer safely**

Before traversal, `ans` is set to `0`, even though zero might not be a node value. This placeholder is never returned for a valid nonempty list merely because of initialization.

At the first node, `n` becomes `1`, and `random.randint(1, 1)` must return `1`. Therefore `n == x` is certainly true, and `ans` is replaced by the first node’s actual value. Later nodes may replace it, but the reservoir always contains a processed node from that point onward. The nonempty-list guarantee is what makes this initialization valid.

**Why replacement produces a uniform sample**

The proof is easiest by induction.

After the first node, it is selected with probability $1$, which equals $1/1$. Assume that after the first $i-1$ nodes, each has probability $1/(i-1)$ of occupying the reservoir.

When node $i$ arrives, it replaces the reservoir with probability $1/i$, so its own final probability after this step is $1/i$.

Any earlier node remains selected only when two events both occur:

- it was selected before node $i$, with probability $1/(i-1)$;
- node $i$ does not replace it, with probability $(i-1)/i$.

Multiplying gives

$$
\frac{1}{i-1} \cdot \frac{i-1}{i} = \frac{1}{i}.
$$

Thus, after processing node $i$, every one of the $i$ nodes has probability $1/i$. The invariant holds at every prefix.

When the traversal ends after $N$ nodes, each node consequently has probability $1/N$ of supplying `ans`. Returning `ans` is therefore a uniform node sample.

**Looking at survival over the rest of the list**

The same result can be understood from one fixed node’s entire journey. Suppose a node is at one-based position $i$ in a list of length $N$.

It enters the reservoir when visited with probability $1/i$. At position $i+1`, it survives with probability $i/(i+1)`. At position $i+2`, it survives with probability $(i+1)/(i+2)`, and so on. Its final probability is

$$
\frac{1}{i}
\cdot \frac{i}{i+1}
\cdot \frac{i+1}{i+2}
\cdots
\frac{N-1}{N}
= \frac{1}{N}.
$$

All intermediate factors cancel. Early nodes begin with a larger chance to enter but face more future opportunities for replacement. Late nodes have a smaller entry probability but fewer future threats. Reservoir sampling balances those effects exactly.

**A concrete three-node trace**

For a list `1 -> 2 -> 3`:

- Node `1` is selected with certainty when `n = 1`.
- Node `2` replaces it with probability $1/2$. After this step, both nodes have probability $1/2$.
- Node `3` replaces the current answer with probability $1/3$. If it does not replace, which occurs with probability $2/3$, the existing uniform choice among the first two survives.

The final probabilities are therefore:

$$
P(1) = \frac{1}{2}\cdot\frac{2}{3}=\frac{1}{3},
\qquad
P(2) = \frac{1}{2}\cdot\frac{2}{3}=\frac{1}{3},
\qquad
P(3) = \frac{1}{3}.
$$

The actual random outcome can vary from call to call; uniformity is a property of the distribution, not a promise that a short sequence of calls contains each value the same number of times.

**Why every call starts over**

`getRandom()` resets `n` and `ans` and traverses again from `self.head`. This produces a fresh reservoir sample for that call. Reusing the prior answer without a new traversal would not constitute a fresh uniform choice unless additional preprocessed state were stored.

The constructor itself does not discover the length and does not copy any values. That directly addresses the unknown-length, constant-extra-space follow-up. It also means the work is paid on each draw rather than once during construction.

Provided the linked list remains unchanged, each call samples from the same node population. If a caller mutates node links after construction, a later traversal would naturally sample whatever chain is reachable from the stored head at that moment; the challenge’s normal model treats the supplied list as fixed.

**Why storing only values is sufficient**

The reservoir variable keeps `head.val`, not a reference to the selected node. The required output is the node’s value, so retaining the full node is unnecessary. The proof still reasons about node identities: even if two nodes have equal values and become observationally indistinguishable when returned, each participates in the replacement process separately.

## Complexity detail

Let $N$ be the number of nodes and let $D$ be the number of calls to `getRandom()`.

The constructor assigns one reference and takes $O(1)$ time. One `getRandom()` call visits every node exactly once. Each visit performs constant work: an increment, one random integer generation, a comparison, an occasional assignment, and one pointer advance. A single draw therefore takes $O(N)$ time.

Across $D$ draws, the exact solution takes $O(ND)$ total time after the $O(1)$ constructor. This is materially different from the `O(n + draws)` complexity recorded in the variant manifest, which would describe preprocessing the list into an array once and then making constant-time draws. The exact solution does not perform that preprocessing; its reservoir traversal repeats for every draw.

Only `n`, `ans`, `x`, and the traversal pointer are used in addition to the stored head reference. Their number does not grow with $N$, so auxiliary space is $O(1)$. There is no recursion and therefore no length-dependent call stack.

The random generator’s internal state is treated as constant-size library machinery under the usual complexity model. The input list itself is not copied and is not counted as auxiliary storage.

## Alternatives and edge cases

- **Copy values into an array:** Traverse once during construction, store all $N$ values, and use random indexed access for each call. This costs $O(N)$ initialization time and space but only $O(1)$ per draw, for $O(N+D)$ across $D$ draws. It matches the manifest’s stated complexity but not the exact supplied solution, and it does not satisfy the constant-space follow-up.

- **Count length, then walk to a random index:** One can determine $N$ first, draw an index, and traverse to it. Without storing values, this still takes $O(N)$ per call and may require two passes if the length is recomputed. Caching a fixed list length reduces it to one partial traversal per draw but assumes the list never changes.

- **Reservoir sampling:** The exact method is the appropriate choice when length is unknown, the source behaves like a stream, or copying the population is too expensive. It trades $O(N)$ time per draw for $O(1)$ auxiliary space.

- **Single-node list:** The first iteration chooses that node with probability one, so every call returns its value. No special branch is necessary.

- **Duplicate node values:** Sampling is uniform over nodes, not distinct values. If a value appears in $f$ of $N$ nodes, it is returned with probability $f/N$, which follows directly from each occurrence’s $1/N$ chance.

- **Negative values and zero:** `ans = 0` is only a placeholder. The first node certainly overwrites it, so every allowed node value, including negative numbers and zero, is handled without a sentinel conflict.

- **Empty list:** The contract guarantees a nonempty head. With an empty list, the loop would never replace the placeholder and would incorrectly return `0`; supporting empty input would require an explicitly defined behavior, but adding one is unnecessary under this contract.

- **Repeated calls:** Each invocation reruns independent random decisions. The results may repeat, and repetition is not evidence of bias. Random sampling is with replacement across calls because selecting a node does not remove it.

- **Very large or unknown lists:** The algorithm never needs the final length in advance and uses constant auxiliary memory. It can process nodes as they arrive, provided the stream eventually ends so the method can return.

- **An infinite stream:** Reservoir sampling always maintains a fair sample of the finite prefix seen so far, but `getRandom()` cannot return after traversing a truly infinite stream. The linked-list contract guarantees a finite number of nodes.

- **Random-number boundaries:** `randint(1, n)` includes both endpoints. This inclusion is essential: there are exactly $n$ equally likely outcomes, and one of them triggers replacement. Using an API with an exclusive upper bound would require adjusting the arguments and comparison.

- **Mutating the list during a draw:** The proof assumes one stable finite sequence for the duration of traversal. Concurrent structural mutation could skip, repeat, or indefinitely extend nodes, so synchronization would be necessary in a different concurrent contract.
