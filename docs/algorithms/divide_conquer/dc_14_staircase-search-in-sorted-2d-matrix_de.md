# Suche in einer 2D-Matrix (Treppensuche)

| | |
|---|---|
| **ID** | `dc_14` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(N + M)$ Zeit, $O(1)$ Speicherplatz |
| **Schwierigkeitsgrad** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Suche in einer 2D-Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/) |

## Aufgabenstellung

Schreiben Sie einen effizienten Algorithmus, der in einer `m x n` ganzzahligen Matrix `matrix` nach einem Wert `target` sucht. Diese Matrix weist folgende Eigenschaften auf:
- Die Ganzzahlen in jeder Zeile sind von links nach rechts aufsteigend sortiert.
- Die Ganzzahlen in jeder Spalte sind von oben nach unten in aufsteigender Reihenfolge sortiert.

**Eingabe:** Eine 2D-Matrix der Dimensionen M × N und eine `target`-Ganzzahl.
**Ausgabe:** Ein boolescher Wert, der angibt, ob der gesuchte Wert vorhanden ist.

## Wann man es verwendet

- Ein sehr häufig auftretendes Problem der Matrixdurchquerung.
- Um zu veranschaulichen, wie man die Eigenschaften der zweidimensionalen Sortierung nutzt, um ganze Zeilen oder Spalten in $O(1)$ Zeit pro Schritt mathematisch auszuschließen.

## Vorgehensweise

**1. Der Schwachpunkt der binären Suche:**
Da die Zeilen sortiert sind, könnten wir einfach eine eindimensionale binäre Suche für jede einzelne Zeile durchführen! Dies würde $O(M log N)$ Zeit in Anspruch nehmen.
Aber Moment mal! Die Spalten sind AUCH sortiert. Können wir beide Eigenschaften gleichzeitig nutzen?

**2. Der Treppenansatz (Teile und herrsche):**
Betrachten wir die **obere rechte** Ecke der Matrix.
Nehmen wir an, die Matrix lautet:
```text
 1   4   7  11
 2   5   8  12
 3   6   9  16
```
Das Element oben rechts ist `11`. Sei unser `target` gleich `5`.
Wenn wir `target` mit `11` und `5 < 11` vergleichen.
Da die Spalte streng aufsteigend von oben nach unten sortiert ist, muss jede Zahl UNTERHALB von `11` in dieser Spalte GRÖSSER sein als `11`. Daher müssen sie auch größer sein als `5`!
Wir können die GESAMTE LETZTE SPALTE mathematisch eliminieren! Wir verschieben unseren Zeiger nach links (zu `7`).

Vergleichen wir nun `target=5` mit `7`. `5 < 7`. Wir eliminieren die Spalte erneut! Bewegen wir uns nach links zu `4`.
Vergleichen wir `target=5` mit `4`. `5 > 4`.
Da die Zeile streng aufsteigend von links nach rechts sortiert ist, muss jede Zahl LINKS von `4` in dieser Zeile KLEINER als `4` sein. Daher müssen sie auch kleiner als `5` sein!
Wir können die GESAMTE ERSTE ZEILE mathematisch ausschließen! Wir bewegen unseren Zeiger nach unten (zu `5`).

Vergleiche `target=5` mit `5`. Übereinstimmung gefunden!

**3. Die Regeln:**
Beginne bei `row = 0`, `col = N - 1` (oben rechts).
- Wenn `matrix[row][col] == target`: Gib `True` zurück.
- Wenn `matrix[row][col] > target`: Das Ziel muss sich links befinden. `col -= 1`.
- Wenn `matrix[row][col] < target`: Das Ziel muss sich unten befinden. `row += 1`.
*(Hinweis: Du kannst auch in der unteren linken Ecke beginnen und genau die umgekehrte Logik anwenden! Du kannst NICHT oben links oder unten rechts beginnen, da beide gültigen Richtungen gleichzeitig zu größeren bzw. kleineren Zahlen führen würden, was eine mehrdeutige Verzweigung zur Folge hätte).*

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dc_14: Staircase Search in Sorted 2D Matrix.

Given an n x m matrix where each row and each
"""


def solve(matrix, n, m, target):
    """Staircase search from the top-right corner."""
    if n == 0 or m == 0:
        return False
    i, j = 0, m - 1
    while i < n and j >= 0:
        v = matrix[i][j]
        if v == target:
            return True
        if v > target:
            j -= 1
        else:
            i += 1
    return False
```

</details>

## Schritt-für-Schritt-Anleitung

`matrix` ist 3 × 4 (oben). `target = 6`.
Start `row = 0`, `col = 3` (val = 11).

1. `11 > 6`. Nach links bewegen. `col = 2`.
2. `matrix[0][2]` = 7. `7 > 6`. Nach links bewegen. `col = 1`.
3. `matrix[0][1]` = 4. `4 < 6`. Nach unten bewegen. `row = 1`.
4. `matrix[1][1]` = 5. `5 < 6`. Nach unten bewegen. `row = 2`.
5. `matrix[2][1]` = 6. `6 == 6`. ÜBEREINSTIMMUNG!

Gibt `True` zurück. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(M + N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(M + N)$ | $O(1)$ |

Im schlimmsten Fall befindet sich das Ziel in der unteren linken Ecke, und der Zeiger muss die gesamte obere Zeile (N Schritte) und die gesamte linke Spalte (M Schritte) durchlaufen. Der zurückgelegte Weg ist eine „Treppe“ von rechts oben nach links unten. Die Gesamtzahl der Schritte darf M + N nicht überschreiten. Die Zeitkomplexität beträgt streng $O(M + N)$.
Die Platzkomplexität beträgt $O(1)$.

## Varianten & Optimierungen

- **Reines „Teile und herrsche“ (Quad-Tree):** Ist $O(M+N)$ die schnellstmögliche Lösung? Für eine quadratische N × N-Matrix ist dies $O(N)$. Können wir es in $O(\log N)$ schaffen? Eigentlich nicht. Aber wir können einen reinen „Divide-and-Conquer“-Algorithmus schreiben, der das zentrale Element überprüft. Er eliminiert einen der vier Quadranten vollständig und durchsucht die anderen drei Quadranten rekursiv. T(N) = 3T(N/2) -> $O(N^{log_2 3})$ ~= $O(N^{1.58})$. Somit ist der $O(M+N)$-Treppenansatz unbestreitbar die mathematisch optimale Lösung!
- **Suche in einer 2D-Matrix I (LeetCode 74):** Eine deutlich einfachere Variante, bei der die LETZTE Ganzzahl einer Zeile streng kleiner ist als die ERSTE Ganzzahl der nächsten Zeile. Die gesamte Matrix ist einfach ein riesiges, gefaltetes, sortiertes 1D-Array! Man kann einfach eine reine $O(log(MN)$) Binärsuche unter Verwendung von `row = mid // n` und `col = mid % n` durchführen.

## Anwendungen in der Praxis

- **Datenkompression (Blocksortierung):** Durchsuchen strukturell begrenzter zweidimensionaler Blöcke nach Quantisierungsschwellenwerten in JPEG-/MPEG-Kodierungsalgorithmen.

## Verwandte Algorithmen in cOde(n)

- **[searching_01 – Binäre Suche](../searching/search_01_binary-search.md)** — Zur Lösung der einfacheren Variante „Matrix I“.
- **[dc_03 – K-kleinstes Element (Quickselect)](dc_03_kth-smallest-quickselect.md)** — Eine weitere Anwendung von „Decrease and Conquer“, bei der ein Teil des Suchraums deterministisch verworfen wird.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
nach dem Vorbild der kanonischen Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
