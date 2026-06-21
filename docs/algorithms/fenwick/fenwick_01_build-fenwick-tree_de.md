# Fenwick Tree (Binary Indexed Tree) erstellen

| | |
|---|---|
| **ID** | `fenwick_01` |
| **Kategorie** | fenwick |
| **Komplexität (erforderlich)** | $O(N)$ oder $O(N \log N)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **Wikipedia** | [Fenwick tree](https://en.wikipedia.org/wiki/Fenwick_tree) |

## Problemstellung

Gegeben sei ein Array `arr` mit N Ganzzahlen. Konstruieren Sie einen **Fenwick Tree** (auch bekannt als Binary Indexed Tree oder BIT).
Ein Fenwick Tree ist ein 1-indiziertes Array `BIT`, bei dem jedes Element die Summe eines bestimmten Bereichs von Elementen des ursprünglichen Arrays speichert. Diese Struktur ermöglicht sowohl das Aktualisieren von Elementen als auch die Berechnung von Präfixsummen in $O(\log N)$ Zeit.
Sie müssen dieses `BIT`-Array aus dem gegebenen `arr` konstruieren.

**Eingabe:** Ein Array von Ganzzahlen `arr` der Größe N.
**Ausgabe:** Ein Array `BIT` der Größe N + 1, das den konstruierten Fenwick Tree repräsentiert.

## Wann man ihn verwendet

- Wenn Sie ein Array haben, das häufige Elementaktualisierungen erfährt (z. B. `arr[i] += 5`) und Sie häufig die Summe der Elemente von Index 0 bis Index `i` abfragen müssen.
- Fenwick Trees sind wesentlich einfacher zu implementieren und verbrauchen weniger Speicher als Segment Trees, sind jedoch etwas weniger flexibel (sie handhaben kumulative Summen problemlos, haben aber Schwierigkeiten mit Bereichsmaxima).

## Ansatz

Ein Fenwick Tree basiert vollständig auf binärer Bit-Manipulation.
Die Kernidee: Jede Ganzzahl kann als Summe von Zweierpotenzen dargestellt werden (ihre Binärdarstellung). Ähnlich kann eine kumulative Häufigkeit als Summe von Teilhäufigkeiten dargestellt werden.
In einem BIT ist der Index `i` für einen Bereich von Elementen verantwortlich, der bei `i` endet. Die *Länge* dieses Bereichs entspricht exakt dem **Wert des niedrigsten gesetzten Bits (LSB)** in der Binärdarstellung von `i`.
- Index `12` ist binär `1100`. Das niedrigste gesetzte Bit ist `0100` (was dezimal 4 entspricht). Daher speichert `BIT[12]` die Summe der letzten 4 Elemente, die bei Index 12 enden (d. h. die Elemente 9, 10, 11, 12).

**Aufbau des Baums:**
Der naive Weg, ihn zu bauen, besteht darin, mit einem `BIT`-Array aus Nullen zu beginnen und für jedes Element `arr[i]` die `update`-Funktion aufzurufen. Dies benötigt $O(N \log N)$ Zeit.

**Die $O(N)$-Optimierung:**
Wir können den Baum in strikt $O(N)$ Zeit aufbauen!
1. Initialisieren Sie ein 1-indiziertes Array `BIT` der Größe N+1.
2. Kopieren Sie alle Elemente von `arr` (welches 0-indiziert ist) direkt in `BIT` (welches 1-indiziert ist).
3. Iterieren Sie `i` von 1 bis N.
4. An Index `i` enthält `BIT[i]` bereits die korrekte Summe für seinen Bereich. Wir müssen diese Summe an den *nächsten* Knoten weitergeben, der für `i` verantwortlich ist.
5. Der unmittelbare Elternknoten von `i` im BIT ist mathematisch `parent = i + (i & -i)`.
6. Wenn `parent <= N`, addieren Sie einfach `BIT[i]` zu `BIT[parent]`!

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

## Durchlauf

`arr = [3, 2, -1, 6, 5, 4]`, N = 6.
Initialisiere `BIT`: `[0, 3, 2, -1, 6, 5, 4]`.

**i = 1:** `BIT[1]` ist 3. Elternknoten = `1 + (1 & -1)` = `1 + 1` = `2`.
`BIT[2] += BIT[1]` -> 2 + 3 = 5.
`BIT = [0, 3, 5, -1, 6, 5, 4]`.

**i = 2:** `BIT[2]` ist 5. Elternknoten = `2 + (2 & -2)` = `2 + 2` = `4`.
`BIT[4] += BIT[2]` -> 6 + 5 = 11.
`BIT = [0, 3, 5, -1, 11, 5, 4]`.

**i = 3:** `BIT[3]` ist -1. Elternknoten = `3 + (3 & -3)` = `3 + 1` = `4`.
`BIT[4] += BIT[3]` -> 11 + (-1) = 10.
`BIT = [0, 3, 5, -1, 10, 5, 4]`.

**i = 4:** `BIT[4]` ist 10. Elternknoten = `4 + (4 & -4)` = `4 + 4` = `8`.
`8 > N(6)`. Nichts tun.

**i = 5:** `BIT[5]` ist 5. Elternknoten = `5 + (5 & -5)` = `5 + 1` = `6`.
`BIT[6] += BIT[5]` -> 4 + 5 = 9.
`BIT = [0, 3, 5, -1, 10, 5, 9]`.

**i = 6:** `BIT[6]` ist 9. Elternknoten = `6 + (6 & -6)` = `6 + 2` = `8`.
`8 > N`. Nichts tun.

Finales `BIT` = `[0, 3, 5, -1, 10, 5, 9]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Die optimierte Konstruktion besucht jeden Index genau einmal und führt eine bitweise $O(1)$-Berechnung sowie eine Addition durch. Die Gesamtlaufzeit beträgt strikt $O(N)$.
Die Platzkomplexität beträgt $O(N)$, um das BIT-Array der Größe N+1 zu speichern.

## Varianten & Optimierungen

- **Segment Tree Konstruktion:** Wenn Sie tatsächlich Bereichsminima/-maxima anstelle von Summen benötigen, müssen Sie einen Segment Tree bauen. Segment Trees lassen sich ebenfalls in $O(N)$ Zeit aufbauen, erfordern jedoch einen Speicher-Overhead von $O(4N)$ im Vergleich zu $O(N)$ beim Fenwick Tree.

## Anwendungen in der Praxis

- **Datenbank-Analytik:** Unterstützung von "Rolling Sum"-Spalten in OLAP-Datenbanken, in denen Zeilen häufig aktualisiert werden.
- **Datenkompression:** Pflege dynamischer Häufigkeitstabellen für die adaptive arithmetische Kodierung.

## Verwandte Algorithmen in cOde(n)

- **[fenwick_02 - Range Sum Query](fenwick_02_range-sum-query-bit.md)** — Wie man das gerade erstellte Array verwendet, um Präfixsummen-Abfragen zu beantworten.
- **[segment_tree_01 - Segment Tree Build](../segment_tree/segtree_01_point-update-range-query.md)** — Die mächtigere, vielseitigere Alternative zu Fenwick Trees.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*