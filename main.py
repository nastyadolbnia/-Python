#import random
#lst = ['robot'] * 10
#lst += ['human'] * 10
#random.shuffle(lst)
#data = pd.DataFrame({'whoAmI'lst})
#data.head()

import pandas as pd

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})

data['isRobot'] = data['whoAmI'].apply(lambda x: 1 if x == 'robot' else 0)
data['isHuman'] = data['whoAmI'].apply(lambda x: 1 if x == 'human' else 0)

data.head()



