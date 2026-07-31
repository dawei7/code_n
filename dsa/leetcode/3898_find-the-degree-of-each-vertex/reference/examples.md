## Examples

**Example 1**

```mermaid
graph LR
  accTitle: Example 1 triangle graph
  accDescr: Vertices 0, 1, and 2 are each connected to both other vertices, so every vertex has degree 2.
  v0((0)) --- v1((1))
  v0 --- v2((2))
  v1 --- v2
```

- Input: `matrix = [[0,1,1],[1,0,1],[1,1,0]]`
- Output: `[2,2,2]`
- Explanation:
  - Vertex $0$ is adjacent to vertices $1$ and $2$, giving degree $2$.
  - Vertex $1$ is adjacent to vertices $0$ and $2$, giving degree $2$.
  - Vertex $2$ is adjacent to vertices $0$ and $1$, giving degree $2$.

  Therefore the degree array is `[2,2,2]`.

**Example 2**

```mermaid
graph LR
  accTitle: Example 2 graph with an isolated vertex
  accDescr: Vertices 0 and 1 are connected by one edge, while vertex 2 has no incident edge.
  v0((0)) --- v1((1))
  v2((2))
```

- Input: `matrix = [[0,1,0],[1,0,0],[0,0,0]]`
- Output: `[1,1,0]`
- Explanation:
  - Vertex $0$ has the single neighbor $1$, so its degree is $1$.
  - Vertex $1$ has the single neighbor $0$, so its degree is $1$.
  - Vertex $2$ is isolated and has degree $0$.

  Therefore the degree array is `[1,1,0]`.

**Example 3**

- Input: `matrix = [[0]]`
- Output: `[0]`
- Explanation: The graph contains one vertex and no edges, so that vertex has degree $0$.
