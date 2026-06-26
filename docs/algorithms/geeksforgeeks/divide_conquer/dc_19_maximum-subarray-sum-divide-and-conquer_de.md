# Maximum Subarray Sum (Divide and Conquer)

| | |
|---|---|
| **ID** | `dc_19` |
| **Category** | divide_conquer |
| **Complexity (required)** | $O(N \log N)$ Time, $O(\log N)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) |

## Problem statement

Gegeben ist ein Array `nums` von Ganzzahlen. Finden Sie das zusammenhängende Subarray (das mindestens eine Zahl enthält), welches die größte Summe aufweist, und geben Sie diese Summe zurück.
*Einschränkung:* Sie MÜSSEN das Problem mit dem Divide-and-Conquer-Ansatz lösen, anstatt den optimaleren $O(N)$ Kadane-Algorithmus zu verwenden.

**Input:** Ein Array `nums` von Ganzzahlen.
**Output:** Eine Ganzzahl, die die maximale Subarray-Summe repräsentiert.

## Wann man diesen Ansatz verwendet

- Wenn explizit verlangt wird, zu beweisen, dass Sie Array-Intervallprobleme auf einen Rekursionsbaum abbilden können.
- Wenn Sie mehrere Anfragen bezüglich des maximalen Subarrays in *unterschiedlichen* Bereichen des Arrays dynamisch beantworten müssen (in diesem Fall wird genau diese Logik verwendet, um einen Segment Tree aufzubauen).

## Ansatz

**1. Die räumliche Logik des Max Subarray:**
Wenn wir ein Array exakt in der Mitte teilen (linke Hälfte und rechte Hälfte), MUSS das globale maximale zusammenhängende Subarray an genau einer von drei Stellen existieren:
1. Es ist vollständig in der linken Hälfte enthalten.
2. Es ist vollständig in der rechten Hälfte enthalten.
3. Es überspannt die Trennlinie und erstreckt sich sowohl über die linke als auch über die rechte Hälfte!

**2. Der Divide-Schritt:**
Finden Sie den `mid`-Punkt.
Rufen Sie rekursiv `max_subarray(left, mid)` auf, um das beste Subarray strikt auf der linken Seite zu finden.
Rufen Sie rekursiv `max_subarray(mid + 1, right)` auf, um das beste Subarray strikt auf der rechten Seite zu finden.

**3. Der Conquer-Schritt (Die Crossing-Summe):**
Wie finden wir das maximale Subarray, das die Trennlinie überspannt?
Es MUSS `nums[mid]` und `nums[mid+1]` enthalten.
Daher starten wir bei `mid` und iterieren rückwärts nach links, wobei wir eine laufende Summe führen und die absolute maximale Summe aufzeichnen, die wir jemals erreichen. Nennen wir dies `max_left_cross`.
Dann starten wir bei `mid+1` und iterieren vorwärts nach rechts, führen ebenfalls eine laufende Summe und zeichnen die absolute maximale Summe auf. Nennen wir dies `max_right_cross`.
Die absolut beste Crossing-Subarray-Summe ist einfach `max_left_cross + max_right_cross`!

**4. Finale Auflösung:**
Geben Sie das Maximum der drei Möglichkeiten zurück: `Left Half Max`, `Right Half Max` oder die `Crossing Max`.

## Algorithmus

<details>
<summary>Show Algorithm</summary>

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

## Walk-through

`nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]`. N = 9.
Konzentrieren wir uns auf die Crossing-Berechnung für den obersten Split:
`left = 0`, `right = 8`, `mid = 4` (Wert `-1`).
Linke Hälfte: `[-2, 1, -3, 4, -1]`. Rechte Hälfte: `[2, 1, -5, 4]`.

1. **Berechne `max_left_cross` (von `mid=4` abwärts bis `0`):**
   - Index 4 (Wert -1): Summe = -1. `left_sum = -1`.
   - Index 3 (Wert 4): Summe = 3. `left_sum = 3`.
   - Index 2 (Wert -3): Summe = 0. `left_sum` bleibt `3`.
   - Index 1 (Wert 1): Summe = 1. `left_sum` bleibt `3`.
   - Index 0 (Wert -2): Summe = -1. `left_sum` bleibt `3`.
   - Die beste Summe nach links ist `3`.
2. **Berechne `max_right_cross` (von `mid=5` aufwärts bis `8`):**
   - Index 5 (Wert 2): Summe = 2. `right_sum = 2`.
   - Index 6 (Wert 1): Summe = 3. `right_sum = 3`.
   - Index 7 (Wert -5): Summe = -2. `right_sum` bleibt `3`.
   - Index 8 (Wert 4): Summe = 2. `right_sum` bleibt `3`.
   - Die beste Summe nach rechts ist `3`.
3. **Kombinieren:**
   - `cross_max = 3 + 3 = 6`.

*(Angenommen, die linke Hälfte lieferte 4 und die rechte Hälfte lieferte 4).*
Rückgabe `max(4, 4, 6) = 6`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(N \log N)$ | $O(\log N)$ |

Der Rekursionsbaum hat eine Tiefe von $\log_2 N$.
Auf jeder Ebene erfordert die Berechnung der Crossing-Summe eine lineare Iteration von der Mitte bis zu den Rändern. Über alle Knoten auf einer bestimmten Ebene des Baums hinweg wird das gesamte Array exakt einmal durchlaufen, was $O(N)$ Arbeit entspricht.
Nach dem Master-Theorem gilt T(N) = 2T(N/2) + $O(N)$ -> $O(N \log N)$.
Die Platzkomplexität beträgt $O(\log N)$ für den Rekursions-Stack.

## Varianten & Optimierungen

- **Kadane-Algorithmus ($O(N)$):** Der strikt überlegene Dynamic-Programming-Ansatz. `local_max = max(nums[i], local_max + nums[i])`, `global_max = max(global_max, local_max)`. Er führt eine laufende Summe und setzt diese auf 0 zurück, falls die Summe negativ wird. Erfordert nur $O(1)$ Platz.
- **Segment Tree ($O(N)$ Aufbau, $O(\log N)$ Abfrage):** Wenn Sie wiederholt die maximale Subarray-Summe für UNTERSCHIEDLICHE Bereiche innerhalb desselben Arrays abfragen müssen (z. B. "Was ist die maximale Summe zwischen Index 100 und 500?"), benötigt Kadane $O(N)$ pro Abfrage. Ein Segment Tree speichert `left_max`, `right_max`, `total_sum` und `global_max` für jeden Knoten in einem Binärbaum, was sofortige $O(\log N)$ Abfragen ermöglicht!

## Anwendungen in der Praxis

- **Finanzhandelssysteme:** Während Kadane für statische Arrays besser ist, wird die Divide-and-Conquer- bzw. Segment-Tree-Variante häufig in Echtzeit-Orderbüchern verwendet, um schnell den maximalen lokalisierten Preisrückgang oder Gewinnanstieg über beliebige, sich dynamisch ändernde historische Zeitfenster abzufragen.

## Verwandte Algorithmen in cOde(n)

- **[dp_06 - Kadane's Algorithm](../dynamic/dp_06_kadanes-algorithm.md)** — Der strikt überlegene $O(N)$ DP-Ansatz.
- **[dc_02 - Majority Element](dc_02_majority-element.md)** — Das identische algorithmische Grundgerüst (teilen, links rekursiv, rechts rekursiv, Crossing-Logik zusammenführen).

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*