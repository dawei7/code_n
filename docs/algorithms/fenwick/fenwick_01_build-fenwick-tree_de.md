# Fenwick Tree erstellen (binärer indizierter Baum)

| | |
|---|---|
| **ID** | `fenwick_01` |
| **Kategorie** | fenwick |
| **Komplexität (erforderlich)** | $O(N)$ oder $O(N \log N)$ |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **Wikipedia** | [Fenwick Tree](https://en.wikipedia.org/wiki/Fenwick_tree) |

## Aufgabenstellung

Gegeben sei ein Array `arr` mit N ganzen Zahlen. Konstruieren Sie einen **Fenwick Tree** (auch bekannt als binär indizierter Baum oder BIT). 
Ein Fenwick Tree ist ein 1-indiziertes Array `BIT`, in dem jedes Element die Summe eines bestimmten Bereichs von Elementen aus dem ursprünglichen Array speichert. Diese Struktur ermöglicht sowohl die Aktualisierung von Elementen als auch die Berechnung von Präfixsummen in $O(\log N)$ Zeit.
Sie müssen dieses `BIT`-Array aus dem gegebenen `arr` konstruieren.

**Eingabe:** Ein Array von ganzen Zahlen `arr` der Größe N.
**Ausgabe:** Ein Array `BIT` der Größe N + 1, das den konstruierten Fenwick Tree darstellt.

## Wann man ihn verwendet

- Wenn Sie ein Array haben, dessen Elemente häufig aktualisiert werden (z. B. `arr[i] += 5`), und Sie häufig die Summe der Elemente vom Index 0 bis zum Index `i` abfragen müssen. 
- Fenwick Trees sind wesentlich einfacher zu programmieren und benötigen weniger Speicher als Segment Trees, sind jedoch etwas weniger flexibel (sie können kumulative Summen problemlos verarbeiten, haben jedoch Schwierigkeiten mit Bereichsmaxima).

## Vorgehensweise

Ein Fenwick Tree basiert vollständig auf binärer Bitmanipulation. 
Die Kernidee: Jede ganze Zahl lässt sich als Summe von Zweierpotenzen darstellen (ihre binäre Darstellung). Analog dazu lässt sich eine kumulative Häufigkeit als Summe von Teilhäufigkeiten darstellen.
In einem BIT ist der Index `i` für einen Bereich von Elementen zuständig, der bei `i` endet. Die *Länge* dieses Bereichs entspricht genau dem **Wert des niedrigstwertigen Bits (LSB)** in der binären Darstellung von `i`.
- Der Index `12` lautet binär `1100`. Das niedrigste gesetzte Bit ist `0100` (was im Dezimalsystem 4 entspricht). Daher speichert `BIT[12]` die Summe der letzten 4 Elemente, die am Index 12 enden (d. h. die Elemente 9, 10, 11, 12).

**Aufbau des Baums:**
Die naive Vorgehensweise beim Aufbau besteht darin, mit einem `BIT`-Array aus Nullen zu beginnen und für jedes Element `arr[i]` die Funktion `update` aufzurufen. Dies benötigt $O(N \log N)$ Zeit.

**Die $O(N)$-Optimierung:**
Wir können den Baum in streng $O(N)$ Zeit aufbauen!
1. Initialisiere ein Array `BIT` mit 1-Indizierung und der Größe N+1.
2. Kopiere alle Elemente von `arr` (das 0-indiziert ist) direkt in `BIT` (das 1-indiziert ist).
3. Durchlaufe `i` von 1 bis N.
4. Am Index `i` enthält `BIT[i]` derzeit die korrekte Summe für seinen Bereich. Wir müssen diese Summe an den *nächsten* Knoten weitergeben, der für `i` zuständig ist.
5. Der unmittelbare Elternknoten von `i` im BIT ist mathematisch gesehen `parent = i + (i & -i)`.
6. Wenn `parent <= N`, addiere einfach `BIT[i]` zu `BIT[parent]`!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for fenwick_01: Build Fenwick Tree.

bit[i] = sum of arr[i - 2^k + 1 .. i] where k is the
number of trailing zeros in i.
"""


def solve(arr, n):
    if n == 0:
        return []
    bit = [0] * (n + 1)
    for i in range(1, n + 1):
        bit[i] = arr[i - 1]
    for i in range(1, n + 1):
        j = i + (i & -i)
        if j <= n:
            bit[j] += bit[i]
    return bit
```

</details>

## Schritt-für-Schritt-Anleitung

`arr = [3, 2, -1, 6, 5, 4]`, N = 6.
Initialisiere `BIT`: `[0, 3, 2, -1, 6, 5, 4]`.

**i = 1:** `BIT[1]` ist 3. Elternteil = `1 + (1 & -1)` = `1 + 1` = `2`.
`BIT[2] += BIT[1]` -> 2 + 3 = 5.
`BIT = [0, 3, 5, -1, 6, 5, 4]`.

**i = 2:** `BIT[2]` ist 5. Elternteil = `2 + (2 & -2)` = `2 + 2` = `4`.
`BIT[4] += BIT[2]` -> 6 + 5 = 11.
`BIT = [0, 3, 5, -1, 11, 5, 4]`.

**i = 3:** `BIT[3]` ist -1. Elternteil = `3 + (3 & -3)` = `3 + 1` = `4`.
`BIT[4] += BIT[3]` -> 11 + (-1) = 10.
`BIT = [0, 3, 5, -1, 10, 5, 4]`.

**i = 4:** `BIT[4]` ist 10. Elternteil = `4 + (4 & -4)` = `4 + 4` = `8`.
`8 > N(6)`. Keine Aktion.

**i = 5:** `BIT[5]` ist 5. Elternteil = `5 + (5 & -5)` = `5 + 1` = `6`.
`BIT[6] += BIT[5]` -> 4 + 5 = 9.
`BIT = [0, 3, 5, -1, 10, 5, 9]`.

**i = 6:** `BIT[6]` ist 9. Elternteil = `6 + (6 & -6)` = `6 + 2` = `8`.
`8 > N`. Nichts tun.

Endgültiges `BIT` = `[0, 3, 5, -1, 10, 5, 9]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(N)$ |
| **Schlimmster Fall** | $O(N)$ | $O(N)$ |

Bei der optimierten Konstruktion wird jeder Index genau einmal besucht, wobei jeweils eine $O(1)$ bitweise Berechnung und Addition durchgeführt wird. Die Gesamtzeit beträgt streng $O(N)$.
Die Platzkomplexität beträgt $O(N)$, um das BIT-Array der Größe N+1 zu speichern.

## Varianten & Optimierungen

- **Segment Tree-Konstruktion:** Wenn Sie tatsächlich statt bloßer Summen die Minimal- und Maximalwerte eines Bereichs benötigen, müssen Sie einen Segment Tree erstellen. Segment Trees werden ebenfalls in $O(N)$ Zeit aufgebaut, erfordern jedoch im Vergleich zum Fenwick Tree $O(N)$ einen Speicher-Overhead von $O(4N)$.

## Praktische Anwendungen

- **Datenbankanalyse:** Unterstützung von „Rolling-Sum“-Spalten in OLAP-Datenbanken, in denen Zeilen häufig aktualisiert werden.
- **Datenkompression:** Pflege dynamischer Häufigkeitstabellen für die adaptive arithmetische Kodierung.

## Verwandte Algorithmen in cOde(n)

- **[fenwick_02 – Bereichssummenabfrage](fenwick_02_range-sum-query-bit.md)** – Wie man das soeben erstellte Array tatsächlich nutzt, um Präfixsummenabfragen zu beantworten.
- **[segment_tree_01 – Aufbau eines Segmentbaums](../segment_tree/segtree_01_point-update-range-query.md)** – Die aufwendigere, aber vielseitigere Alternative zu Fenwick-Bäumen.

---

*Diese Dokumentation ist ein Originalbeitrag für cOde(n),
der sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
