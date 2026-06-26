# Formale mathematische Spezifikation: Circular Queue (Array-basiert)

## 1. Definitionen und Notation

Sei $K \in \mathbb{Z}^+$ die feste Kapazität der Circular Queue. Wir definieren den Zustand der Queue als Tupel $\mathcal{S} = (A, h, t, n)$, wobei:

*   $A = [a_0, a_1, \dots, a_{K-1}]$ eine Sequenz von Elementen ist, für die $a_i \in \mathcal{D} \cup \{\perp\}$ gilt, wobei $\mathcal{D}$ die Domäne der Datenelemente ist. $\perp$ bezeichnet einen nicht initialisierten oder logisch leeren Platz.
*   $h \in \{0, 1, \dots, K-1\}$ der Index des vordersten Elements (head) ist.
*   $t \in \{0, 1, \dots, K-1\}$ der Index des zuletzt eingefügten Elements (tail) ist.
*   $n \in \{0, 1, \dots, K\}$ die aktuelle Anzahl der in der Queue gespeicherten Elemente ist.

Der Zustandsraum $\mathcal{S}$ ist durch das kartesische Produkt $\mathcal{D}^K \times \mathbb{Z}_K \times \mathbb{Z}_K \times \{0, \dots, K\}$ definiert.

## 2. Algebraische Charakterisierung

Die Circular Queue wird durch die folgenden Übergangsfunktionen und Invarianten bestimmt. Wir definieren den Modulo-Operator als $x \pmod K$.

### Zustandsübergänge
Gegeben eine Operation, entwickelt sich der Zustand $\mathcal{S}_i = (A_i, h_i, t_i, n_i)$ zu $\mathcal{S}_{i+1}$ wie folgt:

1.  **`enQueue(v)`**: Wenn $n_i < K$:
    *   $t_{i+1} = (t_i + 1) \pmod K$
    *   $A_{i+1}[t_{i+1}] = v$
    *   $n_{i+1} = n_i + 1$
    *   $h_{i+1} = h_i$ (wenn $n_i = 0$, $h_{i+1} = t_{i+1}$)

2.  **`deQueue()`**: Wenn $n_i > 0$:
    *   $h_{i+1} = (h_i + 1) \pmod K$
    *   $n_{i+1} = n_i - 1$
    *   $t_{i+1} = t_i$

### Invarianten
Die Korrektheit der Struktur wird durch die folgenden Invarianten gewahrt:
*   **Größenbeschränkung:** $0 \le n \le K$.
*   **Leer-Bedingung:** Die Queue ist genau dann leer, wenn $n = 0$.
*   **Voll-Bedingung:** Die Queue ist genau dann voll, wenn $n = K$.
*   **Tail-Head-Beziehung:** Wenn $n > 0$, steht der Index des tail in folgender Beziehung zum head:
    $t = (h + n - 1) \pmod K$.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Sei $T(op)$ die Zeitkomplexität einer beliebigen Operation $op \in \{\text{enQueue, deQueue, Front, Rear, isEmpty, isFull}\}$.

Jede Operation besteht aus einer konstanten Anzahl arithmetischer Operationen (Addition, Modulo) und Speicherzugriffsoperationen (Array-Indizierung). Speziell gilt für jede Operation:
$$T(op) = \Theta(1)$$
Da der Modulo-Operator $x \pmod K$ in Hardware als bitweise Operation oder als einzelne Divisionsinstruktion implementiert ist, ist die Ausführungszeit unabhängig von der Kapazität $K$ oder der Anzahl der Elemente $n$. Somit ist die amortisierte und die Zeitkomplexität im Schlechtesten Fall $O(1)$.

### Platzkomplexität
Die Platzkomplexität wird durch den Speicherbedarf für das Array $A$ und die Hilfsvariablen $(h, t, n)$ bestimmt.

*   **Zusätzlicher Speicher:** Die Variablen $h, t, n$ benötigen $O(1)$ Platz.
*   **Gesamtspeicher:** Das Array $A$ benötigt $K$ Plätze der Größe $|\mathcal{D}|$. 
$$S(K) = \text{sizeof}(A) + \text{sizeof}(h, t, n) = K \cdot |\mathcal{D}| + O(1)$$
Asymptotisch ist die Platzkomplexität $O(K)$. Dies ist optimal für einen Puffer mit fester Kapazität, da es die theoretische Untergrenze für die Speicherung von $K$ Elementen erreicht.