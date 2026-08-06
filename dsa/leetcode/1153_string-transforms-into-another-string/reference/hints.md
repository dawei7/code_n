## Hints

1. Model characters as graph vertices, adding an edge when one character must be converted into another.
2. Consider what happens if one source character would have to become more than one target character.
3. Such a requirement is impossible, so every graph vertex may have at most one outgoing edge.
4. Determine how a linked-list-shaped component can be processed.
5. Determine how a directed cycle can be processed.
6. A character with no outgoing edge can serve as temporary storage to open every cycle.
