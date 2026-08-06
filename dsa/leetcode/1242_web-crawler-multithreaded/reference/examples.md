## Examples

**Example 1**

- Input: `urls = ["http://news.yahoo.com","http://news.yahoo.com/news","http://news.yahoo.com/news/topics/","http://news.google.com","http://news.yahoo.com/us"], edges = [[2,0],[2,1],[3,2],[3,1],[0,4]], startUrl = "http://news.yahoo.com/news/topics/"`
- Output: `["http://news.yahoo.com","http://news.yahoo.com/news","http://news.yahoo.com/news/topics/","http://news.yahoo.com/us"]`

Starting from URL `2`, the crawler reaches Yahoo URLs `0`, `1`, and `4`. Google URL `3` has a different hostname and is excluded.

```mermaid
flowchart TD
    accTitle: Example 1 concurrent Yahoo crawl
    accDescr: Yahoo start URL 2 links to Yahoo URLs 0 and 1, URL 0 links to Yahoo URL 4, and Google URL 3 is outside the permitted hostname despite its links toward URLs 2 and 1.

    n2["2: news.yahoo.com/news/topics/<br/>startUrl"] --> n0["0: news.yahoo.com"]
    n2 --> n1["1: news.yahoo.com/news"]
    n0 --> n4["4: news.yahoo.com/us"]
    n3["3: news.google.com<br/>different hostname"] -.-> n2
    n3 -.-> n1
```

**Example 2**

- Input: `urls = ["http://news.yahoo.com","http://news.yahoo.com/news","http://news.yahoo.com/news/topics/","http://news.google.com"], edges = [[0,2],[2,1],[3,2],[3,1],[3,0]], startUrl = "http://news.google.com"`
- Output: `["http://news.google.com"]`
- Explanation: Every outgoing link from `startUrl` has a different hostname, so none of those pages may be crawled.

The Yahoo-to-Yahoo links exist in the source graph but remain unreachable because crossing the hostname boundary is forbidden.

```mermaid
flowchart TD
    accTitle: Example 2 cross-host links are rejected
    accDescr: Google start URL 3 links to three Yahoo URLs, but each link is rejected because its hostname differs. The remaining Yahoo-to-Yahoo links are therefore unreachable.

    n3["3: news.google.com<br/>startUrl"] -. different hostname .-> n0["0: news.yahoo.com"]
    n3 -. different hostname .-> n1["1: news.yahoo.com/news"]
    n3 -. different hostname .-> n2["2: news.yahoo.com/news/topics/"]
    n0 --> n2
    n2 --> n1
```
