# Vorkommen in sortiertem Array zählen

| | |
|---|---|
| **ID** | `search_11` |
| **Kategorie** | searching |
| **Komplexität (erforderlich)** | $O(\log N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) |

## Problemstellung

Gegeben ist ein sortiertes Array `arr` und ein `target`-Wert. Das Array kann doppelte Elemente enthalten.
Ermitteln Sie die Gesamtzahl der Vorkommen von `target` im Array.
Sie müssen dies mit einer Zeitkomplexität von $O(\log N)$ lösen.

**Eingabe:** Ein sortiertes Integer-Array `arr` und ein Integer `target`.
**Ausgabe:** Ein Integer, der die Gesamtzahl des `target` repräsentiert.

## Wann ist dies zu verwenden?

- Um die linke Grenze (Left Bound) und rechte Grenze (Right Bound) einer Sequenz von Duplikaten präzise zu bestimmen.
- Immer dann, wenn eine Standard-Binary Search fehlschlägt, weil Sie das *allererste* Vorkommen eines Elements benötigen und nicht irgendein beliebiges Vorkommen in der Mitte.

## Ansatz

**1. Der Fehler der Standard-Binary Search:**
Wenn `arr = [2, 2, 2, 2, 2]` und `target = 2` ist, findet die Standard-Binary Search die `2` am Index 2 und gibt diesen sofort zurück.
Wenn wir die Vorkommen zählen wollen, könnten wir eine `while`-Schleife schreiben, um ausgehend von Index 2 linear nach links und rechts zu scannen, um alle anderen `2`en zu finden.
ABER: Was, wenn das Array EINE MILLION `2`en enthält? Der lineare Scan würde 1.000.000 Operationen benötigen! Dies macht unseren $O(\log N)$-Algorithmus zu einem $O(N)$-Algorithmus und verletzt damit die Zeitvorgabe vollständig!

**2. Das erste Vorkommen finden (Lower Bound):**
Um strikt in $O(\log N)$-Zeit zu bleiben, müssen wir Binary Search verwenden, um den EXAKTEN Startindex des `target` zu finden.
Wir modifizieren die Standard-Binary Search: Wenn wir `arr[mid] == target` finden, **GEBEN WIR NICHT SOFORT ZURÜCK!**
Stattdessen denken wir: "Ich habe eine 2 gefunden. Aber es könnten noch weitere 2en links von mir sein!"
Also speichern wir diesen Index als potenzielle Antwort und verwerfen dann bewusst die rechte Hälfte des Arrays! `right = mid - 1`.
Wir führen dies fort. Der letzte Index, den wir vor Abbruch der Schleife gespeichert haben, ist garantiert das ERSTE Vorkommen!

**3. Das letzte Vorkommen finden (Upper Bound):**
Wir schreiben eine zweite, nahezu identische Binary Search.
Wenn wir `arr[mid] == target` finden, denken wir: "Ich habe eine 2 gefunden. Aber es könnten noch weitere 2en rechts von mir sein!"
Wir speichern den Index und verwerfen die linke Hälfte! `left = mid + 1`.
Der letzte gespeicherte Index ist garantiert das LETZTE Vorkommen!

**4. Die finale Zählung:**
Sobald wir `first_index` und `last_index` haben, ist die Gesamtzahl einfach `last_index - first_index + 1`.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for search_11: Count Occurrences (Sorted).

Sorted array; count how many times ``target`` appears. Two
binary searches: one for the first occurrence (lower_bound),
one for the last (upper_bound). Difference = count.
O(log n) time.
"""


def solve(data, target, n):
    if n == 0:
        return 0

    def lower_bound(lo, hi, t):
        while lo < hi:
            mid = (lo + hi) // 2
            if data[mid] < t:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def upper_bound(lo, hi, t):
        while lo < hi:
            mid = (lo + hi) // 2
            if data[mid] <= t:
                lo = mid + 1
            else:
                hi = mid
        return lo

    first = lower_bound(0, n, target)
    if first == n or data[first] != target:
        return 0
    last = upper_bound(first, n, target)
    return last - first
```

</details>

## Durchlauf

`arr = [1, 2, 2, 2, 2, 3, 4]`, `target = 2`. Länge 7.

**Erstes Vorkommen finden:**
1. `L=0, R=6, M=3`. `arr[3] = 2 == target`.
   - `first_idx = 3`. `R = M-1 = 2`.
2. `L=0, R=2, M=1`. `arr[1] = 2 == target`.
   - `first_idx = 1`. `R = M-1 = 0`.
3. `L=0, R=0, M=0`. `arr[0] = 1 < target`.
   - `L = M+1 = 1`.
4. `L=1, R=0`. `L <= R` ist falsch. Schleife endet. `first_idx = 1`.

**Letztes Vorkommen finden:**
1. `L=0, R=6, M=3`. `arr[3] = 2 == target`.
   - `last_idx = 3`. `L = M+1 = 4`.
2. `L=4, R=6, M=5`. `arr[5] = 3 > target`.
   - `R = M-1 = 4`.
3. `L=4, R=4, M=4`. `arr[4] = 2 == target`.
   - `last_idx = 4`. `L = M+1 = 5`.
4. `L=5, R=4`. `L <= R` ist falsch. Schleife endet. `last_idx = 4`.

Anzahl = `4 - 1 + 1 = 4`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(\log N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(\log N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(\log N)$ | $O(1)$ |

Wir führen exakt zwei separate Binary Searches nacheinander aus.
Jede Binary Search benötigt $O(\log N)$ Zeit.
Die Gesamtzeit beträgt $O(\log N + \log N) = O(2 \log N)$, was strikt durch $O(\log N)$ begrenzt ist.
Die Platzkomplexität ist $O(1)$, da wir nur Integer-Pointer-Variablen verwenden.

## Varianten & Optimierungen

- **C++ `std::lower_bound`:** In modernem C++ ist dieser exakte Algorithmus nativ in der Standardbibliothek enthalten! `std::lower_bound(arr, target)` gibt einen Pointer auf das *erste* Vorkommen zurück. `std::upper_bound(arr, target)` gibt einen Pointer auf das Element exakt *hinter* dem letzten Vorkommen zurück. Die Zählung ist so einfach wie `upper_bound - lower_bound`.
- **Python `bisect`:** Das Äquivalent in Pythons Standardbibliothek. `bisect.bisect_left()` findet den Index des ersten Vorkommens und `bisect.bisect_right()` findet das Element nach dem letzten Vorkommen.

## Praxisanwendungen

- **Log-Datei-Analyse:** Wenn Millionen von Server-Log-Einträgen nach Zeitstempel sortiert sind (z. B. `12:00:01`, `12:00:01`, `12:00:01`, `12:00:05`), zählt dieser Algorithmus schnell und präzise, wie viele Anfragen zu einer bestimmten Sekunde auftraten, ohne die gesamte Datei scannen zu müssen.

## Verwandte Algorithmen in cOde(n)

- **[search_02 - Binary Search](search_02_binary-search.md)** — Der grundlegende Algorithmus, auf dem dieser aufbaut.
- **[arrays_03 - Majority Element](../arrays/arrays_03_majority-element.md)** — Wenn das Array sortiert ist, kann dieser Algorithmus verwendet werden, um sofort zu prüfen, ob die Anzahl eines Elements > N/2 ist, was beweist, dass es ein Majority Element ist – in $O(\log N)$-Zeit anstelle der $O(N)$-Zeit des Boyer-Moore-Algorithmus!

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*