## General

**Model accounts as connected components**

Each row begins with a name and then lists email addresses. Two account rows describe the same person when they share at least one email. That relationship is transitive: if account A shares an email with B, and B shares another email with C, all three accounts belong to one merged person even if A and C have no email directly in common.

This is a connectivity problem. Treat every account index as a node. A shared email creates an edge between the account rows containing it. The desired merged accounts are exactly the connected components of this implicit graph.

The exact solution finds those components with a disjoint-set union structure, also called union-find. It does not explicitly store every graph edge. Instead, it discovers shared emails while scanning the accounts and immediately joins the corresponding account indices.

**What the union-find arrays mean**

For `n` account rows, `p[i]` is the current parent of account index `i`. Initially every account is its own component, so `p[i] = i`. A root is an index whose parent is itself.

The `size` array stores the number of union-find nodes in each root’s component. It is meaningful at roots and helps keep trees shallow.

The `find(x)` operation follows parent pointers until it reaches the component root. On the recursive return path it performs path compression by assigning `p[x]` directly to that root. Future finds from the same path become faster.

The `union(a, b)` operation finds both roots. If the roots already match, the accounts are already connected and nothing changes. Otherwise, the smaller component is attached below the larger component and the new root’s size is updated. In an equal-size tie, this exact code attaches `pa` under `pb` because it uses `>` rather than `>=`. Either tie direction is correct.

**Use each email as evidence of a connection**

The dictionary `d` maps an email to one account index where that email was previously seen.

While scanning account `i`:

- If an email is new, store `d[email] = i`.
- If it was seen before in account `d[email]`, union `i` with that stored account.

There is no need to retain a list of every account for each email. The first observed account serves as a hub. If the same email appears in five accounts, unioning the later four with the first connects all five into one component.

This scan also handles chains across different emails. Suppose account 0 shares `a@mail` with account 1, while account 1 shares `b@mail` with account 2. The first shared email unions 0 and 1; the second unions 1 and 2. Union-find then gives all three the same root, correctly applying transitivity.

The account name is deliberately not used as a union key. Different people may have the same name, so equal names alone do not prove identity. Conversely, the problem guarantees that all account rows belonging to the same person have the same name, making it safe to choose the name later from any component member.

**Gather emails after all unions are known**

The solution performs a second pass through the accounts. For every account index `i`, it calls `uf.find(i)` to obtain its final root and adds all emails from that row into `g[root]`.

This pass happens after all unions because a root observed midway through the first scan might later be attached beneath another root. Grouping only after connectivity is complete avoids maintaining and merging email collections during every union.

Each group uses a set. The set removes duplicates if an email appears in multiple account rows in the same component, which is exactly why those rows were connected. It also protects against repeated occurrences without relying on their input arrangement.

**Build the requested output**

For each root and its email set, the solution creates

`[accounts[root][0]] + sorted(emails)`.

The first item is the name taken from the root’s original account. This is valid because every account in one component represents the same person and therefore has the same name under the problem guarantee.

The emails are sorted because each merged account must list them in sorted order. The collection of merged account rows itself may appear in any order, so iteration order over `g.items()` does not need an additional outer sort.

**A transitive example**

Consider these conceptual rows:

- Account 0: name Alex, emails `a@mail` and `b@mail`.
- Account 1: name Alex, emails `b@mail` and `c@mail`.
- Account 2: name Alex, emails `c@mail` and `d@mail`.

When `b@mail` is encountered in account 1, accounts 1 and 0 are united. When `c@mail` is encountered in account 2, accounts 2 and 1 are united. All three then have one root even though account 0 and account 2 never directly share an email.

The second pass inserts all four unique addresses into that root’s set, and the output sorts them. This is precisely the transitive merge required.

**Why the component construction is correct**

Every union is justified by a shared email, so it never joins accounts without evidence that they belong to the same person. Therefore any two indices that end in one union-find component are connected by a chain of shared-email relationships and should be merged.

In the other direction, every occurrence after an email’s first occurrence is unioned with that first account. Thus all accounts sharing a direct email are connected. Union-find’s transitivity then connects every path in the implicit graph. No required connection is omitted.

The grouping pass places every account’s emails under its final component root, and the set produces exactly the union of addresses from that component. Hence every output row contains all and only the emails belonging to one connected person, with duplicates removed and the email portion sorted.

## Complexity detail

Let `A` be the number of account rows, `E` the total number of email occurrences across all rows, and `U` the number of distinct emails.

The first pass handles every email occurrence once. Each repeated email can cause a constant number of union-find operations. With path compression and union by size, a sequence of operations costs `O((A + E) alpha(A))`, where `alpha` is the inverse Ackermann function and grows so slowly that it is effectively constant for practical input sizes.

The second pass again visits all `E` email occurrences and performs one find per account row. Building the sets is expected `O(E)` under normal hash-table behavior.

Finally, emails are sorted separately inside their components. If component email counts are `u1, u2, ...`, the exact sorting cost is the sum of `O(ui log ui)`. This is at most `O(U log U)`. A clear combined bound is `O((A + E) alpha(A) + U log U)` expected time, often simplified to `O(E log E)` because `U <= E` and account metadata is small relative to email occurrences.

Union-find uses `O(A)` space. The email-owner map and grouped sets use `O(U)` stored email keys, excluding references already held by the input. The returned rows contain `O(U)` emails. Auxiliary storage is therefore `O(A + U)`, customarily written as `O(A + E)` or `O(E)` when every account has at least one email.

## Alternatives and edge cases

- **Explicit account graph plus DFS or BFS:** Connect account indices that share emails, then traverse connected components. This is correct but may store more adjacency data than union-find. Care is needed not to create a quadratic clique for an email appearing in many accounts; connecting all occurrences to one representative is sufficient.

- **Email-node graph:** Treat emails as vertices, connect all emails within each account, and traverse components. This also works and can associate a name with each component, but it creates graph edges and traversal state that the union-find solution avoids.

- **Union emails instead of accounts:** Assign an identifier to every unique email and union addresses appearing in the same row. This is a valid design, but the exact solution’s account-index nodes make selecting a guaranteed component name particularly direct.

- **Merge by name:** This is incorrect because two different people can share the same name. Only shared email addresses establish a merge.

- **Shared email appearing many times:** Every later account is unioned with the first stored owner. A star of unions connects all occurrences without storing every pairwise relationship.

- **Transitive but not direct overlap:** Union-find is specifically valuable here. A chain of different shared emails collapses into one component even when the endpoints have no email in common.

- **Duplicate emails in merged rows:** The grouping set removes repeated addresses before sorting and output.

- **Several disconnected people with the same name:** They retain different roots because no email causes a union. They correctly appear as separate result rows.

- **Root choice changes:** Union by size may choose any account index as root, and path compression may update parents. The chosen root does not affect the email set, and the name remains valid because a component’s accounts have matching names.

- **Result row ordering:** Only the emails within each row must be sorted. The problem permits the outer rows in any order, so dictionary iteration order is acceptable.
