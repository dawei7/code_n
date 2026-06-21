# Bereichs-Update, Punkt-Abfrage (BIT)

| | |
|---|---|
| **ID** | `fenwick_04` |
| **Kategorie** | fenwick |
| **Komplexität (erforderlich)** | $O(\log N)$ Abfrage/Update |
| **Schwierigkeit** | 6/10 |
| **Interview-Relevanz** | 4/10 |
| **LeetCode-Äquivalent** | (Klassische BIT-Variante) |

## Problemstellung

Gegeben sei ein Array der Größe N, das mit 0 initialisiert ist. Implementieren Sie einen Fenwick Tree, der ein umgekehrtes Paradigma unterstützt:
1. `range_update(left, right, delta)`: Addiere `delta` zu **jedem einzelnen Element** im inklusiven Bereich `[left, right]`.
2. `point_query(index)`: Gib den aktuellen Wert des Elements an `index` zurück.

Beide Operationen müssen in strikter $O(\log N)$-Zeit ausgeführt werden.

**Eingabe:** Eine Sequenz von `range_update`- und `point_query`-Operationen.
**Ausgabe:** Die Ergebnisse der Punkt-Abfragen.

## Wann man es verwendet

- Wenn Sie ein massives Array haben, bei dem Sie häufig flächendeckende Änderungen vornehmen (z. B. „gib +500 HP an alle Einheiten im Bereich 10-50“), aber nur den Status einzelner Einheiten abfragen müssen, nicht die Summen über Bereiche.
- Dies kehrt den Standard-Fenwick Tree (`fenwick_02`) perfekt um, welcher Punkt-Updates und Bereichs-Abfragen handhabt!

## Ansatz

Würden wir einen Standard-BIT verwenden, müsste ein `range_update` von `left` bis `right` iterieren und `point_update` für jedes Element aufrufen. Das benötigt $O(K \log N)$, wobei K die Länge des Bereichs ist. Wenn K groß ist, degeneriert dies zu $O(N \log N)$.

**Der Differenz-Array-Ansatz:**
Wir ändern, was der BIT physisch speichert. Anstatt die Array-Werte zu speichern, speichert der BIT das **Differenz-Array**.
In einem Differenz-Array gilt `diff[i] = arr[i] - arr[i-1]`.
Das bedeutet, der tatsächliche Wert von `arr[index]` entspricht exakt der Präfixsumme des Differenz-Arrays von 0 bis `index`!

Da der BIT nun Differenzen speichert:
1. **Bereichs-Update `[L, R]` mit `delta`:**
   - Wir müssen das Differenz-Array nur an zwei Stellen anpassen!
   - `BIT.add(L, delta)`: Dies addiert effektiv `delta` zum Element L und zu *jedem darauf folgenden Element*.
   - `BIT.add(R + 1, -delta)`: Dies hebt das `delta` für alle Elemente nach R wieder auf.
   - Dies benötigt exakt zwei $O(\log N)$-Operationen!
2. **Punkt-Abfrage an `index`:**
   - Der Wert ist einfach die Präfixsumme des Differenz-Arrays bis `index`.
   - `BIT.query_prefix(index)`.
   - Dies benötigt exakt eine $O(\log N)$-Operation!

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

## Ablaufbeispiel

Array der Größe 5 (Indizes 0 bis 4). Anfangs alles 0.
Der BIT speichert Differenzen.

**1. Bereichs-Update [1, 3] mit +10:**
- `_add(2, 10)`: Die Elemente 1, 2, 3, 4 haben nun logisch +10.
- `_add(5, -10)`: Element 4 hat das +10 wieder aufgehoben.
- Logischer Array-Zustand: `[0, 10, 10, 10, 0]`.

**2. Bereichs-Update [2, 4] mit +5:**
- `_add(3, 5)`: Die Elemente 2, 3, 4 erhalten +5.
- `_add(6, -5)`: Außerhalb des Bereichs, wird ignoriert.
- Logischer Array-Zustand: `[0, 10, 15, 15, 5]`.

**3. Punkt-Abfrage(index 2):**
- Präfixsumme bis Index 2 (1-basierter Index 3).
- Summe = `_add(2)` + `_add(3)` Effekte.
- Ergebnis ergibt exakt `15`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(\log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(\log N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(\log N)$ | $O(N)$ |

Beide Operationen reduzieren sich darauf, die Standard-BIT-Funktionen `_add` oder `_query_prefix` eine konstante Anzahl von Malen (1 oder 2) auszuführen. Daher sind alle Operationen strikt $O(\log N)$.
Die Platzkomplexität beträgt $O(N)$ für die Array-Allokation.

## Varianten & Optimierungen

- **Segment Tree mit Lazy Propagation:** Ein Segment Tree kann Bereichs-Updates ebenfalls in $O(\log N)$-Zeit durchführen, erfordert jedoch „Lazy Propagation“ (das Speichern ausstehender Updates in Knoten und deren Weitergabe an Kinder während der Abfragen). Der Fenwick-Differenz-Ansatz ist etwa 5-mal kürzer zu implementieren und bei den Konstanten strikt schneller!

## Anwendungen in der Praxis

- **Gaming:** Anwenden massiver Area-of-Effect (AoE) Status-Buffs/Debuffs auf Einheiten, die in Tower-Defense-Gittern aufgereiht sind, und anschließendes sofortiges Abfragen individueller Einheiten-Statistiken während Schadensberechnungen.

## Verwandte Algorithmen in cOde(n)

- **[fenwick_02 - Range Sum Query](fenwick_02_range-sum-query-bit.md)** — Das exakte Gegenstück zu dieser Struktur.
- **[fenwick_05 - Range Update Range Query](fenwick_05_range-update-range-query-bit.md)** — Die ultimative Fusion, die diese Differenz-Array-Logik mit einem zweiten BIT kombiniert, um BEIDE Bereichsoperationen zu unterstützen!

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*