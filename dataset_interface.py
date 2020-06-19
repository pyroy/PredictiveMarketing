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

def get_suggested_keywords(keyword_rapport=DBZ, conv=0.03, avg_product_value=100, cutoff=10, mode="cpc"):
    profit_values = {}
    volume_values = {}
    recommend_sea = []
    recommend_seo = []
    for index, row in DBZ.iterrows():
        # clicks * conversion * product value
        if float(row['CPC (USD)']) == 0.0: continue
        profit = avg_product_value - int(1/conv) * float(row['CPC (USD)'])
        profit_values[row['Keyword']] = profit
        click_v[row['Keyword']] = clicks
        k.append(row['Keyword'])

    # Only takes CPC into account
    if mode == "cpc":
        suggestions = sorted(k, key = lambda keyword: -profit_values[keyword])[:cutoff]

    # Takes search volume into account
    elif mode == "cpc+sv":
        suggestions = sorted(k, key = lambda keyword: -profit_values[keyword]*math.log(volume_values[keyword]))[:cutoff]

    # Take SV & Competitive Density into account
    else:
        suggestions = sorted(k, key = lambda keyword: -profit_values[keyword]*math.log(volume_values[keyword])/cd_values[keyword])[:cutoff]
    
    total_clicks = sum([click_v[k] for k in suggestions])
    total_revenue = sum([omzet_values[k] for k in suggestions])
    total_competition = sum([-math.log(cd_values[k]) for k in suggestions])
    total_unspent_budget = sum([unspent_v[k] for k in suggestions])
    return suggestions, total_clicks, total_revenue, total_competition, total_unspent_budget

def get_suggestions(mode="cpc", budget=5000, cutoff=10):
    sk, tcs, tr, tc, tub = get_suggested_keywords(budget_per_keyword = budget/cutoff, cutoff = cutoff, mode = mode)
    print("Suggested keywords:")
    for k in sk:
        print("- " + k)
    print("\nTotal Clicks:\t\t{}".format(int(tcs)))
    print("Negative Log CD:\t{}".format(round(tc,2)))
    print("\n=====\nBudget:\t\t\t{}$".format(budget))
    print("Unspent Budget:\t\t{}$".format(round(tub,2)))
    print("Total Revenue:\t\t{}$".format(round(tr,2)))
    pm = int(100*tr/(budget-tub)-100)
    if pm > 0:
        print("Profit Margin:\t\t+{}%".format(pm))
    else:
        print("Profit Margin:\t\t{}%".format(pm))
