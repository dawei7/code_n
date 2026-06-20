# Median zweier sortierter Arrays

| | |
|---|---|
| **ID** | `dc_09` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(log(min(M, N)$)) Zeit, $O(1)$ Speicherplatz |
| **Schwierigkeitsgrad** | 10/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [Median zweier sortierter Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) |

## Aufgabenstellung

Gegeben sind zwei sortierte Arrays `nums1` und `nums2` der Größe `m` bzw. `n`. Gib den Median der beiden sortierten Arrays zurück.
Die Gesamtlaufzeitkomplexität sollte $O(log(m+n)$) betragen.

**Eingabe:** Zwei sortierte Ganzzahl-Arrays `nums1` und `nums2`.
**Ausgabe:** Eine Gleitkommazahl, die den exakten Median darstellt.

## Wann man diese Aufgabe verwenden sollte

- Gilt weithin als eine der schwierigsten Standardfragen in technischen Vorstellungsgesprächen.
- Sie testet Ihre Fähigkeit, die binäre Suche nicht auf die Suche nach einem *Wert* zu beschränken, sondern stattdessen eine binäre Suche nach einer *strukturellen Trenngrenze* durchzuführen.

## Vorgehensweise

**1. Die Bedeutung des Medians:**
Würden wir beide Arrays zu einem einzigen großen Array `A` der Größe `M + N` zusammenführen, würde der Median `A` das Array perfekt in zwei Hälften teilen.
- **Linke Hälfte:** Enthält genau (M + N + 1) // 2 Elemente. Jedes Element hier ist kleiner als jedes Element in der rechten Hälfte.
- **Rechte Hälfte:** Enthält den Rest.
Ist `M + N` ungerade, ist der Median das größte Element in der linken Hälfte.
Ist `M + N` gerade, ist der Median der Mittelwert aus dem größten Element in der linken Hälfte und dem kleinsten Element in der rechten Hälfte.

**2. Partitionierung statt Zusammenführung:**
Wir wollen die Arrays NICHT physisch zusammenführen! (Das würde $O(M+N)$ Zeit in Anspruch nehmen).
Stattdessen wollen wir eine virtuelle Trennlinie durch `nums1` und eine virtuelle Trennlinie durch `nums2` ziehen, sodass gilt:
`len(nums1_left) + len(nums2_left) == (M + N + 1) // 2`.
Das bedeutet: Wenn wir einen Teilungspunkt `partitionX` in `nums1` wählen, ist der Teilungspunkt `partitionY` in `nums2` mathematisch VORGEGEBEN!
`partitionY = (M + N + 1) // 2 - partitionX`.

**3. Binäre Suche nach der perfekten Partition:**
Wir führen die binäre Suche nach `partitionX` nur im kleineren Array durch (nehmen wir `nums1`, sodass der Suchraum $O(log(\min(M, N)$ ist)).
An jedem beliebigen `partitionX` prüfen wir, ob es GÜLTIG ist.
Es ist genau dann gültig, wenn:
- `maxLeftX <= minRightY` (Das größte Element links von X ist kleiner als das kleinste rechts von Y).
- `maxLeftY <= minRightX` (Das größte Element links von Y ist kleiner als das kleinste Element rechts von X).

Wenn `maxLeftX > minRightY`: Wir haben in `X` zu weit rechts partitioniert. Wir müssen unseren Zeiger für die binäre Suche `high` nach links verschieben!
Wenn `maxLeftY > minRightX`: Wir haben in `X` zu weit links partitioniert. Wir müssen unseren Zeiger für die binäre Suche `low` nach rechts verschieben!

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

## Schritt-für-Schritt-Anleitung

`nums1 = [1, 3, 8, 9, 15]`. `X = 5`.
`nums2 = [7, 11, 18, 19, 21, 25]`. `Y = 6`.
Gesamtanzahl der Elemente = 11 (ungerade). Zielgröße der linken Hälfte = (5 + 6 + 1) // 2 = 6.

1. **Binäre Suche 1:**
   - `low = 0, high = 5`. `partitionX = 2`. (Nimm 2 aus nums1).
   - `partitionY = 6 - 2 = 4`. (Nimm 4 aus nums2).
   - `maxLeftX = nums1[1] = 3`. `minRightX = nums1[2] = 8`.
   - `maxLeftY = nums2[3] = 19`. `minRightY = nums2[4] = 21`.
   - Überprüfung: `3 <= 21` (Wahr). `19 <= 8` (FALSCH!).
   - Da `maxLeftY > minRightX`(`19 > 8`), brauchen wir MEHR von `nums1`, um das große `19` herauszuschieben! `low = partitionX + 1 = 3`.
2. **Binäre Suche 2:**
   - `low = 3, high = 5`. `partitionX = 4`. (Nimm 4 von nums1).
   - `partitionY = 6 - 4 = 2`. (Nimm 2 von nums2).
   - `maxLeftX = nums1[3] = 9`. `minRightX = nums1[4] = 15`.
   - `maxLeftY = nums2[1] = 11`. `minRightY = nums2[2] = 18`.
   - Überprüfung: `9 <= 18` (Wahr). `11 <= 15` (Wahr!).
   - ÜBEREINSTIMMUNG GEFUNDEN!
3. **Median berechnen:**
   - Die Gesamtzahl ist ungerade. Der Median ist `max(maxLeftX, maxLeftY)`.
   - `max(9, 11) = 11`.

Das Ergebnis ist `11.0`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(log(min(M, N)$)) | $O(1)$ |
| **Schlechtester Fall** | $O(log(min(M, N)$)) | $O(1)$ |

Wir führen die binäre Suche nur auf dem kleineren Array durch. Somit ist der Suchraum durch \min(M, N) begrenzt, was zu einer Zeitkomplexität von genau $O(log(\min(M, N)$)) führt.
Es werden keine neuen Arrays oder Rekursionsstapel erstellt. Die Platzkomplexität beträgt streng $O(1)$.

## Varianten & Optimierungen

- **K-tes Element zweier sortierter Arrays:** Das Ermitteln des Medians ist im Grunde nichts anderes als das Ermitteln des K-ten Elements, wobei K = (M+N)/2 ist. Man kann genau denselben Partitionsalgorithmus verwenden, um das K-te kleinste Element zweier sortierter Arrays zu finden, indem man lediglich die Zielgröße der linken Hälfte so anpasst, dass sie genau `K` beträgt.

## Praktische Anwendungen

- **Verteilte Datenbanken (Sharding):** Wenn ein Index auf zwei physisch getrennte Datenbankknoten aufgeteilt und dort sortiert ist, kannst du den globalen Median abfragen, ohne den gesamten Inhalt eines der beiden Shards über das Netzwerk umschichten zu müssen! Du musst nur $O(\log N)$ Mal hin und her pingen, um die Partitionsgrenze zu ermitteln.

## Verwandte Algorithmen in cOde(n)

- **[searching_01 – Binäre Suche](../searching/search_01_binary-search.md)** — Der grundlegende Kernmechanismus des Algorithmus.
- **[dc_03 – K-kleinstes Element (Quickselect)](dc_03_kth-smallest-quickselect.md)** — Ermittlung des Medians bzw. des k-ten Elements eines einzelnen UNSORTIERTEN Arrays in $O(N)$ Zeit.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
