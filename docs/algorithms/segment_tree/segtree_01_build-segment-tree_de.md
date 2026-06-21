# Segment Tree aufbauen

| | |
|---|---|
| **ID** | `segtree_01` |
| **Kategorie** | segment_tree |
| **Komplexität (erforderlich)** | $O(N)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **Wikipedia** | [Segment tree](https://en.wikipedia.org/wiki/Segment_tree) |

## Problemstellung

Gegeben sei ein Array `arr` der Größe N. Konstruieren Sie einen **Segment Tree**, um schnelle $O(\log N)$ Bereichsabfragen (wie Summe, Minimum oder Maximum über ein Teilarray) sowie $O(\log N)$ Punktaktualisierungen zu ermöglichen.
Sie müssen die Funktion `build()` implementieren, die das interne Baum-Array aus dem ursprünglichen Eingabe-Array in $O(N)$ Zeit initialisiert.

**Eingabe:** Ein Integer-Array `arr`.
**Ausgabe:** Ein internes Array `tree`, das den konstruierten Segment Tree repräsentiert.

## Wann man ihn verwendet

- Segment Trees sind der unangefochtene König für veränderbare Bereichsabfragen.
- Verwenden Sie ihn, wenn Sie ein Array haben, das häufigen **Aktualisierungen** unterliegt und Sie gleichzeitig häufige **Bereichsabfragen** beantworten müssen (z. B. "Was ist die Summe vom Index L bis R?").
- (Wenn das Array *unveränderlich* ist, sind Präfixsummen-Arrays oder Sparse Tables besser geeignet. Wenn Sie nur Punktaktualisierungen und Summenabfragen benötigen, sind Fenwick Trees einfacher zu implementieren. Segment Trees können *alles*.)

## Ansatz

Ein Segment Tree ist ein perfekt balancierter Binärbaum.
- Der **Wurzelknoten** repräsentiert das gesamte Array `arr[0...N-1]`.
- Jeder interne Knoten repräsentiert das zusammengeführte Ergebnis seiner beiden Kinder.
- Das **linke Kind** repräsentiert die erste Hälfte: `arr[0...mid]`.
- Das **rechte Kind** repräsentiert die zweite Hälfte: `arr[mid+1...N-1]`.
- Die **Blattknoten** repräsentieren die einzelnen Elemente des Arrays: `arr[i]`.

**Array-Repräsentation:**
Anstatt `Node`-Objekte mit Pointern zu erstellen, bilden wir den Binärbaum perfekt auf ein 1D-Array ab (genau wie bei einem Binary Heap)!
- Die Wurzel befindet sich am Index `1` (1-basiert für einfachere Berechnungen).
- Das linke Kind des Knotens `v` befindet sich am Index `2 * v`.
- Das rechte Kind des Knotens `v` befindet sich am Index `2 * v + 1`.
- Um einen Baum mit N Blättern sicher zu speichern, muss das Baum-Array eine Größe von `4 * N` haben.

**Aufbau (Post-Order-Traversierung):**
Wir verwenden eine Divide-and-Conquer-Rekursion.
1. Starten Sie an der Wurzel (`v=1`), die `[0, N-1]` abdeckt.
2. Finden Sie die Mitte `mid`.
3. Bauen Sie rekursiv das linke Kind (`2*v`) auf, das `[0, mid]` abdeckt.
4. Bauen Sie rekursiv das rechte Kind (`2*v+1`) auf, das `[mid+1, N-1]` abdeckt.
5. Sobald die Kinder aufgebaut sind, führt der aktuelle Knoten `v` einfach deren Ergebnisse zusammen (z. B. `tree[v] = tree[2*v] + tree[2*v+1]`).
6. Basisfall: Wenn `left == right`, befinden wir uns an einem Blatt. Setzen Sie einfach `tree[v] = arr[left]`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for segtree_01: Build Segment Tree.

Build a sum-segment tree bottom-up and return as a flat list.
"""


def solve(arr, n):
    if n == 0:
        return []
    tree = [0] * (4 * n)

    def build(node, lo, hi):
        if lo == hi:
            tree[node] = arr[lo]
        else:
            mid = (lo + hi) // 2
            build(2 * node, lo, mid)
            build(2 * node + 1, mid + 1, hi)
            tree[node] = tree[2 * node] + tree[2 * node + 1]

    build(1, 0, n - 1)
    return tree
```

</details>

## Durchlauf

`arr = [1, 3, 5]`. N=3. Baumgröße = 12.
Wurzel `v=1` deckt `[0, 2]` ab. `mid = 1`.

- **Linker Zweig `v=2` deckt `[0, 1]` ab. `mid = 0`.**
  - Linker Zweig `v=4` deckt `[0, 0]` ab. Blatt! `tree[4] = arr[0] = 1`.
  - Rechter Zweig `v=5` deckt `[1, 1]` ab. Blatt! `tree[5] = arr[1] = 3`.
  - Zusammenführung `v=2`: `tree[2] = tree[4] + tree[5] = 1 + 3 = 4`.

- **Rechter Zweig `v=3` deckt `[2, 2]` ab.**
  - Blatt! `tree[3] = arr[2] = 5`.

- **Zusammenführung Wurzel `v=1`:**
  - `tree[1] = tree[2] + tree[3] = 4 + 5 = 9`.

Finales Baum-Array (ungenutzte nachfolgende Nullen ignoriert):
`[0, 9, 4, 5, 1, 3, 0, ...]`
*(Index 0 wird nicht verwendet. Die Wurzel ist 9. Ihre Kinder sind 4 und 5. Die Kinder von 4 sind 1 und 3).* ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(N)$ |

Die Rekursion besucht jeden Knoten im Baum genau einmal. Ein perfekt balancierter Binärbaum mit N Blättern hat insgesamt 2N - 1 Knoten. Daher ist die Aufbauzeit strikt $O(N)$.
Die Platzkomplexität beträgt $O(N)$, da wir ein Array der Größe 4N allokieren.

## Varianten & Optimierungen

- **Iterativer Segment Tree:** Es ist möglich, Segment Trees iterativ von unten nach oben aufzubauen und abzufragen! Anstatt bei v=1 zu beginnen, platzieren Sie die Blätter von Index N bis 2N-1 und laufen dann rückwärts von N-1 bis 1, wobei Sie `tree[i] = tree[2*i] + tree[2*i+1]` berechnen. Dies benötigt exakt 2N Platz und vermeidet jeglichen Rekursions-Overhead! Er wird in der wettbewerbsorientierten Programmierung aufgrund seiner hohen Geschwindigkeit stark bevorzugt.

## Anwendungen in der Praxis

- **Datenbank-Indizes:** Werden konzeptionell in hierarchischen Datenbankarchitekturen für schnelle mehrdimensionale räumliche Abfragen verwendet.

## Verwandte Algorithmen in cOde(n)

- **[segtree_02 - Range Sum Query](segtree_02_range-sum-query.md)** — Die Abfrageoperation, die diesen aufgebauten Baum nutzt.
- **[fenwick_01 - Build Fenwick Tree](../fenwick/fenwick_01_build.md)** — Eine einfachere, nicht-rekursive Alternative für bestimmte Arten von Bereichsabfragen.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) erstellt wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für wettbewerbsorientierte Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*