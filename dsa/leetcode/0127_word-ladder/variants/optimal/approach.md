## General

Words form an unweighted graph: each allowed dictionary word is a vertex, and two vertices are adjacent when they differ in exactly one position. `beginWord` is the starting vertex even if it is not in the dictionary.

The shortest number of transformations in an unweighted graph is found by breadth-first search. The selected solution generates one-letter mutations on demand instead of building every graph edge in advance.

**Why BFS gives the shortest ladder**

The queue is processed in layers. Layer zero contains `beginWord`; the next layer contains dictionary words reachable with one change; the following layer contains words reachable with two changes, and so on.

BFS completely processes all words at a smaller distance before any word at a larger distance. Therefore the first time `endWord` is discovered, no shorter transformation can exist.

The method can return immediately on discovery because only the shortest length is requested. Unlike Word Ladder II, it does not need to finish the layer to collect alternative shortest parents.

**How `ans` counts words rather than edges**

`ans` starts at one because a sequence containing only `beginWord` has one word before any transformation.

At the beginning of each outer queue iteration, the source increments `ans`. The current queue layer then generates its next-layer neighbors. If one of them is `endWord`, that new endpoint makes the sequence one word longer, so the current `ans` is returned.

For a direct one-letter transformation, the first outer iteration changes `ans` from one to two and returns two, correctly counting both endpoints.

**The queue-layer invariant**

At the start of one outer iteration, all queued strings are at the same transformation distance from `beginWord`.

`range(len(q))` captures that layer's size before new neighbors are appended. The inner loop removes exactly those words. Newly discovered words wait in the queue for the next outer iteration, preserving level order.

If the code processed the growing queue without a fixed size, it could mix distances and make the shared `ans` value inaccurate.

**Generating candidate neighbors**

For a current string, the source creates mutable character list `s`. At every position it tries all 26 lowercase letters, joins the list into candidate `t`, and restores the original character after finishing that position.

Any candidate accepted from `words` differs in at most one position and belongs to the allowed dictionary. A candidate using the original character equals the current word; normally it has already been removed and is ignored.

Replacing one position at a time covers every possible dictionary neighbor, so no valid next transformation is missed.

**Why immediate removal is safe**

When a valid candidate is first discovered, it is appended to the queue and removed from `words`.

If another current-layer parent can also reach it, enqueueing it again is unnecessary for a length-only problem. Both routes have the same distance, and future reachability from that word is identical.

Immediate removal therefore prevents duplicate work and cycles without losing a shorter answer. A later layer also cannot re-add the word and create a longer redundant route.

**The `beginWord` dictionary nuance**

The source does not remove `beginWord` from `words` before the search. If the input dictionary happens to contain it, generating the unchanged character at each position can find the start itself on the first expansion.

The first such occurrence enqueues `beginWord` once and removes it. This creates one redundant later visit, but not an infinite loop. Its useful neighbors were already removed when first discovered, and `beginWord != endWord` by contract.

Discarding `beginWord` before BFS would avoid this extra work and make every accepted mutation differ by exactly one letter rather than possibly zero on that one occasion.

**Why missing `endWord` still returns zero**

The source has no explicit early check for `endWord in words`. If it is absent, no generated candidate can equal it while also passing `t in words`.

The BFS eventually exhausts every reachable dictionary word and returns zero. An early membership test would save work but is not required for correctness.

**Tracing `hit` to `cog`**

Layer one contains `hit` and uses `ans = 2` while generating `hot`. The next expansion uses `ans = 3` and discovers `dot` and `lot`.

The next layer discovers `dog` and `log` with sequence length four. Expanding either at the following layer generates `cog`, and `ans = 5` is returned.

The method does not reconstruct whether the route used `dot` or `lot`; both have the same shortest word count.

**Exact source dependencies**

The annotation uses `List[str]`, and the queue uses `deque`, but neither is imported. A standalone module needs `from typing import List` and `from collections import deque`.

The input list itself is not mutated. `set(wordList)` creates a separate membership structure that is destructively reduced.

## Complexity detail

Let $W$ be dictionary size and $L$ the common word length. Each word is normally enqueued at most once and tries $26L$ mutations.

In Python, joining a length-$L$ character list and hashing the resulting candidate take $O(L)$, so worst-case time is $O(WL^2)$. The redundant start visit, when applicable, adds only one word's mutation work.

The dictionary set, queue, and mutable character list use $O(W+L)$ references/characters beyond the input, commonly summarized as $O(WL)$ when counting stored string data or $O(W)$ additional references because the set reuses input string objects.

The manifest's generic $O(N)$ time and space can be understood only when word length and the fixed alphabet are treated as bounded constants. With $L\le10$, that simplification is practical, but the explicit bound explains the string operations.

The integer output uses constant space.

## Alternatives and edge cases

- **Bidirectional BFS:** Search from both endpoints and expand the smaller frontier. It often reduces the explored search space substantially.
- **Wildcard buckets:** Precompute patterns like `h*t` to retrieve neighbors sharing one erased position. This trades preprocessing space for faster adjacency lookup.
- **Compare against every dictionary word:** Checking one-character difference costs $O(WL)$ per expanded vertex and can become quadratic in word count.
- **Queue full paths:** Unnecessary when only length is requested and duplicates prefixes in memory.
- **Remove `beginWord` initially:** Avoids the exact source's possible redundant self-enqueue.
- **Check missing `endWord` first:** Returns zero without BFS.
- **Direct one-letter route:** Returns two because both endpoint words count.
- **No route:** Queue exhaustion returns zero.
- **Begin absent from dictionary:** Fully supported because it is seeded directly.
- **Unique dictionary words:** The set conversion preserves all allowed vertices.
- **Same-character mutation:** Usually filtered by prior removal; explicitly skipping it would reduce candidate work.
- **Immediate visited marking:** Removing on enqueue is necessary to avoid duplicate queue entries.
- **First discovery:** Safe to return because BFS layers are ordered.
- **Missing imports:** `List` and `deque` must be supplied.
- **Output meaning:** Return words in the sequence, which is one more than the number of transformation edges.
