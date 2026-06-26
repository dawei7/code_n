# 2D Fenwick Tree (Sub-matrix Sum)

| | |
|---|---|
| **ID** | `fenwick_03` |
| **Category** | fenwick |
| **Complexity (required)** | $O(log N * log M)$ Query/Update |
| **Difficulty** | 7/10 |
| **Interview relevance** | 3/10 |
| **LeetCode Equivalent** | [Range Sum Query 2D - Mutable](https://leetcode.com/problems/range-sum-query-2d-mutable/) |

## Problem statement

Gegeben ist eine 2D-Matrix der Dimensionen N x M. Implementieren Sie einen 2-dimensionalen Fenwick Tree, der folgende Operationen unterstützt:
1. `update(row, col, value)`: Aktualisieren Sie die Matrix an der Position `(row, col)` auf den neuen `value`.
2. `query(row1, col1, row2, col2)`: Geben Sie die Summe der Elemente innerhalb des Rechtecks zurück, das durch die obere linke Ecke `(row1, col1)` und die untere rechte Ecke `(row2, col2)` definiert ist.

Beide Operationen müssen strikt schneller als $O(N)$ Zeit sein.

**Input:** Eine 2D-Matrix und eine Reihe von `update`- und `query`-Operationen.
**Output:** Die Ergebnisse der Bereichsabfragen (Range Queries).

## When to use it

- Wenn Sie ein massives Gitter (z. B. ein Bild, eine Spielkarte) mit sich ständig ändernden Werten haben und Flächensummen abfragen müssen.
- Dies ist die veränderbare (mutable) Version der Standard-Matrix für "2D Prefix Sum". Eine Standard-2D-Präfixsumme beantwortet Abfragen in $O(1)$, benötigt aber $O(N \times M)$, um ein einzelnes Pixel zu aktualisieren! Ein 2D-Fenwick-Baum führt Aktualisierungen in Bruchteilen einer Millisekunde durch.

## Approach

Ein 1D-Fenwick Tree ist ein Array, bei dem `BIT[x]` die Summe eines horizontalen Bereichs enthält.
Ein 2D-Fenwick Tree ist einfach ein 2D-Array (Matrix), bei dem `BIT[x][y]` die Summe eines **Rechtecks** enthält, das bei `(x, y)` endet. Die Breite des Rechtecks wird durch das niedrigste gesetzte Bit von `x` bestimmt, und die Höhe wird durch das niedrigste gesetzte Bit von `y` bestimmt!

**2D Point Update:**
Anstelle einer einzelnen `while`-Schleife verwenden wir zwei verschachtelte `while`-Schleifen!
Für ein gegebenes `(row, col)`-Update mit `delta`:
Wir iterieren `x` aufwärts durch die Zeilen. Innerhalb dieser Schleife iterieren wir `y` aufwärts durch die Spalten und addieren `delta` zu `BIT[x][y]`.

**2D Prefix Query:**
Um die Summe des Rechtecks von `(0,0)` bis `(row, col)` zu erhalten:
Wir iterieren `x` abwärts. Innerhalb dieser Schleife iterieren wir `y` abwärts und akkumulieren `BIT[x][y]`.

**2D Range Query:**
Genau wie bei 2D-Präfixsummen verwendet die Abfrage einer Sub-Matrix `(r1, c1)` bis `(r2, c2)` das Inklusions-Exklusions-Prinzip:
`Area = Prefix(r2, c2) - Prefix(r1-1, c2) - Prefix(r2, c1-1) + Prefix(r1-1, c1-1)`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for fenwick_03: 2D Fenwick Tree (Sub-matrix Sum).

Build a 2D Binary Indexed Tree on an n x n matrix,
"""


def solve(matrix, n, updates, queries, q):
    """2D BIT with point updates and sub-matrix sum queries.

    1-based BIT indexing internally (so cell (r, c) maps to
    BIT[r+1][c+1]).
    """
    if n == 0:
        return [0] * q
    # Build BIT.
    bit = [[0] * (n + 1) for _ in range(n + 1)]
    work = [row[:] for row in matrix]

    def update(r, c, delta):
        r += 1
        c += 1
        i = r
        while i <= n:
            j = c
            while j <= n:
                bit[i][j] += delta
                j += j & -j
            i += i & -i

    def prefix(r, c):
        # Sum over (0,0) .. (r,c) inclusive. Caller must clamp
        # r, c to -1 (which yields 0).
        if r < 0 or c < 0:
            return 0
        r += 1
        c += 1
        s = 0
        i = r
        while i > 0:
            j = c
            while j > 0:
                s += bit[i][j]
                j -= j & -j
            i -= i & -i
        return s

    # Build the BIT by inserting each cell's initial value.
    for r in range(n):
        for c in range(n):
            if matrix[r][c] != 0:
                update(r, c, matrix[r][c])

    # Apply updates.
    for r, c, delta in updates:
        work[r][c] += delta
        update(r, c, delta)

    # Answer queries.
    out = []
    for r1, c1, r2, c2 in queries:
        s = (prefix(r2, c2)
             - prefix(r1 - 1, c2)
             - prefix(r2, c1 - 1)
             + prefix(r1 - 1, c1 - 1))
        out.append(s)
    return out
```

</details>

## Walk-through

*(Konzeptionell)*
`matrix = [[1, 2], [3, 4]]`

1. **Query Region (0,0) to (1,1):**
   - Wir benötigen `Pref(2,2) - Pref(0,2) - Pref(2,0) + Pref(0,0)`.
   - `Pref(0, x)` und `Pref(x, 0)` geben natürlicherweise `0` zurück, da die `while i > 0`-Schleife sofort terminiert.
   - Wir berechnen `Pref(2,2)` durch Akkumulation der `BIT`-Werte abwärts.
   - Ergebnis: 1 + 2 + 3 + 4 = 10. ✓

2. **Update(0, 1, value=5):**
   - Alter Wert ist 2. Neuer Wert ist 5. `delta = 3`.
   - `_add(1, 2, delta=3)`
   - Schleife `i` von 1 bis `rows`. Innerhalb davon Schleife `j` von 2 bis `cols`.
   - `BIT[1][2] += 3`.
   - `BIT[2][2] += 3`.
   - Der Baum spiegelt sofort die 2D-Mutation wider! ✓

## Complexity

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(N * M)$ |
| **Durchschnittlicher Fall** | $O(log N * log M)$ | $O(N * M)$ |
| **Schlechtester Fall** | $O(log N * log M)$ | $O(N * M)$ |

Aufgrund der zwei verschachtelten `while`-Schleifen, die die Bits manipulieren, benötigen die Operationen $O(log N \times log M)$ Zeit. Für eine 1000 x 1000 Matrix sind das etwa 10 x 10 = 100 Operationen, was unglaublich schnell ist!
Die Platzkomplexität beträgt $O(N \times M)$, um die 2D-BIT-Arrays zu speichern.

## Variants & optimizations

- **3D Fenwick Tree:** Die Logik lässt sich beliebig erweitern! Sie können einfach eine dritte `while`-Schleife für die Z-Achse verschachteln, um 3D-Volumina im Raum in $O(log N \times log M \times log Z)$ Zeit abzufragen.

## Real-world applications

- **Computer Vision & Grafik:** Sofortige Anpassung von Helligkeits-/Kontrastbereichen in Bildbearbeitungsprogrammen und Berechnung der durchschnittlichen Leuchtdichte von begrenzten Pixel-Rechtecken.
- **Spatial Indexing:** Schnelle Abfrage von Dichte/Populationen innerhalb rechteckiger Koordinatengrenzen auf dynamischen, gitterbasierten Karten.

## Related algorithms in cOde(n)

- **[fenwick_02 - Range Sum Query](fenwick_02_range-sum-query-bit.md)** — Der 1D-Vorläufer.
- **[dynamic_10 - Max Maximal Square](../dynamic/dp_10_unique-paths.md)** *(Konzeptioneller Link)* — Standard 2D-DP/Präfix-Matrizen basieren auf der exakt gleichen Inklusions-Exklusions-Geometrie.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*