# Baumhöhe (Maximale Tiefe)

| | |
|---|---|
| **ID** | `tree_04` |
| **Kategorie** | Bäume |
| **Komplexität (erforderlich)** | $O(n)$ |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) |

## Problemstellung

Gegeben ist die `root` eines Binärbaums; geben Sie dessen **maximale Tiefe** (oder Höhe) zurück.

Die maximale Tiefe eines Binärbaums ist die Anzahl der Knoten entlang des längsten Pfades vom Wurzelknoten bis zum am weitesten entfernten Blattknoten.

**Eingabe:** Der Wurzelknoten eines Binärbaums.
**Ausgabe:** Eine Ganzzahl, die die Höhe repräsentiert.

**Beispiel:**
Gegeben sei der Baum:
```
      3
     / \
    9  20
      /  \
     15   7
```
**Ausgabe:** `3` (Der Pfad 3 -> 20 -> 15 hat 3 Knoten).

## Wann man es verwendet

- Als grundlegende Subroutine für hochkomplexe Baumalgorithmen.
- Um zu bestimmen, ob ein Baum balanciert ist (durch Vergleich der Höhe des linken und rechten Teilbaums).
- Um die Worst-Case-Suchzeit für einen Binary Search Tree zu bewerten (die Suche ist `O(h)`).

## Ansatz

Das Finden der Höhe eines Baums ist ein klassisches rekursives **Divide and Conquer**-Problem, das sich hervorragend auf eine **Post-order**-Traversierung abbilden lässt.

Wenn Sie die maximale Tiefe eines Baums ausgehend von Knoten `A` wissen möchten, müssen Sie lediglich zwei Fragen stellen:
1. Was ist die maximale Tiefe meines linken Teilbaums?
2. Was ist die maximale Tiefe meines rechten Teilbaums?

Die Höhe von `A` ist einfach das Maximum dieser beiden Zahlen, plus `1` (um `A` selbst zu berücksichtigen).
Wenn der Knoten `None` (leer) ist, beträgt seine Tiefe mathematisch `0`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for tree_04: Tree Height.

A leaf has height 0; a non-leaf has height 1 + max(child height).
"""


def solve(children, root, n):
    def depth(u):
        if not children[u]:
            return 0
        return 1 + max(depth(v) for v in children[u])
    return depth(root)
```

</details>

## Durchlauf (Rekursiv)

Sei der Baum:
```
    A
     \
      B
     /
    C
```

Aufruf von `max_depth(A)`:
- `left_depth = max_depth(None)` -> gibt `0` zurück.
- `right_depth = max_depth(B)`:
  - `left_depth = max_depth(C)`:
    - `left_depth = max_depth(None)` -> gibt `0` zurück.
    - `right_depth = max_depth(None)` -> gibt `0` zurück.
    - Gibt `max(0, 0) + 1` = `1` zurück. (Höhe von C ist 1).
  - `right_depth = max_depth(None)` -> gibt `0` zurück.
  - Gibt `max(1, 0) + 1` = `2` zurück. (Höhe von B ist 2).
- Gibt `max(0, 2) + 1` = `3` zurück.

Endergebnis: `3`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n)$ | $O(log n)$ |
| **Durchschnittlicher Fall** | $O(n)$ | $O(log n)$ |
| **Schlechtester Fall** | $O(n)$ | $O(n)$ |

Wir müssen jeden einzelnen Knoten besuchen, um sicherzustellen, dass wir keinen tiefen, versteckten Zweig übersehen, daher ist die Zeit strikt `O(n)`.
Die Platzkomplexität wird durch den Rekursions-Stack (bei DFS) oder die Queue-Größe (bei BFS) bestimmt. Im schlechtesten Fall (einer Linked List) benötigt DFS `O(n)` Stack-Platz. Bei BFS hält die Queue maximal N/2 Knoten auf der breitesten Ebene, was bedeutet, dass BFS in perfekt balancierten Bäumen `O(n)` Heap-Platz benötigt.

## Varianten & Optimierungen

- **Minimale Tiefe:** Ein sehr ähnlicher Algorithmus, der den kürzesten Pfad zu einem Blatt findet. Im Gegensatz zur maximalen Tiefe müssen Sie vorsichtig sein: Wenn ein Knoten nur ein Kind hat, ist die minimale Tiefe NICHT `0` (das leere Kind), Sie müssen den gültigen Kindknoten weiter traversieren.
- **N-äre Bäume:** Anstatt `max(left, right)` zu verwenden, iterieren Sie einfach über `node.children` und verfolgen Sie das laufende Maximum der `depth`.

## Anwendungen in der Praxis

- **AVL-Bäume / Rot-Schwarz-Bäume:** Balancierungsmechanismen in selbstbalancierenden Bäumen überprüfen während des Einfügens ständig die relativen Höhen der Teilbäume, um zu wissen, wann Rotationsalgorithmen ausgelöst werden müssen.

## Verwandte Algorithmen in cOde(n)

- **[tree_11 - Balanced Tree Check](tree_11_balanced-tree-check.md)** — Ein Algorithmus, der direkt auf `max_depth` aufbaut, um die allgemeine Integrität einer Baumstruktur zu überprüfen.
- **[tree_05 - Level Order Traversal](tree_05_level-order-traversal.md)** — Die BFS-Technik, die beim iterativen Ansatz verwendet wird.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*