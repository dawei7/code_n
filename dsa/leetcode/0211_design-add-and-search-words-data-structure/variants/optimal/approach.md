## General

**Why ordinary membership storage is not enough**

`addWord` stores literal lowercase words, but `search` accepts patterns in
which `.` can stand for any one lowercase letter. A hash set can answer an
ordinary exact lookup efficiently, yet a pattern such as `.ad` represents up
to 26 concrete strings. Generating all replacements and looking each one up
would repeat prefix work and scale poorly as the number of wildcards grows.

A trie stores words by their prefixes. Each edge consumes one character, so a
literal query follows one edge while a dot can branch to every existing edge
at that same depth. Crucially, it explores only prefixes that were actually
inserted rather than blindly constructing every theoretical replacement.

**What one trie node records**

The exact solution defines a small `Trie` node class. Every node contains a
26-element `children` list and an `is_end` boolean. Child position 0 represents
`a`, position 1 represents `b`, and position 25 represents `z`; `None` means
that no stored word continues through that letter. `is_end` distinguishes a
complete inserted word from a path that exists only as a prefix of a longer
word.

`WordDictionary` owns one root node in `self.trie`. The root represents the
empty prefix. If `bad`, `bake`, and `dad` have been inserted, the first two
words share the root's `b` child and the next `a` child, then diverge. The word
beginning with `d` uses another root child. Prefix sharing is the reason the
trie can avoid repeatedly storing and checking the same beginning.

**Adding a word preserves all previously stored words**

`addWord` begins at the root. For every character `c`, it computes
`ord(c) - ord('a')`, which is an index from 0 through 25 under the lowercase
input guarantee. If the corresponding child is absent, the method creates a
new `Trie` node there. It then moves into that child whether it was new or
already present.

After consuming the whole word, it sets `node.is_end = True`. The flag is set
only at the final node. If `bad` is inserted, the nodes for `b` and `ba` exist,
but neither becomes a stored word accidentally. Inserting `ba` later reuses
those nodes and marks the `ba` node without damaging the longer `bad` route.
Inserting an already stored word is idempotent: its path is reused and its
already-true endpoint flag remains true.

**Literal search follows a single forced route**

The public `search` method defines a recursive helper, also named `search`, and
starts it with the complete pattern and root node. Inside one helper call, a
`for` loop scans characters from left to right.

For an ordinary lowercase character, only one child can match. If that child
is `None`, no inserted word can match this pattern, so the helper immediately
returns `False`. Otherwise it assigns that child to `node` and continues with
the next pattern position. If the loop reaches the end, it returns
`node.is_end`. This last test enforces complete-word matching: a path spelling
`ba` is not enough to match `ba` when only `bad` was inserted, because the
`ba` node is not marked as an ending.

The code calculates `idx = ord(c) - ord('a')` before checking whether `c` is a
dot. For `c == '.'`, that numerical value is negative, but it is never used to
index `children`: the expression checking a missing literal begins with
`c != '.'`, and Python short-circuits before evaluating the child access when
that condition is false. The wildcard branch then iterates over children
directly.

**A dot creates a choice among existing children**

When the current character is `.`, exactly one arbitrary lowercase letter
must be consumed. The helper loops through all 26 child positions of the
current node. For each non-`None` child, it recursively searches the unconsumed
suffix `word[i + 1:]` starting from that child.

This recursive call models one concrete choice for the dot. Moving to a child
consumes exactly one trie edge, while slicing away positions through `i`
ensures the recursive call begins at the next unmatched pattern character. If
any choice can match the complete suffix, the helper returns `True`
immediately. That short-circuit can save most of the potential work when a
successful branch is found early.

If every existing child fails, the wildcard cannot be matched and the helper
returns `False`. The immediate return after the child loop is intentional. The
current frame must not fall through and continue its original `for` loop,
because the recursive call—not the current node—owns all positions after the
dot.

**Trace the wildcard example**

Suppose `bad`, `dad`, and `mad` have been added. Searching for `.ad` starts at
the root and sees a dot at position 0. It tries each existing first-letter
child. Under the `b` child, the recursive call receives `ad`. It follows the
literal `a` edge and then the literal `d` edge. The suffix ends at the node
marked by insertion of `bad`, so that branch returns `True`; the remaining
root children need not be explored.

Searching for `pad` follows no wildcard at the first position. The root has no
`p` child, so it returns `False` immediately. Searching for `b..` first follows
the forced `b` edge. The first dot branches among children below `b`; only
existing paths are tried. Choosing `a` leads to the second dot, where choosing
`d` reaches the end node for `bad`, making the pattern match.

