# Suche in einer 2D-Matrix (Treppensuche)

| | |
|---|---|
| **ID** | `dc_14` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(N + M)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/) |

## Problemstellung

Schreiben Sie einen effizienten Algorithmus, der einen Wert `target` in einer `m x n` Integer-Matrix `matrix` sucht. Diese Matrix weist folgende Eigenschaften auf:
- Die Integer-Werte in jeder Zeile sind von links nach rechts aufsteigend sortiert.
- Die Integer-Werte in jeder Spalte sind von oben nach unten aufsteigend sortiert.

**Eingabe:** Eine 2D-Matrix der Dimensionen M x N und ein Integer `target`.
**Ausgabe:** Ein Boolean-Wert, der angibt, ob das `target` vorhanden ist.

## Wann ist dieser Algorithmus zu verwenden?

- Ein sehr häufiges Problem bei der Matrix-Traversierung.
- Um zu demonstrieren, wie man die Eigenschaften zweidimensionaler Sortierung nutzt, um mathematisch ganze Zeilen oder Spalten in $O(1)$ Zeit pro Schritt zu verwerfen.

## Ansatz

**1. Die Schwäche der binären Suche:**
Da die Zeilen sortiert sind, könnten wir einfach eine 1D-Binärsuche auf jeder einzelnen Zeile durchführen! Dies würde $O(M log N)$ Zeit in Anspruch nehmen.
Aber Moment! Die Spalten sind EBENFALLS sortiert. Können wir beide Eigenschaften gleichzeitig nutzen?

**2. Der Treppen-Ansatz (Decrease and Conquer):**
Betrachten Sie die **obere rechte** Ecke der Matrix.
Nehmen wir an, die Matrix sieht so aus:
```text
 1   4   7  11
 2   5   8  12
 3   6   9  16
```
Das Element oben rechts ist `11`. Sei unser `target` gleich `5`.
Wenn wir `target` mit `11` vergleichen, gilt `5 < 11`.
Da die Spalte streng aufsteigend von oben nach unten sortiert ist, muss jede Zahl UNTERHALB von `11` in dieser Spalte GRÖSSER als `11` sein. Folglich müssen sie auch größer als `5` sein!
Wir können mathematisch die GESAMTE LETZTE SPALTE eliminieren! Wir bewegen unseren Pointer nach links (zu `7`).

Vergleichen wir nun `target=5` mit `7`. `5 < 7`. Wir eliminieren die Spalte erneut! Wir bewegen uns nach links zu `4`.
Vergleichen wir `target=5` mit `4`. `5 > 4`.
Da die Zeile streng aufsteigend von links nach rechts sortiert ist, muss jede Zahl LINKS von `4` in dieser Zeile KLEINER als `4` sein. Folglich müssen sie auch kleiner als `5` sein!
Wir können mathematisch die GESAMTE ERSTE ZEILE eliminieren! Wir bewegen unseren Pointer nach unten (zu `5`).

Vergleichen wir `target=5` mit `5`. Treffer gefunden!

**3. Die Regeln:**
Starten Sie bei `row = 0`, `col = N - 1` (oben rechts).
- Wenn `matrix[row][col] == target`: Gebe `True` zurück.
- Wenn `matrix[row][col] > target`: Das `target` muss links liegen. `col -= 1`.
- Wenn `matrix[row][col] < target`: Das `target` muss unterhalb liegen. `row += 1`.
*(Hinweis: Sie können auch in der unteren linken Ecke starten und die exakt umgekehrte Logik anwenden! Sie dürfen NICHT oben links oder unten rechts starten, da beide gültigen Richtungen gleichzeitig zu größeren/kleineren Zahlen führen würden, was zu einem mehrdeutigen Verzweigungspfad führen würde).*

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

## Durchlauf

`matrix` ist 3 x 4 (siehe oben). `target = 6`.
Start `row = 0`, `col = 3` (Wert = 11).

1. `11 > 6`. Bewege nach links. `col = 2`.
2. `matrix[0][2]` = 7. `7 > 6`. Bewege nach links. `col = 1`.
3. `matrix[0][1]` = 4. `4 < 6`. Bewege nach unten. `row = 1`.
4. `matrix[1][1]` = 5. `5 < 6`. Bewege nach unten. `row = 2`.
5. `matrix[2][1]` = 6. `6 == 6`. TREFFER!

Gibt `True` zurück. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(M + N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(M + N)$ | $O(1)$ |

Im schlechtesten Fall befindet sich das `target` in der unteren linken Ecke, und der Pointer muss den gesamten Weg über die oberste Zeile (N Schritte) und die gesamte linke Spalte hinunter (M Schritte) zurücklegen. Der Pfad beschreibt eine "Treppe" von oben rechts nach unten links. Die Gesamtzahl der Schritte kann M + N nicht überschreiten. Die Zeitkomplexität ist strikt $O(M + N)$.
Die Platzkomplexität beträgt $O(1)$.

## Varianten & Optimierungen

- **Reines Divide and Conquer (Quad-Tree):** Ist $O(M+N)$ das schnellstmögliche? Für eine quadratische N x N Matrix ist es $O(N)$. Können wir es in $O(\log N)$ erreichen? Tatsächlich nein. Aber wir können einen reinen Divide-and-Conquer-Algorithmus schreiben, der das mittlere Element prüft. Er eliminiert einen der 4 Quadranten vollständig und durchsucht die anderen 3 Quadranten rekursiv. T(N) = 3T(N/2) -> $O(N^{log_2 3})$ ~= $O(N^{1.58})$. Somit ist der $O(M+N)$ Treppen-Ansatz unbestreitbar die mathematisch optimale Lösung!
- **Search a 2D Matrix I (LeetCode 74):** Eine deutlich einfachere Variante, bei der die LETZTE Ganzzahl einer Zeile strikt kleiner ist als die ERSTE Ganzzahl der nächsten Zeile. Die gesamte Matrix ist lediglich ein riesiges, in 1D sortiertes Array, das umgebrochen wurde! Man kann einfach eine reine $O(log(MN))$-Binärsuche mit `row = mid // n` und `col = mid % n` durchführen.

## Anwendungen in der Praxis

- **Datenkompression (Block-Sortierung):** Scannen von strukturell eingeschränkten 2D-Raumblöcken für Quantisierungsschwellenwerte in JPEG/MPEG-Kodierungsalgorithmen.

## Verwandte Algorithmen in cOde(n)

- **[searching_01 - Binary Search](../searching/search_01_binary-search.md)** — Zur Lösung der einfacheren "Matrix I"-Variante.
- **[dc_03 - Kth Smallest Element (Quickselect)](dc_03_kth-smallest-quickselect.md)** — Eine weitere Anwendung von Decrease and Conquer, bei der ein Teil des Suchraums deterministisch verworfen wird.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Wettbewerbsprogrammierungs-Referenzseiten verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*