## Hints

1. Treat courses as vertices and prerequisite relationships as directed edges. Completing every course is impossible when this graph contains a cycle.
2. When the graph is a directed acyclic graph (DAG), the answer is the number of vertices on its longest directed path.
3. Dynamic programming on the DAG can compute that longest path.
