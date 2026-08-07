## Function Contract

**Inputs**

- `startUrl`: The URL where the crawl begins. It is present in the parser's URL library.
- `htmlParser`: An injected interface whose blocking `getUrls(url)` operation returns the URLs linked from `url`.

Conceptually, the supplied interface has this operation:

```text
getUrls(url) -> list of URLs linked from url
```

Each call simulates an HTTP request, blocks until that request finishes, and is guaranteed to return within 15 ms. A single-threaded crawler exceeds the time limit, so independent parser calls must overlap.

For authored custom tests, `urls` is the URL library and each pair `[from, to]` in `edges` is a directed link between indexed URLs. Submitted code receives only `startUrl` and `htmlParser`; it cannot access `urls` or `edges` directly.

Let $V$ be the number of same-host URLs reachable from `startUrl`, and let $E$ be the number of outgoing links returned while processing those $V$ pages. URL strings have source-bounded length at most 300.

**Return value**

Return every URL reachable from `startUrl` through a path consisting only of URLs with the starting hostname. Include `startUrl`, include every qualifying URL exactly once, exclude all off-host URLs, and return the result in any order.
