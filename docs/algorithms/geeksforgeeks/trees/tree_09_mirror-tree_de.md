# Invert/Mirror Binary Tree

| | |
|---|---|
| **ID** | `tree_09` |
| **Kategorie** | trees |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(H)$ Platz |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Invert Binary Tree](https://leetcode.com/problems/invert-birnary-tree/) |

## Problemstellung

Gegeben ist der `root` eines Binary Tree. Invertieren Sie den Baum und geben Sie dessen `root` zurück.
Das Invertieren eines Binary Tree bedeutet, die linken und rechten Kinder JEDES Knotens im Baum zu vertauschen. Der resultierende Baum sollte ein perfektes Spiegelbild des ursprünglichen Baums sein.

**Eingabe:** Ein `root`-Knoten eines Binary Tree.
**Ausgabe:** Der `root`-Knoten des invertierten Baums.

## Wann wird es verwendet?

- Die berüchtigtste Interview-Frage aller Zeiten, größtenteils aufgrund des viralen Tweets von Max Howell (dem Erfinder von Homebrew): *"Google: 90% unserer Ingenieure nutzen die Software, die du geschrieben hast (Homebrew), aber du kannst keinen Binary Tree an einem Whiteboard invertieren, also verpiss dich."*
- Zum Testen grundlegender rekursiver Baum-Traversierung und des Vertauschens von Pointern.

## Ansatz

**1. Die Analogie des "Top-Down-Tauschs":**
Wenn Sie einen gesamten Baum spiegeln möchten, beginnen Sie an der `root`.
Sie vertauschen physisch den linken Kind-Zweig der `root` mit dem rechten Kind-Zweig.
Nun ist die oberste Ebene gespiegelt! Aber die Subtrees selbst befinden sich noch in ihrer ursprünglichen Reihenfolge.
Also gehen Sie in den linken Subtree hinunter und vertauschen dessen Kinder. Dann gehen Sie in den rechten Subtree hinunter und vertauschen dessen Kinder.
Sie setzen diesen Prozess rekursiv fort, bis Sie den absoluten Boden des Baums erreichen (ein `null`-Blatt).

**2. Die DFS Pre-Order-Traversierung:**
Diese Logik entspricht perfekt einer rekursiven Depth First Search (DFS).
An jedem gegebenen `node`:
1. Speichern Sie den `node.left` Pointer in einer temporären Variable.
2. Überschreiben Sie `node.left` mit `node.right`.
3. Überschreiben Sie `node.right` mit der temporären Variable.
4. Rufen Sie die Funktion rekursiv für den neuen `node.left` auf.
5. Rufen Sie die Funktion rekursiv für den neuen `node.right` auf.

**3. Die BFS-Alternative:**
Sie können dies auch iterativ mithilfe einer Breadth First Search (BFS) und einer Queue erreichen!
Anstatt eines rekursiven Call-Stacks fügen Sie die `root` in eine Queue ein.
Solange die Queue nicht leer ist, entnehmen Sie einen Knoten, vertauschen dessen Kinder und fügen alle nicht-null Kinder in die Queue ein, um sie später zu vertauschen.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for tree_09: Mirror Tree.

Reverse every node's child list.
"""


def solve(children, root, n):
    return [list(reversed(c)) for c in children]
```

</details>

## Durchlauf

Ursprünglicher Baum:
```text
      4
    /   \
   2     7
  / \   / \
 1   3 6   9
```

**Rekursive DFS:**
1. **`invert(4)`:**
   - Vertausche Kinder von 4. `4.left` wird `7`, `4.right` wird `2`.
   - Rufe `invert(7)` auf.
2. **`invert(7)`:** (Hinweis: dies ist aktuell das *linke* Kind von 4)
   - Vertausche Kinder von 7. `7.left` wird `9`, `7.right` wird `6`.
   - Rufe `invert(9)` auf. `9` ist ein Blatt, es vertauscht seine `null`-Kinder und kehrt zurück.
   - Rufe `invert(6)` auf. `6` ist ein Blatt, kehrt zurück.
3. **`invert(2)`:** (Hinweis: dies ist aktuell das *rechte* Kind von 4)
   - Vertausche Kinder von 2. `2.left` wird `3`, `2.right` wird `1`.
   - Rufe `invert(3)` auf. Kehrt zurück.
   - Rufe `invert(1)` auf. Kehrt zurück.

Resultierender Baum:
```text
      4
    /   \
   7     2
  / \   / \
 9   6 3   1
```
Perfekt gespiegelt! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Jeder einzelne Knoten im Baum muss exakt einmal besucht werden, um seine Kinder zu vertauschen. Das Besuchen eines Knotens benötigt $O(1)$ Zeit. Die Zeitkomplexität ist strikt $O(N)$.
Die Platzkomplexität ist durch den rekursiven Call-Stack (oder die Größe der BFS-Queue) begrenzt.
Für DFS ist die maximale Tiefe des Call-Stacks die Höhe des Baums $O(H)$. Im schlechtesten Fall (einem entarteten, Linked-List-ähnlichen Baum) ist dies $O(N)$. In einem balancierten Baum ist es $O(\log N)$.
Für BFS ist die maximale Queue-Größe die Breite der untersten Ebene des Baums. In einem perfekt balancierten Baum ist dies N/2, was strikt zu $O(N)$ Platz vereinfacht wird.

## Varianten & Optimierungen

- **Symmetric Tree (`tree_12`):** Ein verwandtes Problem, das fragt, ob ein Baum ein Spiegelbild seiner SELBST ist. (d. h. ist der linke Subtree eine exakte Invertierung des rechten Subtrees?).

## Anwendungen in der Praxis

- **Computergrafik / UI-Rendering:** Wenn ein Entwickler ein komplexes UI-Element oder ein 3D-Objekt erstellt, das als Scene Graph (Baum) repräsentiert wird, erfordert das horizontale "Spiegeln" des Objekts eine algorithmische Baum-Invertierung!

## Verwandte Algorithmen in cOde(n)

- **[tree_01 - Pre-order Traversal](tree_01_preorder-traversal.md)** — Das grundlegende rekursive Muster, das von der DFS-Lösung verwendet wird.
- **[tree_05 - Level Order Traversal](tree_05_level-order-traversal.md)** — Das grundlegende Queue-basierte Muster, das von der BFS-Lösung verwendet wird.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Seiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*