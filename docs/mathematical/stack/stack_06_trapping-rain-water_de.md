# Formale mathematische Spezifikation: Trapping Rain Water

## 1. Definitionen und Notation

Sei $H = [h_0, h_1, \dots, h_{n-1}]$ eine Folge nicht-negativer ganzer Zahlen, die das Höhenprofil (Elevation Map) darstellt, wobei $h_i \in \mathbb{N}_0$ für alle $i \in \{0, 1, \dots, n-1\}$ gilt. Die Breite jedes Balkens ist als Einheitsintervall definiert.

Wir definieren die folgenden Mengen und Variablen:
*   **Indexmenge:** $I = \{0, 1, \dots, n-1\}$.
*   **Stack:** Eine Folge $S = (s_1, s_2, \dots, s_k)$, wobei $s_j \in I$ die Indizes der Balken im Stack repräsentiert. Der Stack erhält die Monotonieeigenschaft $h_{s_1} \geq h_{s_2} \geq \dots \geq h_{s_k}$ aufrecht.
*   **Wasservolumen:** Das gesamte angesammelte Wasser $W$ ist ein skalarer Wert, der durch die Summe des in jeder horizontalen Schicht oder jedem „Tal“ des Höhenprofils angesammelten Wassers definiert ist.
*   **Zustandsraum:** Der Zustand in der Iteration $i$ ist durch das Tupel $(S_i, W_i)$ definiert, wobei $S_i$ die Stack-Konfiguration und $W_i$ das kumulierte Volumen des angesammelten Wassers nach der Verarbeitung des Index $i$ ist.

## 2. Algebraische Charakterisierung

Der Algorithmus berechnet das gesamte angesammelte Wasser, indem er die Fläche in horizontale Rechtecke zerlegt. Für jeden Index $i$ wird ein Tal identifiziert, wenn $h_i > h_{s_k}$ gilt (wobei $s_k$ das oberste Element des Stacks ist).

Sei $t$ der vom Stack mittels `pop` entfernte Index ($t = s_k$), der den Boden des Tals darstellt. Sei $l$ das neue oberste Element des Stacks ($l = s_{k-1}$), das die linke Grenze darstellt. Die rechte Grenze ist der aktuelle Index $i$.

Das Wasservolumen $\Delta W$, das durch den aktuellen Balken $i$ relativ zum entfernten Boden $t$ angesammelt wird, ist gegeben durch:
$$\Delta W = (\min(h_i, h_l) - h_t) \times (i - l - 1)$$

Das Gesamtvolumen $W$ ist die Summe über alle derartigen Ereignisse:
$$W = \sum_{i=0}^{n-1} \sum_{t \in \text{Popped}_i} (\min(h_i, h_{l_i}) - h_t) \cdot (i - l_i - 1)$$
wobei $\text{Popped}_i$ die Menge der Indizes ist, die im Schritt $i$ vom Stack mittels `pop` entfernt wurden, und $l_i$ der Index ist, der nach dem `pop`-Vorgang an der Spitze des Stacks verbleibt.

**Schleifeninvariante:**
Zu Beginn jeder Iteration $i$ enthält der Stack $S$ Indizes $s_1, s_2, \dots, s_k$, sodass $h_{s_1} \geq h_{s_2} \geq \dots \geq h_{s_k}$ gilt. Die Variable $W$ speichert korrekt das gesamte Wasservolumen, das von allen Balken $h_0, \dots, h_{i-1}$ angesammelt wurde, die durch mindestens einen Balken zu ihrer Linken und einen zu ihrer Rechten begrenzt sind.

## 3. Komplexitätsanalyse

### Zeitkomplexität
Die Zeitkomplexität beträgt $O(n)$. 
**Beweis:** 
Betrachten wir die auf dem Stack ausgeführten Operationen. Jeder Index $j \in I$ wird genau einmal auf den Stack mittels `push` gelegt. Ein Index $j$ wird höchstens einmal vom Stack mittels `pop` entfernt. 
Sei $T(n)$ die Gesamtzahl der Operationen. Die Schleife läuft $n$-mal durch. Innerhalb der Schleife prüft die `while`-Bedingung den Stack, und die `pop`-Operation wird ausgeführt. Da jedes Element genau einmal mittels `push` hinzugefügt und höchstens einmal mittels `pop` entfernt wird, ist die Gesamtzahl der `pop`-Operationen über die gesamte Ausführung hinweg durch $n$ beschränkt. Somit ergibt sich der Gesamtaufwand zu:
$$T(n) = \sum_{i=0}^{n-1} (1 + \text{pops}_i) = n + \sum_{i=0}^{n-1} \text{pops}_i = n + n = 2n$$
Da $2n \in O(n)$ gilt, ist der Algorithmus linear in der Zeit.

### Platzkomplexität
Die Platzkomplexität beträgt $O(n)$.
**Beweis:**
Der zusätzliche Speicherbedarf (Auxiliary Space) wird durch den Stack $S$ dominiert. Im Schlechtesten Fall (Worst-Case) ist das Eingabe-Array $H$ streng monoton fallend (z. B. $h_i > h_{i+1}$ für alle $i$). In diesem Fall ist die `while`-Bedingung $h_i > h_{s_k}$ niemals erfüllt, und jeder Index $i \in I$ wird auf den Stack mittels `push` gelegt, ohne dass ein Element mittels `pop` entfernt wird. Die Stack-Größe $|S|$ erreicht $n$. Daher beträgt die Platzkomplexität $O(n)$.