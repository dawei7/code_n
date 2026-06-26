# In-order Traversal

| | |
|---|---|
| **ID** | `tree_02` |
| **Kategorie** | trees |
| **Komplexität (erforderlich)** | $O(n)$ |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) |

## Problemstellung

Gegeben ist die `root` eines Binary Tree. Geben Sie ein Array zurück, das die Werte seiner Knoten in der Reihenfolge eines **In-order Traversal** enthält.

**Eingabe:** Der Wurzelknoten (root) eines Binary Tree.
**Ausgabe:** Ein Array mit den Knotenwerten.

**Beispiel:**
Gegeben sei der folgende Baum:
```
    1
     \
      2
     /
    3
```
**Ausgabe:** `[1, 3, 2]`

## Wann man es verwendet

- **Binary Search Trees (BST):** Dies ist der wichtigste Traversal-Algorithmus für einen BST. Ein In-order Traversal eines perfekt balancierten BST liefert **immer Elemente in strikt aufsteigender Reihenfolge**.
- Um einen Baum in ein Array zu flachen, beispielsweise für einfache Lookups des `k-th` kleinsten Elements.
- Bei der Auswertung von Infix-Ausdrücken (z. B. `A + B * C`) in einem Ausdrucksbaum.

## Ansatz

In-order bedeutet, dass die `Root` **zwischen** ihren Teilbäumen verarbeitet wird:
1. Rekursives Traversieren des `Left` Teilbaums.
2. Verarbeiten des aktuellen Knotens (`Root`).
3. Rekursives Traversieren des `Right` Teilbaums.

Mnemotechnik: **L N R** (Left, Node, Right).

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for tree_02: Inorder Traversal.

Multi-way tree: first-child subtree, then the node, then each
remaining child subtree left-to-right.
"""


def solve(children, root, n):
    out = []

    def walk(u):
        if children[u]:
            walk(children[u][0])
        out.append(u)
        for v in children[u][1:]:
            walk(v)

    walk(root)
    return out
```

</details>

## Durchlauf (Iterativ)

Angenommen, der Baum ist ein BST:
```
      4
    /   \
   2     6
  / \   / \
 1   3 5   7
```

1. `current = 4`. `Stack = []`.
2. Gehe nach links. Push 4, Push 2, Push 1. `current` ist None. `Stack = [4, 2, 1]`.
3. Pop 1. Verarbeite **1**. Gehe nach rechts (`current = None`).
4. Gehe nach links (übersprungen, da None).
5. Pop 2. Verarbeite **2**. Gehe nach rechts (`current = 3`).
6. Gehe nach links bei 3. Push 3. `Stack = [4, 3]`.
7. Pop 3. Verarbeite **3**. Gehe nach rechts (`None`).
8. Gehe nach links (übersprungen).
9. Pop 4. Verarbeite **4**. Gehe nach rechts (`current = 6`).
10. Gehe nach links bei 6. Push 6, Push 5. `Stack = [6, 5]`.
11. Pop 5. Verarbeite **5**. Gehe nach rechts (`None`).
12. Pop 6. Verarbeite **6**. Gehe nach rechts (`current = 7`).
13. Gehe nach links bei 7. Push 7. `Stack = [7]`.
14. Pop 7. Verarbeite **7**. Gehe nach rechts (`None`).
15. Schleife beendet.

Endergebnis: `[1, 2, 3, 4, 5, 6, 7]`. Es ist perfekt sortiert! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n)$ | $O(log n)$ |
| **Durchschnittlicher Fall** | $O(n)$ | $O(log n)$ |
| **Schlechtester Fall** | $O(n)$ | $O(n)$ |

Wir besuchen jeden einzelnen Knoten genau einmal, was zu einer Zeitkomplexität von `O(n)` führt.
Die Platzkomplexität hängt von der Baumhöhe `h` ab. In einem balancierten BST beträgt die maximale Stack-Tiefe `O(log n)`. Wenn der Baum vollständig nach links entartet ist, schiebt die innere Schleife jeden einzelnen Knoten auf den Stack, bevor ein einziger Pop erfolgt, was zu einer Speichernutzung von `O(n)` führt.

## Varianten & Optimierungen

- **Reverse In-order Traversal:** Wenn Sie `Right -> Node -> Left` traversieren, erhalten Sie die Elemente eines BST in strikt **absteigender** Reihenfolge. Dies ist äußerst nützlich, um das K-te *größte* Element zu finden.

## Anwendungen in der Praxis

- **Datenbank-Bereichsabfragen (Range Queries):** Wenn eine SQL-Abfrage `SELECT * WHERE ID BETWEEN 10 AND 50` lautet, löst der B-Tree-Index die Grenzen auf und führt dann einfach ein In-order Traversal durch, um den sortierten Bereich abzurufen.

## Verwandte Algorithmen in cOde(n)

- **[tree_01 - Pre-order Traversal](tree_01_preorder-traversal.md)** — Traversierung N, L, R.
- **[tree_06 - BST Search](tree_06_bst-search.md)** — Verständnis der BST-Invarianten.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*