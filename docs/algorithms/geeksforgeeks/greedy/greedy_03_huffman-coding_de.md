# Huffman-Kodierung

| | |
|---|---|
| **ID** | `greedy_03` |
| **Kategorie** | greedy |
| **Komplexität (erforderlich)** | $O(N \log N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **Wikipedia** | [Huffman coding](https://en.wikipedia.org/wiki/Huffman_coding) |

## Problemstellung

Gegeben ist ein Array von eindeutigen Zeichen und deren entsprechende Häufigkeiten in einer Textdatei. Konstruieren Sie einen Huffman-Baum, um für jedes Zeichen einen binären Code variabler Länge zu generieren.
Das Ziel ist es, die Gesamtzahl der Bits zu minimieren, die für die Komprimierung der Textdatei erforderlich sind.

**Eingabe:** Zwei Arrays `chars[]` und `freq[]`.
**Ausgabe:** Ein Dictionary, das jedes Zeichen auf seinen optimalen binären String abbildet (z. B. `{'a': '0', 'b': '10', 'c': '11'}`).

## Wann man es verwendet

- Zur Lösung des Problems der optimalen präfixfreien binären Kodierung.
- Um zu demonstrieren, wie Priority Queues (Min-Heaps) verwendet werden können, um Binärbäume von unten nach oben (bottom-up) zu konstruieren.

## Ansatz

**1. Die Präfixfrei-Regel:**
Wenn 'a' als `0` kodiert wird, darf der Code keines anderen Zeichens mit `0` BEGINNEN (wie `01` oder `011`). Würden sie das tun, wüsste ein Decoder beim Lesen einer `0` nicht, ob er bei 'a' stoppen oder weiterlesen soll!
Ein Binärbaum garantiert dies auf natürliche Weise! Wenn wir Zeichen NUR in den Blattknoten platzieren, ist der Pfad von der Wurzel zu jedem Blatt (links=0, rechts=1) garantiert präfixfrei.

**2. Die Greedy-Intuition:**
Zeichen, die sehr häufig vorkommen (wie 'e' oder 'a'), sollten sehr KURZE Codes haben (flach im Baum). Zeichen, die selten vorkommen (wie 'z' oder 'q'), sollten LANGE Codes haben (tief im Baum).
Daher sollten wir gierig die zwei Zeichen mit den ABSOLUT NIEDRIGSTEN Häufigkeiten wählen und sie so tief wie möglich in den Baum schieben, indem wir sie zu Geschwistern machen!

**3. Der Algorithmus (Bottom-Up Baumkonstruktion):**
1. Erstellen Sie für jedes Zeichen einen Blattknoten, der dessen Häufigkeit speichert. Fügen Sie alle Blattknoten in eine **Min-Heap** (Priority Queue) ein, sortiert nach Häufigkeit.
2. Solange mehr als 1 Knoten in der Min-Heap vorhanden ist:
   - Entnehmen Sie die zwei Knoten mit den niedrigsten Häufigkeiten (nennen wir sie `left` und `right`).
   - Erstellen Sie einen neuen "internen" Elternknoten. Dessen Häufigkeit ist `left.freq + right.freq`.
   - Hängen Sie `left` und `right` als dessen Kinder an.
   - Fügen Sie diesen neuen Elternknoten wieder in die Min-Heap ein!
3. Schließlich verbleibt nur noch 1 Knoten in der Min-Heap. Dies ist die Wurzel des gesamten Huffman-Baums!

**4. Code-Generierung:**
Führen Sie eine einfache DFS von der Wurzel aus durch. Wenn Sie nach links gehen, hängen Sie eine '0' an. Wenn Sie nach rechts gehen, hängen Sie eine '1' an. Wenn Sie einen Blattknoten erreichen, speichern Sie den akkumulierten String in Ihrem Dictionary für dieses Zeichen.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for greedy_03: Huffman Coding.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n log n) time.
"""


def solve(chars, freq, n):
    import heapq
    if n == 0:
        return 0
    if n == 1:
        return freq[0]
    heap = [[f, 0, ""] for f in freq]
    heapq.heapify(heap)
    total = 0
    while len(heap) > 1:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        merged = [a[0] + b[0], 0, ""]
        total += merged[0]
        heapq.heappush(heap, merged)
    return total
```

</details>

## Durchlauf

Zeichen: `a:5`, `b:9`, `c:12`, `d:13`, `e:16`, `f:45`.
`pq = [a:5, b:9, c:12, d:13, e:16, f:45]` (Sortiert).

1. Entnehme `a:5`, `b:9`. Verschmelze zu `1:14`.
   `pq = [c:12, d:13, 1:14, e:16, f:45]`.
2. Entnehme `c:12`, `d:13`. Verschmelze zu `2:25`.
   `pq = [1:14, e:16, 2:25, f:45]`.
3. Entnehme `1:14`, `e:16`. Verschmelze zu `3:30`.
   `pq = [2:25, 3:30, f:45]`.
4. Entnehme `2:25`, `3:30`. Verschmelze zu `4:55`.
   `pq = [f:45, 4:55]`.
5. Entnehme `f:45`, `4:55`. Verschmelze zu `5:100`.
   `pq = [5:100]`.
6. Nur noch 1 Knoten übrig! Das ist die Wurzel.

**DFS von `5:100`:**
- Links zu `f:45` -> Code **"0"**.
- Rechts zu `4:55` \implies Code "1".
  - Links zu `2:25` -> Code "10".
    - Links zu `c:12` -> Code **"100"**.
    - Rechts zu `d:13` -> Code **"101"**.
  - Rechts zu `3:30` \implies Code "11".
    - Links zu `1:14` -> Code "110".
      - Links zu `a:5` -> Code **"1100"**.
      - Rechts zu `b:9` -> Code **"1101"**.
    - Rechts zu `e:16` -> Code **"111"**.

Beachten Sie, wie `f` (höchste Häufigkeit 45) 1 Bit erhält, während `a` (niedrigste Häufigkeit 5) 4 Bits erhält! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N \log N)$ | $O(N)$ |

Der Aufbau der anfänglichen Min-Heap benötigt $O(N)$.
Wir entnehmen zwei Knoten und fügen N-1 Mal einen Knoten hinzu. Priority Queue Operationen benötigen $O(\log N)$. Daher benötigt die while-Schleife $O(N \log N)$ Zeit.
Die DFS benötigt $O(N)$ Zeit, um die insgesamt 2N-1 Knoten im Baum zu besuchen.
Die gesamte Zeitkomplexität wird von der Priority Queue dominiert: $O(N \log N)$.
Die Platzkomplexität beträgt $O(N)$, um die Knoten in der Heap, die Knoten im Baum und das Ausgabe-Dictionary zu speichern.

## Varianten & Optimierungen

- **Zwei-Queue-Optimierung:** Wenn die anfänglichen Eingabe-Arrays BEREITS strikt nach Häufigkeit sortiert sind, können Sie $O(N)$ Zeit erreichen! Verwenden Sie anstelle einer Min-Heap zwei Standard-FIFO-Queues. Queue 1 enthält die anfänglich sortierten Blätter. Queue 2 enthält die neu generierten internen Knoten. Vergleichen Sie bei jedem Schritt einfach die Vorderseite von Queue 1 und Queue 2, um das absolute Minimum zu finden.

## Anwendungen in der Praxis

- **Datenkomprimierung:** Die Huffman-Kodierung ist die grundlegende Entropiekodierungs-Engine innerhalb des massiven DEFLATE-Algorithmus, der ZIP-Dateien, GZIP und PNG-Bilder antreibt! Sie wird buchstäblich milliardenfach pro Sekunde im Internet verwendet.

## Verwandte Algorithmen in cOde(n)

- **[greedy_01 - Activity Selection](greedy_01_activity-selection.md)** — Ein weiterer Algorithmus, bei dem Sortierung maßgeblich eine gierige Entscheidung bestimmt.
- **[graph_10 - Prim's MST](../graphs/graph_10_prim-s-mst.md)** — Eine weitere Anwendung, die stark auf dem Entnehmen aus einer Priority Queue basiert, um einen Baum zu konstruieren.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link oben auf der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*