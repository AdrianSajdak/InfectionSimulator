# Symulacja Zakażeń

Ten projekt symuluje rozprzestrzenianie się zakażenia w populacji poruszającej się w dwuwymiarowym obszarze. Demonstruje takie koncepty jak programowanie obiektowe, wzorce projektowe (Stan i Pamiątka) oraz przestrzega zasad SOLID. Projekt realizowany w ramach zajęć na uczelni Politechnika Krakowska dla przedmiotu Technologie Obiektowe.

## Spis treści

- [Funkcjonalności](#funkcjonalności)
- [Wymagania](#wymagania)
- [Instalacja](#instalacja)
- [Użycie](#użycie)
- [Scenariusze](#scenariusze)
- [Struktura Projektu](#struktura-projektu)
- [Wzorce Projektowe](#wzorce-projektowe)
- [Wkład w Projekt](#wkład-w-projekt)
- [Licencja](#licencja)

## Funkcjonalności

- Symulacja osób poruszających się losowo w zdefiniowanym obszarze.
- Rozprzestrzenianie się zakażenia na podstawie bliskości i czasu kontaktu.
- Różne stany zdrowia: Zdrowy, Objawowy, Bezobjawowy, Wyzdrowiały, Odporny.
- Wizualizacja przy użyciu Pygame.
- Możliwość zapisu i wczytywania stanu symulacji.
- Dwa scenariusze:
  - Scenariusz 1: Brak początkowej odporności.
  - Scenariusz 2: Część osób posiada początkową odporność.

## Wymagania

- Python 3.6 lub nowszy
- Biblioteka Pygame

## Instalacja

1. **Sklonuj Repozytorium**

   ```bash
   git clone https://github.com/AdrianSajdak/InfectionSimulator.git
   pip install -r requirements.txt

   ```Uruchom
   python main.py


