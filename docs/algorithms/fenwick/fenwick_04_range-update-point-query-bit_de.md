# Bereichsaktualisierung, Punktabfrage (BIT)

| | |
|---|---|
| **ID** | `fenwick_04` |
| **Kategorie** | fenwick |
| **Komplexität (erforderlich)** | $O(\log N)$ Abfrage/Aktualisierung |
| **Schwierigkeitsgrad** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **LeetCode-Äquivalent** | (Klassische BIT-Variante) |

## Aufgabenstellung

Gegeben sei ein Array der Größe N, das auf 0 initialisiert ist. Implementieren Sie einen Fenwick Tree, der ein invertiertes Paradigma unterstützt:
1. `range_update(left, right, delta)`: Fügen Sie `delta` zu **jedem einzelnen Element** im inklusiven Bereich `[left, right]` hinzu.
2. `point_query(index)`: Gib den aktuellen Wert des Elements an Position `index` zurück.

Beide Operationen müssen in streng $O(\log N)$ Zeit ausgeführt werden.

**Eingabe:** Eine Folge von `range_update`- und `point_query`-Operationen.
**Ausgabe:** Die Ergebnisse der Punktabfragen.

## Wann man es verwendet

- Wenn man ein riesiges Array hat, in dem man häufig pauschale Änderungen vornimmt (z. B. „allen Einheiten im Bereich 10–50 +500 HP geben“), aber nur den Status einzelner Einheiten kennen muss, nicht die Summen für den gesamten Bereich.
- Dies ist das perfekte Gegenstück zum Standard-Fenwick Tree (`fenwick_02`), der Punktaktualisierungen und Bereichsabfragen verarbeitet!

## Vorgehensweise

Würden wir ein Standard-BIT verwenden, würde ein `range_update` erfordern, von `left` bis `right` zu durchlaufen und für jedes Element `point_update` aufzurufen. Das dauert $O(K log N)$, wobei K die Bereichslänge ist. Ist K groß, degeneriert dies zu $O(N \log N)$.

**Der Differenz-Array-Ansatz:**
Wir ändern, was das BIT physisch speichert. Anstatt die Array-Werte zu speichern, speichert das BIT das **Differenz-Array**.
In einem Differenzarray gilt `diff[i] = arr[i] - arr[i-1]`.
Das bedeutet, dass der tatsächliche Wert von `arr[index]` genau der Präfixsumme des Differenzarrays von 0 bis `index` entspricht!

Wenn das BIT Differenzen speichert:
1. **Bereichsaktualisierung von `[L, R]` mit `delta`:**
   - Wir müssen das Differenzarray nur an zwei Stellen bearbeiten!
   - `BIT.add(L, delta)`: Dies addiert effektiv `delta` zum Element L und *zu jedem darauf folgenden Element für immer*.
   - `BIT.add(R + 1, -delta)`: Dies hebt das `delta` für alle Elemente, die streng nach R liegen, auf.
   - Dies erfordert genau zwei $O(\log N)$-Operationen!
2. **Punktabfrage bei `index`:**
   - Der Wert ist einfach die Präfixsumme des Differenzarrays bis `index`.
   - `BIT.query_prefix(index)`.
   - Dies erfordert genau eine $O(\log N)$-Operation!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for fenwick_04: Range Update + Point Query (BIT).

Maintain an array of n integers under repeated
"""


def solve(arr, n, range_updates, point_queries, q):
    """Range add + point query via single BIT.

    Seed the BIT with the initial arr values (so the point
    query at idx returns arr[idx] + accumulated deltas).
    """
    bit = [0] * (n + 2)

    def update(i, delta):
        i += 1
        while i <= n + 1:
            bit[i] += delta
            i += i & -i

    def prefix(i):
        i += 1
        s = 0
        while i > 0:
            s += bit[i]
            i -= i & -i
        return s

    # Initialize the BIT with the DIFF array, not the values.
    # For the "range update, point query" technique, the BIT
    # stores a difference array so that point query at idx
    # gives the current value at idx.
    if n > 0:
        update(0, arr[0])
        for i in range(1, n):
            update(i, arr[i] - arr[i - 1])
    # Apply range updates: diff array approach.
    for l, r, val in range_updates:
        update(l, val)
        if r + 1 < n:
            update(r + 1, -val)
    # Point queries: read prefix sum at each index.
    out = []
    for (idx,) in point_queries:
        out.append(prefix(idx))
    return out
```

</details>

## Schritt-für-Schritt-Anleitung

Array der Größe 5 (Indizes 0 bis 4). Anfangs sind alle Elemente 0.
BIT speichert die Differenzen.

**1. Bereich [1, 3] mit +10 aktualisieren:**
- `_add(2, 10)`: Die Elemente 1, 2, 3, 4 haben nun logisch gesehen +10.
- `_add(5, -10)`: Bei Element 4 wird das +10 aufgehoben.
- Logischer Array-Zustand: `[0, 10, 10, 10, 0]`.

**2. Bereich [2, 4] um +5 aktualisieren:**
- `_add(3, 5)`: Die Elemente 2, 3 und 4 erhalten +5.
- `_add(6, -5)`: Außerhalb des Bereichs, wird ignoriert.
- Logischer Array-Zustand: `[0, 10, 15, 15, 5]`.

**3. Punktabfrage (Index 2):**
- Präfixsumme bis zum Index 2 (1-basierter Index 3).
- Summe = `_add(2)` + `_add(3)` Auswirkungen.
- Das Ergebnis ergibt genau `15`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(\log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(\log N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(\log N)$ | $O(N)$ |

Beide Operationen laufen darauf hinaus, dass die Standard-BIT-Funktionen `_add` oder `_query_prefix` eine konstante Anzahl von Malen (1 oder 2) ausgeführt werden. Daher sind alle Operationen streng $O(\log N)$.
Die Platzkomplexität beträgt $O(N)$ für die Zuweisung des Arrays.

## Varianten & Optimierungen

- **Segment Tree mit Lazy Propagation:** Ein Segment Tree kann Bereichsaktualisierungen ebenfalls in $O(\log N)$-Zeit durchführen, erfordert jedoch „Lazy Propagation“ (das Speichern ausstehender Aktualisierungen in Knoten und deren Weitergabe an untergeordnete Knoten bei Abfragen). Der Fenwick-Differenz-Ansatz ist in der Programmierung etwa fünfmal kürzer und in Bezug auf die Konstanten streng genommen schneller!

## Praktische Anwendungen

- **Gaming:** Anwendung umfangreicher Status-Buffs/Debuffs mit Flächenwirkung (Area of Effect, AoE) auf Einheiten, die in Tower-Defense-Rastern aufgereiht sind, und anschließende sofortige Abfrage der individuellen Einheitswerte bei der Schadensberechnung.

## Verwandte Algorithmen in cOde(n)

- **[fenwick_02 – Range-Sum-Abfrage](fenwick_02_range-sum-query-bit.md)** — Das exakte Gegenteil dieser Struktur.
- **[fenwick_05 – Range Update Range Query](fenwick_05_range-update-range-query-bit.md)** – Die ultimative Fusion, die diese Differenz-Array-Logik mit einem zweiten BIT kombiniert, um BEIDE Bereichsoperationen zu unterstützen!

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
