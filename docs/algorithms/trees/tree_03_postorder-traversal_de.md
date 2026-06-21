# Post-order Traversal

| | |
|---|---|
| **ID** | `tree_03` |
| **Kategorie** | trees |
| **Komplexität (erforderlich)** | $O(n)$ |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/) |

## Problemstellung

Gegeben ist die `root` eines Binary Tree. Geben Sie ein Array zurück, das die Werte seiner Knoten in der Reihenfolge eines **Post-order Traversal** enthält.

**Eingabe:** Der Wurzelknoten eines Binary Tree.
**Ausgabe:** Ein Array mit den Knotenwerten.

**Beispiel:**
Gegeben ist der folgende Baum:
```
    1
     \
      2
     /
    3
```
**Ausgabe:** `[3, 2, 1]`

## Wann man es verwendet

- Um einen Baum sicher zu **löschen**. Sie MÜSSEN die Kinder eines Knotens löschen, bevor Sie den Speicher des Knotens selbst sicher freigeben können. Post-order garantiert, dass die Kinder zuerst verarbeitet werden.
- Um den Speicherplatz/die Größe/die Höhe eines Verzeichnisses zu berechnen. Die Gesamtgröße eines Ordners ist die Summe seiner Dateien + die Summe aller Unterordner. Sie müssen die Unterordner (Kinder) vollständig berechnen, bevor Sie den übergeordneten Ordner berechnen können.
- Bei der Auswertung von Postfix-Ausdrücken (Umgekehrte Polnische Notation, z. B. `A B C * +`).

## Ansatz

Post-order bedeutet, dass die Wurzel **nach** ihren Teilbäumen verarbeitet wird:
1. Rekursives Traversieren des `Left` Teilbaums.
2. Rekursives Traversieren des `Right` Teilbaums.
3. Verarbeiten des aktuellen Knotens (`Root`).

Eselsbrücke: **L R N** (Left, Right, Node).

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for tree_03: Postorder Traversal.

Multi-way tree: recurse on each child subtree, then visit the node.
"""


def solve(children, root, n):
    out = []

    def walk(u):
        for v in children[u]:
            walk(v)
        out.append(u)

    walk(root)
    return out
```

</details>

## Durchlauf (Zwei-Stack-Methode)

Baum:
```
      A
    /   \
   B     C
```

1. `stack1 = [A]`, `stack2 = []`.
2. `A` per `pop` entfernen. In `stack2` pushen. `stack2 = [A]`.
3. `A.left` (B) pushen. `A.right` (C) pushen. `stack1 = [B, C]`.
4. `C` per `pop` entfernen. In `stack2` pushen. `stack2 = [A, C]`.
5. `C` hat keine Kinder.
6. `B` per `pop` entfernen. In `stack2` pushen. `stack2 = [A, C, B]`.
7. `B` hat keine Kinder.
8. `stack1` ist leer.
9. `stack2` per `pop` in ein Array übertragen: `B` entfernen, `C` entfernen, `A` entfernen.

Ausgabe: `[B, C, A]`. (Left, Right, Node). ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n)$ | $O(log n)$ |
| **Durchschnittlicher Fall** | $O(n)$ | $O(log n)$ |
| **Schlechtester Fall** | $O(n)$ | $O(n)$ |

*(Hinweis: Die Zwei-Stack-Methode verwendet strikt $O(n)$ Platz, aber eine echte 1-Stack-Lösung skaliert basierend auf der Höhe).*
Wir besuchen jeden Knoten einmal, was $O(n)$ Zeit in Anspruch nimmt. Eine korrekte 1-Stack-Implementierung verwendet $O(h)$ Speicher, was je nach Ausgewogenheit des Baums zwischen $O(log n)$ und $O(n)$ liegt.

## Varianten & Optimierungen

- **1-Stack-Ansatz:** Um nur einen Stack zu verwenden, müssen Sie einen `last_visited` Pointer beibehalten. Wenn Sie einen `peek` auf das oberste Element des Stacks ausführen und dessen `right` Kind `None` ist oder dem `last_visited` entspricht, bedeutet dies, dass Sie beide Zweige vollständig erkundet haben und den Knoten sicher per `pop` entfernen und verarbeiten können. Andernfalls müssen Sie dessen `right` Kind pushen und tiefer in den Baum absteigen.

## Anwendungen in der Praxis

- **AST-Codegenerierung:** Wenn ein Compiler einen Abstract Syntax Tree in Maschinencode oder Bytecode umwandelt, verwendet er Post-order Traversal. Sie können den `ADD` Assembler-Befehl erst ausgeben, wenn Sie den Code ausgegeben haben, der beide Operanden-Variablen in die CPU-Register lädt.

## Verwandte Algorithmen in cOde(n)

- **[tree_01 - Pre-order Traversal](tree_01_preorder-traversal.md)** — Traversierung N, L, R.
- **[tree_02 - In-order Traversal](tree_02_inorder-traversal.md)** — Traversierung L, N, R.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Seiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*