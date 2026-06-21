# Suche in einem rotierten sortierten Array

| | |
|---|---|
| **ID** | `search_12` |
| **Kategorie** | searching |
| **Komplexität (erforderlich)** | $O(\log N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 10/10 |
| **LeetCode-Äquivalent** | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) |

## Problemstellung

Gegeben ist ein Integer-Array `nums`, das in aufsteigender Reihenfolge sortiert ist (mit eindeutigen Werten).
Bevor das Array an Ihre Funktion übergeben wird, wurde es möglicherweise an einem unbekannten Pivot-Index `k` **rotiert**.
Zum Beispiel könnte `[0,1,2,4,5,6,7]` am Pivot-Index 3 rotiert werden und zu `[4,5,6,7,0,1,2]` werden.
Geben Sie bei gegebenem Array `nums` nach der möglichen Rotation und einem Integer `target` den Index von `target` zurück, falls es in `nums` enthalten ist, oder `-1`, falls es nicht in `nums` enthalten ist.
Sie müssen einen Algorithmus mit einer Laufzeitkomplexität von $O(\log N)$ schreiben.

**Eingabe:** Ein rotiertes sortiertes Array `nums` und ein `target`-Wert.
**Ausgabe:** Ein Integer, der den Index repräsentiert.

## Wann man es verwendet

- Eine der berüchtigtsten und häufigsten Variationen der Binary Search in FAANG-Vorstellungsgesprächen.
- Testet Ihre Fähigkeit, logische Invarianten (Garantien) für die Hälfte eines Datensatzes aufzustellen, wenn der gesamte Datensatz leicht korrumpiert ist.

## Ansatz

**1. Die Garantie des rotierten Arrays:**
Bei einer Standard-Binary Search wählen wir einen `mid`-Punkt. Da das Array perfekt sortiert ist, wissen wir automatisch, in welcher Hälfte sich das `target` befinden muss.
In einem *rotierten* Array ist das Array nach der Wahl von `mid` NICHT MEHR perfekt sortiert!
ABER es gibt eine massive mathematische Garantie: **Wenn man ein rotiertes sortiertes Array in zwei Hälften teilt, ist IMMER genau EINE der beiden Hälften perfekt sortiert!**

Betrachten Sie `[4, 5, 6, 7, 0, 1, 2]`. Der `mid` ist `7`.
- Die linke Hälfte `[4, 5, 6, 7]` ist perfekt sortiert!
- Die rechte Hälfte `[7, 0, 1, 2]` ist korrumpiert.

Betrachten Sie `[6, 7, 0, 1, 2, 4, 5]`. Der `mid` ist `1`.
- Die linke Hälfte `[6, 7, 0, 1]` ist korrumpiert.
- Die rechte Hälfte `[1, 2, 4, 5]` ist perfekt sortiert!

**2. Die Logik der Invarianten-Eliminierung:**
Wir müssen herausfinden, *welche* Hälfte die sortierte ist.
Wir vergleichen einfach den Anfang des Arrays mit der Mitte! Wenn `nums[left] <= nums[mid]`, ist die linke Hälfte die perfekt sortierte. Andernfalls ist die rechte Hälfte die sortierte!

Sobald wir die perfekt sortierte Hälfte gefunden haben, haben wir eine saubere Umgebung! Wir prüfen, ob das `target` mathematisch innerhalb der Grenzen dieser sortierten Hälfte liegt.
- Wenn dies der Fall ist, verwerfen wir die korrumpierte Hälfte vollständig und führen eine Standard-Binary Search auf der sortierten Hälfte durch!
- Wenn dies NICHT der Fall ist, MUSS sich das `target` irgendwo in der korrumpierten Hälfte verstecken! Wir verwerfen die sortierte Hälfte und wiederholen den Vorgang für die korrumpierte Hälfte!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for search_12: Search in Rotated Sorted Array.

