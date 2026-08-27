# Guided Example: Web Crawler Multithreaded

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"urls": ["http://news.yahoo.com", "http://news.yahoo.com/news", "http://news.yahoo.com/news/topics/", "http://news.google.com", "http://news.yahoo.com/us"], "edges": [[2, 0], [2, 1], [3, 2], [3, 1], [0, 4]], "start_url": "http://news.yahoo.com/news/topics/"}`
- **Required output:** `{"urls": ["http://news.yahoo.com", "http://news.yahoo.com/news", "http://news.yahoo.com/news/topics/", "http://news.yahoo.com/us"], "properties": ["same-host-only", "unique", "all-fetches-finish"]}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a URL `startUrl` and an interface `HtmlParser`, implement **a Multi-threaded web crawler** to crawl all links that are under the **same hostname** as `startUrl`.

The objective is to compute `{"urls": ["http://news.yahoo.com", "http://news.yahoo.com/news", "http://news.yahoo.com/news/topics/", "http://news.yahoo.com/us"], "properties": ["same-host-only", "unique", "all-fetches-finish"]}` from `{"urls": ["http://news.yahoo.com", "http://news.yahoo.com/news", "http://news.yahoo.com/news/topics/", "http://news.google.com", "http://news.yahoo.com/us"], "edges": [[2, 0], [2, 1], [3, 2], [3, 1], [0, 4]], "start_url": "http://news.yahoo.com/news/topics/"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Overlap the blocking parser calls

`htmlParser.getUrls(url)` simulates a network request and blocks until the page’s links arrive. A single-threaded traversal would spend most of its wall time waiting. The exact solution uses a `ThreadPoolExecutor` with eight workers so independent fetches can run concurrently.

The main thread remains responsible for graph discovery, hostname filtering, visited membership, and task submission. Worker threads execute only the blocking parser calls. This separation avoids needing a lock around `visited` or `pending`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"urls": ["http://news.yahoo.com", "http://news.yahoo.com/news", "http://news.yahoo.com/news/topics/", "http://news.google.com", "http://news.yahoo.com/us"], "edges": [[2, 0], [2, 1], [3, 2], [3, 1], [0, 4]], "start_url": "http://news.yahoo.com/news/topics/"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Parse the starting hostname

`startUrl.split("/", 3)[2]` splits an HTTP URL at most three times. For `"http://news.yahoo.com/path"`, the components begin `"http:"`, an empty string, and `"news.yahoo.com"`. Index two is the hostname.

The same expression is used for neighbors. It relies on the restricted source format: HTTP URLs without ports. A general crawler should use a standard URL parser.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `startUrl.split("/", 3)[2]` splits an HTTP URL at most three... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Track discovery before scheduling

`visited` begins with `startUrl`. The executor immediately receives one future for `htmlParser.getUrls(startUrl)`, stored in the `pending` set.

When a same-host neighbor is discovered, the main thread first adds it to `visited` and then submits its parser call. Marking before submission is essential. Several completed pages may link to the same neighbor; the first one marks it, and later occurrences fail `neighbor not in visited`, so exactly one fetch is scheduled.

Because all checks and insertions happen sequentially in the main thread, there is no check-then-add race on the set.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"urls": ["http://news.yahoo.com", "http://news.yahoo.com/news", "http://news.yahoo.com/news/topics/", "http://news.yahoo.com/us"], "properties": ["same-host-only", "unique", "all-fetches-finish"]}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"urls": ["http://news.yahoo.com", "http://news.yahoo.com/news", "http://news.yahoo.com/news/topics/", "http://news.google.com", "http://news.yahoo.com/us"], "edges": [[2, 0], [2, 1], [3, 2], [3, 1], [0, 4]], "start_url": "http://news.yahoo.com/news/topics/"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"urls": ["http://news.yahoo.com", "http://news.yahoo.com/news", "http://news.yahoo.com/news/topics/", "http://news.yahoo.com/us"], "properties": ["same-host-only", "unique", "all-fetches-finish"]}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Single-threaded DFS or BFS:** It has the same :** - **Single-threaded DFS or BFS:** It has the same graph-work complexity but serializes blocking requests and can exceed the time limit.
- **Shared worker queue:** Long-lived worker threads can pop URLs and coordinate an unfinished-work counter. This offers more control but requires careful locking and termination detection.
- **Async I/O:** An asynchronous parser interface could overlap requests without threads, but the supplied interface is synchronous and blocking.
- **Duplicate links from different pages:** The main-thread visited check schedules the target exactly once.
- **Graph cycles:** A previously visited URL is never resubmitted, so cycles terminate.
- **Off-host links:** They are neither marked nor fetched, even if they later link back to the starting host.
- **Long chain:** Dependency discovery limits concurrency; thread count cannot parallelize unknown future URLs.
- **Wide frontier:** Up to eight independent parser calls can overlap.
- **Parser exception:** `future.result()` propagates it; retry or partial-result logic is outside the exact source.
- **Any result order:** Set conversion is unordered, which the contract permits.
- **Restricted hostname parsing:** The split expression assumes the stated HTTP-without-port format.
- **Distributed follow-up:** At billion-URL scale, consistent hashing can assign hosts or URLs to nodes, durable distributed queues can balance work, deduplication must be partitioned, failed leases must be retried, and global termination requires tracking both queued and in-flight work. Those systems concerns are beyond this single-process source.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V+E)$. Let \(V\) be the reachable same-host URL count and \(E\) the outgoing links returned from those pages. Each qualifying URL is submitted once, and each outgoing link is inspected once. With expected constant-time set operations and treating URL parsing as constant, total work is expected \(O(V+E)\).
- **Auxiliary Space Complexity:** $O(V)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
