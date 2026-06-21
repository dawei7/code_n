# Regular Expression Matching

| | |
|---|---|
| **ID** | `dp_30` |
| **Kategorie** | dynamic |
| **Komplexität (erforderlich)** | $O(M * N)$ Zeit, $O(M * N)$ Platz |
| **Schwierigkeit** | 9/10 |
| **Relevanz für Vorstellungsgespräche** | 5/10 |
| **LeetCode-Äquivalent** | [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/) |

## Problemstellung

Gegeben sind ein Eingabestring `s` und ein Muster `p`. Implementieren Sie einen Regular Expression Matcher mit Unterstützung für `.` und `*`, wobei gilt:
- `.` entspricht einem beliebigen einzelnen Zeichen.
- `*` entspricht null oder mehr Vorkommen des **vorhergehenden** Elements.
Der Abgleich muss den gesamten Eingabestring abdecken (kein teilweiser Abgleich).

**Eingabe:** Zwei Strings `s` und `p`.
**Ausgabe:** Ein Boolean: `True`, falls `s` auf `p` passt, ansonsten `False`.

## Wann man es verwendet

- Um fortgeschrittene String-DP-Verarbeitung zu demonstrieren, bei der der Zustandsübergang aufgrund von Modifikatoren mit variabler Länge (wie `*`) mehr als einen Schritt ZURÜCK blickt.
- *Hinweis:* Verwechseln Sie dies nicht mit Wildcard Matching (`dp_09`), bei dem `*` für *eine beliebige Sequenz* steht. Hier bedeutet `a*` spezifisch null oder mehr `a`s!

## Ansatz

**1. Definition des Zustands:**
Sei `dp[i][j]` ein Boolean, der angibt, ob das Präfix `s[0...i-1]` auf das Musterpräfix `p[0...j-1]` passt.

**2. Bestimmung der Basisfälle:**
- `dp[0][0] = True`: Ein leerer String passt auf ein leeres Muster.
- `dp[i][0] = False`: Ein nicht-leerer String passt NIEMALS auf ein leeres Muster.
- `dp[0][j]`: Ein leerer String KANN auf ein nicht-leeres Muster passen, aber NUR, wenn das Muster eine Sequenz optionaler Zeichen ist (z. B. `a*b*c*`).
  Damit ein leerer String auf `p[0...j-1]` passt, MUSS das letzte Zeichen `*` sein. Wenn wir dieses `*` und das davorstehende Zeichen ignorieren, muss der Rest des Musters EBENFALLS auf den leeren String passen!
  `dp[0][j] = dp[0][j-2]` (falls `p[j-1] == '*'`).

**3. Bestimmung des Übergangs (Die Rekursionsgleichung):**
Wir vergleichen das aktuelle Zeichen `s[i-1]` mit `p[j-1]`.
- **Fall A (Direkte Übereinstimmung):**
  Wenn `p[j-1]` ein normales Zeichen ist und `p[j-1] == s[i-1]`, oder wenn `p[j-1] == '.'`, liegt eine 1-zu-1-Übereinstimmung vor!
  Die Strings passen zusammen, wenn ihre verbleibenden Präfixe zusammenpassen.
  `dp[i][j] = dp[i-1][j-1]`
- **Fall B (Das knifflige `*`):**
  Wenn `p[j-1] == '*'`, betrachten wir das Zeichen *vor* dem Stern: `p[j-2]`.
  Wir haben zwei verschiedene Möglichkeiten, das `*` gültig zu machen:
  1. **Null Vorkommen (Ignorieren):** Wir verwerfen einfach das `*` und das davorstehende Zeichen.
     `dp[i][j] = dp[i][j-2]`
  2. **Ein oder mehrere Vorkommen (Verwenden):** Wir können es nur verwenden, WENN das vorhergehende Zeichen `p[j-2]` tatsächlich auf `s[i-1]` passt (oder ein `.` ist). Wenn es passt, "konsumieren" wir `s[i-1]`, behalten aber das `*` im Muster aktiv, damit es weitere Zeichen konsumieren kann!
     `dp[i][j] = dp[i-1][j]` (Nur gültig, wenn `p[j-2] == s[i-1]` oder `p[j-2] == '.'`)

  Da beide Möglichkeiten gültig sein können, bilden wir ein logisches `OR`!

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

