from pyAugmentText.methods import synonyms_replacement
from pyAugmentText.methods import back_translation

def augment(text_list, methods=["synonyms", "back_translation"], num_samples=10):
    new_list = []
    num_samples_split = round(num_samples/len(methods))
    for m in methods:
        if m == "synonyms":
            for itr in range(0, max(
                1, num_samples_split - (
                len(text_list) * sum([len(text.split()) for text in text_list])/2)
            )):
                for text in text_list:
                    for l in range(1, int(len(text.split())/2)):
                        new_list.append(synonyms_replacement.replace_text(text, l))
        if m == "back_translation":
            for text in text_list:
                new_list += back_translation.get_back_translation(text)
            rem = num_samples_split - len(text_list)
            for text in random.sample(new_list[0:num_samples_split], rem):
                new_list += back_translation.get_back_translation(text)
    return new_list
