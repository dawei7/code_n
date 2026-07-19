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

A collection of web pages is represented by URLs and directed links. Starting from `start_url`, crawl every page that is reachable by following links, but include a page only when its hostname is exactly the same as the hostname of `start_url`. A hostname is the portion between the `http://` prefix and the next `"/"`, if any.

Each reachable same-host page must appear exactly once in the result, including `start_url`, and the URLs may be returned in any order. Links may form cycles, may point back to pages already visited, and may lead to another hostname; do not crawl beyond an off-host URL. In cOde(n), `urls` and index pairs in `edges` provide the deterministic graph used by LeetCode's `HtmlParser.getUrls` interface.

### Function Contract

**Inputs**

- `urls`: A list of unique page URLs; index $i$ identifies page `urls[i]`.
- `edges`: Directed pairs `[from_index, to_index]` indicating that the first page links to the second.
- `start_url`: A URL contained in `urls` from which the crawl begins.

Let $V$ be the number of reachable same-host URLs and $E$ the number of outgoing links inspected from those URLs.

**Return value**

- Every URL reachable from `start_url` without leaving its hostname, in any order and without duplicates.

### Examples

**Example 1**

- Input: `urls = ["http://news.yahoo.com","http://news.yahoo.com/news","http://news.yahoo.com/news/topics/","http://news.google.com","http://news.yahoo.com/us"]`, `edges = [[2,0],[2,1],[3,2],[3,1],[0,4]]`, `start_url = "http://news.yahoo.com/news/topics/"`
- Output: `["http://news.yahoo.com/news/topics/","http://news.yahoo.com","http://news.yahoo.com/news","http://news.yahoo.com/us"]`

The three Yahoo pages reached through links stay within the starting hostname.

**Example 2**

- Input: `urls = ["http://news.yahoo.com","http://news.yahoo.com/news","http://news.yahoo.com/news/topics/","http://news.google.com"]`, `edges = [[0,2],[2,1],[3,2],[3,1],[3,0]]`, `start_url = "http://news.google.com"`
- Output: `["http://news.google.com"]`

Every outgoing link changes the hostname, so none is followed.

**Example 3**

- Input: `urls = ["http://a.com","http://a.com/x","http://a.com/y"]`, `edges = [[0,1],[1,2],[2,0]]`, `start_url = "http://a.com"`
- Output: `["http://a.com","http://a.com/x","http://a.com/y"]`

The visited set terminates the cycle while retaining each page once.
