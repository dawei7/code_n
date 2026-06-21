# Formale mathematische Spezifikation: Trie Insert und Search

## 1. Definitionen und Notation

Sei $\Sigma$ ein endliches Alphabet (z. B. $\Sigma = \{a, b, \dots, z\}$). Ein Trie ist ein gewurzelter Baum $T = (V, E)$, der über $\Sigma$ definiert ist, wobei jeder Knoten $v \in V$ ein Präfix eines oder mehrerer Strings in einem Dictionary $D \subset \Sigma^*$ repräsentiert.

- **Knoten ($V$):** Jeder Knoten $v \in V$ ist ein Tupel $(C_v, \omega_v)$, wobei:
    - $C_v: \Sigma \to V \cup \{\bot\}$ eine partielle Abbildung von Zeichen auf Kindknoten ist.
    - $\omega_v \in \{0, 1\}$ ein boolescher Indikator ist, wobei $\omega_v = 1$ genau dann gilt, wenn der Pfad von der Wurzel zu $v$ einem String $s \in D$ entspricht.
- **Wurzel ($r$):** Der eindeutige Knoten $r \in V$, der den leeren String $\epsilon$ repräsentiert.
- **Zustandsraum ($\mathcal{S}$):** Die Menge aller möglichen Tries $T$, die aus einer Menge von Strings $D$ konstruiert werden können.
- **Operationen:**
    - `insert(s)`: Eine Transformation $T \to T'$, sodass $D' = D \cup \{s\}$.
    - `search(s)`: Ein Prädikat $P(s, T) \to \{0, 1\}$, definiert als $P(s, T) = 1 \iff s \in D$.
    - `startsWith(p)`: Ein Prädikat $Q(p, T) \to \{0, 1\}$, definiert als $Q(p, T) = 1 \iff \exists s \in D$, sodass $p$ ein Präfix von $s$ ist.

## 2. Algebraische Charakterisierung

Sei $s = c_1 c_2 \dots c_m$ ein String der Länge $m$. Wir definieren die Traversierungsfunktion $\tau: V \times \Sigma^* \to V \cup \{\bot\}$ rekursiv:

1. $\tau(v, \epsilon) = v$
2. $\tau(v, c_1 \dots c_m) = \begin{cases} \tau(C_v(c_1), c_2 \dots c_m) & \text{wenn } C_v(c_1) \neq \bot \\ \bot & \text{wenn } C_v(c_1) = \bot \end{cases}$

### Korrektheitsinvarianten
Die Operationen unterliegen den folgenden logischen Bedingungen:

- **Insertion:** Nach `insert(s)` erfüllt der resultierende Trie $T'$ die Bedingung:
  $\forall s' \in D \cup \{s\}, \tau(r, s') = v \implies \omega_v = 1$.
- **Search:** Das Prädikat `search(s)` ist definiert als:
  $$\text{search}(s) = \begin{cases} \omega_{\tau(r, s)} & \text{wenn } \tau(r, s) \neq \bot \\ 0 & \text{wenn } \tau(r, s) = \bot \end{cases}$$
- **Präfix-Suche:** Das Prädikat `startsWith(p)` ist definiert als:
  $$\text{startsWith}(p) = \begin{cases} 1 & \text{wenn } \tau(r, p) \neq \bot \\ 0 & \text{wenn } \tau(r, p) = \bot \end{cases}$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Sei $m = |s|$ die Länge des Eingabestrings. 

Für jede Operation (`insert`, `search`, `startsWith`) führt der Algorithmus eine Sequenz von Übergängen $\tau(v, c_i)$ aus. Jeder Übergang beinhaltet ein Lookup in der Abbildung $C_v$. Unter der Annahme, dass $C_v$ als Hash Map oder Array fester Größe implementiert ist, beträgt die Lookup-Zeit $O(1)$.
Die Gesamtzeit $T(m)$ ist die Summe des Aufwands über die Länge des Strings:
$$T(m) = \sum_{i=1}^{m} O(1) = O(m)$$
Somit ist die Zeitkomplexität linear in Bezug auf die Länge des Eingabestrings und unabhängig von der Gesamtzahl der im Trie gespeicherten Strings $N$.

### Platzkomplexität
- **Hilfsplatzkomplexität:** Der Algorithmus verwendet $O(1)$ zusätzlichen Platz für Pointer und Schleifenvariablen während der Traversierung.
- **Gesamtplatzkomplexität:** Im schlechtesten Fall, in dem keine zwei Strings ein Präfix teilen, erfordert jedes Zeichen jedes eingefügten Strings $s_i$ die Erstellung eines neuen Knotens. Für eine Menge von Strings $D = \{s_1, s_2, \dots, s_n\}$ beträgt die Gesamtplatzkomplexität:
  $$S = O\left(\sum_{i=1}^{n} |s_i|\right)$$
  Für eine einzelne Insertion der Länge $m$ beträgt die inkrementelle Platzkomplexität $O(m)$. Im Kontext der Trie-Struktur ist dies optimal, da es die minimale Anzahl an Knoten darstellt, die erforderlich ist, um die Menge $D$ als Präfixbaum zu repräsentieren.