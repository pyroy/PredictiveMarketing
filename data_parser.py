import pandas
import pickle

# Load in the csv files
domein_rapport = pandas.read_csv("Datasets/Domein rapport - Socialbrothers.nl.csv")
google_ads = pandas.read_csv("Datasets/Google Ads - Zoekwoordrapport.csv", skiprows=2)
rapport = pandas.read_csv("Datasets/Zoekwoordrapport - Stofzuiger.csv")

# Filter on rows where the CTR is known, we need it for the profit margin equation.
google_ads = google_ads.loc[google_ads['CTR'] != ' --']
google_ads = google_ads.loc[google_ads['CTR'] != '0,00%']
google_ads.drop(google_ads.tail(3).index,inplace=True)

domein_rapport = domein_rapport.loc[domein_rapport['Traffic'] != 0]

with open("Datasets/google_ads.pydb", "wb") as file:
    pickle.dump(google_ads, file)

with open("Datasets/domain_rapport.pydb", "wb") as file:
    pickle.dump(domein_rapport, file)

with open("Datasets/stofzuiger.pydb", "wb") as file:
    pickle.dump(rapport, file)
