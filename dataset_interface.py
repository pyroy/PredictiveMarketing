import pandas
import requests
import pickle, math
from io import StringIO

KEY = "a37240a09f1fb41acc983de0c2f0f49d"

def call_api_related_kw(keyword):
    response = requests.get(f"https://api.semrush.com/?type=phrase_related&key={KEY}&phrase={keyword}&export_columns=Ph,Nq,Cp,Nr&database=nl&display_limit=1000&display_sort=nq_desc&display_filter=%2B|Nq|Lt|1000")
    DB = pandas.read_csv(StringIO(response.text), sep=';')
    return DB

def get_kd(keywords):
    phrase = ";".join(keywords)
    response = requests.get(f"https://api.semrush.com/?type=phrase_kdi&key={KEY}&&export_columns=Ph,Kd&phrase={phrase}&database=nl")
    DB = pandas.read_csv(StringIO(response.text), sep=';')
    return DB['Keyword Difficulty Index']

# Load in the database
def get_suggested_keywords(keyword="stofzuiger", conv=0.03, avg_product_value=100, sv_cutoff=100, ret_cutoff=10, check_seo=False):
    DBZ = call_api_related_kw(keyword)
    profit_values = {}
    volume_values = {}
    keydif_values = []
    recommend_sea = []
    recommend_seo = []
    k = []
    k2 = []
    for index, row in DBZ.iterrows():
        # clicks * conversion * product value
        if int(row['Search Volume']) < sv_cutoff: continue
        if int(row['Number of Results']) == 0: continue
        volume_values[row['Keyword']] = int(row['Search Volume'])
        k2.append(row['Keyword'])
        if float(row['CPC']) == 0.0: continue
        profit = avg_product_value - int(1/conv) * float(row['CPC'])
        if profit > 0:
            profit_values[row['Keyword']] = profit
            k.append(row['Keyword'])
            
    
    
    # sea_suggestions = sorted(k, key = lambda keyword: -profit_values[keyword])
    # seo_suggestions = sorted(k, key = lambda keyword: keydif_values[keyword])

    sea_suggestions = sorted(k, key = lambda keyword: -profit_values[keyword]*math.log(volume_values[keyword]))

    if check_seo:
        while(k2):
            keydif_values.extend(list(zip(k2[:100], get_kd(k2[:100]))))
            k2 = k2[100:]
            if len(keydif_values) > 1200:
                return ['error']

        keydif_values = dict(keydif_values)

        seo_suggestions = sorted(k, key = lambda keyword: keydif_values[keyword]*math.log(volume_values[keyword]))
        seo_suggestions = [key_k for key_k in k if keydif_values[key_k] < 80]
        
        return sea_suggestions[:ret_cutoff], seo_suggestions[:ret_cutoff]

    # Take SV & Competitive Density into account
    # sea_suggestions = sorted(k, key = lambda keyword: -profit_values[keyword]*math.log(volume_values[keyword])/cd_values[keyword])[:cutoff]
    
    return sea_suggestions[:ret_cutoff], []

