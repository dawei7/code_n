# Longest Common Prefix

| | |
|---|---|
| **ID** | `string_11` |
| **Kategorie** | strings |
| **Komplexität (erforderlich)** | $O(N \times M)$ Zeit, $O(1)$ Platz |
| **Schwierigkeit** | 2/10 |
| **Relevanz für Vorstellungsgespräche** | 9/10 |
| **LeetCode-Äquivalent** | [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/) |

## Problemstellung

Schreiben Sie eine Funktion, um den längsten gemeinsamen Präfix-String innerhalb eines Arrays von Strings zu finden.
Falls kein gemeinsamer Präfix existiert, geben Sie einen leeren String `""` zurück.

**Eingabe:** Ein Array von Strings `strs`.
**Ausgabe:** Ein String, der den längsten gemeinsamen Präfix repräsentiert.

**Beispiel 1:**
`strs = ["flower", "flow", "flight"]`
Ausgabe: `"fl"`.

**Beispiel 2:**
`strs = ["dog", "racecar", "car"]`
Ausgabe: `""`. (Es gibt keinen gemeinsamen Präfix unter den Eingabe-Strings).

## Anwendung

- Zum Finden gemeinsamer Verzeichnispfade, Namespace-Präfixe oder Grenzen für die Autovervollständigung.
- Eine sehr beliebte, direkte Frage in Vorstellungsgesprächen, um Ihre Fähigkeit zu testen, Index-out-of-bounds-Fehler zu vermeiden.

## Ansatz

**1. Horizontales Scannen (Der intuitive Weg):**
1. Betrachten Sie den allerersten String im Array als Ihren anfänglichen "Präfix".
2. Iterieren Sie nacheinander durch den Rest der Strings.
3. Vergleichen Sie jeden String mit Ihrem aktuellen "Präfix".
4. Wenn der aktuelle String nicht mit dem Präfix beginnt, kürzen Sie das letzte Zeichen des Präfixes und versuchen Sie es erneut!
5. Wenn der Präfix leer wird (`""`), bedeutet dies, dass absolut kein gemeinsamer Präfix existiert. Geben Sie sofort `""` zurück.
6. Geben Sie den Präfix zurück, nachdem alle Strings überprüft wurden.

**2. Vertikales Scannen (Der optimale Weg):**
Horizontales Scannen kann langsam sein, wenn ein riesiges Array aus sehr langen, identischen Strings vorliegt, der letzte String im Array jedoch nur `"a"` ist. Wir würden Millionen von Zeichen scannen, bevor wir den Präfix schließlich auf `"a"` kürzen.
Stattdessen scannen wir vertikal!
Wir betrachten das 0-te Zeichen aller Strings. Wenn sie übereinstimmen, gehen wir zum 1-ten Zeichen aller Strings über. Wir fahren fort, bis wir eine Nichtübereinstimmung der Zeichen finden oder das Ende eines der Strings erreichen!

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for string_11: Longest Common Substring.

Length of the longest common substring (consecutive, not
subsequence) of s1 and s2. Standard DP: dp[i][j] = length
of the common suffix of s1[..i] and s2[..j]. The answer
is the max over the table.
"""


def solve(s1, s2, n1, n2):
    if n1 == 0 or n2 == 0:
        return 0
    best = 0
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > best:
                    best = dp[i][j]
            else:
                dp[i][j] = 0
    return best
```

</details>

## Durchlauf (Vertikales Scannen)

`strs = ["flower", "flow", "flight"]`.

**`i = 0` (Überprüfung des 0-ten Zeichens):**
- `strs[0][0]` ist `'f'`.
- `strs[1][0]` ist `'f'`. Übereinstimmung.
- `strs[2][0]` ist `'f'`. Übereinstimmung.

**`i = 1` (Überprüfung des 1-ten Zeichens):**
- `strs[0][1]` ist `'l'`.
- `strs[1][1]` ist `'l'`. Übereinstimmung.
- `strs[2][1]` ist `'l'`. Übereinstimmung.

**`i = 2` (Überprüfung des 2-ten Zeichens):**
- `strs[0][2]` ist `'o'`.
- `strs[1][2]` ist `'o'`. Übereinstimmung.
- `strs[2][2]` ist `'i'`. Nichtübereinstimmung! (`'i' != 'o'`).

Geben Sie `strs[0][:2]` zurück, was `"fl"` entspricht. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \times \min(M)$) | $O(1)$ |
| **Durchschnittlicher Fall** | $O(N \times M)$ | $O(1)$ |
| **Schlechtester Fall** | $O(N \times M)$ | $O(1)$ |

Sei N die Anzahl der Strings und M die maximale Länge eines Strings.
Im schlechtesten Fall sind alle Strings identisch. Der Algorithmus vergleicht jedes Zeichen jedes Strings. Die Gesamtzahl der Vergleiche beträgt N x M. Daher ist die Zeitkomplexität $O(N \times M)$ (oder $O(S)$, wobei S die Summe aller Zeichen ist).
Die Platzkomplexität beträgt $O(1)$ zusätzlichen konstanten Speicher, vorausgesetzt, das Substring-Slicing `strs[0][:i]` ist optimiert oder gibt String-Pointer zurück.

## Varianten & Optimierungen

- **Sortierung $O(S log N)$:** Wenn Sie das Array von Strings lexikographisch (alphabetisch) sortieren, müssen Sie nur den *ersten* und den *letzten* String im sortierten Array vergleichen! Der längste gemeinsame Präfix zwischen diesen beiden ist garantiert der längste gemeinsame Präfix für das gesamte Array. Das Sortieren benötigt jedoch $O(S log N)$, was es mathematisch langsamer macht als lineares Scannen.
- **Trie $O(S)$:** Fügen Sie alle Strings in einen Trie ein. Traversieren Sie dann den Trie. Solange ein Knoten genau 1 Kind hat (und nicht das Ende eines Wortes markiert), ist er Teil des gemeinsamen Präfixes!

## Anwendungen in der Praxis

- **Kommandozeilen-Autovervollständigung:** Wenn Sie die `TAB`-Taste in einem Unix-Terminal drücken, berechnet die Shell den längsten gemeinsamen Präfix aller gültigen ausführbaren Dateien, die mit Ihrer aktuellen Eingabe übereinstimmen, um den Rest des Befehls zu vervollständigen!

## Verwandte Algorithmen in cOde(n)

- **[trie_01 - Trie Insert/Search](../trie/trie_01_trie-insert-search.md)** — Die Datenstruktur, die stark für die dynamische Beantwortung von präfixbasierten Anfragen optimiert ist.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) verfasst wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folgen Sie dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*