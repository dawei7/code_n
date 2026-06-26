# Binary Tree Right Side View

| | |
|---|---|
| **ID** | `tree_18` |
| **Kategorie** | trees |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(D)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) |

## Problemstellung

Gegeben ist der `root` eines Binary Tree. Stellen Sie sich vor, Sie stehen auf der **rechten Seite** des Baums. Geben Sie die Werte der Knoten zurück, die Sie von oben nach unten sehen können.
Mit anderen Worten: Geben Sie den am weitesten rechts liegenden Knoten auf jeder Ebene des Baums zurück.

**Eingabe:** Ein `root`-Knoten eines Binary Tree.
**Ausgabe:** Ein Array von Integern, das die Ansicht von der rechten Seite repräsentiert.

## Wann man es verwendet

- Um Ihr Verständnis für Level-Order (BFS) Traversal oder Ihre Cleverness bei der Depth-First Search zu demonstrieren.
- Eine der häufigsten Variationen des standardmäßigen Level-Order Traversals.

## Ansatz

**1. Der Level-Order (BFS) Ansatz:**
Der intuitivste Weg, dies zu lösen, besteht darin, den Baum in horizontale Ebenen zu unterteilen.
Wir verwenden eine Queue, um ein standardmäßiges Level-Order Traversal (`tree_05`) durchzuführen.
Auf jeder Ebene verarbeiten wir alle Knoten von links nach rechts. Der allerletzte Knoten, den wir auf dieser Ebene verarbeiten, ist genau der Knoten, der von der rechten Seite aus sichtbar ist! Wir fügen den Wert dieses letzten Knotens einfach unserem Ergebnis-Array hinzu, bevor wir zur nächsten Ebene übergehen.

**2. Der clevere DFS-Ansatz (Reverse Pre-Order):**
BFS erfordert $O(W)$ Platz (wobei W die maximale Breite des Baums ist). Können wir es mit DFS lösen?
Ein standardmäßiges Pre-Order DFS lautet: Root -> Left -> Right.
Was, wenn wir es umkehren? Root -> Right -> Left!
Indem wir zuerst nach rechts gehen, ist der allererste Knoten, auf den wir bei einer neuen Tiefe stoßen, mathematisch garantiert der am weitesten rechts liegende Knoten auf dieser Tiefe!
Wir geben einfach eine `depth`-Variable durch die Rekursion weiter und führen ein Array für die Ergebnisse.
Wenn `depth == len(results)` gilt, bedeutet dies, dass wir eine Tiefe erreicht haben, die wir zuvor noch nicht gesehen haben! Da wir den rechten Zweig priorisieren, muss dies der am weitesten rechts liegende Knoten sein! Wir fügen ihn zu `results` hinzu.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for tree_18: Right Side View.

BFS level-by-level; the rightmost node at each level is the
one visible from the right side. Return the list of those
nodes, top-to-bottom.
"""


def solve(children, root, n):
    """Right side view of a binary tree."""
    if root == -1:
        return []
    from collections import deque
    levels = []
    q = deque([(root, 0)])
    while q:
        u, d = q.popleft()
        while len(levels) <= d:
            levels.append([])
        levels[d].append(u)
        if children[u][0] != -1:
            q.append((children[u][0], d + 1))
        if children[u][1] != -1:
            q.append((children[u][1], d + 1))
    return [level[-1] for level in levels]
```

</details>

## Walk-through

Baum:
```text
      1
    /   \
   2     3
    \     \
     5     4
    /
   6
```

**DFS Walk-through:**
1. `dfs(1, depth=0)`: `0 == len([])`. Füge `1` hinzu. `res = [1]`.
   - Aufruf rechts: `dfs(3, depth=1)`
2. `dfs(3, depth=1)`: `1 == len([1])`. Füge `3` hinzu. `res = [1, 3]`.
   - Aufruf rechts: `dfs(4, depth=2)`
3. `dfs(4, depth=2)`: `2 == len([1, 3])`. Füge `4` hinzu. `res = [1, 3, 4]`.
   - Aufruf rechts: `dfs(null)`
   - Aufruf links: `dfs(null)`
   - Rückkehr zu 3.
   - Knoten 3 hat kein links.
   - Rückkehr zu 1.
   - Aufruf links von 1: `dfs(2, depth=1)`
4. `dfs(2, depth=1)`: `1 != len([1, 3, 4])`. Überspringe das Hinzufügen. (Er wird von 3 blockiert!)
   - Aufruf rechts: `dfs(5, depth=2)`
5. `dfs(5, depth=2)`: `2 != len([1, 3, 4])`. Überspringe das Hinzufügen. (Blockiert durch 4!)
   - Aufruf links: `dfs(6, depth=3)`
6. `dfs(6, depth=3)`: `3 == len([1, 3, 4])`. Moment, Tiefe 3 ist neu! Füge `6` hinzu.
   - `res = [1, 3, 4, 6]`.

Endergebnis: `[1, 3, 4, 6]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Sowohl bei BFS als auch bei DFS wird jeder Knoten genau einmal besucht. Die Zeitkomplexität beträgt $O(N)$.
Die Platzkomplexität unterscheidet sich leicht je nach Form des Baums:
- **DFS:** Begrenzt durch die Baumhöhe $O(H)$. Bei einem balancierten Baum beträgt der Platzbedarf $O(\log N)$. Bei einem entarteten Baum (skewed tree) verschlechtert er sich auf $O(N)$.
- **BFS:** Begrenzt durch die Baumbreite $O(W)$. Bei einem balancierten Baum hat die unterste Ebene $N/2$ Knoten, daher beträgt der Platzbedarf $O(N)$. Bei einem entarteten Baum (wie eine Linked List) ist die Breite 1, daher beträgt der Platzbedarf $O(1)$.
In Big-O-Notation sind beide im schlechtesten Fall technisch gesehen $O(N)$ Platzkomplexität.

## Varianten & Optimierungen

- **Left Side View:** Exakt die gleiche BFS-Logik (prüfe `if i == 0` anstelle von `level_length - 1`) oder exakt die gleiche DFS-Logik (traversiere `node.left` vor `node.right`).
- **Bottom View:** Eine deutlich schwierigere Variante, bei der man die horizontalen X-Koordinaten verfolgen muss (ähnlich wie beim Vertical Order Traversal) und eine Hash Map mit dem letzten Knoten überschreiben muss, der an jeder X-Koordinate gesehen wurde.

## Anwendungen in der Praxis

- **2D-Spiel-Rendering:** Rendering von 2.5D-isometrischen Bäumen oder überlappenden UI-Elementen, bei denen nur die "äußersten" Begrenzungen der hierarchischen Bounding Boxes auf den Bildschirm gezeichnet werden müssen, um GPU-Zyklen zu sparen.

## Verwandte Algorithmen in cOde(n)

- **[tree_05 - Level Order Traversal](tree_05_level-order-traversal.md)** — Die BFS-Engine, die für den iterativen Ansatz verwendet wird.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*