# 2D-Fenwick Tree (Summe einer Teilmatrix)

| | |
|---|---|
| **ID** | `fenwick_03` |
| **Kategorie** | fenwick |
| **Komplexität (erforderlich)** | $O(log N * log M)$ Abfrage/Aktualisierung |
| **Schwierigkeitsgrad** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 3/10 |
| **LeetCode-Äquivalent** | [Range Sum Query 2D – Mutable](https://leetcode.com/problems/range-sum-query-2d-mutable/) |

## Aufgabenstellung

Gegeben sei eine 2D-Matrix der Dimensionen N × M. Implementiere einen zweidimensionalen Fenwick Tree, der Folgendes unterstützt:
1. `update(row, col, value)`: Aktualisiere die Matrix an der Position `(row, col)` auf den neuen Wert `value`.
2. `query(row1, col1, row2, col2)`: Die Summe der Elemente innerhalb des Rechtecks zurückgeben, das durch seine obere linke Ecke `(row1, col1)` und seine untere rechte Ecke `(row2, col2)` definiert ist.

Beide Operationen müssen deutlich schneller als $O(N)$ sein.

**Eingabe:** Eine 2D-Matrix sowie eine Reihe von `update`- und `query`-Operationen.
**Ausgabe:** Die Ergebnisse der Bereichsabfragen.

## Wann sollte man es verwenden?

- Wenn Sie ein riesiges Raster (z. B. ein Bild, eine Spielkarte) mit sich ständig ändernden Werten haben und Bereichssummen abfragen müssen.
- Dies ist die veränderbare Version der Standard-„2D-Präfixsummen“-Matrix. Eine Standard-2D-Präfixsumme beantwortet Abfragen in $O(1)$, benötigt jedoch $O(N \times M)$ für die Aktualisierung eines einzelnen Pixels! Ein 2D-Fenwick Tree aktualisiert sich in Bruchteilen einer Millisekunde.

## Vorgehensweise

Ein 1D-Fenwick Tree ist ein Array, in dem `BIT[x]` die Summe eines horizontalen Bereichs enthält.
Ein 2D-Fenwick Tree ist einfach ein 2D-Array (eine Matrix), in dem `BIT[x][y]` die Summe eines **Rechtecks** enthält, das bei `(x, y)` endet. Die Breite des Rechtecks wird durch das niedrigste gesetzte Bit von `x` bestimmt, und die Höhe wird durch das niedrigste gesetzte Bit von `y` bestimmt!

**2D-Punktaktualisierung:**
Anstelle einer einzelnen `while`-Schleife verwenden wir zwei verschachtelte `while`-Schleifen!
Für eine gegebene `(row, col)`-Aktualisierung mit `delta`:
Wir durchlaufen `x` in aufsteigender Reihenfolge durch die Zeilen. Innerhalb dieser Schleife durchlaufen wir `y` in aufsteigender Reihenfolge durch die Spalten und addieren `delta` zu `BIT[x][y]`.

**2D-Präfixabfrage:**
Um die Summe des Rechtecks von `(0,0)` bis `(row, col)` zu erhalten:
Wir durchlaufen `x` nach unten. Innerhalb dieser Schleife durchlaufen wir `y` nach unten und akkumulieren `BIT[x][y]`.

**2D-Bereichsabfrage:**
Genau wie bei 2D-Präfixsummen wird bei der Abfrage einer Teilmatrix von `(r1, c1)` bis `(r2, c2)` das Inklusions-Exklusions-Prinzip angewendet:
`Area = Prefix(r2, c2) - Prefix(r1-1, c2) - Prefix(r2, c1-1) + Prefix(r1-1, c1-1)`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

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

## Schritt-für-Schritt-Anleitung

*(Konzeptionell)*
`matrix = [[1, 2], [3, 4]]`

1. **Abfrage des Bereichs (0,0) bis (1,1):**
   - Wir benötigen `Pref(2,2) - Pref(0,2) - Pref(2,0) + Pref(0,0)`.
   - `Pref(0, x)` und `Pref(x, 0)` geben natürlich `0` zurück, da die `while i > 0`-Schleife sofort beendet wird.
   - Wir berechnen `Pref(2,2)`, indem wir die `BIT`-Werte von oben nach unten akkumulieren.
   - Ergebnis: 1 + 2 + 3 + 4 = 10. ✓

2. **Update(0, 1, Wert=5):**
   - Der alte Wert ist 2. Der neue ist 5. `delta = 3`.
   - `_add(1, 2, delta=3)`
   - Schleife `i` von 1 bis `rows`. Darin Schleife `j` von 2 bis `cols`.
   - `BIT[1][2] += 3`.
   - `BIT[2][2] += 3`.
   - Der Baum spiegelt die 2D-Mutation sofort wider! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(N * M)$ |
| **Durchschnittlicher Fall** | $O(log N * log M)$ | $O(N * M)$ |
| **Schlechteste** | $O(log N * log M)$ | $O(N * M)$ |

Aufgrund der beiden verschachtelten `while`-Schleifen, die Bits manipulieren, benötigen die Operationen $O(log N x log M)$ Zeit. Bei einer 1000 × 1000-Matrix sind das etwa 10 × 10 = 100 Operationen, was unglaublich schnell ist!
Die Platzkomplexität beträgt $O(N \times M)$ für die Speicherung der 2D-BIT-Arrays.

## Varianten & Optimierungen

- **3D-Fenwick Tree:** Die Logik lässt sich unendlich erweitern! Man kann einfach eine dritte `while`-Schleife für die Z-Achse verschachteln, um 3D-Volumina im Raum in $O(log N x log M x log Z)$ Zeit abzufragen.

## Praktische Anwendungen

- **Computer Vision & Grafik:** Sofortige Anpassung von Helligkeits-/Kontrastbereichen in Bildbearbeitungsprogrammen und Berechnung der durchschnittlichen Leuchtdichte von begrenzten Pixelrechtecken.
- **Räumliche Indizierung:** Schnelle Abfrage von Dichte/Bevölkerungszahlen innerhalb rechteckiger Koordinatengrenzen auf dynamischen, gitterbasierten Karten.

## Verwandte Algorithmen in cOde(n)

- **[fenwick_02 – Range-Sum-Abfrage](fenwick_02_range-sum-query-bit.md)** — Der 1D-Vorläufer.
- **[dynamic_10 - Max Maximal Square](../dynamic/dp_10_unique-paths.md)** *(Konzeptioneller Zusammenhang)* — Standardmäßige 2D-DP-/Präfixmatrizen basieren auf genau derselben Inklusions-Exklusions-Geometrie.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
nach dem Vorbild der kanonischen Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
