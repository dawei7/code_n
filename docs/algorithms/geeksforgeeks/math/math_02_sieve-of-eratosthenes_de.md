# Sieb des Eratosthenes

| | |
|---|---|
| **ID** | `math_02` |
| **Kategorie** | math |
| **Komplexität (erforderlich)** | $O(N log(log N)$) Zeit, $O(N)$ Platz |
| **Schwierigkeit** | 3/10 |
| **Relevanz für Vorstellungsgespräche** | 8/10 |
| **LeetCode-Äquivalent** | [Count Primes](https://leetcode.com/problems/count-primes/) |

## Problemstellung

Gegeben sei eine Ganzzahl `N`. Finde alle Primzahlen, die echt kleiner oder gleich `N` sind.
Eine Primzahl ist eine natürliche Zahl, die echt größer als 1 ist und nicht durch die Multiplikation zweier kleinerer natürlicher Zahlen gebildet werden kann.

**Eingabe:** Eine Ganzzahl `N`.
**Ausgabe:** Eine Liste aller Primzahlen \le N.

## Wann man es verwendet

- Wenn man schnell eine Lookup-Tabelle von Primzahlen vorberechnen muss, um mehrere Anfragen in $O(1)$ Zeit zu verarbeiten.
- Die standardmäßige Brute-Force-Prüfung mit $O(\sqrt{N})$ für jede Zahl benötigt $O(N \sqrt{N})$ Zeit. Das Sieb erledigt dieselbe Aufgabe für das gesamte Array in nahezu linearer Zeit!

## Ansatz

**1. Die Strategie des Durchstreichens:**
Anstatt mathematisch zu prüfen, ob eine bestimmte Zahl X eine Primzahl ist, arbeiten wir rückwärts!
Wir wissen, dass `2` eine Primzahl ist. Daher ist jedes Vielfache von `2` (`4, 6, 8, 10...`) mathematisch garantiert KEINE Primzahl!
Wir können einfach ein Array von Zahlen durchgehen und alle Vielfachen von 2 durchstreichen.
Dann gehen wir zur nächsten nicht durchgestrichenen Zahl (`3`). Diese muss eine Primzahl sein! Wir streichen alle Vielfachen von `3` (`6, 9, 12...`) durch.
Wir gehen zur nächsten nicht durchgestrichenen Zahl (`5`, da `4` bereits durch `2` durchgestrichen wurde!). Wir streichen alle ihre Vielfachen durch.

**2. Die Optimierung (\sqrt{N}-Grenze):**
Müssen wir bis N weiter Vielfache durchstreichen?
Nein! Wenn N = 100 ist, ist die Quadratwurzel 10.
Wenn wir die Zahl `11` erreichen, wäre ihr erstes Vielfaches, das noch nicht durch eine kleinere Primzahl durchgestrichen wurde, 11 x 11 = 121. Aber 121 ist größer als 100!
Daher müssen wir nur die Vielfachen für Primzahlen bis \lfloor\sqrt{N}\rfloor durchstreichen. Jede Zahl, die danach im gesamten Array nicht durchgestrichen ist, ist garantiert eine Primzahl!

**3. Der Algorithmus:**
1. Erstelle ein Boolean-Array `is_prime` der Größe N+1, initialisiert mit `True`.
2. Setze `is_prime[0] = False` und `is_prime[1] = False`.
3. Iteriere `p` von `2` bis \sqrt{N}.
4. Wenn `is_prime[p]` den Wert `True` hat:
   - Es ist eine Primzahl! Streiche alle ihre Vielfachen durch.
   - Starte eine verschachtelte Schleife `i` bei p x p (da alle kleineren Vielfachen wie p x 2 oder p x 3 bereits durch 2 und 3 durchgestrichen wurden!).
   - Erhöhe `i` um p bis N. Setze `is_prime[i] = False`.
5. Gib nach der Schleife die Indizes des Arrays zurück, die noch `True` sind.

## Algorithmus

<details>
<summary>Algorithmus anzeigen</summary>

```python
"""Optimal solution for math_02: Sieve of Eratosthenes.

Mark every multiple of each prime as composite. The remaining
unmarked numbers are the primes. O(n log log n) time.
"""


def solve(n):
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]
```

</details>

## Durchlauf

`N = 20`. `limit = floor(sqrt(20)) = 4`.
Initiales Array: `[F, F, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T]`

1. `p = 2`:
   - `is_prime[2]` ist True.
   - Starte Schleife bei `2 * 2 = 4`. Schrittweite 2.
   - Streiche `4, 6, 8, 10, 12, 14, 16, 18, 20`.
2. `p = 3`:
   - `is_prime[3]` ist True.
   - Starte Schleife bei `3 * 3 = 9`. Schrittweite 3.
   - Streiche `9`. (`12` ist bereits durchgestrichen). Streiche `15`. (`18` ist bereits durchgestrichen).
3. `p = 4`:
   - `is_prime[4]` ist False! (Durch 2 durchgestrichen). Überspringen!
4. Schleife endet (da `p > 4`).

Verbleibende Trues: `2, 3, 5, 7, 11, 13, 17, 19`. ✓

## Komplexität

| | Zeit | Platz |
|---|---|---|
| **Bestfall** | $O(N \log(\log N)$) | $O(N)$ |
| **Durchschnittlicher Fall** | $O(N \log(\log N)$) | $O(N)$ |
| **Schlechtester Fall** | $O(N \log(\log N)$) | $O(N)$ |

Die äußere Schleife läuft \sqrt{N} mal. Die innere Schleife läuft \frac{N}{2} mal für 2, \frac{N}{3} mal für 3, \frac{N}{5} mal für 5, usw.
Die Gesamtzahl der Ausführungen der inneren Schleife ist exakt N x (\frac{1}{2} + \frac{1}{3} + \frac{1}{5} + \frac{1}{7} + ...).
Dies ist die harmonische Reihe der Primzahlen, die mathematisch durch $O(log(log N)$) begrenzt ist.
Daher ist die gesamte Zeitkomplexität $O(N log(log N)$). Dies ist so unglaublich nah an der linearen Zeit $O(N)$, dass für N=1.000.000 gilt: log(log(10^6)) ~= 2.6.
Die Platzkomplexität beträgt strikt $O(N)$ für das Boolean-Array.

## Varianten & Optimierungen

- **Segmentiertes Sieb:** Wenn N riesig ist (z. B. 10^9), benötigt ein Array von 10^9 Booleans 1 Gigabyte RAM und verursacht massive CPU-Cache-Misses. Das segmentierte Sieb berechnet zuerst die Primzahlen bis \sqrt{N} und verarbeitet dann den verbleibenden Bereich in kleinen, cache-freundlichen Blöcken der Größe 10^5, wodurch der Speicherbedarf drastisch auf $O(\sqrt{N})$ reduziert wird.
- **Sieb des kleinsten Primfaktors (SPF):** Anstatt `True/False` zu speichern, speichere den ganzzahligen Wert der Primzahl, die die Zahl durchgestrichen hat! `spf[15] = 3`. Dieses modifizierte Sieb erlaubt es, jede Zahl im Array in $O(\log N)$ Zeit mathematisch in Primfaktoren zu zerlegen, indem man einfach den Pointern bis zur 1 folgt!

## Anwendungen in der Praxis

- **Kryptographie-Generierung:** Generierung des Kandidatenpools für riesige Primzahlen, die getestet und als geheime Schlüssel P und Q in RSA-Verschlüsselungsalgorithmen verwendet werden.

## Verwandte Algorithmen in cOde(n)

- **[math_09 - Miller-Rabin-Primzahltest](math_09_miller-rabin-primality-test.md)** — Der alternative Algorithmus, der verwendet wird, wenn man nur prüfen muss, ob eine einzelne RIESIGE Zahl eine Primzahl ist (z. B. 10^{100}), wobei das Erstellen eines Arrays der Größe N physisch unmöglich ist.

---

*Diese Dokumentation ist ein Originalinhalt, der für cOde(n) geschrieben wurde und sich an der kanonischen Struktur orientiert, die von Referenzseiten für kompetitives Programmieren verwendet wird. Für den kanonischen Enzyklopädie-Eintrag folge dem Wikipedia-Link am Seitenanfang. Quell-Repository: <https://github.com/dawei7/code_n>.*