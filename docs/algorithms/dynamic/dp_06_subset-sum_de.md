# Teilmenge-Summe

| | |
|---|---|
| **ID** | `dp_06` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(n²)$ |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Teilmenge-Summen-Problem](https://en.wikipedia.org/wiki/Subset_sum_problem) |

## Aufgabenstellung

Gegeben sei eine Menge nicht-negativer Ganzzahlen `nums` und eine Zielsumme
`target`. Bestimme, ob es eine **Teilmenge** von `nums` gibt,
deren Summe genau `target` ergibt. (Jedes Element darf
höchstens einmal verwendet werden.)

**Eingabe:** ein Array `nums` und eine Zielsumme `target`.
**Ausgabe:** `True`, wenn eine Teilmenge die Summe `target` ergibt, andernfalls `False`.

**Beispiel:**

| Zahlen | Ziel | Antwort | Teilmenge |
|---|---|---|---|
| `[3, 34, 4, 12, 5, 2]` | 9 | Wahr | `{4, 5}` oder `{3, 2, 4}` |
| `[3, 34, 4, 12, 5, 2]` | 30 | Falsch | — |
| `[1, 5, 11, 5]` | 11 | Wahr | `{11}` |
| `[1, 2, 3]` | 7 | Wahr | `{1, 2, 4}` (Nr. 4) — Moment, `{1, 3, 3}` — eigentlich nein. Die Antwort lautet „Falsch“; 1+2+3=6 ≠ 7. |

## Wann man es verwendet

- Die Entscheidungsversion des 0/1-Rucksacks. Grundlage für
  „**Partition**“-Probleme (`dp_17`), das **Merkle-Hellman**-
  Kryptosystem und viele Teilprobleme in Vorstellungsgesprächen.
- Immer wenn die Frage lautet: „**Kann ich eine Teilmenge auswählen, die
  genau X entspricht?**“, ist dies die richtige Herangehensweise.

## Vorgehensweise

Sei `dp[i][t]` = Können die ersten `i` Elemente eine Teilmenge bilden, deren
Summe `t` ergibt?

**Rekursion** (betrachte das Element `nums[i-1]`):
- **Überspringen:** `dp[i][t] = dp[i-1][t]`.
- **Berücksichtigen** (wenn `nums[i-1] <= t`): `dp[i][t] = dp[i-1][t - nums[i-1]]`.
- Entweder: `dp[i][t] = dp[i-1][t] OR dp[i-1][t - nums[i-1]]`.

**Basisfall:** `dp[0][0] = True` (die leere Menge ergibt 0).
`dp[0][t] = False` für `t > 0`.

**Antwort:** `dp[n][target]`.

**Speicheroptimierung:** Die 2D-Tabelle in ein 1D-`bool`
Array umwandeln und **von rechts nach links** durchlaufen, damit wir die
Zeile, die wir noch verwenden, nicht überschreiben:

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

## Schritt-für-Schritt-Anleitung

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

| t | dp[t] vorher | Kandidat (dp[t-1]) | dp[t] danach |
|---:|---:|---:|---:|
| 5 | F | dp[4]=F | F |
| 4 | F | dp[3]=T | **T** |
| 3 | T | dp[2]=F | T |
| 2 | F | dp[1]=F | F |
| 1 | F | dp[0]=T | **T** |

`dp = [T, T, F, T, T, F]`.

**x = 4:**

| t | dp[t] vorher | Kandidat (dp[t-4]) | dp[t] danach |
|---:|---:|---:|---:|
| 5 | F | dp[1]=T | **T** |
| 4 | T | dp[0]=T | T |

`dp = [T, T, F, T, T, T]`.

**x = 1:**

| t | dp[t] vorher | Kandidat (dp[t-1]) | dp[t] danach |
|---:|---:|---:|---:|
| 5 | T | dp[4]=T | T |
| 4 | T | dp[3]=T | T |

`dp[5] = T`. Antwort: Richtig. ✓

## Komplexität

| | Zeit | Speicher |
|---|---|---|
| **Best** | $O(n·target)$ | $O(target)$ |
| **Durchschnittlicher Fall** | $O(n·target)$ | $O(target)$ |
| **Schlechtester Fall** | $O(n·target)$ | $O(target)$ |

Pseudopolynomial in `target` (gleiche Einschränkung wie beim 0/1-Rucksackproblem).
Bei sehr großen `target` ist die exakte Lösung exponentiell.

## Varianten & Optimierungen

- **Teilmengen zählen** — `dp[t] = dp[t] or dp[t - x]`
  in `dp[t] = dp[t] + dp[t - x]` ändern.
- **Die tatsächliche Teilmenge finden** — führe parallel ein `parent[t, i]`
  , das angibt, ob `dp[t]` durch „Skip“ oder „Take“ gesetzt wurde; gehe
  zurück, um die Teilmenge zu rekonstruieren.
- **Partition mit gleicher Teilmenge-Summe** (`dp_17`) — gibt es
  eine Teilmenge, deren Summe `total / 2` ergibt? Wende diese DP mit
  `target = total / 2` an.
- **Minimale Differenz der Teilmengen-Summen** — Minimiere `|sum1 - sum2|`
  über eine Partition in zwei annähernd gleiche Teilmengen. Gleiche DP,
  anderes Ziel (erreichbare Summen verfolgen, beste finden).
- **Begrenzte Teilmengen-Summe** (jedes Element höchstens `k`-mal) —
  verwende den Trick der binären Zerlegung, um auf 0/1 umzuwandeln.
- **Mehrere Abfragen** — sortiere `nums` einmal, verwende dann für jede
  Abfrage eine auf sortierten Mengen basierende DP (Meet-in-the-Middle für
  `n > 30`).

## Anwendungen in der Praxis

- **Merkle-Hellman-Rucksack-Kryptosystem** — basiert auf der
  Schwierigkeit des Teilsummenproblems. (Durch Gitterreduktion geknackt, aber
  historisch bedeutsam.)
- **Ressourcenzuweisung** — „Können wir das verfügbare Personal so zuweisen,
  dass genau die erforderlichen Arbeitsstunden abgedeckt werden?“
- **Terminplanung** — „Gibt es eine Teilmenge von Aufträgen, die genau in
  die Tageskapazität passt?“
- **Kombinatorische Auktionen** — „Gibt es eine Teilmenge von Geboten,
  die genau dem Mindestpreis des Verkäufers entspricht?“
- **Portfolio-Neugewichtung** — „Können wir eine Teilmenge von
  Positionen auswählen, deren Summe dem angestrebten Nominalwert entspricht?“

## Verwandte Algorithmen in cOde(n)

- **[dp_03 — 0/1-Rucksackproblem](dp_03_knapsack.md)** — begrenzte
  Variante mit zwei Attributen (Gewicht + Wert), Maximierung.
  (d=5/10, r=9/10)
- **[dp_17 — Partition Equal Subset Sum](dp_17_partition-equal-subset-sum.md)** —
  `dp_06` angewendet auf `target = total/2`. (d=5/10, r=9/10)
- **[dp_05 — Münzwechsel](dp_05_coin-change.md)** — unbegrenzte
  Variante (jede Münze kann mehrfach verwendet werden). (d=5/10, r=9/10)
- **[dp_30 — Wechselgeld (Anzahl der Möglichkeiten)](dp_30_coin-change-count-ways.md)** —
  unbegrenzt, Anzahl der Lösungen. (d=3/10, r=9/10)

---

*Diese Dokumentation ist ein Originalbeitrag, der für cOde(n) verfasst wurde,
in Anlehnung an die kanonische Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Den kanonischen Enzyklopädieeintrag
finden Sie unter dem Wikipedia-Link oben auf der Seite.
Quell-Repository: <https://github.com/dawei7/code_n>.*
