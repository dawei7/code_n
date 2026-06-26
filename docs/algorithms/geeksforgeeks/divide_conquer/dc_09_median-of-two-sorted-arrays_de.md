# Median of Two Sorted Arrays

| | |
|---|---|
| **ID** | `dc_09` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(log(min(M, N)$)) Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 10/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) |

## Problemstellung

Gegeben sind zwei sortierte Arrays `nums1` und `nums2` der Größe `m` bzw. `n`. Geben Sie den Median der beiden sortierten Arrays zurück.
Die gesamte Zeitkomplexität sollte $O(log(m+n)$) betragen.

**Eingabe:** Zwei sortierte Integer-Arrays `nums1` und `nums2`.
**Ausgabe:** Eine Fließkommazahl, die den exakten Median repräsentiert.

## Wann man es verwendet

- Gilt weithin als eine der schwierigsten Standardfragen in technischen Vorstellungsgesprächen.
- Es testet die Fähigkeit, die Binäre Suche von der Suche nach einem *Wert* zu abstrahieren und stattdessen eine Binäre Suche nach einer *strukturellen Partitionsgrenze* durchzuführen.

## Ansatz

**1. Die Bedeutung des Medians:**
Wenn wir beide Arrays zu einem einzigen großen Array `A` der Größe `M + N` zusammenführen würden, würde der Median `A` perfekt in zwei Hälften teilen.
- **Linke Hälfte:** Enthält genau (M + N + 1) // 2 Elemente. Jedes Element hier ist kleiner als jedes Element in der rechten Hälfte.
- **Rechte Hälfte:** Enthält den Rest.
Wenn `M + N` ungerade ist, ist der Median das größte Element der linken Hälfte.
Wenn `M + N` gerade ist, ist der Median der Durchschnitt aus dem größten Element der linken Hälfte und dem kleinsten Element der rechten Hälfte.

**2. Partitionierung statt Zusammenführung:**
Wir wollen die Arrays NICHT physisch zusammenführen! (Das würde $O(M+N)$ Zeit in Anspruch nehmen).
Stattdessen wollen wir eine virtuelle Trennlinie durch `nums1` und eine virtuelle Trennlinie durch `nums2` ziehen, sodass gilt:
`len(nums1_left) + len(nums2_left) == (M + N + 1) // 2`.
Das bedeutet, wenn wir einen Partitionspunkt `partitionX` in `nums1` wählen, ist der Partitionspunkt `partitionY` in `nums2` mathematisch ERZWUNGEN!
`partitionY = (M + N + 1) // 2 - partitionX`.

**3. Binäre Suche nach der perfekten Partition:**
Wir führen die Binäre Suche für `partitionX` nur auf dem kleineren Array durch (sagen wir `nums1`, sodass der Suchraum $O(log(\min(M, N)$)) beträgt).
Bei jedem gegebenen `partitionX` prüfen wir, ob es GÜLTIG ist.
Es ist genau dann gültig, wenn:
- `maxLeftX <= minRightY` (Das größte Element links von X ist kleiner oder gleich dem kleinsten Element rechts von Y).
- `maxLeftY <= minRightX` (Das größte Element links von Y ist kleiner oder gleich dem kleinsten Element rechts von X).

Wenn `maxLeftX > minRightY`: Wir haben in `X` zu weit rechts partitioniert. Wir müssen unseren `high`-Pointer der Binären Suche nach links verschieben!
Wenn `maxLeftY > minRightX`: Wir haben in `X` zu weit links partitioniert. Wir müssen unseren `low`-Pointer der Binären Suche nach rechts verschieben!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dc_09: Median of Two Sorted Arrays.

