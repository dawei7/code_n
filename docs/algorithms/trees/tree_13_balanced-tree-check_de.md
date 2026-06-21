# Balanced Binary Tree Check

| | |
|---|---|
| **ID** | `tree_13` |
| **Category** | trees |
| **Complexity (required)** | $O(N)$ Time, $O(H)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 7/10 |
| **LeetCode Equivalent** | [Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/) |

## Problem statement

*(Hinweis: Dies ist eine Duplikat-Datei für die Logik des Balanced Binary Tree, ursprünglich identisch mit `tree_11`)*

Gegeben sei ein Binary Tree; bestimmen Sie, ob dieser **höhenbalanciert** ist.
Ein höhenbalancierter Binary Tree ist als ein Binary Tree definiert, bei dem sich die Höhen der linken und rechten Teilbäume jedes Knotens um nicht mehr als 1 unterscheiden.

**Input:** Ein `root`-Knoten eines Binary Tree.
**Output:** Ein Boolean, der angibt, ob der Baum balanciert ist.

## Wann man es verwendet

- Um zu verifizieren, dass ein benutzerdefinierter Algorithmus zum Einfügen in einen Baum (wie AVL- oder Red-Black-Logik) seine Invarianten korrekt einhält.
- Eine klassische Interview-Frage, um die Effizienz von Top-Down- gegenüber Bottom-Up-DFS zu testen.

## Ansatz

**1. Der naive Top-Down-Ansatz ($O(N^2)$):**
Die mathematische Definition erfordert die Überprüfung der Höhe des linken und rechten Teilbaums. Wir haben bereits eine `height()`-Funktion (`tree_04`).
Wir könnten eine Funktion schreiben, die `height(root.left)` und `height(root.right)` berechnet. Wenn sie sich um mehr als 1 unterscheiden, geben wir `False` zurück.
Anschließend rufen wir die Funktion rekursiv für `root.left` und `root.right` auf, um *deren* Teilbäume zu verifizieren.
**Der Fehler:** Die Berechnung der Höhe benötigt $O(N)$ Zeit. Wir führen eine $O(N)$-Berechnung rekursiv N-mal aus! Das ergibt eine Zeitkomplexität von $O(N^2)$!

**2. Die Bottom-Up-DFS-Optimierung ($O(N)$):**
Beachten Sie, dass der Computer ohnehin bis ganz nach unten in den Baum vordringen MUSS, um die Höhe eines Knotens zu berechnen!
Anstatt eine separate `isBalanced()`-Funktion und eine `height()`-Funktion auszuführen, was wäre, wenn wir sie kombinieren?
Wir führen eine Post-Order-DFS durch, um die Höhe von unten nach oben zu berechnen.
Wenn ein linkes Kind seine Höhe zurückgibt (z. B. `2`) und ein rechtes Kind seine Höhe zurückgibt (z. B. `4`), weiß der Elternknoten sofort: "Moment! 4 - 2 = 2. Meine Teilbäume sind nicht balanciert!"
Anstatt seine eigene Höhe an den darüber liegenden Elternknoten zurückzugeben, gibt er ein spezielles Flag zurück: `-1`!

**3. Das ansteckende Versagen:**
Wenn ein Knoten eine `-1` von einem seiner Kinder erhält, bedeutet dies, dass der Baum die Balance-Prüfung in der Tiefe nicht bestanden hat. Er stoppt sofort die Berechnung und gibt einfach `-1` nach oben weiter. Die `-1` propagiert bis zur Wurzel!
Wenn der finale Aufruf an der Wurzel `-1` zurückgibt, ist der Baum nicht balanciert. Wenn er eine normale positive Ganzzahl (die Höhe) zurückgibt, ist der Baum balanciert!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for tree_13: Balanced Tree Check.

Return True iff the binary tree is height-balanced:
"""


def solve(children, root, n):
    """Return True iff the binary tree is height-balanced."""
    balanced = [True]

    def height(u):
        if u == -1:
            return 0
        l = height(children[u][0])
        r = height(children[u][1])
        if abs(l - r) > 1:
            balanced[0] = False
        return 1 + max(l, r)

    height(root)
    return balanced[0]
```

</details>

## Walk-through

Baum:
```text
      1
     / \
    2   2
   / \
  3   3
 / \
4   4
```

1. **DFS erreicht Knoten `3` (den auf der linken Seite):**
   - Er prüft sein linkes Kind `4`. Es ist ein Blatt. Das linke Kind gibt `1` zurück.
   - Er prüft sein rechtes Kind `4`. Es ist ein Blatt. Das rechte Kind gibt `1` zurück.
   - Die Differenz ist 1 - 1 = 0. Balanciert.
   - Knoten `3` gibt seine Höhe zurück: 1 + \max(1, 1) = 2.
2. **DFS evaluiert Knoten `2` (den auf der linken Seite):**
   - Das linke Kind `3` gab die Höhe `2` zurück.
   - Das rechte Kind `3` (das Blatt) gibt die Höhe `1` zurück.
   - Die Differenz ist 2 - 1 = 1. Balanciert!
   - Knoten `2` gibt seine Höhe zurück: 1 + \max(2, 1) = 3.
3. **DFS evaluiert Knoten `1` (Wurzel):**
   - Das linke Kind `2` gab die Höhe `3` zurück.
   - Das rechte Kind `2` (das Blatt ganz rechts) gibt die Höhe `1` zurück.
   - Die Differenz ist 3 - 1 = 2.
   - 2 > 1! Nicht balanciert!
   - Die Wurzel gibt `-1` zurück.
4. Die Hauptfunktion prüft `check_height(root) != -1`. `-1 != -1` ist False.
Gibt `False` zurück. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Die DFS-Traversierung besucht jeden einzelnen Knoten genau einmal. Sobald eine Verletzung gefunden wird, bricht sie die weitere tiefe Rekursion sofort ab (obwohl sie immer noch nach oben durchgereicht wird).
Die Zeitkomplexität ist strikt $O(N)$.
Die Platzkomplexität ist durch den rekursiven Call Stack begrenzt, welcher der Höhe des Baumes $O(H)$ entspricht. Im Durchschnitts-/Bestfall (balancierter Baum) ist der Platzbedarf $O(\log N)$. Im schlechtesten Fall (einseitig ausgeprägter Baum) verschlechtert er sich auf $O(N)$.

## Varianten & Optimierungen

- **Top-Down-Cache:** Wenn Sie aus architektonischen Gründen den $O(N^2)$ Top-Down-Ansatz verwenden müssen (z. B. bei Verwendung einer externen API zum Abrufen der Höhe), können Sie eine Hash Map verwenden, um die Höhe jedes Knotens zu memoize-en, wodurch die Zeitkomplexität künstlich wieder auf $O(N)$ gesenkt wird.

## Anwendungen in der Praxis

- **AVL-Bäume / Red-Black-Trees:** Diese Prüfung ist grundlegend in die Einfüge- und Löschoperationen von selbstbalancierenden Binary Search Trees eingebettet. Wenn die Teilbäume die Regel `abs(left - right) <= 1` verletzen, wird sofort eine physische Baumrotation ausgelöst.

## Verwandte Algorithmen in cOde(n)

- **[tree_04 - Tree Height](tree_04_tree-height.md)** — Die grundlegende rekursive Funktion, die diesen gesamten Algorithmus antreibt.
- **[tree_22 - AVL Insert](tree_22_avl-insert-simplified.md)** — Wie man den Baum physisch repariert, wenn diese Funktion `False` zurückgibt!

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Wettbewerbs-Programmier-Referenzseiten verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*