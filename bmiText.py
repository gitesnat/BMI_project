mnoznikMetryczny = 1         
mnoznikImperialny = 703      

def bmiText():
  daneRaw = open("./dane_raw.txt","r")
  dane = open("./dane.txt","a")
  pomiary = (daneRaw.readlines())
  while True:                                                                                           
    jednostka = input("W jakich jednostkach chcesz wprowadzić pomiar? (metryczne[1]/imperialne[2])\n")  
    if(jednostka == "1" or jednostka == "2"): break                                                     
  mnoznik = mnoznikMetryczny if jednostka == "1" else mnoznikImperialny   
  for item in pomiary:
    item = item.split()
    waga = int(item[0])
    wzrost = int(item[1])/(100 if mnoznik == mnoznikMetryczny else 1)
    bmi = round((waga/wzrost**2) * mnoznik,2)
    dane.write(f"{"M" if mnoznik == mnoznikMetryczny else "I"} {waga}  {wzrost}  {bmi}\n")   
  daneRaw.close()
  dane.close()