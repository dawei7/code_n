## General
**Separate fetching from traversal coordination.** Extract the starting hostname once. Maintain a set of visited URLs and a set of pending futures. Submit the first `getUrls` call to a bounded thread pool, then wait until at least one pending fetch finishes rather than waiting for all current work as a batch.

**Schedule newly discovered pages exactly once.** The coordinating thread processes every completed future. For each returned neighbor, compare its full hostname, then add it to `visited` before submitting another fetch. Because only the coordinator mutates `visited` and `pending`, no additional lock is needed for those structures, while the parser calls themselves overlap in worker threads.

**Continue until no work remains.** A future is removed when its links are consumed, and every accepted new URL creates one replacement future. When the pending set becomes empty, every scheduled page has completed and no undiscovered same-host edge remains. Every returned URL is reachable by construction, and induction along reachability paths shows that every valid page is eventually scheduled.

## Complexity detail
Each of the $V$ accepted pages is scheduled once and each of the $E$ outgoing links is inspected once, so total computational work is $O(V+E)$. Blocking parser latency overlaps across a bounded number of workers. The visited set, pending futures, and returned URLs require $O(V)$ space.

## Alternatives and edge cases
- **Single-threaded traversal:** It is functionally correct but serializes every blocking parser call and does not satisfy the concurrency objective.
- **One unmanaged thread per URL:** It exposes parallelism but can create an unbounded number of threads and exhaust resources.
- **Batch barriers:** Waiting for an entire level before submitting newly available work leaves workers idle behind one slow fetch.
- **Duplicate links:** Mark a URL before task submission so repeated discoveries create one parser call.
- **Cycle:** The visited set prevents completed or pending pages from being scheduled again.
- **Off-host bridge:** Never fetch an off-host page, even if it could link back to the starting host.
- **Worker exception:** Retrieving each future's result surfaces parser failures rather than silently losing part of the crawl.
- **No outgoing links:** The pending set drains after the starting fetch and the result contains only `startUrl`.
