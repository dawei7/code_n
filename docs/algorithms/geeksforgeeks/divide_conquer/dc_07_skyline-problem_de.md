# The Skyline Problem

| | |
|---|---|
| **ID** | `dc_07` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(N \log N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 9/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [The Skyline Problem](https://leetcode.com/problems/the-skyline-problem/) |

## Problemstellung

Die Skyline einer Stadt ist die äußere Kontur der Silhouette, die von allen Gebäuden der Stadt aus der Ferne betrachtet gebildet wird. Gegeben sind die Positionen und Höhen aller Gebäude; berechnen Sie die Skyline, die von diesen Gebäuden gemeinsam gebildet wird.
Die Gebäude sind als Array `buildings` gegeben, wobei `buildings[i] = [left_i, right_i, height_i]`.
Die Skyline sollte als eine Liste von "Schlüsselpunkten" `[x_i, y_i]` zurückgegeben werden, sortiert nach ihrer x-Koordinate. Ein Schlüsselpunkt ist der linke Endpunkt eines horizontalen Liniensegments, das die Oberkante eines Gebäudes repräsentiert.

**Eingabe:** Ein 2D-Integer-Array `buildings`.
**Ausgabe:** Ein 2D-Integer-Array von Schlüsselpunkten, die die Skyline-Kontur bilden.

## Wann man es verwendet

- Zur Demonstration von fortgeschrittenem Divide and Conquer beim Mergen, insbesondere wie man zwei separate Listen von überlappenden Intervallen/Koordinaten zusammenführt.
- Hinweis: Dieses Problem ist ebenso bekannt für seine Lösung mittels Priority Queue (Max-Heap). Beide Ansätze sind akzeptabel und liegen bei $O(N \log N)$.

## Ansatz

**1. Der Divide-Schritt:**
Wenn wir nur EIN Gebäude `[L, R, H]` haben, ist die Skyline trivial! Es sind lediglich zwei Schlüsselpunkte: die obere linke Ecke `[L, H]` und die untere rechte Ecke, an der das Gebäude wieder auf den Boden abfällt `[R, 0]`.
Wir können das Array von N Gebäuden rekursiv exakt in der Mitte teilen, bis jedes Segment genau ein Gebäude enthält!

**2. Der Conquer-Schritt (Merge):**
Dies ist der schwierigste Teil des Problems. Wir haben zwei Skylines, `left_skyline` und `right_skyline`, beide sortiert nach ihren X-Koordinaten. Wir müssen sie zu einer einzigen `merged_skyline` zusammenführen.
Wir verwenden zwei Pointer, `i` für die linke Skyline und `j` für die rechte Skyline.
Zudem müssen wir die *aktuelle Höhe* beider Skylines verfolgen, während wir über sie hinwegstreichen. Nennen wir sie `h1` (links) und `h2` (rechts).

- Wir wählen den Schlüsselpunkt mit der KLEINEREN X-Koordinate. Nehmen wir an, `left_skyline[i]` liegt weiter links.
- Wir aktualisieren unsere aktuelle `h1` auf `left_skyline[i].y`.
- Was ist die globale Höhe der zusammengeführten Skyline an dieser X-Koordinate? Da sich die Gebäude überlappen, ist die tatsächliche Höhe einfach das MAXIMUM der aktuellen Höhen beider Skylines! `max_h = max(h1, h2)`.
- Wenn sich diese `max_h` von der Höhe des letzten Punktes unterscheidet, den wir zu `merged_skyline` hinzugefügt haben, bedeutet dies, dass sich die Skyline gerade in der Höhe verändert hat! Wir fügen `[x, max_h]` zu unserer `merged_skyline` hinzu.
- Wir inkrementieren `i`.
*(Wenn die X-Koordinaten exakt identisch sind, aktualisieren wir SOWOHL `h1` ALS AUCH `h2`, wählen das Maximum und inkrementieren SOWOHL `i` ALS AUCH `j`)*.

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

## Walk-through

*(Konzeptionell)*
`sk1 = [[2, 10], [9, 0]]` (Gebäude 1)
`sk2 = [[3, 15], [7, 0]]` (Gebäude 2)

1. `i=0`, `j=0`. `x1=2`, `x2=3`. `x1 < x2`.
   `x=2`, `h1=10`. `max_h = max(10, 0) = 10`.
   Füge `[2, 10]` hinzu. `i=1`.
2. `i=1`, `j=0`. `x1=9`, `x2=3`. `x2 < x1`.
   `x=3`, `h2=15`. `max_h = max(10, 15) = 15`.
   Füge `[3, 15]` hinzu. `j=1`.
3. `i=1`, `j=1`. `x1=9`, `x2=7`. `x2 < x1`.
   `x=7`, `h2=0`. `max_h = max(10, 0) = 10`.
   Füge `[7, 10]` hinzu. `j=2`.
4. `j` ist erschöpft. Hänge den Rest von `sk1` an.
   Füge `[9, 0]` hinzu. `i=2`.

Zusammengeführtes Ergebnis: `[[2, 10], [3, 15], [7, 10], [9, 0]]`. ✓ (Die Skyline springt bei 2 nach oben, bei 3 noch höher, fällt bei 7 auf das Dach des ersten Gebäudes zurück und bei 9 auf den Boden).

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N \log N)$ | $O(N)$ |

Der Rekursionsbaum teilt sich exakt wie bei Merge Sort in zwei Hälften ($O(\log N)$ Tiefe).
Auf jeder Ebene iteriert die Funktion `merge_skylines` linear durch die Teil-Skylines. Der gesamte Merge-Aufwand auf einer bestimmten Ebene des Baums summiert sich zu $O(N)$.
Daher gilt T(N) = 2T(N/2) + $O(N)$ -> $O(N \log N)$.
Die Platzkomplexität beträgt $O(N)$, da die neu zusammengeführten Arrays auf der obersten Ebene bis zu 2N Punkte enthalten können.

## Varianten & Optimierungen

- **Sweep Line + Max-Heap:** Der gebräuchlichere Ansatz. Anstatt die Gebäude zu teilen, zerlegt man jedes Gebäude in zwei "Ereignisse": `(Left, Height, ENTER)` und `(Right, Height, EXIT)`. Man sortiert alle 2N Ereignisse nach ihrer X-Koordinate. Während man von links nach rechts streicht, fügt man bei einem ENTER-Ereignis die Höhe in einen Max-Heap ein. Bei einem EXIT-Ereignis entfernt man diese Höhe "lazy" aus dem Max-Heap. Das aktuelle Maximum des Heaps ist IMMER die aktuelle Skyline-Höhe! Ebenfalls strikt $O(N \log N)$.

## Anwendungen in der Praxis

- **Computergrafik (Verdeckungsberechnung):** In 2D-Rendering-Engines bestimmt dieser Algorithmus exakt, welche Sprites (wie Berge oder Parallax-Hintergrundebenen) die dahinter liegenden Ebenen visuell verdecken, wodurch die Engine das Rendern der verdeckten Pixel komplett überspringen kann.

## Verwandte Algorithmen in cOde(n)

- **[sort_01 - Merge Sort](../sorting/sort_01_merge-sort.md)** — Das buchstäblich identische Divide and Conquer-Architekturmuster.
- **[heap_03 - Sweep Line Skyline](../heap/heap_03_sweep-line-skyline.md)** — Die Priority-Queue-Variante dieses exakten Problems.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*