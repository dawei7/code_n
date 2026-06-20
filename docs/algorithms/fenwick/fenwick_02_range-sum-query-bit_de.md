# Bereichssummenabfrage (Punktaktualisierung)

| | |
|---|---|
| **ID** | `fenwick_02` |
| **Kategorie** | fenwick |
| **Komplexität (erforderlich)** | $O(\log N)$ Abfrage, $O(\log N)$ Aktualisierung |
| **Schwierigkeitsgrad** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [Bereichssummenabfrage – veränderbar](https://leetcode.com/problems/range-sum-query-mutable/) |

## Aufgabenstellung

Gegeben sei ein Array `arr` und sein vorab erstellter Fenwick Tree (BIT). Implementiere zwei Operationen:
1. `update(index, value)`: Aktualisiere das ursprüngliche Array so, dass `arr[index] = value` gilt.
2. `query(left, right)`: Geben Sie die Summe der Elemente in `arr` vom Index `left` bis `right` (einschließlich) zurück.

Sie müssen beide Operationen in streng $O(\log N)$-Zeit ausführen.

**Eingabe:** Ein vorab erstelltes `BIT`-Array sowie eine Folge von `update`- und `query`-Operationen.
**Ausgabe:** Das Ergebnis der `query` Operationen.

## Wann man es verwendet

- Wenn sich Array-Elemente ständig ändern (mutieren) und man kontinuierlich die Summe eines Teil-Arrays abfragen muss.
- Ein Standard-Präfixsummen-Array (`sum[i] = sum[i-1] + arr[i]`) beantwortet Abfragen in $O(1)$, aber die Aktualisierung eines einzelnen Elements dauert $O(N)$, da man das gesamte Präfix-Array neu schreiben muss! Fenwick schafft hier einen perfekten Ausgleich.

## Vorgehensweise

**Punktaktualisierung:**
Wenn das ursprüngliche Array `arr` am Index `i` seinen Wert ändert, setzen wir das BIT nicht direkt. Wir berechnen das *Delta* (die Differenz) zwischen dem neuen und dem alten Wert.
Dieses `delta` müssen wir zu `BIT[i]` sowie zu jedem übergeordneten Knoten im BIT addieren, der für `i` verantwortlich ist!
Um den Baum bis zu allen zuständigen übergeordneten Knoten zu durchlaufen, verwenden wir die Regel: `index = index + (index & -index)`.
Wir wiederholen den Vorgang so lange, bis der Index die Größe des BIT überschreitet.

**Abfrage der Präfixsumme:**
Um die Summe von 0 bis i zu ermitteln, beginnen wir bei `BIT[i]` (das die Summe eines bestimmten Abschnitts des Arrays enthält, der bei i endet).
Um die verbleibenden Abschnitte zu erhalten, entfernen wir das niedrigste gesetzte Bit, um den vorherigen Abschnitt zu finden: `index = index - (index & -index)`.
Wir summieren diese Werte und wiederholen den Vorgang, bis der Index 0 erreicht.

**Bereichsabfrage [left, right]:**
Genau wie bei herkömmlichen Präfixsummen-Arrays ist die Summe von `[left, right]` einfach:
`PrefixSum(right) - PrefixSum(left - 1)`.

*(Beachte: Das BIT ist 1-indiziert, während das ursprüngliche Array in der Regel 0-indiziert ist. Addiere immer 1 zum Array-Index, bevor du ihn an die BIT-Operationen übergibst!)*

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

## Schritt-für-Schritt-Anleitung

`arr = [3, 2, -1, 6]`. BIT ist `[0, 3, 5, -1, 10]`.

**1. Abfragebereich [0, 2]:**
- Wir benötigen `_query_prefix(2 + 1)` – `_query_prefix(0)`.
- `_query_prefix(3)`:
  - `total += BIT[3]` (-1). `total = -1`.
  - `i = 3 - (3 & -3) = 3 - 1 = 2`.
  - `total += BIT[2]` (5). `total = 4`.
  - `i = 2 - (2 & -2) = 2 - 2 = 0`. Schleife endet. 4 zurückgeben.
- Summe ist 4 – 0 = 4. ✓ (3 + 2 – 1 = 4).

**2. Update(Index 1, Wert 5):**
- Der alte Wert von `arr[1]` ist 2. Der neue Wert ist 5. `delta = 3`.
- `_add(1 + 1, 3)` -> `_add(2, 3)`.
  - `BIT[2] += 3` → 5 + 3 = 8.
  - `i = 2 + (2 & -2) = 4`.
  - `BIT[4] += 3` → 10 + 3 = 13.
  - `i = 4 + 4 = 8`. 8 > 4. Schleife endet.
- BIT ist nun `[0, 3, 8, -1, 13]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(\log N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(\log N)$ | $O(N)$ |

Die Anzahl der gesetzten Bits an einem Index i bestimmt die Anzahl der Iterationen in den `while`-Schleifen. Der maximale Index ist N. Eine ganze Zahl N hat höchstens ~= log₂(N) Bits. Daher erfordert das Durchlaufen des Baums nach oben oder unten eine streng begrenzte Anzahl von $O(\log N)$ Schritten.
Die Platzkomplexität beträgt $O(N)$ für die Speicherung des Baums.

## Varianten & Optimierungen

- **Segment Tree:** Ein Segment Tree benötigt die gleiche $O(\log N)$ Zeit, ermöglicht jedoch Abfragen von Bereichen für Maximum, Minimum, GCD und beliebige benutzerdefinierte assoziative Funktionen. Der Fenwick Tree funktioniert NUR perfekt für Operationen, die eine Umkehrung haben (wie die Addition die Subtraktion und XOR das XOR), da `Range(L,R)` auf der Subtraktion von `Prefix(L-1)` beruht!

## Praktische Anwendungen

- **Finanzbücher:** Schnelles Abrufen der Nettosumme von Transaktionen innerhalb eines beliebigen Datumsbereichs, wobei historische Transaktionskorrekturen das Finanzbuch in Echtzeit aktualisieren können.

## Verwandte Algorithmen in cOde(n)

- **[fenwick_01 – Baum aufbauen](fenwick_01_build-fenwick-tree.md)** — Der erforderliche Konstruktionsschritt.
- **[segtree_01 – Segment Tree-Abfrage](../segment_tree/segtree_01_point-update-range-query.md)** – Genau dasselbe Problem, gelöst mit einer etwas aufwendigeren Datenstruktur.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
nach dem Vorbild der kanonischen Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