Given two sorted arrays `a` (length m) and `b`
"""


def solve(a, b, m, n):
    """Median of two sorted arrays in O(log(min(m, n)))."""
    if m > n:
        return solve(b, a, n, m)
    lo, hi = 0, m
    half = (m + n + 1) // 2
    while lo <= hi:
        i = (lo + hi) // 2
        j = half - i
        if i > 0 and a[i - 1] > b[j]:
            hi = i - 1
        elif i < m and j > 0 and b[j - 1] > a[i]:
            lo = i + 1
        else:
            # Found the right partition.
            if i == 0:
                left_max = b[j - 1]
            elif j == 0:
                left_max = a[i - 1]
            else:
                left_max = max(a[i - 1], b[j - 1])
            if (m + n) % 2 == 1:
                return float(left_max)
            if i == m:
                right_min = b[j]
            elif j == n:
                right_min = a[i]
            else:
                right_min = min(a[i], b[j])
            return (left_max + right_min) / 2
```

</details>

## Durchlauf

`nums1 = [1, 3, 8, 9, 15]`. `X = 5`.
`nums2 = [7, 11, 18, 19, 21, 25]`. `Y = 6`.
Gesamtzahl der Elemente = 11 (ungerade). Zielgröße der linken Hälfte = (5 + 6 + 1) // 2 = 6.

1. **Binäre Suche 1:**
   - `low = 0, high = 5`. `partitionX = 2`. (Nimm 2 von nums1).
   - `partitionY = 6 - 2 = 4`. (Nimm 4 von nums2).
   - `maxLeftX = nums1[1] = 3`. `minRightX = nums1[2] = 8`.
   - `maxLeftY = nums2[3] = 19`. `minRightY = nums2[4] = 21`.
   - Prüfung: `3 <= 21` (Wahr). `19 <= 8` (FALSCH!).
   - Da `maxLeftY > minRightX` (`19 > 8`), benötigen wir MEHR von `nums1`, um die große `19` herauszudrängen! `low = partitionX + 1 = 3`.
2. **Binäre Suche 2:**
   - `low = 3, high = 5`. `partitionX = 4`. (Nimm 4 von nums1).
   - `partitionY = 6 - 4 = 2`. (Nimm 2 von nums2).
   - `maxLeftX = nums1[3] = 9`. `minRightX = nums1[4] = 15`.
   - `maxLeftY = nums2[1] = 11`. `minRightY = nums2[2] = 18`.
   - Prüfung: `9 <= 18` (Wahr). `11 <= 15` (Wahr!).
   - ÜBEREINSTIMMUNG GEFUNDEN!
3. **Median berechnen:**
   - Die Gesamtzahl ist ungerade. Der Median ist `max(maxLeftX, maxLeftY)`.
   - `max(9, 11) = 11`.

Das Ergebnis ist `11.0`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(log(min(M, N)$)) | $O(1)$ |
| **Schlechtester Fall** | $O(log(min(M, N)$)) | $O(1)$ |

Wir führen die Binäre Suche nur auf dem kleineren Array durch. Daher ist der Suchraum durch $\min(M, N)$ begrenzt, was zu einer exakten Zeitkomplexität von $O(log(\min(M, N)$)) führt.
Es werden keine neuen Arrays oder Rekursions-Stacks erstellt. Die Platzkomplexität ist strikt $O(1)$.

## Varianten & Optimierungen

- **K-tes Element von zwei sortierten Arrays:** Das Finden des Medians ist im Grunde nur das Finden des K-ten Elements, wobei K = (M+N)/2. Sie können exakt denselben Partitionsalgorithmus verwenden, um das K-te kleinste Element von zwei sortierten Arrays zu finden, indem Sie die Zielgröße der linken Hälfte einfach auf `K` setzen.

## Anwendungen in der Praxis

- **Verteilte Datenbanken (Sharding):** Wenn ein Index über zwei physisch unterschiedliche Datenbankknoten geshardet und sortiert ist, können Sie den globalen Median abfragen, ohne das gesamte Shard über das Netzwerk übertragen zu müssen! Sie müssen nur $O(\log N)$ Mal hin und her pingen, um die Partitionsgrenze zu bestimmen.

## Verwandte Algorithmen in cOde(n)

- **[searching_01 - Binary Search](../searching/search_01_binary-search.md)** — Der grundlegende Algorithmus-Mechanismus.
- **[dc_03 - Kth Smallest Element (Quickselect)](dc_03_kth-smallest-quickselect.md)** — Finden des Medians/K-ten Elements eines einzelnen UNSORTIERTEN Arrays in $O(N)$ Zeit.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*