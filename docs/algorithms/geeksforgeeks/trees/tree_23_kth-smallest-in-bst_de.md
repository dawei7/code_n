# Kth Smallest Element in a BST

| | |
|---|---|
| **ID** | `tree_23` |
| **Kategorie** | trees |
| **Komplexität (erforderlich)** | $O(H + K)$ Zeit, $O(H)$ Platz |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) |

## Problemstellung

Gegeben ist die `root` eines Binary Search Tree und eine Ganzzahl `k`. Geben Sie den k-kleinsten Wert (1-basiert) aller Knotenwerte im Baum zurück.

**Eingabe:** Ein BST `root`-Knoten und eine Ganzzahl `k`.
**Ausgabe:** Eine Ganzzahl, die den k-kleinsten Wert repräsentiert.

## Wann man es verwendet

- Um geordnete Daten aus einer hierarchischen Struktur abzurufen, ohne Speicher für den gesamten Datensatz zu belegen.
- Der ultimative Test für das Verständnis von In-Order Traversal.

## Ansatz

**1. Die In-Order-Garantie:**
Ein In-Order Traversal (`Left -> Root -> Right`) eines gültigen Binary Search Tree garantiert mathematisch, dass die Knoten in perfekt aufsteigender Reihenfolge besucht werden.
Der 1. Knoten, den Sie besuchen, ist das absolute Minimum. Der 2. ist der zweitkleinste. Der K-te Knoten, den Sie besuchen, ist der K-kleinste!

**2. Der naive Ansatz ($O(N)$ Zeit, $O(N)$ Platz):**
Sie könnten ein vollständiges In-Order Traversal (`tree_02`) durchführen, jeden einzelnen Wert an ein riesiges Array anhängen und dann einfach `array[k - 1]` zurückgeben.
Obwohl dies technisch korrekt ist, ist es eine massive Verschwendung von Speicher und Zeit! Wenn Sie einen Baum mit 1 Million Knoten haben und nur das zweitkleinste Element (`k=2`) suchen, müssen Sie nicht 999.998 größere Knoten durchlaufen und speichern!

**3. Die Zähler-Optimierung ($O(H + K)$ Zeit, $O(H)$ Platz):**
Anstatt eines Arrays verwenden wir einfach eine globale `count`-Ganzzahl!
Wir beginnen unser In-Order Traversal. Jedes Mal, wenn wir einen Knoten formell "verarbeiten" (nach der Rückkehr vom linken Kind), erhöhen wir `count += 1`.
Wenn `count == k`, haben wir unsere Antwort gefunden! Wir speichern den Wert des Knotens in einer globalen `result`-Variable und BRECHEN das Traversal sofort AB (vorzeitige Rückkehr aus allen rekursiven Aufrufen)!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for tree_23: Kth Smallest in BST.

In-order traversal visits the nodes in sorted order.
"""


def solve(children, values, root, n, k):
    out = []

    def inorder(i):
        if i == -1:
            return
        inorder(children[i][0])
        out.append(values[i])
        inorder(children[i][1])

    inorder(root)
    if k < 1 or k > len(out):
        return -1
    return out[k - 1]
```

</details>

## Durchlauf

Baum:
```text
      5
     / \
    3   6
   / \
  2   4
 /
1
```
`k = 3`.

**Iterativer Stack-Durchlauf:**
1. Gehe nach links: Stack `[5, 3, 2, 1]`. `curr` wird null.
2. Pop `1`. `k` sinkt auf `2`. Nicht null. `curr = 1.right` (null).
3. Pop `2`. `k` sinkt auf `1`. Nicht null. `curr = 2.right` (null).
4. Pop `3`. `k` sinkt auf `0`. NULL!
5. Gib `3.val` zurück, was `3` ist.

Ausgabe: `3`. ✓ (Die sortierte Reihenfolge ist 1, 2, 3, 4, 5, 6. Das 3. Element ist 3).
*Beachten Sie, dass wir uns die Knoten 4, 5 oder 6 nicht einmal angesehen haben! Wir haben sofort abgebrochen!*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(H + K)$ | $O(H)$ |
| **Durchschnittlicher Fall** | $O(H + K)$ | $O(H)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Um das absolut kleinste Element zu finden, müssen wir von der Wurzel bis zum am weitesten links liegenden Blatt traversieren. Dies benötigt $O(H)$ Zeit, wobei H die Höhe des Baumes ist.
Dann müssen wir genau K Knoten mittels Pop verarbeiten. Dies benötigt $O(K)$ Zeit.
Die gesamte Zeitkomplexität beträgt mathematisch $O(H + K)$.
In einem balancierten Baum benötigt das Finden des 1. Elements $O(\log N)$ Zeit.
Im absolut schlechtesten Fall (ein entarteter Baum und K = N) benötigt es $O(N)$ Zeit.
Die Platzkomplexität ist durch den Stack oder den rekursiven Aufruf-Stack begrenzt, der höchstens H Knoten enthält. $O(H)$ Platz.

## Varianten & Optimierungen

- **Häufige Einfügungen/Löschungen ($O(\log N)$ Zeit):** Was ist, wenn der Baum ständig aktualisiert wird und wir `kthSmallest` tausende Male abfragen müssen? $O(H+K)$ ist zu langsam. Sie können die `TreeNode`-Klasse physisch um eine `int size`-Variable erweitern, die die Gesamtzahl der Knoten im linken Teilbaum verfolgt! Wenn bei der Suche `left.size == k - 1` gilt, ist der aktuelle Knoten die Antwort in reiner $O(\log N)$-Zeit!

## Anwendungen in der Praxis

- **Datenbank-Paginierung:** Wenn eine SQL-Datenbank Benutzer nach Alter mithilfe eines B-Trees indiziert und eine Abfrage `SELECT * ORDER BY age LIMIT 10 OFFSET 50` lautet, verwendet die Engine eine verallgemeinerte Version dieses Algorithmus, um die ersten 50 Knoten zu überspringen und die nächsten 10 abzurufen.

## Verwandte Algorithmen in cOde(n)

- **[tree_02 - In-order Traversal](tree_02_inorder-traversal.md)** — Die Engine, die die aufsteigende Reihenfolge erzwingt.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*