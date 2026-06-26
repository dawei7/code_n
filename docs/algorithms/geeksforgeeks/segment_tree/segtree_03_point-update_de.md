# Point Update

| | |
|---|---|
| **ID** | `segtree_03` |
| **Kategorie** | segment_tree |
| **Komplexität (erforderlich)** | $O(\log N)$ |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) |

## Problemstellung

Gegeben sei ein konstruierter Segment Tree; implementieren Sie eine Funktion, um den Wert eines einzelnen Elements im ursprünglichen Array zu aktualisieren.
Wenn ein Element `arr[pos]` auf `new_val` geändert wird, muss der Segment Tree aktualisiert werden, um diese Änderung widerzuspiegeln.
Die Aktualisierung muss in $O(\log N)$ Zeit ausgeführt werden und dabei nur die spezifischen Baumknoten aktualisieren, die das geänderte Element enthalten.

**Eingabe:** Ein Integer `pos` (der Index im Array) und ein Integer `new_val`.
**Ausgabe:** Der Segment Tree, der in-place modifiziert wurde.

## Wann man es verwendet

- Dies ist die Operation, die Segment Trees (und Fenwick Trees) herkömmlichen Prefix-Sum-Arrays überlegen macht. Prefix-Sum-Arrays benötigen $O(1)$ für Abfragen, aber $O(N)$ für Aktualisierungen. Segment Trees benötigen $O(\log N)$ für Abfragen und $O(\log N)$ für Aktualisierungen, was das perfekte Gleichgewicht für veränderbare Daten bietet.

## Ansatz

Eine Punktaktualisierung ist im Wesentlichen eine spezialisierte Traversierung bis hinunter zu einem einzelnen Blatt.
Wenn wir `arr[pos]` aktualisieren, müssen wir den Blattknoten aktualisieren, der für `pos` verantwortlich ist. Wir müssen jedoch auch jeden Vorfahren-Knoten bis hinauf zur Wurzel aktualisieren, da deren aggregierte Werte (z. B. Summen) nun veraltet sind!

**Die Logik:**
1. Beginnen Sie am Wurzelknoten `v=1`, der den Bereich `[0, N-1]` abdeckt.
2. Prüfen Sie, ob der aktuelle Knoten ein Blatt ist (`tl == tr`).
   - Wenn ja, haben wir den exakten Knoten für `pos` erreicht! Aktualisieren Sie dessen Wert in `tree[v]` und kehren Sie zurück.
3. Wenn es kein Blatt ist, berechnen Sie `tm = (tl + tr) // 2`.
4. Bestimmen Sie, welches Kind den Index `pos` enthält:
   - Wenn `pos <= tm`, liegt der Zielindex in der linken Hälfte. Rekursion im linken Kind (`2*v`).
   - Wenn `pos > tm`, liegt der Zielindex in der rechten Hälfte. Rekursion im rechten Kind (`2*v+1`).
5. **Backtracking (Der entscheidende Schritt):** Während die Rekursion zurück zur Wurzel abgewickelt wird, muss der aktuelle Knoten `v` seinen Wert durch Zusammenführen seiner beiden Kinder neu berechnen: `tree[v] = tree[v*2] + tree[v*2+1]`. Da sich der Wert eines der Kinder gerade geändert hat, stellt dies sicher, dass die Änderung perfekt bis zur Wurzel durchschlägt!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for segtree_03: Point Update.

Apply point updates and return the resulting array.
"""


def solve(arr, n, updates, q):
    work = list(arr)
    for idx, val in updates:
        if 0 <= idx < n:
            work[idx] = val
    return work
```

</details>

## Durchlauf

Array: `[1, 3, 5]`. N=3. Baum-Array (Werte): `[0, 9, 4, 5, 1, 3]`.
Aktualisierung: `pos = 1` (der Wert `3`), `new_val = 10`.

`_update(v=1, tl=0, tr=2, pos=1, val=10)`
- `tm = 1`. `pos (1) <= tm (1)`. Gehe nach links!

`_update(v=2, tl=0, tr=1, pos=1, val=10)`
- `tm = 0`. `pos (1) > tm (0)`. Gehe nach rechts!

`_update(v=5, tl=1, tr=1, pos=1, val=10)`
- `tl == tr`! Blattknoten erreicht.
- `tree[5] = 10`. Zurückkehren.

**Zurückkehren zu `v=2`:**
- `tree[2] = tree[4] + tree[5]`
- `tree[2] = 1 + 10 = 11`. (Aktualisiert von 4 auf 11!). Zurückkehren.

**Zurückkehren zu `v=1`:**
- `tree[1] = tree[2] + tree[3]`
- `tree[1] = 11 + 5 = 16`. (Aktualisiert von 9 auf 16!). Zurückkehren.

Aktualisierung abgeschlossen! Der Pfad vom Blatt zur Wurzel wurde in 3 Schritten aktualisiert. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(\log N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(\log N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(\log N)$ | $O(\log N)$ |

Die Höhe eines perfekt balancierten Binärbaums für N Elemente ist exakt \lceil log_2 N \rceil. Wir besuchen auf dem Weg nach unten nur einen Knoten pro Ebene und aktualisieren auf dem Rückweg einen Knoten pro Ebene. Daher ist die Zeitkomplexität $O(\log N)$.
Die Platzkomplexität beträgt $O(\log N)$ für den rekursiven Aufruf-Stack.

## Varianten & Optimierungen

- **Delta-Aktualisierungen:** Anstatt `new_val` zu übergeben, haben Aktualisierungen manchmal die Form `arr[pos] += delta`. In diesem Fall addieren Sie einfach `delta` zu `tree[v]` bei jedem Schritt auf dem Weg nach unten, wodurch das Zusammenführen der Kinder auf dem Rückweg komplett entfällt! `tree[v] += delta`.
- **Iterative Aktualisierung:** In einem Bottom-up-Segment-Tree befindet sich der Blattknoten am Index `p = pos + N`. Sie aktualisieren `tree[p] = new_val`. Dann verwenden Sie einfach eine `while p > 1: p //= 2; tree[p] = tree[2*p] + tree[2*p+1]` Schleife, um in 3 Zeilen Code zur Wurzel zu gelangen!

## Praxisanwendungen

- **Bestenlisten:** Wenn sich die Punktzahl eines Spielers ändert (Punktaktualisierung), müssen die globalen Ranking-Schwellenwerte und Summen (Bereichsabfragen) sofort aktualisiert werden, ohne die Spieleserver einzufrieren.

## Verwandte Algorithmen in cOde(n)

- **[fenwick_03 - Point Update](../fenwick/fenwick_03_update.md)** — Eine wesentlich leichtere und schnellere $O(\log N)$-Aktualisierung, die jedoch strikt auf umkehrbare Operationen (wie Summe/XOR) beschränkt ist, im Gegensatz zu Segment Trees.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*