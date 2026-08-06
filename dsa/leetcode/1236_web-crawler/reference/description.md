## Description

Given a URL `startUrl` and an `HtmlParser` interface, crawl every link reachable from `startUrl` that belongs to exactly the same hostname. Return all URLs discovered by the crawl in any order.

The crawler must:

- begin at `startUrl`;
- call `htmlParser.getUrls(url)` to obtain the URLs linked from a page;
- avoid crawling the same URL more than once; and
- explore only URLs whose hostname equals the hostname of `startUrl`.

The hostname is the domain portion of a URL. The source illustrates the distinction with this decomposition:

| Component | Value |
|---|---|
| Complete URL | `http://example.org:8888/foo/bar#bang` |
| Hostname | `example.org` |
| Host | `example.org:8888` |

For this problem, every URL uses the `http` protocol and contains no explicit port. Thus `http://leetcode.com/problems` and `http://leetcode.com/contest` share a hostname, whereas `http://example.org/test` and `http://example.com/abc` do not.

The parser exposes one read-only operation, `getUrls(url)`, which returns every URL linked from the given page. In custom-test fixtures, `urls` contains the URL library and each pair `[from, to]` in `edges` represents a directed link between two indexed URLs. Your submitted code receives `startUrl` and the parser interface; it does not directly access `urls` or `edges`.
