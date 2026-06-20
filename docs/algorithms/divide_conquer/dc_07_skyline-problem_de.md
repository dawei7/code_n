# Das Skyline-Problem

| | |
|---|---|
| **ID** | `dc_07` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(N \log N)$ Zeit, $O(N)$ Speicherplatz |
| **Schwierigkeitsgrad** | 9/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [Das Skyline-Problem](https://leetcode.com/problems/the-skyline-problem/) |

## Aufgabenstellung

Die Skyline einer Stadt ist die äußere Kontur der Silhouette, die alle Gebäude dieser Stadt aus der Ferne bilden. Gegeben sind die Standorte und Höhen aller Gebäude. Geben Sie die Skyline zurück, die diese Gebäude gemeinsam bilden.
Die Gebäude werden als Array von `buildings` angegeben, wobei `buildings[i] = [left_i, right_i, height_i]`.
Die Skyline soll als Liste von „Schlüsselpunkten“ `[x_i, y_i]` zurückgegeben werden, sortiert nach ihrer x-Koordinate. Ein Schlüsselpunkt ist der linke Endpunkt eines horizontalen Liniensegments, das die Oberkante eines Gebäudes darstellt.

**Eingabe:** Ein zweidimensionales Ganzzahl-Array `buildings`.
**Ausgabe:** Ein zweidimensionales Ganzzahl-Array mit Schlüsselpunkten, die die Skyline-Kontur bilden.

## Wann man es verwendet

- Zur Veranschaulichung fortgeschrittener „Divide-and-Conquer“-Zusammenführung, insbesondere wie man zwei separate Listen überlappender Intervalle/Koordinaten zusammenführt.
- Hinweis: Dieses Problem ist ebenso bekannt für seine Lösung mit einer Priority Queue (Max-Heap). Beide Lösungen sind zulässig und $O(N \log N)$.

## Vorgehensweise

**1. Der Teilungsschritt:**
Wenn wir nur EIN Gebäude `[L, R, H]` haben, ist die Skyline trivial! Es gibt nur zwei Schlüsselpunkte: die obere linke Ecke `[L, H]` und die untere rechte Ecke, an der das Gebäude wieder auf den Boden trifft `[R, 0]`.
Wir können das Array mit N Gebäuden rekursiv genau in zwei Hälften teilen, bis jeder Teil genau ein Gebäude enthält!

**2. Der Zusammenführungsschritt:**
Der absolut schwierigste Teil des Problems. Wir haben zwei Skylines, `left_skyline` und `right_skyline`, die beide nach ihren X-Koordinaten sortiert sind. Wir müssen sie zu einer einzigen `merged_skyline` zusammenführen.
Wir verwenden zwei Zeiger: `i` für die linke Skyline und `j` für die rechte Skyline.
Außerdem müssen wir die *aktuelle Höhe* beider Skylines im Auge behalten, während wir sie abtasten. Nennen wir sie `h1` (links) und `h2` (rechts).

- Wir wählen den Schlüsselpunkt mit der KLEINEREN X-Koordinate aus. Nehmen wir an, `left_skyline[i]` liegt weiter links.
- Wir aktualisieren unseren aktuellen `h1` auf `left_skyline[i].y`.
- Wie hoch ist die Gesamt-Höhe der zusammengeführten Skyline an dieser X-Koordinate? Da sich die Gebäude überlappen, ist die tatsächliche Höhe einfach das MAXIMUM der aktuellen Höhen beider Skylines! `max_h = max(h1, h2)`.
- Wenn sich dieser `max_h` von der Höhe des letzten Punktes unterscheidet, den wir zu `merged_skyline` hinzugefügt haben, bedeutet dies, dass sich die Höhe der Skyline gerade geändert hat! Wir addieren `[x, max_h]` zu unserem `merged_skyline`.
- Wir erhöhen `i`.
*(Wenn die X-Koordinaten exakt identisch sind, aktualisieren wir SOWOHL `h1` als auch `h2`, wählen den Maximalwert aus und erhöhen SOWOHL `i` als auch `j`)*.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dc_07: Skyline Problem.

Given n axis-aligned rectangular buildings as
"""


def solve(buildings, n):
    """Skyline via D&C: recurse, then merge two skylines."""
    if n == 0:
        return []
    if n == 1:
        l, h, r = buildings[0]
        return [[l, h], [r, 0]]
    mid = n // 2
    left = solve(buildings[:mid], mid)
    right = solve(buildings[mid:], n - mid)
    return _merge(left, right)

def _merge(left, right):
    result = []
    h1 = h2 = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            x, h1 = left[i][0], left[i][1]
            i += 1
        elif left[i][0] > right[j][0]:
            x, h2 = right[j][0], right[j][1]
            j += 1
        else:
            x = left[i][0]
            h1 = left[i][1]
            h2 = right[j][1]
            i += 1
            j += 1
        h = max(h1, h2)
        if not result or result[-1][1] != h:
            result.append([x, h])
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result
```

</details>

## Schritt-für-Schritt-Anleitung

*(Konzeptionell)*
`sk1 = [[2, 10], [9, 0]]` (Gebäude 1)
`sk2 = [[3, 15], [7, 0]]` (Gebäude 2)

1. `i=0`, `j=0`. `x1=2`, `x2=3`. `x1 < x2`.
   `x=2`, `h1=10`. `max_h = max(10, 0) = 10`.
   `[2, 10]` hinzufügen. `i=1`.
2. `i=1`, `j=0`. `x1=9`, `x2=3`. `x2 < x1`.
   `x=3`, `h2=15`. `max_h = max(10, 15) = 15`.
   `[3, 15]` hinzufügen. `j=1`.
3. `i=1`, `j=1`. `x1=9`, `x2=7`. `x2 < x1`.
   `x=7`, `h2=0`. `max_h = max(10, 0) = 10`.
   `[7, 10]` hinzufügen. `j=2`.
4. `j` ist erschöpft. Den Rest von `sk1` anhängen.
   `[9, 0]` hinzufügen. `i=2`.

Zusammengeführtes Ergebnis: `[[2, 10], [3, 15], [7, 10], [9, 0]]`. ✓ (Die Skyline springt bei 2 nach oben, springt bei 3 noch höher, fällt bei 7 wieder auf das Dach des ersten Gebäudes zurück und fällt bei 9 auf den Boden).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(N)$ |
| **Schlechteste** | $O(N \log N)$ | $O(N)$ |

Der Rekursionsbaum teilt sich genau wie beim Merge-Sort ($O(\log N)$ Tiefe) in zwei Hälften.
Auf jeder Ebene durchläuft die Funktion `merge_skylines` die Teil-Skylines linear. Der gesamte Aufwand für das Zusammenführen auf einer bestimmten Ebene des Baums beläuft sich auf $O(N)$.
Daher gilt: T(N) = 2T(N/2) + $O(N)$ -> $O(N \log N)$.
Die Platzkomplexität beträgt $O(N)$, da die neu zusammengeführten Arrays auf der obersten Ebene bis zu 2N Punkte enthalten.

## Varianten & Optimierungen

- **Sweep Line + Max-Heap:** Der gängigere Ansatz. Anstatt die Gebäude aufzuteilen, zerlegt man jedes Gebäude in zwei „Ereignisse“: `(Left, Height, ENTER)` und `(Right, Height, EXIT)`. Man sortiert alle 2N Ereignisse nach ihrer X-Koordinate. Beim Durchlaufen von links nach rechts wird die Höhe in einen Max-Heap verschoben, sobald man auf ein ENTER-Ereignis stößt. Triffst du auf ein EXIT-Ereignis, entfernst du diese Höhe verzögert aus dem Max-Heap. Die aktuelle Spitze des Heaps ist IMMER die aktuelle Skyline-Höhe! Auch streng $O(N \log N)$.

## Anwendungen in der Praxis

- **Computergrafik (Ermittlung verdeckter Flächen):** In 2D-Rendering-Engines bestimmt genau dieser Algorithmus, welche Sprites (wie Berge oder Parallax-Hintergrundebenen) die dahinter liegenden Ebenen visuell verdecken, sodass die Engine das Rendern der verdeckten Pixel komplett überspringen kann.

## Verwandte Algorithmen in cOde(n)

- **[sort_01 – Merge-Sort](../sorting/sort_01_merge-sort.md)** — Das buchstäblich exakt identische Architekturmuster „Teile und herrsche“.
- **[heap_03 – Sweep-Line-Skyline](../heap/heap_03_sweep-line-skyline.md)** – Die Priority Queues-Variante genau dieses Problems.

---

*Diese Dokumentation ist ein für cOde(n) verfasster Originalinhalt,
der sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
