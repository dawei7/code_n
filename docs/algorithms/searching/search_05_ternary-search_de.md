# Ternary Search

| | |
|---|---|
| **ID** | `search_05` |
| **Kategorie** | searching |
| **Komplexität (erforderlich)** | $O(\log_3 N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **Wikipedia** | [Ternary search](https://en.wikipedia.org/wiki/Ternary_search) |

## Problemstellung

Gegeben ist ein sortiertes Array `arr` und ein `target`-Wert.
Finde den Index des `target` im Array. Falls das `target` nicht vorhanden ist, gib `-1` zurück.
Im Gegensatz zur Binary Search, die das Array in zwei Hälften teilt, musst du das Array in 3 Abschnitte unterteilen.

**Eingabe:** Ein sortiertes Array `arr` und ein `target`-Wert.
**Ausgabe:** Eine Ganzzahl, die den Index repräsentiert.

## Wann man es verwendet

- Um nach einem spezifischen Wert in einem sortierten Array zu suchen (obwohl es in der Praxis der Binary Search unterlegen ist).
- **Hauptanwendungsfall:** Finden des exakten Maximums oder Minimums einer unimodalen mathematischen Funktion f(x) (eine stetige Kurve, die streng monoton bis zu einem Gipfel ansteigt und danach streng monoton abfällt, wie eine Parabel).

## Ansatz

**1. Die drei Abschnitte:**
Die Binary Search verwendet einen `mid`-Pointer, um das Array in zwei Hälften zu teilen.
Die Ternary Search verwendet ZWEI `mid`-Pointer (`mid1` und `mid2`), um das Array in drei exakt gleiche Drittel zu teilen.
- `mid1 = left + (right - left) / 3`
- `mid2 = right - (right - left) / 3`

**2. Die Eliminationslogik (Array-Suche):**
Wir vergleichen das `target` sowohl mit `mid1` als auch mit `mid2`.
- Wenn `target == arr[mid1]`, gib `mid1` zurück.
- Wenn `target == arr[mid2]`, gib `mid2` zurück.
- Wenn `target < arr[mid1]`: Das `target` MUSS im ersten Drittel liegen. `right = mid1 - 1`.
- Wenn `target > arr[mid2]`: Das `target` MUSS im letzten Drittel liegen. `left = mid2 + 1`.
- Andernfalls muss das `target` im mittleren Drittel gefangen sein! `left = mid1 + 1` und `right = mid2 - 1`.

**3. Die Eliminationslogik (Suche nach dem Gipfel einer unimodalen Funktion):**
Wenn eine Parabel f(x) ausgewertet wird, um ihren höchsten Punkt zu finden:
- Wenn f(\text{mid1}) < f(\text{mid2}): Der Gipfel MUSS rechts von `mid1` liegen. Wir verwerfen das gesamte erste Drittel! `left = mid1`.
- Wenn f(\text{mid1}) > f(\text{mid2}): Der Gipfel MUSS links von `mid2` liegen. Wir verwerfen das gesamte letzte Drittel! `right = mid2`.
Wir wiederholen dies, bis `left` und `right` auf dem exakten Gipfel konvergieren!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for search_05: Ternary Search.

Auto-generated from challenges/algorithms/searching.py:SPECS.
O(log n) time.
"""


def solve(data, target, n):
    low, high = 0, n - 1
    while low <= high:
        third = (high - low) // 3
        mid1 = low + third
        mid2 = high - third
        if data[mid1] == target:
            return mid1
        if data[mid2] == target:
            return mid2
        if target < data[mid1]:
            high = mid1 - 1
        elif target > data[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1
    return -1
```

</details>

## Durchlauf

`arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`, `target = 7`.

1. `left = 0`, `right = 9`.
   - `mid1 = 0 + 9//3 = 3`. `arr[3] = 4`.
   - `mid2 = 9 - 9//3 = 6`. `arr[6] = 7`.
   - `arr[mid2] == 7`! Treffer gefunden!
   - Gib `mid2 = 6` zurück.

Ergebnis: `6`. ✓

*Was, wenn `target = 5`?*
1. `left=0`, `right=9`, `mid1=3 (val=4)`, `mid2=6 (val=7)`.
   - `5` ist weder 4 noch 7.
   - `5 < 4`? Falsch.
   - `5 > 7`? Falsch.
   - Es liegt in der Mitte! `left = 4`, `right = 5`.
2. `left=4`, `right=5`.
   - `mid1 = 4 + 1//3 = 4`. `arr[4] = 5`.
   - `arr[mid1] == 5`! Treffer gefunden.
   - Gib `mid1 = 4` zurück. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(\log_3 N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(\log_3 N)$ | $O(1)$ |

Der Suchraum wird bei jedem Schritt um den Faktor 3 reduziert. Daher beträgt die Zeitkomplexität $O(log_3 N)$.
**Moment, ist $log_3 N$ nicht kleiner als $log_2 N$? Sollte die Ternary Search nicht schneller sein als die Binary Search?**
NEIN! Während die Ternary Search weniger *Iterationen* benötigt, erfordert sie ZWEI Vergleiche pro Iteration anstelle von nur einem!
Mathematisch gesehen ist die Anzahl der Vergleiche für die Binary Search ~= 1 x log_2 N.
Die Anzahl der Vergleiche für die Ternary Search ist ~= 2 x log_3 N.
Nach der Basiswechselformel gilt: 2 log_3 N = 2 \frac{log_2 N}{log_2 3} ~= 1.26 log_2 N.
Daher führt die Ternary Search 26 % MEHR Vergleiche durch als die Binary Search! Sie ist für die standardmäßige Array-Suche strikt unterlegen.
Die Platzkomplexität beträgt $O(1)$.

## Varianten & Optimierungen

- **Golden-Section Search:** Eine Optimierung der Ternary Search zur Suche nach unimodalen Gipfeln. Anstatt in jeder Iteration zwei neue Mittelpunkte zu berechnen, wird das Verhältnis des Goldenen Schnitts (\phi ~= 1.618) verwendet, sodass einer der vorherigen Mittelpunkte in der nächsten Iteration perfekt wiederverwendet werden kann, was die Funktionsauswertungen um 50 % reduziert!

## Praxisanwendungen

- **Machine Learning (Hyperparameter-Tuning):** Finden der optimalen Lernrate, die die Kurve der Verlustfunktion (Loss Function) minimiert. Wenn bekannt ist, dass die Verlustfunktion konvex (unimodal) ist, kann die Ternary Search das mathematische Minimum exakt lokalisieren, ohne rechenintensive Ableitungen aus der Analysis (Gradient Descent) zu verwenden.

## Verwandte Algorithmen in cOde(n)

- **[search_02 - Binary Search](search_02_binary-search.md)** — Der standardmäßige, in der Praxis überlegene $O(log_2 N)$ Suchalgorithmus.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*