from pyAugmentText.methods import synonyms_replacement

def augment(text, methods=[("synonyms", 3)]):
    for m in methods:
        if m == "synonyms":
            return synonyms_replacement.synonyms_replacement(text, m[1])
    