A sorted array that has been rotated at some unknown pivot.
Find the index of ``target`` (or -1) in O(log n) time.
Find the pivot (smallest element) first, then binary-search
the half that could contain the target.
"""


def solve(data, target, n):
    if n == 0:
        return -1
    low, high = 0, n - 1
    # Find the rotation pivot: the smallest element.
    while low < high:
        mid = (low + high) // 2
        if data[mid] > data[high]:
            low = mid + 1
        else:
            high = mid
    pivot = low
    # Decide which half to search.
    if pivot == 0:
        low, high = 0, n - 1
    elif data[0] <= target <= data[pivot - 1]:
        # Target is in the upper half (data[0..pivot-1]).
        low, high = 0, pivot - 1
    else:
        # Target is in the lower half (data[pivot..n-1]).
        low, high = pivot, n - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

</details>

## Durchlauf

`nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 0`. Länge 7.

1. `L=0, R=6, M=3`. `nums[3] = 7`.
   - `7 == 0`? Falsch.
   - Ist links sortiert? `nums[L] (4) <= nums[M] (7)` -> WAHR! Links ist sortiert `[4, 5, 6, 7]`.
   - Ist das `target` in der linken Hälfte? `4 <= 0 < 7` -> FALSCH! Das `target` ist nicht in der sortierten Hälfte.
   - Verwerfe die linke Hälfte. `L = M+1 = 4`.
2. `L=4, R=6, M=5`. `nums[5] = 1`.
   - `1 == 0`? Falsch.
   - Ist links sortiert? `nums[L] (0) <= nums[M] (1)` -> WAHR! Links ist sortiert `[0, 1]`.
   - Ist das `target` in der linken Hälfte? `0 <= 0 < 1` -> WAHR!
   - Das `target` ist in der sortierten Hälfte! Verwerfe die rechte Hälfte. `R = M-1 = 4`.
3. `L=4, R=4, M=4`. `nums[4] = 0`.
   - `0 == 0`! Treffer gefunden!
   - Gib `mid = 4` zurück.

Ergebnis: `4`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(\log N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(\log N)$ | $O(1)$ |

Obwohl das Array rotiert und teilweise korrumpiert ist, garantiert unser Algorithmus, dass wir bei jeder Iteration exakt 50 % des verbleibenden Suchraums verwerfen!
Daher bleibt die Zeitkomplexität identisch mit der einer unveränderten Binary Search: $O(\log N)$.
Die Platzkomplexität beträgt $O(1)$, da wir nur drei Integer-Pointer-Variablen verwenden.

## Varianten & Optimierungen

- **Search in Rotated Array II (mit Duplikaten):** Wenn das Array Duplikate enthalten kann (z. B. `[1, 0, 1, 1, 1]`), schlägt unsere Prüfung `nums[left] <= nums[mid]` FEHL! (1 ist \le 1, also denkt der Algorithmus, die linke Hälfte `[1, 0, 1]` sei sortiert, was falsch ist!). Um dies zu beheben, müssen Sie eine Prüfung hinzufügen: Wenn `nums[left] == nums[mid]`, kann man nicht sicher sein, welche Hälfte sortiert ist, also führt man `left += 1` aus, um das Duplikat manuell zu überspringen. Dies verschlechtert die Zeitkomplexität im schlechtesten Fall auf $O(N)$.
- **Find Minimum in Rotated Sorted Array:** Ein verwandtes Problem, bei dem das Ziel spezifisch darin besteht, den Pivot-Punkt (das kleinste Element) zu finden, anstatt ein beliebiges `target`.

## Anwendungen in der Praxis

- **Circular Buffers / Ring Buffers:** Datenströme (wie Audio-/Video-Rendering-Streams) werden oft in Arrays fester Größe gespeichert, bei denen der "Head" zum Index 0 zurückspringt, wenn er das Ende erreicht, wodurch effektiv ein permanent rotiertes sortiertes Array von Zeitstempeln entsteht.

## Verwandte Algorithmen in cOde(n)

- **[search_02 - Binary Search](search_02_binary-search.md)** — Der grundlegende Algorithmus, der hier stark modifiziert wird.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Seiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*