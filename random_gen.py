import pandas as pd
import random
import os
import numpy as np

for sub in range(21, 51):

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

    location = np.random.randint(0, 3, size=18)

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

    for j in location:
        if j == 0:
            locy.append(-400)
            loc2y.append(0)
            loc3y.append(400)
        if j == 1:
            locy.append(0)
            loc2y.append(-400)
            loc3y.append(400)
        if j == 2:
            locy.append(400)
            loc2y.append(0)
            loc3y.append(-400)

    output = {'first_pic': first_pic,
              'second_pic': second_pic,
              'locy': locy,
              'lure1': lure1,
              'loc2y': loc2y,
              'lure2': lure2,
              'loc3y': loc3y,
              'location': location,
              'change': change,
              'key': key}

    output = pd.DataFrame(output)

    data_folder = 'C:/Users/Wanjia/OneDrive - University Of Oregon/Desktop/ContinDiff_js/sub_file'

    output_path = os.path.join(data_folder, 'sub{:02d}.csv'.format(sub))
    output.to_csv(output_path, index=True, index_label='index')
