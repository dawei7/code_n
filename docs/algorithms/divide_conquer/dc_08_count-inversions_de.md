# Count Inversions

| | |
|---|---|
| **ID** | `dc_08` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(N \log N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **GeeksForGeeks Äquivalent** | [Count Inversions in an array](https://www.geeksforgeeks.org/inversion-count-in-array-using-merge-sort/) |

## Problemstellung

Gegeben ist ein Array von Ganzzahlen; finden Sie die Anzahl der Inversionen (Inversion Count) in diesem Array.
Zwei Elemente `a[i]` und `a[j]` bilden eine Inversion, wenn `a[i] > a[j]` und `i < j` gilt.
Einfacher ausgedrückt misst dies, wie weit (oder nah) das Array davon entfernt ist, vollständig sortiert zu sein. Wenn das Array bereits sortiert ist, beträgt die Anzahl der Inversionen 0. Wenn das Array in umgekehrter Reihenfolge sortiert ist, ist die Anzahl der Inversionen maximal.

**Eingabe:** Ein Integer-Array `arr`.
**Ausgabe:** Eine Ganzzahl, die die Gesamtzahl der Inversionen darstellt.

## Wann man es verwendet

- Um Ihr tiefgreifendes Verständnis von **Merge Sort** zu testen.
- Wenn Sie die "Unsortiertheit" quantifizieren oder den Kendall-Rangkorrelationskoeffizienten eines Datensatzes berechnen müssen.

## Ansatz

**1. Der Fehler bei $O(N^2)$-Prüfungen:**
Der naive Ansatz besteht darin, zwei verschachtelte `for`-Schleifen zu verwenden. Für jedes Element `i` werden alle Elemente `j` rechts davon überprüft. Wenn `arr[i] > arr[j]` gilt, wird ein Zähler erhöht. Dies benötigt $O(N^2)$ Zeit.

**2. Nutzung von Merge Sort:**
Eine Inversion tritt auf, wenn ein größeres Element *vor* einem kleineren Element erscheint.
Welcher Algorithmus ist explizit darauf ausgelegt, Elemente in der falschen Reihenfolge zu finden und sie physisch zu tauschen, bis sie sortiert sind? Merge Sort!
Wir können einen Standard-Merge Sort verwenden und einfach einen Zähler innerhalb der `merge`-Funktion hinzufügen!

**3. Der magische Zählschritt:**
Während des `merge`-Schritts haben wir ein `left_half`-Array und ein `right_half`-Array. Beide Hälften sind intern sortiert.
Wir verwenden zwei Pointer, `i` für `left_half` und `j` für `right_half`.
- Wenn `left_half[i] <= right_half[j]`: Sie sind in der richtigen Reihenfolge. Keine Inversion!
- Wenn `left_half[i] > right_half[j]`: Wir haben eine Inversion gefunden! Moment, wir haben nicht nur EINE Inversion gefunden... wir haben eine ganze Menge davon gefunden!
  Da `left_half` strikt sortiert ist, gilt: Wenn `left_half[i]` strikt größer als `right_half[j]` ist, dann MUSS JEDES EINZELNE ELEMENT rechts von `i` in der `left_half` ebenfalls größer als `right_half[j]` sein!
  Daher haben wir sofort `len(left_half) - i` Inversionen gefunden! Wir addieren dies direkt zu unserem Gesamtzähler.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dc_08: Count Inversions.

Count the number of inversions in an array of n
"""


def solve(arr, n):
    """Count inversions via merge sort."""
    if n <= 1:
        return 0
    work = list(arr)

    def sort_count(lo, hi):
        if lo >= hi:
            return 0
        mid = (lo + hi) // 2
        count = sort_count(lo, mid) + sort_count(mid + 1, hi)
        left = work[lo:mid + 1]
        right = work[mid + 1:hi + 1]
        i = j = 0
        k = lo
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                work[k] = left[i]
                i += 1
            else:
                work[k] = right[j]
                count += len(left) - i
                j += 1
            k += 1
        while i < len(left):
            work[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            work[k] = right[j]
            j += 1
            k += 1
        return count

    return sort_count(0, n - 1)
```

</details>

## Durchlauf

`arr = [2, 4, 1, 3]`.

1. Aufteilen in `[2, 4]` und `[1, 3]`.
2. **Linke Hälfte `[2, 4]`:**
   - Aufteilen in `[2]` und `[4]`.
   - Merge `[2]` und `[4]`:
     - `2 <= 4`. Addiere 2.
     - Addiere 4. `split_inv = 0`. Gibt `[2, 4]` zurück, inv=0.
3. **Rechte Hälfte `[1, 3]`:**
   - Aufteilen in `[1]` und `[3]`.
   - Merge `[1]` und `[3]`:
     - `1 <= 3`. Addiere 1.
     - Addiere 3. `split_inv = 0`. Gibt `[1, 3]` zurück, inv=0.
4. **Globaler Merge `[2, 4]` und `[1, 3]`:**
   - `i=0` (Wert 2), `j=0` (Wert 1).
   - `2 > 1`! INVERSION!
   - `split_inv += (len(left) - i)` -> `split_inv += (2 - 0)` -> `2` Inversionen gefunden! (Sowohl 2 als auch 4 sind > 1).
   - Addiere 1. `j` wird 1.
   - `i=0` (Wert 2), `j=1` (Wert 3).
   - `2 <= 3`. Addiere 2. `i` wird 1.
   - `i=1` (Wert 4), `j=1` (Wert 3).
   - `4 > 3`! INVERSION!
   - `split_inv += (len(left) - i)` -> `split_inv += (2 - 1)` -> `1` Inversion gefunden! (4 > 3).
   - Addiere 3. `j` wird 2.
   - `j` erschöpft. Addiere verbleibendes `[4]`.
   - Gesamt `split_inv = 3`.

Ergebnis `total_inversions = 0 + 0 + 3 = 3`. ✓
*(Die 3 Inversionen sind (2,1), (4,1), (4,3))*.

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N \log N)$ | $O(N)$ |

Da wir buchstäblich nur einen Standard-Merge Sort ausführen, ist die Zeitkomplexität in allen Fällen strikt auf $O(N \log N)$ begrenzt.
Die Platzkomplexität beträgt $O(N)$, da die Merge-Arrays auf jeder Ebene temporäre Kopien erstellen.

## Varianten & Optimierungen

- **Fenwick Tree / Binary Indexed Tree (BIT):** Sie können dies auch iterativ mit einem Fenwick Tree in $O(N \log N)$ Zeit lösen. Sie iterieren von rechts nach links durch das Array. Für jedes Element fragen Sie den Fenwick Tree ab, wie viele Elemente Sie *bereits verarbeitet* haben, die strikt kleiner als das aktuelle Element sind. Dann fügen Sie das aktuelle Element in den Fenwick Tree ein. Dies ist extrem elegant und erfordert $O(\text{Max\_Value})$ Platz oder eine Koordinatenkompression.
- **Reverse Pairs (LeetCode 493):** Eine schwierigere Variante, bei der eine Inversion als `nums[i] > 2 * nums[j]` definiert ist. Sie können IMMER NOCH Merge Sort verwenden! Sie müssen lediglich eine schnelle $O(N)$-Zählschleife *vor* der Standard-Merge-Pointer-Logik ausführen.

## Anwendungen in der Praxis

- **Collaborative Filtering / Empfehlungssysteme:** Berechnung der Kendall-Tau-Distanz zwischen den Ranglisten-Präferenzlisten zweier Benutzer. Wenn Benutzer A 5 Filme bewertet und Benutzer B sie anders einstuft, quantifiziert die Anzahl der Inversionen direkt, wie unterschiedlich ihre Geschmäcker sind!

## Verwandte Algorithmen in cOde(n)

- **[sort_01 - Merge Sort](../sorting/sort_01_merge-sort.md)** — Der reine Sortieralgorithmus ohne interne Zähler.
- **[fenwick_01 - Binary Indexed Tree](../fenwick/fenwick_01_binary-indexed-tree.md)** — Die alternative Datenstruktur, die in der Lage ist, Inversionen zu zählen.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*