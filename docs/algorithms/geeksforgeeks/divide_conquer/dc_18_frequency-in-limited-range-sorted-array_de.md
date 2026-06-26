# Häufigkeit von Elementen in einem sortierten Array

| | |
|---|---|
| **ID** | `dc_18` |
| **Kategorie** | divide_conquer |
| **Komplexität (erforderlich)** | $O(\log N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) |

## Problemstellung

Gegeben ist ein Array von Ganzzahlen `nums`, das in nicht-absteigender Reihenfolge sortiert ist. Finden Sie die Start- und Endposition eines gegebenen `target`-Wertes.
Wenn `target` nicht im Array gefunden wird, geben Sie `[-1, -1]` zurück.
Sie müssen einen Algorithmus mit einer Zeitkomplexität von $O(\log N)$ implementieren.
*(Alternativ formuliert: Zählen Sie die Häufigkeit von `target` im sortierten Array durch Rückgabe von `end_index - start_index + 1`).*

**Eingabe:** Ein sortiertes Array von Ganzzahlen `nums` und eine Ganzzahl `target`.
**Ausgabe:** Ein Array `[start_index, end_index]`.

## Wann ist dieser Ansatz zu verwenden?

- Immer dann, wenn Sie ein Array durchsuchen müssen, in dem doppelte Elemente erlaubt sind, und Sie die Grenzen eines bestimmten Element-Clusters bestimmen müssen.
- Dies ist die grundlegende Erweiterung der Standard-Binary Search.

## Ansatz

**1. Die Schwäche der Standard-Binary Search:**
Wenn das Array `[5, 7, 7, 8, 8, 8, 8, 8, 10]` ist und `target` den Wert `8` hat.
Die Standard-Binary Search landet möglicherweise zufällig auf Index `5`. Sie gibt `5` zurück und terminiert. Aber Sie wissen nicht, wo die `8`en beginnen oder enden!
Sie *könnten* von Index 5 aus linear nach links und rechts scannen, bis die `8`en aufhören. Wenn jedoch das gesamte Array aus 1 Million Elementen nur aus `8`en besteht, verschlechtert sich Ihr linearer Scan auf $O(N)$, was zu einer Zeitüberschreitung (Time Limit Exceeded) führt!

**2. Divide and Conquer (Modifizierte Binary Search):**
Wir können die Binary Search ZWEIMAL ausführen.
- Einmal, um das absolut linkeste Vorkommen von `target` zu finden.
- Einmal, um das absolut rechteste Vorkommen von `target` zu finden.

**3. Finden der linken Grenze:**
Wenn wir nach dem `target` suchen und `nums[mid] == target` gilt, was sollten wir tun?
Normalerweise würden wir stoppen. Da wir aber das LINKESTE Vorkommen suchen, nehmen wir an, dass `mid` möglicherweise nicht das am weitesten links liegende Element ist!
Wir speichern `ans = mid` und schneiden die rechte Hälfte des Arrays aggressiv ab! Wir setzen `high = mid - 1` und suchen weiter nach links!

**4. Finden der rechten Grenze:**
Identische Logik. Wenn `nums[mid] == target` gilt, speichern wir `ans = mid`, schneiden aber die linke Hälfte aggressiv ab! Wir setzen `low = mid + 1` und suchen weiter nach rechts, um zu sehen, ob es noch WEITERE Vorkommen von `target` gibt!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dc_18: Frequency in Limited Range (sorted array).

Given a sorted array of positive integers and a
"""


def solve(arr, n, target):
    """Frequency of `target` in a sorted array via two binary
    searches (first and last occurrence)."""
    # First occurrence.
    lo, hi, first = 0, n - 1, -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            first = mid
            hi = mid - 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    if first == -1:
        return 0
    # Last occurrence.
    lo, hi, last = first, n - 1, first
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            last = mid
            lo = mid + 1
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return last - first + 1
```

</details>

## Durchlauf

`nums = [5, 7, 7, 8, 8, 10]`, `target = 8`.

**Durchlauf 1: Linke Grenze (`is_finding_left = True`)**
1. `low=0`, `high=5`. `mid=2` (Wert `7`). `7 < 8`. `low = 3`.
2. `low=3`, `high=5`. `mid=4` (Wert `8`). TREFFER!
   - `ans = 4`.
   - `high = mid - 1 = 3`. (Suche nach links erzwingen!).
3. `low=3`, `high=3`. `mid=3` (Wert `8`). TREFFER!
   - `ans = 3`. (Überschreibt 4, wir haben ein früheres Vorkommen gefunden!).
   - `high = mid - 1 = 2`.
4. `low (3) <= high (2)` ist FALSCH. Schleife endet. `left_bound = 3`.

**Durchlauf 2: Rechte Grenze (`is_finding_left = False`)**
1. `low=0`, `high=5`. `mid=2` (Wert `7`). `7 < 8`. `low = 3`.
2. `low=3`, `high=5`. `mid=4` (Wert `8`). TREFFER!
   - `ans = 4`.
   - `low = mid + 1 = 5`. (Suche nach rechts erzwingen!).
3. `low=5`, `high=5`. `mid=5` (Wert `10`). `10 > 8`.
   - `high = mid - 1 = 4`.
4. `low (5) <= high (4)` ist FALSCH. Schleife endet. `right_bound = 4`.

Ergebnis `[3, 4]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(\log N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(\log N)$ | $O(1)$ |

Wir führen einfach zwei völlig unabhängige $O(\log N)$ Binary Searches nacheinander aus. Daher ergibt sich eine Zeitkomplexität von $O(\log N) + O(\log N) = O(\log N)$.
Die Platzkomplexität beträgt $O(1)$.

## Varianten & Optimierungen

- **`bisect`-Modul in Python:** Anstatt dies manuell zu implementieren, bietet Pythons eingebautes Binary-Search-Modul `bisect_left` (gibt den Index des ersten Vorkommens zurück) und `bisect_right` (gibt den Index unmittelbar *nach* dem letzten Vorkommen zurück).
- **Häufigkeit zählen:** Geben Sie einfach `right_bound - left_bound + 1` zurück.

## Anwendungen in der Praxis

- **Datenbank-Bereichsscans (B-Trees):** Wenn eine SQL-Abfrage wie `SELECT * FROM table WHERE age = 25` ausgeführt wird, verwendet die Datenbank einen B-Tree-Index (einen mehrwegigen binären Suchbaum), um den linkesten Knoten zu finden, der 25 enthält, und liest dann sequenziell die Festplattenseiten, bis sich der Schlüssel auf 26 ändert. Dieser Algorithmus modelliert exakt den Mechanismus zum Auffinden dieses ersten Startblocks.

## Verwandte Algorithmen in cOde(n)

- **[searching_01 - Binary Search](../searching/search_01_binary-search.md)** — Das Fundament.
- **[searching_03 - Search Insert Position](../searching/search_03_search-insert-position.md)** — Eine eng verwandte Variante, bei der `bisect_left` verwendet wird, um die Position zu finden, an der ein Element eingefügt werden *sollte*.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*