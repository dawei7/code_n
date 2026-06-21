# Min und Max in einem Array (Turnier-Methode)

| | |
|---|---|
| **ID** | `dc_17` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(\log N)$ Platz |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **GeeksForGeeks Äquivalent** | [Maximum and minimum of an array using minimum number of comparisons](https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/) |

## Problemstellung

Gegeben ist ein Array der Größe `N`. Finden Sie sowohl das Maximum als auch das Minimum der Elemente im Array.
*Bedingung:* Sie müssen die absolute Anzahl der durchgeführten Vergleichsoperationen minimieren.

**Eingabe:** Ein Integer-Array `nums`.
**Ausgabe:** Ein Tupel `(min_val, max_val)`.

## Wann ist dies zu verwenden?

- Wenn Sie aufgefordert werden, den theoretischen konstanten Faktor eines linearen Suchalgorithmus zu optimieren.
- Als einführender Divide-and-Conquer-Algorithmus, der leichter zu verstehen ist als Merge Sort.

## Ansatz

**1. Die naive lineare Suche:**
Sie initialisieren `min_val = nums[0]` und `max_val = nums[0]`.
Für jedes Element prüfen Sie `if nums[i] < min_val` und anschließend `if nums[i] > max_val`.
Da Sie jedes Element zweimal gegen zwei Schranken prüfen, führen Sie 2N Vergleiche durch.
Geht das auch mit weniger?

**2. Die Divide-and-Conquer (Turnier-) Methode:**
Stellen Sie sich ein Armdrück-Turnier vor, um die stärkste und die schwächste Person zu finden.
Wenn wir das Array exakt in der Mitte teilen, können wir rekursiv das `(min, max)` der linken Hälfte und das `(min, max)` der rechten Hälfte finden.
Wenn die rekursiven Aufrufe zurückkehren, führen wir ein "Finale" durch:
- Das globale `min` ist das kleinere der beiden `min`-Werte aus links/rechts.
- Das globale `max` ist das größere der beiden `max`-Werte aus links/rechts.

Dies erfordert genau 2 Vergleiche, um die Hälften zusammenzuführen.

**3. Basisfälle:**
- Wenn der Array-Ausschnitt 1 Element enthält, geben Sie `(nums[0], nums[0])` zurück. (0 Vergleiche).
- Wenn der Array-Ausschnitt 2 Elemente enthält, vergleichen Sie diese! Geben Sie das kleinere als `min` und das größere als `max` zurück. (1 Vergleich).

*Mathematische Magie:* Durch die Gruppierung der Elemente in Paare im Basisfall und das Weiterreichen nur der Gewinner den Baum hinauf, sinkt die Gesamtzahl der Vergleiche mathematisch von 2N auf \frac{3N}{2} - 2.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dc_17: Min and Max (D&C tournament).

Given an array of n integers, return the minimum
"""


def solve(arr, n):
    """D&C tournament min/max. Returns [lo, hi]."""
    def rec(lo, hi):
        if lo == hi:
            return [arr[lo], arr[lo]]
        if hi == lo + 1:
            if arr[lo] < arr[hi]:
                return [arr[lo], arr[hi]]
            return [arr[hi], arr[lo]]
        mid = (lo + hi) // 2
        a = rec(lo, mid)
        b = rec(mid + 1, hi)
        return [min(a[0], b[0]), max(a[1], b[1])]
    return rec(0, n - 1)
```

</details>

## Durchlauf

`nums = [1000, 11, 445, 1, 330, 3000]`. N = 6.

1. Aufteilen in `[1000, 11, 445]` und `[1, 330, 3000]`.
2. **Linke Hälfte `[1000, 11, 445]`:**
   - Aufteilen in `[1000, 11]` und `[445]`.
   - `[1000, 11]` löst Basisfall 2 aus. (1 Vergleich). Gibt `(11, 1000)` zurück.
   - `[445]` löst Basisfall 1 aus. Gibt `(445, 445)` zurück.
   - Zusammenführen! `min(11, 445)` ist 11. `max(1000, 445)` ist 1000. (2 Vergleiche).
   - Linke Hälfte gibt `(11, 1000)` zurück.
3. **Rechte Hälfte `[1, 330, 3000]`:**
   - Aufteilen in `[1, 330]` und `[3000]`.
   - `[1, 330]` gibt `(1, 330)` zurück. (1 Vergleich).
   - `[3000]` gibt `(3000, 3000)` zurück.
   - Zusammenführen! `min(1, 3000)` ist 1. `max(330, 3000)` ist 3000. (2 Vergleiche).
   - Rechte Hälfte gibt `(1, 3000)` zurück.
4. **Globales Zusammenführen:**
   - `min(11, 1)` ist 1.
   - `max(1000, 3000)` ist 3000. (2 Vergleiche).

Gesamtzahl der Vergleiche: 8.
Vergleiche bei naiver linearer Suche: 2 x 6 = 12.
Wir haben den konstanten Faktor erfolgreich minimiert!

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(\log N)$ |

Die Zeitkomplexität ist strikt $O(N)$, da wir jedes Element verarbeiten. Die spezifische Rekurrenz lautet T(N) = 2T(N/2) + 2 Vergleiche. Gemäß dem Master-Theorem ergibt dies $O(N)$.
Die Platzkomplexität beträgt $O(\log N)$ aufgrund der Tiefe des rekursiven Aufruf-Stacks.

## Varianten & Optimierungen

- **Iterativer Paarvergleich:** Sie können die exakte Schranke von \frac{3N}{2} Vergleichen OHNE die Kosten für den $O(\log N)$ Rekursions-Stack erreichen!
  Initialisieren Sie `global_min` und `global_max`. Iterieren Sie in 2er-Schritten durch das Array. Vergleichen Sie für jedes Paar `(arr[i], arr[i+1])` diese zuerst miteinander!
  Nehmen Sie das kleinere Element und vergleichen Sie es nur mit `global_min`. Nehmen Sie das größere Element und vergleichen Sie es nur mit `global_max`.
  Dies sind 3 Vergleiche pro Elementpaar, was zu exakt \frac{3N}{2} Vergleichen bei $O(1)$ Platzbedarf führt.

## Anwendungen in der Praxis

- **Hardware-Architektur:** Physische Silizium-ALUs (Arithmetic Logic Units), die Vektor-/SIMD-Instruktionen verarbeiten, implementieren genau diese baumstrukturierte Reduktion, um Min/Max-Werte über Hardware-Register hinweg zu finden, da die Vergleiche in einer Binärbaum-Schaltung vollständig parallel ausgeführt werden können.

## Verwandte Algorithmen in cOde(n)

- **[dc_02 - Majority Element](dc_02_majority-element.md)** — Ein weiterer Algorithmus, bei dem grundlegende Array-Eigenschaften in einem binären Rekursionsbaum zusammengeführt werden.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*