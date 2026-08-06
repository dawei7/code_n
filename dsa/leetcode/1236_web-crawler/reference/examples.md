## Examples

**Example 1**

- Input: `urls = ["http://news.yahoo.com","http://news.yahoo.com/news","http://news.yahoo.com/news/topics/","http://news.google.com","http://news.yahoo.com/us"], edges = [[2,0],[2,1],[3,2],[3,1],[0,4]], startUrl = "http://news.yahoo.com/news/topics/"`
- Output: `["http://news.yahoo.com","http://news.yahoo.com/news","http://news.yahoo.com/news/topics/","http://news.yahoo.com/us"]`

The source graph contains all five directed links. Starting at URL `2`, the crawl reaches URLs `0`, `1`, and `4` on `news.yahoo.com`; URL `3` has hostname `news.google.com` and is not reached from the starting page.

```mermaid
flowchart TD
    accTitle: Example 1 Yahoo crawl graph
    accDescr: Start URL 2 points to Yahoo URLs 0 and 1, and URL 0 points to Yahoo URL 4. Google URL 3 points toward URLs 2 and 1 but is outside the starting hostname.

    n2["2: news.yahoo.com/news/topics/<br/>startUrl"] --> n0["0: news.yahoo.com"]
    n2 --> n1["1: news.yahoo.com/news"]
    n0 --> n4["4: news.yahoo.com/us"]
    n3["3: news.google.com<br/>different hostname"] -.-> n2
    n3 -.-> n1
```

**Example 2**

- Input: `urls = ["http://news.yahoo.com","http://news.yahoo.com/news","http://news.yahoo.com/news/topics/","http://news.google.com"], edges = [[0,2],[2,1],[3,2],[3,1],[3,0]], startUrl = "http://news.google.com"`
- Output: `["http://news.google.com"]`
- Explanation: Every URL linked directly from `startUrl` has a different hostname, so none of those links is followed.

The source graph also contains the Yahoo-to-Yahoo links, but they remain unreachable because the crawl must not cross the hostname boundary from URL `3`.

```mermaid
flowchart TD
    accTitle: Example 2 Google crawl graph
    accDescr: Google start URL 3 points to three Yahoo URLs, and every one of those outgoing links is rejected because its hostname differs. Yahoo URL 0 points to URL 2, which points to URL 1.

    n3["3: news.google.com<br/>startUrl"] -. different hostname .-> n0["0: news.yahoo.com"]
    n3 -. different hostname .-> n1["1: news.yahoo.com/news"]
    n3 -. different hostname .-> n2["2: news.yahoo.com/news/topics/"]
    n0 --> n2
    n2 --> n1
```
