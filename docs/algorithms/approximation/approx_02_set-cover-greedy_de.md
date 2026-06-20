# Set-Cover (Greedy-Approximation)

| | |
|---|---|
| **ID** | `approx_02` |
| **Kategorie** | Approximation |
| **Komplexität (erforderlich)** | $O(S * N)$ |
| **Schwierigkeitsgrad** | 4/10 |
| **Relevanz für Vorstellungsgespräche** | 5/10 |
| **Wikipedia** | [Set-Cover-Problem](https://en.wikipedia.org/wiki/Set_cover_problem) |

## Problemstellung

Gegeben sei ein „Universum“ von Elementen U und eine Familie S von Teilmengen von U. Bestimme die minimale Anzahl von Teilmengen aus S, deren Vereinigung dem gesamten Universum U entspricht.
Dies ist ein klassisches NP-schweres Problem. Sie müssen einen gierigen Approximationsalgorithmus implementieren, der ein Approximationsverhältnis von H_n garantiert (wobei H_n die n-te harmonische Zahl ist, ungefähr \ln(N)).

**Eingabe:** Eine Liste von Elementen, die das Universum `U` darstellt, und eine Liste von Listen `S`, die die Teilmengen darstellt.
**Ausgabe:** Eine Liste von Indizes der ausgewählten Teilmengen, die `U` abdecken.

## Wann man es einsetzt

- Immer dann, wenn Sie vor einem Problem der Ressourcenzuweisung stehen, bei dem Sie eine Reihe von Anforderungen mit der geringstmöglichen Anzahl vordefinierter Pakete „abdecken“ müssen.

## Vorgehensweise

Während es für das Vertex-Cover-Problem eine clevere 2-Approximation gab (Auswahl beider Endpunkte einer Kante), gibt es für das Set-Cover-Problem keine Approximation mit konstantem Faktor. Die beste Approximation in Polynomialzeit, die wir erreichen können, wird durch $O(\ln N)$ begrenzt.

**Der Greedy-Ansatz:**
Die Logik ist sehr intuitiv. In jedem Schritt wollen wir die Teilmenge auswählen, die die **größte Anzahl von Elementen abdeckt, die wir bisher noch nicht abgedeckt haben**.

1. Verwalte eine `uncovered`-Menge von Elementen, die anfangs gleich `U` ist.
2. Solange `uncovered` nicht leer ist:
   - Durchlaufe alle verfügbaren Teilmengen in `S`.
   - Zähle für jede Teilmenge, wie viele Elemente darin *auch* in der Menge `uncovered` enthalten sind (d. h. die Größe der Schnittmenge).
   - Wähle die Teilmenge aus, die die größte Schnittmenge ergibt.
   - Füge diese Teilmenge zu unseren Ergebnissen hinzu.
   - Alle Elemente dieser Teilmenge aus der Menge `uncovered` entfernen.
3. Die Ergebnisse zurückgeben.

**Warum ist das H_n-näherungsweise?**
Im schlimmsten Fall könnte die gierige Auswahl „ausgetrickst“ werden und viele leicht überlappende Mengen anstelle der optimalen, sich nicht überlappenden Mengen auswählen. Mathematisch gesehen deckt jedoch jeder Schritt einen erheblichen Anteil der verbleibenden, noch nicht abgedeckten Elemente ab, was zu einer logarithmischen Verhältnisgrenze führt: \ln(|U|) + 1.

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

## Schritt-für-Schritt-Anleitung

`Universe = {1, 2, 3, 4, 5}`
`Subsets = [S0:{1, 2, 3}, S1:{2, 4}, S2:{3, 4}, S3:{4, 5}]`
*(Optimal sind S0 und S3 -> decken alle 5 Elemente mit 2 Mengen ab).*

**Iteration 1:**
`uncovered = {1, 2, 3, 4, 5}`
- `S0` deckt 3 Elemente ab.
- `S1` deckt 2 Elemente ab.
- `S2` deckt 2 Elemente ab.
- `S3` deckt 2 Elemente ab.
Bester Fall ist `S0`. Wähle `S0`.
`uncovered = uncovered - {1, 2, 3} = {4, 5}`.

**Iteration 2:**
`uncovered = {4, 5}`
- `S1` umfasst {2, 4} \cap {4, 5} = {4} (1 Element).
- `S2` deckt {3, 4} \cap {4, 5} = {4} ab (1 Element).
- `S3` deckt {4, 5} \cap {4, 5} = {4, 5} (2 Elemente) ab.
Das beste Ergebnis ist `S3`. Wähle `S3`.
`uncovered = uncovered - {4, 5} = {}`.

Die Schleife ist beendet! Ausgewählt: `[S0, S3]`. ✓
*(In diesem Fall hat der Greedy-Algorithmus tatsächlich die absolut optimale Lösung gefunden).*

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(S * N)$ | $O(S * N)$ |
| **Durchschnittlicher Fall** | $O(S * N^2)$ | $O(S * N)$ |
| **Schlechtester Fall** | $O(S * N^2)$ | $O(S * N)$ |

*Dabei ist N die Größe des Universums und S die Anzahl der Teilmengen.*
Im schlimmsten Fall wird pro Iteration möglicherweise nur ein neues Element abgedeckt, was dazu führt, dass die äußere `while`-Schleife N-mal durchlaufen wird. Im Inneren durchlaufen wir alle S Teilmengen, wobei die Schnittmenge $O(N)$ Zeit in Anspruch nimmt. Die Laufzeit im schlimmsten Fall beträgt $O(S \cdot N^2)$.
Die Platzkomplexität beträgt $O(S \cdot N)$, um die Mengen im Speicher abzulegen.

## Varianten & Optimierungen

- **Gewichtete Mengenabdeckung:** Wenn jede Teilmenge „Kosten“ hat, wählt man nicht die Teilmenge aus, die die absolut maximale Anzahl an Elementen abdeckt, sondern die Teilmenge mit dem niedrigsten **Kosten-Nutzen-Verhältnis**: `cost(s) / elements_covered`. Dadurch bleibt das exakte \ln(N)-Annäherungsverhältnis erhalten!
- **Dancing Links (Algorithmus X):** Wenn man die *exakte* minimale Überdeckung (oder genauer gesagt eine exakte Überdeckung, bei der sich keine Elemente überschneiden) benötigt, löst Donald Knuths Algorithmus X mit „Dancing Links“ das Problem brillant mittels Backtracking, wenn auch immer noch in exponentieller Zeit.

## Anwendungen in der Praxis

- **Software-Abhängigkeiten:** Ein Paketmanager (wie `npm` oder `pip`), der versucht, eine Gesamtheit angeforderter Bibliotheken durch die Installation der absolut minimalen Anzahl von Metapaketen zu erfüllen.
- **Besatzungsplanung:** Fluggesellschaften, die alle planmäßigen Flüge (Universum) mit der minimalen Anzahl vordefinierter Besatzungsschichten (Teilmengen) abdecken.

## Verwandte Algorithmen in cOde(n)

- **[approx_01 – Vertex Cover](approx_01_vertex-cover-2-approx.md)** — Ein Sonderfall von Set Cover, bei dem jedes Element (Kante) in genau zwei Mengen (Knoten) vorkommt.
- **[greedy_02 – Fractional Knapsack](../greedy/greedy_02_fractional-knapsack.md)** — Nutzt dieselbe „Kosten-Nutzen“-Heuristik nach dem Greedy-Prinzip.

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
nach dem Vorbild der kanonischen Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag finden Sie unter dem
Wikipedia-Link oben auf der Seite. Quell-Repository:
<https://github.com/dawei7/code_n>.*
