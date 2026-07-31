# Web Crawler

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1236 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Depth-First Search, Breadth-First Search, Interactive |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/web-crawler/) |

## Problem Description

### Goal

A collection of web pages is represented by URLs and directed links. Starting from `startUrl`, crawl every page that is reachable by following links, but include a page only when its hostname is exactly the same as the hostname of `startUrl`. A hostname is the portion between the `http://` prefix and the next `"/"`, if any.

Each reachable same-host page must appear exactly once in the result, including `startUrl`, and the URLs may be returned in any order. Links may form cycles, may point back to pages already visited, and may lead to another hostname; do not crawl beyond an off-host URL. The read-only `HtmlParser.getUrls(url)` interface supplies the outgoing links for a page.

### Function Contract

**Inputs**

- `startUrl`: The URL from which the crawl begins.
- `htmlParser`: A read-only `HtmlParser` object whose `getUrls(url)` method returns the URLs linked from `url`.

Authored JSON cases construct `htmlParser` from a fixture containing unique `urls` and directed index pairs `edges`; these are fixture fields, not additional function parameters.

Let $V$ be the number of reachable same-host URLs and $E$ the number of outgoing links inspected from those URLs.

**Return value**

- Every URL reachable from `startUrl` without leaving its hostname, in any order and without duplicates.

### Examples

**Example 1**

- Input: `startUrl = "http://news.yahoo.com/news/topics/"`, `htmlParser = {"urls":["http://news.yahoo.com","http://news.yahoo.com/news","http://news.yahoo.com/news/topics/","http://news.google.com","http://news.yahoo.com/us"],"edges":[[2,0],[2,1],[3,2],[3,1],[0,4]]}`
- Output: `["http://news.yahoo.com/news/topics/","http://news.yahoo.com","http://news.yahoo.com/news","http://news.yahoo.com/us"]`

The three Yahoo pages reached through links stay within the starting hostname.

**Example 2**

- Input: `startUrl = "http://news.google.com"`, `htmlParser = {"urls":["http://news.yahoo.com","http://news.yahoo.com/news","http://news.yahoo.com/news/topics/","http://news.google.com"],"edges":[[0,2],[2,1],[3,2],[3,1],[3,0]]}`
- Output: `["http://news.google.com"]`

Every outgoing link changes the hostname, so none is followed.

**Example 3**

- Input: `startUrl = "http://a.com"`, `htmlParser = {"urls":["http://a.com","http://a.com/x","http://a.com/y"],"edges":[[0,1],[1,2],[2,0]]}`
- Output: `["http://a.com","http://a.com/x","http://a.com/y"]`

The visited set terminates the cycle while retaining each page once.
