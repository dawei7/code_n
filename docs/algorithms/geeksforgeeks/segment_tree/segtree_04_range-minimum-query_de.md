# Range Minimum Query

| | |
|---|---|
| **ID** | `segtree_04` |
| **Category** | segment_tree |
| **Complexity (required)** | $O(\log N)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 5/10 |
| **LeetCode Equivalent** | N/A (Standard Data Structure Query) |

## Problem statement

Gegeben sei ein Segment Tree, der für ein spezifisches Array `arr` konstruiert wurde. Führen Sie eine **Range Minimum Query (RMQ)** durch.
Finden Sie das kleinste Element in `arr` zwischen den Indizes `left` und `right` (einschließlich): `min(arr[left...right])`.
Sie müssen das Ergebnis in einer Zeitkomplexität von strikt $O(\log N)$ zurückgeben.

**Input:** Zwei Ganzzahlen `l` und `r`, die die Grenzen der Anfrage darstellen.
**Output:** Eine Ganzzahl, die den Minimalwert in diesem Teilsegment repräsentiert.

## Wann man es verwendet

- Dies verdeutlicht den größten Vorteil von Segment Trees gegenüber Fenwick Trees. Fenwick Trees basieren auf mathematischen Inversen (z. B. A - B). Die `min()`-Funktion besitzt keine mathematische Inverse! Daher können Fenwick Trees KEINE Range Minimum Queries durchführen. Segment Trees hingegen schon!

## Ansatz

Die Traversierungslogik ist absolut identisch mit der Range Sum Query (`segtree_02`).
Die einzigen Änderungen betreffen die **Merge-Operation** und den **Identitätswert**.

1. **Identitätswert:** Wenn eine Anfrage einen Knoten trifft, der "keine Überschneidung" (No Overlap) aufweist (der Knoten liegt vollständig außerhalb des Anfragebereichs), muss ein Wert zurückgegeben werden, der das mathematische Endergebnis *nicht beeinflusst*.
   - Für die Summe ist die Identität `0` (da X + 0 = X).
   - Für das Minimum ist die Identität `Infinity` (da \min(X, \infty) = X).
2. **Merge-Operation:** Wenn ein Knoten eine Anfrage auf seine linken und rechten Kinder aufteilt, muss er deren Ergebnisse kombinieren.
   - Für die Summe verwenden wir `+`.
   - Für das Minimum verwenden wir `min()`.

*(Hinweis: Das interne `tree`-Array muss während der `_build`-Phase ebenfalls unter Verwendung von `min(left, right)` konstruiert worden sein!)*

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for segtree_04: Range Minimum Query.

Build a min-segment tree on arr (each node stores
"""


def solve(arr, n, queries, q):
    """Range Minimum Query via segment tree."""
    if n == 0:
        return [0] * q
    tree = [0] * (4 * n)

    def build(node, lo, hi):
        if lo == hi:
            tree[node] = arr[lo]
        else:
            mid = (lo + hi) // 2
            build(2 * node, lo, mid)
            build(2 * node + 1, mid + 1, hi)
            tree[node] = min(tree[2 * node], tree[2 * node + 1])

    def query(node, lo, hi, l, r):
        if l > hi or r < lo:
            return float("inf")
        if l <= lo and hi <= r:
            return tree[node]
        mid = (lo + hi) // 2
        return min(query(2 * node, lo, mid, l, r),
                   query(2 * node + 1, mid + 1, hi, l, r))

    build(1, 0, n - 1)
    out = []
    for l, r in queries:
        out.append(query(1, 0, n - 1, l, r))
    return out
```

</details>

## Durchlauf

Array: `[8, 2, 5, 1, 9]`. N=5.
Anfrage: `[0, 2]`. (Wir erwarten als Ergebnis `min(8, 2, 5) = 2`).

Angenommen, der Baum deckt `[0, 4]` ab.
`_query(v=1, tl=0, tr=4, l=0, r=2)` -> Teilweise Überschneidung. Mid=2.
- **Linker Zweig (`[0, 2]`):** `_query(v=2, tl=0, tr=2, l=0, r=2)`
  - Vollständige Überschneidung! `l(0) <= tl(0)` und `tr(2) <= r(2)`.
  - Gibt `tree[2]` zurück. (Das vorberechnete Minimum von `[8, 2, 5]` ist `2`).
- **Rechter Zweig (`[3, 4]`):** `_query(v=3, tl=3, tr=4, l=0, r=2)`
  - Keine Überschneidung! `tl(3) > r(2)`.
  - Gibt `Infinity` zurück.

Kombination: `min(2, Infinity) = 2`.
Ergebnis: 2. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(\log N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(\log N)$ | $O(\log N)$ |

Die Traversierung schneidet an den Grenzen ab, was die maximale Anzahl an Knotenbesuchen pro Ebene auf 4 begrenzt. Die maximale Tiefe beträgt log N. Die Zeitkomplexität ist strikt $O(\log N)$.
Die Platzkomplexität beträgt $O(\log N)$ für den rekursiven Aufruf-Stack.

## Varianten & Optimierungen

- **Sparse Table:** Wenn das Array *unveränderlich* ist (keine punktuellen Updates erfolgen), kann RMQ mit einer Vorverarbeitungszeit von $O(N \log N)$ und einer strikten Abfragezeit von $O(1)$ mittels einer Sparse Table gelöst werden! Eine Sparse Table speichert das Minimum jedes Bereichs der Länge 2^k. Um einen beliebigen Bereich abzufragen, überlappt man zwei Blöcke der Länge 2^k, die den Bereich abdecken.
- **RMQ in $O(N)$ Platz / $O(1)$ Abfrage:** Es ist theoretisch möglich, RMQ in $O(1)$ Zeit mit $O(N)$ Vorverarbeitung durchzuführen, indem das Problem auf das Lowest Common Ancestor (LCA) Problem mittels eines Cartesian Tree reduziert wird und anschließend LCA mittels des Farach-Colton-und-Bender-Algorithmus auf ein eingeschränktes RMQ zurückgeführt wird. Dies ist extrem komplex und wird in einem Vorstellungsgespräch niemals erwartet.

## Anwendungen in der Praxis

- **Lowest Common Ancestor (LCA):** Wie oben erwähnt, kann das Finden des niedrigsten gemeinsamen Vorfahren in einem beliebigen Baum über eine Euler-Tour auf ein 1D-Array abgebildet werden, wodurch das Baumproblem in eine Standard-Range-Minimum-Query auf dem Array umgewandelt wird!

## Verwandte Algorithmen in cOde(n)

- **[segtree_02 - Range Sum Query](segtree_02_range-sum-query.md)** — Das grundlegende Muster unter Verwendung der Summe.
- **[segtree_05 - Lazy Propagation](segtree_05_range-update-with-lazy-propagation.md)** — Wie man massive Bereichs-Updates auf diesen Bäumen durchführt.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*