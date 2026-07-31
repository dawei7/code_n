## General

Build a trie from every string in `words`. Each trie node represents a prefix of at least one word, so merely reaching a node proves that the consumed characters form a valid string; no terminal marker is needed.

Let `best[i]` be the minimum number of valid strings whose concatenation is `target[:i]`. Start with `best[0] = 0` and every other state unreachable. From each reachable position `start`, walk forward through both `target` and the trie. Every successful step ending at index `end` identifies the valid piece `target[start:end + 1]`, so it can update `best[end + 1]` with `best[start] + 1`. Stop that walk as soon as the required trie edge is absent.

Each update appends one verified word prefix to an already valid construction, so it never creates an invalid state. Conversely, consider the final piece of any construction of `target[:i]`: its starting position is an earlier reachable state, and the trie walk from that position visits its ending position. The transition therefore considers every possible final piece. Taking the minimum makes every `best[i]` optimal, including the full target.

## Complexity detail

Let $S$ be the sum of the lengths of `words` and $T$ be the length of `target`. Building the trie takes $O(S)$ time and space. In the worst case, the trie walk starting at each target position scans the entire remaining suffix, totaling $O(T^2)$ time. The dynamic-programming array uses $O(T)$ space, so the combined bounds are $O(S + T^2)$ time and $O(S + T)$ space.

## Alternatives and edge cases

- **Explicit prefix set:** Materializing every prefix as a separate string can duplicate shared characters and makes substring construction or hashing part of each transition.
- **Rolling hash plus range optimization:** Hashing and greedy or segment-tree techniques can improve the large-target variant, but they add collision handling and are unnecessary for this problem's $T \le 5000$ bound.
- **Whole words only:** A valid piece may be any nonempty prefix, even when it is not itself present as a full entry in `words`.
- **Repeated use:** The same valid prefix may be selected more than once; the dynamic program imposes no consumption limit.
- **Unreachable suffix:** If every trie walk from reachable positions stops before covering the target, the final state remains unreachable and the answer is `-1`.
