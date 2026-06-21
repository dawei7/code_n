# Job Assignment (Branch and Bound)

| | |
|---|---|
| **ID** | `bb_02` |
| **Kategorie** | branch_and_bound |
| **Komplexität (erforderlich)** | $O(N!)$ Schlechtester Fall |
| **Schwierigkeit** | 7/10 |
| **Relevanz für Vorstellungsgespräche** | 3/10 |
| **Wikipedia** | [Assignment problem](https://en.wikipedia.org/wiki/Assignment_problem) |

## Problemstellung

Gegeben sind N Arbeiter und N Jobs sowie eine 2D-Kostenmatrix, wobei `cost[i][j]` die Kosten für die Zuweisung von Arbeiter `i` zu Job `j` darstellt.
Jeder Arbeiter muss genau einem Job zugewiesen werden, und jeder Job muss genau einem Arbeiter zugewiesen werden.
Finden Sie die Zuweisung, welche die Gesamtkosten minimiert.

Während der bekannte Ungarische Algorithmus dieses Problem exakt in $O(N^3)$ Zeit löst, müssen Sie hier demonstrieren, wie man es mittels einer generischen **Branch and Bound**-Zustandsraumsuche löst.

**Eingabe:** Eine N x N Ganzzahlmatrix `cost`.
**Ausgabe:** Die minimal möglichen Gesamtkosten.

## Wann man es verwendet

- Um zu lernen, wie man untere Schranken (Lower Bounds) für matrixbasierte kombinatorische Optimierungsprobleme konstruiert.
- Branch and Bound ist hochgradig anpassungsfähig: Wenn Sie komplexe nicht-lineare Nebenbedingungen hinzufügen (z. B. "Arbeiter A kann am Dienstag nicht arbeiten, wenn Arbeiter B Job 3 ausführt"), versagt der Ungarische Algorithmus vollständig, während B&B das Problem weiterhin lösen kann, indem einfach ungültige Zustände verworfen werden!

## Ansatz

Wir können dies als Entscheidungsbaum betrachten.
Ebene 0 weist Arbeiter 0 einen Job zu. Ebene 1 weist Arbeiter 1 einen Job zu, usw.
Auf Ebene 0 hat Arbeiter 0 N Möglichkeiten. Dies erzeugt N Zweige.
Wenn wir alle Zweige untersuchen, prüfen wir N! Permutationen.

**Branch and Bound Pruning (Beschneidung):**
Wir müssen eine **untere Schranke** für jede Teilzuweisung berechnen. Wenn wir die ersten 2 Arbeiter zugewiesen haben, was sind die absolut *minimalen* Kosten für die verbleibenden N-2 Arbeiter?
Da wir minimieren, gilt: Wenn diese `lower_bound` **größer oder gleich** unseren bisher gefundenen globalen `min_cost` ist, beschneiden wir den Zweig!

**Wie berechnet man die untere Schranke?**
Eine sehr einfache und schnelle untere Schranke: Betrachten Sie für jeden nicht zugewiesenen Arbeiter die verfügbaren, nicht zugewiesenen Jobs und nehmen Sie an, dass sie unabhängig voneinander einfach den absolut günstigsten wählen können (unter Ignorierung von Konflikten, bei denen zwei Arbeiter denselben günstigen Job wollen).
`bound = current_accumulated_cost + sum(min(available jobs) for each unassigned worker)`.
Diese Schranke ist mathematisch garantiert $\le$ den tatsächlichen Kosten der vollständigen Zuweisung, was sie sicher für das Pruning macht.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for bb_02: Job Assignment.

Given an n x n cost matrix cost[i][j] = cost to assign job j
to worker i, find the minimum-cost assignment. Brute-force
enumerate all n! permutations of jobs. Setup keeps n small
(n <= 6) so this is tractable.
"""


def solve(cost, n):
    if n == 0:
        return 0
    jobs = list(range(n))
    best = float("inf")

    def helper(worker, used, current):
        nonlocal best
        if worker == n:
            if current < best:
                best = current
            return
        for job in jobs:
            if not used[job]:
                used[job] = True
                helper(worker + 1, used, current + cost[worker][job])
                used[job] = False

    helper(0, [False] * n, 0)
    return best
```

</details>

## Durchlauf

*(Konzeptionell)*
`Kostenmatrix:`
```text
W0: [9, 2, 7]
W1: [6, 4, 3]
W2: [5, 8, 1]
```

1. **Wurzel (Keine Zuweisungen):** Schranke = W0 min(2) + W1 min(3) + W2 min(1) = 6. In den Heap einfügen.
2. **Wurzel entnehmen. Zweig W0:**
   - W0 wählt J0 (Kosten 9). Schranke = 9 + W1 min(3) + W2 min(1) = 13.
   - W0 wählt J1 (Kosten 2). Schranke = 2 + W1 min(3) + W2 min(1) = 6.
   - W0 wählt J2 (Kosten 7). Schranke = 7 + W1 min(4) + W2 min(5) = 16. *(Beachten Sie, dass sich das Minimum geändert hat, da J2 belegt ist!)*
3. **Heap-Zustand:** `[6 (J1), 13 (J0), 16 (J2)]`.
4. **J1-Zweig entnehmen (Best-First). Zweig W1:**
   - W1 wählt J0 (Kosten 6). Summe = 2+6=8. Schranke = 8 + W2 min(1) = 9.
   - W1 wählt J2 (Kosten 3). Summe = 2+3=5. Schranke = 5 + W2 min(5) = 10.
5. **Tiefste Ebene:** Der Heap priorisiert die Erweiterung des Pfades mit `Schranke 9`. W2 ist gezwungen, J2 (Kosten 1) zu wählen. Gesamtkosten = 9.
   - `min_final_cost = 9`.
6. Nun betrachtet der Heap die Pfade mit `Schranke 13` und `Schranke 16` von W0. Da 13 \ge 9, werden diese vollständig BESCHNITTEN und terminiert! ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N^3)$ | $O(N)$ |
| **Durchschnittlicher Fall** | Viel schneller als N! | $O(2^N)$ |
| **Schlechtester Fall** | $O(N!)$ | $O(N!)$ |

Im absolut schlechtesten Fall, in dem die Schranke nichts beschneidet, erzeugt der Baum N! Blätter, was faktorielle Zeit in Anspruch nimmt. Die Priority Queue wächst ebenfalls an, um faktorielle Elemente im Speicher zu halten. Die Best-First-Suchheuristik führt jedoch dazu, dass in Standard-Datensätzen die optimale Lösung fast sofort gefunden wird, wodurch der Großteil des Baumes beschnitten wird.

## Varianten & Optimierungen

- **Ungarischer Algorithmus ($O(N^3)$):** Die exakte, deterministische DP/kombinatorische Lösung. Er erstellt einen bipartiten Graphen und manipuliert die Matrixzeilen und -spalten, um kostenfreie perfekte Matchings zu finden. Er ist für das reine Job-Assignment-Problem mathematisch strikt überlegen gegenüber B&B.

## Anwendungen in der Praxis

- **Ride-Sharing:** Uber/Lyft, die gleichzeitig N Fahrer N Fahrgästen zuweisen, um die globale Gesamtwartezeit zu minimieren.

## Verwandte Algorithmen in cOde(n)

- **[flow_03 - Bipartite Matching](../flow/flow_03_bipartite-matching.md)** — Die ungewichtete, rein strukturelle Version des Zuweisungsproblems.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*