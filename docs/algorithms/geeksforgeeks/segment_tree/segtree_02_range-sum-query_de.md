# Range Sum Query

| | |
|---|---|
| **ID** | `segtree_02` |
| **Category** | segment_tree |
| **Complexity (required)** | $O(\log N)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) |

## Problem statement

Gegeben ist ein Segment Tree, der für ein spezifisches Array `arr` konstruiert wurde. Führen Sie eine Range Sum Query durch.
Berechnen Sie die Summe der Elemente von `arr` zwischen den Indizes `left` und `right` (einschließlich): `sum(arr[left...right])`.
Sie müssen das Ergebnis in strikter $O(\log N)$-Zeit zurückgeben, indem Sie den vorab aufgebauten Segment Tree durchlaufen.

**Input:** Zwei Ganzzahlen `l` und `r`, die die Grenzen der Anfrage darstellen.
**Output:** Eine Ganzzahl, die die Summe repräsentiert.

## Wann man es verwendet

- Wenn Sie aggregierte Daten (Summe, Minimum, Maximum, XOR) aus einem beliebigen Teilsegment eines massiven Arrays extrahieren müssen und sich dieses Array in Zukunft ändern könnte.

## Ansatz

Ein Knoten in einem Segment Tree ist für ein spezifisches Segment `[tl, tr]` (tree left, tree right) verantwortlich.
Wenn wir eine Anfrage für einen Bereich `[l, r]` stellen, beginnen wir am Wurzelknoten (der `[0, N-1]` abdeckt) und durchlaufen den Baum rekursiv.

Bei jedem Knoten `v`, der `[tl, tr]` abdeckt, gibt es drei Möglichkeiten:
1. **Keine Überschneidung:** Das Segment des Knotens `[tl, tr]` liegt vollständig *außerhalb* des Anfragebereichs `[l, r]`.
   - Aktion: Dieser Knoten ist nutzlos. Geben Sie `0` zurück (das neutrale Element für die Summe).
2. **Vollständige Überschneidung:** Das Segment des Knotens `[tl, tr]` liegt vollständig *innerhalb* des Anfragebereichs `[l, r]`!
   - Aktion: Das vorab berechnete Ergebnis dieses Knotens ist perfekt relevant! Wir müssen nicht tiefer in den Baum absteigen. Geben Sie sofort `tree[v]` zurück. Hier liegt der massive Geschwindigkeitsvorteil von $O(\log N)$!
3. **Partielle Überschneidung:** Das Segment des Knotens überschneidet sich mit dem Anfragebereich, liegt aber nicht vollständig darin.
   - Aktion: Wir müssen die Anfrage aufteilen und beide Kinder abfragen!
   - Rekursion auf das linke Kind (`2*v`), das `[tl, tm]` abdeckt.
   - Rekursion auf das rechte Kind (`2*v+1`), das `[tm+1, tr]` abdeckt.
   - Geben Sie die Summe beider rekursiven Aufrufe zurück.

*(Hinweis: Beim rekursiven Abstieg übergeben wir normalerweise `l` und `r` unverändert oder schränken sie mathematisch mittels `min`/`max` ein. Der einfachste Weg ist, `l` und `r` unverändert zu lassen und sich auf den Basisfall "Keine Überschneidung" zu verlassen, um Anfragen außerhalb der Grenzen abzufangen!).*

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for segtree_02: Range Sum Query.

Build a segment tree, then for each (l, r) return the
range sum. O(log n) per query.
"""


def solve(arr, n, queries, q):
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
            tree[node] = tree[2 * node] + tree[2 * node + 1]

    def query(node, lo, hi, l, r):
        if l > hi or r < lo:
            return 0
        if l <= lo and hi <= r:
            return tree[node]
        mid = (lo + hi) // 2
        return query(2 * node, lo, mid, l, r) + query(2 * node + 1, mid + 1, hi, l, r)

    build(1, 0, n - 1)
    out = []
    for l, r in queries:
        out.append(query(1, 0, n - 1, l, r))
    return out
```

</details>

## Durchlauf

Array: `[1, 3, 5]`. N=3. Baum deckt `[0, 2]` ab.
Anfrage: `[0, 1]`.

`_sum(v=1, tl=0, tr=2, l=0, r=1)`
- `[0, 2]` liegt nicht vollständig innerhalb von `[0, 1]`. Partielle Überschneidung!
- `tm = 1`. Rekursion links und rechts.

**Linker Zweig:** `_sum(v=2, tl=0, tr=1, l=0, r=1)`
- `[0, 1]` IST vollständig innerhalb von `[0, 1]`. Vollständige Überschneidung!
- Rückgabe `tree[2]`. (Wir wissen aus `segtree_01`, dass `tree[2]` den Wert `1 + 3 = 4` speichert).

**Rechter Zweig:** `_sum(v=3, tl=2, tr=2, l=0, r=1)`
- `l (0) > tr (2)` ist falsch. `r (1) < tl (2)` ist WAHR!
- Keine Überschneidung! Rückgabe `0`.

Kombination: `sum_left (4) + sum_right (0) = 4`.
Ergebnis: 4. ✓ *(Korrekt, 1 + 3 = 4).*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(\log N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(\log N)$ | $O(\log N)$ |

Da wir die Rekursion in dem Moment stoppen, in dem ein Knoten vollständig innerhalb des Anfragebereichs liegt, besuchen wir nie mehr als 4 Knoten pro Ebenentiefe. Die Tiefe des Baums ist log N. Daher ist die Zeitkomplexität strikt auf $O(\log N)$ begrenzt.
Die Platzkomplexität beträgt $O(\log N)$ für den rekursiven Aufruf-Stack.

## Varianten & Optimierungen

- **Einschränken des Anfragebereichs (Clamping):** Einige Implementierungen ziehen es vor, `l` und `r` beim Übergeben an die Kinder einzuschränken: `_sum(v*2, tl, tm, l, min(r, tm))`. Dies verhindert das Übergeben ungültiger Grenzen wie `l > r` vollständig und macht die `l > tr`-Prüfung überflüssig. Beide Ansätze sind funktional identisch und $O(\log N)$.
- **Iterative Anfrage:** Wenn der Baum iterativ von unten nach oben aufgebaut wurde, können Sie die Anfrage von den Blättern bis zur Wurzel in einer einfachen `while l <= r:`-Schleife durchführen, was in der Praxis deutlich schneller ist.

## Anwendungen in der Praxis

- **Finanzbuchhaltung:** Summierung des Gesamtvolumens von Transaktionen, die zwischen den Zeitstempeln T_1 und T_2 in einer Live-Datenbank stattgefunden haben, in der neue Transaktionen ständig historische Aggregationen aktualisieren.

## Verwandte Algorithmen in cOde(n)

- **[segtree_04 - Range Minimum Query](segtree_04_range-minimum-query.md)** — Die exakt gleiche Durchlaufslogik, nur dass `+` durch `min()` ersetzt wird.
- **[fenwick_02 - Query](../fenwick/fenwick_02_query.md)** — Ein Fenwick Tree erreicht dieselbe $O(\log N)$-Anfrage mittels einer wesentlich einfacheren Schleife.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*