import pandas
import pickle

with open("Datasets/domain_rapport.pydb", "rb") as file:
    DB = pickle.load(file)

def equation(database=DB, keyword='social brothers', conv=0.03, productwaarde=100):
    row = DB.loc[DB['Keyword'] == keyword]
    CTR = int(row['Traffic'])/int(row['Search Volume'])
    CPC = float(row['CPC'])

    omzet_per_click = CTR * conv * productwaarde
    return omzet_per_click - CPC

sv = 0
tt = 0
for index, row in DB.iterrows():
    sv += int(row['Search Volume'])
    tt += int(row['Traffic'])
    
tctr = tt / sv
