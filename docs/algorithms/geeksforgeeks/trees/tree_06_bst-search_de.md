# Binary Search Tree (BST) Suche

| | |
|---|---|
| **ID** | `tree_06` |
| **Kategorie** | Bäume |
| **Komplexität (erforderlich)** | $O(H)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/) |

## Problemstellung

Gegeben ist die `root` eines Binary Search Tree (BST) und ein Integer `val`.
Finde den Knoten im BST, dessen Wert gleich `val` ist, und gib den Teilbaum zurück, dessen Wurzel dieser Knoten ist. Falls ein solcher Knoten nicht existiert, gib `null` zurück.

**Eingabe:** Ein BST `root`-Knoten und ein Integer `val`.
**Ausgabe:** Der gesuchte `Node` oder `null`.

## Wann man es verwendet

- Um extrem schnelle Suchvorgänge in sortierten, hierarchischen Daten durchzuführen.
- Als grundlegender Baustein, der beweist, warum BSTs für die Suche mathematisch Linked Lists überlegen sind.

## Ansatz

**1. Die BST-Eigenschaft:**
Ein Binary Search Tree ist kein zufälliger Baum. Er besitzt eine strikte mathematische Invariante:
Für JEDEN Knoten sind alle Werte in seinem **Left Subtree** strikt KLEINER als der Wert des Knotens. Alle Werte in seinem **Right Subtree** sind strikt GRÖSSER als der Wert des Knotens.

**2. Die Analogie zur binären Suche:**
Diese Eigenschaft spiegelt exakt wider, wie eine standardmäßige binäre Suche (`search_02`) auf einem sortierten Array funktioniert!
Wenn wir uns an einem `current_node` befinden, vergleichen wir dessen Wert mit unserem `target`.
- Wenn `target == current_node.val`: Wir haben ihn gefunden! Gib den Knoten zurück.
- Wenn `target < current_node.val`: Das Ziel ist kleiner. Aufgrund der BST-Eigenschaft sind wir uns zu 100 % mathematisch sicher, dass das Ziel, falls es existiert, im Left Subtree liegen MUSS! Wir verwerfen den Right Subtree vollständig und gehen zu `current_node.left` über.
- Wenn `target > current_node.val`: Das Ziel ist größer. Es MUSS im Right Subtree liegen! Verwirf den Left Subtree und gehe zu `current_node.right` über.

**3. Rekursion vs. Iteration:**
Da wir uns immer nur entlang eines einzigen Pfades nach unten bewegen (wir verzweigen nie und müssen nie zurückkehren), benötigen wir eigentlich keine Rekursion! Eine einfache `while`-Schleife, die einen Pointer aktualisiert, erreicht dieselbe Logik, jedoch mit $O(1)$ Speicher anstelle von $O(H)$ Call-Stack-Speicher.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for tree_06: BST Search.

Walk a binary search tree, comparing the target to each node's
value, going left or right accordingly.
"""


def solve(children, values, root, n, target):
    u = root
    while u is not None and u != -1:
        if values[u] == target:
            return u
        left, right = children[u]
        if target < values[u]:
            u = left if left != -1 else None
        else:
            u = right if right != -1 else None
    return -1
```

</details>

## Durchlauf

`Tree = [4, 2, 7, 1, 3]`, `target = 2`.
Baumstruktur:
```text
      4
    /   \
   2     7
  / \
 1   3
```

1. `curr` zeigt auf `4`.
   - `4 == 2`? Nein.
   - `2 < 4`? Ja! Das Ziel muss links liegen.
   - `curr = curr.left` (zeigt auf `2`).
2. `curr` zeigt auf `2`.
   - `2 == 2`? Ja! Treffer gefunden!
   - Gib den Knoten `2` zurück. ✓

`target = 5`.
1. `curr` zeigt auf `4`.
   - `5 > 4`. Gehe nach rechts. `curr` zeigt auf `7`.
2. `curr` zeigt auf `7`.
   - `5 < 7`. Gehe nach links. `curr = curr.left`.
3. Knoten `7` hat kein linkes Kind! `curr.left` ist `None`.
4. Die Schleife terminiert, da `curr is None`.
5. Gib `None` zurück. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(\log N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Sei H die Höhe des Baumes.
Bei jedem Schritt steigen wir exakt eine Ebene tiefer in den Baum hinab. Wir besuchen Knoten nie erneut. Die maximale Anzahl an Vergleichen entspricht exakt der Höhe des Baumes.
Daher ist die Zeitkomplexität $O(H)$.
Wenn der Baum perfekt balanciert ist (z. B. ein AVL- oder Rot-Schwarz-Baum), ist die Höhe H = log_2 N. Die Zeit beträgt $O(\log N)$.
**SCHLECHTESTER FALL:** Wenn Elemente in sortierter Reihenfolge in den Baum eingefügt wurden (z. B. 1, 2, 3, 4, 5), entartet der Baum zu einer geraden Linie (einer Linked List). Die Höhe wird zu H = N. Die Zeit verschlechtert sich auf $O(N)$!
Die Platzkomplexität für die iterative Version ist strikt $O(1)$.

## Varianten & Optimierungen

- **Closest Value in BST:** Anstatt exakt dann zurückzugeben, wenn `curr.val == val`, pflegt man eine Variable `closest_val`. Bei jedem Knoten prüft man, ob `abs(curr.val - target) < abs(closest_val - target)`. Man bewegt sich weiterhin exakt auf die gleiche Weise nach links oder rechts!

## Anwendungen in der Praxis

- **Datenbank-Indizierung:** B-Trees (eine verallgemeinerte Version von BSTs) sind die grundlegende Datenstruktur, die von SQL-Datenbanken (wie MySQL und PostgreSQL) verwendet wird, um `SELECT * WHERE id = 5` in Mikrosekunden auszuführen, anstatt die gesamte Datenbank zu durchsuchen.

## Verwandte Algorithmen in cOde(n)

- **[tree_08 - BST Insert](tree_08_bst-insert.md)** — Der Schwester-Algorithmus. Wenn eine Suche fehlschlägt und `None` erreicht, ist genau dieser `None`-Punkt mathematisch exakt die Stelle, an der man das Ziel einfügen würde, um den BST aufrechtzuerhalten!
- **[search_02 - Binary Search](../searching/search_02_binary-search.md)** — Das Array-basierte Äquivalent dieser exakten Logik.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*