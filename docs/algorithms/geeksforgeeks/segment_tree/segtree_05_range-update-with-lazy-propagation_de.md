# Bereichsaktualisierung mit Lazy Propagation (Summe)

| | |
|---|---|
| **ID** | `segtree_05` |
| **Kategorie** | segment_tree |
| **Komplexität (erforderlich)** | $O(\log N)$ |
| **Schwierigkeit** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 5/10 |
| **Wikipedia** | [Segment tree (Lazy propagation)](https://en.wikipedia.org/wiki/Segment_tree) |

## Problemstellung

Standard-Segment-Trees unterstützen Punktaktualisierungen in $O(\log N)$. Wenn Sie jedoch einen gesamten Bereich von Elementen aktualisieren müssen (z. B. „Addiere 5 zu allen Elementen vom Index L bis R“), benötigt der Aufruf der Punktaktualisierungsfunktion für jedes Element $O((R - L + 1) \log N)$ Zeit, was im Schlechtesten Fall zu $O(N \log N)$ führt!
Implementieren Sie einen **Bereichsaktualisierungs-Mechanismus** (Range Update), der eine strikte Zeitkomplexität von $O(\log N)$ für massive, kontinuierliche Aktualisierungen garantiert.

**Eingabe:** Bereichsgrenzen `l` und `r` sowie ein Delta-Wert `val`, der zum Bereich addiert werden soll.
**Ausgabe:** Der Segment Tree, der in-place modifiziert wurde.

## Wann ist dies zu verwenden?

- Dies ist das absolute Nonplusultra der Verwaltung veränderbarer Arrays. Sie benötigen dies, wenn ein Array massiven Blockoperationen (Werte addieren, Werte setzen, Bits flippen) zusammen mit kontinuierlichen Bereichsabfragen unterzogen wird.

## Ansatz

**Das Problem:**
Wenn wir 5 zum Bereich `[0, 1000]` addieren, ist das Besuchen aller 1000 Blätter, um sie zu aktualisieren, zu langsam.

**Die Lösung: Lazy Propagation**
Anstatt die Blätter sofort zu aktualisieren, halten wir bei den höchstmöglichen Knoten an, die den Bereich vollständig abdecken, aktualisieren deren Gesamtsumme direkt und hinterlassen eine „Notiz“ (einen Lazy-Wert) auf ihnen, die besagt: *„Hey, meine Kinder müssen ebenfalls um 5 erhöht werden, aber ich bin gerade zu faul, es ihnen mitzuteilen.“*
Wir schieben diese Lazy-Aktualisierungen erst dann an die Kinder weiter, wenn eine zukünftige Abfrage oder Aktualisierung diese tatsächlich besuchen muss!

1. Erstellen Sie ein `lazy`-Array der gleichen Größe wie das `tree`-Array, initialisiert mit 0.
2. **Push Down:** Erstellen Sie eine Hilfsfunktion, die prüft, ob ein Knoten `v` einen Lazy-Wert besitzt. Falls ja:
   - Addieren Sie den Lazy-Wert zur tatsächlichen Summe beider Kinder. (Achtung: Wenn ein Kind 4 Elemente abdeckt, bedeutet das Addieren von 5 zum Kind, dass sich dessen Gesamtsumme um 5 x 4 = 20 erhöht. Wir müssen mit der Segmentlänge multiplizieren!).
   - Addieren Sie den Lazy-Wert zum `lazy`-Tracking-Array beider Kinder, damit diese ihn später weitergeben können.
   - Löschen Sie den Lazy-Wert von `v`.
3. **Bereichsaktualisierung:** Durchlaufen Sie den Baum genau wie bei einer Bereichsabfrage.
   - *Entscheidend:* Rufen Sie immer **Push Down** auf, bevor Sie einen Knoten verarbeiten!
   - Bei vollständiger Überlappung: Aktualisieren Sie die Summe des aktuellen Knotens (`val * length`). Addieren Sie `val` zum `lazy`-Tracker dieses Knotens. Kehren Sie zurück! (Besuchen Sie die Kinder nicht!).
   - Bei teilweiser Überlappung: Führen Sie Push Down aus, rekursieren Sie nach links und rechts und aktualisieren Sie den aktuellen Knoten basierend auf seinen Kindern.
4. **Bereichsabfrage:** Durchlaufen Sie den Baum exakt wie zuvor, aber rufen Sie IMMER **Push Down** auf, bevor Sie einen Knoten verarbeiten!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for segtree_05: Range Update with Lazy Propagation.

Build a sum-segment tree, then apply a sequence
"""


def solve(arr, n, range_updates, queries, q):
    """Sum-segment tree with lazy-propagation range updates."""
    if n == 0:
        return [0] * q
    tree = [0] * (4 * n)
    lazy = [0] * (4 * n)

    def build(node, lo, hi):
        if lo == hi:
            tree[node] = arr[lo]
            return
        mid = (lo + hi) // 2
        build(2 * node, lo, mid)
        build(2 * node + 1, mid + 1, hi)
        tree[node] = tree[2 * node] + tree[2 * node + 1]

    def apply(node, lo, hi, val):
        """Apply a pending update of `val` to this node."""
        tree[node] += val * (hi - lo + 1)
        lazy[node] += val

    def push(node, lo, hi):
        """Push pending lazy update down to children."""
        if lazy[node] != 0 and lo != hi:
            mid = (lo + hi) // 2
            apply(2 * node, lo, mid, lazy[node])
            apply(2 * node + 1, mid + 1, hi, lazy[node])
            lazy[node] = 0

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
        tree[node] = tree[2 * node] + tree[2 * node + 1]

    def query(node, lo, hi, l, r):
        if l > hi or r < lo:
            return 0
        if l <= lo and hi <= r:
            return tree[node]
        push(node, lo, hi)
        mid = (lo + hi) // 2
        return query(2 * node, lo, mid, l, r) + query(2 * node + 1, mid + 1, hi, l, r)

    build(1, 0, n - 1)
    for l, r, val in range_updates:
        update(1, 0, n - 1, l, r, val)
    out = []
    for l, r in queries:
        out.append(query(1, 0, n - 1, l, r))
    return out
```

</details>

## Durchlauf

Array: `[0, 0, 0, 0]`.
`update_range(0, 3, addend=5)`:
- Wurzel `v=1` deckt `[0, 3]` ab. Vollständige Überlappung!
- `tree[1] += 5 * 4 = 20`.
- `lazy[1] += 5`.
- **Sofortige Rückkehr!** Die Kinder (`v=2, 3`) bleiben unberührt. $O(1)$ Zeitaufwand!

`query(0, 1)`:
- Wurzel `v=1` deckt `[0, 3]` ab. Teilweise Überlappung.
- **Push Down!** `lazy[1]` ist 5.
  - Linkes Kind `v=2` deckt `[0, 1]` ab. `tree[2] += 5 * 2 = 10`. `lazy[2] = 5`.
  - Rechtes Kind `v=3` deckt `[2, 3]` ab. `tree[3] += 5 * 2 = 10`. `lazy[3] = 5`.
  - `lazy[1] = 0`.
- Rekursion linker Zweig `v=2` (`[0, 1]`):
  - Vollständige Überlappung! Rückgabe `tree[2]` (10).
- Rekursion rechter Zweig `v=3` (`[2, 3]`):
  - Keine Überlappung! Rückgabe 0.
- Ergebnis: `10 + 0 = 10`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(\log N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(\log N)$ | $O(\log N)$ |

Durch die sofortige Rückkehr bei vollständiger Überlappung benötigen Bereichsaktualisierungen strikt $O(\log N)$ Zeit, was exakt der Komplexität von Bereichsabfragen entspricht!
Die Platzkomplexität beträgt $O(N)$ für das zusätzliche `lazy`-Array.

## Varianten & Optimierungen

- **Zuweisungsaktualisierungen:** Anstatt `+= delta` müssen Sie möglicherweise `arr[L...R] = val` strikt setzen. Die Logik der Lazy Propagation ist identisch, außer dass Sie beim Push Down den Lazy-Wert des Kindes *überschreiben*, anstatt ihn zu addieren (`lazy[v*2] = lazy[v]`), und Sie den Baumwert des Kindes *überschreiben* (`tree[v*2] = lazy[v] * length`). Sie benötigen zudem ein spezielles Flag (wie `lazy != None`), um zwischen „Setze auf 0“ und „Keine ausstehende Aktualisierung“ zu unterscheiden.

## Anwendungen in der Praxis

- **Kalendersysteme:** Das Buchen eines Zeitblocks setzt das Verfügbarkeits-Array `[start_date, end_date]` in $O(\log N)$ Zeit auf `False`.

## Verwandte Algorithmen in cOde(n)

- **[segtree_06 - Range Min Lazy Update](segtree_06_range-min-with-lazy-updates.md)** — Die exakt gleiche Logik, angepasst für Minimum-Segment-Trees.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*