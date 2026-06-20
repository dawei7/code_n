# Inversionen zählen

| | |
|---|---|
| **ID** | `dc_08` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(N \log N)$ Zeit, $O(N)$ Speicherplatz |
| **Schwierigkeitsgrad** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 7/10 |
| **GeeksForGeeks-Äquivalent** | [Anzahl der Inversionen in einem Array](https://www.geeksforgeeks.org/inversion-count-in-array-using-merge-sort/) |

## Aufgabenstellung

Gegeben ist ein Array aus ganzen Zahlen. Ermitteln Sie die Anzahl der Inversionen im Array.
Zwei Elemente `a[i]` und `a[j]` bilden eine Inversion, wenn `a[i] > a[j]` und `i < j`.
Einfacher ausgedrückt: Es misst, wie weit (oder nah) das Array davon entfernt ist, vollständig sortiert zu sein. Ist das Array bereits sortiert, beträgt die Anzahl der Inversionen 0. Ist das Array in umgekehrter Reihenfolge sortiert, ist die Anzahl der Inversionen maximal.

**Eingabe:** Ein Array aus ganzen Zahlen `arr`.
**Ausgabe:** Eine Ganzzahl, die die Gesamtzahl der Inversionen angibt.

## Wann man es verwendet

- Um dein tiefgreifendes Verständnis von **Merge Sort** zu testen.
- Wenn du den Grad der „Unsortiertheit“ quantifizieren oder den Kendall-Rangkorrelationskoeffizienten eines Datensatzes berechnen musst.

## Vorgehensweise

**1. Der Fehler bei den $O(N^2)$-Prüfungen:**
Der naive Ansatz besteht darin, zwei verschachtelte `for`-Schleifen zu verwenden. Für jedes Element `i` werden alle Elemente `j` rechts davon überprüft. Ist `arr[i] > arr[j]`, wird ein Zähler erhöht. Dies dauert $O(N^2)$ Zeit.

**2. Auf dem Merge-Sort „mitreiten“:**
Eine Inversion liegt vor, wenn ein größeres Element *vor* einem kleineren Element auftritt.
Welcher Algorithmus ist ausdrücklich darauf ausgelegt, Elemente in falscher Reihenfolge zu finden und sie physisch auszutauschen, bis sie in der richtigen Reihenfolge sind? Der Mergesort!
Wir können einen Standard-Mergesort verwenden und einfach einen Zähler in die Funktion `merge` einfügen!

**3. Der magische Zählschritt:**
Während des `merge`-Schritts haben wir ein `left_half`-Array und ein `right_half`-Array. Beide Hälften sind intern sortiert.
Wir verwenden zwei Zeiger: `i` für `left_half` und `j` für `right_half`.
- Wenn `left_half[i] <= right_half[j]`: Sie sind in der richtigen Reihenfolge. Keine Inversion!
- Wenn `left_half[i] > right_half[j]`: Wir haben eine Inversion gefunden! Moment, wir haben nicht nur EINE Inversion gefunden … wir haben eine ganze Menge davon gefunden!
  Da `left_half` streng sortiert ist, gilt: Wenn `left_half[i]` streng größer als `right_half[j]` ist, MUSS JEDES EINZELNE ELEMENT rechts von `i` in `left_half` ebenfalls größer als `right_half[j]` sein!
  Daher haben wir sofort `len(left_half) - i` Inversionen gefunden! Wir addieren dies direkt zu unserem Gesamtzähler hinzu.

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

## Schritt-für-Schritt-Anleitung

`arr = [2, 4, 1, 3]`.

1. Aufteilen in `[2, 4]` und `[1, 3]`.
2. **Linke Hälfte `[2, 4]`:**
   - Aufteilen in `[2]` und `[4]`.
   - `[2]` und `[4]` zusammenführen:
 - `2 <= 4`. 2 hinzufügen.
 - 4 hinzufügen. `split_inv = 0`. Gibt `[2, 4]` zurück, inv=0.
3. **Rechte Hälfte `[1, 3]`:**
   - Aufteilen in `[1]` und `[3]`.
   - Zusammenführen von `[1]` und `[3]`:
 - `1 <= 3`. Add 1.
 - Add 3. `split_inv = 0`. Gibt `[1, 3]` zurück, inv=0.
4. **Globale Zusammenführung von `[2, 4]` und `[1, 3]`:**
   - `i=0` (Wert 2), `j=0` (Wert 1).
   - `2 > 1`! INVERSION!
   - `split_inv += (len(left) - i)` -> `split_inv += (2 - 0)` -> `2` Inversionen gefunden! (Sowohl 2 als auch 4 sind > 1).
   - 1 addieren. `j` wird zu 1.
   - `i=0` (Wert 2), `j=1` (Wert 3).
   - `2 <= 3`. 2 addieren. `i` wird zu 1.
   - `i=1` (Wert 4), `j=1` (Wert 3).
   - `4 > 3`! INVERSION!
   - `split_inv += (len(left) - i)` -> `split_inv += (2 - 1)` -> `1` Inversion gefunden! (4 > 3).
   - 3 hinzufügen. `j` wird zu 2.
   - `j` erschöpft. Verbleibendes `[4]` hinzufügen.
   - Gesamt `split_inv = 3`.

Ergebnis `total_inversions = 0 + 0 + 3 = 3`. ✓
*(Die 3 Inversionen sind (2,1), (4,1), (4,3))*.

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N \log N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N \log N)$ | $O(N)$ |

