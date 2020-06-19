from OpenDutchWordnet import Wn_grid_parser
instance = Wn_grid_parser(Wn_grid_parser.odwn)

while True:
    woord = input(">")
    senses = instance.lemma_get_generator(woord)
    for sense in senses:
        print(sense.get_lemma())
