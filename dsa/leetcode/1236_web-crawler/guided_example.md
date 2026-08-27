# Guided Example: Web Crawler

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"startUrl": "http://news.yahoo.com/news/topics/", "htmlParser": {"urls": ["http://news.yahoo.com", "http://news.yahoo.com/news", "http://news.yahoo.com/news/topics/", "http://news.google.com", "http://news.yahoo.com/us"], "edges": [[2, 0], [2, 1], [3, 2], [3, 1], [0, 4]]}}`
- **Required output:** `["http://news.yahoo.com", "http://news.yahoo.com/news", "http://news.yahoo.com/news/topics/", "http://news.yahoo.com/us"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a url `startUrl` and an interface `HtmlParser`, implement a web crawler to crawl all links that are under the **same hostname** as `startUrl`.

The objective is to compute `["http://news.yahoo.com", "http://news.yahoo.com/news", "http://news.yahoo.com/news/topics/", "http://news.yahoo.com/us"]` from `{"startUrl": "http://news.yahoo.com/news/topics/", "htmlParser": {"urls": ["http://news.yahoo.com", "http://news.yahoo.com/news", "http://news.yahoo.com/news/topics/", "http://news.google.com", "http://news.yahoo.com/us"], "edges": [[2, 0], [2, 1], [3, 2], [3, 1], [0, 4]]}}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Model pages and links as a directed graph

Treat every URL as a graph vertex. A call to `htmlParser.getUrls(url)` reveals the outgoing edges from that vertex. Starting from `startUrl`, the task is to traverse all reachable vertices while refusing edges whose destination has a different hostname.

The exact solution uses recursive depth-first search. The set `ans` serves two purposes: it records the answer and marks pages already visited.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"startUrl": "http://news.yahoo.com/news/topics/", "htmlParser": {"urls": ["http://news.yahoo.com", "http://news.yahoo.com/news", "http://news.yahoo.com/news/topics/", "http://news.google.com", "http://news.yahoo.com/us"], "edges": [[2, 0], [2, 1], [3, 2], [3, 1], [0, 4]]}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Extract a hostname under the stated URL format

Every URL uses the literal `http://` prefix and has no port. The helper `host(url)` removes the first seven characters with `url[7:]`, leaving the hostname and optional path. Splitting that remainder on `'/'` and taking element zero returns the hostname.

For `"http://news.yahoo.com/news"`, removing seven characters gives `"news.yahoo.com/news"`, and the first split component is `"news.yahoo.com"`. For a URL with no path, the entire remainder is the hostname.

This parser is intentionally tied to the contract. It is not a general URL parser: `https://` has a different prefix length, ports would be included in the host text, and other URL features would need a standard parsing library.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Every URL uses the literal `http://` prefix and has no port.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Mark a page before following its links

`dfs(url)` first checks `if url in ans`. If the page was already seen, it returns immediately. Otherwise, it adds the URL to `ans` before asking the parser for outgoing links.

Marking before recursion is essential. The graph can contain cycles such as A linking to B and B linking back to A. If A were marked only after finishing B, the back edge would recursively enter A again forever. Early marking makes every subsequent visit to A stop.

It also guarantees that `htmlParser.getUrls(url)` is called at most once for each crawled URL.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["http://news.yahoo.com", "http://news.yahoo.com/news", "http://news.yahoo.com/news/topics/", "http://news.yahoo.com/us"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"startUrl": "http://news.yahoo.com/news/topics/", "htmlParser": {"urls": ["http://news.yahoo.com", "http://news.yahoo.com/news", "http://news.yahoo.com/news/topics/", "http://news.google.com", "http://news.yahoo.com/us"], "edges": [[2, 0], [2, 1], [3, 2], [3, 1], [0, 4]]}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["http://news.yahoo.com", "http://news.yahoo.com/news", "http://news.yahoo.com/news/topics/", "http://news.yahoo.com/us"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Iterative DFS stack:** Preserve the same trave:** - **Iterative DFS stack:** Preserve the same traversal while avoiding recursion-limit risk. It uses \(O(V)\) explicit stack and visited storage.
- **Breadth-first search:** Use a queue instead of recursion. It visits the same graph and has the same asymptotic bounds; only visitation order changes.
- **Cache `start_host`:** Compute the starting hostname once and compare every neighbor against it. This avoids repeatedly parsing the current URL.
- **Standard URL parser:** Necessary for HTTPS, ports, authentication, or other general URL syntax. The seven-character slice is valid only under this problem’s restricted format.
- **Graph cycle:** Early insertion into `ans` prevents infinite recursion and repeated parser calls.
- **Duplicate outgoing links:** Even if a parser returned them, the visited guard would prevent duplicate crawling.
- **Off-host link back to the start host:** The off-host page itself is never crawled, so links reachable only through it are correctly excluded; the entire path must remain same-host.
- **Trailing slash:** It changes the URL identity, though it does not change the hostname.
- **Start page with no outgoing links:** It is added and returned as the sole result.
- **Any output order:** Converting a set yields unspecified order, which the contract explicitly permits.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V+E)$. Let \(V\) be the number of reachable same-host URLs, \(E\) the outgoing links returned from those pages, and \(L\) the maximum URL length. Each qualifying page is parsed, hashed, inserted, and queried once, and every returned edge is inspected. Treating URL operations as constant gives the manifest’s expected \(O(V+E)\) time.
- **Auxiliary Space Complexity:** $O(V)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
