# Abgleich mit regulären Ausdrücken

| | |
|---|---|
| **ID** | `dp_30` |
| **Kategorie** | dynamisch |
| **Komplexität (erforderlich)** | $O(M * N)$ Zeit, $O(M * N)$ Speicherplatz |
| **Schwierigkeitsgrad** | 9/10 |
| **Relevanz für Vorstellungsgespräche** | 5/10 |
| **LeetCode-Äquivalent** | [Abgleich mit regulären Ausdrücken](https://leetcode.com/problems/regular-expression-matching/) |

## Aufgabenstellung

Gegeben sei eine Eingabezeichenkette `s` und ein Muster `p`. Implementiere einen regulären Ausdruck mit Unterstützung für `.` und `*`, wobei gilt:
- `.` Stimmt mit einem beliebigen einzelnen Zeichen überein.
- `*` passt auf null oder mehr des **vorangehenden** Elements.
Der Abgleich sollte die gesamte Eingabezeichenkette abdecken (keine Teilabgleiche).

**Eingabe:** Zwei Zeichenketten `s` und `p`.
**Ausgabe:** Ein boolescher Wert: `True`, wenn `s` mit `p` übereinstimmt, andernfalls `False`.

## Wann man es verwendet

- Um fortgeschrittene String-DP-Verarbeitung zu veranschaulichen, bei der der Zustandsübergang aufgrund von Modifikatoren variabler Länge (wie `*`) mehr als einen Schritt RÜCKWÄRTS geht.
- *Hinweis:* Verwechsle dies nicht mit dem Wildcard-Matching (`dp_09`), bei dem `*` mit *beliebigen Sequenzen* übereinstimmt. Hier bedeutet `a*` ausdrücklich null oder mehr `a`s!

## Vorgehensweise

**1. Definieren des Zustands:**
Sei `dp[i][j]` ein Boolescher Wert, der angibt, ob das Präfix `s[0...i-1]` mit dem Musterpräfix `p[0...j-1]` übereinstimmt.

**2. Grundfälle ermitteln:**
- `dp[0][0] = True`: Eine leere Zeichenkette stimmt mit einem leeren Muster überein.
- `dp[i][0] = False`: Eine nicht leere Zeichenkette stimmt NIEMALS mit einem leeren Muster überein.
- `dp[0][j]`: Eine leere Zeichenkette KANN mit einem nicht leeren Muster übereinstimmen, jedoch NUR, wenn das Muster eine Folge optionaler Zeichen ist (z. B. `a*b*c*`).
  Damit eine leere Zeichenkette mit `p[0...j-1]` übereinstimmt, MUSS das letzte Zeichen `*` sein, und wenn wir `*` und das davorliegende Zeichen ignorieren, muss der Rest des Musters AUCH mit der leeren Zeichenkette übereinstimmen!
  `dp[0][j] = dp[0][j-2]` (wenn `p[j-1] == '*'`).

**3. Finde den Übergang (die Rekursionsbeziehung):**
Wir vergleichen das aktuelle Zeichen `s[i-1]` mit `p[j-1]`.
- **Fall A (Direkte Übereinstimmung):**
  Wenn `p[j-1]` ein normales Zeichen ist und `p[j-1] == s[i-1]`, oder wenn `p[j-1] == '.'`, handelt es sich um eine 1:1-Übereinstimmung!
  Die Strings stimmen überein, wenn ihre verbleibenden Präfixe übereinstimmen.
  `dp[i][j] = dp[i-1][j-1]`
- **Fall B (Das knifflige `*`):**
  Wenn `p[j-1] == '*'`, betrachten wir das Zeichen *vor* dem Sternchen: `p[j-2]`.
  Wir haben zwei verschiedene Möglichkeiten, um `*` gültig zu machen:
  1. **Null Vorkommen (Ignorieren):** Wir verwerfen einfach `*` und das vorangehende Zeichen.
 `dp[i][j] = dp[i][j-2]`
  2. **Ein oder mehrere Vorkommen (verwenden):** Wir können es nur verwenden, WENN das vorangehende Zeichen `p[j-2]` tatsächlich mit `s[i-1]` übereinstimmt (oder ein `.` ist). Wenn es übereinstimmt, „verbrauchen“ wir `s[i-1]`, behalten aber das `*` im Muster aktiv, damit es weitere Zeichen verbrauchen kann!
     `dp[i][j] = dp[i-1][j]` (Nur gültig, wenn `p[j-2] == s[i-1]` oder `p[j-2] == '.'`)

  Da beide Optionen gültig sind, nehmen wir den Booleschen Wert `OR`!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for dp_30: Coin Change (Count Ways).

dp[a] = number of ways to make a. For each coin c, walk
forward: dp[a] += dp[a - c].
"""


def solve(coins, n, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:
        for a in range(c, amount + 1):
            dp[a] += dp[a - c]
    return dp[amount]
```

</details>

## Schritt-für-Schritt-Anleitung

`s = "aab"`, `p = "c*a*b"`. M=3, N=5.
Basisfälle (i=0): `dp[0][0]=T`.
`j=2 ('*')`: `dp[0][2] = dp[0][0] = T` („c*“).
`j=4 ('*')`: `dp[0][4] = dp[0][2] = T` („c*a*“).

1. **i = 1 („a“):**
   - `j=1 ('c')`: Falsch.
   - `j=2 ('*')`: Keine Vorkommen (`dp[1][0]=F`).
   - `j=3 ('a')`: Direkte Übereinstimmung. `dp[1][3] = dp[0][2] = T`.
   - `j=4 ('*')`: Keine Vorkommen (`dp[1][2]=F`) ODER Verwenden (`p[j-2]=='a' == s[i-1]`, also `dp[0][4]=T`). `dp[1][4] = T`.
2. **i = 2 („a“):**
   - `j=4 ('*')`: Keine Vorkommen (`dp[2][2]=F`) ODER Verwende es (`p[j-2]=='a' == s[i-1]`, also `dp[1][4]=T`). `dp[2][4] = T`.
3. **i = 3 ('b'):**
   - `j=4 ('*')`: Keine Vorkommen (`dp[3][2]=F`). Die Verwendung schlägt fehl (`'a' != 'b'`). Falsch.
   - `j=5 ('b')`: Direkte Übereinstimmung. `dp[3][5] = dp[2][4] = T`!

Das Ergebnis `dp[3][5]` ist `True`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Best** | $O(M * N)$ | $O(M * N)$ |
| **Durchschnittlicher Fall** | $O(M * N)$ | $O(M * N)$ |
| **Schlechtester Fall** | $O(M * N)$ | $O(M * N)$ |

Die verschachtelten Schleifen werden bedingungslos genau M × N Mal ausgeführt. Die Zeitkomplexität beträgt streng $O(M \times N)$.
Die Platzkomplexität beträgt $O(M \times N)$ für die DP-Matrix. Technisch lässt sie sich mit einem eindimensionalen rollierenden Array auf $O(N)$ reduzieren, doch da `*` einen Rückblick auf `j-2` erfordert, wird die Zustandsverwaltung in einer Interviewsituation sehr fehleranfällig. Aus Gründen der Übersichtlichkeit ist die 2D-Matrix bei weitem vorzuziehen.

## Varianten & Optimierungen

- **Top-Down-Memoisation:** Viele empfinden den rekursiven Ansatz `is_match(i, j)` als intuitiver, da sich die Verzweigung (Verwendung von `*` vs. Ignorieren von `*`) visuell perfekt auf rekursive Aufrufe abbilden lässt und man die Schleife für den Basisfall „leere Zeichenkette“ vermeidet.
- **NFA (nichtdeterministischer endlicher Automat):** Der mathematisch reine Weg, dies in der Industrie zu lösen (wie das `re`-Modul in Python oder `grep` unter Linux)) besteht darin, das Muster `p` in einen Zustandsmaschinengraphen (NFA) zu kompilieren und diesen Graphen anschließend mit der Zeichenkette `s` zu durchlaufen. Damit lassen sich weitaus komplexere Regex-Funktionen ohne DP-Arrays verarbeiten!

## Praktische Anwendungen

- **Compiler & Lexer:** Die Grundlage für die Tokenisierung von Quellcode-Zeichenketten in diskrete grammatikalische Symbole auf Basis von Regex-Syntaxregeln.

## Verwandte Algorithmen in cOde(n)

- **[dp_09 – Wildcard-Abgleich](dp_09_wildcard-matching.md)** — Die einfachere Variante, bei der `*` bedingungslos auf jede beliebige Sequenz passt, anstatt sich an das vorangehende Zeichen zu binden.

---

*Diese Dokumentation ist ein Originalbeitrag für cOde(n),
der sich an der kanonischen Struktur orientiert, die von Referenzseiten
zum Thema Wettbewerbsprogrammierung verwendet wird. Den kanonischen
Enzyklopädieeintrag finden Sie unter dem Wikipedia-Link oben auf der Seite.
Quell-Repository:
<https://github.com/dawei7/code_n>.*
