# Durchmesser eines Binärbaums

| | |
|---|---|
| **ID** | `tree_07` |
| **Kategorie** | Bäume |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(H)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/) |

## Problemstellung

Gegeben ist der `root` eines Binärbaums. Geben Sie die Länge des **Durchmessers** des Baums zurück.
Der Durchmesser eines Binärbaums ist die Länge des längsten Pfades zwischen zwei beliebigen Knoten in einem Baum. Dieser Pfad kann durch den `root` verlaufen, muss es aber nicht.
Die Länge eines Pfades zwischen zwei Knoten wird durch die Anzahl der Kanten zwischen ihnen definiert.

**Eingabe:** Ein `root`-Knoten eines Binärbaums.
**Ausgabe:** Eine Ganzzahl, die den Durchmesser repräsentiert.

## Wann man es verwendet

- Ein klassischer Test für eine Bottom-Up Post-Order DFS-Traversierung.
- Es testet die Fähigkeit, eine globale Zustandsvariable zu verwalten und gleichzeitig einen anderen Wert im rekursiven Aufruf-Stack zurückzugeben.

## Ansatz

**1. Die "Bogen"-Analogie:**
Stellen Sie sich vor, Sie heben den Baum an seiner Wurzel an. Der längste Pfad zwischen zwei beliebigen Knoten sieht aus wie ein riesiger Bogen, der von einem Blatt ausgeht, NACH OBEN zu einem Verbindungsknoten führt und dann NACH UNTEN zu einem anderen Blatt verläuft.
Was ist für einen beliebigen Knoten im Baum der längste Pfad, der direkt als "Bogen" durch ihn hindurchführt?
Mathematisch MUSS er lauten: `(Längster Pfad nach unten in seinem linken Teilbaum) + (Längster Pfad nach unten in seinem rechten Teilbaum)`.

**2. Die Bottom-Up-Berechnung:**
Um den globalen Durchmesser zu finden, müssen wir diesen "Bogen"-Wert für JEDEN EINZELNEN KNOTEN im Baum berechnen und das absolute Maximum, das wir jemals sehen, festhalten!
Woher wissen wir, welches der längste Pfad nach unten in einem Teilbaum ist? Das ist einfach die **Höhe (`tree_04`)** des Teilbaums!
Wenn wir also die Höhe des Baums mittels Post-Order DFS berechnen, haben wir an jedem einzelnen Knoten auf magische Weise die Höhe seines linken Kindes `L` und die Höhe seines rechten Kindes `R`.
Die Bogengröße durch diesen Knoten ist `L + R`.
Wir aktualisieren einfach eine globale `max_diameter`-Variable, falls `L + R` größer ist!

**3. Die duale Rekursion:**
Die rekursive Funktion erfüllt gleichzeitig ZWEI verschiedene Zwecke:
1. **An den Elternknoten:** Sie gibt ihre eigene Höhe zurück (`1 + max(L, R)`).
2. **An die globale Variable:** Sie berechnet und aktualisiert den Durchmesser-Bogen (`L + R`).

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for tree_07: Tree Diameter.

For each node, the longest path through it is the sum of the two
tallest subtree depths. The diameter is the max of that sum.
"""


def solve(children, root, n):
    if n == 0:
        return 0
    best = 0

    def depth(u):
        nonlocal best
        if not children[u]:
            return 0
        top_two = [0, 0]
        for v in children[u]:
            d = depth(v)
            if d >= top_two[0]:
                top_two = [d, top_two[0]]
            elif d > top_two[1]:
                top_two[1] = d
        through = top_two[0] + top_two[1]
        if through > best:
            best = through
        return 1 + top_two[0]

    depth(root)
    return best
```

</details>

## Durchlauf

Baum:
```text
      1
     / \
    2   3
   / \
  4   5
```

1. **`height(4)`:**
   - Links ist null -> 0. Rechts ist null -> 0.
   - Lokaler Durchmesser: 0 + 0 = 0. `max_diameter = max(0, 0) = 0`.
   - Gibt Höhe zurück: 1 + \max(0, 0) = 1.
2. **`height(5)`:**
   - Links null -> 0. Rechts null -> 0.
   - Lokaler Durchmesser: 0 + 0 = 0. `max_diameter = 0`.
   - Gibt Höhe zurück: 1.
3. **`height(2)`:**
   - Links gab 1 zurück. Rechts gab 1 zurück.
   - Lokaler Durchmesser: 1 + 1 = 2. `max_diameter = max(0, 2) = 2`.
   - Gibt Höhe zurück: 1 + \max(1, 1) = 2.
4. **`height(3)`:**
   - Links null -> 0. Rechts null -> 0.
   - Lokaler Durchmesser: 0. `max_diameter = 2`.
   - Gibt Höhe zurück: 1.
5. **`height(1)` (Wurzel):**
   - Links (von 2) gab 2 zurück. Rechts (von 3) gab 1 zurück.
   - Lokaler Durchmesser: 2 + 1 = 3. `max_diameter = max(2, 3) = 3`.
   - Gibt Höhe zurück: 1 + \max(2, 1) = 3.

Rekursion endet. Rückgabe `max_diameter = 3`. ✓
(Der Pfad ist `4 -> 2 -> 1 -> 3`, welcher 3 Kanten hat).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Die DFS-Traversierung besucht jeden einzelnen Knoten genau einmal. An jedem Knoten werden $O(1)$ konstante Additionen und `max()`-Operationen durchgeführt.
Die Zeitkomplexität ist exakt $O(N)$.
Die Platzkomplexität ist durch den rekursiven Aufruf-Stack begrenzt, welcher der Höhe des Baums $O(H)$ entspricht. Im besten/durchschnittlichen Fall (ausgeglichener Baum) ist der Platzbedarf $O(\log N)$. Im schlechtesten Fall (einseitig ausgeprägter Baum) verschlechtert er sich auf $O(N)$.

## Varianten & Optimierungen

- **Binary Tree Maximum Path Sum (`tree_10`):** Der exakt gleiche architektonische Ansatz! Aber anstatt Kanten zu zählen (`left_height + right_height`), summieren Sie die Werte der Knoten (`node.val + max_left_sum + max_right_sum`), mit einer zusätzlichen Prüfung, um negative Pfade zu ignorieren.

## Anwendungen in der Praxis

- **Netzwerk-Routing:** Finden des absolut längsten physischen Übertragungspfades (Latenz-Flaschenhals) innerhalb einer baumbasierten Netzwerktopologie, um Paket-Timeouts zu bestimmen.

## Verwandte Algorithmen in cOde(n)

- **[tree_04 - Tree Height](tree_04_tree-height.md)** — Die grundlegende rekursive Funktion, die diesen gesamten Algorithmus antreibt.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Wettbewerbsprogrammierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*