# Optimal Merge Pattern

| | |
|---|---|
| **ID** | `greedy_05` |
| **Kategorie** | greedy |
| **Komplexität (erforderlich)** | $O(N \log N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **LeetCode-Äquivalent** | [Minimum Cost to Connect Sticks](https://leetcode.com/problems/minimum-cost-to-connect-sticks/) |

## Problemstellung

Gegeben sind `N` Dateien (oder Stöcke, oder Seile) unterschiedlicher Größe. Sie müssen diese zu einer einzigen großen Datei zusammenführen.
Das Zusammenführen zweier Dateien der Größe `A` und `B` verursacht einen Rechenaufwand von exakt `A + B`. Die neue zusammengeführte Datei hat die Größe `A + B` und wird wieder dem Pool der Dateien hinzugefügt.
Finden Sie die absolut minimale Gesamtkosten, die erforderlich sind, um alle `N` Dateien zu einer einzigen zusammenzuführen.

**Eingabe:** Ein Integer-Array `sizes`, das die Größen von `N` Dateien repräsentiert.
**Ausgabe:** Ein Integer, der die minimalen Gesamtkosten für das Zusammenführen repräsentiert.

## Wann ist es anzuwenden?

- Bei jedem Problem, das nach den "minimalen Kosten zum Verbinden von Seilen/Stöcken/Dateien" fragt.
- Sehr eng verwandt mit der Logik der Huffman-Kodierung.

## Ansatz

**1. Die Erkenntnis zur Kostenakkumulation:**
Wenn wir die Dateien A und B zusammenführen, werden die Kosten `A+B` fällig.
Später führen wir das Ergebnis mit C zusammen. Die Kosten betragen `(A+B) + C`.
Beachten Sie, dass `A` und `B` ZWEIMAL zu den Gesamtkosten addiert wurden! `C` wurde EINMAL addiert.
Das bedeutet, dass die Größen von Dateien, die früh zusammengeführt werden, bei nachfolgenden Zusammenführungen wiederholt zu den Gesamtkosten addiert werden.
**Greedy-Entscheidung:** Um die Gesamtsumme zu minimieren, müssen wir die **absolut kleinsten** Dateien zuerst zusammenführen, damit deren winzige Größen diejenigen sind, die wiederholt addiert werden! Die größten Dateien sollten bis ganz zum Schluss aufgehoben werden, damit ihre massiven Größen nur einmal zu den Gesamtkosten addiert werden.

**2. Die Priority Queue (Min-Heap):**
Wir benötigen eine Datenstruktur, die uns ständig die zwei kleinsten Elemente liefert, selbst wenn wir neue zusammengeführte Elemente erstellen und diese zurück in den Pool werfen.
Ein Min-Heap ist hierfür perfekt geeignet!

**3. Der Algorithmus:**
1. Fügen Sie alle Dateigrößen in einen Min-Heap ein.
2. Solange mehr als 1 Datei im Heap vorhanden ist:
   - Entnehmen Sie die zwei kleinsten Dateien: `file1` und `file2`.
   - Berechnen Sie deren Zusammenführungskosten: `cost = file1 + file2`.
   - Addieren Sie diese `cost` zu unserem `total_cost`-Akkumulator.
   - Fügen Sie die neue zusammengeführte Datei `cost` wieder in den Min-Heap ein!
3. Wenn genau 1 Datei im Heap verbleibt, sind wir fertig!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for greedy_05: Optimal Merge Pattern.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n log n) time.
"""


def solve(sizes, n):
    import heapq
    if n <= 1:
        return 0
    heap = list(sizes)
    heapq.heapify(heap)
    total = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        merged = a + b
        total += merged
        heapq.heappush(heap, merged)
    return total
```

</details>

## Durchlauf

`sizes = [4, 3, 2, 6]`.
`heap = [2, 3, 4, 6]`.
`total = 0`.

1. Entnehme `2`, `3`.
   `current_cost = 2 + 3 = 5`.
   `total = 0 + 5 = 5`.
   Füge `5` hinzu. `heap = [4, 5, 6]`.
2. Entnehme `4`, `5`.
   `current_cost = 4 + 5 = 9`.
   `total = 5 + 9 = 14`.
   Füge `9` hinzu. `heap = [6, 9]`.
3. Entnehme `6`, `9`.
   `current_cost = 6 + 9 = 15`.
   `total = 14 + 15 = 29`.
   Füge `15` hinzu. `heap = [15]`.
4. Heap-Länge ist 1. Beende.

Ergebnis `29`. ✓
*(Hätten wir sie linear zusammengeführt `4+3=7`, `7+2=9`, `9+6=15`, wären die Gesamtkosten `7+9+15=31`. Durch die Verwendung des optimalen Musters haben wir 2 Rechenzyklen eingespart!)*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N \log N)$ | $O(N)$ |

Der Aufbau des initialen Heaps benötigt $O(N)$ mittels `heapify`.
Die `while`-Schleife läuft exakt N-1 Mal. In jeder Iteration führen wir zwei `heappop`-Operationen und eine `heappush`-Operation durch. Priority-Queue-Operationen benötigen $O(\log N)$.
Die gesamte Zeitkomplexität beträgt strikt $O(N \log N)$.
Die Platzkomplexität beträgt $O(N)$, um die Elemente im Heap zu speichern. (Bei einer In-Place-Modifikation des Eingabe-Arrays ist sie logisch immer noch $O(N)$, technisch gesehen jedoch $O(1)$ zusätzlicher Speicherplatz).

## Varianten & Optimierungen

- **K-Wege-Zusammenführung:** Was ist, wenn Sie exakt K Dateien gleichzeitig zu den Kosten ihrer Summe zusammenführen können? Die Logik ist identisch, aber Sie entnehmen K Elemente auf einmal. *Grenzfall:* Wenn Sie dies tun, könnten Sie am Ende eine letzte Zusammenführung mit < K Elementen erhalten, was suboptimal ist! Sie müssen den initialen Heap mit Dummy-Dateien der Größe `0` auffüllen, bis (N - 1) \pmod{K - 1} == 0 gilt.

## Anwendungen in der Praxis

- **Datenbank-Abfrageplaner:** Wenn eine SQL-Abfrage eine massiv parallele `SORT`-Operation auf Milliarden von Zeilen durchführt, die nicht in den RAM passen, teilt die Datenbank diese in Tausende kleiner sortierter Blöcke auf der Festplatte auf. Um diese wieder zusammenzuführen, verwendet der Abfrageplaner das Optimal Merge Pattern, um teure Festplatten-I/O-Lesezugriffe zu minimieren.
- **Seilspleiß-Algorithmen:** Berechnung der minimalen kinetischen Energie, die erforderlich ist, um Fragmente von Kohlenstofffaserkabeln in der Materialwissenschaft zu verbinden.

## Verwandte Algorithmen in cOde(n)

- **[greedy_03 - Huffman Coding](greedy_03_huffman-coding.md)** — Exakt dieselbe Logik! Huffman baut einen Baum auf, bei dem die Kantengewichte von unten nach oben durch das Zusammenführen der zwei niedrigsten Frequenzen akkumuliert werden.
- **[sort_04 - Merge Sort](../sorting/sort_04_merge-sort.md)** — Basiert auf dem Zusammenführen sortierter Arrays, obwohl Merge Sort ein Top-Down-Divide-and-Conquer-Ansatz ist und kein Greedy-Bottom-Up-Ansatz.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*