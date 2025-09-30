# 🏁 Checkers AI  

Projekt implementujący grę **Warcaby (Checkers)** w Pythonie z interfejsem graficznym w **Pygame** oraz przeciwnikiem sterowanym przez algorytm **Minimax**.  

---

## 📌 Funkcje  

1. **Tryb gry**  
   - Gra dla jednego gracza (Ty – czerwone pionki, AI – białe pionki).  

2. **Sterowanie i rozgrywka**  
   - Obsługa ruchów myszką – zaznaczanie i przesuwanie pionków.  
   - Reguły warcabów:  
     - pionki poruszają się tylko do przodu  
     - damka może poruszać się również do tyłu  
     - bicie tylko do przodu (dla pionka), możliwe bicie wielokrotne  
     - damka może bić w obu kierunkach  
     - promocja na damkę w standardowy sposób (po dojściu do ostatniego rzędu)  

3. **AI przeciwnik**  
   - Algorytm Minimax z przeszukiwaniem do określonej głębokości (`depth = 3`).  

4. **Grafika**  
   - Prosta, czytelna oprawa wizualna oparta na bibliotece pygame.  

---

## 🖼️ Screenshot  

*(możesz tu wrzucić zrzut ekranu np. `screenshot.png`)*  

---

## ⚙️ Wymagania  

- Python 3.8+  
- Biblioteka **Pygame**  

### Instalacja:  
```bash
pip install pygame
```

### Klonowanie repozytorium i uruchomienie gry:
```bash
git clone https://github.com/twoj-nick/checkers-ai.git
cd checkers-ai
python main.py
```

### 🎮 Sterowanie
- Lewy przycisk myszy – wybór pionka oraz miejsce docelowe
- Czerwone pionki – gracz
- Białe pionki – sterowane przez AI


### 🧠 Algorytm AI
AI korzysta z algorytmu Minimax:
- Przegląda wszystkie możliwe ruchy do ustalonej głębokości (depth).
- Ocena pozycji oparta jest na liczbie pionków i dam.
#### Wybiera ruch:
- maksymalizujący szanse wygranej dla AI
- minimalizujący szanse przeciwnika
