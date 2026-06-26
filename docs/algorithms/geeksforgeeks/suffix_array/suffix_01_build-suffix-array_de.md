# Suffix Array erstellen

| | |
|---|---|
| **ID** | `suffix_01` |
| **Kategorie** | suffix_array |
| **Komplexität (erforderlich)** | $O(N \log N \log N)$ Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 8/10 |
| **Relevanz für Vorstellungsgespräche** | 3/10 |
| **GeeksForGeeks Äquivalent** | [Suffix Array Definition and Construction](https://www.geeksforgeeks.org/suffix-array-set-1-introduction/) |

## Problemstellung

Gegeben sei ein String `s` der Länge N. Konstruiere dessen **Suffix Array**.
Ein Suffix Array ist ein sortiertes Array aller Suffixe eines Strings.
Anstatt die tatsächlichen Suffixe des Strings zu speichern (was $O(N^2)$ Platz beanspruchen würde), speichert das Suffix Array die Start-**Indizes** dieser Suffixe in lexikographischer (alphabetischer) Reihenfolge.

**Eingabe:** Ein String `s`.
**Ausgabe:** Ein Integer-Array der Größe N, das die sortierten Indizes enthält.

## Wann man es verwendet

- Um blitzschnelle Textsuchen in einem statischen Dokument durchzuführen.
- Es ist eine speichereffiziente Alternative zur Suffix Tree Datenstruktur, die exakt dieselben massiven Teilstring-Anfragen löst, dabei jedoch drastisch weniger Speicher benötigt.

## Ansatz

**1. Die naive $O(N^2 \log N)$ Sortierung:**
Wenn `s = "banana"`.
Die Suffixe sind: `0: "banana"`, `1: "anana"`, `2: "nana"`, `3: "ana"`, `4: "na"`, `5: "a"`.
Wir legen diese in ein Array und verwenden eine Standard-Sortierung.
Sortiert: `"a" (5)`, `"ana" (3)`, `"anana" (1)`, `"banana" (0)`, `"na" (4)`, `"nana" (2)`.
Das Suffix Array ist `[5, 3, 1, 0, 4, 2]`.
Die Standard-Sortierung vergleicht Strings $O(N \log N)$ mal. Jeder String-Vergleich benötigt $O(N)$ Zeit. Die Gesamtlaufzeit beträgt $O(N^2 \log N)$. Dies ist viel zu langsam für einen Text mit 1 Million Zeichen!

**2. Die Prefix-Doubling-Optimierung ($O(N \log^2 N)$):**
Wir müssen nicht ganze Suffixe auf einmal vergleichen. Wir können sie schrittweise sortieren!
- **Durchlauf 1 (Länge 1):** Wir sortieren die Suffixe NUR basierend auf ihrem ersten Zeichen. Wir weisen jedem Suffix einen "Rang" zu.
- **Durchlauf 2 (Länge 2):** Wir möchten die Suffixe basierend auf ihren ersten 2 Zeichen sortieren. Aber Moment! Die ersten 2 Zeichen eines Suffixes, das bei `i` beginnt, sind einfach das erste Zeichen von `i` kombiniert mit dem ersten Zeichen von `i+1`! Da wir die Ränge der Länge 1 BEREITS berechnet haben, können wir einfach basierend auf dem Tupel sortieren: `(Rank[i], Rank[i+1])`!
- **Durchlauf 3 (Länge 4):** Wir möchten basierend auf den ersten 4 Zeichen sortieren. Die ersten 4 Zeichen von `i` sind die ersten 2 Zeichen von `i` kombiniert mit den ersten 2 Zeichen von `i+2`! Wir sortieren basierend auf `(Rank[i], Rank[i+2])`!

Indem wir die Länge, die wir betrachten, verdoppeln (1, 2, 4, 8...), benötigen wir nur $\log_2 N$ Durchläufe, um Strings der Länge N vollständig zu sortieren.
In jedem Durchlauf sortieren wir ein Array von N Tupeln, was $O(N \log N)$ Zeit in Anspruch nimmt.
Gesamtzeit: $O(\log N \text{ Durchläufe})$ x $O(N \log N \text{ Sortierung})$ = $O(N \log^2 N)$.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for suffix_01: Build Suffix Array.

Naive: build all n suffixes and sort them. O(n^2 log n).
"""


def solve(s, n):
    if n == 0:
        return []
    return sorted(range(n), key=lambda i: s[i:])
```

</details>

## Durchlauf

`s = "banana"`, N = 6.
**Initialisierung (Präfixe der Länge 1):**
Die Tupel sind `(s[i], s[i+1])`.
- `0 (ba)`: `(1, 0)`
- `1 (an)`: `(0, 13)`
- `2 (na)`: `(13, 0)`
- `3 (an)`: `(0, 13)`
- `4 (na)`: `(13, 0)`
- `5 (a_)`: `(0, -1)`
Sortiert: `[5 (a_), 1 (an), 3 (an), 0 (ba), 2 (na), 4 (na)]`.

**Iteration 1 (Länge 2 -> Länge 4 Präfixe):**
Wir weisen den sortierten Elementen neue Integer-Ränge zu:
- `5` erhält Rang 0.
- `1` und `3` sind identisch `(0, 13)`, beide erhalten Rang 1.
- `0` erhält Rang 2.
- `2` und `4` sind identisch `(13, 0)`, beide erhalten Rang 3.
Nun erstellen wir Tupel für die Länge 4.
Für Suffix `1 (anana)` ist das Tupel `(Rang von 1, Rang von 1+2)`.
Rang von 1 ist `1`. Rang von 3 ist `1`. Das Tupel ist `(1, 1)`.
Für Suffix `3 (ana)` ist das Tupel `(Rang von 3, Rang von 5)`.
Rang von 3 ist `1`. Rang von 5 ist `0`. Das Tupel ist `(1, 0)`.
Man beachte, wie `3` nun ein KLEINERES Tupel hat als `1`! `"ana"` kommt korrekt vor `"anana"`!
Wir sortieren die neuen Tupel.

Nach $\log_2 N$ Iterationen ist jedes Suffix perfekt separiert und sortiert.
Rückgabe: `[5, 3, 1, 0, 4, 2]`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log^2 N)$ | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N \log^2 N)$ | $O(N)$ |
| **Schlechtester Fall** | $O(N \log^2 N)$ | $O(N)$ |

Der Algorithmus durchläuft eine `while`-Schleife $\log_2 N$ mal.
Innerhalb der Schleife sortiert die eingebaute `sort()`-Funktion ein Array von N Objekten, was $O(N \log N)$ Zeit benötigt.
Die gesamte Zeitkomplexität beträgt sauber $O(N \log^2 N)$.
Die Platzkomplexität beträgt $O(N)$, um die Arrays der `Suffix`-Objekte und Ränge zu speichern.

## Varianten & Optimierungen

- **Radix Sort Optimierung ($O(N \log N)$):** In der inneren Schleife sortieren wir ein Array von 2D-Tupeln `(rank1, rank2)`. Wir benötigen hierfür keine $O(N \log N)$ Vergleichssortierung! Wir können einen 2-Pass Radix Sort (`sort_08`) verwenden. Dies reduziert die innere Sortierung auf $O(N)$, wodurch die gesamte algorithmische Zeit auf mathematisch garantierte $O(N \log N)$ sinkt!
- **DC3 / Skew Algorithmus ($O(N)$):** Es existieren unglaublich komplexe Linearzeit-Algorithmen zur nativen Konstruktion von Suffix Arrays, diese gelten jedoch im Allgemeinen als zu ausführlich für technische Vorstellungsgespräche.

## Anwendungen in der Praxis

- **Volltext-Suchmaschinen:** ElasticSearch und Lucene verwenden Suffix Arrays/Trees im Hintergrund, um Teilstrings in massiven Gigabyte-großen Log-Dateien sofort zu finden, ohne die Datei scannen zu müssen.
- **Datenkompression:** Suffix Arrays sind der grundlegende Schritt der Burrows-Wheeler-Transformation, welche die mathematische Engine hinter der `bzip2`-Kompression ist.

## Verwandte Algorithmen in cOde(n)

- **[suffix_03 - LCP Array (Kasai's Algorithm)](suffix_03_lcp-array-kasai-s-algorithm.md)** — Das obligatorische sekundäre Array, das Suffix Arrays erst nützlich für die Lösung komplexer String-Probleme macht.
- **[suffix_02 - Pattern Search](suffix_02_pattern-search-with-suffix-array.md)** — Wie man das generierte Suffix Array verwendet, um sofort Teilstrings zu finden.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*