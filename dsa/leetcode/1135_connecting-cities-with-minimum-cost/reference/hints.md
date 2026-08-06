## Hints

1. Model the cities and their bidirectional connections as a weighted graph.
2. Connecting every city at minimum total cost is a minimum spanning tree problem.
3. A variation of Kruskal's algorithm can construct that tree.
4. Sort connections by cost and use a union-find data structure to merge components without creating cycles.
5. Determine explicitly how the process can verify that every city became connected.
6. Initially there are `n` connected components. Every successful connection of two different components reduces that count by one, so a valid result must finish with exactly one component; otherwise, return `-1`.
