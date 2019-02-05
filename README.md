# PerceptronPicklePl



There are provided two pretrained models, one that provides more information on a word (polish_full_merged_10.pickle, and second that provides less, but is more accurate (polish_simplified.pickle) and is lighter.

They are trained tagged corpora, where agglutinated endings and particles are not treated as single words, if they are written together. This allows us to use those models for tagging text, that is not prepared in such a way, that all agglutination particles are detached from words.

They have been trained on lists of tagged sentence/words extracted from Milionowy Korpus (it can be downloaded from here: http://nkjp.pl/index.php?page=14&lang=0).

In order to tag with NLTK perceptron tagger polish sentences, they must be loaded manually in this way:

`from nltk.tag.perceptron import PerceptronTagger`

`tagger = PerceptronTagger(load=False)`

`tagger.load(path_to_pretrained_model)`

`tagger.tag(sentence_as_a_list_of_words) (eg. tagger.tag(['Ala', 'ma', 'kota', '.'])`

If you would like to train again a model, do this:

`tagger.train(tagged_corpus_of_sentences, save_loc='path_where_you_want_to_save_model', nr_iter=nr_of_iterations)`

In order to work correctly every punctuation mark need to be a single item in such a list. 

The simplified model operates on a number of about 100 POSes, and is useful for case specification and analysis of a sentence. The full model operates on a number of more than 800 poses. 

