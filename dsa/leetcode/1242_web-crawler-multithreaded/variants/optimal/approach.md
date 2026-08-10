## General

**Overlap the blocking parser calls**

`htmlParser.getUrls(url)` simulates a network request and blocks until the page’s links arrive. A single-threaded traversal would spend most of its wall time waiting. The exact solution uses a `ThreadPoolExecutor` with eight workers so independent fetches can run concurrently.

The main thread remains responsible for graph discovery, hostname filtering, visited membership, and task submission. Worker threads execute only the blocking parser calls. This separation avoids needing a lock around `visited` or `pending`.

**Parse the starting hostname**

`startUrl.split("/", 3)[2]` splits an HTTP URL at most three times. For `"http://news.yahoo.com/path"`, the components begin `"http:"`, an empty string, and `"news.yahoo.com"`. Index two is the hostname.

The same expression is used for neighbors. It relies on the restricted source format: HTTP URLs without ports. A general crawler should use a standard URL parser.

**Track discovery before scheduling**

`visited` begins with `startUrl`. The executor immediately receives one future for `htmlParser.getUrls(startUrl)`, stored in the `pending` set.

When a same-host neighbor is discovered, the main thread first adds it to `visited` and then submits its parser call. Marking before submission is essential. Several completed pages may link to the same neighbor; the first one marks it, and later occurrences fail `neighbor not in visited`, so exactly one fetch is scheduled.

Because all checks and insertions happen sequentially in the main thread, there is no check-then-add race on the set.

**Wait for whichever request finishes first**

While any futures remain, the code calls:

`wait(pending, return_when=FIRST_COMPLETED)`.

This blocks only until at least one request completes. It returns a set of completed futures and a set of still-pending futures. The assignment `completed, pending = ...` replaces `pending` with the not-yet-finished tasks.

There may be several completed futures by the time the main thread resumes. The loop processes all of them. For each returned neighbor:

- extract its hostname;
- reject it if the hostname differs;
- reject it if it was already visited;
- otherwise mark it and submit a new blocking fetch, adding that future to `pending`.

The pending set can therefore grow dynamically while completed tasks are processed.

**Why the loop detects completion correctly**

Every newly discovered qualifying URL receives one future, and every future remains in `pending` until `wait` reports it completed. Processing a completed future may add more futures. The loop ends only when there are no unfinished or newly submitted fetches.

At that point, every discovered page has had its outgoing links processed, and no processed link revealed an undiscovered same-host page. The reachable search frontier is empty, so the crawl is complete.

The executor context manager waits for worker cleanup before returning.


Safety follows from the hostname check: only `startUrl` and neighbors whose parsed hostname equals the saved hostname enter `visited`. Uniqueness follows from set membership and marking before scheduling.

For completeness, take any same-host URL reachable through a same-host path from `startUrl`. The start is scheduled. When each predecessor’s future completes, its outgoing list is inspected and the next path URL is scheduled unless already visited. Induction along the path proves the destination is eventually visited and fetched.

Thus converting `visited` to a list returns exactly the required reachable same-host URLs, in an arbitrary allowed order.

**What multithreading improves**

Graph-processing work is not asymptotically reduced. The benefit is wall-clock overlap: while one worker waits on a parser call, other workers can wait on or finish other calls. At most eight fetches execute at once.

The speedup depends on graph shape. A broad frontier offers parallel work. A single long chain reveals only one next page after each fetch and remains mostly sequential because later requests are not known yet.

**Failure behavior**

Calling `future.result()` returns the parser output or re-raises an exception from the worker. The exact source does not catch such exceptions, so a parser failure aborts the crawl. The problem interface guarantees normal bounded completion.

## Complexity detail

Let \(V\) be the reachable same-host URL count and \(E\) the outgoing links returned from those pages. Each qualifying URL is submitted once, and each outgoing link is inspected once. With expected constant-time set operations and treating URL parsing as constant, total work is expected \(O(V+E)\).

If maximum URL length \(L\) is included, splitting and hashing produce a more explicit expected bound of \(O((V+E)L)\). Eight workers change latency and constants, not total work.

`visited`, futures, and the executor queue can hold \(O(V)\) entries, giving \(O(V)\) algorithm-managed space. Completed adjacency lists are parser results and can add transient storage proportional to returned edges. The fixed eight worker threads are \(O(1)\) with respect to \(V\).

## Alternatives and edge cases

- **Single-threaded DFS or BFS:** It has the same graph-work complexity but serializes blocking requests and can exceed the time limit.
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
