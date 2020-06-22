import pandas
import pickle, math

# Load in the database
with open("Datasets/domain_rapport.pydb", "rb") as file:
    DB = pickle.load(file)

with open("Datasets/stofzuiger.pydb", "rb") as file:
    DBZ = pickle.load(file)

# Calculate profit per keyword using the equation in berekening.txt
def equation1(database=DB, keyword='social brothers', conv=0.03, productwaarde=100):
    row = DB.loc[DB['Keyword'] == keyword]
    CTR = int(row['Traffic'])/int(row['Search Volume'])
    CPC = float(row['CPC'])

    omzet_per_click = CTR * conv * productwaarde
    return omzet_per_click - CPC

def get_suggested_keywords(keyword_rapport=DBZ, conv=0.03, avg_product_value=100, sv_cutoff=100, ret_cutoff=10):
    profit_values = {}
    volume_values = {}
    keydif_values = {}
    recommend_sea = []
    recommend_seo = []
    k = []
    for index, row in DBZ.iterrows():
        # clicks * conversion * product value
        if float(row['CPC (USD)']) == 0.0: continue
        if int(row['Volume']) < sv_cutoff: continue
        if int(row['Number of Results']) == 0: continue
        profit = avg_product_value - int(1/conv) * float(row['CPC (USD)'])
        profit_values[row['Keyword']] = profit
        volume_values[row['Keyword']] = int(row['Volume'])
        keydif_values[row['Keyword']] = float(row['Keyword Difficulty'])
        k.append(row['Keyword'])

    #sea_suggestions = sorted(k, key = lambda keyword: -profit_values[keyword])
    #seo_suggestions = sorted(k, key = lambda keyword: keydif_values[keyword])

    # Takes search volume into account
    sea_suggestions = sorted(k, key = lambda keyword: -profit_values[keyword]*math.log(volume_values[keyword]))
    seo_suggestions = sorted(k, key = lambda keyword: keydif_values[keyword]*math.log(volume_values[keyword]))
    seo_suggestions = [key_k for key_k in k if keydif_values[key_k] < 80]

    # Take SV & Competitive Density into account
    # sea_suggestions = sorted(k, key = lambda keyword: -profit_values[keyword]*math.log(volume_values[keyword])/cd_values[keyword])[:cutoff]
    
    return sea_suggestions[:ret_cutoff], seo_suggestions[:ret_cutoff]
