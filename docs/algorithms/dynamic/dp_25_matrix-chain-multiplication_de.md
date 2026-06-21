# Matrix Chain Multiplication (Top-Down Memoization)

| | |
|---|---|
| **ID** | `dp_25` |
| **Kategorie** | dynamic_programming |
| **Komplexität (erforderlich)** | $O(n^3)$ |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [Burst Balloons (konzeptionell ähnlich)](https://leetcode.com/problems/burst-balloons/) |

## Problemstellung

*(Dies ist die Top-Down-rekursive Variante von `dp_13_matrix-chain-multiplication`)*.

Gegeben ist eine Sequenz von `n` Matrizen. Finde die minimale Anzahl an skalaren Multiplikationen, die erforderlich sind, um alle Matrizen miteinander zu multiplizieren. Die Reihenfolge der Multiplikation bestimmt die Kosten.

**Eingabe:** Ein Array `p[]`, wobei die Matrix A_i die Dimensionen `p[i-1] x p[i]` hat.
**Ausgabe:** Eine Ganzzahl, die die minimalen Kosten repräsentiert.

## Wann man es verwendet

- Der Bottom-Up-Ansatz (`dp_13`) erfordert komplexe Schleifen über die Kettenlängen `L`. Viele Ingenieure empfinden den Top-Down-rekursiven Ansatz als deutlich intuitiver, um ihn während eines Whiteboard-Interviews zu implementieren.
- Er demonstriert perfekt das Konzept der **Memoization**.

## Ansatz

Wir definieren eine rekursive Funktion `solve(i, j)`, die die minimalen Kosten für die Multiplikation der Teilkette von Matrix A_i bis Matrix A_j zurückgibt.

**Induktionsanfang (Basis):**
Wenn `i == j`, gibt es nur eine Matrix! Die Kosten für die Multiplikation einer einzelnen Matrix sind `0`.

**Rekursionsschritt:**
Wenn `i < j`, versuchen wir, an jedem möglichen Teilungspunkt `k` (wobei i \le k < j) eine Klammer zu setzen.
Die Kosten für ein spezifisches `k` sind:
`cost = solve(i, k) + solve(k + 1, j) + p[i-1] * p[k] * p[j]`

Wir wählen das Minimum all dieser Kosten.
Um eine exponentielle Zeitkomplexität von $O(2^n)$ zu vermeiden (durch das wiederholte Berechnen desselben `solve(i, j)`), speichern wir die Ergebnisse in einer 2D-Cache-Tabelle `memo[i][j]`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_25: Matrix Chain Multiplication.

m[i][j] = min over k of m[i][k] + m[k+1][j] +
dims[i][0] * dims[k][1] * dims[j][1].
"""


def solve(dims, n):
    if n <= 1:
        return 0
    INF = float("inf")
    m = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            m[i][j] = INF
            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dims[i][0] * dims[k][1] * dims[j][1]
                if cost < m[i][j]:
                    m[i][j] = cost
    return m[0][n - 1]
```

</details>

## Durchlauf

`p = [10, 20, 30, 40]`. `n = 3`. (Matrizen A, B, C).

Aufruf von `solve(1, 3)` (Löse ABC).
- Versuche `k=1`: `solve(1,1) + solve(2,3) + 10*20*40`.
  - `solve(1,1)` liefert `0`.
  - Aufruf von `solve(2,3)` (Löse BC).
    - Versuche `k=2`: `solve(2,2) + solve(3,3) + 20*30*40`.
      - `solve(2,2)` = `0`. `solve(3,3)` = `0`. Kosten = `24000`.
    - Liefert `24000`. Speichert `memo[2][3] = 24000`.
  - Summe für `k=1`: `0 + 24000 + 8000 = 32000`.

- Versuche `k=2`: `solve(1,2) + solve(3,3) + 10*30*40`.
  - Aufruf von `solve(1,2)` (Löse AB).
    - Versuche `k=1`: `solve(1,1) + solve(2,2) + 10*20*30`.
      - `0 + 0 + 6000 = 6000`.
    - Liefert `6000`. Speichert `memo[1][2] = 6000`.
  - `solve(3,3)` liefert `0`.
  - Summe für `k=2`: `6000 + 0 + 12000 = 18000`.

Das Minimum aus `32000` und `18000` ist `18000`.
Speichere `memo[1][3] = 18000`. Liefert `18000`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n^3)$ | $O(n^2)$ |
| **Durchschnittlicher Fall** | $O(n^3)$ | $O(n^2)$ |
| **Schlechtester Fall** | $O(n^3)$ | $O(n^2)$ |

Die Anzahl der eindeutigen Zustände in der `memo`-Tabelle beträgt $O(n^2)$. Für jeden Zustand `(i, j)` führen wir eine Schleife der Größe bis zu `n` aus, um alle Teilungspunkte `k` zu testen. Daher beträgt die Zeitkomplexität exakt $O(n^3)$.
Die Platzkomplexität beträgt $O(n^2)$ für die Memoization-Tabelle und $O(n)$ für den Rekursions-Stack.

## Varianten & Optimierungen

- **Bottom-Up:** Der iterative Bottom-Up-Ansatz vermeidet den Overhead des $O(n)$-Rekursions-Stacks und ist in der Praxis aufgrund der CPU-Cache-Lokalität geringfügig schneller, theoretisch jedoch identisch.

## Anwendungen in der Praxis

- **SQL-Abfrageoptimierung:** Datenbank-Engines verwenden eine stark modifizierte Version dieses Algorithmus, um die optimale Join-Reihenfolge für `SELECT * FROM A JOIN B JOIN C` zu bestimmen und die Erzeugung von Zwischenergebnissen zu minimieren.

## Verwandte Algorithmen in cOde(n)

- **[dp_13 - Matrix Chain Multiplication](dp_13_matrix-chain-multiplication.md)** — Das iterative, Bottom-Up-Gegenstück.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den enzyklopädischen Standardeintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*