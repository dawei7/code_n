# String to Integer (atoi)

| | |
|---|---|
| **ID** | `string_12` |
| **Kategorie** | strings |
| **Komplexität (erforderlich)** | $O(N)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/) |

## Problemstellung

Implementieren Sie die Funktion `myAtoi(string s)`, die einen String in eine 32-Bit-Ganzzahl mit Vorzeichen umwandelt (ähnlich der `atoi`-Funktion in C/C++).
Der Algorithmus muss folgende strikte Regeln befolgen:
1. **Whitespace:** Ignorieren Sie führende Leerzeichen (`" "`).
2. **Vorzeichen:** Bestimmen Sie das Vorzeichen, indem Sie prüfen, ob das nächste Zeichen `'-'` oder `'+'` ist. Nehmen Sie `+` an, falls keines von beiden vorhanden ist.
3. **Konvertierung:** Lesen Sie die nächsten Zeichen ein, bis ein Nicht-Ziffer-Zeichen oder das Ende des Inputs erreicht ist. Der Rest des Strings wird ignoriert. Konvertieren Sie diese Ziffern in eine Ganzzahl.
4. **Rundung:** Falls die Ganzzahl außerhalb des Bereichs für 32-Bit-Ganzzahlen mit Vorzeichen `[-2^31, 2^31 - 1]` liegt, kappen Sie die Zahl so, dass sie innerhalb dieses Bereichs bleibt.

**Input:** Ein String `s`.
**Output:** Eine gekappte 32-Bit-Ganzzahl.

## Wann man es verwendet

- Um Benutzereingaben (die immer als String vorliegen) sicher in eine mathematische Zahl umzuwandeln und dabei alle Randfälle sauber zu behandeln, ohne eine Exception auszulösen.
- Eine der berüchtigtsten Fragen in Vorstellungsgesprächen, um die Liebe zum Detail und den Umgang mit Randfällen zu testen.

## Ansatz

**1. Das deterministische Parsing in vier Schritten:**
Dieses Problem erfordert keinen ausgeklügelten Algorithmus, sondern die disziplinierte Ausführung einer Zustandsmaschine (State Machine).
- **Schritt 1: Trimmen.** Entfernen Sie führende Leerzeichen.
- **Schritt 2: Vorzeichen.** Prüfen Sie den Index 0 auf `+` oder `-`. Falls gefunden, speichern Sie das Vorzeichen und bewegen Sie den Pointer weiter.
- **Schritt 3: Ziffern.** Iterieren Sie durch den String. Solange das Zeichen eine Ziffer (`'0'`-`'9'`) ist, multiplizieren Sie die laufende Summe mit 10 und addieren die neue Ziffer. Wenn Sie auf ein Nicht-Ziffer-Zeichen (wie einen Buchstaben oder ein Leerzeichen) stoßen, halten Sie sofort AN.
- **Schritt 4: Überlauf.** Falls die laufende Summe das Maximum einer 32-Bit-Ganzzahl überschreitet, kappen Sie den Wert und geben ihn sofort zurück.

**2. Die mathematische Ziffernkonvertierung:**
Wie wandeln wir das Zeichen `'7'` in die Ganzzahl `7` um, ohne eine eingebaute `int()`-Funktion zu verwenden?
Zeichen sind im Hintergrund lediglich ASCII-Ganzzahlen!
`'0'` entspricht ASCII 48. `'7'` entspricht ASCII 55.
Daher ist der Ganzzahlwert einfach `ASCII('7') - ASCII('0') = 55 - 48 = 7`!

**3. Umgang mit Überläufen in streng typisierten Sprachen:**
In Python haben Ganzzahlen eine beliebige Präzision, daher kann man die Zahl einfach wachsen lassen und am Ende kappen.
In C++ oder Java würde `total * 10 + digit` den Speicherbereich physisch zum Absturz bringen (Overflow Exception), BEVOR Sie die Chance haben, den Wert zu kappen!
Um dies zu beheben, prüfen wir vor der Multiplikation mit 10: `if total > MAX_INT / 10`. Falls dies zutrifft, führt die Multiplikation garantiert zu einem Überlauf! Kappen Sie den Wert und geben Sie ihn sofort zurück!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for string_12: String to Integer (atoi).

