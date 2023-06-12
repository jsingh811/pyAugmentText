# pyAugmentText
Python library for augmenting text data with new modified samples based on existing samples.

```  
from pyAugmentText.methods import synonyms_replacement

text_list = [
  "I love to go outdoors to ride my bike.",
  "Can you lend me some money for a few hours?"
]
new_list = []
for text in text_list:
  new_list.append(synonyms_replacement.replace_text(text, 3))

print(new_list)
# >> [' I love to giveuptheghost outdoors to tantalize my pedal.', ' tail you impart me some money for a few hour?']
```
