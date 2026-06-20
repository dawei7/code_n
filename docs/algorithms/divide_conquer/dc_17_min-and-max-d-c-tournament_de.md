# Min und Max in einem Array (Turniermethode)

| | |
|---|---|
| **ID** | `dc_17` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(\log N)$ Speicherplatz |
| **Schwierigkeitsgrad** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 4/10 |
| **GeeksForGeeks-Äquivalent** | [Maximum und Minimum eines Arrays mit minimaler Anzahl an Vergleichen](https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/) |

## Aufgabenstellung

Gegeben ist ein Array der Größe `N`. Finde sowohl das größte als auch das kleinste Element im Array.
*Einschränkung:* Du musst die absolute Anzahl der durchgeführten Vergleichsoperationen minimieren.

**Eingabe:** Ein Array aus ganzen Zahlen `nums`.
**Ausgabe:** Ein Tupel `(min_val, max_val)`.

## Wann man es verwendet

- Wenn man aufgefordert wird, den theoretischen konstanten Faktor eines linearen Scan-Algorithmus zu optimieren.
- Ein einführender „Teile und herrsche“-Algorithmus, der leichter zu verstehen ist als der Mergesort.

## Vorgehensweise

**1. Der naive lineare Scan:**
Sie initialisieren `min_val = nums[0]` und `max_val = nums[0]`.
Für jedes Element prüfen Sie `if nums[i] < min_val` und anschließend `if nums[i] > max_val`.
Da jedes Element zweimal anhand zweier Grenzen überprüft wird, führt man 2N Vergleiche durch.
Können wir die Anzahl reduzieren?

**2. Die „Teile und herrsche“-Methode (Turnier):**
Stellen Sie sich ein Armdrück-Turnier vor, bei dem die stärkste und die schwächste Person ermittelt werden sollen.
Wenn wir das Array genau in der Mitte teilen, können wir rekursiv den `(min, max)` der linken Hälfte und den `(min, max)` der rechten Hälfte ermitteln.
Wenn die rekursiven Aufrufe zurückkehren, haben wir einfach ein „Finale“:
- Das globale `min` ist der kleinere der beiden linken/rechten `min`-Werte.
- Das globale `max` ist der größere der beiden linken/rechten `max`-Werte.

Dies erfordert genau 2 Vergleiche, um die Hälften zusammenzuführen.

**3. Basisfälle:**
- Wenn der Array-Ausschnitt 1 Element enthält, gib `(nums[0], nums[0])` zurück. (0 Vergleiche).
- Wenn der Array-Ausschnitt 2 Elemente enthält, vergleiche sie! Gib das kleinere als `min` und das größere als `max` zurück. (1 Vergleich).

*Mathematische Magie:* Indem im Basisfall Elemente zu Paaren gruppiert und nur die Gewinner im Baum weiterverarbeitet werden, sinkt die Gesamtzahl der Vergleiche mathematisch von 2N auf \frac{3N}{2} - 2.

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

## Schritt-für-Schritt-Anleitung

`nums = [1000, 11, 445, 1, 330, 3000]`. N = 6.

1. Aufteilen in `[1000, 11, 445]` und `[1, 330, 3000]`.
2. **Linke Hälfte `[1000, 11, 445]`:**
   - Aufteilen in `[1000, 11]` und `[445]`.
   - `[1000, 11]` löst den Basisfall 2 aus. (1 Vergleich). Gibt `(11, 1000)` zurück.
   - `[445]` löst den Basisfall 1 aus. Gibt `(445, 445)` zurück.
   - Zusammenführen! `min(11, 445)` ist 11. `max(1000, 445)` ist 1000. (2 Vergleiche).
   - Die linke Hälfte gibt `(11, 1000)` zurück.
3. **Rechte Hälfte `[1, 330, 3000]`:**
   - Aufteilung in `[1, 330]` und `[3000]`.
   - `[1, 330]` gibt `(1, 330)` zurück. (1 Vergleich).
   - `[3000]` gibt `(3000, 3000)` zurück.
   - Zusammenführen! `min(1, 3000)` ist 1. `max(330, 3000)` ist 3000. (2 Vergleiche).
   - Die rechte Hälfte gibt `(1, 3000)` zurück.
4. **Globales Zusammenführen:**
   - `min(11, 1)` ist 1.
   - `max(1000, 3000)` ist 3000. (2 Vergleiche).

Gesamtzahl der Vergleiche: 8.
Vergleiche beim naiven linearen Durchlauf: 2 × 6 = 12.
Wir haben den konstanten Faktor erfolgreich minimiert!

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(\log N)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(\log N)$ |
| **Schlechtester Fall** | $O(N)$ | $O(\log N)$ |

Die Zeitkomplexität beträgt streng $O(N)$, da wir jedes Element verarbeiten. Die spezifische Rekursionsbeziehung lautet T(N) = 2T(N/2) + 2 Vergleiche. Gemäß dem Master-Theorem ist dies $O(N)$.
Die Platzkomplexität beträgt $O(\log N)$ aufgrund der Tiefe des rekursiven Aufrufstapels.

## Varianten & Optimierungen

- **Iterativer Paarvergleich:** Man kann genau dieselbe Vergleichsgrenze von \frac{3N}{2} erreichen, OHNE den Speicherplatzaufwand des $O(\log N)$-Rekursionsstapels!
  Initialisiere `global_min` und `global_max`. Durchlaufen Sie das Array in Schritten von 2. Vergleichen Sie für jedes Paar `(arr[i], arr[i+1])` zunächst die beiden Elemente UNTEREINANDER!
  Nehmen Sie das kleinere Element und vergleichen Sie es nur mit `global_min`. Nimm den größeren Wert und vergleiche ihn nur mit `global_max`.
  Das sind 3 Vergleiche pro Elementepaar, was genau \frac{3N}{2} Vergleiche auf dem $O(1)$-Speicherplatz ergibt.

## Anwendungen in der Praxis

- **Hardwarearchitektur:** Physikalische Silizium-ALUs (Arithmetic Logic Units), die Vektor-/SIMD-Befehle verarbeiten, implementieren genau diese baumstrukturierte Reduktion, um Min-/Max-Werte über Hardware-Register hinweg zu ermitteln, da die Vergleiche in einer Binärbaumschaltung vollständig parallel ausgeführt werden können.

## Verwandte Algorithmen in cOde(n)

- **[dc_02 – Majority Element](dc_02_majority-element.md)** — Ein weiterer Algorithmus, bei dem grundlegende Array-Eigenschaften über einen binären Rekursionsbaum wieder zusammengeführt werden.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
nach dem Vorbild der kanonischen Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
