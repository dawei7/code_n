# Symmetric Tree Check

| | |
|---|---|
| **ID** | `tree_14` |
| **Category** | trees |
| **Complexity (required)** | $O(N)$ Time, $O(H)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Symmetric Tree](https://leetcode.com/problems/symmetric-tree/) |

## Problem statement

*(Hinweis: Dies ist eine Duplikat-Datei für die Symmetric Tree-Logik, ursprünglich identisch mit `tree_12`)*

Gegeben ist der `root` eines Binary Tree. Prüfen Sie, ob er ein Spiegelbild seiner selbst ist (d. h. symmetrisch um seine Mitte).

**Eingabe:** Ein `root`-Knoten eines Binary Tree.
**Ausgabe:** Ein Boolean, der angibt, ob der Baum symmetrisch ist.

## Wann man es verwendet

- Um die Fähigkeit zu testen, zwei verschiedene Bäume (oder zwei verschiedene Zweige desselben Baums) gleichzeitig zu traversieren.
- Eine natürliche Weiterentwicklung der Prüfung, ob zwei Bäume identisch sind (`Same Tree`).

## Ansatz

**1. Die "Two Pointer" Tree Traversal:**
Wenn wir prüfen wollen, ob die linke Seite des Baums ein Spiegelbild der rechten Seite ist, können wir einfach zwei gleichzeitige DFS-Traversierungen durchführen!
Wir starten einen Pointer `left_ptr` bei `root.left` und einen weiteren Pointer `right_ptr` bei `root.right`.

**2. Die Spiegelbedingungen:**
Damit der Baum auf der aktuellen Ebene symmetrisch ist, müssen drei Dinge erfüllt sein:
1. `left_ptr.val` MUSS gleich `right_ptr.val` sein.
2. Das LINKE Kind des `left_ptr` MUSS das RECHTE Kind des `right_ptr` spiegeln. (Äußere Kanten).
3. Das RECHTE Kind des `left_ptr` MUSS das LINKE Kind des `right_ptr` spiegeln. (Innere Kanten).

**3. Die rekursiven Basisfälle:**
- Wenn BEIDE Pointer `null` sind, haben wir das Ende perfekt erreicht. Gib `True` zurück.
- Wenn EIN Pointer `null` ist, der andere aber NICHT, stimmen die strukturellen Formen nicht überein! Gib `False` zurück.
- Wenn ihre Werte nicht übereinstimmen, gib `False` zurück.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for tree_14: Symmetric Tree Check.

Return True iff the binary tree is symmetric around
"""


def solve(children, root, n):
    """True iff the binary tree is a mirror of itself around the root."""
    if root == -1:
        return True

    def is_mirror(a, b):
        if a == -1 and b == -1:
            return True
        if a == -1 or b == -1:
            return False
        return (
            is_mirror(children[a][0], children[b][1])
            and is_mirror(children[a][1], children[b][0])
        )

    return is_mirror(children[root][0], children[root][1])
```

</details>

## Walk-through

Baum:
```text
      1
     / \
    2   2
   / \ / \
  3  4 4  3
```

1. **`is_mirror(2 (links), 2 (rechts))`:**
   - Werte stimmen überein (`2 == 2`).
   - Rekursiver Aufruf:
     - `is_mirror(3 (links), 3 (rechts))` -> Äußere Kanten
     - `is_mirror(4 (links), 4 (rechts))` -> Innere Kanten
2. **`is_mirror(3, 3)`:**
   - Werte stimmen überein (`3 == 3`).
   - Ruft `is_mirror(null, null)` und `is_mirror(null, null)` auf. Beide geben `True` zurück.
   - Gibt `True` zurück.
3. **`is_mirror(4, 4)`:**
   - Werte stimmen überein (`4 == 4`).
   - Ruft `is_mirror(null, null)` und `is_mirror(null, null)` auf. Beide geben `True` zurück.
   - Gibt `True` zurück.
4. Der erste Aufruf gibt `True AND True` => `True` zurück.

Gibt `True` zurück. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Wir traversieren jeden einzelnen Knoten im Baum genau einmal (oder die Hälfte der Knoten zweimal, was mathematisch äquivalent zu $O(N)$ ist). Die Zeitkomplexität ist strikt $O(N)$.
Die Platzkomplexität ist durch den rekursiven Call Stack (DFS) oder die Queue (BFS) begrenzt.
Bei DFS ist die maximale Tiefe des Call Stacks $O(H)$. Im schlechtesten Fall (ein völlig einseitiger Baum) verschlechtert sich dies auf $O(N)$. Bei einem balancierten symmetrischen Baum beträgt sie $O(\log N)$.
Bei BFS hält die Queue auf der untersten Ebene maximal N/2 Paare, was einer Platzkomplexität von strikt $O(N)$ entspricht.

## Varianten & Optimierungen

- **Same Tree:** Exakt derselbe Algorithmus, aber anstatt die Zweige zu kreuzen (`t1.left, t2.right`), prüft man identische Zweige (`t1.left, t2.left`).
- **Subtree of Another Tree:** Ein zweiteiliger Algorithmus, bei dem man eine Standard-DFS auf dem Hauptbaum durchführt und bei jedem Knoten den `Same Tree`-Algorithmus gegen den Ziel-Subtree auslöst!

## Anwendungen in der Praxis

- **Computer Vision / 3D-Modellierung:** Überprüfung, ob ein generiertes 3D-Mesh (oft als BSP-Tree oder Octree gespeichert) perfekt symmetrisch zu einer Achse ist, bevor physikalische Berechnungen oder Rendering-Optimierungen angewendet werden.

## Verwandte Algorithmen in cOde(n)

- **[tree_09 - Mirror Tree](tree_09_mirror-tree.md)** — Der aktive Algorithmus, um einen Baum physisch in sein Spiegelbild zu mutieren.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*