# House Robber

| | |
|---|---|
| **ID** | `dp_11` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(n)$ |
| **Schwierigkeit** | 5/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **Wikipedia** | [Fibonacci-Folge](https://en.wikipedia.org/wiki/Fibonacci_sequence) (gleiche Struktur) |

## Problembeschreibung

Sie sind ein Einbrecher und planen einen Raubzug entlang einer Straße. Die Straße hat `n` Häuser in einer Reihe, jedes mit einem bestimmten Geldbetrag `nums[i]`. Benachbarte Häuser verfügen über verbundene Sicherheitssysteme – das Ausrauben zweier benachbarter Häuser in derselben Nacht löst den Alarm aus. Maximieren Sie den gesamten Geldbetrag, den Sie stehlen können, ohne zwei benachbarte Häuser auszurauben.

**Eingabe:** `nums = [a0, a1, ..., a(n-1)]`.
**Ausgabe:** der maximale Gesamtbetrag.

**Beispiel:**

| nums | Ausgeraubt | Max |
|---|---|---:|
| `[1, 2, 3, 1]` | 1+3 oder 2+1 | **4** |
| `[2, 7, 9, 3, 1]` | 2+9+1 | **12** |
| `[2, 1, 1, 2]` | 2+1 (mittleres überspringen) oder 1+2 | **4** |
| `[5]` | 5 | **5** |
| `[]` | (keine) | **0** |

## Anwendung

- Das kanonische "**Rauben-Überspringen-Entscheiden**" 1D-DP-Problem und eines der bekanntesten Aufwärmübungen für Vorstellungsgespräche. Die Rekurrenz ist intuitiv: Entscheiden Sie bei jedem Haus, ob Sie es überspringen (das bisherige Maximum beibehalten) oder rauben (den Betrag zum Maximum von vor zwei Häusern addieren).
- Grundlage für viele **2-Häuser-Überspringen** DP-Varianten: House Robber II (kreisförmig), House Robber III (Baum) und das "delete-and-earn"-Problem (welches sich mittels Bucket Sort auf House Robber zurückführen lässt).

## Ansatz

Sei `dp[i]` = der maximale Geldbetrag, der unter Berücksichtigung der ersten `i+1` Häuser (Häuser `0..i`) geraubt werden kann.

**Rekurrenz:** Bei Haus `i` gibt es zwei Optionen:
- **Überspringen:** `dp[i] = dp[i-1]`.
- **Rauben:** `dp[i] = nums[i] + dp[i-2]`. (Da Haus `i-1` nicht ausgeraubt werden darf, wird der vorherige Wert von `i-2` genommen.)
- Maximum wählen: `dp[i] = max(dp[i-1], nums[i] + dp[i-2])`.

**Induktionsanfang:** `dp[0] = nums[0]` (nur ein Haus, raube es).
`dp[1] = max(nums[0], nums[1])`.

**Platzoptimierung:** `dp[i]` hängt nur von den letzten beiden Werten ab. Verwenden Sie zwei Variablen: `prev` (= `dp[i-1]`) und `prev2` (= `dp[i-2]`).

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

## Durchlauf

`nums = [2, 7, 9, 3, 1]`. Ergebnis: 12.

| i | nums[i] | prev2 | prev | candidate = prev | nums[i] + prev2 | curr = max |
|---:|---:|---:|---:|---:|---:|---:|
| init | — | 2 | 7 | — | — | — |
| 2 | 9 | 7 | 7 | 7 | 9 + 2 = 11 | **11** |
| 3 | 3 | 7 | 11 | 11 | 3 + 7 = 10 | **11** |
| 4 | 1 | 11 | 11 | 11 | 1 + 11 = 12 | **12** |

Gibt 12 zurück. ✓ (Raube Häuser 0, 2, 4: 2 + 9 + 1 = 12.)

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(n)$ | $O(1)$ — rolling |
| **Durchschnittlicher Fall** | $O(n)$ | $O(1)$ |
| **Schlechtester Fall** | $O(n)$ | $O(1)$ |

Die 2D `dp`-Tabellenversion benötigt $O(n)$ Platz, aber die Rolling-Implementierung benötigt $O(1)$. Beide haben eine Zeitkomplexität von $O(n)$.

## Varianten & Optimierungen

- **House Robber II (kreisförmig)** — die Häuser stehen in einem Kreis, daher sind Haus `0` und Haus `n-1` ebenfalls benachbart. Lösen Sie das reguläre Problem zweimal: einmal für `nums[0..n-2]` und einmal für `nums[1..n-1]`, und wählen Sie das Maximum.
- **House Robber III (Baum)** — die Häuser sind Knoten in einem Binärbaum; kein Eltern-Kind-Paar darf ausgeraubt werden. Rekursion auf Teilbäumen; jeder Knoten gibt `(rob_this, dont_rob_this)` zurück.
- **Delete and Earn** — gegeben sind Punkte, die man nehmen kann, wobei benachbarte Punkte verboten sind, aber die Beziehung basiert auf dem Wert und nicht auf der Position. Sortieren Sie nach Werten (Bucket Sort) und führen Sie dann House Robber auf dem Bucket-Array aus.
- **Maximale Summe nicht benachbarter Elemente** — exakt dasselbe Problem mit anderer Formulierung.

## Anwendungen in der Praxis

- **Auftragsplanung mit Konflikten** — wählen Sie eine Teilmenge von Aufträgen aus, bei denen keine zwei benachbarten (in einer bestimmten Reihenfolge) ausgewählt werden können.
- **Teilmengenauswahl mit paarweisen Ausschlüssen** — wählen Sie Elemente aus einer Liste aus, bei der einige Paare sich gegenseitig ausschließen.
- **Spieltheorie** — viele DP-Probleme in Zwei-Personen-Spielen lassen sich auf dieselbe "Entscheiden oder Überspringen"-Rekurrenz reduzieren.

## Verwandte Algorithmen in cOde(n)

- **[dp_01 — Fibonacci](dp_01_fibonacci.md)** — gleiche 2-Variablen-Rolling-Struktur, Addition statt Maximum. (d=5/10, r=9/10)
- **[dp_02 — Climbing Stairs](dp_02_climbing-stairs.md)** — dieselbe Struktur mit einer Addition statt eines Maximums. (d=5/10, r=9/10)
- **[dp_18 — Max Product Subarray](dp_18_max-product-subarray.md)** — dieselbe 1D-Entscheiden-oder-Überspringen-Struktur, aber der DP-Zustand muss sowohl das Minimum als auch das Maximum verfolgen (wegen negativer Zahlen). (d=5/10, r=9/10)

---

*Diese Dokumentation ist ein Originalinhalt für cOde(n), modelliert nach der kanonischen Struktur, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Anfang der Seite. Quell-Repository: <https://github.com/dawei7/code_n>.*