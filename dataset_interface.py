import pandas
import pickle, math
from io import StringIO

KEY = "4c9d22952d099e8099c4f552977deb20"

def call_api_related_kw(keyword):
    response = requests.get(f"https://api.semrush.com/?type=phrase_related&key={KEY}&phrase={keyword}&export_columns=Ph,Nq,Cp,Co,Nr,Td,Rr,Fk&database=nl&display_limit=1000&display_sort=nq_desc&display_filter=%2B|Nq|Lt|1000")
    DB = pandas.read_csv(StringIO(response.text))
    return DB

# Load in the database
def get_suggested_keywords(keyword="stofzuiger", conv=0.03, avg_product_value=100, sv_cutoff=100, ret_cutoff=10):
    DBZ = call_api_related_kw(keyword)
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

    sea_suggestions = sorted(k, key = lambda keyword: -profit_values[keyword]*math.log(volume_values[keyword]))
    seo_suggestions = sorted(k, key = lambda keyword: keydif_values[keyword]*math.log(volume_values[keyword]))
    seo_suggestions = [key_k for key_k in k if keydif_values[key_k] < 80]

    # Take SV & Competitive Density into account
    # sea_suggestions = sorted(k, key = lambda keyword: -profit_values[keyword]*math.log(volume_values[keyword])/cd_values[keyword])[:cutoff]
    
    return sea_suggestions[:ret_cutoff], seo_suggestions[:ret_cutoff]

