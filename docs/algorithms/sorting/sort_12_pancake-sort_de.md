# Pancake Sort

| | |
|---|---|
| **ID** | `sort_12` |
| **Kategorie** | sorting |
| **Komplexität (erforderlich)** | $O(N^2)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 2/10 |
| **LeetCode-Äquivalent** | [Pancake Sorting](https://leetcode.com/problems/pancake-sorting/) |

## Problemstellung

Gegeben ist ein Array von Integern `arr`. Sortieren Sie das Array in aufsteigender Reihenfolge.
Sie dürfen das Array AUSSCHLIESSLICH durch eine einzige spezifische Operation modifizieren: `flip(k)`.
Eine `flip(k)`-Operation kehrt das Sub-Array `arr[0...k]` um.
Geben Sie die Sequenz der `k`-Werte zurück, die das Array sortieren.

**Eingabe:** Ein unsortiertes Array von Integern `arr`.
**Ausgabe:** Ein Array von Integern, das die Flip-Größen repräsentiert.

## Wann man es verwendet

- Eher ein logisches Rätsel als ein praktischer Algorithmus.
- Historisch berühmt, da Bill Gates' EINZIGE veröffentlichte wissenschaftliche Arbeit (geschrieben während seiner Zeit in Harvard) eine Optimierung der mathematischen Schranken des Pancake Sortings war!

## Ansatz

**1. Die Pfannenwender-Analogie:**
Stellen Sie sich einen unordentlichen Stapel Pfannkuchen unterschiedlicher Größe vor. Sie möchten den größten Pfannkuchen ganz unten und den kleinsten ganz oben haben.
Sie haben nur ein Werkzeug: einen Pfannenwender. Sie können den Pfannenwender unter den k-ten Pfannkuchen von oben schieben und den gesamten Stapel, der auf dem Pfannenwender liegt, komplett umdrehen!

**2. Die "Move to End"-Strategie:**
Wie bekommen wir den absolut größten Pfannkuchen ganz nach unten auf den Stapel?
1. Zuerst finden wir den größten Pfannkuchen. Angenommen, er befindet sich an Index `i`.
2. Wir schieben den Pfannenwender darunter und führen `flip(i)` aus.
3. Jetzt befindet sich der größte Pfannkuchen an Index `0` (ganz oben auf dem Stapel)!
4. Wir schieben den Pfannenwender unter den GESAMTEN Stapel: `flip(N-1)`.
5. Der gesamte Stapel wird umgekehrt, wodurch der größte Pfannkuchen perfekt ganz unten (Index `N-1`) platziert wird!

**3. Verkleinerung des Stapels:**
Da der größte Pfannkuchen nun perfekt an der Unterseite platziert ist, tun wir so, als wäre der Stapel um einen Pfannkuchen kürzer!
Wir finden den *zweitgrößten* Pfannkuchen im verbleibenden Stapel (Indizes `0` bis `N-2`).
Wir führen einen `flip` aus, um ihn an die Spitze (`0`) zu bringen, und dann einen `flip`, um ihn an das Ende des aktiven Stapels (`N-2`) zu befördern.
Wir wiederholen diesen Prozess, bis die Größe des aktiven Stapels auf 1 geschrumpft ist.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for sort_12: Pancake Sort.

The only allowed operation is ``reverse prefix [0..k]`` for
some k. For each pass, find the maximum in the current
unsorted prefix, flip it to the front, then flip the prefix
to drop the max to the end. O(n^2) flips.
"""


def solve(data, n):
    def flip(end):
        start = 0
        while start < end:
            data[start], data[end] = data[end], data[start]
            start += 1
            end -= 1

    size = n
    while size > 1:
        # Find index of the maximum element in data[0..size-1].
        max_idx = 0
        for i in range(1, size):
            if data[i] > data[max_idx]:
                max_idx = i
        if max_idx != size - 1:
            if max_idx != 0:
                flip(max_idx)
            flip(size - 1)
        size -= 1
    return data
```

</details>

## Durchlauf

`arr = [3, 2, 4, 1]`. `N = 4`. `result = []`.

**Iteration 1 (`curr_size = 4`):**
1. Das größte Element in `[3, 2, 4, 1]` ist `4` an `max_idx = 2`.
2. `max_idx != 0`. `flip(2)`!
   - Umkehrung von `arr[0...2]`: `[4, 2, 3, 1]`.
   - `result.append(3)`.
3. `flip(3)` (der gesamte aktive Stapel)!
   - Umkehrung von `arr[0...3]`: `[1, 3, 2, 4]`.
   - `result.append(4)`.
Das größte Element `4` ist nun perfekt an der letzten Position!

**Iteration 2 (`curr_size = 3`):**
1. Das größte Element in `[1, 3, 2]` ist `3` an `max_idx = 1`.
2. `max_idx != 0`. `flip(1)`!
   - Umkehrung von `arr[0...1]`: `[3, 1, 2, 4]`.
   - `result.append(2)`.
3. `flip(2)` (der aktive Stapel)!
   - Umkehrung von `arr[0...2]`: `[2, 1, 3, 4]`.
   - `result.append(3)`.
`3` ist nun perfekt an der richtigen Stelle!

**Iteration 3 (`curr_size = 2`):**
1. Das größte Element in `[2, 1]` ist `2` an `max_idx = 0`.
2. `max_idx == 0`! Es muss nicht an die Spitze geflippt werden!
3. `flip(1)` (der aktive Stapel)!
   - Umkehrung von `arr[0...1]`: `[1, 2, 3, 4]`.
   - `result.append(2)`.
`2` ist nun perfekt an der richtigen Stelle!

Das Array ist vollständig sortiert: `[1, 2, 3, 4]`. ✓
Sequenz der `k`-Flips: `[3, 4, 2, 3, 2]`.

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N^2)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N^2)$ | $O(1)$ |

Das Finden des maximalen Elements erfordert einen linearen Scan in $O(N)$.
Das Umkehren des Arrays benötigt $O(N)$ Operationen.
Da wir diesen Prozess N-mal wiederholen müssen (einmal für jede Pfannkuchengröße), sind die gesamten Operationen durch $O(N \times (N + N)) = O(N^2)$ begrenzt.
Die maximale Anzahl an `flip`-Operationen, die erforderlich ist, um einen beliebigen Stapel der Größe N zu sortieren, ist mathematisch als \le \frac{18}{11}N bewiesen.
Die Platzkomplexität beträgt $O(1)$ für das Sortieren des Arrays, obwohl die LeetCode-Variante ein $O(N)$-Array benötigt, um die Folge der Antworten zu speichern.

## Varianten & Optimierungen

- **Burnt Pancake Sort:** Eine berüchtigt schwierige mathematische Variante, bei der jeder Pfannkuchen auf einer Seite verbrannt ist. Sie müssen den Stapel nach Größe sortieren UND sicherstellen, dass bei jedem Pfannkuchen die verbrannte Seite vollständig nach unten zeigt!

## Anwendungen in der Praxis

- **Genetik:** Die mathematischen Operationen des Pancake Sortings modellieren perfekt das biologische Phänomen der "Chromosomen-Inversionen", bei denen sich DNA-Segmente physisch ablösen, umkehren und wieder in das Genom einfügen!

## Verwandte Algorithmen in cOde(n)

- **[sort_02 - Selection Sort](sort_02_selection-sort.md)** — Der am nächsten verwandte Standard-Sortieralgorithmus, der ebenfalls nach dem maximalen Element sucht und es direkt an das Ende des Arrays verschiebt, wodurch die aktive Grenze verkleinert wird.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*