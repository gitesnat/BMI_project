# Import seaborn
import seaborn as sns
import pandas as pd

daneGotowe = {
  "system":[],
  "waga":[],
  "wzrost":[],
  "bmi":[]
}

dane = open("./dane.txt", "r")  
pomiary = dane.readlines()
for item in pomiary:
  item = item.split()
  daneGotowe["system"].append(item[0]) 
  daneGotowe["waga"].append(int(item[1])*(0.45 if item[0]=="I"else 1))
  daneGotowe["wzrost"].append(float(item[2])*(0.025 if item[0]=="I"else 1))
  daneGotowe["bmi"].append(float(item[3]))
dataFrame =  pd.DataFrame.from_dict(data=daneGotowe)
dataFrame = dataFrame.sort_values(by=["wzrost"], ascending=False)
print(dataFrame)

sns.set_theme()
sns.relplot(
data=dataFrame,
x=dataFrame["waga"], y=dataFrame["wzrost"], 
col="system", hue="bmi",
)
# sns.relplot(data=dataFrame,
# x="waga", y="wzrost", values="bmi", kind="line")