**Why the recursive search returns exactly the right answer**

At any helper call, `node` represents the prefix already matched by earlier
choices. A literal character preserves this fact only by moving along its one
matching edge. A dot preserves it by considering every existing one-letter
extension, which covers all and only allowed substitutions. Thus every
recursive path corresponds to one possible interpretation of the dots, and no
legal interpretation is omitted.

Reaching the end returns true only at a node marked by `addWord`, so a
successful path has the same length as the query and represents a complete
stored word. Conversely, if a stored word matches the pattern, its next edge
is followed at every literal and is among the children tried at every dot; the
search can reach its marked endpoint and return true. This covers both sides:
the algorithm cannot invent a match, and it cannot miss a real one.

The manifest summary currently says the branch uses an “iterative frontier,”
but the exact source uses recursive depth-first branching with suffix slices.
This document follows the executable source. The two strategies express the
same trie search idea, but their temporary-state behavior is not identical.

## Complexity detail

Let $L$ be the length of the added word or search pattern, let $d$ be the
number of dots in a query, let $B$ be the maximum number of existing children
examined at a wildcard node with $B \le 26$, and let $T$ be the number of trie
nodes created across all insertions.

`addWord` processes each character once, so it takes $O(L)$ time. It creates at
most $L$ nodes, giving $O(L)$ additional persistent space for that call in the
worst case and no new nodes when the entire path already exists.

A search without dots follows one path in $O(L)$ time. Wildcards can branch,
and in the worst case the search explores up to $B^d$ relevant paths, with
character scanning and Python suffix-slice creation across them. The stated
upper bound is $O(LB^d)$ time. The problem limits a search to at most two dots,
but branching can still be significant when many matching prefixes exist.

The persistent dictionary occupies $O(T)$ nodes. Each node contains 26
references, and 26 is a fixed constant, so the arrays do not change that
asymptotic bound. A literal query uses constant traversal state. Wildcard
search adds recursive frames only when a dot is encountered; branches are
explored sequentially rather than stored simultaneously. The recursion depth
is at most $d+1$, while the created suffix strings can total $O(dL)$ live space
along one recursion path, which is $O(L)$ under the stated two-dot constraint.
Persistent trie storage remains the manifest's dominant $O(T)$ structure.

## Alternatives and edge cases

- **Iterative frontier of nodes:** Keep every node that can match the current pattern prefix, replacing the frontier with matching literal children or all children for a dot. It avoids recursion and substring slices but can hold a broad set of nodes at once; it is the method described by the manifest summary, not by the exact source file.
- **Nested dictionaries with an end sentinel:** A map stores only present character edges and naturally supports sparse alphabets. It may save empty child slots but adds hashing and per-entry overhead; the fixed array exploits the lowercase-only contract.
- **Words grouped by length in hash sets:** Search only words of the pattern's length and compare characters with dot matching. It is simple, but a query can scan every stored word of that length, giving $O(NL)$ time for $N$ candidates.
- **No dots:** Search follows exactly one route and never recurses, so a missing character fails immediately and a complete route still requires `is_end` at its endpoint.
- **A dot at the first character:** The root's existing children are the complete set of possible first letters. Empty slots are skipped, so the search never explores letters absent from all stored words.
- **Consecutive dots:** Each recursive level consumes exactly one dot and one edge. A pattern such as `b..` therefore matches only three-letter words beginning with `b`, not shorter or longer words.
- **A prefix but not a word:** If the pattern is exhausted at an unmarked internal node, the helper returns false even if that node has children. Matching must consume an entire added word of the same length.
- **An added word that prefixes another:** Both can be represented by marking the shorter endpoint while retaining its children. Searches for either length consult the appropriate endpoint flag.
- **Duplicate additions:** Reusing a path and assigning `True` again does not create duplicate logical entries. The required structure records membership, not frequency.
- **Maximum input sizes:** Words have length at most 25 and queries contain at most two dots, keeping recursion shallow. Up to $10^4$ operations can still build many nodes, so sharing prefixes remains valuable.
- **Lowercase and dot preconditions:** `addWord` accepts only lowercase letters, and only search patterns may contain dots. The fixed-index calculation and wildcard branch assume those guarantees; other characters are outside the contract.
- **Input preservation:** The implementation reads each supplied string and creates slices during wildcard recursion, but strings are immutable and the caller's values are never changed.
