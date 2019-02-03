# PerceptronPicklePl



Provided are three pretrained models for Polish language:

polish_full_5.pickle
polish_simplified_5.pickle
polish_simplified_uber_5.pickle

They have been trained on Milionowy Korpus (it can be downloaded from here: http://nkjp.pl/index.php?page=14&lang=0)


In order to tag with NLTK perceptron tagger polish sentences, they must be loaded manually in this way:

`from nltk.tag.perceptron import PerceptronTagger`

`tagger = PerceptronTagger(load=False)`

`tagger.load(path_to_pretrained_model)`

`tagger.tag(sentence_as_a_list_of_words) (eg. tagger.tag(['Ala', 'ma', 'kota', '.'])`



In order to work correctly every punctuation mark need to be a single item in such a list. 
Also agglutination endings and particles need to be separated and presented as single items 
(eg. ['chciał', 'by', 'm'] or ['jeśliby', 'm', 'zechciał']). A simple code for preparing polish
sentences in this way will be provided.

These models are different from each other on account of data provided for every single part of
speech. The first one is the fullest, so every word is described as it should be (genders, cases,
persons etc), but the result is that there are around 800 parts of speech. That leads to the 
effect that the model not very reliable, especially if your main concern is cases. The second and 
third are much  simplified, basically for those POSes that are part of some declension model, left
were only cases, and verbs have only tenses and aspect attributes (in uber even aspect had been
thrown away). But thanks to that there are only about 100 poses, and tagging (especially for 
cases) is much more reliable.
