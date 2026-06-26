# Bubble Sort

| | |
|---|---|
| **ID** | `sort_01` |
| **Kategorie** | sorting |
| **Komplexität (erforderlich)** | $O(n^2)$ |
| **Schwierigkeit** | 1/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **Wikipedia** | [Bubble sort](https://en.wikipedia.org/wiki/Bubble_sort) |

## Problemstellung

Gegeben sei ein Array von Integern `arr`. Sortieren Sie das Array in aufsteigender Reihenfolge unter Verwendung des Bubble-Sort-Algorithmus.

**Eingabe:** Ein unsortiertes Array von Integern `arr`.
**Ausgabe:** Das Array, sortiert in strikt aufsteigender Reihenfolge.

**Beispiel:**
| Eingabe `arr` | Ausgabe |
|---|---|
| `[64, 34, 25, 12, 22, 11, 90]` | `[11, 12, 22, 25, 34, 64, 90]` |

## Wann man es verwendet

- **Niemals** in der Produktion. Es ist berüchtigt dafür, unglaublich ineffizient zu sein.
- In Informatik-Einführungskursen als pädagogisches Werkzeug, um die Konzepte der algorithmischen Komplexität und des Tauschens (Swapping) einzuführen.
- Wenn Sie absolut sicher sind, dass das Array fast vollständig sortiert ist, kann ein leicht optimierter Bubble Sort in $O(n)$ Zeit fertiggestellt werden, obwohl Insertion Sort dieses Szenario wesentlich besser handhabt.

## Ansatz

Bubble Sort ist nach der Art und Weise benannt, wie größere Elemente an das Ende des Arrays „aufsteigen“ (wie Blasen in einer Flüssigkeit).
Wir iterieren durch das Array und vergleichen benachbarte Elemente. Wenn das linke Element größer als das rechte Element ist, tauschen wir sie.

Indem wir dies über das gesamte Array hinweg tun, wird garantiert, dass das absolut größte Element an den letzten Index geschoben wird.
Wir wiederholen diesen Prozess dann für die verbleibenden `n-1` Elemente, dann für die verbleibenden `n-2` Elemente, bis keine weiteren Tauschvorgänge mehr erforderlich sind.

**Optimierung:** Wenn wir einen vollständigen Durchlauf durch das Array machen und keinen einzigen Tausch vornehmen, bedeutet dies, dass das Array bereits perfekt sortiert ist, und wir können die Schleife sofort abbrechen.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for sort_01: Bubble Sort.

Sort the list in place by repeatedly swapping adjacent pairs.
O(n^2) time, O(1) extra space.
"""


def solve(data, n):
    for end in range(n - 1, 0, -1):
        for i in range(end):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
    return data
```

</details>

## Ablaufbeispiel

Sei `arr = [5, 1, 4, 2]`.

**Durchlauf 1 (`i=0`):**
- Vergleiche `5` und `1`: `5 > 1`. Tausche. `[1, 5, 4, 2]`
- Vergleiche `5` und `4`: `5 > 4`. Tausche. `[1, 4, 5, 2]`
- Vergleiche `5` und `2`: `5 > 2`. Tausche. `[1, 4, 2, 5]`
*Das größte Element `5` ist an das Ende aufgestiegen.*

**Durchlauf 2 (`i=1`):**
*(Wir müssen nur bis zum vorletzten Element prüfen)*
- Vergleiche `1` und `4`: `1 < 4`. Kein Tausch. `[1, 4, 2, 5]`
- Vergleiche `4` und `2`: `4 > 2`. Tausche. `[1, 2, 4, 5]`
*Das zweitgrößte Element `4` ist an seiner korrekten Position.*

**Durchlauf 3 (`i=2`):**
- Vergleiche `1` und `2`: `1 < 2`. Kein Tausch. `[1, 2, 4, 5]`
*In diesem Durchlauf wurden keine Tauschvorgänge vorgenommen! `swapped = False`. Wir brechen vorzeitig ab.*

Finales Array: `[1, 2, 4, 5]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(n^2)$ | $O(1)$ |
| **Schlechtester Fall** | $O(n^2)$ | $O(1)$ |

Die Zeitkomplexität wird durch die verschachtelten Schleifen dominiert. Die äußere Schleife läuft `n` Mal, und die innere Schleife läuft bis zu `n` Mal, was zu `n * (n - 1) / 2` Vergleichen führt, was $O(n^2)$ ergibt. Der Bestfall $O(n)$ tritt ein, wenn das Array bereits sortiert ist und unsere `swapped`-Optimierung die Schleife nach dem ersten Durchlauf abbricht. Der Platzbedarf ist strikt $O(1)$, da die Tauschvorgänge in-place erfolgen.

## Varianten & Optimierungen

- **Cocktail Shaker Sort:** Eine bidirektionale Variante von Bubble Sort. Anstatt die größten Elemente nur nach rechts aufsteigen zu lassen, lässt er das größte Element nach rechts aufsteigen und lässt dann auf dem Rückweg das kleinste Element nach links „aufsteigen“. Dies reduziert die Anzahl der Durchläufe leicht, bleibt aber bei $O(n^2)$.

## Anwendungen in der Praxis

- Keine. Fast jede moderne Bibliotheksimplementierung von Sortieralgorithmen (wie Javas `Arrays.sort` oder Pythons `sort()`) verwendet Timsort, Quicksort oder Merge Sort. Für kleine Arrays wird Insertion Sort aufgrund der wesentlich geringeren konstanten Faktoren definitiv gegenüber Bubble Sort bevorzugt.

## Verwandte Algorithmen in cOde(n)

- **[sort_03 - Insertion Sort](sort_03_insertion-sort.md)** — Ein wesentlich besserer $O(n^2)$-Algorithmus, der tatsächlich in der Produktion als Unterprogramm für kleine Array-Segmente verwendet wird.
- **[sort_02 - Selection Sort](sort_02_selection-sort.md)** — Ein weiterer $O(n^2)$-Sortieralgorithmus für pädagogische Zwecke, der die Gesamtzahl der Tauschvorgänge auf exakt `n` minimiert.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*