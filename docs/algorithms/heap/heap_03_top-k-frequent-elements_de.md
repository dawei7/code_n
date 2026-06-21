# Top K Frequent Elements

| | |
|---|---|
| **ID** | `heap_03` |
| **Kategorie** | heap |
| **Komplexität (erforderlich)** | $O(N log K)$ oder $O(N)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) |

## Problemstellung

Gegeben ist ein Array von Ganzzahlen `nums` und eine Ganzzahl `k`. Geben Sie die `k` häufigsten Elemente zurück. Sie können die Antwort in einer beliebigen Reihenfolge zurückgeben.
Die Zeitkomplexität Ihres Algorithmus muss strikt besser als $O(N \log N)$ sein.

**Eingabe:** Ein Array von Ganzzahlen `nums` und eine Ganzzahl `k`.
**Ausgabe:** Eine Liste von `k` Ganzzahlen, die die häufigsten Elemente repräsentieren.

## Wann man es verwendet

- Eine weitere massiv populäre FAANG-Interviewfrage.
- Testet Ihre Fähigkeit, einen Hash Map-Frequenzzähler direkt mit einer Priority Queue oder einem Bucket Sort-Algorithmus zu verknüpfen.

## Ansatz

**Ansatz 1: Der Min-Heap VIP-Club ($O(N log K)$)**
Dies ist exakt die gleiche Logik wie bei `heap_02`!
1. Iterieren Sie über das Array und zählen Sie die Häufigkeiten mithilfe einer Hash Map (`O(N)`).
2. Iterieren Sie über die eindeutigen `(frequency, number)`-Paare in der Map.
3. Fügen Sie diese in einen Min-Heap der Größe K ein. Wir konfigurieren den Heap so, dass er nach `frequency` sortiert!
4. Wenn die Heap-Größe K überschreitet, entfernen Sie das Element mit der kleinsten Frequenz mittels pop.
5. Extrahieren Sie die K verbleibenden Elemente aus dem Heap.

**Ansatz 2: Bucket Sort ($O(N)$)**
Da die absolute maximale Frequenz, die eine Zahl haben kann, exakt N beträgt (falls das Array nur aus derselben Zahl besteht), können wir ein begrenztes Array als Buckets verwenden!
1. Erstellen Sie die Hash Map der Häufigkeiten (`O(N)`).
2. Erstellen Sie ein Array aus leeren Listen (Buckets) der Größe N + 1.
3. Für jedes `(frequency, number)`-Paar in der Map, hängen Sie die `number` an die Liste bei `bucket[frequency]` an.
4. Iterieren Sie rückwärts vom maximalen Bucket-Index N bis 1. Sammeln Sie Zahlen, bis Sie exakt K Elemente haben!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for heap_03: Top K Frequent Elements.

Count occurrences with a hash map, then push (count, value) into
a max-heap. Pop the top k. The output is sorted in DESCENDING
order of frequency; ties broken by value in DESCENDING order so
the verify can do a plain equality check.
"""


def solve(data, n, k):
    import heapq
    if k <= 0 or n == 0:
        return []
    counts = {}
    for value in data:
        counts[value] = counts.get(value, 0) + 1
    # Max-heap via (-count, -value). Inverting both ensures ties
    # are broken by DESCENDING value (the smaller -v comes first).
    heap = [(-c, -v) for v, c in counts.items()]
    heapq.heapify(heap)
    out = []
    for _ in range(min(k, len(heap))):
        neg_c, neg_v = heapq.heappop(heap)
        out.append(-neg_v)
    return out
```

</details>

## Durchlauf

`nums = [1, 1, 1, 2, 2, 3]`, `k = 2`.

**Bucket Sort Ausführung:**
1. `freq_map`: `{1: 3, 2: 2, 3: 1}`.
2. `buckets` Initialisierung: `[[], [], [], [], [], [], []]` (Größe 7).
3. Befüllen:
   - Zahl 1 hat Frequenz 3: `buckets[3].append(1)`.
   - Zahl 2 hat Frequenz 2: `buckets[2].append(2)`.
   - Zahl 3 hat Frequenz 1: `buckets[1].append(3)`.
   - `buckets = [[], [3], [2], [1], [], [], []]`.
4. Rückwärts iterieren:
   - `i = 6`: leer.
   - `i = 5`: leer.
   - `i = 4`: leer.
   - `i = 3`: Enthält `[1]`. `result = [1]`. Länge ist 1 \neq 2.
   - `i = 2`: Enthält `[2]`. `result = [1, 2]`. Länge ist 2 == K. Rückgabe!

Endergebnis: `[1, 2]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ Bucket Sort | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N)$ Bucket Sort | $O(N)$ |
| **Schlechtester Fall** | $O(N log K)$ Heap | $O(N)$ |

Der Heap-Ansatz ist durch $O(N log K)$ begrenzt, wenn alle Elemente eindeutig sind und K nahe bei N liegt.
Der Bucket Sort-Ansatz vermeidet logarithmische Operationen vollständig und iteriert über exakt begrenzte Arrays, was strikt $O(N)$ Zeit in Anspruch nimmt!
Beide Algorithmen benötigen $O(N)$ Platz (der Heap-Ansatz für die Hash Map, der Bucket Sort für die verschachtelten Listen).

## Varianten & Optimierungen

- **Trie / Suffix Tree:** Wenn die Elemente massive Strings anstelle von Ganzzahlen wären, könnte die Berechnung der Hash Map aufgrund von aufwendigem String-Hashing zum Flaschenhals werden. Ein Trie kann verwendet werden, um String-Vorkommen nativ zu zählen.
- **MapReduce:** Bei Big Data (z. B. Zählen von Wörtern in Petabytes von Text-Logs) wird dieser Algorithmus in parallele "Map"-Worker, die lokale Häufigkeiten erzeugen, und "Reduce"-Worker, die diese zusammenführen und einen laufenden Top-K-Heap pflegen, aufgeteilt.

## Anwendungen in der Praxis

- **E-Commerce:** Generierung des Widgets "Die 10 meistverkauften Artikel dieser Stunde" auf einer stark frequentierten Homepage.
- **Cybersicherheit:** Erkennung von DDoS-Angriffen durch Identifizierung der IP-Adressen mit den höchsten Anfragefrequenzen in den Firewall-Logs.

## Verwandte Algorithmen in cOde(n)

- **[heap_02 - Kth Largest Element](heap_02_kth-largest-element.md)** — Die Grundlage des Min-Heap-Größe-K-Tricks.
- **[sort_06 - Radix/Bucket Sort](../sorting/sort_06_radix-sort.md)** — Die Theorie, die der $O(N)$ Array-Index-als-Frequenz-Optimierung zugrunde liegt.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Wettbewerbs-Programmierseiten verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*