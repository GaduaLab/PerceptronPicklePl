
# improve the tagged words sample
# adds aglutinated be to the words that they are attached to.
# in Milionowy they are singled out, and there is reason behind it
# but the problem is that parsing polish text in order to
# detach these aglutination particles is much too complicated
# it's much better then to feed perceptron with forms, that it will
# be later expected to tag

def merge_aggl_by(tagged):

    new_tagged =[]
    for sentence in tagged:
        less_index = 0
        new_sentence = []
        for index, tagged_word in enumerate(sentence):

            if tagged_word[1] == 'aggl_by':

                word = sentence[index-1][0]
                aggl_word = word + tagged_word[0]
                # only works for simplified

                pos = sentence[index-1][1] + ',aggl_by'
                new_sentence[index-1-less_index] = (aggl_word, pos)

                less_index += 1
                continue

            new_sentence.append(tagged_word)
        new_tagged.append(new_sentence)

    return new_tagged


def merge_aggl_endings(tagged):
    poses = set()
    new_tagged = []
    for sentence in tagged:
        less_index = 0
        new_sentence = []
        for index, tagged_word in enumerate(sentence):

            if tagged_word[1] == 'aglt':

                word = sentence[index - 1][0]
                aggl_word = word + tagged_word[0]

                new_sentence[index - 1 - less_index] = (aggl_word, sentence[index - 1][1])
                poses.add(sentence[index - 1 - less_index][1])
                less_index += 1

                continue

            new_sentence.append(tagged_word)
        new_tagged.append(new_sentence)

    return new_tagged

def merge_aglutination_parts(tagged, save_to=None):

    agl_by = merge_aggl_by(tagged)
    agl_end = merge_aggl_endings(agl_by)

    if save_to:
        file = open(save_to, 'w')
        file.write('tagged=' + str(agl_end))
        file.close()

    return agl_end

if __name__ == '__main__':

   from pol_tagged import tagged
   merge_aglutination_parts(tagged, save_to='pol_tagged_aggl.py')
   from pol_tagged_simplified import tagged
   merge_aglutination_parts(tagged, save_to='pol_tagged_simplified_aggl.py')
   from pol_tagged_simplified_uber import tagged
   merge_aglutination_parts(tagged, save_to='pol_tagged_simplified_uber_aggl.py')









