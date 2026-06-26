# Binary Tree Root-to-Leaf Paths

| | |
|---|---|
| **ID** | `tree_21` |
| **Kategorie** | trees |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(H)$ Platz |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/) |

## Problemstellung

Gegeben ist die `root` eines Binary Tree. Geben Sie alle Pfade von der Wurzel bis zu einem Blatt in beliebiger Reihenfolge zurück.
Ein Blatt ist ein Knoten ohne Kinder.
Die Pfade sollten als Strings formatiert sein, wobei die Knoten durch `"->"` getrennt werden.

**Eingabe:** Ein `root`-Knoten eines Binary Tree.
**Ausgabe:** Ein Array von Strings, die die Pfade repräsentieren.

## Wann man es verwendet

- Um Kompetenz im Bereich Backtracking-basiertes DFS-Zustandsmanagement zu demonstrieren.
- Als grundlegender Baustein für jedes Pfadfindungsproblem (z. B. Path Sum II).

## Ansatz

**1. Der "String Accumulator" DFS:**
Um einen Pfad von der Wurzel bis zu einem Blatt aufzubauen, müssen wir unsere Historie durch den Baum weitergeben!
Wir schreiben eine rekursive DFS-Funktion, die den `current_node` UND den `current_path_string` als Parameter entgegennimmt.
Wenn wir einen Knoten besuchen, hängen wir dessen Wert sofort an den String an: `new_path = current_path_string + str(node.val)`.

**2. Der Blatt-Auslöser:**
Woher wissen wir, wann ein Pfad beendet ist? Wenn wir ein Blatt erreichen!
Ein Blatt ist strikt definiert als `!node.left and !node.right`.
Wenn der aktuelle Knoten ein Blatt ist, sind wir fertig! Wir hängen `new_path` direkt an unser globales `results`-Array an. Wir führen KEINE weitere Rekursion durch.

**3. Die sich verzweigenden Pfade:**
Wenn der Knoten KEIN Blatt ist, muss der Pfad fortgesetzt werden.
Wir hängen einfach `"->"` an unseren String an und übergeben ihn rekursiv an beide Kinder!
`dfs(node.left, new_path + "->")`
`dfs(node.right, new_path + "->")`
Da Strings in Python/Java unveränderlich (immutable) sind, erzeugt das Weitergeben von `new_path` an einen Zweig eine vollständig unabhängige physische Kopie des Strings im Speicher. Wenn der DFS zum Backtracking zurückkehrt, um den anderen Zweig zu durchlaufen, bleibt der ursprüngliche `new_path` völlig unberührt!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for tree_21: Root-to-Leaf Paths.

Return every root-to-leaf path as a list of node-index
lists. DFS from the root, accumulating the path; record
a copy when a leaf is reached.
"""


def solve(children, root, n):
    if n == 0 or root == -1:
        return []
    out = []

    def dfs(i, path):
        if i == -1:
            return
        path.append(i)
        if children[i][0] == -1 and children[i][1] == -1:
            out.append(list(path))
        else:
            dfs(children[i][0], path)
            dfs(children[i][1], path)
        path.pop()
    dfs(root, [])
    return out
```

</details>

## Durchlauf

Baum:
```text
      1
    /   \
   2     3
    \
     5
```

1. **`dfs(1, "")`:**
   - `path` wird zu `"1"`.
   - Knoten 1 hat Kinder. `path` wird zu `"1->"`.
   - Ruft `dfs(2, "1->")` auf.
   - Ruft `dfs(3, "1->")` auf.
2. **`dfs(2, "1->")`:**
   - `path` wird zu `"1->2"`.
   - Knoten 2 hat ein Kind (5). `path` wird zu `"1->2->"`.
   - Ruft `dfs(5, "1->2->")` auf.
3. **`dfs(5, "1->2->")`:**
   - `path` wird zu `"1->2->5"`.
   - Knoten 5 ist ein Blatt!
   - `res.append("1->2->5")`.
   - Kehrt zu 2 zurück, dann zu 1.
4. **`dfs(3, "1->")`:**
   - `path` wird zu `"1->3"`.
   - Knoten 3 ist ein Blatt!
   - `res.append("1->3")`.

Endergebnis: `["1->2->5", "1->3"]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(N^2)$ | $O(N)$ |

Die DFS-Traversierung besucht jeden einzelnen Knoten genau einmal.
Da jedoch die String-Konkatenation (`+`) physisch einen neuen String im Speicher erzeugt, wächst der String in einem extrem unausgeglichenen Baum (in Form einer Linked List) bei jedem Schritt um 1 Zeichen. Die Zeit für das Kopieren des Strings beträgt 1 + 2 + 3 ... + N = $O(N^2)$ im absoluten Schlechtesten Fall!
Um eine strikte $O(N)$-Zeit unabhängig von Sprachoptimierungen zu garantieren, müssen Sie ein Array von Werten weitergeben und nur dann `.join("->")` auf das Array anwenden, wenn Sie ein Blatt erreichen!
Die Platzkomplexität ist durch den rekursiven Aufruf-Stack $O(H)$ begrenzt.

## Varianten & Optimierungen

- **Path Sum II (Backtracking Array):** Anstatt eines Strings übergeben Sie eine laufende Summe und ein Array. Wenn `sum == target`, fügen Sie eine tiefe Kopie des Arrays zu Ihren Ergebnissen hinzu. Da Arrays veränderlich sind, MÜSSEN Sie den Knoten am Ende der DFS-Funktion explizit mit `.pop()` aus dem Array entfernen, bevor sie zurückkehrt! Dies ist Standard-Backtracking (`backtracking_01`).

## Anwendungen in der Praxis

- **Dateisystem-Crawling:** Gegeben ein hierarchischer Verzeichnisbaum (wie `C:/`), generiert dieser exakte Algorithmus die absoluten Dateipfade (z. B. `C:/Users/David/Documents/file.txt`) für jede einzelne Datei im System!

## Verwandte Algorithmen in cOde(n)

- **[tree_01 - Pre-order Traversal](tree_01_preorder-traversal.md)** — Das grundlegende Muster, das verwendet wird, um den Zustand durch den Baum weiterzugeben.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*