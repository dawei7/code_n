# Search Suggestions System

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1268 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, String, Binary Search, Trie, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/search-suggestions-system/) |

## Problem Description

### Goal

You are given an array of product-name strings `products` and a string `searchWord`. Build a suggestion system that responds after every character of `searchWord` is typed. At each step, a product is eligible only when it starts with the entire prefix typed so far.

Return at most three eligible names for each prefix. When more than three products share that prefix, choose the three lexicographically minimum product names. The final result must contain one suggestion list for every successive character of `searchWord`, in typing order.

### Function Contract

**Inputs**

- `products`: an array of $n$ unique strings made of lowercase English letters, where $1 \le n \le 1000$.
- `searchWord`: a lowercase English string of length $m$, where $1 \le m \le 1000$.

The total number of characters across all product names is

$$
S = \sum_{p \in \texttt{products}} \lvert p \rvert,
$$

where $1 \le S \le 2 \cdot 10^4$.

**Return value**

- Return a list of $m$ lists. Entry $k$ contains the lexicographically smallest three or fewer products beginning with `searchWord[:k + 1]`.

### Examples

**Example 1**

- Input: `products = ["mobile","mouse","moneypot","monitor","mousepad"]`, `searchWord = "mouse"`
- Output: `[["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]`

**Example 2**

- Input: `products = ["havana"]`, `searchWord = "havana"`
- Output: `[["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]`

**Example 3**

- Input: `products = ["bags","baggage","banner","box","cloths"]`, `searchWord = "bags"`
- Output: `[["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]`

### Required Complexity

- **Time:** $O(S+m)$
- **Space:** $O(S+m)$

<details>
<summary>Approach</summary>

#### General

**Store every searchable prefix once**

Build a trie containing every product name. A trie node represents one product prefix, and its outgoing edges represent the possible next lowercase letters. Mark the terminal node of each product with that complete name. Inserting all names touches exactly $S$ characters.

Each prefix node also needs its three lexicographically minimum products. Filling those lists during arbitrary insertion would require repeatedly comparing product names. Instead, traverse the completed trie in lexicographic order. A terminal is visited before its descendants, and child edges are visited from `a` through `z`, so complete products appear in exactly lexicographic order.

**Let the first three visits settle each prefix**

Maintain the trie-node path during the lexicographic traversal. When a terminal product is reached, offer that product to every non-root node on its path. Append it only while that node has fewer than three suggestions. Because terminals arrive in lexicographic order, the first three products recorded at a node are precisely the three minimum names having that node's prefix. Later products cannot improve its list.

Every terminal product walks its own prefix path once during this filling phase. Summed across all terminals, that is another $S$ node visits. Iterating the fixed lowercase alphabet at trie nodes adds only a constant factor.

**Follow the typed word without searching the corpus again**

Start at the trie root and follow one edge per character of `searchWord`. After each successful step, copy that node's stored list into the answer. If an edge is missing, the current prefix has no matching product; every longer prefix is also impossible, so append empty lists for the remaining characters.

For any typed prefix, the traversal reaches exactly the trie node representing it. The construction placed at that node the first three terminal products in lexicographic order among all names below it. Those names are therefore exactly the required suggestions, which establishes the result for every answer position.

#### Complexity detail

Trie construction and the lexicographic filling phase each process $O(S)$ character or path entries. Following `searchWord` and copying lists of at most three references takes $O(m)$ time, so the total is $O(S+m)$.

The trie, terminal references, traversal stack, and stored suggestion references use $O(S)$ auxiliary space. The returned list contains $m$ inner lists of at most three references, using $O(m)$ additional space; together they use $O(S+m)$ space.

#### Alternatives and edge cases

- **Sort and narrow two pointers:** Sorting products and shrinking a lexicographic interval after each character is concise, but string comparisons give it a larger worst-case preprocessing bound than the trie construction.
- **Binary search for every prefix:** Two boundary searches in a sorted product array avoid scanning all products, but repeatedly comparing progressively longer prefixes adds logarithmic searches and string-comparison work.
- **Filter every product after every keystroke:** This direct method is correct, but it can inspect all $n$ products for each of the $m$ prefixes.
- **More than three matches:** A node stops accepting products after its first three lexicographic terminals; later matches cannot displace them.
- **A product equals the prefix:** A terminal is visited before longer descendants, so the shorter product correctly precedes its extensions.
- **No match:** Once trie traversal misses an edge, the current and all later suggestion lists are empty.
- **One product:** Every prefix of `searchWord` that it contains returns that single product, with no special handling.

</details>
