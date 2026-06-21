# Stable Marriage Problem (Gale-Shapley)

| | |
|---|---|
| **ID** | `greedy_13` |
| **Kategorie** | greedy |
| **Komplexität (erforderlich)** | $O(N^2)$ Zeit, $O(N^2)$ Platz |
| **Schwierigkeit** | 6/10 |
| **Relevanz für Vorstellungsgespräche** | 3/10 |
| **Wikipedia** | [Gale-Shapley algorithm](https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm) |

## Problemstellung

Gegeben sind `N` Männer und `N` Frauen, wobei jede Person alle Mitglieder des anderen Geschlechts nach ihren Präferenzen geordnet hat.
Verheirate die Männer und Frauen so, dass es KEINE zwei Personen des anderen Geschlechts gibt, die sich gegenseitig lieber hätten als ihre aktuellen Partner.
Wenn es keine solchen Paare gibt, gelten die Ehen als **"stabil"**.
Gib eine Liste der `N` stabilen Paare zurück.

**Eingabe:** Ein 2D-Array `men_prefs` der Größe N x N und ein 2D-Array `women_prefs` der Größe N x N.
**Ausgabe:** Ein Array/Dictionary, das Männer auf Frauen abbildet (oder umgekehrt).

## Wann man es verwendet

- Zur Lösung von Problemen des bipartiten Matchings, bei denen beide Mengen strikte Präferenzlisten haben.
- *Trivia:* Der Gale-Shapley-Algorithmus garantiert mathematisch, dass für jede gleiche Anzahl von Männern und Frauen IMMER ein stabiles Matching existiert. Er wurde 2012 mit dem Nobelpreis für Wirtschaftswissenschaften ausgezeichnet!

## Ansatz

**1. Der Antragsteller und der Empfänger:**
Der Algorithmus bestimmt eine Gruppe als "Antragsteller" (traditionell die Männer) und die andere als "Empfänger" (die Frauen).
- Männer machen gierig (greedily) Anträge bei ihrer jeweils besten noch verfügbaren Wahl auf ihrer Liste.
- Frauen nehmen den besten Antrag, den sie erhalten, vorläufig an. Wenn später ein besserer Antrag eingeht, werden sie ihren aktuellen Partner rücksichtslos verlassen und den neuen annehmen!

**2. Die Datenstrukturen:**
- `free_men`: Eine Queue von Männern, die aktuell unverheiratet sind.
- `women_partner`: Ein Array, das verfolgt, mit wem jede Frau aktuell verlobt ist (anfangs überall `-1`).
- `man_next_proposal`: Ein Array, das den *Index* der nächsten Frau verfolgt, der ein Mann einen Antrag machen sollte (damit er nicht derselben Frau zweimal einen Antrag macht).
- **Optimierung:** Wenn eine Frau einen neuen Antrag von Mann B erhält, während sie mit Mann A verlobt ist, muss sie wissen, wen sie bevorzugt. Das Durchsuchen ihrer Präferenzliste dauert $O(N)$ Zeit. Wir können eine `inverse_women_prefs`-Matrix vorab berechnen, bei der `matrix[woman][man]` seinen numerischen Rang (z. B. 1. Wahl, 5. Wahl) in $O(1)$ Zeit zurückgibt!

**3. Der Algorithmus (Solange es einen freien Mann gibt):**
1. Entnehme einen Mann `m` aus der `free_men`-Queue.
2. Betrachte seine Präferenzliste. Finde die am höchsten bewertete Frau `w`, der er noch keinen Antrag gemacht hat.
3. Hat `w` einen Partner?
   - **NEIN:** Sie nimmt an! Sie sind verlobt.
   - **JA:** Sie vergleicht ihren aktuellen Partner `m_old` mit dem neuen Antragsteller `m`.
     - Wenn sie `m_old` bevorzugt, weist sie `m` ab. `m` kommt zurück in die `free_men`-Queue!
     - Wenn sie `m` bevorzugt, nimmt sie `m` an! Sie sind verlobt. `m_old` wird verlassen und kommt zurück in die `free_men`-Queue!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for greedy_13: Stable Marriage (Gale-Shapley).