Da wir buchstäblich nur ein Standard-Merge-Sort ausführen, ist die Zeitkomplexität in allen Fällen streng auf $O(N \log N)$ begrenzt.
Die Platzkomplexität beträgt $O(N)$, da die Merge-Arrays auf jeder Ebene temporäre Kopien erstellen.

## Varianten & Optimierungen

- **Fenwick Tree / Binärindizierter Baum (BIT):** Man kann diese Aufgabe auch iterativ mithilfe eines Fenwick-Baums in $O(N \log N)$ Zeit lösen. Man durchläuft das Array von rechts nach links. Für jedes Element fragt man den Fenwick Tree ab, um zu sehen, wie viele Elemente, die streng kleiner als das aktuelle Element sind, man *bereits verarbeitet* hat. Anschließend fügen Sie das aktuelle Element in den Fenwick Tree ein. Dies ist äußerst elegant und erfordert $O(\text{Max\_Value})$ Speicherplatz oder Koordinatenkompression.
- **Reverse Pairs (LeetCode 493):** Eine schwierigere Variante, bei der eine Inversion wie in `nums[i] > 2 * nums[j]` definiert ist. Du kannst TROTZDEM Merge-Sort verwenden! Du musst lediglich *vor* der Ausführung der Standardlogik für den Merge-Zeiger eine kurze $O(N)$ Zählschleife durchführen.

## Anwendungen in der Praxis

- **Kollaboratives Filtern / Empfehlungssysteme:** Berechnung des Kendall-Tau-Abstands zwischen den bewerteten Präferenzlisten zweier Nutzer. Wenn Nutzer A 5 Filme bewertet und Nutzer B diese anders bewertet, quantifiziert die Anzahl der Inversionen direkt, wie unterschiedlich ihre Vorlieben sind!

## Verwandte Algorithmen in cOde(n)

- **[sort_01 – Merge-Sort](../sorting/sort_01_merge-sort.md)** — Der reine Sortieralgorithmus ohne interne Zähler.
- **[fenwick_01 – Binärindizierter Baum](../fenwick/fenwick_01_binary-indexed-tree.md)** — Die alternative Datenstruktur, mit der sich die Zählung von Vertauschungen lösen lässt.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
nach dem Vorbild der kanonischen Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
