# Längste aufsteigende Teilfolge (LIS)

| | |
|---|---|
| **ID** | `dp_07` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(n log n)$ |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Längste monoton steigende Teilfolge](https://en.wikipedia.org/wiki/Longest_increasing_subsequence) |

## Aufgabenstellung

Gegeben sei eine Zahlenfolge `a[0..n-1]`. Bestimme die Länge der
längsten **streng monoton steigenden Teilfolge** (die nicht
unbedingt zusammenhängend sein muss). Eine Teilfolge ist eine Teilmenge, die
die Reihenfolge beibehält; „steigend“ bedeutet, dass jedes Element
streng größer ist als das vorhergehende.

**Eingabe:** ein Array aus vergleichbaren Elementen.
**Ausgabe:** die Länge der LIS.

**Beispiel:**

| Eingabe | LIS | Länge |
|---|---|---:|
| `[10, 9, 2, 5, 3, 7, 101, 18]` | `[2, 3, 7, 18]` oder `[2, 3, 7, 101]` | 4 |
| `[0, 1, 0, 3, 2, 3]` | `[0, 1, 2, 3]` | 4 |
| `[7, 7, 7, 7]` | (keines streng monoton steigend) | 1 |
| `[]` | (leer) | 0 |

## Wann man es verwendet

- Das klassische Problem „**$O(n²)$ DP, das durch einen
  Patience-Sorting-Trick zu $O(n log n)$ wird**“. Die $O(n log n)$-Version
  wird bei jedem Top-Unternehmen abgefragt.
- Immer dann, wenn man eine **reihenfolgeerhaltende Teilmenge** finden muss, die
  eine Monotoniebedingung erfüllt, kommt LIS oder eine Variante
  dazu zur Anwendung.
- Grundlage für die **auf Patience-Sorting basierenden
  Sortieralgorithmen** und die Zerlegung in die **minimale Anzahl
  aufsteigender Teilfolgen** (Dilworth-Theorem).

## Vorgehensweise

Es gibt zwei kanonische Ansätze. Die Engine von cOde(n) vergleicht
mit dem $O(n log n)$-Ansatz, daher konzentrieren wir uns darauf.

### Der $O(n log n)$-Ansatz mit Patience-Sorting

Führen Sie ein Array `tails[]`, wobei `tails[i]` der **kleinstmögliche
Endwert** einer beliebigen bisher beobachteten aufsteigenden Teilfolge der
Länge `i+1` ist. Dieses Array ist stets sortiert.

Für jedes Element `x` in der Eingabe:
- Finde die **position ganz links** in `tails`, die `>= x` ist
  (mithilfe der binären Suche).
- Ersetze `tails[pos]` durch `x`.
- Wenn `x` größer ist als jeder bestehende Tail-Wert, verlängert es die
  längste Teilfolge – füge es an.

Die Länge von `tails` am Ende ist die LIS-Länge.

**Warum es funktioniert:** Das Array `tails` ist eine nach Länge absteigende
Zusammenfassung aller in Frage kommenden Teilfolgen. Für jede Länge behalten wir
nur den „kleinstmöglichen Endabschnitt“ bei, da ein kleinerer Endabschnitt
immer mindestens genauso gut ist wie ein größerer (es können mehr Elemente
darauf folgen).

### Der $O(n²)$-DP-Ansatz (zum Verständnis)

`dp[i]` = Länge der LIS, die bei `a[i]` endet. Rekursion:
`dp[i] = 1 + max(dp[j])` über alle `j < i` mit `a[j] < a[i]`.
Ergebnis: `max(dp)`. Die obige $O(n log n)$-Version ist eine deutliche
Verbesserung und sollte auswendig gelernt werden.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_07: Longest Increasing Subsequence.

Patience sorting with binary search — O(n log n).
"""


def solve(arr):
    import bisect
    tails = []
    for v in arr:
        i = bisect.bisect_left(tails, v)
        if i == len(tails):
            tails.append(v)
        else:
            tails[i] = v
    return len(tails)
```

</details>

## Schritt-für-Schritt-Anleitung

`a = [10, 9, 2, 5, 3, 7, 101, 18]`.

| x | lower_bound(tails, x) | tails danach |
|---:|---:|---|
| 10 | 0 | `[10]` |
| 9 | 0 | `[9]` (ersetzt 10) |
| 2 | 0 | `[2]` (ersetzt 9) |
| 5 | 1 | `[2, 5]` |
| 3 | 1 | `[2, 3]` (ersetzt 5) |
| 7 | 2 | `[2, 3, 7]` |
| 101 | 3 | `[2, 3, 7, 101]` |
| 18 | 3 | `[2, 3, 7, 18]` (ersetzt 101) |

`len(tails) = 4`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(n log n)$ | $O(n)$ |
| **Durchschnittlicher Fall** | $O(n log n)$ | $O(n)$ |
| **Schlechtester Fall** | $O(n log n)$ | $O(n)$ |

Die binäre Suche benötigt $O(log n)$ pro Element, und wir führen sie n
Mal durch. Das `tails`-Array enthält höchstens n Elemente.

Im Fall einer streng absteigenden Eingabe wird bei `tails` niemals ein
Endelement ersetzt, sodass die binäre Suche bei jedem Schritt die vollen $O(log n)$ durchführt
– insgesamt also immer noch $O(n log n)$.

## Varianten & Optimierungen

- **Streng steigend → nicht absteigend** — ändere
  `lower_bound` (erstes `>=`) in `upper_bound` (erstes `>`).
  Dadurch werden gleiche Elemente korrekt behandelt.
- **Die tatsächliche Sequenz rekonstruieren** – speichere ein paralleles
  `parent[i]`-Array (den Index `j`, der ersetzt wurde, als
  wir `tails[pos]` aktualisiert haben). Dann gehe vom letzten
  Element zurück, um die LIS in umgekehrter Reihenfolge zu rekonstruieren. $O(n)$ zusätzlicher
  Speicherplatz und $O(n)$ Rekonstruktionszeit.
- **Längste nicht-absteigende Teilfolge von 2D-Punkten** —
  nach x sortieren, dann LIS auf y anwenden. Wird beim „Russische-Puppen“-
  Umschlagproblem verwendet.
- **Patience-Sort** — dieser Algorithmus ist genau das Patience-
  Sortierung; die Anzahl der Stack entspricht der LIS-Länge, und die
  vollständige Patience-Sortierung erzeugt eine stabile Sortierung in $O(n log n)$.

## Anwendungen in der Praxis

- **Diff- und Merge-Tools** — Finden des längsten übereinstimmenden Blocks
  von Zeilen zwischen zwei Dateiversionen. Der Diff-Algorithmus
  lässt sich auf LCS (siehe dort) zurückführen, es tritt jedoch eine ähnliche dynamische Programmierung auf.
- **Molekularbiologie** — Finden konservierter Teilsequenzen in
  DNA- bzw. Proteinsequenzen.
- **Finanzanalyse** — Finden der längsten Folge
  steigender Aktienkurse, verwendet in der Trendanalyse.
- **Patience-Sortierung** — der obige Algorithmus IST die Patience-Sortierung;
  die Stapelanzahl entspricht der LIS-Länge. Die Patience-Sortierung
  ist $O(n log n)$ und stabil.

## Verwandte Algorithmen in cOde(n)

- **[dp_29 — LIS (Patience-Sortierung)](dp_29_lis-patience-sort.md)** —
  derselbe Algorithmus, jedoch als Sortierergebnis und nicht als
  reine dynamische Programmierung dargestellt. (d=5/10, r=9/10)
- **[dp_04 — Längste gemeinsame Teilfolge](dp_04_longest-common-subsequence.md)** —
  ähnliche Struktur, jedoch mit zwei Folgen statt einer.
  (d=5/10, r=9/10)
- **[stack_02 — Nächstgrößeres Element](stack_02_next-greater-element.md)** —
  ein weiteres klassisches Problem vom Typ „längste aufsteigende Teilfolge“, gelöst
  mit einem monotonen Stack in $O(n)$. (d=4/10, r=7/10)

---

*Diese Dokumentation ist ein Originalbeitrag für cOde(n),
der sich an der kanonischen Struktur orientiert, die von Referenzseiten
zum Thema Wettbewerbsprogrammierung verwendet wird. Den kanonischen
Enzyklopädieeintrag finden Sie über den Wikipedia-Link oben auf der Seite.
Quell-Repository: <https://github.com/dawei7/code_n>.*