## Durchlauf

`s = "aab"`, `p = "c*a*b"`. M=3, N=5.
Basisfälle (i=0): `dp[0][0]=T`.
`j=2 ('*')`: `dp[0][2] = dp[0][0] = T` ("c*").
`j=4 ('*')`: `dp[0][4] = dp[0][2] = T` ("c*a*").

1. **i = 1 ('a'):**
   - `j=1 ('c')`: False.
   - `j=2 ('*')`: Null Vorkommen (`dp[1][0]=F`).
   - `j=3 ('a')`: Direkte Übereinstimmung. `dp[1][3] = dp[0][2] = T`.
   - `j=4 ('*')`: Null Vorkommen (`dp[1][2]=F`) ODER Verwenden (`p[j-2]=='a' == s[i-1]`, also `dp[0][4]=T`). `dp[1][4] = T`.
2. **i = 2 ('a'):**
   - `j=4 ('*')`: Null Vorkommen (`dp[2][2]=F`) ODER Verwenden (`p[j-2]=='a' == s[i-1]`, also `dp[1][4]=T`). `dp[2][4] = T`.
3. **i = 3 ('b'):**
   - `j=4 ('*')`: Null Vorkommen (`dp[3][2]=F`). Verwenden schlägt fehl (`'a' != 'b'`). False.
   - `j=5 ('b')`: Direkte Übereinstimmung. `dp[3][5] = dp[2][4] = T`!

Das Ergebnis `dp[3][5]` ist `True`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(M * N)$ | $O(M * N)$ |
| **Durchschnittlicher Fall** | $O(M * N)$ | $O(M * N)$ |
| **Schlechtester Fall** | $O(M * N)$ | $O(M * N)$ |

Die verschachtelten Schleifen werden bedingungslos genau M x N Mal ausgeführt. Die Zeitkomplexität ist strikt $O(M \times N)$.
Die Platzkomplexität beträgt $O(M \times N)$ für die DP-Matrix. Sie kann technisch auf $O(N)$ mit einem 1D-Rolling-Array reduziert werden, aber da `*` einen Rückblick auf `j-2` erfordert, wird die Zustandsverwaltung in einem Vorstellungsgespräch sehr fehleranfällig. Die 2D-Matrix ist aufgrund ihrer Klarheit weitaus vorzuziehen.

## Varianten & Optimierungen

- **Top-Down Memoization:** Viele empfinden den rekursiven Ansatz `is_match(i, j)` als intuitiver, da das Verzweigen (`*` verwenden vs. `*` ignorieren) visuell perfekt auf rekursive Aufrufe abgebildet wird und man die Schleife für den Basisfall des leeren Strings vermeidet.
- **NFA (Nicht-deterministische endliche Automaten):** Der mathematisch saubere Weg, dies in der Industrie zu lösen (wie das `re`-Modul in Python oder `grep` in Linux), besteht darin, das Muster `p` in einen Zustandsautomaten-Graphen (NFA) zu kompilieren und dann den Graphen mit dem String `s` zu durchlaufen. Dies bewältigt weitaus komplexere Regex-Funktionen ohne DP-Arrays!

## Anwendungen in der Praxis

- **Compiler & Lexer:** Die Grundlage für das Tokenisieren von Quellcode-Strings in diskrete grammatikalische Symbole basierend auf RegEx-Syntaxregeln.

## Verwandte Algorithmen in cOde(n)

- **[dp_09 - Wildcard Matching](dp_09_wildcard-matching.md)** — Der einfachere Verwandte, bei dem `*` bedingungslos auf eine beliebige Sequenz passt, anstatt an das vorhergehende Zeichen gebunden zu sein.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitive Programmierung verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*