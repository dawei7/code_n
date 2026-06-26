# Bucket Sort

| | |
|---|---|
| **ID** | `sort_09` |
| **Kategorie** | Sortieren |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(N + K)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 3/10 |
| **Wikipedia** | [Bucket sort](https://en.wikipedia.org/wiki/Bucket_sort) |

## Problemstellung

Gegeben ist ein Array von N Fließkommazahlen `arr`, wobei jedes Element gleichmäßig über einen bekannten Bereich (z. B. `[0.0, 1.0)`) verteilt ist.
Sortieren Sie das Array in strikt linearer $O(N)$ Durchschnittszeit.

**Eingabe:** Ein unsortiertes Array von Floats `arr`.
**Ausgabe:** Ein sortiertes Array.

## Wann sollte man es verwenden?

- Wenn bekannt ist, dass die Eingabedaten **gleichmäßig verteilt** (gleichmäßig gestreut) über einen bestimmten Bereich sind.
- Der absolut beste Algorithmus zum Sortieren von Fließkommazahlen zwischen `0.0` und `1.0`, bei denen Radix Sort und Counting Sort versagen, da die Werte keine Ganzzahlen sind.

## Ansatz

**1. Die Taubenschlag-Analogie:**
Wenn Sie 100 Schüler mit Noten haben, die gleichmäßig von 0 bis 100 reichen, und Sie diese sortieren möchten, werfen Sie sie nicht alle in einen riesigen Raum, um sie zu vergleichen.
Sie erstellen 10 leere Buckets: Bucket 1 für Noten 0-9, Bucket 2 für 10-19... Bucket 10 für 90-100.
Sie werfen die Schüler in $O(1)$ Zeit in ihre jeweiligen Buckets. Da die Noten perfekt gleichmäßig verteilt sind, erhält jeder Bucket etwa 10 Schüler.
Anschließend sortieren Sie jeden kleinen Bucket einzeln. Zum Schluss verketten Sie die Buckets in der richtigen Reihenfolge!

**2. Die Bucket-Hash-Funktion:**
Woher wissen wir, in welchen Bucket ein Float gehört?
Wenn wir genau N leere Buckets erstellen und die Daten gleichmäßig zwischen `0.0` und `1.0` verteilt sind, multiplizieren wir den Wert mit N, um den Index zu erhalten!
`bucket_index = int(N * arr[i])`
Beispiel: N=10. Wenn der Wert `0.23` ist, landet er im Bucket `int(10 * 0.23) = 2`.

**3. Das interne Sortieren:**
Nachdem alle Elemente auf die Buckets verteilt wurden, können einige Buckets aufgrund geringfügiger Zufälligkeiten 2 oder 3 Elemente enthalten.
Wir iterieren durch alle N Buckets und führen einen Standard-Sortieralgorithmus (normalerweise **Insertion Sort**) auf jedem Bucket aus.
Da die Buckets extrem klein sind (durchschnittliche Größe ~= 1), wird Insertion Sort pro Bucket im Wesentlichen in $O(1)$ Zeit ausgeführt!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for sort_09: Bucket Sort.

Auto-generated from challenges/algorithms/sorting.py:SPECS.
O(n) time.
"""


def solve(data, n):
    if n == 0:
        return data
    min_val = min(data)
    max_val = max(data)
    span = max_val - min_val
    if span == 0:
        return data
    bucket_count = min(n, 10)
    bucket_size = span / bucket_count
    buckets = [[] for _ in range(bucket_count)]
    for value in data:
        idx = int((value - min_val) / bucket_size)
        if idx == bucket_count:
            # Float rounding: the max value can land one bucket too far.
            idx -= 1
        buckets[idx].append(value)
    for bucket in buckets:
        bucket.sort()
    index = 0
    for bucket in buckets:
        for value in bucket:
            data[index] = value
            index += 1
    return data
```

</details>

## Durchlauf

`arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12]`. `N = 8`.

1. Erstelle 8 leere Buckets.
2. Verteilen:
   - `0.78 * 8 = 6.24`. Bucket 6.
   - `0.17 * 8 = 1.36`. Bucket 1.
   - `0.39 * 8 = 3.12`. Bucket 3.
   - `0.26 * 8 = 2.08`. Bucket 2.
   - `0.72 * 8 = 5.76`. Bucket 5.
   - `0.94 * 8 = 7.52`. Bucket 7.
   - `0.21 * 8 = 1.68`. Bucket 1.
   - `0.12 * 8 = 0.96`. Bucket 0.
3. Buckets:
   - `B0 = [0.12]`
   - `B1 = [0.17, 0.21]` (Sortierung wird angewendet! Bleibt `0.17, 0.21`).
   - `B2 = [0.26]`
   - `B3 = [0.39]`
   - `B4 = []`
   - `B5 = [0.72]`
   - `B6 = [0.78]`
   - `B7 = [0.94]`
4. Verketten:
   - `[0.12, 0.17, 0.21, 0.26, 0.39, 0.72, 0.78, 0.94]`.

Das Ergebnis ist perfekt sortiert! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N^2)$ | $O(N)$ |

Das Verteilen von N Elementen benötigt $O(N)$ Zeit.
Das Verketten von N Buckets benötigt $O(N)$ Zeit.
Die Zeit zum Sortieren der Buckets hängt stark von der Datenverteilung ab. Da die Daten gleichmäßig verteilt sind, hat jeder Bucket eine durchschnittliche Länge von N/N = 1. Das Sortieren eines Arrays der Länge 1 ist $O(1)$. Die gesamte Sortierzeit beträgt N x $O(1) = O(N)$.
Daher ist die durchschnittliche Zeitkomplexität $O(N)$.
**SCHLECHTESTER FALL:** Wenn die Daten extrem gehäuft sind (z. B. alle 10.000 Floats liegen exakt um `0.51`), landet JEDES einzelne Element im exakt gleichen Bucket! Der Algorithmus verfällt dazu, einen $O(N^2)$ Insertion Sort auf dem gesamten Array auszuführen!
Die Platzkomplexität beträgt $O(N)$, um das 2D-Array der Buckets zu speichern.

## Varianten & Optimierungen

- **Generalisierte Bereichs-Buckets:** Wenn die Daten nicht `[0.0, 1.0)` sind, sondern von `MIN` bis `MAX` reichen, wird die Bucket-Hash-Formel wie folgt angepasst: `index = floor((arr[i] - MIN) / (MAX - MIN) * (bucket_count - 1))`.
- **Top K Frequent Elements (`hash_07`):** Bucket Sort ist als implizite Hash Map-Umkehrung sehr beliebt! Wenn Sie die Häufigkeiten von Elementen haben, können Sie die Häufigkeiten als Bucket-Indizes verwenden. Der höchste nicht leere Bucket liefert Ihnen sofort das häufigste Element in $O(N)$ Zeit!

## Praxisanwendungen

- **Sensordaten-Analyse:** Sortieren von Temperatur-, Feuchtigkeits- oder Telemetrie-Datenströmen, die im Tagesverlauf natürlich gleichmäßigen Grenzen folgen, wodurch der $O(N \log N)$-Overhead von Quicksort vermieden wird.

## Verwandte Algorithmen in cOde(n)

- **[sort_03 - Insertion Sort](sort_03_insertion-sort.md)** — Der optimale Algorithmus zum Sortieren der winzigen Sub-Arrays innerhalb der Buckets.
- **[sort_07 - Counting Sort](sort_07_counting-sort.md)** — Konzeptionell identisch mit Bucket Sort, aber bei jedem Bucket ist mathematisch garantiert, dass er genau einen eindeutigen Ganzzahlwert enthält.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*