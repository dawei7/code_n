# Range Sum Query (Point Update)

| | |
|---|---|
| **ID** | `fenwick_02` |
| **Kategorie** | fenwick |
| **Komplexität (erforderlich)** | $O(\log N)$ Query, $O(\log N)$ Update |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [Range Sum Query - Mutable](https://leetcode.com/problems/range-sum-query-mutable/) |

## Problemstellung

Gegeben ist ein Array `arr` und dessen vorkonstruierter Fenwick Tree (BIT). Implementieren Sie zwei Operationen:
1. `update(index, value)`: Aktualisieren Sie das ursprüngliche Array so, dass `arr[index] = value` gilt.
2. `query(left, right)`: Geben Sie die Summe der Elemente in `arr` vom Index `left` bis `right` (einschließlich) zurück.

Sie müssen beide Operationen in strikter $O(\log N)$-Zeit ausführen.

**Eingabe:** Ein bereits aufgebautes `BIT`-Array sowie eine Sequenz von `update`- und `query`-Operationen.
**Ausgabe:** Das Ergebnis der `query`-Operationen.

## Wann man es verwendet

- Wenn sich Array-Elemente ständig ändern (mutieren) und Sie kontinuierlich die Summe eines Teil-Arrays abfragen müssen.
- Ein Standard-Präfixsummen-Array (`sum[i] = sum[i-1] + arr[i]`) beantwortet Anfragen in $O(1)$, aber das Aktualisieren eines einzelnen Elements benötigt $O(N)$, da das gesamte Präfix-Array neu geschrieben werden muss! Der Fenwick Tree gleicht dies perfekt aus.

## Ansatz

**Punkt-Update:**
Wenn das ursprüngliche Array `arr` am Index `i` seinen Wert ändert, setzen wir den Wert im BIT nicht direkt. Wir berechnen das *Delta* (die Differenz) zwischen dem neuen Wert und dem alten Wert.
Wir müssen dieses `delta` zu `BIT[i]` addieren und zu jedem Elternknoten im BIT, der für `i` verantwortlich ist!
Um den Baum zu allen verantwortlichen Elternknoten hinaufzugehen, verwenden wir die Regel: `index = index + (index & -index)`.
Wir führen die Schleife aus, bis der Index die Größe des BIT überschreitet.

**Präfixsummen-Abfrage:**
Um die Summe von 0 bis i zu finden, beginnen wir bei `BIT[i]` (welches die Summe eines spezifischen Abschnitts des Arrays enthält, der bei i endet).
Um die verbleibenden Abschnitte zu erhalten, entfernen wir das niedrigste gesetzte Bit, um den vorherigen Abschnitt zu finden: `index = index - (index & -index)`.
Wir akkumulieren diese Werte und führen die Schleife aus, bis der Index 0 erreicht.

**Bereichsabfrage [left, right]:**
Genau wie bei Standard-Präfixsummen-Arrays ist die Summe von `[left, right]` einfach:
`PrefixSum(right) - PrefixSum(left - 1)`.

*(Denken Sie daran: Der BIT ist 1-indiziert, während das ursprüngliche Array normalerweise 0-indiziert ist. Addieren Sie immer 1 zum Array-Index, bevor Sie ihn an die BIT-Operationen übergeben!)*

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for fenwick_02: Range Sum Query (BIT).

Build a BIT, apply updates, then answer each range-sum query.
"""


def solve(arr, n, updates, queries, q):
    if n == 0:
        return [0] * q
    bit = [0] * (n + 1)
    for i in range(1, n + 1):
        bit[i] = arr[i - 1]
    for i in range(1, n + 1):
        j = i + (i & -i)
        if j <= n:
            bit[j] += bit[i]

    def update(i, delta):
        i += 1
        while i <= n:
            bit[i] += delta
            i += i & -i

    work = list(arr)
    for idx, val in updates:
        delta = val - work[idx]
        work[idx] = val
        update(idx, delta)

    out = []
    for l, r in queries:
        def prefix(i):
            s = 0
            i += 1
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s
        out.append(prefix(r) - (prefix(l - 1) if l > 0 else 0))
    return out
```

</details>

## Durchlauf

`arr = [3, 2, -1, 6]`. BIT ist `[0, 3, 5, -1, 10]`.

**1. Abfrage Bereich [0, 2]:**
- Wir benötigen `_query_prefix(2 + 1)` - `_query_prefix(0)`.
- `_query_prefix(3)`:
  - `total += BIT[3]` (-1). `total = -1`.
  - `i = 3 - (3 & -3) = 3 - 1 = 2`.
  - `total += BIT[2]` (5). `total = 4`.
  - `i = 2 - (2 & -2) = 2 - 2 = 0`. Schleife endet. Rückgabe 4.
- Summe ist 4 - 0 = 4. ✓ (3 + 2 - 1 = 4).

**2. Update(index 1, value 5):**
- Altes `arr[1]` ist 2. Neu ist 5. `delta = 3`.
- `_add(1 + 1, 3)` -> `_add(2, 3)`.
  - `BIT[2] += 3` -> 5 + 3 = 8.
  - `i = 2 + (2 & -2) = 4`.
  - `BIT[4] += 3` -> 10 + 3 = 13.
  - `i = 4 + 4 = 8`. 8 > 4. Schleife endet.
- BIT ist nun `[0, 3, 8, -1, 13]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(\log N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(\log N)$ | $O(N)$ |

Die Anzahl der gesetzten Bits in einem Index i bestimmt die Anzahl der Iterationen in den `while`-Schleifen. Der maximale Index ist N. Eine Ganzzahl N hat höchstens ~= log_2(N) Bits. Daher erfordert das Traversieren des Baumes nach oben oder unten strikt begrenzte $O(\log N)$-Schritte.
Die Platzkomplexität beträgt $O(N)$ für die Speicherung des Baumes.

## Varianten & Optimierungen

- **Segment Tree:** Ein Segment Tree benötigt die gleiche $O(\log N)$-Zeit, erlaubt es Ihnen jedoch, Bereiche für Maximum, Minimum, GCD und beliebige benutzerdefinierte assoziative Funktionen abzufragen. Der Fenwick Tree funktioniert NUR perfekt für Operationen, die eine Inverse besitzen (wie Addition die Subtraktion hat, XOR das XOR), da `Range(L,R)` auf der Subtraktion von `Prefix(L-1)` basiert!

## Anwendungen in der Praxis

- **Finanzbuchhaltung:** Schnelles Abrufen der Nettosumme von Transaktionen innerhalb eines beliebigen Datumsbereichs, während gleichzeitig historische Transaktionskorrekturen eine Echtzeit-Aktualisierung des Hauptbuchs ermöglichen.

## Verwandte Algorithmen in cOde(n)

- **[fenwick_01 - Build Tree](fenwick_01_build-fenwick-tree.md)** — Der erforderliche Konstruktionsschritt.
- **[segtree_01 - Segment Tree Query](../segment_tree/segtree_01_point-update-range-query.md)** — Dasselbe Problem gelöst mit einer etwas komplexeren Datenstruktur.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*