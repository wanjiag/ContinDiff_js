import pandas as pd
import random
import numpy as np
import os

cwd = os.getcwd()

for sub in range(1, 51):

    num = list(range(1, 19))
    random.shuffle(num)
    list_a = ["stimuli/scene/pairs/A" + str(e) + ".jpg" for e in num]
    list_b = ["stimuli/scene/pairs/B" + str(e) + ".jpg" for e in num]

    lure = list(range(1, 37))
    random.shuffle(lure)
    lure = ["stimuli/scene/lures/" + str(e) + ".jpg" for e in lure]
    lure1 = lure[0:18]
    lure2 = lure[18:37]

    change = np.random.randint(0, 2, size=18)

    location = [1, 2, 3]

    list_a_first = np.random.randint(0, 2, size=18)

    first_pic = []
    second_pic = []
    key = [] # same = 'j', different = 'k'

    count = 0
    for i in list_a_first:
        if i == 1:
            first_pic.append(list_a[count])
            if change[count] == 0:
                second_pic.append(list_a[count])
                key.append('j')
            else:
                second_pic.append(list_b[count])
                key.append('k')
        else:
            first_pic.append(list_b[count])
            if change[count] == 0:
                second_pic.append(list_b[count])
                key.append('j')
            else:
                second_pic.append(list_a[count])
                key.append('k')
        count += 1

    locy = []
    loc2y = []
    loc3y = []

    for j in range(len(num)):
        random.shuffle(location)
        locy.append(location[0])
        loc2y.append(location[1])
        loc3y.append(location[2])

    output = {'first_pic': first_pic,
              'second_pic': second_pic,
              'locy': locy,
              'lure1': lure1,
              'loc2y': loc2y,
              'lure2': lure2,
              'loc3y': loc3y,
              'change': change,
              'key': key}

    output = pd.DataFrame(output)

    output_path = os.path.join(cwd, 'sub_file', 'sub{:02d}.csv'.format(sub))
    output.to_csv(output_path, index=True, index_label='index')
