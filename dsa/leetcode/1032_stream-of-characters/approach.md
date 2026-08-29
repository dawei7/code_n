## General

**A query asks about suffixes ending now**

After each new letter arrives, every candidate answer must end at that newest letter. The uncertainty is only how far backward the candidate suffix begins.

Searching every word forward would require trying many different suffix starting positions. Reversing the viewpoint removes that branching. If a word is stored backward, then reading the stream from newest character to oldest follows a single path from the trie's root.

For example, word `"cd"` is inserted as `"dc"`. When the stream ends in `"...cd"`, searching its characters backward reads `d` and then `c`, exactly the stored trie path. A suffix match in forward order becomes a prefix match in reversed order.

**Trie node structure**

Each `Trie` node has `children`, a list of 26 possible next nodes, and `is_end`, which marks whether some complete reversed word ends there.

For lowercase character `c`, `ord(c) - ord('a')` maps `a` through `z` to indices zero through 25. A fixed child array avoids hash lookups and is safe because both words and query letters are guaranteed lowercase English letters.

The constructor inserts every word. In `insert`, `w[::-1]` visits its letters from last to first. A missing child node is created; an existing child is reused, allowing words with common suffixes in normal order to share trie prefixes after reversal.

After the final reversed character, `node.is_end = True` records a complete word. Reinserting a duplicate word simply follows the same path and sets the same flag again.

**Store arriving letters**

`StreamChecker` keeps all received letters in `self.cs`. Every call to `query` appends the new letter before searching, ensuring the current suffix includes that letter.

Only a bounded recent suffix can match. The maximum word length is 200, and a suffix longer than every word cannot be equal to a word. The exact code passes `self.cs[-self.limit:]` with `self.limit = 201`. This creates a list containing at most the most recent 201 characters.

Using 201 rather than 200 is harmless. Every trie path representing a word ends by depth 200 at the latest. If a terminal node is reached, search returns true immediately before an extra older character matters. If no terminal is reached within 200 steps, no dictionary word matches; the possible 201st step cannot create a word longer than the allowed maximum.

**Search from newest to oldest**

The slice is in ordinary chronological order, but `Trie.search` loops over `w[::-1]`. Its first processed character is therefore the newest stream letter.

At each character:

- Compute its child index.
- If that child does not exist, return `False`. No stored reversed word begins with the characters already read, so no suffix can match.
- Move to the child.
- If `node.is_end` is true, return `True`. The processed newest-to-oldest characters form a complete reversed word, meaning the corresponding forward characters form a stream suffix.

The early terminal test is essential because a shorter word may be a suffix of the current stream even when more old characters are available. For words `"f"` and `"kl"`, a query ending in `f` must return true after one trie edge; it must not require the entire retained stream to match.

If the loop finishes without reaching a terminal, it returns `False`. Following a trie prefix is not enough; some complete word must end there.

**Trace the example**

The words `"cd"`, `"f"`, and `"kl"` are inserted as paths `d -> c`, `f`, and `l -> k`.

After queries `a` and `b`, reverse search begins with letters that have no root path, so both return false.

After `c`, the newest letter `c` still has no matching root edge because `"cd"` must end in `d`, not `c`.

After `d`, search follows root edge `d` and then edge `c`. The second node is terminal, so the current stream suffix `"cd"` matches and returns true.

After `f`, the first edge `f` already reaches a terminal node, so the one-character suffix matches.

After `l` following `k`, reverse search follows `l` then `k` and recognizes `"kl"`.

Older letters before each suffix do not matter because the method returns as soon as a terminal path is found.

**Why a missing edge proves failure**

Suppose the reversed scan has followed characters corresponding to the most recent suffix and the next required trie edge is absent. Every stored word matching the stream would need exactly that sequence as the beginning of its reversed form. Since no trie path has it, no longer candidate can repair the mismatch. Returning immediately is safe.

This prefix-pruning is the main benefit of the trie. Search work often stops long before reaching the maximum word length.

**Why the result is correct**

If search returns true at a terminal node after reading `k` characters backward, those characters equal a stored reversed word of length `k`. Reversing both sides shows that the last `k` stream characters equal the original word, so a valid nonempty suffix exists.

Conversely, suppose the stream has a suffix equal to some stored word. Insertion created a trie path for that word's reversed characters and marked its final node. The bounded slice contains the entire suffix because its length is at most 200. Backward search follows that path and reaches the terminal, returning true. Thus the query result is true exactly when at least one stored word is a current suffix.

**Persistent state across calls**

The trie is constructed once and reused. Query results do not reset `self.cs` because later suffixes may include letters from earlier calls. The current call adds only one character, and the search always anchors at the newest end.

The exact implementation retains the full history list even though it searches only the last 201 characters. Trimming the list would preserve answers and reduce persistent stream storage, but the provided source chooses simpler append-only history.

## Complexity detail

Let `S` be the total number of characters across all input words, `W` the maximum word length, and `Q` the number of query calls.

Trie construction processes each word character once, taking `O(S)` time. Each query copies a slice of at most `W + 1` characters and searches at most that many trie edges, so one query costs `O(W)` and all queries cost `O(QW)`. Total time is `O(S + QW)`, matching the manifest.

The trie has at most one new node per inserted character. Each node holds 26 child slots, which is a constant alphabet factor, so trie storage is `O(S)`.

The manifest records `O(S + W)` active matching space: trie storage plus the bounded slice examined by one query. The exact source additionally keeps every received character in `self.cs`, so its persistent object storage after `Q` calls is more precisely `O(S + Q)`, with an `O(W)` temporary slice per query. Trimming `self.cs` to its last `W` characters would make the implementation itself meet the manifest's bounded-history expression.

## Alternatives and edge cases

- **Forward trie with every suffix start:** Store words normally and try searches from several recent positions after each query. This repeats work across candidate lengths; reversal turns them into one root-to-leaf scan.
- **Hash set of words:** Build every suffix of the recent stream and test membership. At most `W` suffixes exist, but materializing them can cost `O(W^2)` characters per query.
- **Aho-Corasick automaton:** Failure links can process each new character incrementally and report suffix matches efficiently. It offers stronger streaming performance but is substantially more complex than a reversed trie for `W <= 200`.
- **Store a bounded deque:** Keeping only the latest `W` characters is sufficient and changes persistent stream history from `O(Q)` to `O(W)`.
- **One-character word:** The first child reached during search is terminal, so any query with that letter returns true immediately.
- **A word that is a suffix of another word:** The shorter word's terminal appears before the longer path ends. Early return correctly accepts the shorter suffix.
- **Duplicate words:** Reinsertion reuses nodes and leaves the same terminal flag true; behavior is unchanged.
- **Shared normal suffixes:** Words such as `"cd"` and `"ad"` share root edge `d` in the reversed trie, saving nodes.
- **Stream shorter than every word:** The slice contains the entire stream, and search returns false unless a complete shorter word actually ends along its path.
- **Stream much longer than 200:** Only recent characters can participate in a matching word. Older history is ignored by search even though the exact list retains it.
- **Why 201 is safe:** It is one larger than the maximum word length, but no valid trie terminal requires that extra character and successful search returns before it.
- **Missing first edge:** If no word ends in the newest letter, search rejects after one step because every valid suffix must end there.
- **Lowercase contract:** Array indexing assumes characters from `a` through `z`. Other characters could produce invalid indices and are outside the source domain.
- **Nonempty words:** No terminal is placed at the trie root, matching the requirement that the reported suffix and every input word are nonempty.
