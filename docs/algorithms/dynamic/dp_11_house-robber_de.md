# Einbrecher

| | |
|---|---|
| **ID** | `dp_11` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(n)$ |
| **Schwierigkeitsgrad** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Fibonacci-Folge](https://en.wikipedia.org/wiki/Fibonacci_sequence) (gleiche Form) |

## Aufgabenstellung

Du bist ein Einbrecher, der einen Raubzug entlang einer Straße plant. Die Straße
besteht aus `n` Häusern in einer Reihe, in denen jeweils eine bestimmte Geldsumme
`nums[i]` aufbewahrt wird. Benachbarte Häuser verfügen über miteinander verbundene Alarmanlagen –
wenn du in derselben Nacht zwei benachbarte Häuser ausraubst, wird
der Alarm ausgelöst. Maximiere die Gesamtsumme des Geldes, das du stehlen kannst, ohne
zwei benachbarte Häuser auszurauben.

**Eingabe:** `nums = [a0, a1, ..., a(n-1)]`.
**Ausgabe:** die maximale Gesamtsumme des Geldes.

**Beispiel:**

| Zahlen | Ausgeraubt | Max |
|---|---|---:|
| `[1, 2, 3, 1]` | 1+3 oder 2+1 | **4** |
| `[2, 7, 9, 3, 1]` | 2+9+1 | **12** |
| `[2, 1, 1, 2]` | 2+1 (mittleres Haus überspringen) oder 1+2 | **4** |
| `[5]` | 5 | **5** |
| `[]` | (keine) | **0** |

## Wann man es verwendet

- Die klassische „**rob-skip-decide**“-1D-DP und eine der
  bekanntesten Aufwärmaufgaben in Vorstellungsgesprächen. Die Rekursion ist
  intuitiv: Entscheide bei jedem Haus, ob du es überspringst (behalte das
  vorherige Maximum) oder es nimmst (addiere es zum Maximum von vor zwei Häusern
  hinzu).
- Grundlage für viele **2-Haus-Überspringen**-DP-Varianten: „House
  Robber II“ (zyklisch), „House Robber III“ (Baum) und das
  „Delete-and-Earn“-Problem (das sich über Bucket-Sort auf „House
  Robber“ zurückführen lässt).

## Vorgehensweise

Sei `dp[i]` = der maximale Raubbetrag, der unter Berücksichtigung nur der
ersten `i+1` Häuser (Häuser `0..i`) erzielt werden kann.

**Rekursion:** Bei Haus `i` gibt es zwei Optionen:
- **Überspringen:** `dp[i] = dp[i-1]`.
- **Es nehmen:** `dp[i] = nums[i] + dp[i-2]`. (Das Haus `i-1` kann noch nicht
  ausgeraubt worden sein, daher liegt der letzte Raub bei `i-2`.)
- Das Maximum nehmen: `dp[i] = max(dp[i-1], nums[i] + dp[i-2])`.

**Basisfall:** `dp[0] = nums[0]` (nur ein Haus, nehmen).
`dp[1] = max(nums[0], nums[1])`.

**Speicherplatzoptimierung:** `dp[i]` hängt nur von den letzten beiden
Werten ab. Würfeln mit zwei Variablen: `prev` (= `dp[i-1]`) und
`prev2` (= `dp[i-2]`).

**Ergebnis:** `dp[n-1]` (oder `prev` am Ende der Schleife).

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_11: House Robber.

Max sum of non-adjacent elements.
"""


def solve(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    dp = [0] * (n + 1)
    dp[1] = arr[0]
    for i in range(2, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i - 1])
    return dp[n]
```

</details>

## Schritt-für-Schritt-Anleitung

`nums = [2, 7, 9, 3, 1]`. Antwort: 12.

| i | nums[i] | prev2 | prev | candidate = prev | nums[i] + prev2 | curr = max |
|---:|---:|---:|---:|---:|---:|---:|
| init | — | 2 | 7 | — | — | — |
| 2 | 9 | 7 | 7 | 7 | 9 + 2 = 11 | **11** |
| 3 | 3 | 7 | 11 | 11 | 3 + 7 = 10 | **11** |
| 4 | 1 | 11 | 11 | 11 | 1 + 11 = 12 | **12** |

Gibt 12 zurück. ✓ (Rob bewohnt die Häuser 0, 2, 4: 2 + 9 + 1 = 12.)

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(n)$ | $O(1)$ — rollierend |
| **Durchschnittlicher Fall** | $O(n)$ | $O(1)$ |
| **Schlechteste** | $O(n)$ | $O(1)$ |

Die 2D-Tabellenversion `dp` benötigt $O(n)$ Speicherplatz, die rollende
Implementierung hingegen $O(1)$. Beide benötigen $O(n)$ Zeit.

## Varianten & Optimierungen

- **House Robber II (kreisförmig)** — Die Häuser stehen im Kreis, daher
  sind Haus `0` und Haus `n-1` ebenfalls benachbart. Löse das
  reguläre Problem zweimal: einmal für `nums[0..n-2]`, einmal für
  `nums[1..n-1]`, nimm den Maximalwert. (Nicht direkt in cOde(n).)
- **House Robber III (Baum)** — Häuser sind Knoten in einem binären
  Baum, keine zwei Eltern-Kind-Paare dürfen ausgeraubt werden. Rekursion auf
  Teilbäumen; jeder Knoten gibt `(rob_this, dont_rob_this)` zurück.
- **Löschen und Verdienen** — bestimmte Punkte dürfen genommen werden, benachbarte
  Punkte sind verboten, aber die Beziehung basiert auf dem Wert und nicht
  auf der Position. Bucket-Sortierung nach Wert, anschließend „House Robber“
  auf das Bucket-Array anwenden.
- **Maximale Summe nicht benachbarter Elemente** — genau dasselbe
  Problem mit anderer Formulierung.

## Anwendungen in der Praxis

- **Auftragsplanung mit Konflikten** — Wähle eine Teilmenge von Aufträgen aus,
  bei der keine zwei benachbarten (in einer bestimmten Reihenfolge) ausgewählt werden dürfen.
- **Teilmengenauswahl mit paarweisen Ausschlüssen** – Wähle Elemente
  aus einer Liste aus, wobei sich einige Paare gegenseitig ausschließen.
- **Spieltheorie** – Viele DP-Probleme bei Zwei-Spieler-Spielen lassen sich
  auf dieselbe „Entscheiden oder Überspringen“-Rekursion zurückführen.

## Verwandte Algorithmen in cOde(n)

- **[dp_01 — Fibonacci](dp_01_fibonacci.md)** — dieselbe „rollende“ Form mit 2 Variablen,
  Addition statt Maximalwert. (d=5/10, r=9/10)
- **[dp_02 — Treppensteigen](dp_02_climbing-stairs.md)** —
  dieselbe Struktur mit einem „+“ anstelle von „max“ (d=5/10, r=9/10)
- **[dp_18 — Subarray mit maximalem Produkt](dp_18_max-product-subarray.md)** —
  gleiche 1D-Entscheide-oder-Überspringe-Form, aber der DP-Zustand muss
  sowohl Min als auch Max verfolgen (wegen negativer Werte). (d=5/10, r=9/10)

---

*Diese Dokumentation ist Originalinhalt, der für cOde(n) verfasst wurde,
nach dem Vorbild der kanonischen Struktur, die von Referenzseiten zum Thema
Wettbewerbsprogrammierung verwendet wird. Für den kanonischen Enzyklopädieeintrag
folgen Sie bitte dem Wikipedia-Link oben auf der Seite.
Quell-Repository: <https://github.com/dawei7/code_n>.*
