# Projekt2 -Wtyczka do programu QGIS

# Cel projektu 

Głównym zadaniem było stworzenie wtyczki w programie QT Designer do programu QGIS, dzięki której policzymy różnicę wysokości między dwoma punktami oraz pole powierzchni jeśli wybierzemy przynjamniej trzy punkty.


# Podstawowe funkcje

- obliczenie różnicy wysokości między dwoma zaznaczonymi punktami
- obliczenie pola powierzchni między trzema zaznaczonymu punktami metodą Gaussa

# Wymagania

- system operacyjny Windows 10 lub 11
- program QGIS wersja 3.28.4
- python 3.9.7
- biblioteka qgis.PyQt
- biblioteka qgis.utilis
- biblioteka PyQt5
- biblioteka qgis._core
- biblioteka qgis._gui

# Informacje
- Pole przechowujące wysokość to liczba zmienno przecinkowa, inaczej decimal number.

# Interfejs wtyczki

Żeby uruchomić wtyczkę otworzyć program QGIS, wyszukać ją i zainstalować w górnej zakładce 'wtyczki'.


Przykład wykonałem na podstwie osnowy wysokościowej Białegostoku.


![image](https://github.com/adamstan102/Projekt2/assets/129062363/4ee291d4-3280-47dd-b2e1-4badaac3059b)

Po wybraniu więcej niż dwóch punktów wyskoczy komunikat, że musiamy wybrać dokładnie dwa punkty. 

Gdy wybierzemy dwa punkty, program wyświetli id punktu i obliczy różnice wysokości w metrach.


![image](https://github.com/adamstan102/Projekt2/assets/129062363/90abf502-0b49-4835-802e-60e036265a20)


Podobnie korzysta się z wtyczki w celu obliczenia pola. W tym przypadku musimy wybrać więcej niż trzy punkty w programie qgis.


![image](https://github.com/adamstan102/Projekt2/assets/129062363/5321b2df-08ab-4c6f-b034-9e5041074704)


Program wyświetli nr punktu w Qgis'ie oraz obliczy pole w metrach kwadratowych.



# Znane błędy

Na ten moment możemy obliczać różnice wysokości jedynie w układzie plevrf2007nh.
