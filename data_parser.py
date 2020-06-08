import pandas

# Load in the csv files
domein_rapport = pandas.read_csv("Datasets/Domein rapport - Socialbrothers.nl.csv")
google_ads = pandas.read_csv("Datasets/Google Ads - Zoekwoordrapport.csv", skiprows=2)
rapport = pandas.read_csv("Datasets/Zoekwoordrapport - Stofzuiger.csv")

# Filter on rows where the CTR is known, we need it for the profit margin equation.
google_ads = google_ads.loc[google_ads['CTR'] != ' --']

