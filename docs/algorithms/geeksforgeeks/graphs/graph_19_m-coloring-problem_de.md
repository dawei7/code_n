# M-Coloring Problem

| | |
|---|---|
| **ID** | `graph_19` |
| **Kategorie** | graphs |
| **Komplexität (erforderlich)** | $O(M^V)$ Zeit, $O(V)$ Platz |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **GeeksForGeeks Äquivalent** | [m Coloring Problem](https://www.geeksforgeeks.org/m-coloring-problem/) |

## Problemstellung

Gegeben ist ein ungerichteter Graph und eine Ganzzahl `M`. Bestimmen Sie, ob es möglich ist, jeden Knoten mit maximal `M` verschiedenen Farben zu färben, sodass keine zwei benachbarten Knoten dieselbe Farbe haben.

**Eingabe:** Anzahl der Knoten `V`, eine Adjazenzliste `adj` (oder Matrix) und eine Ganzzahl `M`.
**Ausgabe:** Ein boolescher Wert. `True`, falls eine gültige Färbung existiert, andernfalls `False`.

## Wann ist es anzuwenden?

- Wenn M = 2, handelt es sich lediglich um den $O(V+E)$ Bipartite Graph Check (`graph_12`).
- Wenn M \ge 3, wird das Problem **NP-vollständig**. Es gibt keinen Algorithmus mit polynomieller Laufzeit. Sie MÜSSEN Backtracking verwenden.
- Wenn Sie Einschränkungen bei der Zeitplanung oder Kartenfärbung lösen müssen.

## Ansatz

**1. Der Backtracking-Zustandsraum-Baum:**
Da es keinen effizienten Graphenalgorithmus zur Lösung dieses Problems gibt, müssen wir es mittels Backtracking (`backtracking_01`) durch Brute-Force-Suche lösen.
Unser Zustand ist einfach ein `colors[]`-Array, das die Farbzuweisung (von 1 bis M) für jeden Knoten von `0` bis `V-1` verfolgt.

**2. Der rekursive Schritt:**
Beginnen Sie bei Knoten `0`.
Versuchen Sie, die Farbe `1` zuzuweisen. Ist dies sicher? (Überprüfen Sie alle Nachbarn von Knoten `0`. Hat irgendein Nachbar aktuell die Farbe `1`? Falls nicht, ist es sicher!).
Wenn es sicher ist, weisen Sie temporär `colors[0] = 1` zu und gehen Sie rekursiv zum Knoten `1` über!
Wenn Knoten `1` erfolgreich eine gültige Farbe findet, fahren Sie fort!
Wenn wir jemals einen Knoten erreichen, bei dem KEINE der `M` Farben sicher ist, gibt die Rekursion `False` zurück.
Dies löst ein Backtracking aus! Der vorherige Knoten macht seine Farbzuweisung `colors[i] = 0` rückgängig und versucht die nächste Farbe in der Schleife.

**3. Terminierung:**
Wenn unsere rekursive Funktion erfolgreich Knoten `V` erreicht (was bedeutet, dass sie erfolgreich eine Farbe für `V-1` zugewiesen hat), haben wir eine gültige globale Färbung gefunden! Geben Sie `True` zurück.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for graph_19: M-Coloring Problem.

Return True iff the graph can be colored with m colors
such that no two adjacent vertices share a color.

Backtracking: assign colors to vertices one at a time.
At each step, try each color; if it doesn't conflict with
any already-colored neighbor, recurse.
"""


def solve(n, edges, m):
    if n == 0:
        return True
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    color = [-1] * n

    def safe(v, c):
        for u in adj[v]:
            if color[u] == c:
                return False
        return True

    def helper(v):
        if v == n:
            return True
        for c in range(m):
            if safe(v, c):
                color[v] = c
                if helper(v + 1):
                    return True
                color[v] = -1
        return False

    return helper(0)
```

</details>

## Durchlauf

`V = 4`. `M = 3`. Der Graph ist ein vollständiger Graph K_4 (jeder Knoten ist mit jedem anderen Knoten verbunden).
`adj = {0:[1,2,3], 1:[0,2,3], 2:[0,1,3], 3:[0,1,2]}`.

1. `curr = 0`:
   - Versuche Farbe 1. Sicher. `colors[0] = 1`. Rekursion.
2. `curr = 1`:
   - Versuche Farbe 1. Unsicher (Nachbar 0 hat Farbe 1).
   - Versuche Farbe 2. Sicher. `colors[1] = 2`. Rekursion.
3. `curr = 2`:
   - Versuche Farbe 1. Unsicher.
   - Versuche Farbe 2. Unsicher.
   - Versuche Farbe 3. Sicher. `colors[2] = 3`. Rekursion.
4. `curr = 3`:
   - Versuche Farbe 1. Unsicher.
   - Versuche Farbe 2. Unsicher.
   - Versuche Farbe 3. Unsicher.
   - Schleife endet. Gibt `False` zurück.
5. Backtrack zu `curr=2`.
   - `colors[2] = 0`. Keine weiteren Farben zum Ausprobieren. Gibt `False` zurück.
6. Backtrack zu `curr=1`.
   - `colors[1] = 0`. Versuche Farbe 3. Sicher. `colors[1] = 3`. Rekursion.
7. `curr = 2`:
   - Versuche Farbe 1. Unsicher.
   - Versuche Farbe 2. Sicher! `colors[2] = 2`. Rekursion.
8. `curr = 3`:
   - Versuche Farbe 1, 2, 3... alle unsicher! Gibt `False` zurück.
9. Der gesamte Baum evaluiert schließlich zu `False`. Ein vollständiger Graph mit 4 Knoten erfordert exakt 4 Farben.

Ergebnis `False`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(V)$ | $O(V)$ |
| **Durchschnittlicher Fall** | $O(M^V)$ | $O(V)$ |
| **Schlechtester Fall** | $O(M^V)$ | $O(V)$ |

An jedem der V Knoten durchlaufen wir M mögliche Farbwahlen. Dies erzeugt einen M-ären Baum der Tiefe V.
Die Gesamtzahl der theoretischen Knoten im Zustandsraum-Baum ist M^V.
An jedem Knoten benötigt `is_safe` $O(V)$ Zeit. Daher ist die Zeitkomplexität im schlechtesten Fall strikt durch $O(V \cdot M^V)$ begrenzt.
Die Platzkomplexität beträgt strikt $O(V)$ für das `colors`-Array und die Tiefe des Rekursions-Stacks.

## Varianten & Optimierungen

- **Grad-Sortierung (Heuristische Optimierung):** Anstatt die Knoten in numerischer Reihenfolge `0, 1, 2...` zu verarbeiten, sortieren Sie die Knoten nach ihrem Grad (Anzahl der Kanten) in absteigender Reihenfolge! Das Färben der am stärksten eingeschränkten (verbundenen) Knoten zuerst beschneidet den Backtracking-Baum frühzeitig drastisch und verbessert die durchschnittliche Laufzeit erheblich.
- **Vier-Farben-Satz:** In planaren Graphen (Graphen, die ohne sich kreuzende Kanten auf Papier gezeichnet werden können, wie eine physische Landkarte) sind M=4 mathematisch IMMER ausreichend, um den Graphen zu färben! Dies war der erste bedeutende mathematische Satz, der von einem Computer bewiesen wurde.

## Anwendungen in der Praxis

- **Sudoku-Solver:** Ein Sudoku-Spielfeld ist lediglich ein Graph mit 81 Knoten, bei dem M=9 gilt. Kanten existieren zwischen zwei beliebigen Zellen in derselben Zeile, Spalte oder 3x3-Box. Derselbe Backtracking-Code löst Sudokus!
- **Stundenplanung an Universitäten:** Knoten sind Prüfungen. Kanten existieren zwischen zwei Prüfungen, wenn ein Student für beide eingeschrieben ist. M ist die Anzahl der verfügbaren Zeitfenster. Wenn der Graph M-färbbar ist, existiert ein konfliktfreier Zeitplan!

## Verwandte Algorithmen in cOde(n)

- **[graph_12 - Bipartite Check](graph_12_bipartite-check.md)** — Der Spezialfall M=2, der mittels BFS linear lösbar ist.
- **[backtracking_01 - Subset Sum Decision](../backtracking/backtrack_01_subset-sum-decision.md)** — Das grundlegende Muster für alle NP-vollständigen Algorithmen zur erschöpfenden Suche.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Seiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*