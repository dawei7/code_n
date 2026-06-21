# Matrix Chain Multiplication

| | |
|---|---|
| **ID** | `dp_13` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(N^3)$ Zeit, $O(N^2)$ Platz |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **Wikipedia** | [Matrix chain multiplication](https://en.wikipedia.org/wiki/Matrix_chain_multiplication) |

## Problemstellung

Gegeben ist eine Sequenz von Matrizen; finden Sie den effizientesten Weg, diese Matrizen miteinander zu multiplizieren.
Die Matrixmultiplikation ist assoziativ, was bedeutet, dass `A * (B * C)` das gleiche mathematische Ergebnis liefert wie `(A * B) * C`. Die *Anzahl der erforderlichen skalaren Multiplikationen* kann jedoch je nach Gruppierung drastisch variieren!
Die Multiplikation einer P x Q Matrix mit einer Q x R Matrix erfordert P x Q x R skalare Multiplikationen.
Gegeben ist ein Array `p`, das die Dimensionen von N Matrizen repräsentiert, sodass die i-te Matrix die Dimension `p[i-1] x p[i]` hat. Finden Sie die minimale Anzahl an skalaren Multiplikationen, die benötigt werden, um die gesamte Kette zu multiplizieren.

**Eingabe:** Ein Array von Integern `p` der Länge N+1.
**Ausgabe:** Ein Integer, der die minimale Anzahl an skalaren Multiplikationen repräsentiert.

## Wann man es verwendet

- Die kanonische Einführung in **Interval DP** (auch bekannt als Range DP).
- Verwenden Sie dies immer dann, wenn ein Problem Sie auffordert, benachbarte Elemente in einem Array optimal zu klammern, zu gruppieren oder zusammenzuführen.

## Ansatz

**1. Den Zustand definieren:**
Sei `dp[i][j]` die minimale Anzahl an skalaren Multiplikationen, die benötigt werden, um die Kette von Matrizen von Matrix `i` bis Matrix `j` zu multiplizieren.

**2. Die Basisfälle finden:**
Wenn `i == j`, gibt es nur eine Matrix! Die Kosten, eine einzelne Matrix mit nichts zu multiplizieren, sind 0.
`dp[i][i] = 0` für alle i.

**3. Den Übergang finden (Die Rekurrenz):**
Um eine Kette von Matrizen von `i` bis `j` zu multiplizieren, müssen wir eine finale Multiplikation durchführen, die zwei Unterketten verbindet. Wir können die Kette an einem Index `k` teilen (wobei i \le k < j).
Die Kosten für diese Teilung bei `k` sind:
- Die optimalen Kosten zur Berechnung der linken Unterkette: `dp[i][k]`
- Die optimalen Kosten zur Berechnung der rechten Unterkette: `dp[k+1][j]`
- Die Kosten, um die beiden resultierenden Matrizen miteinander zu multiplizieren: Die resultierende linke Matrix hat die Dimensionen `p[i-1] x p[k]`, und die rechte Matrix ist `p[k] x p[j]`. Die Multiplikation kostet `p[i-1] * p[k] * p[j]`.

Wir versuchen ALLE möglichen Teilungspunkte `k` und wählen das Minimum!
`dp[i][j] = min( dp[i][k] + dp[k+1][j] + p[i-1]*p[k]*p[j] )` für alle i \le k < j.

**4. Die Tabelle aufbauen (Bottom-Up nach Länge):**
Dies ist der kniffligste Teil von Interval DP! Sie können NICHT einfach `i` von 0 bis N und `j` von 0 bis N durchlaufen.
Um `dp[1][4]` zu berechnen, benötigen Sie `dp[1][2]` und `dp[3][4]`. Sie müssen zuerst alle Intervalle der Länge 2 berechnen, dann Länge 3, dann Länge 4!
Die äußere Schleife muss über die `length` des Intervalls iterieren.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_13: Matrix Chain Multiplication.

dp[i][j] = min cost of multiplying matrices i..j.
"""


def solve(p):
    n = len(p) - 1
    if n <= 1:
        return 0
    INF = float("inf")
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = INF
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    return dp[0][n - 1]
```

</details>

## Durchlauf

`p = [10, 20, 30, 40]`. Es gibt 3 Matrizen (A, B, C).
A ist 10 x 20, B ist 20 x 30, C ist 30 x 40.
`n = 3`. `dp` ist 4 x 4, initialisiert mit 0.

1. **Länge = 2:**
   - **i = 1, j = 2 (AB):**
     - k = 1: `dp[1][1] + dp[2][2] + p[0]*p[1]*p[2]`
     - = 0 + 0 + 10 x 20 x 30 = 6000. `dp[1][2] = 6000`.
   - **i = 2, j = 3 (BC):**
     - k = 2: `dp[2][2] + dp[3][3] + p[1]*p[2]*p[3]`
     - = 0 + 0 + 20 x 30 x 40 = 24000. `dp[2][3] = 24000`.

2. **Länge = 3:**
   - **i = 1, j = 3 (ABC):**
     - k = 1 (Auswertung als A(BC)): `dp[1][1] + dp[2][3] + p[0]*p[1]*p[3]`
       - = 0 + 24000 + 10 x 20 x 40 = 24000 + 8000 = 32000.
     - k = 2 (Auswertung als (AB)C): `dp[1][2] + dp[3][3] + p[0]*p[2]*p[3]`
       - = 6000 + 0 + 10 x 30 x 40 = 6000 + 12000 = 18000.
     - Das Minimum ist 18000. `dp[1][3] = 18000`.

Das Ergebnis `dp[1][3]` ist 18000. ✓ (Die Gruppierung als (AB)C ist fast doppelt so schnell!).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N^3)$ | $O(N^2)$ |
| **Durchschnittlicher Fall** | $O(N^3)$ | $O(N^2)$ |
| **Schlechtester Fall** | $O(N^3)$ | $O(N^2)$ |

Die verschachtelten Schleifen definieren $O(N^2)$ Intervalle `(i, j)`. Für jedes Intervall läuft die `k`-Schleife bis zu N Mal. Die gesamte Zeitkomplexität ist strikt $O(N^3)$.
Die Platzkomplexität beträgt $O(N^2)$ für die 2D DP-Matrix.

## Varianten & Optimierungen

- **Ausgabe der Klammerung:** Wenn Sie einen String wie `"(A(BC))"` zurückgeben müssen, müssen Sie eine zweite N x N Matrix `split[i][j]` führen, die den Integer `k` speichert, der die minimalen Kosten ergab. Rekonstruieren Sie dann den String rekursiv!
- **Burst Balloons:** Ein extrem schwieriges LeetCode Hard-Problem, das mathematisch identisch mit der Matrix Chain Multiplication ist. Sie iterieren über Längen und versuchen, einen Ballon `k` als den *letzten* Ballon auszuwählen, der im Intervall platzt!

## Anwendungen in der Praxis

- **Datenbank-Query-Optimierer:** Bestimmung der optimalen Join-Reihenfolge für komplexe SQL-Statements (z. B. `A JOIN B JOIN C`), um den Overhead bei der Erstellung temporärer Tabellen zu minimieren.

## Verwandte Algorithmen in cOde(n)

- **[dp_14 - Palindromic Partitioning](dp_14_palindromic-partitioning.md)** — Ein weiteres Interval DP, das Schnitte über einen zusammenhängenden String optimiert.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Wettbewerbsprogrammierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*