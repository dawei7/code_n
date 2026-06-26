# Pre-order Traversal

| | |
|---|---|
| **ID** | `tree_01` |
| **Kategorie** | trees |
| **Komplexität (erforderlich)** | $O(n)$ |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/) |

## Problemstellung

Gegeben ist die `root` eines Binary Tree. Geben Sie ein Array zurück, das die Werte seiner Knoten in der Reihenfolge der **Pre-order Traversal** enthält.

**Eingabe:** Der Wurzelknoten eines Binary Tree.
**Ausgabe:** Ein Array mit den Knotenwerten.

**Beispiel:**
Gegeben sei der Baum:
```
    1
     \
      2
     /
    3
```
**Ausgabe:** `[1, 2, 3]`

## Anwendungsbereiche

- Zum Erstellen einer **Kopie** (Klon) eines Baums. Die Pre-order Traversal serialisiert die Wurzel zuerst, was es ermöglicht, den Baum einfach von oben nach unten zu rekonstruieren.
- Beim Auswerten von Präfix-Ausdrücken (z. B. `+ * A B C`) in einem Ausdrucksbaum.
- Beim Durchsuchen von Verzeichnisstrukturen in einem Betriebssystem (man möchte das übergeordnete Verzeichnis besuchen, bevor man dessen Unterordner erkundet).

## Ansatz

Es gibt drei primäre Depth-First Search (DFS) Traversierungen für Binary Trees: Pre-order, In-order und Post-order.
Der Name spezifiziert genau, wann der **aktuelle Knoten (Root)** im Verhältnis zu seinen Kindern verarbeitet wird.

**Pre**-order bedeutet, dass die Wurzel **vor** ihren Teilbäumen verarbeitet wird:
1. Verarbeite den aktuellen Knoten (`Root`).
2. Traveriere rekursiv den `Left` Teilbaum.
3. Traveriere rekursiv den `Right` Teilbaum.

Eselsbrücke: **N L R** (Node, Left, Right).

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for tree_01: Preorder Traversal.

Multi-way tree: children[i] is the list of i's children. Visit
the node, then recurse on each child left-to-right.
"""


def solve(children, root, n):
    out = []

    def walk(u):
        out.append(u)
        for v in children[u]:
            walk(v)

    walk(root)
    return out
```

</details>

## Durchlauf (Iterativ)

Sei der Baum wie folgt gegeben:
```
      A
    /   \
   B     C
  / \   /
 D   E F
```

1. Init: `Stack = [A]`. `Result = []`
2. Pop `A`. `Result = [A]`. Push `A.right` (C), dann `A.left` (B). `Stack = [C, B]`.
3. Pop `B`. `Result = [A, B]`. Push `E`, dann `D`. `Stack = [C, E, D]`.
4. Pop `D`. `Result = [A, B, D]`. `D` hat keine Kinder. `Stack = [C, E]`.
5. Pop `E`. `Result = [A, B, D, E]`. `E` hat keine Kinder. `Stack = [C]`.
6. Pop `C`. `Result = [A, B, D, E, C]`. Push `C.right` (None), dann `F`. `Stack = [F]`.
7. Pop `F`. `Result = [A, B, D, E, C, F]`. Keine Kinder. `Stack = []`.

Schleife beendet. Ausgabe: `A -> B -> D -> E -> C -> F`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n)$ | $O(log n)$ |
| **Durchschnittlicher Fall** | $O(n)$ | $O(log n)$ |
| **Schlechtester Fall** | $O(n)$ | $O(n)$ |

Wir besuchen jeden einzelnen Knoten genau einmal, was strikt `O(n)` Zeit in Anspruch nimmt.
Die Platzkomplexität hängt von der Höhe des Baums `h` ab. In einem perfekt balancierten Baum beträgt die maximale Tiefe (und damit die maximale Größe des Rekursions-Stacks oder des expliziten Stacks) `O(log n)`. Im schlechtesten Fall (einem komplett unbalancierten, Linked-List-artigen Baum) wächst die Stack-Tiefe auf `O(n)`.

## Varianten & Optimierungen

- **Morris Traversal:** Ein brillanter `O(1)` Platz-Algorithmus, der die Baumstruktur temporär modifiziert, indem er Links von den Blättern zurück zu ihren Vorfahren erstellt. Er eliminiert die Notwendigkeit sowohl für den Call-Stack als auch für explizite Stacks, mutiert jedoch den Baum während der Traversierung.

## Anwendungen in der Praxis

- **DOM-Rendering:** Wenn ein Browser HTML parst, rendert er die übergeordneten Tags (wie `<div>`), bevor er rekursiv in die Tiefe geht, um die untergeordneten Tags (wie `<p>`) zu rendern.
- **Baum-Serialisierung:** JSON-Parsing/Stringifizierung funktioniert effektiv über Pre-order DFS-Traversierungen eines Objektgraphen.

## Verwandte Algorithmen in cOde(n)

- **[tree_02 - In-order Traversal](tree_02_inorder-traversal.md)** — Traveriere L, N, R.
- **[tree_03 - Post-order Traversal](tree_03_postorder-traversal.md)** — Traveriere L, R, N.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*