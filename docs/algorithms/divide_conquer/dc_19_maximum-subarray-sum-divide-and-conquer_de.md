# Maximale Summe eines Teilarrays (Teile und herrsche)

| | |
|---|---|
| **ID** | `dc_19` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(N \log N)$ Zeit, $O(\log N)$ Speicherplatz |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 6/10 |
| **LeetCode-Äquivalent** | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) |

## Aufgabenstellung

Gegeben ist ein Ganzzahl-Array `nums`. Finde das zusammenhängende Teilarray (das mindestens eine Zahl enthält), das die größte Summe aufweist, und gib dessen Summe zurück.
*Einschränkung:* Sie MÜSSEN die Aufgabe mit dem „Teile und herrsche“-Ansatz lösen und dürfen nicht den optimaleren $O(N)$ Kadane-Algorithmus verwenden.

**Eingabe:** Ein Array aus ganzen Zahlen `nums`.
**Ausgabe:** Eine ganze Zahl, die die maximale Summe des Teilarrays angibt.

## Wann man diese Methode anwendet

- Wenn ausdrücklich verlangt wird, zu beweisen, dass man Array-Intervall-Probleme auf einen Rekursionsbaum abbilden kann.
- Wenn Sie mehrere Abfragen zum maximalen Teilarray in *verschiedenen* Bereichen des Arrays dynamisch beantworten müssen (in diesem Fall wird genau diese Logik zum Aufbau eines Segmentbaums verwendet).

## Vorgehensweise

**1. Die räumliche Logik des maximalen Teilarrays:**
Wenn wir ein Array genau in zwei Hälften teilen (linke Hälfte und rechte Hälfte), MUSS das globale maximale zusammenhängende Teilarray an genau einer von drei Stellen liegen:
1. Es befindet sich vollständig in der linken Hälfte.
2. Es befindet sich vollständig in der rechten Hälfte.
3. Es erstreckt sich über die Trennlinie hinweg und umfasst sowohl die linke als auch die rechte Hälfte!

**2. Der Teilungsschritt:**
Finde den Punkt `mid`.
Rufe rekursiv `max_subarray(left, mid)` auf, um das beste Teilarray streng links davon zu finden.
Rufe rekursiv `max_subarray(mid + 1, right)` auf, um das beste Teilarray streng rechts zu finden.

**3. Der Eroberungsschritt (die Kreuzungssumme):**
Wie finden wir das maximale Teilarray, das die Trennlinie überspannt?
Es MUSS `nums[mid]` und `nums[mid+1]` enthalten.
Also beginnen wir bei `mid` und iterieren rückwärts nach links, wobei wir eine laufende Summe führen und die absolut höchste Summe notieren, die wir jemals erreichen. Nennen wir diese `max_left_cross`.
Dann beginnen wir bei `mid+1` und iterieren vorwärts nach rechts, wobei wir eine laufende Summe führen und die absolut höchste Summe notieren, die wir jemals erreicht haben. Nennen wir diese `max_right_cross`.
Die absolut beste Summe der überkreuzenden Teilsequenz ist ganz einfach `max_left_cross + max_right_cross`!

**4. Endgültiges Ergebnis:**
Gib das Maximum der drei Möglichkeiten zurück: `Left Half Max`, `Right Half Max` oder `Crossing Max`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dc_19: Maximum Subarray Sum (Divide and Conquer).

