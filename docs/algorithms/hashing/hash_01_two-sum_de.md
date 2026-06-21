# Two Sum

| | |
|---|---|
| **ID** | `hash_01` |
| **Kategorie** | hashing |
| **Komplexität (erforderlich)** | $O(n)$ |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Hash table](https://en.wikipedia.org/wiki/Hash_table) |

## Problemstellung

Gegeben ist ein Array von Integern `nums` und ein Zielwert `target`. Geben Sie die **Indizes der beiden Zahlen** zurück, die sich zu `target` addieren. Sie können davon ausgehen, dass jede Eingabe genau eine Lösung hat, und Sie dürfen dasselbe Element nicht zweimal verwenden.

**Eingabe:** ein Array `nums` und ein Integer `target`.
**Ausgabe:** zwei Indizes `i ≠ j` mit `nums[i] + nums[j] = target`.

**Beispiel:**

| nums | target | Antwort | Summe |
|---|---|---|---:|
| `[2, 7, 11, 15]` | 9 | `[0, 1]` | 2 + 7 |
| `[3, 2, 4]` | 6 | `[1, 2]` | 2 + 4 |
| `[3, 3]` | 6 | `[0, 1]` | 3 + 3 |

## Wann man es verwendet

- Die mit Abstand am häufigsten gestellte **Aufwärm- / Telefon-Screening-Frage** in Coding-Interviews. LeetCode #1. Es geht nicht darum, ob Sie den Algorithmus kennen (es ist das Dictionary-Lookup); es geht darum, ob Sie:
  - **Die Komplexität argumentieren können** ($O(n²)$ Brute-Force vs. $O(n)$ Hash Map)
  - **Die Trade-offs diskutieren können** (zusätzlicher Speicherplatz für die Map vs. $O(1)$ zusätzlicher Speicherplatz für die sortierte Two-Pointer-Variante)
  - **Generalisieren können** zu 3-Sum, 4-Sum, K-Sum oder zu "zwei Zahlen nahe an einem Zielwert" (Binäre Suche auf dem sortierten Array)
- Ein exzellenter Test, ob Sie zur richtigen Datenstruktur (Hash Map) greifen, wenn das Problem danach fragt, ein "Komplement" in $O(n)$ Zeit zu finden.

## Ansatz

Für jedes Element `nums[i]` müssen wir herausfinden, ob `target - nums[i]` bereits früher im Array aufgetreten ist.

**Brute-Force** ($O(n²)$): verschachtelte Schleife. Jedes Paar ausprobieren.

**Sortieren + Two-Pointer** ($O(n log n)$): das Array sortieren und dann zwei Pointer von den Enden aus aufeinander zubewegen. Die "Antwort-Indizes" müssen separat gespeichert werden, da das Sortieren die ursprüngliche Reihenfolge zerstört. Die Two-Pointer-Variante benötigt $O(1)$ zusätzlichen Speicherplatz.

**Hash Map** ($O(n)$, die produktive Version): für jedes `nums[i]` prüfen, ob `target - nums[i]` in der Map vorhanden ist.
- Falls ja: Wir haben unsere Antwort gefunden, gib `[map[target - nums[i]], i]` zurück.
- Falls nein: Speichere `nums[i] -> i` in der Map und fahre fort.

Dies hat eine Zeitkomplexität von $O(n)$ und eine Platzkomplexität von $O(n)$. Ein einziger Durchlauf.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for hash_01: Two Sum.

Single pass: walk the array, for each value check whether
target - value has been seen. If yes, return the two indices.
Otherwise, store the current value's index in the map. O(n).
"""


def solve(arr, target, n):
    seen = {}
    for i in range(n):
        complement = target - arr[i]
        if complement in seen:
            return sorted([seen[complement], i])
        seen[arr[i]] = i
    return [-1, -1]
```

</details>

## Durchlauf

`nums = [2, 7, 11, 15]`, `target = 9`.

| i | x | complement | bereits gesehen | Aktion | danach gesehen |
|---:|---:|---:|---|---|---|
| 0 | 2 | 7 | `{}` | speichere 2→0 | `{2: 0}` |
| 1 | 7 | 2 | `{2: 0}` | gefunden! gib `[0, 1]` zurück | — |

Antwort: `[0, 1]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n)$ | $O(n)$ |
| **Durchschnittlicher Fall** | $O(n)$ | $O(n)$ |
| **Schlechtester Fall** | $O(n)$ | $O(n)$ |

Hash-Table-Lookups und -Einfügungen sind im Erwartungswert $O(1)$ (Schlechtester Fall $O(n)$ bei einer schlechten Hash-Funktion, aber in der Praxis $O(1)$ für Integer-Keys).

## Varianten & Optimierungen

- **Sortiert + Two-Pointer** ($O(n log n)$ Zeit, $O(1)$ Platz) — wenn Sie sich die zusätzliche Hash Map nicht leisten können. Der Nachteil ist, dass Sie die ursprünglichen Indizes durch die Sortierung hindurch verfolgen müssen.
- **3-Sum, 4-Sum, K-Sum** — erweitern Sie das Muster. 3-Sum: sortieren, dann für jedes `i` das "Two Sum"-Problem auf dem Rest des Arrays mit dem Zielwert `target - nums[i]` lösen. Duplikate überspringen. $O(n²)$ für 3-Sum.
- **Two Sum II (sortierte Eingabe)** — das Array ist bereits sortiert; die Two-Pointer-Lösung ist $O(n)$ mit $O(1)$ zusätzlichem Speicherplatz.
- **Two Sum BST** — gegeben ein BST, finde zwei Knoten, die sich zu einem Zielwert addieren. Verwenden Sie den In-Order-Iterator + Reverse-In-Order-Iterator (Two-Pointer auf einem BST) für $O(n)$ Zeit und $O(log n)$ Platz.
- **Subarray sum equals k** — das verwandte Präfixsummen- + Hash-Map-Problem (`hash_02`).

## Anwendungen in der Praxis

- **Rechnungsabgleich** — eingehende Zahlungen offenen Rechnungen zuordnen; die "zwei Rechnungen, die sich zur Einzahlung summieren" ist exakt Two Sum.
- **Paarfindung in Finanzdatensätzen** — finde zwei Transaktionen, die sich zu Null aufsummieren (eine Überweisung + die entsprechende Gebühr, ein Kauf + ein Verkauf, etc.).
- **Cache-Key-Konstruktion** — gegeben eine Anfrage mit zwei Parametern `a, b`, prüfe, ob das (geordnete) Paar `(a, b)` in einem Ergebnis-Cache vorhanden ist; dies ist das "Two Sum"-Muster in verkleideter Form.
- **Sudoku- und Kreuzworträtsel-Solver** — "zwei Zellen, die sich zu N summieren" ist eine häufige Teilprüfung.

## Verwandte Algorithmen in cOde(n)

- **[hash_02 — Subarray Sum Equals K](hash_02_subarray-sum-equals-k.md)** — die Verallgemeinerung der Präfixsumme. (d=4/10, r=9/10)
- **[hash_03 — Longest Substring Without Repeating](hash_03_longest-substring-without-repeating.md)** — Hash-Set mit Sliding Window. (d=4/10, r=9/10)
- **[search_02 — Binary Search](search_02_binary-search.md)** — der alternative $O(n log n)$ / $O(1)$ Ansatz für sortierte Eingaben. (d=3/10, r=8/10)

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*