Each free man proposes to his next-best. The woman accepts
iff she prefers him to her current match.
"""


def solve(n, men_prefs, women_prefs):
    if n == 0:
        return []
    next_w = [0] * n
    woman_engaged_to = [-1] * n
    man_engaged_to = [-1] * n
    woman_rank = [[0] * n for _ in range(n)]
    for w in range(n):
        for rank, m in enumerate(women_prefs[w]):
            woman_rank[w][m] = rank
    free_men = list(range(n))
    while free_men:
        m = free_men.pop(0)
        w = men_prefs[m][next_w[m]]
        next_w[m] += 1
        if woman_engaged_to[w] == -1:
            woman_engaged_to[w] = m
            man_engaged_to[m] = w
        else:
            current = woman_engaged_to[w]
            if woman_rank[w][m] < woman_rank[w][current]:
                woman_engaged_to[w] = m
                man_engaged_to[m] = w
                man_engaged_to[current] = -1
                free_men.append(current)
            else:
                free_men.insert(0, m)
    return man_engaged_to
```

</details>

## Durchlauf

`N = 2`.
`men_prefs`:
- `M0`: `[W1, W0]` (Bevorzugt 1 gegenüber 0)
- `M1`: `[W1, W0]` (Bevorzugt 1 gegenüber 0)

`women_prefs`:
- `W0`: `[M0, M1]` (Bevorzugt 0 gegenüber 1)
- `W1`: `[M1, M0]` (Bevorzugt 1 gegenüber 0)

`women_partner = [-1, -1]`. `free_men = [0, 1]`.

1. Entnehme `M0`.
   - Macht `W1` einen Antrag (1. Wahl).
   - `W1` ist frei! Verlobt! `women_partner = [-1, 0]`.
2. Entnehme `M1`.
   - Macht `W1` einen Antrag (1. Wahl).
   - `W1` ist mit `M0` verlobt.
   - Vergleich: `W1` bevorzugt `M1` (Rang 0) gegenüber `M0` (Rang 1).
   - Verlässt `M0`! Verlobt mit `M1`. `women_partner = [-1, 1]`.
   - `M0` wird verlassen und zurück zu `free_men` hinzugefügt.
3. Entnehme `M0`.
   - Macht `W0` einen Antrag (2. Wahl).
   - `W0` ist frei! Verlobt! `women_partner = [0, 1]`.
4. `free_men` ist leer. Beende.

Ergebnis: `(M0-W0)`, `(M1-W1)`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(N^2)$ |
| **Durchschnittlicher Fall** | $O(N^2)$ | $O(N^2)$ |
| **Schlechtester Fall** | $O(N^2)$ | $O(N^2)$ |

Im schlechtesten Fall macht jeder Mann jedem einzelnen Antragsteller genau einmal einen Antrag. Es gibt N Männer und N Frauen, also gibt es höchstens N^2 Anträge. Dank unserer `women_ranks`-Matrix zur Vorberechnung dauert das Annehmen oder Ablehnen eines Antrags strikt $O(1)$ Zeit. Daher beträgt die gesamte Zeitkomplexität $O(N^2)$.
Die Platzkomplexität beträgt $O(N^2)$, um die `women_ranks`-Matrix zu speichern (die Eingabelisten haben ebenfalls eine Größe von $O(N^2)$).

## Varianten & Optimierungen

- **Bias der Antragsteller:** Der Gale-Shapley-Algorithmus ist bekanntermaßen "Antragsteller-optimal" und "Empfänger-pessimal". Die Gruppe, die die Anträge stellt, erhält IMMER ihr absolut bestmögliches stabiles Matching. Die Gruppe, die die Anträge empfängt, erhält IMMER ihr absolut schlechtestes stabiles Matching! Um die Frauen zu bevorzugen, kehre den Algorithmus einfach um, sodass die Frauen die Anträge stellen.

## Anwendungen in der Praxis

- **The National Resident Matching Program (NRMP):** Das tatsächliche System, das in den Vereinigten Staaten seit 1952 verwendet wird, um Tausende von Medizinabsolventen an Krankenhaus-Assistenzarztprogramme zu vermitteln. Krankenhäuser bewerten Studenten, Studenten bewerten Krankenhäuser, und Gale-Shapley vermittelt sie fehlerfrei!
- **CDN-Server-Zuweisung:** Zuweisung von Benutzern zu physischen Content Delivery Network-Knoten basierend auf Latenzpräferenzen und Kapazitätsgrenzen der Serverlast.

## Verwandte Algorithmen in cOde(n)

- **[graph_12 - Bipartite Check](../graphs/graph_12_bipartite-check.md)** — Der grundlegende Algorithmus, um Knoten in zwei disjunkte Mengen (wie Männer und Frauen) zu trennen, bevor sie gematcht werden.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*