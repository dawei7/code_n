## General
Given a url `startUrl` and an interface `HtmlParser`, implement a web crawler to crawl all links that are under the **same hostname** as `startUrl`, the algorithm executes depth-first search (DFS) recursion to explore valid decision branches. It utilizes a hash set (`set`) to track unique elements and prevent duplicate processing in $O(1)$ time.

## Complexity detail
- **Time Complexity**: $O(V+E)$ — Operation count bound.
- **Space Complexity**: $O(V)$ — Auxiliary memory allocation bound.
