# Seminar 3 - A gentle introduction to feature-driven development

O să considerăm următoarea problemă
```text
Scrieți o aplicație pentru a gestiona o listă de fructe.
Fiecare fruct o să aibă un nume, culoare, și greutate.
Aplicația să permită următoarele funcționalități:
1. adăugare fructe: utilizatorul introduce detaliile fructelor
și aplicația le adaugă în listă
2. filtrare după culoare: utilizatorul introduce o culoare
iar aplicația afișează acele fructe care sunt de culoarea
respectivă
3. afișarea sumei greutății tuturor fructelor
```

- după ce am introdus probleme un pic mai complexe decât cele considerate până acum, trebuie să ne gândim la cum
gestionăm complexitatea asta. În ce constă complexitatea asta?
- dacă până acum am avut numere sau șiruri, eventual matrici, în probleme ca și cea considerată, avem obiecte din viața reală
- așa cum obiectele din viața reală vin cu proprietăți, comportamente și dificultăți din viața reală, ceea ce pentru
numere, șiruri sau matrici au fost operații evidente, pe care trebuia să le combinăm într-un anumit fel, pentru obiecte
din viața reală ne confruntăm și de maparea realității în cod.
- în primul rând, trebuie să reprezentăm obiectele din viața reală în cod. Reprezentarea asta e de fapt o metaforă.
- o să vrem să grupăm propetățile unui obiect într-un singur loc. 

- :bulb: reprezentare prin dicționar:
```python
fruit = {
    "name": "apple",
    "color": "red",
    "weight": 100
}
```

:bulb: Sau o listă:
```python
fruit = ["apple", "red", 100]
```

:bulb: sau mai încolo, clase( dar again, asta mai încolo):

```python
class Fruit:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
```

Cu asta, am rezolvat reprezentarea de obiecte. Însă, aplicația necesită și niște funcționalități, care sunt la fel de complexe.
Maparea realității în cod mentenabil, lizibil și curat necesită o abordare de implementare la fel de curată. 
După ce am desfăcut problema prin crearea listei de activități, lista de funcționalități, etc., trebuie să ne gândim la cum
implementăm fiecare funcționalitate. TDD e o abordare pentru asta. După ce *am identificat un task pentru care să scriem o funcție*,
repetăm următorii pași:
1. scriem test (da, prima dată scriem testul, apoi implementarea)
2. vedem că testul pică(pare redundant dar uneori te scapă de niște cazuri de eroare, ideea e să ne asigurăm că nu cumva din greșeală merge cazul asta fără ca noi să avem ceva implementat)
3. implementăm funcția
4. rulăm testele, dacă pică, revenim la pasul 3.
5. refactorizăm codul, dacă e cazul(first make it work, then make it pretty. But do make it pretty), și verificăm să mai treacă testele


## Teste
Pentru a testa că funcția face ce vrem noi să facă,o să testăm cu `assert`.
```python
assert my_function(my_data) == my_result, "This is what the user sees if the test fails"
```
Important de menționat să încercăm să scriem funcții testabile. Funcția să fie cât mai pură și independentă.

:x: :
```python
numbers = [1, -2, 2, -3, ...]
def filter_positive_numbers():
    for number in numbers: # folosește variabila din afară, mai greu de testat
        if number > 0:
            print(number) # nu am cum să testez ce returnrează
```
În funcția de sus, dacă vreau să văd ce a făcut funcția, *trebuie să
știu ce era în listă* când s-a apelat(and boy do we not know that oh-so often),
*trebuie să mă uit la consolă* să văd ce a printat și să verific de mână că a făcut ce trebuie. Dacă într-o zi
vreau să afișez rezultatele astea într-o aplicație cu interfață grafică, pot să arunc funcția de tot.


:white_check_mark:
```python
global_numbers = [1, -2, 2, -3, ...]

def filter_positive_numbers(numbers):
    positive_numbers = []
    for number in numbers:
        if number > 0:
            positive_numbers.append(number)
    return positive_numbers
```
În funcția de sus, dacă vreau să văd ce a făcut funcția, *nu trebuie să știu ce era în listă* când s-a apelat,
trebuie să știu doar ce am trimis ca parametru, *nu trebuie să mă uit la consolă* să văd ce a printat și să verific de mână că a făcut ce trebuie.
Pot să-i dau pe loc ce parametri vreau eu fără să trebuiască să vânez prin cod după altă variabilă să-i văd valoarea.
Rezultatul e returnat, deci pot să verific pe loc dacă e ce trebuie, fără să mai caut prin consolă. 
Dar cel mai important, pot să scriu teste automate pentru funcița asta, și nu o să mai trebuiască să mă gândesc
la toate cazurile astea de fiecare dată când rulez programul și vreau să verific. Testele automate o să fie acolo
și o să aibă grijă ca dacă aș modifica ceva în funcție, să nu stric ceva ce funcționa deja.

Combinăm TDD cu FDD. Pentru fiecare funcționalitate, scriem teste, apoi implementăm funcționalitatea.



:bulb: Împărțirea laboratorului în iterații echilibrate este importantă. Nimeni n-o să vă laude că ați făcut toate
funcționalitățile deodată(ba chiar vă încurcă, cum o să tot modificăm întregul proiect). Ideea e tocmai să învățăm să
împărțim problemele în bucăți mici digerabile, fără să fim prea ambițioși(că vă duce în burnout nu de alta) dar să 
nici nu lăsăm tot la ultima sută de metri, că se întâmplă și asta.


