# Interpolation Search

| | |
|---|---|
| **ID** | `search_08` |
| **Kategorie** | searching |
| **Komplexität (erforderlich)** | $O(\log(\log N)$) Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **Wikipedia** | [Interpolation search](https://en.wikipedia.org/wiki/Interpolation_search) |

## Problemstellung

Gegeben ist ein sortiertes Array `arr` und ein `target`-Wert.
Finde den Index des `target` im Array. Falls das `target` nicht vorhanden ist, gib `-1` zurück.
Optimiere die Suche für Szenarien, in denen die Elemente gleichmäßig verteilt sind (z. B. `10, 20, 30, 40, 50`).

**Eingabe:** Ein sortiertes Array `arr` und ein `target`-Wert.
**Ausgabe:** Eine Ganzzahl, die den Index repräsentiert.

## Wann sollte man es verwenden

- Bei der Suche in einem physischen Telefonbuch.
- Wenn die Datenmenge riesig und streng gleichmäßig verteilt ist. Wenn die Daten gehäuft oder exponentiell verteilt sind (z. B. `1, 2, 4, 100, 10000`), verschlechtert sich dieser Algorithmus drastisch.

## Ansatz

**1. Die Telefonbuch-Analogie:**
Wenn du "Zebra" in einem Wörterbuch suchst, schlägst du es genau in der Mitte auf? (Binäre Suche).
NEIN! Du weißt, dass "Z" ganz am Ende des Alphabets steht, also schlägst du das Wörterbuch instinktiv zu 95 % hinten auf!
Wenn du "Apple" suchst, schlägst du es zu 5 % vorne auf.
Interpolation Search ahmt die menschliche Intuition nach. Es schätzt die wahrscheinliche Position des Ziels basierend auf seinem Wert im Verhältnis zu den Minimal- und Maximalwerten des Arrays.

**2. Die Interpolationsformel:**
Bei der Standard-Binären Suche ist der Mittelpunkt immer:
mid = left + \frac{1}{2} \cdot (right - left)

Bei der Interpolation Search ersetzen wir den festen Bruch \frac{1}{2} durch ein dynamisches Verhältnis!
Ratio = \frac{\text{target} - arr[left]}{arr[right] - arr[left]}
Wenn das Array von 0 bis 100 reicht und das Ziel 80 ist, beträgt das Verhältnis \frac{80-0}{100-0} = 0.8.
Wir multiplizieren dieses Verhältnis dann mit dem Indexbereich, um unsere exakte "Probe"-Position zu finden:
probe = left + \lfloor Ratio \cdot (right - left) \rfloor

**3. Die Eliminationslogik:**
Genau wie bei der Binären Suche!
- Wenn `arr[probe] == target`: Gib `probe` zurück.
- Wenn `arr[probe] < target`: `left = probe + 1`.
- Wenn `arr[probe] > target`: `right = probe - 1`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for search_08: Interpolation Search.

Auto-generated from challenges/algorithms/searching.py:SPECS.
O(n) time.
"""


def solve(data, target, n):
    low, high = 0, n - 1
    while low <= high and data[low] <= target <= data[high]:
        if data[high] == data[low]:
            if data[low] == target:
                return low
            return -1
        # Probe position estimated from the target's value.
        pos = low + (target - data[low]) * (high - low) // (data[high] - data[low])
        if pos < low or pos > high:
            return -1
        value = data[pos]
        if value == target:
            return pos
        if value < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1
```

</details>

## Durchlauf

`arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]`. `target = 80`. Länge 10.

1. `left = 0` (Wert 10), `right = 9` (Wert 100).
   - Ratio = \frac{80 - 10}{100 - 10} = \frac{70}{90} = 0.777.
   - probe = 0 + \lfloor 0.777 x 9 \rfloor = \lfloor 7.0 \rfloor = 7.
   - Prüfe `arr[7]`: Es ist `80`!
   - `80 == 80`! Treffer gefunden!

Ergebnis: `7`. ✓
*(Die Binäre Suche hätte 3 Iterationen benötigt, um es zu finden: mid=4, mid=7. Die Interpolation Search fand es sofort in genau 1 Iteration, indem sie die mathematische Position korrekt erraten hat!)*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(\log(\log N)$) | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Wenn die Daten perfekt gleichmäßig verteilt sind, landet die Probe jedes Mal unglaublich nah am Ziel, wodurch der Suchraum exponentiell schneller schrumpft als bei der Binären Suche. Die durchschnittliche Zeitkomplexität beträgt $O(log(log N)$).
Für ein Array mit 4 Milliarden Elementen (N = 2^{32}) benötigt die Binäre Suche 32 Operationen. Die Interpolation Search benötigt ~= log_2(32) = 5 Operationen!
Wenn die Daten jedoch exponentiell verteilt sind (z. B. `[1, 2, 4, 8, 16, 1000]`) und das Ziel `15` ist, wird die Probe-Berechnung wiederholt den Index 0 schätzen, was den Algorithmus dazu zwingt, sich jeweils nur um 1 Index vorwärts zu tasten, wodurch er vollständig zu einer $O(N)$ linearen Suche degradiert!
Die Platzkomplexität beträgt $O(1)$.

## Varianten & Optimierungen

- **Robust Interpolation Search:** Ein hybrider Algorithmus, der die Interpolationsformel verwendet, um die Probe zu schätzen, aber dann erzwingt, dass das Suchfenster um mindestens eine garantierte Blockgröße C schrumpft (ähnlich wie bei der Jump Search). Wenn die Daten gehäuft vorliegen, fällt er elegant auf $O(\log N)$ zurück, anstatt auf $O(N)$ abzufallen.

## Anwendungen in der Praxis

- **Datenbank-Primärschlüssel:** Da automatisch inkrementierende Primärschlüssel in SQL-Datenbanken (`1, 2, 3...`) eine perfekt gleichmäßige arithmetische Folge bilden, ermöglicht die Interpolation Search der Datenbank-Engine, in $O(1)$-Zeit sofort zum exakten Festplattenblock zu springen, der die benötigte Zeile enthält, wodurch die B-Baum-Traversierung vollständig übersprungen wird!

## Verwandte Algorithmen in cOde(n)

- **[search_02 - Binary Search](search_02_binary-search.md)** — Der mathematisch sicherere, universell einsetzbare Suchalgorithmus, der unabhängig von der Datenverteilung funktioniert.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für Wettbewerbsprogrammierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*