# Formale mathematische Spezifikation: Group Anagrams

## 1. Definitionen und Notation

Sei $\Sigma = \{'a', 'b', \dots, 'z'\}$ das Alphabet der englischen Kleinbuchstaben, wobei $|\Sigma| = 26$ gilt. Sei $\Sigma^*$ die Menge aller endlichen Strings über $\Sigma$.

*   **Eingabe:** Eine endliche Sequenz von Strings $S = (s_1, s_2, \dots, s_N)$, wobei jeder String $s_i \in \Sigma^*$ und $|s_i| \le K$ erfüllt.
*   **Äquivalenzrelation für Anagramme:** Wir definieren eine Äquivalenzrelation $\sim$ auf $\Sigma^*$. Zwei Strings $s_a, s_b$ sind Anagramme, notiert als $s_a \sim s_b$, genau dann, wenn sie Permutationen voneinander sind. Formal sei $\phi: \Sigma^* \to \mathbb{N}_0^{26}$ eine Häufigkeitsabbildung, sodass $\phi(s) = (c_a, c_b, \dots, c_z)$, wobei $c_j$ die Anzahl des Zeichens $j \in \Sigma$ im String $s$ ist. Dann gilt:
    $$s_a \sim s_b \iff \phi(s_a) = \phi(s_b)$$
*   **Ausgabe:** Eine Partition von $S$ in Äquivalenzklassen $\{E_1, E_2, \dots, E_m\}$, sodass für jedes $E_j$ gilt: $\forall s_x, s_y \in E_j, s_x \sim s_y$, und für jedes $E_i \neq E_j$ gilt: $\forall s_x \in E_i, s_y \in E_j, s_x \not\sim s_y$.
*   **Zustandsraum:** Sei $\mathcal{H}$ eine Hash Map (assoziatives Array), die die Domäne $\mathcal{D} = \mathbb{N}_0^{26}$ auf die Kodomäne $\mathcal{R} = \mathcal{P}(\Sigma^*)$ abbildet, wobei $\mathcal{P}$ die Potenzmenge bezeichnet.

## 2. Algebraische Charakterisierung

Der Algorithmus basiert auf der Existenz eines kanonischen Repräsentanten für jede Äquivalenzklasse unter $\sim$.

**Die Invariante:**
Sei $H_i$ der Zustand der Hash Map nach der Verarbeitung der ersten $i$ Strings. Die Invariante lautet:
$$\forall \text{ key } \kappa \in \text{dom}(H_i), H_i(\kappa) = \{s \in \{s_1, \dots, s_i\} \mid \phi(s) = \kappa\}$$

**Korrektheit via Fundamentalsatz der Arithmetik (Variante):**
Während der Häufigkeitsvektor $\phi(s)$ der standardmäßige kanonische Schlüssel ist, kann man eine Abbildung $\psi: \Sigma^* \to \mathbb{Z}^+$ unter Verwendung der ersten 26 Primzahlen $P = \{p_1, p_2, \dots, p_{26}\}$ definieren:
$$\psi(s) = \prod_{j=1}^{26} p_j^{c_j}$$
Nach dem Fundamentalsatz der Arithmetik ist die Primfaktorzerlegung von $\psi(s)$ eindeutig. Somit gilt $\psi(s_a) = \psi(s_b) \iff \phi(s_a) = \phi(s_b)$. Dies bestätigt, dass die Gruppierung mathematisch fundiert ist, vorausgesetzt, das Produkt überschreitet nicht die Wortbreite der Maschine (Überlauf).

**Übergang:**
Für jeden String $s_{i+1}$ lautet die Aktualisierungsregel:
$$H_{i+1} = H_i \cup \{ (\phi(s_{i+1}), H_i(\phi(s_{i+1})) \cup \{s_{i+1}\}) \}$$
wobei die Vereinigung als Einfüge- oder Aktualisierungsoperation in der Hash Map definiert ist.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Der Algorithmus verarbeitet $N$ Strings. Für jeden String $s_i$ der Länge $k_i \le K$:
1.  **Häufigkeitsabbildung:** Die Berechnung von $\phi(s_i)$ erfordert einen einfachen Durchlauf durch den String, was $O(k_i)$ Operationen ergibt.
2.  **Hash Map Zugriff:** Das Einfügen oder Aktualisieren der Map beinhaltet die Berechnung eines Hash-Wertes für das 26-Tupel. Da die Tupelgröße konstant ist ($|\Sigma| = 26$), sind die Hash-Berechnung und das Einfügen in die Map im Durchschnitt $O(1)$.

Die gesamte Zeitkomplexität $T(N, K)$ ergibt sich aus der Summe:
$$T(N, K) = \sum_{i=1}^{N} O(k_i) + O(N) \approx O\left(\sum_{i=1}^{N} K\right) = O(N \cdot K)$$
Somit ist der Algorithmus linear in Bezug auf die Gesamtzahl der Zeichen in der Eingabe.

### Platzkomplexität
Die Platzkomplexität $S(N, K)$ wird durch die Speicherung der Strings und der Hash Map bestimmt:
1.  **Hash Map Speicher:** Wir speichern jeden der $N$ Strings genau einmal in der Hash Map. Die Gesamtzahl der gespeicherten Zeichen beträgt $\sum_{i=1}^N k_i \le N \cdot K$.
2.  **Zusätzlicher Speicher:** Die Schlüssel der Hash Map (Tupel der Größe 26) belegen $O(N \cdot 26) = O(N)$ Speicherplatz.

Summiert man diese Komponenten:
$$S(N, K) = O(N \cdot K + N) = O(N \cdot K)$$
Die Platzkomplexität beträgt $O(N \cdot K)$, was optimal ist, da sie proportional zur Größe der Eingabedaten ist.