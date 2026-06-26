# Bereichs-Update, Bereichs-Abfrage (Dual BIT)

| | |
|---|---|
| **ID** | `fenwick_05` |
| **Kategorie** | fenwick |
| **Komplexität (erforderlich)** | $O(\log N)$ Abfrage/Update |
| **Schwierigkeit** | 9/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **LeetCode-Äquivalent** | (Fortgeschrittenes Competitive Programming) |

## Problemstellung

Gegeben sei ein Array der Größe N, das mit 0 initialisiert ist. Implementieren Sie eine Datenstruktur, die BEIDE der folgenden Operationen unterstützt:
1. `range_update(left, right, delta)`: Addiere `delta` zu jedem Element im inklusiven Bereich `[left, right]`.
2. `range_query(left, right)`: Gib die Summe aller Elemente im inklusiven Bereich `[left, right]` zurück.

Beide Operationen müssen in strikter $O(\log N)$-Zeit ausgeführt werden. Während ein Segment Tree mit Lazy Propagation dies auf natürliche Weise leisten kann, müssen Sie dies hier unter Verwendung von **Fenwick Trees (BITs)** erreichen, um den Speicheraufwand zu minimieren und die Geschwindigkeit durch einen kleineren konstanten Faktor zu maximieren.

**Eingabe:** Eine Sequenz von `range_update`- und `range_query`-Operationen.
**Ausgabe:** Die Ergebnisse der Bereichs-Abfragen.

## Einsatzgebiete

- In stark eingeschränkten Umgebungen des Competitive Programming, in denen ein Segment Tree zu viel Speicher verbraucht oder etwas zu langsam ist, um strikte Zeitlimits einzuhalten.
- Eine brillante Demonstration fortgeschrittener algebraischer Manipulation von Datenstrukturen.

## Ansatz

Betrachten wir die Mathematik eines Differenz-Arrays (aus `fenwick_04`).
Wenn wir `D` zum Bereich `[L, R]` addieren, sind unsere Updates im Differenz-Array `Diff[L] += D` und `Diff[R+1] -= D`.
Was passiert, wenn wir die Präfixsumme bis zum Index `X` abfragen?
Der wahre Wert des Elements `i` ist \sum_{j=1}^{i} Diff[j].
Daher ist die Präfixsumme bis `X`:
PrefixSum(X) = \sum_{i=1}^{X} \text{value}[i] = \sum_{i=1}^{X} \sum_{j=1}^{i} Diff[j]

Beachten Sie, dass Diff[1] X-mal addiert wird. Diff[2] wird (X-1)-mal addiert. Diff[i] wird (X - i + 1)-mal addiert!
Wir können diese Summe algebraisch umschreiben:
PrefixSum(X) = \sum_{i=1}^{X} Diff[i] x (X - i + 1)
PrefixSum(X) = \sum_{i=1}^{X} (Diff[i] x X + Diff[i]) - \sum_{i=1}^{X} (Diff[i] x i)
PrefixSum(X) = (X + 1) \sum_{i=1}^{X} Diff[i] - \sum_{i=1}^{X} (Diff[i] x i)

**Die Dual BIT-Erkenntnis:**
Diese Gleichung enthält zwei verschiedene Summen!
1. \sum Diff[i] — Dies ist einfach ein Standard-BIT, das das Differenz-Array verwaltet (`BIT1`)!
2. \sum (Diff[i] x i) — Dies erfordert ein **zweites BIT** (`BIT2`), das dasselbe Differenz-Array verwaltet, jedoch multipliziert mit dem Index i!

Um die Präfixsumme bis `X` abzufragen, fragen wir einfach beide BITs nach ihren Präfixsummen ab und setzen sie in die Gleichung ein:
`PrefixSum(X) = (X + 1) * BIT1.query(X) - BIT2.query(X)`

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for fenwick_05: Range Update + Range Query (BIT).

