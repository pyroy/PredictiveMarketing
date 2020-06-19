from OpenDutchWordnet import Wn_grid_parser
instance = Wn_grid_parser(Wn_grid_parser.odwn)

def get_similar_words(woord):
    ret = []
    senses = instance.lemma_get_generator(woord)
    for sense in senses:
        le_el = instance.les_find_le(sense.get_id())
        if not le_el: raise Exception
        syn = instance.synsets_find_synset(le_el.get_synset_id())
        meanings = instance.les_all_les_of_one_synset(syn.get_id())

        for meaning in meanings:
            ret.append(meaning.get_lemma())

    return list(set(ret))
