## General

**Model pages and links as a directed graph**

Treat every URL as a graph vertex. A call to `htmlParser.getUrls(url)` reveals the outgoing edges from that vertex. Starting from `startUrl`, the task is to traverse all reachable vertices while refusing edges whose destination has a different hostname.

The exact solution uses recursive depth-first search. The set `ans` serves two purposes: it records the answer and marks pages already visited.

**Extract a hostname under the stated URL format**

Every URL uses the literal `http://` prefix and has no port. The helper `host(url)` removes the first seven characters with `url[7:]`, leaving the hostname and optional path. Splitting that remainder on `'/'` and taking element zero returns the hostname.

For `"http://news.yahoo.com/news"`, removing seven characters gives `"news.yahoo.com/news"`, and the first split component is `"news.yahoo.com"`. For a URL with no path, the entire remainder is the hostname.

This parser is intentionally tied to the contract. It is not a general URL parser: `https://` has a different prefix length, ports would be included in the host text, and other URL features would need a standard parsing library.

**Mark a page before following its links**

`dfs(url)` first checks `if url in ans`. If the page was already seen, it returns immediately. Otherwise, it adds the URL to `ans` before asking the parser for outgoing links.

Marking before recursion is essential. The graph can contain cycles such as A linking to B and B linking back to A. If A were marked only after finishing B, the back edge would recursively enter A again forever. Early marking makes every subsequent visit to A stop.

It also guarantees that `htmlParser.getUrls(url)` is called at most once for each crawled URL.

**Filter every outgoing edge by hostname**

For every `next` URL returned by the parser, the code compares `host(url)` with `host(next)`. The current `url` was reached only through same-host edges from `startUrl`, so its hostname equals the starting hostname. Comparing the neighbor with the current page is therefore equivalent to comparing it directly with `startUrl`.

If the hostnames match, `dfs(next)` explores the neighbor. The membership guard at the beginning of `dfs` prevents duplicate work. If they differ, the edge is ignored and the off-host page is never added or queried.

The local variable name `next` shadows Python’s built-in `next` function inside the loop, but the code does not need that built-in there.

**Why comparing with the current host is safe**

The initial call starts on `startUrl`. Assume every URL entered by `dfs` has the start hostname. A recursive call occurs only after its neighbor’s hostname equals the current URL’s hostname, so the neighbor also has the start hostname. By induction, every visited URL is on the required host.

This establishes the filtering invariant even though the start hostname is not stored separately.

**Completeness of the traversal**

Take any same-host URL reachable from `startUrl` through a path of same-host links. The start is visited directly. If the crawler visits one vertex on the path, it examines all outgoing links, recognizes the next path vertex as same-host, and recursively visits it unless it was already visited. Induction along the path shows that the destination is eventually added.

Thus `ans` contains every qualifying reachable URL. The hostname invariant proves it contains no off-host URL, and set semantics prove each appears once.

**Following a cycle**

Suppose start page A links to B and B links to A and C, all on the same host. The crawler adds A, then enters B. It adds B, sees A, and calls `dfs(A)`; that call returns at once because A is in `ans`. It then reaches C normally. The cycle neither duplicates URLs nor causes infinite recursion.

**Return order and URL identity**

`return list(ans)` converts the visited set to the required list. Set iteration order is not part of the contract, and any output order is accepted.

URL strings are treated as exact identities. The statement says a trailing slash creates a different URL, so `"http://site.com"` and `"http://site.com/"` occupy different set entries and may both be crawled if linked.

**Recursion depth**

The recursion follows one DFS path at a time. A chain of \(V\) same-host pages can create \(O(V)\) call depth. With up to 1000 URLs, a standard Python recursion limit may be close to the worst case. The accepted source relies on its execution environment; an iterative stack is safer for portability.

## Complexity detail

Let \(V\) be the number of reachable same-host URLs, \(E\) the outgoing links returned from those pages, and \(L\) the maximum URL length. Each qualifying page is parsed, hashed, inserted, and queried once, and every returned edge is inspected. Treating URL operations as constant gives the manifest’s expected \(O(V+E)\) time.

More explicitly, slicing, splitting, and hashing can inspect \(O(L)\) characters. The exact bound is expected \(O((V+E)L)\), and the code recomputes `host(url)` for each outgoing edge rather than caching it.

The visited set and returned list hold \(O(V)\) URL references, and recursion can reach \(O(V)\) depth. Auxiliary space is \(O(V)\), excluding parser-owned link data and counting URL strings as existing inputs.

## Alternatives and edge cases

- **Iterative DFS stack:** Preserve the same traversal while avoiding recursion-limit risk. It uses \(O(V)\) explicit stack and visited storage.
- **Breadth-first search:** Use a queue instead of recursion. It visits the same graph and has the same asymptotic bounds; only visitation order changes.
- **Cache `start_host`:** Compute the starting hostname once and compare every neighbor against it. This avoids repeatedly parsing the current URL.
- **Standard URL parser:** Necessary for HTTPS, ports, authentication, or other general URL syntax. The seven-character slice is valid only under this problem’s restricted format.
- **Graph cycle:** Early insertion into `ans` prevents infinite recursion and repeated parser calls.
- **Duplicate outgoing links:** Even if a parser returned them, the visited guard would prevent duplicate crawling.
- **Off-host link back to the start host:** The off-host page itself is never crawled, so links reachable only through it are correctly excluded; the entire path must remain same-host.
- **Trailing slash:** It changes the URL identity, though it does not change the hostname.
- **Start page with no outgoing links:** It is added and returned as the sole result.
- **Any output order:** Converting a set yields unspecified order, which the contract explicitly permits.
