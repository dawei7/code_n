# Fisher-Yates Shuffle

| | |
|---|---|
| **ID** | `randomized_03` |
| **Kategorie** | randomized |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [Shuffle an Array](https://leetcode.com/problems/shuffle-an-array/) |

## Problemstellung

Gegeben ist ein Array mit N Elementen. Mische das Array so, dass alle Permutationen des Arrays mit gleicher Wahrscheinlichkeit auftreten.
Dies muss in $O(N)$ Zeit und mit $O(1)$ zusätzlichem Speicherplatz (in-place) erfolgen.

**Eingabe:** Ein Array `nums`.
**Ausgabe:** Dasselbe Array, zufällig gemischt.

## Anwendung

- Zur perfekten und effizienten Randomisierung von Daten. Dies ist der Goldstandard-Algorithmus zum Mischen von Arrays (wird intern in `random.shuffle()` in Python und `std::shuffle` in C++ verwendet).

## Ansatz

Ein naiver Ansatz könnte jedem Element eine Zufallszahl zuweisen und nach dieser sortieren ($O(N \log N)$) oder wiederholt zufällige Indizes auswählen und diese tauschen ($O(N^2)$ und mathematisch verzerrt).

Der **Fisher-Yates Shuffle** (speziell die moderne Durstenfeld-Variante) ist elegant, $O(N)$ und mathematisch perfekt.

Die Grundidee ähnelt dem Ziehen von Karten aus einem Stapel:
1. Man hat einen "Stapel" von N noch nicht gezogenen Karten (die Array-Indizes von 0 bis N-1).
2. Wähle eine zufällige Karte aus dem Stapel der noch nicht gezogenen Karten.
3. Verschiebe sie in den "gezogenen" Stapel am Ende des Arrays.
4. Um dies in-place zu tun, tauschen wir einfach die zufällig gewählte Karte mit der Karte, die sich aktuell am Ende des Stapels der noch nicht gezogenen Karten befindet!
5. Verringere die Größe des Stapels der noch nicht gezogenen Karten um 1.
6. Wiederhole den Vorgang, bis nur noch 1 Karte übrig ist.

**Detaillierte Schritte:**
Iteriere `i` rückwärts von N-1 bis 1.
In jedem Schritt:
- Generiere einen zufälligen Index `j`, sodass 0 \le j \le i gilt. (Hinweis: `j` kann gleich `i` sein, was bedeutet, dass das Element an seinem Platz bleibt, was für eine gleichmäßige Wahrscheinlichkeitsverteilung entscheidend ist).
- Tausche `arr[i]` und `arr[j]`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for randomized_03: Fisher-Yates Shuffle.

Given an array of n elements, return a uniformly
"""


def solve(arr, n):
    """Fisher-Yates shuffle. Returns a new list."""
    import random
    work = list(arr)
    for i in range(n - 1, 0, -1):
        j = random.randint(0, i)
        work[i], work[j] = work[j], work[i]
    return work
```

</details>

## Durchlauf

`nums = [A, B, C, D]`

1. `i = 3` (Element D).
   - Ziehe ein zufälliges `j` zwischen 0 und 3. Nehmen wir an, `j = 1` (Element B).
   - Tausche `nums[3]` und `nums[1]`.
   - `nums = [A, D, C, B]`. (`B` ist nun an seiner endgültigen Position fixiert).
2. `i = 2` (Element C).
   - Ziehe ein zufälliges `j` zwischen 0 und 2. Nehmen wir an, `j = 2` (Element C).
   - Tausche `nums[2]` und `nums[2]`. (Bleibt an Ort und Stelle!).
   - `nums = [A, D, C, B]`. (`C` ist nun fixiert).
3. `i = 1` (Element D).
   - Ziehe ein zufälliges `j` zwischen 0 und 1. Nehmen wir an, `j = 0` (Element A).
   - Tausche `nums[1]` und `nums[0]`.
   - `nums = [D, A, C, B]`. (`A` ist fixiert).

Die Schleife endet. Das verbleibende Element `D` an Index 0 ist trivialerweise fixiert.
Finales gemischtes Array: `[D, A, C, B]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Die Schleife läuft exakt N-1 Mal durch. Die Generierung der Zufallszahl und der Tauschvorgang benötigen $O(1)$ Zeit. Die Zeitkomplexität ist strikt $O(N)$.
Das gesamte Mischen erfolgt vollständig in-place. Die Platzkomplexität beträgt $O(1)$.

## Varianten & Optimierungen

- **Vorwärts-Iteration:** Man kann äquivalent `i` von 0 bis N-2 iterieren und ein zufälliges `j` zwischen `i` und N-1 wählen. Die Mathematik funktioniert exakt gleich und erzeugt eine "fixierte" Partition, die von links nach rechts wächst, anstatt von rechts nach links.

## Praxisanwendungen

- **Kryptographie:** Wird in der RC4-Stromchiffre verwendet, um die Permutationsmatrix (Key Scheduling Algorithm) gleichmäßig zu initialisieren.
- **Gaming:** Mischen von Playlists in Spotify oder Mischen von Kartenstapeln beim Online-Poker, um Fairness zu garantieren.

## Verwandte Algorithmen in cOde(n)

- **[randomized_02 - Reservoir Sampling](randomized_02_reservoir-sampling.md)** — Ein verwandtes Konzept zur Auswahl einer Teilmenge, anstatt das gesamte Set zu mischen.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*