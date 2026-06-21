# Binäre Suche

| | |
|---|---|
| **ID** | `search_02` |
| **Kategorie** | searching |
| **Komplexität (erforderlich)** | $O(log n)$ |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **Wikipedia** | [Binary search](https://en.wikipedia.org/wiki/Binary_search) |

## Problemstellung

Gegeben ist ein **sortiertes** Array `a[0..n-1]` (aufsteigend) und ein `target`. Finde den Index von `target` im Array oder gib `-1` zurück, falls es nicht vorhanden ist.

**Eingabe:** Ein sortiertes Array und ein Zielwert.
**Ausgabe:** Der Index von `target` oder `-1`.

**Beispiel:**

| a | target | Antwort |
|---|---|---:|
| `[1, 3, 5, 7, 9, 11, 13, 15]` | 7 | 3 |
| `[1, 3, 5, 7, 9, 11, 13, 15]` | 12 | -1 |
| `[5]` | 5 | 0 |
| `[5]` | 3 | -1 |
| `[]` | 0 | -1 |

## Wann man sie verwendet

- Der kanonische **Divide-and-Conquer-Suchalgorithmus** und der wichtigste Suchalgorithmus überhaupt. Wird in irgendeiner Form in nahezu jedem Vorstellungsgespräch abgefragt.
- Die **"invariantenbasierte"** Vorlage (left/right Pointer, Berechnung von `mid`, Vergleich, Verschieben eines Pointers) ist zudem die Grundlage für viele Probleme, die keine reine Suche sind: lower/upper bound, Suche in rotierten Arrays, "find first bad version", "find the peak", "find the minimum in a rotated sorted array", "search a 2D matrix", "find the kth smallest" usw.

## Ansatz

Verwalte einen Suchbereich `[lo, hi]` und eine Schleifeninvariante: `target` (falls vorhanden) befindet sich in `a[lo..hi]`. In jeder Iteration:
- Berechne `mid`. Zwei gängige Formeln:
  - `mid = (lo + hi) // 2` (klassisch; Überlaufrisiko bei sehr großen Arrays in Low-Level-Sprachen)
  - `mid = lo + (hi - lo) // 2` (überlaufsicher)
- Vergleiche `a[mid]` mit `target`:
  - **Gleich:** gefunden, gib `mid` zurück.
  - **Kleiner als:** die Antwort (falls vorhanden) liegt rechts; `lo = mid + 1`.
  - **Größer als:** die Antwort (falls vorhanden) liegt links; `hi = mid - 1`.
- Schleife, bis `lo > hi`. Gib dann `-1` zurück.

Die Invariante gilt bei jedem Schritt. Wenn die Schleife also mit `lo > hi` endet, wissen wir, dass `target` nicht im Array enthalten ist.

**Schleifenvarianten:**
- **Geschlossenes Intervall** `[lo, hi]` — initialisiert mit `lo = 0`, `hi = n - 1`. Abbruch bei `lo > hi`. Am gebräuchlichsten.
- **Halboffenes Intervall** `[lo, hi)` — initialisiert mit `lo = 0`, `hi = n`. Abbruch bei `lo == hi`. Standard in C++ `std::lower_bound`.
- **Offenes Intervall** `(lo, hi)` — initialisiert mit `lo = -1`, `hi = n`. Abbruch bei `hi - lo == 1`. Wird für einige saubere rekursive Formulierungen verwendet.

Wähle eine Variante und bleibe dabei; das Vermischen der Konventionen ist die häufigste Ursache für Off-by-one-Fehler.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for search_02: Binary Search.

Sorted array; halve the search space each step. O(log n) time.
"""


def solve(data, target, n):
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        value = data[mid]
        if value == target:
            return mid
        if value < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

</details>

## Durchlauf

`a = [1, 3, 5, 7, 9, 11, 13, 15]`, `target = 7`.

| Iter | lo | hi | mid | a[mid] | cmp | next |
|---:|---:|---:|---:|---:|---|---|
| 1 | 0 | 7 | 3 | 7 | == | return 3 |

(Trivialerweise im ersten Schritt gefunden — aber log₂(8) = 3, daher sind für ein Array mit 8 Elementen 1-3 Iterationen zu erwarten.)

Versuchen wir `target = 12` (nicht vorhanden):

| Iter | lo | hi | mid | a[mid] | cmp | next |
|---:|---:|---:|---:|---:|---|---|
| 1 | 0 | 7 | 3 | 7 | < | lo = 4 |
| 2 | 4 | 7 | 5 | 11 | < | lo = 6 |
| 3 | 6 | 7 | 6 | 13 | > | hi = 5 |
| 4 | 6 | 5 | — | — | exit | return -1 |

3 Iterationen, um die Abwesenheit zu bestätigen. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(1)$ — beim ersten Versuch in `mid` gefunden | $O(1)$ |
| **Durchschnittlicher Fall** | $O(log n)$ | $O(1)$ |
| **Schlechtester Fall** | $O(log n)$ | $O(1)$ |

Die iterative Variante hat $O(1)$ Platzkomplexität; die rekursive Variante hat $O(log n)$ Platzkomplexität für den Stack.

## Varianten & Optimierungen

- **Lower bound / upper bound** — gibt die linkeste (oder rechteste) Position zurück, an der `target` eingefügt werden könnte. Die Grundlage für C++ `std::lower_bound` / `std::upper_bound` und für das `bisect`-Modul in Python. Die Änderung besteht aus einer einzigen Zeile im Vergleich (kein vorzeitiger Rückgabewert bei `==`).
- **Suche in rotiertem sortiertem Array** — siehe `search_12`. Entscheide, welche Hälfte sortiert ist, und prüfe dann, ob `target` in dieser Hälfte liegt.
- **First bad version** — finde den ersten Index, bei dem `isBadVersion(i)` True ist. Identisch mit lower-bound, jedoch mit einem benutzerdefinierten Prädikat.
- **Suche in einer 2D-Matrix** — behandle die flache Matrix als ein 1D-sortiertes Array; verwende die Standard-Binärsuche mit `mid_row = mid // n_cols` und `mid_col = mid % n_cols`.
- **Binäre Suche auf der Antwort** — viele Probleme besitzen eine monotone "Ist das groß genug?"-Prüfung, und die Binärsuche kann auf den Antwortraum angewendet werden (Koko eating bananas, minimum days to ship, etc.).

## Anwendungen in der Praxis

- **Datenbank-Index-Lookup** — B-Baum-Indizes verallgemeinern die Binärsuche auf Knoten in der Größe von Festplattenblöcken; gleiche $O(log n)$-Struktur.
- **Wörterbuch-Suche** — Finden eines Wortes in einem sortierten Lexikon.
- **git bisect** — Binärsuche über die Commit-Historie, um den Commit zu finden, der einen Fehler eingeführt hat.
- **Versionsbereichsprüfungen** — "Ist diese Version älter als X?" ist in vielen Build-Systemen eine Binärsuche.
- **Cache-Line-Binärsuche** — für Arrays, die klein genug sind, um in den L1-Cache zu passen, ist die Binärsuche aufgrund der Cache-Freundlichkeit (kein Pointer-Chasing) schneller als Hash-Tabellen-Lookups.

## Verwandte Algorithmen in cOde(n)

- **[search_03 — BFS Grid](search_03_bfs-grid.md)** — Graphensuche, wenn das Array ein Gitter ist. (d=5/10, r=8/10)
- **[search_04 — DFS Grid](search_04_dfs-grid.md)** — die andere Suchreihenfolge für Graphen. (d=4/10, r=8/10)
- **[search_12 — Search in Rotated Sorted Array](search_12_search-in-rotated-sorted-array.md)** — die schwierigere Variante. (d=5/10, r=8/10)
- **[hash_01 — Two Sum](hash_01_two-sum.md)** — alternativer $O(n)$-Ansatz unter Verwendung einer Hash Map. (d=4/10, r=9/10)

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den enzyklopädischen Standardeintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*