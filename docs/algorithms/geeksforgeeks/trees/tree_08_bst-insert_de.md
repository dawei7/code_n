# Binary Search Tree (BST) Insert

| | |
|---|---|
| **ID** | `tree_08` |
| **Kategorie** | trees |
| **Komplexität (erforderlich)** | $O(H)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/) |

## Problemstellung

Gegeben ist der `root`-Knoten eines Binary Search Tree (BST) und ein `value`, das in den Baum eingefügt werden soll. Geben Sie den `root`-Knoten des BST nach dem Einfügen zurück.
Es wird garantiert, dass der neue Wert im ursprünglichen BST noch nicht existiert.
Sie müssen den neuen Knoten so einfügen, dass die mathematischen Invarianten des BST vollständig erhalten bleiben.

**Eingabe:** Ein BST `root`-Knoten und eine Ganzzahl `val`.
**Ausgabe:** Der `root`-Knoten des modifizierten BST.

## Wann man es verwendet

- Um einen Binary Search Tree von Grund auf neu aufzubauen.
- Eine extrem häufige Aufwärmübung in Vorstellungsgesprächen, die Ihr Verständnis von Tree-Pointern und der BST-Eigenschaft testet.

## Ansatz

**1. Die Blatt-Garantie:**
In einem standardmäßigen, nicht balancierten BST gibt es unendlich viele gültige Stellen, um einen neuen Wert einzufügen, die die mathematische Eigenschaft erfüllen.
Es gibt jedoch genau EINE Stelle, die absolut trivial zu finden ist: **Als neuer Blattknoten ganz unten im Baum!**
Wir müssen den Baum niemals umstrukturieren, Knoten vertauschen oder Teilbäume verschieben. Wir fügen den neuen Knoten einfach dort ein, wo er natürlicherweise am unteren Ende landet.

**2. Die Strategie der "fehlgeschlagenen Suche":**
Wie finden wir heraus, wo er natürlicherweise landet? Wir tun einfach so, als würden wir nach dem Wert SUCHEN (`tree_06`)!
Wir beginnen an der Wurzel.
- Wenn `val` < current, gehen wir nach links.
- Wenn `val` > current, gehen wir nach rechts.
Da der Wert im Baum nicht existiert, wird unsere Suche irgendwann in einer Sackgasse enden (einem `null`-Pointer).
Genau diese `null`-Stelle ist mathematisch der perfekte Ort, um unseren neuen Knoten anzuhängen!

**3. Pointer-Verwaltung:**
Wenn wir dies iterativ durchführen, müssen wir vorsichtig sein! Wenn `curr` zu `null` wird, haben wir den Baum verlassen und können unseren neuen Knoten nicht mehr anhängen, da wir die Referenz auf unseren Elternknoten verloren haben!
Daher müssen wir einen nachlaufenden Pointer `parent` verwenden, um den letzten gültigen Knoten im Auge zu behalten, auf dem wir standen, bevor wir den Baum verlassen haben.
Sobald wir den Baum verlassen, hängen wir den neuen Knoten je nach Wert an `parent.left` oder `parent.right` an!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for tree_08: BST Insert.

Walk a BST, insert at the first empty child slot.
"""


def solve(children, values, root, n, key):
    new_children = [list(c) for c in children]
    new_values = list(values)
    if n == 0:
        new_values.append(key)
        new_children.append([-1, -1])
        return new_children, new_values
    u = root
    while True:
        if key == new_values[u]:
            return new_children, new_values
        if key < new_values[u]:
            left, right = new_children[u]
            if left == -1:
                new_idx = len(new_values)
                new_values.append(key)
                new_children.append([-1, -1])
                new_children[u][0] = new_idx
                return new_children, new_values
            u = left
        else:
            left, right = new_children[u]
            if right == -1:
                new_idx = len(new_values)
                new_values.append(key)
                new_children.append([-1, -1])
                new_children[u][1] = new_idx
                return new_children, new_values
            u = right
```

</details>

## Durchlauf

`Tree = [4, 2, 7, 1, 3]`, `val = 5`.
Baumstruktur:
```text
      4
    /   \
   2     7
  / \
 1   3
```

1. `curr = 4`, `parent = None`.
   - `val (5) > 4`. Gehe nach rechts.
   - `parent` wird zu `4`. `curr` wird zu `7`.
2. `curr = 7`.
   - `val (5) < 7`. Gehe nach links.
   - `parent` wird zu `7`. `curr` wird zu `curr.left` (was `None` ist).
3. Die Schleife endet, weil `curr is None`!
4. Wir sind bei `parent = 7` aus dem Baum gefallen.
5. Überprüfung: `val (5) < parent.val (7)`.
6. Anhängen: `parent.left = new TreeNode(5)`.

Neuer Baum:
```text
      4
    /   \
   2     7
  / \   /
 1   3 5
```
Gibt Wurzel `4` zurück. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(\log N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Sei H die Höhe des Baumes.
Die iterative Traversierung geht pro Schritt genau eine Ebene tiefer, bis sie ein Blatt erreicht. Die Anzahl der Schritte entspricht exakt der Tiefe des Einfügepunktes.
Daher ist die Zeitkomplexität genau $O(H)$.
Wenn der Baum balanciert ist, gilt H = log_2 N. Wenn er stark einseitig ist, gilt H = N.
Die Platzkomplexität für die iterative Version ist $O(1)$ (konstanter Platz), da wir nur Speicher für den einen neuen Knoten zuweisen. (Die rekursive Version benötigt $O(H)$ Platz auf dem Call Stack).

## Varianten & Optimierungen

- **AVL Tree Insert (`tree_22`):** Dieses einfache Einfügen ist schnell, aber das Einfügen von sortierten Daten (`1, 2, 3, 4, 5`) lässt den Baum zu einer $O(N)$ Linked List degenerieren. Ein AVL-Insert führt genau diesen Algorithmus aus, verfolgt dann aber den Pfad rückwärts den Baum hinauf, berechnet an jedem Knoten den "Balance Factor" und rotiert mathematisch die Knoten, um zu garantieren, dass die Höhe des Baumes strikt $O(\log N)$ bleibt!

## Anwendungen in der Praxis

- **Set / Map Implementierungen:** In C++ sind `std::set` und `std::map` intern als Red-Black Trees (eine selbstbalancierende Variante des BST) implementiert. Jedes Mal, wenn Sie `set.insert(5)` aufrufen, wird im Hintergrund eine identische Variante dieses Algorithmus ausgeführt!

## Verwandte Algorithmen in cOde(n)

- **[tree_06 - BST Search](tree_06_bst-search.md)** — Der schreibgeschützte Algorithmus, der exakt dieselbe `while curr is not None`-Pfadlogik verwendet.
- **[tree_15 - BST Delete](tree_15_bst-delete.md)** — Die unglaublich komplizierte Schwesteroperation (das Löschen eines Knotens ist wesentlich schwieriger, da Sie die Kinder umstrukturieren müssen!).

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*