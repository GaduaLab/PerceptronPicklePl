

"""
extracting list of lists of tuples (word, tags) from milionowy corpus.
Milionowy consists of various texts that are divided into a lot
of folders. Each of those folders include files with some particular
data that are named always in the same way.
Files named "ann_morphosyntax.xml" include data that are of interest to us.
Every text is here divided into sentences and then into words, and every word
is described with grammar tags.
This script is to extract all the data from this corpus that
can be used to feed NLTK perceptron.

Return - list of lists (sentences) of tuples (word, tag), that can be fed to Perceptron
"""

import glob, os
import xml.etree.ElementTree as ET

punctuation = {'...': 'ellipsis', '.': 'dot',',':'comma','?':'question mark',
                                    '!': 'exclamation mark',':': 'colon',
                                    ';':'semicolon','-':'hyphen' ,'(':'left parenthesis',
                                    ')':'right parenthesis', '“':'quotation left',
                                    '”': 'quotation right', '"': 'quotation', '–': 'hyphen'}

Milionowy = '.' # it is assumed that the script is run in the same directory that contains folders
                # from milionowy

def extractor(folder = Milionowy, simplified=False):

    listOfTaggedWords = []
    # make a list of all the folders
    proto_dir = os.getcwd()
    os.chdir(folder)
    curdir = os.getcwd()
    directories = [i for i in glob.glob('*') if os.path.isdir(i)]
    full_dir_names = [os.path.join(curdir, i) for i in directories]
    dot = False

    for folder in full_dir_names:

        file = os.path.join(folder, 'ann_morphosyntax.xml')
        if os.path.isfile(file):

            tree = ET.parse(file)
            root = tree.getroot()

            # root[1] - teiCorpus
            # root[1][1][0] - body - it consists of sentences
            from importlib import reload
            for sentence in root[1][1][0]:
                # sentence[0][0] consists of words
                sent = []
                dot = 0
                for index, word in enumerate(sentence[0]):
                    logos = word[0][0][0].text

                    tag = word[0][2][0][1][0].text
                    # tag has this kind of structure:
                    # chodzić:fin:sg:ter:imperf
                    # extract only grammar info


                    if dot == 2 and logos == '.':
                        sent.append(('...', 'ellipsis'))

                        dot = 0
                        continue
                    elif dot == 1 and logos == '.':
                        dot = 2
                        continue

                    elif logos == '.' and index + 1 == len(sentence[0]):
                        sent.append(('.', 'dot'))

                        dot = 0
                        continue
                    elif logos == '.':
                        dot = 1
                        continue

                    # for some reason punctuation marks and
                    # some other words have additional field
                    # <f name="nps">
                    # <binary value="true"/>
                    # < /f>
                    # and so node with grammsr
                    # info is moved one step further.
                    # If this is the case the grammar info is taken from here
                    if not tag:

                        tag = word[0][3][0][1][0].text


                    if logos in punctuation.keys():

                        tag = punctuation[logos]
                        sent.append((logos, tag))
                        continue

                    # cut from tag lemma
                    tag_desc = tag.split(':')[1:]



                    if simplified and len(tag_desc)> 1:
                        # tags will be here simplified
                        # ger

                        if tag_desc[0] == 'ger':
                            # only pos and case
                            tag = tag_desc[0] + ',' + tag_desc[2]
                        elif tag_desc[0] == 'subst':
                            tag = tag_desc[0] + ',' + tag_desc[2]
                        elif tag_desc[0] == 'adj':
                            # adj also have comp info

                            tag = tag_desc[0] + ',' + tag_desc[2] + ',' + tag_desc[4]
                            if simplified == 'uber':
                                tag = tag_desc[0] + ',' + tag_desc[2]
                        elif tag_desc[0] in ['num', 'numcol']:
                            # in numer. only case, numcol means numeral noun
                            tag = tag_desc[0] + ',' + tag_desc[2]
                        elif tag_desc[0] == 'prep':
                            tag = tag_desc[0] + ',' + tag_desc[1]
                        # in verbs only pos and aspect
                        elif tag_desc[0] in ['fin', 'praet', 'bedzie', 'impt']:
                            tag = tag_desc[0] + ',' + tag_desc[3]
                            if simplified == 'uber':
                                tag = tag_desc[0]
                        # get rid of agglutinated endings
                        elif tag_desc[0] == 'aglt':
                            continue
                        elif tag_desc[0] == 'depr':
                            # non standard nouns, but still nouns (szkopy)
                            tag = 'subst,' + tag_desc[2]
                        elif tag_desc[0] in ['pact', 'ppas']:
                            tag = tag_desc[0] + ',' + tag_desc[2] + ',' + tag_desc[4]
                            if simplified == 'uber':
                                tag = tag_desc[0] + ',' + tag_desc[2]
                       
                        elif tag_desc[0] == 'ppron12':
                            tag = tag_desc[0] + ',' + tag_desc[2]
                        elif tag_desc[0] == 'ppron3':
                            tag = tag_desc[0] + ',' + tag_desc[2] + ',' + tag_desc[-2] + ',' + tag_desc[-1]
                        elif tag_desc[0] == 'prep':
                            # get rid of info about nwok and wok forms
                            tag = tag_desc[0] + ',' + tag_desc[1]
                        # qub is beyond me, it obviously contains every other particle like 'nie', 'by', but also some pron like się, czy,
                        elif tag_desc[0] == 'qub':
                            tag = tag_desc[0]

                        elif tag_desc[0] == 'xxx':
                            tag = 'foreign'
                        elif tag_desc[0] == 'winien':
                            tag = tag_desc[0]
                        else:
                            tag = ','.join(tag_desc)
                    elif simplified:
                        tag = tag_desc[0]

                    else:
                        tag = ','.join(tag_desc)


                    # also agl by and nie should be identified with some precision
                    if logos == 'nie':
                        tag = logos
                    if logos == 'by':
                        tag = 'aggl_by'

                    # agglutinated 'by' is described as 'qub', so it's quite simple to recognize a verb in cond mood
                    sent.append((logos, tag))
                listOfTaggedWords.append(sent)

    os.chdir(proto_dir)
    return listOfTaggedWords


from nltk.tag.perceptron import PerceptronTagger


"""
An example of parsed xml


<fs type="morph">
    <f name="orth">
        <string>Close</string>
    </f>
    <!-- Close [11,5] -->
    <f name="nps">
        <binary value="true"/>
    </f>
    <f name="interps">
        <fs type="lex" xml:id="morph_6.4.1-lex">
            <f name="base">
                <string/>
            </f>
            <f name="ctag">
                <symbol value="ign"/>
            </f>
            <f name="msd">
                <symbol value="" xml:id="morph_6.4.1.1-msd"/>
            </f>
        </fs>
        <fs type="lex" xml:id="morph_6.4.3-lex">
            <f name="base">
                <string>close</string>
            </f>
            <f name="ctag">
                <symbol value="subst"/>
            </f>
            <f name="msd">
                <symbol nkjp:manual="true" value="sg:acc:n" xml:id="morph_6.4.3.1-msd"/>
            </f>
        </fs>
    </f>
    <f name="disamb">
        <fs feats="#an8003" type="tool_report">
            <f fVal="#morph_6.4.3.1-msd" name="choice"/>
                <f name="interpretation">
                    <string>close:subst:sg:acc:n</string>
"""
