from nltk.tag.perceptron import PerceptronTagger
import sys
from multiprocessing.dummy import Pool as ThreadPool
import threading
from pol_tagged_aggl import tagged as full
from pol_tagged_simplified_aggl import tagged as simplified
from pol_tagged_simplified_uber_aggl import tagged as uber


tagger1 = PerceptronTagger(load=False)
tagger2 = PerceptronTagger(load=False)
tagger3 = PerceptronTagger(load=False)

def percTraining(tagger, tagged, path):
    tagger.train(tagged, save_loc=path, nr_iter=5)
    return tagger




data = [[tagger1, full, 'polish_full_merged.pickle'], [tagger2, simplified, 'polish_simplified_merged.pickle'], [tagger3, uber, 'polish_simplified.pickle']]


if __name__ == '__main__':
    for el in data:
        t = threading.Thread(target=el[0].train, args=(el[1], el[2]))
        t.start()






W poniedziałkowym materiale " Wiadomości " TVP ujawniono tożsamość osób , które blokowały samochód Magdaleny Ogórek . Do incydentu z udziałem dziennikarki Telewizji Polskiej doszło w sobotę , po emisji programu " Studio Polska " . Część komentatorów zastanawia się , czy publikacja wizerunku osoby biorącej udział w proteście nie narusza prawa , w tym przepisów RODO . O sprawę spytaliśmy ekspertów . 





