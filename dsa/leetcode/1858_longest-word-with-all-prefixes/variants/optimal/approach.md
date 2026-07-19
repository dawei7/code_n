## General
**Represent every prefix once**

Insert every input word into a trie. Each trie edge consumes one character, and
mark the terminal node of each inserted word with that word. A root-to-node
path therefore represents one distinct prefix shared by every word that begins
with that path.

**Traverse only complete chains**

Start at the root and visit a child only when that child is a terminal node.
This restriction exactly encodes the requirement: reaching a node at depth
$d$ means that the nodes at depths $1$ through $d$ were all terminal, so every
nonempty prefix of the node's word occurs in the input. Conversely, every
eligible word has terminal nodes at all those depths, so this traversal cannot
skip it.

Use an explicit stack rather than recursive depth-first search. An individual
word may contain $10^5$ characters, which can exceed a language runtime's call
stack even though the trie itself is valid. Whenever a reachable terminal word
is longer than the current answer, replace the answer; on equal lengths,
replace it only when it is lexicographically smaller. Because every and only
eligible word is compared, the final selection satisfies both ordering rules.

## Complexity detail
Trie insertion processes each of the $S$ input characters once. Traversal
examines at most every created edge once, so total time is $O(S)$. The trie has
at most $S+1$ nodes, and its child maps, terminal references, and explicit
stack use $O(S)$ auxiliary space.

## Alternatives and edge cases
- **Hash set plus every-prefix checks:** storing all words in a set is compact,
  but materializing and hashing every prefix of every word can take
  $O(\sum \lvert w \rvert^2)$ time in languages where slicing copies strings.
- **Length-ordered dynamic construction:** sorting by length and accepting a
  word when `word[:-1]` was already accepted is simple, but sorting adds
  $O(n \log n)$ comparisons and prefix slicing still needs care.
- A missing one-character prefix blocks its entire trie branch, even if many
  longer strings from that branch appear in `words`.
- A one-character input word is eligible by itself because its only nonempty
  prefix is the word itself.
- Input order has no effect, and the lexicographic rule applies only after
  maximum length has been determined.
