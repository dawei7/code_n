## Description

Given a URL `startUrl` and an `HtmlParser` interface, implement a multithreaded crawler that discovers every reachable URL with exactly the same hostname as `startUrl`. Return the discovered URLs in any order.

The crawler must:

- begin at `startUrl`;
- call `htmlParser.getUrls(url)` to obtain the links from a page;
- never crawl the same URL twice; and
- follow only URLs whose hostname equals the hostname of `startUrl`.

The hostname is the domain portion of a URL. The source illustrates the distinction with this decomposition:

| Component | Value |
|---|---|
| Complete URL | `http://example.org:8888/foo/bar#bang` |
| Hostname | `example.org` |
| Host | `example.org:8888` |

For this problem, every URL uses the `http` protocol and contains no explicit port. Consequently, `http://leetcode.com/problems` and `http://leetcode.com/contest` have the same hostname, while `http://example.org/test` and `http://example.com/abc` do not.
