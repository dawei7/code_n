# Subset Sum

| | |
|---|---|
| **ID** | `dp_06` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(n²)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Subset sum problem](https://en.wikipedia.org/wiki/Subset_sum_problem) |

## Problemstellung

Gegeben ist eine Menge nicht-negativer Ganzzahlen `nums` und ein Zielwert `target`. Bestimmen Sie, ob es eine **Teilmenge** von `nums` gibt, deren Summe exakt `target` ergibt. (Jedes Element darf höchstens einmal verwendet werden.)

**Eingabe:** Ein Array `nums` und eine Zielsumme `target`.
**Ausgabe:** `True`, falls eine Teilmenge existiert, die sich zu `target` aufsummiert, andernfalls `False`.

**Beispiel:**

| nums | target | Antwort | Teilmenge |
|---|---|---|---|
| `[3, 34, 4, 12, 5, 2]` | 9 | True | `{4, 5}` oder `{3, 2, 4}` |
| `[3, 34, 4, 12, 5, 2]` | 30 | False | — |
| `[1, 5, 11, 5]` | 11 | True | `{11}` |
| `[1, 2, 3]` | 7 | False | `{1, 2, 4}` (keine 4) — Moment, `{1, 3, 3}` — eigentlich nein. Die Antwort ist False; 1+2+3=6 ≠ 7. |

## Anwendung

- Die Entscheidungsversion des 0/1-Knapsack-Problems. Grundlage für "**Partition**"-Probleme (`dp_17`), das **Merkle-Hellman**-Kryptosystem und viele Teilprobleme in Vorstellungsgesprächen.
- Immer wenn die Frage lautet: "**Kann ich eine Teilmenge wählen, die exakt X ergibt?**", ist dies das passende Schema.

## Ansatz

Sei `dp[i][t]` = können die ersten `i` Elemente eine Teilmenge bilden, die sich zu `t` aufsummiert?

**Rekurrenz** (betrachte das Element `nums[i-1]`):
- **Überspringen:** `dp[i][t] = dp[i-1][t]`.
- **Auswählen** (falls `nums[i-1] <= t`): `dp[i][t] = dp[i-1][t - nums[i-1]]`.
- Beides kombiniert: `dp[i][t] = dp[i-1][t] OR dp[i-1][t - nums[i-1]]`.

**Induktionsanfang:** `dp[0][0] = True` (die leere Menge summiert sich zu 0).
`dp[0][t] = False` für `t > 0`.

**Antwort:** `dp[n][target]`.

**Platzoptimierung:** Reduzierung der 2D-Tabelle auf ein 1D-`bool`-Array, wobei **von rechts nach links** iteriert wird, um die Zeile, die wir noch benötigen, nicht zu überschreiben:

```
dp[0] = True
for x in nums:
    for t from target down to x:
        dp[t] = dp[t] or dp[t - x]
return dp[target]
```

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_06: Subset Sum.

True iff some subset of arr sums to target. Set-based DP over
the running reachable sums.
"""


def solve(arr, target):
    reachable = {0}
    for v in arr:
        reachable = reachable | {s + v for s in reachable}
    return target in reachable
```

</details>

## Durchlauf

`nums = [3, 1, 4, 1]`, `target = 5`. Antwort: True (`{1, 4}`).

`dp = [T, F, F, F, F, F]`.

**x = 3:**

| t | dp[t] vorher | Kandidat (dp[t-3]) | dp[t] nachher |
|---:|---:|---:|---:|
| 5 | F | dp[2]=F | F |
| 4 | F | dp[1]=F | F |
| 3 | F | dp[0]=T | **T** |

`dp = [T, F, F, T, F, F]`.

**x = 1:**

| t | dp[t] vorher | Kandidat (dp[t-1]) | dp[t] nachher |
|---:|---:|---:|---:|
| 5 | F | dp[4]=F | F |
| 4 | F | dp[3]=T | **T** |
| 3 | T | dp[2]=F | T |
| 2 | F | dp[1]=F | F |
| 1 | F | dp[0]=T | **T** |

`dp = [T, T, F, T, T, F]`.

**x = 4:**

| t | dp[t] vorher | Kandidat (dp[t-4]) | dp[t] nachher |
|---:|---:|---:|---:|
| 5 | F | dp[1]=T | **T** |
| 4 | T | dp[0]=T | T |

`dp = [T, T, F, T, T, T]`.

**x = 1:**

| t | dp[t] vorher | Kandidat (dp[t-1]) | dp[t] nachher |
|---:|---:|---:|---:|
| 5 | T | dp[4]=T | T |
| 4 | T | dp[3]=T | T |

`dp[5] = T`. Antwort: True. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n·target)$ | $O(target)$ |
| **Durchschnittlicher Fall** | $O(n·target)$ | $O(target)$ |
| **Schlechtester Fall** | $O(n·target)$ | $O(target)$ |

Pseudopolynomiell in `target` (gleiche Einschränkung wie beim 0/1-Knapsack-Problem).
Für sehr große `target`-Werte ist die exakte Lösung exponentiell.

## Varianten & Optimierungen

- **Teilmengen zählen** — ändere `dp[t] = dp[t] or dp[t - x]` zu `dp[t] = dp[t] + dp[t - x]`.
- **Die tatsächliche Teilmenge finden** — führe ein paralleles `parent[t, i]`-Array, das angibt, ob `dp[t]` durch Überspringen oder Auswählen gesetzt wurde; gehe den Pfad zurück, um die Teilmenge zu rekonstruieren.
- **Partition Equal Subset Sum** (`dp_17`) — existiert eine Teilmenge, die sich zu `total / 2` aufsummiert? Wende dieses DP mit `target = total / 2` an.
- **Minimale Differenz der Teilmengensummen** — minimiere `|sum1 - sum2|` bei einer Partitionierung in zwei annähernd gleiche Teilmengen. Gleiches DP, anderes Ziel (erreichbare Summen verfolgen, das Beste finden).
- **Beschränkte Teilmengensumme** (jedes Element höchstens `k`-mal) — verwende den Binärzerlegungstrick, um es auf 0/1 zu reduzieren.
- **Mehrfache Anfragen** — sortiere `nums` einmal, verwende dann für jede Anfrage ein auf sortierten Mengen basierendes DP (Meet-in-the-middle für `n > 30`).

## Anwendungen in der Praxis

- **Merkle-Hellman-Knapsack-Kryptosystem** — basiert auf der Härte des Subset-Sum-Problems. (Durch Gitterreduktion gebrochen, aber historisch bedeutsam.)
- **Ressourcenallokation** — "können wir das verfügbare Personal so einteilen, dass exakt die benötigten Stunden abgedeckt werden?"
- **Scheduling** — "gibt es eine Teilmenge von Jobs, die exakt in die Tageskapazität passt?"
- **Kombinatorische Auktionen** — "gibt es eine Teilmenge von Geboten, die exakt dem Mindestpreis des Verkäufers entspricht?"
- **Portfolio-Rebalancing** — "können wir eine Teilmenge von Positionen wählen, die sich exakt zum Zielwert aufsummiert?"

## Verwandte Algorithmen in cOde(n)

- **[dp_03 — 0/1 Knapsack](dp_03_knapsack.md)** — beschränkte Variante mit zwei Attributen (Gewicht + Wert), maximieren. (d=5/10, r=9/10)
- **[dp_17 — Partition Equal Subset Sum](dp_17_partition-equal-subset-sum.md)** — `dp_06` angewendet auf `target = total/2`. (d=5/10, r=9/10)
- **[dp_05 — Coin Change](dp_05_coin-change.md)** — unbeschränkte Variante (jede Münze kann mehrfach verwendet werden). (d=5/10, r=9/10)
- **[dp_30 — Coin Change (Count Ways)](dp_30_coin-change-count-ways.md)** — unbeschränkt, Lösungen zählen. (d=3/10, r=9/10)

---

*Diese Dokumentation ist ein Originalinhalt für cOde(n), modelliert nach der kanonischen Struktur, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*