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

Żeby uruchomić wtyczkę otworzyć program QGIS, wyszukać ją i zainstalować w górnej zakładce 'Wtyczki'.


Przykład wykonałem na podstwie osnowy wysokościowej Białegostoku.


![image](https://github.com/adamstan102/Projekt2/assets/129062363/f24cc53d-2a86-40b1-849b-d192850a10f5)


Po wybraniu więcej niż dwóch punktów wyskoczy komunikat, że musiamy wybrać dokładnie dwa punkty. 

Gdy wybierzemy dwa punkty, program wyświetli id punktu i obliczy różnice wysokości w metrach.


![image](https://github.com/adamstan102/Projekt2/assets/129062363/efae9891-8a2c-4aeb-8c7d-4f1244275133)



Podobnie korzysta się z wtyczki w celu obliczenia pola. W tym przypadku musimy wybrać więcej niż trzy punkty w programie qgis.


![image](https://github.com/adamstan102/Projekt2/assets/129062363/8cd4c0d9-af17-4eab-ace1-a7e1aa581431)


Program wyświetli nr punktu w Qgis'ie oraz obliczy pole w metrach kwadratowych.



# Znane błędy

Na ten moment możemy obliczać różnice wysokości jedynie w układzie plevrf2007nh.
