# Set Cover (Greedy Approximation)

| | |
|---|---|
| **ID** | `approx_02` |
| **Kategorie** | Approximation |
| **Komplexität (erforderlich)** | $O(S * N)$ |
| **Schwierigkeit** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 5/10 |
| **Wikipedia** | [Set cover problem](https://en.wikipedia.org/wiki/Set_cover_problem) |

## Problemstellung

Gegeben ist ein „Universum“ von Elementen U und eine Familie S von Teilmengen von U. Gesucht ist die minimale Anzahl an Teilmengen aus S, deren Vereinigung dem gesamten Universum U entspricht.
Dies ist ein klassisches NP-schweres Problem. Sie müssen einen gierigen (greedy) Approximationsalgorithmus implementieren, der ein Approximationsverhältnis von H_n garantiert (wobei H_n die n-te harmonische Zahl ist, ungefähr \ln(N)).

**Eingabe:** Eine Liste von Elementen, die das Universum `U` repräsentieren, und eine Liste von Listen `S`, die die Teilmengen repräsentieren.
**Ausgabe:** Eine Liste von Indizes der ausgewählten Teilmengen, die `U` abdecken.

## Wann ist es zu verwenden?

- Immer dann, wenn Sie vor einem Ressourcenallokationsproblem stehen, bei dem Sie eine Menge von Anforderungen mit der geringstmöglichen Anzahl an vordefinierten Paketen „abdecken“ müssen.

## Ansatz

Während das Vertex-Cover eine geschickte 2-Approximation besitzt (beide Endpunkte einer Kante wählen), hat das Set Cover keine Approximation mit konstantem Faktor. Die beste Approximation in Polynomialzeit, die wir erreichen können, ist durch $O(\ln N)$ beschränkt.

**Der Greedy-Ansatz:**
Die Logik ist sehr intuitiv. In jedem Schritt wählen wir die Teilmenge aus, die die **maximale Anzahl an Elementen abdeckt, die wir bisher noch nicht abgedeckt haben**.

1. Verwalten Sie eine `uncovered` Menge von Elementen, die anfangs gleich `U` ist.
2. Solange `uncovered` nicht leer ist:
   - Iterieren Sie durch alle verfügbaren Teilmengen in `S`.
   - Zählen Sie für jede Teilmenge, wie viele Elemente darin *auch* in der `uncovered` Menge enthalten sind (d. h. die Größe der Schnittmenge).
   - Wählen Sie die Teilmenge aus, die die größte Schnittmenge liefert.
   - Fügen Sie diese Teilmenge zu unseren Ergebnissen hinzu.
   - Entfernen Sie alle Elemente dieser Teilmenge aus der `uncovered` Menge.
3. Geben Sie die Ergebnisse zurück.

**Warum ist es H_n-approximativ?**
Im schlimmsten Fall könnte die gierige Wahl „ausgetrickst“ werden, viele sich leicht überschneidende Mengen anstelle der optimalen, sich nicht überschneidenden Mengen zu wählen. Mathematisch gesehen deckt jedoch jeder Schritt einen signifikanten Anteil der verbleibenden unbedeckten Elemente ab, was zu einer logarithmischen Schranke führt: \ln(|U|) + 1.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for approx_02: Set Cover (Greedy).

Each step picks the set covering the most uncovered elements.
"""


def solve(universe, sets, m, k):
    if k == 0:
        return []
    uncovered = set(universe)
    chosen = []
    while uncovered:
        best_idx = -1
        best_count = 0
        for i, s in enumerate(sets):
            count = sum(1 for x in s if x in uncovered)
            if count > best_count:
                best_count = count
                best_idx = i
        if best_idx == -1 or best_count == 0:
            break
        chosen.append(best_idx)
        for x in sets[best_idx]:
            uncovered.discard(x)
    return sorted(chosen)
```

</details>

## Durchlauf

`Universe = {1, 2, 3, 4, 5}`
`Subsets = [S0:{1, 2, 3}, S1:{2, 4}, S2:{3, 4}, S3:{4, 5}]`
*(Optimal sind S0 und S3 -> deckt alle 5 Elemente mit 2 Mengen ab).*

**Iteration 1:**
`uncovered = {1, 2, 3, 4, 5}`
- `S0` deckt 3 Elemente ab.
- `S1` deckt 2 Elemente ab.
- `S2` deckt 2 Elemente ab.
- `S3` deckt 2 Elemente ab.
Das Beste ist `S0`. Wähle `S0`.
`uncovered = uncovered - {1, 2, 3} = {4, 5}`.

**Iteration 2:**
`uncovered = {4, 5}`
- `S1` deckt {2, 4} \cap {4, 5} = {4} (1 Element) ab.
- `S2` deckt {3, 4} \cap {4, 5} = {4} (1 Element) ab.
- `S3` deckt {4, 5} \cap {4, 5} = {4, 5} (2 Elemente) ab.
Das Beste ist `S3`. Wähle `S3`.
`uncovered = uncovered - {4, 5} = {}`.

Schleife beendet! Ausgewählt: `[S0, S3]`. ✓
*(In diesem Fall hat der Greedy-Algorithmus tatsächlich die absolut optimale Lösung gefunden).*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(S * N)$ | $O(S * N)$ |
| **Durchschnittlicher Fall** | $O(S * N^2)$ | $O(S * N)$ |
| **Schlechtester Fall** | $O(S * N^2)$ | $O(S * N)$ |

*Wobei N die Größe des Universums und S die Anzahl der Teilmengen ist.*
Im schlimmsten Fall decken wir pro Iteration nur 1 neues Element ab, wodurch die äußere `while`-Schleife N-mal durchlaufen wird. Innerhalb der Schleife iterieren wir über alle S Teilmengen, was $O(N)$ Zeit für die Schnittmengenbildung benötigt. Die Zeitkomplexität im schlechtesten Fall beträgt $O(S \cdot N^2)$.
Die Platzkomplexität beträgt $O(S \cdot N)$, um die Mengen im Speicher zu halten.

## Varianten & Optimierungen

- **Weighted Set Cover:** Wenn jede Teilmenge einen „Preis“ hat, wählen Sie anstelle der Teilmenge, die die absolut meisten Elemente abdeckt, diejenige mit dem niedrigsten **Kosteneffizienz**-Verhältnis: `cost(s) / elements_covered`. Dies behält das exakt gleiche \ln(N) Approximationsverhältnis bei!
- **Dancing Links (Algorithm X):** Wenn Sie die *exakte* minimale Abdeckung benötigen (oder spezifisch ein Exact Cover, bei dem sich keine Elemente überschneiden), löst Donald Knuths Algorithm X mittels Dancing Links dies brillant durch Backtracking, allerdings weiterhin in exponentieller Zeit.

## Anwendungen in der Praxis

- **Software-Abhängigkeiten:** Ein Paketmanager (wie `npm` oder `pip`), der versucht, ein Universum von angeforderten Bibliotheken durch die Installation der absolut minimalen Anzahl an Meta-Paketen zu erfüllen.
- **Crew-Planung:** Fluggesellschaften, die alle geplanten Flüge (Universum) mit der minimalen Anzahl an vordefinierten Crew-Schichten (Teilmengen) abdecken.

## Verwandte Algorithmen in cOde(n)

- **[approx_01 - Vertex Cover](approx_01_vertex-cover-2-approx.md)** — Ein Spezialfall des Set Cover, bei dem jedes Element (Kante) in genau zwei Mengen (Knoten) vorkommt.
- **[greedy_02 - Fractional Knapsack](../greedy/greedy_02_fractional-knapsack.md)** — Teilt die heuristische „Kosteneffizienz“-Ratio des Greedy-Ansatzes.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*