## General
**Fix the allowed hostname once.** Extract the hostname from `start_url` before traversal. Comparing the entire URL prefix is insufficient because hostnames such as `news.example.com` and `news.example.com.evil` can share characters without being equal.

**Traverse only accepted pages.** Put `start_url` in both a stack and a hash set. Repeatedly remove one URL, request or look up its outgoing links, and inspect each neighbor. If its hostname differs, ignore it. If it has the same hostname and is not in the visited set, mark it immediately and add it to the stack. Marking on insertion prevents cycles and duplicate links from scheduling the same page more than once.

Every scheduled URL is reachable through a chain of same-host links, so the traversal never adds an invalid page. Conversely, whenever a reachable same-host page has a predecessor that is processed, its link is inspected and the page is scheduled unless already visited. Induction along a reachability path therefore shows that the final visited set contains every and only required URL.

## Complexity detail
Each of the $V$ visited URLs is processed once, and all $E$ outgoing links from those pages are inspected once, giving $O(V+E)$ time. The visited set and traversal stack hold at most $V$ URLs, so auxiliary space is $O(V)$.

## Alternatives and edge cases
- **Breadth-first search:** A queue provides the same $O(V+E)$ guarantees; traversal order is irrelevant because any result order is accepted.
- **List-based visited tracking:** It remains correct but makes membership checks linear and can degrade a long crawl to $O(V^2+E)$ time.
- **Recursive depth-first search:** The logic is compact, but a long link chain can exceed the language's recursion depth.
- **Cycle:** Mark a URL before scheduling it so a back edge cannot create repeated work.
- **Duplicate links:** The visited set ensures repeated references yield one result entry.
- **Off-host bridge:** Do not enqueue an off-host page, even if that page could link back to the original hostname.
- **Hostname lookalike:** Compare the parsed hostname, not an arbitrary textual prefix.
- **No outgoing links:** Return a list containing only `start_url`.