Maintain an array of n integers under repeated
"""


def solve(arr, n, range_updates, range_queries, q):
    """Range add + range sum via two BITs.

    Seed both BITs with the initial arr values so the
    range sum reflects the actual current array.
    """
    INF = n + 5
    bit1 = [0] * (n + 2)
    bit2 = [0] * (n + 2)

    def update(bit, i, delta):
        i += 1
        while i <= n + 1:
            bit[i] += delta
            i += i & -i

    def prefix(bit, i):
        i += 1
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    def range_update(l, r, val):
        update(bit1, l, val)
        if r + 1 < n:
            update(bit1, r + 1, -val)
        update(bit2, l, val * (l - 1))
        if r + 1 < n:
            update(bit2, r + 1, -val * r)

    def prefix_sum(x):
        # sum of [0, x]
        if x < 0:
            return 0
        return prefix(bit1, x) * x - prefix(bit2, x)

    # Initialize: each initial value is a point update (a
    # range update of length 1). This seeds both BITs so the
    # formula (bit1.prefix(x) * x - bit2.prefix(x)) yields
    # sum of arr[0..x] including the initial values.
    for i in range(n):
        range_update(i, i, arr[i])
    for l, r, val in range_updates:
        range_update(l, r, val)
    out = []
    for l, r in range_queries:
        out.append(prefix_sum(r) - prefix_sum(l - 1))
    return out
```

</details>

## Durchlauf

*(Konzeptionell)*
Array-Größe 5. Anfangs alles 0.
1. **Bereichs-Update [1, 3] mit +10:**
   - `L=2, R=4`. `delta=10`.
   - `BIT1`: Addiere `10` an Index 2. Addiere `-10` an Index 5.
   - `BIT2`: Addiere `10 * 2 = 20` an Index 2. Addiere `-10 * 5 = -50` an Index 5.

2. **Bereichs-Abfrage [2, 4]:** (Indizes 3 bis 5)
   - `_get_prefix_sum(5)`:
     - `BIT1` prefix(5) = `10 - 10 = 0`.
     - `BIT2` prefix(5) = `20 - 50 = -30`.
     - `Sum(5) = (5 + 1) * 0 - (-30) = 30`. (Elemente 1,2,3 erhielten +10. Gesamtsumme ist 30). ✓
   - `_get_prefix_sum(2)`:
     - `BIT1` prefix(2) = `10`.
     - `BIT2` prefix(2) = `20`.
     - `Sum(2) = (2 + 1) * 10 - 20 = 10`. (Nur Element 1 erhielt +10 bis Index 2). ✓
   - **Bereichs-Ergebnis:** `Sum(5) - Sum(2) = 30 - 10 = 20`.
   - Elemente an den Array-Indizes 2, 3, 4 sind `10, 10, 0`. Die Summe ist 20! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(\log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(\log N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(\log N)$ | $O(N)$ |

Jedes Update greift auf zwei BITs zu, was 2 x $O(\log N)$ benötigt. Jede Abfrage greift auf zwei BITs zu, was 2 x $O(\log N)$ benötigt. Somit sind alle Operationen strikt durch $O(\log N)$ begrenzt.
Die Platzkomplexität beträgt $O(N)$ für die beiden Arrays, was deutlich geringer ist als der Speicherbedarf für einen Lazy Segment Tree.

## Varianten & Optimierungen

- **Segment Tree mit Lazy Propagation:** Wie erwähnt, die alternative Struktur. Lazy Segment Trees sind konzeptionell einfacher und lassen sich auf Max/Min-Abfragen erweitern, während dieser Dual BIT-Trick NUR für Summierungen funktioniert.

## Anwendungen in der Praxis

- **Hochfrequenzhandel:** Verwaltung von aggregierten Limits bei gestaffelten Preisstrukturen, bei denen kontinuierliche Preisblöcke gleichzeitig aktualisiert werden und Risikosysteme eine Abfragelatenz im Nanosekundenbereich erfordern.

## Verwandte Algorithmen in cOde(n)

- **[fenwick_04 - Range Update Point Query](fenwick_04_range-update-point-query-bit.md)** — Die Grundlage der hier verwendeten Differenz-Array-Mathematik.
- **[segtree_04 - Lazy Propagation](../segment_tree/segtree_04_lazy-propagation.md)** — Der Segment Tree-Ansatz zur Lösung genau dieses Problems.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Competitive Programming verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*