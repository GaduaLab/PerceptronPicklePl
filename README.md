# PerceptronPicklePl

These are pretreined models for perceptron algorithm, that is included into NLTK library of Python. Thanks to them perceptron will be able to analyze Polish sentences with a high degree of accuracy.

There are two pretrained models, one that provides more information on a word (polish_full_merged_10.pickle, and the second one that provides less, but is more accurate (polish_simplified.pickle) and is lighter.

They are trained on tagged corpora, where agglutinated endings and particles are not treated as single words, if they are written together. This allows us to use those models for tagging texts, that are not prepared in such a way, that all agglutination particles are detached from words.

The training process was conducted on lists of tagged sentence/words extracted from Milionowy Korpus (it can be downloaded from here: http://nkjp.pl/index.php?page=14&lang=0).

In order to tag Polish sentences with NLTK perceptron tagger, they must be loaded manually:

`from nltk.tag.perceptron import PerceptronTagger`

`tagger = PerceptronTagger(load=False)`

`tagger.load(path_to_pretrained_model)`

`tagger.tag(sentence_as_a_list_of_words) (eg. tagger.tag(['Ala', 'ma', 'kota', '.'])`

so if you want to input a sentence as a text, you have to put its elements in an array.

If you would like to train again a model, do this:

`tagger.train(tagged_corpus_of_sentences, save_loc='path_where_you_want_to_save_model', nr_iter=nr_of_iterations)`

In order to work correctly every punctuation mark need to be a single item in such a list. 

The simplified model operates on a number of about 100 POSes, and is useful for case specification and analysis of a sentence. The full model operates on a number of more than 800 poses. The list of those poses can be looked up here https://github.com/GaduaLab/PerceptronPicklePl/blob/master/poses.txt.

