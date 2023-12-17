mnoznikMetryczny = 1         #no wiadomo
mnoznikImperialny = 703      # jak się liczy bmi w imperialnym to trzeba wynik pomnożyć razy 703

def pomiar(mnoznik):
  dane = open("./dane.txt", "a")    
  masa = int(input("podaj wagę \n"))                                                              #podawanie masy
  wzrost = int(input(("podaj wzrost (cm/cale)\n")))/(100 if mnoznik == mnoznikMetryczny else 1)   #podawanie wzrostu i trzeba też wziąć pod uwagę że 180cm to 1.8 metra a 5'5" to 65", ale w impreialnym to nie ma sensu więc od razu o cale się pytam czemu nie zapytam się od razu o metry a no nie wiem no tak zrobiłem to niech tak będzie ważne że działa może po prostu nie lubie flaotów przyjmować od użytkownika 
  bmi = round((masa/wzrost**2) * mnoznik,2)                                                       #liczenie bmi  
  print("wskaźnik bmi jest równy: ", bmi)                                                         #wyświetlanie wartości 
  dane.write(f"{"M" if mnoznik == mnoznikMetryczny else "I"} {masa}  {wzrost}  {bmi}\n")          #zapisywanie w pliku
  kolejny = input("czy chcesz dokonać kolejnego pomiaru [y/n]")                                   #pytanie o kolejny pomiar
  dane.close() 
  if(kolejny == "y"): pomiar(mnoznik)                                                             #jeśli tak to jeszcze raz wywołujemy funkcje jeśli nei to kończy sie funkcja i porgram

def bmiInput():                                                                   #otwieram plik z danymi
  while True:                                                                                           #używam najbardziej ekskluzywnej pętli jakiej moge użyć    
    jednostka = input("W jakich jednostkach chcesz wprowadzić pomiar? (metryczne[1]/imperialne[2])\n")  #pytam o jednoski aż do skutku
    if(jednostka == "1" or jednostka == "2"): break                                                     #pętla się breakuje tylko wtedy kiedy zostanie wybrana jednostka (1 labo 2)
  mnoznik = mnoznikMetryczny if jednostka == "1" else mnoznikImperialny                                 #ustalam mnożnik na podstawie wybranej jednoski
  pomiar(mnoznik)                                                                                       #wywołuje funkcje która będzie się otwierać rekurencyjnie az do końca programu
                                                                                           #po zakończeniu programu zamykam plik z danymi