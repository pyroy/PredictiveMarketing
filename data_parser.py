import pandas

domein_rapport = pandas.read_csv("Datasets/Domein rapport - Socialbrothers.nl.csv")
google_ads = pandas.read_csv("Datasets/Google Ads - Zoekwoordrapport.csv", skiprows=2)
rapport = pandas.read_csv("Datasets/Zoekwoordrapport - Stofzuiger.csv")

print(google_ads.head())

google_ads = google_ads.loc[google_ads['CTR'] != ' --']

print(google_ads.head())
