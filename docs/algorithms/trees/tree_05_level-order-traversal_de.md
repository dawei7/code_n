# Level-Order Traversal

| | |
|---|---|
| **ID** | `tree_05` |
| **Kategorie** | trees |
| **Komplexität (erforderlich)** | $O(n)$ |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) |

## Problemstellung

Gegeben ist der `root` eines Binary Tree. Geben Sie die **Level-Order Traversal** der Werte seiner Knoten zurück (d. h. von links nach rechts, Ebene für Ebene).

**Input:** Der Wurzelknoten eines Binary Tree.
**Output:** Ein 2D-Array, wobei jedes innere Array eine einzelne Ebene des Baums repräsentiert.

**Beispiel:**
Gegeben sei der Baum:
```
      3
     / \
    9  20
      /  \
     15   7
```
**Output:** `[[3], [9, 20], [15, 7]]`

## Wann man es verwendet

- Um den kürzesten Pfad von der Wurzel zu einem bestimmten Knoten zu finden (in einem ungewichteten Baum).
- Um einen Baum visuell in einer Terminal-Konsole auszugeben.
- Um einen Baum in eine flache Array-Struktur zu serialisieren/deserialisieren (wie die Standard-Baumdarstellung von LeetCode `[3, 9, 20, null, null, 15, 7]`).

## Ansatz

Die Level-Order Traversal entspricht im Grunde exakt der **Breadth-First Search (BFS)**.

Im Gegensatz zur DFS (die mithilfe eines Stack tief in den Baum eintaucht), expandiert die BFS gleichmäßig in Wellen unter Verwendung einer **Queue** (First-In, First-Out).
1. Fügen Sie den Wurzelknoten zur Queue hinzu (enqueue).
2. Solange die Queue nicht leer ist:
   - Bestimmen Sie, wie viele Knoten sich aktuell in der Queue befinden. Diese Zahl `M` repräsentiert die exakte Größe der aktuellen "Ebene".
   - Iterieren Sie exakt `M` Mal. In jedem Schleifendurchlauf entfernen Sie einen Knoten aus der Queue (dequeue), verarbeiten dessen Wert und fügen dessen linke und rechte Kinder zur Queue hinzu.
   - Alle Kinder, die Sie gerade hinzugefügt haben, warten geduldig am Ende der Queue darauf, in der *nächsten* Ebene verarbeitet zu werden.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for tree_05: Level-Order Traversal.

BFS, return a list of lists — one row per depth.
"""


def solve(children, root, n):
    from collections import deque
    levels = []
    q = deque()
    q.append((root, 0))
    while q:
        u, d = q.popleft()
        while len(levels) <= d:
            levels.append([])
        levels[d].append(u)
        for v in children[u]:
            q.append((v, d + 1))
    return levels
```

</details>

## Durchlauf

Sei der Baum:
```
      A
     / \
    B   C
   /     \
  D       E
```

1. Init: `queue = [A]`. `result = []`.
2. Schleife 1: `level_size = 1`.
   - Dequeue `A`. `current_level = [A]`.
   - Enqueue `B`, `C`. `queue = [B, C]`.
   - Ende der inneren Schleife. `result = [[A]]`.
3. Schleife 2: `level_size = 2`.
   - Dequeue `B`. `current_level = [B]`. Enqueue `D`. `queue = [C, D]`.
   - Dequeue `C`. `current_level = [B, C]`. Enqueue `E`. `queue = [D, E]`.
   - Ende der inneren Schleife. `result = [[A], [B, C]]`.
4. Schleife 3: `level_size = 2`.
   - Dequeue `D`. `current_level = [D]`. Keine Kinder.
   - Dequeue `E`. `current_level = [D, E]`. Keine Kinder.
   - Ende der inneren Schleife. `result = [[A], [B, C], [D, E]]`.
5. Schleife terminiert (`queue` ist leer). ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(n)$ | $O(n)$ |
| **Schlechtester Fall** | $O(n)$ | $O(n)$ |

Wir besuchen jeden Knoten exakt einmal, was strikt $O(n)$ Zeit in Anspruch nimmt.
Die Platzkomplexität wird durch die maximale Größe der Queue definiert. In einem perfekt balancierten Binary Tree ist die absolut breiteste Ebene die unterste Reihe der Blätter. In einem Binary Tree enthält die letzte Reihe ungefähr $N/2$ Knoten. Daher wird die Queue gleichzeitig maximal $N/2$ Knoten halten, was die Platzkomplexität im schlechtesten Fall zu $O(n)$ macht. Der Bestfall von $O(1)$ Platz tritt auf, wenn der Baum eine entartete Linked List ist (Breite von 1).

## Varianten & Optimierungen

- **Zig-Zag Level Order Traversal:** Jedes Mal, wenn Sie eine Ebene beendet haben, prüfen Sie ein boolesches Flag. Wenn `True`, hängen Sie `current_level` normal an das Ergebnis an. Wenn `False`, hängen Sie das `reverse()` von `current_level` an. Schalten Sie das Flag um. Dies ist eine sehr häufige Abwandlung in Vorstellungsgesprächen.

## Anwendungen in der Praxis

- **Netzwerk-Routing:** OSPF (Open Shortest Path First) Protokolle verwenden BFS, um die Netzwerktopologie abzubilden und sicherzustellen, dass Datenpakete die kürzestmögliche Anzahl an Router-Hops bis zu ihrem Ziel nehmen.

## Verwandte Algorithmen in cOde(n)

- **[search_03 - BFS on Grid](../searching/search_03_bfs-grid.md)** — Die exakt gleiche algorithmische Logik angewendet auf eine 2D-Matrix anstelle einer zeigerbasierten Baumstruktur.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*