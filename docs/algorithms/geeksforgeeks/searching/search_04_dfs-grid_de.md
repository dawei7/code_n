# Tiefensuche (DFS) auf einem Gitter

| | |
|---|---|
| **ID** | `search_04` |
| **Kategorie** | searching |
| **Komplexität (erforderlich)** | $O(R \times C)$ Zeit, $O(R \times C)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 10/10 |
| **LeetCode-Äquivalent** | [Number of Islands](https://leetcode.com/problems/number-of-islands/) |

## Problemstellung

Gegeben ist ein $R \times C$ 2D-Gitter, das eine Karte aus `'1'` (Land) und `'0'` (Wasser) darstellt.
Geben Sie die Anzahl der Inseln zurück.
Eine Insel ist von Wasser umgeben und wird durch die Verbindung benachbarter Landflächen horizontal oder vertikal gebildet.

**Eingabe:** Ein 2D-Array `grid`.
**Ausgabe:** Eine Ganzzahl, die die Anzahl der Inseln repräsentiert.

## Wann man es verwendet

- Um Zusammenhangskomponenten in einer Matrix zu finden (z. B. das Finden der Begrenzung eines Objekts).
- Wenn Sie alle möglichen Pfade erschöpfend durchsuchen müssen (Backtracking), anstatt den kürzesten Pfad zu finden (BFS).
- Das am häufigsten abgefragte Algorithmenmuster in Software-Engineering-Interviews.

## Ansatz

**1. Die "Labyrinth-Läufer"-Strategie:**
Im Gegensatz zu BFS, das alles gleichmäßig wie eine Welle erkundet, läuft DFS durch ein Labyrinth, indem man die rechte Hand strikt an der Wand hält.
Sie gehen so tief wie physikalisch möglich einen einzelnen Pfad entlang. Sie kehren erst um (Backtracking), wenn Sie in eine Sackgasse geraten (Wasser, eine Wand oder außerhalb der Grenzen).
Wenn Sie eine Sackgasse erreichen, gehen Sie einen Schritt zurück und versuchen die nächste verfügbare Richtung.

**2. Der Call Stack (LIFO):**
BFS verwendet eine explizite Queue. DFS verwendet inhärent den Call Stack des Systems.
Wenn wir `dfs(r, c)` aufrufen, ruft die Funktion sofort `dfs(r+1, c)` auf. Die ursprüngliche Funktion pausiert und WARTET darauf, dass die Unterfunktion die Erkundung des gesamten Pfades nach unten vollständig abschließt, bevor sie überhaupt in Betracht zieht, `dfs(r-1, c)` zu prüfen.

**3. Zustandsverfolgung (Die Insel versenken):**
Genau wie bei BFS werden wir unendlich zwischen zwei benachbarten Landzellen hin- und herspringen, wenn wir besuchte Zellen nicht verfolgen.
Anstatt ein separates `visited`-Set zu verwenden, ist eine brillante Optimierung für dieses spezifische Problem, das Gitter direkt zu modifizieren (in-place)! Wenn wir eine Landzelle `'1'` besuchen, verwandeln wir sie sofort in Wasser `'0'` (wir versenken die Insel). Dies verhindert physikalisch, dass wir sie jemals erneut besuchen.

**4. Die Hauptschleife:**
Wir iterieren mit einer verschachtelten Doppelschleife durch jede einzelne Zelle im Gitter.
Wenn wir Wasser `'0'` finden, ignorieren wir es.
Wenn wir Land `'1'` finden, MUSS es eine brandneue, unentdeckte Insel sein! Wir erhöhen unseren `island_count` und starten dann den `dfs()`-Torpedo, um rekursiv jedes einzelne Stück verbundenen Landes zu versenken.
Wenn das `dfs()` endet, wurde die gesamte Insel gelöscht, wodurch sichergestellt wird, dass wir sie niemals doppelt zählen.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for search_04: DFS on a 2D grid.

Explore reachable cells depth-first using a LIFO stack.
O(n^2) for an n x n grid.

The engine no longer ships a TrackedStack - the player
brings their own (a plain list with .append() / .pop()
gives the standard LIFO semantics; a plain list is fine
here because the engine doesn't count plain-list ops
and the budget is enforced by the grid reads / writes).
"""


def solve(grid, start, size):
    visited = set()
    stack = [start]
    while stack:
        row, col = stack.pop()
        if (row, col) in visited:
            continue
        visited.add((row, col))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < size and 0 <= nc < size and (nr, nc) not in visited and grid[nr][nc] == 0:
                stack.append((nr, nc))
    return len(visited)
```

</details>

## Durchlauf

Gitter:
`1 1 0`
`1 0 0`
`0 0 1`
`island_count = 0`.

1. `r=0, c=0`: `grid[0][0] == '1'`.
   - `island_count = 1`.
   - Aufruf `dfs(0, 0)`.
2. **Innerhalb von `dfs(0, 0)`**:
   - `grid[0][0] = '0'`.
   - Aufruf `dfs(1, 0)` (unten).
3. **Innerhalb von `dfs(1, 0)`**:
   - `grid[1][0] = '0'`.
   - Aufruf `dfs(2, 0)` (unten) -> Induktionsanfang (Basis) (`grid[2][0] == '0'`). Kehrt zurück.
   - Aufruf `dfs(0, 0)` (oben) -> Induktionsanfang (Basis) (ist bereits `0`!). Kehrt zurück.
   - Aufruf `dfs(1, 1)` (rechts) -> Induktionsanfang (Basis) (`0`). Kehrt zurück.
   - Aufruf `dfs(1, -1)` (links) -> Induktionsanfang (Basis) (außerhalb der Grenzen). Kehrt zurück.
   - `dfs(1, 0)` beendet!
4. **Zurück in `dfs(0, 0)`**:
   - Aufruf `dfs(-1, 0)` (oben) -> Außerhalb der Grenzen.
   - Aufruf `dfs(0, 1)` (rechts) -> Es ist `'1'`!
5. **Innerhalb von `dfs(0, 1)`**:
   - `grid[0][1] = '0'`.
   - Ruft unten, oben, rechts, links auf -> Alle treffen auf Induktionsanfänge (Basisfälle).
   - `dfs(0, 1)` beendet!
6. **Zurück in `dfs(0, 0)`**:
   - Aufruf `dfs(0, -1)` (links) -> Außerhalb der Grenzen.
   - `dfs(0, 0)` beendet! Die Insel oben links ist vollständig gelöscht.

Gitter ist jetzt:
`0 0 0`
`0 0 0`
`0 0 1`

7. Die Schleife läuft weiter bis `r=2, c=2`.
   - `grid[2][2] == '1'`.
   - `island_count = 2`.
   - `dfs(2, 2)` versenkt die Insel unten rechts.

Ergebnis: `2`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(R \times C)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(R \times C)$ | $O(R \times C)$ |
| **Schlechtester Fall** | $O(R \times C)$ | $O(R \times C)$ |

Die verschachtelte `for`-Schleife prüft alle $R \times C$ Zellen. Die `dfs`-Funktion besucht jedes Stück Land genau einmal (und prüft seine Nachbarn). Daher wird jede Zelle eine konstante Anzahl von Malen verarbeitet. Die Zeitkomplexität ist exakt $O(R \times C)$.
Die Platzkomplexität hängt vom Call Stack der Rekursion ab. Im schlimmsten Fall (das gesamte Gitter ist eine riesige, schlangenförmige Insel) geht die DFS $R \times C$ Ebenen tief in die Rekursion, bevor sie sich wieder auflöst. Die Platzkomplexität ist $O(R \times C)$.
*(Wenn das Gitter vollständig aus Wasser besteht, wird DFS nie aufgerufen, was zu $O(1)$ Platz führt).*

## Varianten & Optimierungen

- **Word Search (`backtracking_04`):** Wenn Sie nach einer bestimmten Zeichenfolge suchen, verwenden Sie DFS. Aber entscheidend ist, dass Sie die Insel wieder "ent-versenken" müssen (Backtracking: `grid[r][c] = original_char`), nachdem Sie sie erkundet haben, da ein anderer Wortpfad später möglicherweise denselben Buchstaben kreuzen muss!
- **Union-Find (`graph_09`):** "Number of Islands" kann auch iterativ in $O(R \times C \cdot \alpha(N))$ Zeit mit einer Disjoint-Set-Struktur gelöst werden, die benachbarte `'1'`-Werte zu Graphkomponenten verbindet und die Gesamtzahl der unterschiedlichen Wurzeln zählt.

## Anwendungen in der Praxis

- **Minesweeper:** Wenn Sie auf eine Zelle mit "0" benachbarten Minen klicken, führt das Spiel automatisch DFS/BFS aus, um sofort alle verbundenen "0"-Zellen zu erweitern und freizulegen.

## Verwandte Algorithmen in cOde(n)

- **[search_03 - BFS on a Grid](search_03_bfs-grid.md)** — Der iterative, Queue-basierte Schwesteralgorithmus, der zum Finden kürzester Pfade verwendet wird.
- **[graphs_01 - DFS](../graphs/graph_01_dfs.md)** — Die exakt gleiche Logik, angewendet auf verallgemeinerte Knoten und Kanten anstelle einer 2D-Matrix.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*