Parse a string as a 32-bit signed integer. Skip leading
whitespace, handle an optional +/- sign, read digits
until a non-digit. Clamp to the int32 range.
"""


def solve(s, n):
    if n == 0:
        return 0
    i = 0
    while i < n and s[i] == " ":
        i += 1
    if i == n:
        return 0
    sign = 1
    if s[i] == "+":
        i += 1
    elif s[i] == "-":
        sign = -1
        i += 1
    result = 0
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31
    while i < n and s[i].isdigit():
        digit = int(s[i])
        new_result = result * 10 + digit
        if sign == 1 and new_result > INT_MAX:
            return INT_MAX
        if sign == -1 and -new_result < INT_MIN:
            return INT_MIN
        result = new_result
        i += 1
    return sign * result
```

</details>

## Durchlauf

`s = "   -42"`
1. **Trimmen:** `i` rückt über drei Leerzeichen hinaus auf Index `3`.
2. **Vorzeichen:** `s[3] == '-'`. `sign = -1`. `i` rückt auf `4`.
3. **Ziffern:**
   - `i = 4`: `s[4] = '4'`. `digit = 4`. `result = 0 * 10 + 4 = 4`.
   - `i = 5`: `s[5] = '2'`. `digit = 2`. `result = 4 * 10 + 2 = 42`.
4. Ende des Strings. Rückgabe `sign * result = -42`. ✓

`s = "4193 with words"`
1. **Trimmen:** Keine führenden Leerzeichen. `i = 0`.
2. **Vorzeichen:** Kein Vorzeichen. `sign = 1`.
3. **Ziffern:**
   - `i = 0`: `'4'`. `result = 4`.
   - `i = 1`: `'1'`. `result = 41`.
   - `i = 2`: `'9'`. `result = 419`.
   - `i = 3`: `'3'`. `result = 4193`.
   - `i = 4`: `' '`. `s[i].isdigit()` ist False! Die Schleife bricht sofort ab.
4. Rückgabe `4193`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N)$ | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N)$ | $O(1)$ |

Wir iterieren genau einmal von links nach rechts durch den String.
Die Zeitkomplexität ist strikt $O(N)$, wobei N die Länge des Strings ist.
Die Platzkomplexität ist strikt $O(1)$ (konstanter Platz), da wir nur wenige Ganzzahlvariablen (`i`, `sign`, `result`) speichern.

## Varianten & Optimierungen

- **Valid Number / IsNumeric (`string_04`?):** Eine deutlich schwierigere Variante, bei der man strikt validieren muss, ob ein String mathematisch irgendeine gültige Zahl darstellt (einschließlich Dezimalzahlen, wissenschaftlicher `e`-Notation und führender Nullen), unter Verwendung eines komplexen deterministischen endlichen Automaten (DFA).

## Anwendungen in der Praxis

- **Standardbibliotheken:** Dies ist buchstäblich die exakte Implementierung der `atoi()`-Funktion aus C's `<stdlib.h>`, welche das fundamentale Grundgerüst für das Parsen von benutzerdefinierten Konfigurationen, JSON-Zahlen und HTTP-Headern im gesamten Internet bildet.

## Verwandte Algorithmen in cOde(n)

- **[string_12 - String to Integer (atoi)](#)** — Moment, das ist dieser hier!
- **[math_05 - Reverse Integer](../math/math_05_reverse-integer.md)** — Das Schwesterproblem, das die exakt gleiche Logik für die Überlaufprüfung `result > MAX_INT // 10` erfordert, aber den Modulo-Operator `% 10` verwendet, um Ziffern zu entfernen, anstatt sie hinzuzufügen!

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*