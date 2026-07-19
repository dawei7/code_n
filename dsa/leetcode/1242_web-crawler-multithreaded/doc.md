# Web Crawler Multithreaded

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1242 |
| Difficulty | Medium |
| Category | Concurrency |
| Topics | Depth-First Search, Breadth-First Search, Concurrency |
| Supported Languages | Python |
| Official Link | [LeetCode](https://leetcode.com/problems/web-crawler-multithreaded/) |

## Problem Description

### Goal

Implement a multithreaded web crawler starting from `startUrl`. The supplied thread-safe `HtmlParser.getUrls(url)` operation returns the URLs linked from a page, but each call is a blocking operation with nontrivial latency. Use concurrency so independent pages can be fetched in parallel.

Return every URL reachable from `startUrl` whose hostname exactly matches the starting hostname, in any order and without duplicates. Do not crawl an off-host URL even if it links back to the original host. Links may contain cycles and duplicates, so scheduling and visited-state coordination must remain correct under arbitrary task completion order.

### Function Contract

**Inputs**

- `startUrl`: The page at which crawling begins.
- `htmlParser`: A thread-safe object whose `getUrls(url)` method blocks briefly and returns that page's outgoing links.

Let $V$ be the number of reachable same-host URLs and $E$ the number of outgoing links inspected from those pages.

**Return value**

- Every reachable URL on the starting hostname, exactly once and in any order.

### Examples

**Example 1**

Starting at `"http://news.yahoo.com/news/topics/"` in the sample graph returns the four reachable Yahoo URLs while excluding `"http://news.google.com"`.

**Example 2**

Starting at `"http://news.google.com"` returns only that URL when all of its outgoing links lead to the Yahoo hostname.

**Example 3**

In a same-host cycle, every page is returned once; revisiting an already scheduled page must not create another parser task.
