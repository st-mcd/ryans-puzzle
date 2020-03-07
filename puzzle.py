import json
import itertools
import copy

levels = [
    ["F"],
    ["ER", "OR"],
    ["MEN", "NO", "TH"],
    ["IS", "OG", "TA", "TEW"],
    ["ON", "EA", "OL", "OR", "TI"],
    ["AL", "ATE", "ON", "PEN", "THY", "TEN"]
]

dictionary = json.load(open('words_dictionary.json'))


def search(levels, found=[]):
    combinations = itertools.product(*levels)
    for parts in combinations:
        word = ''.join(parts).lower()
        if word in dictionary:
            found.append(word)

            if(len(levels) > 2):
                nextLevels = copy.deepcopy(levels)

                # remove level parts that have just been used
                for i in range(len(parts)):
                    nextLevels[i].remove(parts[i])

                del nextLevels[0]
                search(nextLevels, found)[0]

            break
    return found


print(search(levels))