Given an array of n integers (with at least one
"""


def solve(arr, n):
    """Maximum subarray sum via divide and conquer."""

    def rec(lo, hi):
        if lo == hi:
            return arr[lo]
        mid = (lo + hi) // 2
        # Best fully in the left half.
        left_best = rec(lo, mid)
        # Best fully in the right half.
        right_best = rec(mid + 1, hi)
        # Best crossing the middle: extend leftward from mid,
        # then rightward from mid+1, and combine.
        s = 0
        left_sum = arr[mid]
        for i in range(mid, lo - 1, -1):
            s += arr[i]
            if s > left_sum:
                left_sum = s
        s = 0
        right_sum = arr[mid + 1]
        for i in range(mid + 1, hi + 1):
            s += arr[i]
            if s > right_sum:
                right_sum = s
        cross = left_sum + right_sum
        return max(left_best, right_best, cross)

    return rec(0, n - 1)
```

</details>

## Schritt-für-Schritt-Anleitung

`nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`. N = 9.
Konzentrieren wir uns auf die Kreuzungsberechnung für die oberste Teilungsebene:
`left = 0`, `right = 8`, `mid = 4` (val `-1`).
Linke Hälfte: `[-2, 1, -3, 4, -1]`. Rechte Hälfte: `[2, 1, -5, 4]`.

1. **Berechne `max_left_cross` (von `mid=4` bis `0`):**
   - Index 4 (Wert -1): Summe = -1. `left_sum = -1`.
   - Index 3 (Wert 4): Summe = 3. `left_sum = 3`.
   - Index 2 (Wert -3): Summe = 0. `left_sum` bleibt `3`.
   - Index 1 (Wert 1): Summe = 1. `left_sum` bleibt `3`.
   - Index 0 (Wert -2): Summe = -1. `left_sum` bleibt `3`.
   - Die beste Summe nach links ist `3`.
2. **Berechne `max_right_cross` (von `mid=5` bis `8`):**
   - Index 5 (Wert 2): Summe = 2. `right_sum = 2`.
   - Index 6 (Wert 1): Summe = 3. `right_sum = 3`.
   - Index 7 (Wert -5): Summe = -2. `right_sum` bleibt `3`.
   - Index 8 (Wert 4): Summe = 2. `right_sum` bleibt `3`.
   - Die beste Summe auf der rechten Seite ist `3`.
3. **Kombinieren:**
   - `cross_max = 3 + 3 = 6`.

*(Angenommen, die linke Hälfte hat 4 zurückgegeben und die rechte Hälfte 4).*
Gib `max(4, 4, 6) = 6` zurück. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(N \log N)$ | $O(\log N)$ |

Der Rekursionsbaum hat eine Tiefe von log₂ N.
Auf jeder Ebene erfordert die Berechnung der Kreuzungssumme eine lineare Iteration von der Mitte zu den Rändern. Über alle Knoten einer bestimmten Ebene des Baums hinweg wird das gesamte Array genau einmal durchlaufen, was einen Aufwand von $O(N)$ verursacht.
Nach dem Master-Theorem gilt T(N) = 2T(N/2) + $O(N)$ -> $O(N \log N)$.
Die Platzkomplexität beträgt $O(\log N)$ für den Rekursionsaufrufstapel.

## Varianten & Optimierungen

- **Kadane-Algorithmus ($O(N)$):** Der streng überlegene Ansatz der dynamischen Programmierung. `local_max = max(nums[i], local_max + nums[i])`, `global_max = max(global_max, local_max)`. Er verwaltet eine laufende Summe und setzt diese auf 0 zurück, wenn die Summe negativ wird. Benötigt nur $O(1)$ Speicherplatz.
- **Segment Tree ($O(N)$ Aufbau, $O(\log N)$ Abfrage):** Wenn Sie wiederholt die maximale Teilarray-Summe für VERSCHIEDENE Bereiche innerhalb desselben Arrays abfragen müssen (z. B. „Wie lautet die maximale Summe zwischen Index 100 und 500?“), benötigt Kadanes Algorithmus $O(N)$ pro Abfrage. Ein Segment Tree speichert die Werte `left_max`, `right_max`, `total_sum` und `global_max` für jeden Knoten in einem binären Baum und ermöglicht so $O(\log N)$ sofortige Abfragen!

## Praktische Anwendungen

- **Finanzhandelssysteme:** Während sich der Kadane-Algorithmus besser für statische Arrays eignet, wird die Variante „Teile und herrsche“ mit Segment Tree in Echtzeit-Orderbüchern intensiv genutzt, um schnell den maximalen lokalen Kursrückgang oder Gewinnanstieg über beliebige, sich dynamisch ändernde historische Zeitfenster abzufragen.

## Verwandte Algorithmen in cOde(n)

- **[dp_06 – Kadanes Algorithmus](../dynamic/dp_06_kadanes-algorithm.md)** — Der streng überlegene $O(N)$ DP-Ansatz.
- **[dc_02 – Majority Element](dc_02_majority-element.md)** — Das identische algorithmische Grundgerüst (Teilen, links rekursiv, rechts rekursiv, Zusammenführen mit Kreuzungslogik).

---

*Diese Dokumentation ist ein Originalbeitrag für cOde(n),
der sich an der kanonischen Struktur orientiert, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
