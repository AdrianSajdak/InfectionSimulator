
# Symulacja Zakażeń

Ten projekt to symulacja rozprzestrzeniania się zakażenia w populacji poruszającej się w dwuwymiarowym obszarze. Symulacja została zaimplementowana w języku Python, z wykorzystaniem wzorców projektowych Stan i Pamiątka, oraz z przestrzeganiem zasad programowania obiektowego i zasad SOLID. Wizualizacja symulacji jest realizowana za pomocą biblioteki Pygame. Projekt realizowany w ramach zajęć na uczelni Politechnika Krakowska dla przedmiotu Technologie Obiektowe.

## Spis treści
- [Funkcjonalności](#funkcjonalności)
- [Wymagania](#wymagania)
- [Instalacja](#instalacja)
- [Użycie](#użycie)
- [Sterowanie](#sterowanie)
- [Scenariusze](#scenariusze)
- [Struktura Projektu](#struktura-projektu)
- [Wzorce Projektowe](#wzorce-projektowe)
  - [Wzorzec Stan](#wzorzec-stan)
  - [Wzorzec Pamiątka](#wzorzec-pamiątka)
- [Zasady SOLID](#zasady-solid)
- [Wkład w Projekt](#wkład-w-projekt)

## Funkcjonalności

- **Symulacja ruchu**: Osobnicy poruszają się w dwuwymiarowym obszarze o wymiarach 100x100 metrów, w losowych kierunkach i z losową prędkością (nie większą niż 2,5 m/s). Kierunek i prędkość mogą się zmieniać w czasie.
- **Interakcje z granicami**: Po dotarciu do granicy obszaru, osobnik ma 50% szans na zawrócenie do wewnątrz obszaru lub 50% szans na opuszczenie obszaru.
- **Wejście nowych osobników**: Nowi osobnicy wkraczają do obszaru w losowych punktach na jego granicach, aby utrzymać ciągłość populacji. Każdy nowy osobnik ma 10% szans na bycie zakażonym wirusem przy wejściu.
- **Stany zdrowia osobników**:
  - Odporny: Nie może zostać zakażony.
  - Wrażliwy: Może być zdrowy lub zakażony.
    - Zdrowy
    - Zakażony:
      - Objawowy
      - Bezobjawowy
- **Zakażenie**:
  - Dochodzi do niego, gdy:
    - Odległość między osobnikami wynosi nie więcej niż 2 metry oraz
    - Czas bliskiego kontaktu wynosi co najmniej 3 sekundy.
  - Prawdopodobieństwo zakażenia:
    - 100% od osobnika objawowego.
    - 50% od osobnika bezobjawowego.
  - Zakażony osobnik pozostaje zakaźny przez 20-30 sekund, po czym zdrowieje i staje się odporny.
- **Wizualizacja**:
  - Osobnicy są przedstawiani jako kręgi na ekranie:
    - Zielony: Zdrowy
    - Czerwony: Objawowy
    - Pomarańczowy: Bezobjawowy
    - Niebieski: Wyzdrowiały
    - Fioletowy: Odporny od początku
- **Zapisywanie i wczytywanie stanu**:
  - Użytkownik może zapisać aktualny stan symulacji do pliku i wczytać go w dowolnym momencie.

## Wymagania

- Python: Wersja 3.6 lub nowsza
- Pygame: Biblioteka do tworzenia gier i wizualizacji
  - Instalacja: `pip install pygame`

## Instalacja

1. **Sklonuj Repozytorium**

   Jeśli masz Git zainstalowany, możesz sklonować repozytorium:

   ```bash
   git clone https://github.com/AdrianSajdak/InfectionSimulator.git
   cd InfectionSimulator
   ```

   Jeśli nie, możesz pobrać plik ZIP z kodem i go rozpakować.

2. **Utwórz Wirtualne Środowisko (Opcjonalnie)**

   Zaleca się utworzenie wirtualnego środowiska, aby zarządzać zależnościami:

   ```bash
   python -m venv venv
   ```

3. **Aktywuj wirtualne środowisko**:

   - Windows:

     ```bash
     venv\Scripts\Activate.ps1
     ```

   - Linux/MacOS:

     ```bash
     source venv/bin/activate
     ```

4. **Zainstaluj Wymagane Biblioteki**

   Użyj pliku `requirements.txt`, jeśli jest dostępny, lub zainstaluj pygame:

   ```bash
   pip install pygame
   ```

## Użycie

Uruchom symulację za pomocą następującej komendy:

```bash
python main.py
```

## Sterowanie

- **Zamknięcie Okna**: Zakończ symulację, zamykając okno GUI.
- **Naciśnij S**: Zapisz aktualny stan symulacji do pliku `simulation_state.pkl`.
- **Naciśnij L**: Wczytaj stan symulacji z pliku `simulation_state.pkl`.

## Scenariusze

Symulacja obsługuje dwa scenariusze, które można wybrać, modyfikując zmienną `scenario` w pliku `main.py`.

1. **Scenariusz 1**: Początkowa populacja oraz nowi osobnicy nie posiadają odporności.

   ```python
   scenario = 1
   ```

2. **Scenariusz 2**: Część początkowej populacji oraz nowi osobnicy posiadają odporność.

   ```python
   scenario = 2
   ```

   W tym scenariuszu można również dostosować prawdopodobieństwo, z jakim osobnicy posiadają odporność, modyfikując wartość `IMMUNE_PROBABILITY` w pliku `config.py`.

## Struktura Projektu

    infection-simulation/
    ├── main.py
    ├── config.py
    ├── vector.py
    ├── position.py
    ├── person.py
    ├── environment.py
    ├── simulation.py
    ├── states/
    │   ├── __init__.py
    │   ├── IState.py
    │   ├── HealthyState.py
    │   ├── SymptomaticState.py
    │   ├── AsymptomaticState.py
    │   ├── RecoveredState.py
    │   └── ImmuneState.py
    └── memento/
        ├── __init__.py
        ├── IMemento.py
        ├── Memento.py
        └── Caretaker.py

- **main.py**: Główny punkt wejścia aplikacji. Ustawia scenariusz i uruchamia symulację.
- **config.py**: Plik konfiguracyjny zawierający stałe używane w symulacji, takie jak prędkości, prawdopodobieństwa i kolory.
- **vector.py**: Implementacja klasy `Vector`, reprezentującej prędkość i kierunek ruchu osobnika.
- **position.py**: Implementacja klasy `Position`, reprezentującej pozycję osobnika w obszarze symulacji.
- **person.py**: Definicja klasy `Person`, reprezentującej osobnika w symulacji. Zarządza stanami zdrowia i ruchem.
- **environment.py**: Klasa `Environment` zarządza wszystkimi osobnikami w symulacji, w tym ich tworzeniem i usuwaniem.
- **simulation.py**: Orkiestruje symulację, obsługuje pętlę główną, zdarzenia i interakcję z użytkownikiem.
- **states/**: Katalog zawierający implementacje wzorca Stan:
    - **IState.py**: Interfejs dla stanów.
    - **HealthyState.py**: Stan zdrowego osobnika.
    - **SymptomaticState.py**: Stan osobnika z objawami.
    - **AsymptomaticState.py**: Stan osobnika bez objawów.
    - **RecoveredState.py**: Stan osobnika, który wyzdrowiał.
    - **ImmuneState.py**: Stan osobnika odpornego od początku.
- **memento/**: Katalog zawierający implementacje wzorca Pamiątka:
    - **IMemento.py**: Interfejs dla pamiątek.
    - **Memento.py**: Klasa przechowująca stan symulacji.
    - **Caretaker.py**: Klasa zarządzająca pamiątkami, umożliwia zapis i odczyt stanu.

# Wzorce Projektowe

## Wzorzec Stan
Wzorzec Stan pozwala na zmianę zachowania obiektu w zależności od jego stanu wewnętrznego. W tym projekcie zastosowano go do modelowania różnych stanów zdrowia osobników.

### Klasy stanu:
- **HealthyState**: Reprezentuje zdrowego osobnika, który może zostać zakażony.
- **SymptomaticState**: Reprezentuje osobnika z objawami choroby.
- **AsymptomaticState**: Reprezentuje osobnika bez objawów choroby.
- **RecoveredState**: Reprezentuje osobnika, który wyzdrowiał i jest odporny.
- **ImmuneState**: Reprezentuje osobnika odpornego od początku.

### Diagram UML Wzorca Stan:
                +------------------+
                |     Person       |
                +------------------+
                | - state: State   |
                +------------------+
                | + setState(s)    |
                | + request()      |
                +------------------+
                        |
                        v
                +------------------+
                |      State       |
                +------------------+
                | + handle()       |
                +------------------+
                ^                  ^
                |                  |
    +------------------+    +------------------+
    |  HealthyState    |    | SymptomaticState |
    +------------------+    +------------------+
    | + handle()       |    | + handle()       |
    +------------------+    +------------------+

## Wzorzec Pamiątka

Wzorzec Pamiątka umożliwia zapisywanie i przywracanie stanu obiektu bez naruszania hermetyzacji. W projekcie jest używany do zapisywania i wczytywania stanu symulacji.

### Klasy:
- **IMemento**: Interfejs dla pamiątki.
- **Memento**: Przechowuje stan symulacji.
- **Caretaker**: Zarządza pamiątkami, umożliwia zapis i przywracanie stanu.

### Diagram UML Wzorca Pamiątka:
```plaintext
+-----------------------+          +-------------------+
|    Simulation         |          |     Memento       |
+-----------------------+          +-------------------+
| - environment         |          | - state           |
| - time                |          +-------------------+
| - caretaker           |
+-----------------------+
        |                                 ^
        |                                 |
        v                                 |
+-----------------------+          +-------------------+
|     Caretaker         |--------->|   Environment     |
+-----------------------+          +-------------------+
| - mementos: Memento[] |
| + save()              |
| + restore(index)      |
+-----------------------+
```

## Zasady SOLID

Projekt został zaimplementowany zgodnie z zasadami SOLID:

- **S - Single Responsibility Principle (Zasada Pojedynczej Odpowiedzialności)**: Każda klasa ma jednoznaczną odpowiedzialność.
- **O - Open/Closed Principle (Zasada Otwarte/Zamknięte)**: Klasy są otwarte na rozszerzenia, ale zamknięte na modyfikacje.
- **L - Liskov Substitution Principle (Zasada Podstawienia Liskov)**: Obiekty klas dziedziczących mogą zastępować obiekty klas bazowych bez zmiany poprawności programu.
- **I - Interface Segregation Principle (Zasada Segregacji Interfejsów)**: Klient nie powinien być zmuszany do zależności od interfejsów, których nie używa.
- **D - Dependency Inversion Principle (Zasada Odwrócenia Zależności)**: Wysokopoziomowe moduły nie powinny zależeć od modułów niskopoziomowych; oba powinny zależeć od abstrakcji.

## Wkład w Projekt

Wszelkie wkłady są mile widziane! Jeśli chcesz przyczynić się do rozwoju projektu:

1. **Sforkuj Repozytorium**  
   Kliknij na "Fork" w repozytorium GitHub.

2. **Utwórz Gałąź Funkcjonalności**  
   ```bash
   git checkout -b feature/NazwaFunkcjonalności
   ```
3. **Zatwierdź Zmiany**  
   ```bash
   git commit -m 'Dodaj nową funkcjonalność'
   ```
4. **Wypchnij na Gałąź**  
   ```bash
   git push origin feature/NazwaFunkcjonalności
   ```
5. **Otwórz Pull Request**  
   Przejdź do swojego forka na GitHub i otwórz Pull Request.

## Autor:
Adrian Sajdak


