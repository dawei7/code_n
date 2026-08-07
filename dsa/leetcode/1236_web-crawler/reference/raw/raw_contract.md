## Function Contract

**Inputs**

- `startUrl`: The URL where the crawl begins. It is one of the URLs known to the parser.
- `htmlParser`: A read-only interface whose `getUrls(url)` method returns the outgoing links from `url`.

Authored JSON cases construct `htmlParser` from a fixture containing `urls` and directed index pairs `edges`. Those fixture fields model the injected parser and are not additional function parameters.

Let $V$ be the number of same-host URLs reachable from `startUrl`, and let $E$ be the number of outgoing links returned while processing those $V$ pages. URL strings have source-bounded length at most 300.

**Return value**

Return every URL reachable from `startUrl` through a path containing only URLs with the starting hostname. Include `startUrl`, include each qualifying URL exactly once, exclude every off-host URL, and return the result in any order.
