# Formale mathematische Spezifikation: Zykluserkennung in einer Linked List

## 1. Definitionen und Notation

Sei die Linked List als gerichteter Graph $G = (V, E)$ dargestellt, wobei $V = \{v_0, v_1, \dots, v_{n-1}\}$ die Menge der Knoten und $E \subseteq V \times V$ die Menge der Kanten ist. Da die Struktur eine einfach verkettete Liste ist, hat jeder Knoten $v_i$ einen Ausgangsgrad von höchstens 1. Speziell existiert eine Nachfolgerfunktion $f: V \to V \cup \{\text{null}\}$, sodass $(v_i, v_j) \in E \iff f(v_i) = v_j$.

- **Pfad:** Eine Sequenz von Knoten $(p_0, p_1, \dots, p_k)$, sodass $p_{i+1} = f(p_i)$ für alle $0 \le i < k$ gilt.
- **Zyklus:** Ein Pfad $(p_0, p_1, \dots, p_k)$ ist ein Zyklus, wenn $p_k = p_0$ und $k > 0$ gilt.
- **Zustandsraum:** Sei $\mathcal{S} = V \times V$ der Zustandsraum der zwei Pointer, wobei ein Zustand $s_t = (\sigma_t, \phi_t)$ die Positionen des langsamen Pointers $\sigma$ und des schnellen Pointers $\phi$ zum Zeitschritt $t$ repräsentiert.
- **Übergangsfunktion:** Die Entwicklung der Pointer wird durch die Abbildung $\delta: \mathcal{S} \to \mathcal{S}$ definiert:
  $$\delta(\sigma, \phi) = (f(\sigma), f(f(\phi)))$$
  wobei $f(\text{null}) = \text{null}$ gilt.

## 2. Algebraische Charakterisierung

### Die Zyklusbedingung
Ein Zyklus existiert genau dann, wenn ein $t > 0$ existiert, sodass $\sigma_t = \phi_t$ gilt.

Sei $L$ die Distanz vom Kopf $v_0$ zum ersten Knoten des Zyklus $v_c$, und sei $C$ die Länge des Zyklus. Zum Zeitpunkt $t$ sind die Positionen:
- $\sigma_t = f^t(v_0)$
- $\phi_t = f^{2t}(v_0)$

Wenn ein Zyklus existiert, treten die Pointer für hinreichend große $t$ in den Zyklus ein. Sei $t = L + k$. Die Pointer treffen sich, wenn:
$$L + k \equiv 2(L + k) \pmod C$$
$$L + k \equiv 2L + 2k \pmod C$$
$$k \equiv -(L) \pmod C$$
Dies impliziert $k = mC - L$ für eine ganze Zahl $m$. Somit findet das Treffen bei $t = L + (mC - L) = mC$ statt. Die Distanz vom Kopf zum Treffpunkt ist $mC$, was ein Vielfaches der Zykluslänge ist.

### Der Start des Zyklus
Um den Start des Zyklus zu finden, setzen wir einen Pointer auf $v_0$ zurück und bewegen beide mit Einheitsgeschwindigkeit. Sei der Treffpunkt $v_m$. Die Distanz von $v_0$ nach $v_c$ ist $L$. Die Distanz von $v_m$ nach $v_c$ ist $C - (L \pmod C)$. Indem beide Pointer mit Geschwindigkeit 1 bewegt werden, treffen sie sich nach genau $L$ Schritten bei $v_c$, da:
$$v_0 \xrightarrow{L} v_c \quad \text{und} \quad v_m \xrightarrow{L} v_c$$

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität beträgt $O(N)$, wobei $N = |V|$ ist.
- **Phase 1 (Erkennung):** Der schnelle Pointer $\phi$ tritt in höchstens $L$ Schritten in den Zyklus ein. Sobald er sich darin befindet, vergrößert sich die relative Distanz zwischen $\phi$ und $\sigma$ in jedem Schritt um 1. Da die Zykluslänge $C \le N$ ist, wird der schnelle Pointer den langsamen Pointer in höchstens $C$ Schritten "überrunden". Gesamtschritte $T_1 \le L + C \le N$.
- **Phase 2 (Start finden):** Die Pointer durchlaufen die Distanz $L$ vom Kopf bis zum Zyklusstart. Da $L < N$, gilt $T_2 = L < N$.
- **Gesamtzeit:** $T(N) = T_1 + T_2 = O(N)$.

### Platzkomplexität
Der Algorithmus verwaltet unabhängig von der Eingabegröße $N$ genau zwei Pointer, $\sigma$ und $\phi$.
- Der benötigte zusätzliche Speicherplatz ist $S(N) = \Theta(1)$.
- Da die Eingabe als Referenz auf den Kopf der Liste bereitgestellt wird, beträgt die gesamte Platzkomplexität $O(1)$ über die Speicherung des Eingabegraphen hinaus.