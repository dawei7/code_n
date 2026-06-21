# Range Minimum Query mit Lazy Updates

| | |
|---|---|
| **ID** | `segtree_06` |
| **Kategorie** | segment_tree |
| **Komplexität (erforderlich)** | $O(\log N)$ |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **LeetCode-Äquivalent** | [Falling Squares](https://leetcode.com/problems/falling-squares/) |

## Problemstellung

Adaptieren Sie die Lazy-Propagation-Technik für einen **Range Minimum Query** Segment Tree.
Unterstützen Sie zwei Operationen:
1. `add_range(l, r, val)`: Addiere `val` zu allen Elementen in `arr[l...r]`.
2. `query_min(l, r)`: Finde das Minimum aller Elemente in `arr[l...r]`.
Beide Operationen müssen in einer strikten Zeitkomplexität von $O(\log N)$ ausgeführt werden.

**Eingabe:** Eine Sequenz von Bereichs-Additions- und Bereichs-Abfrageoperationen.
**Ausgabe:** Die Ergebnisse der Bereichsabfragen.

## Wann man es verwendet

- Um die nuancierten Unterschiede zu verstehen, wie Lazy Propagation verschiedene Aggregationsfunktionen beeinflusst. Summen-Bäume multiplizieren den Lazy-Wert mit der Segmentlänge. Min/Max-Bäume tun dies *nicht*!

## Ansatz

Die Kernstruktur ist identisch mit `segtree_05`. Wir benötigen ein `tree`-Array, um die Minima zu speichern, und ein `lazy`-Array, um ausstehende Additionen zu speichern.

**Der entscheidende Unterschied (Pushing Down):**
Wenn ein Knoten das Segment `[0, 1000]` repräsentiert und sein aktuelles Minimum `15` ist.
Wenn wir zu jedem einzelnen Element in diesem Segment `5` addieren, was passiert mit dem Minimum?
Jedes Element erhöht sich um 5. Daher erhöht sich auch das Minimum um exakt 5! Es wird zu `20`.
Im Gegensatz zum Summen-Segment-Tree **multiplizieren wir den Lazy-Wert NICHT mit der Segmentlänge!** Der Minimalwert verschiebt sich um exakt denselben `delta`-Wert wie die Elemente selbst!

Dies macht die Lazy Propagation für Min/Max-Bäume tatsächlich *einfacher* zu implementieren als für Summen-Bäume, da man während der `_push`-Operation nicht einmal die Segmentlängen (`tm - tl + 1`) berechnen oder weitergeben muss!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for segtree_06: Range Min with Lazy Updates.

Build a min-segment tree on arr. Apply a sequence
"""


def solve(arr, n, range_updates, queries, q):
    """Min-segment tree with lazy-assignment range updates."""
    if n == 0:
        return [0] * q
    INF_VAL = 10**9
    tree = [INF_VAL] * (4 * n)
    lazy = [None] * (4 * n)   # None = no pending assignment.

    def build(node, lo, hi):
        if lo == hi:
            tree[node] = arr[lo]
            return
        mid = (lo + hi) // 2
        build(2 * node, lo, mid)
        build(2 * node + 1, mid + 1, hi)
        tree[node] = min(tree[2 * node], tree[2 * node + 1])

    def apply(node, lo, hi, val):
        """Apply a pending assignment of `val` to this node."""
        tree[node] = val
        lazy[node] = val

    def push(node, lo, hi):
        """Push pending assignment down to children."""
        if lazy[node] is not None and lo != hi:
            mid = (lo + hi) // 2
            apply(2 * node, lo, mid, lazy[node])
            apply(2 * node + 1, mid + 1, hi, lazy[node])
            lazy[node] = None

    def update(node, lo, hi, l, r, val):
        if l > hi or r < lo:
            return
        if l <= lo and hi <= r:
            apply(node, lo, hi, val)
            return
        push(node, lo, hi)
        mid = (lo + hi) // 2
        update(2 * node, lo, mid, l, r, val)
        update(2 * node + 1, mid + 1, hi, l, r, val)
        tree[node] = min(tree[2 * node], tree[2 * node + 1])

    def query(node, lo, hi, l, r):
        if l > hi or r < lo:
            return INF_VAL
        if l <= lo and hi <= r:
            return tree[node]
        push(node, lo, hi)
        mid = (lo + hi) // 2
        return min(query(2 * node, lo, mid, l, r),
                   query(2 * node + 1, mid + 1, hi, l, r))

    build(1, 0, n - 1)
    for l, r, val in range_updates:
        update(1, 0, n - 1, l, r, val)
    out = []
    for l, r in queries:
        out.append(query(1, 0, n - 1, l, r))
    return out
```

</details>

## Walk-through

Array: `[10, 20, 30]`. Der Baum deckt `[0, 2]` ab. Das Minimum der Wurzel ist `10`.
`update_range(0, 2, addend=5)`:
- Wurzel `v=1` deckt `[0, 2]` ab. Vollständige Überlappung!
- `tree[1] += 5`. (Das Minimum ist jetzt 15).
- `lazy[1] += 5`.
- Sofortige Rückkehr.

`query_min(1, 2)`:
- Wurzel `v=1`. Teilweise Überlappung.
- **Push Down!** `lazy[1]` ist 5.
  - Linkes Kind (deckt `[0, 1]` ab, altes Minimum `10`): `tree[2] += 5 = 15`. `lazy[2] = 5`.
  - Rechtes Kind (deckt `[2, 2]` ab, altes Minimum `30`): `tree[3] += 5 = 35`. `lazy[3] = 5`.
  - `lazy[1] = 0`.
- Rekursion nach links `[0, 1]`: Teilweise Überlappung.
  - **Push Down!** `lazy[2]` ist 5.
    - Blatt `0` (Wert `10`): `tree[4] += 5 = 15`.
    - Blatt `1` (Wert `20`): `tree[5] += 5 = 25`.
  - ... Gibt letztendlich `tree[5] = 25` zurück.
- Rekursion nach rechts `[2, 2]`: Vollständige Überlappung.
  - Gibt `tree[3] = 35` zurück.
- Zusammenführung: `min(25, 35) = 25`. ✓

*(Das Array ist konzeptionell `[15, 25, 35]`. Das Minimum der Indizes 1 und 2 ist tatsächlich 25).*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(\log N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(\log N)$ | $O(N)$ |

Strikte $O(\log N)$ für sowohl Abfragen als auch Bereichs-Updates.

## Varianten & Optimierungen

- **Zuweisungs-Updates (Set Range):** Wenn das Update `set_range(l, r, val)` lautet, wird `tree[v]` einfach zu `val` (da das Minimum eines Arrays, in dem jedes Element identisch ist, einfach dieses Element selbst ist!).

## Anwendungen in der Praxis

- **Ressourcenallokation:** Verwaltung eines Zeitplans für verfügbare CPU-Kerne. Wenn ein Job geplant wird, der C Kerne von Zeit T_1 bis T_2 belegt, führt man eine Bereichssubtraktion durch. Eine Abfrage nach den maximal verfügbaren Kernen in einem Zeitrahmen ist eine Range Maximum Query.

## Verwandte Algorithmen in cOde(n)

- **[segtree_05 - Lazy Propagation Sum](segtree_05_range-update-with-lazy-propagation.md)** — Erklärt die Kernphilosophie der verzögerten Aktualisierung (Lazy Tracking).

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*