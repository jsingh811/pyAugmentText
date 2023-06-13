from transformers import pipeline

en_fr_translator = pipeline("translation_en_to_fr", model="t5-base")
fr_en_translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en")


def get_back_translation(text):
    fr = en_fr_translator(text)[0]["translation_text"]
    en = fr_en_translator(fr)[0]["translation_text"]
    return en

if __name__ == "__main__":
    orig_text = "I love ice cream so I went outside to get it from the store 5 miles way."
    back_translated = get_back_translation(orig_text)
    print(f"{orig_text=}\n{back_translated=}")
