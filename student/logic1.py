import numpy as np
import pandas as pd
from .models import Student
def load_data():
    df=pd.read_csv('static/lol.csv')
    return df[:61]


grade_dict = { 'A': ['Congratulations! You\'re rocking it!! Keep up the good work!',
                     'Ah, this is perfection. Well done! Keep it up!'
                    'Thats the way! Feel proud of yourself, you\'re doing GREAT!',
                    'Bravo!! Encore!! Your hard work has clearly paid off!'],
              'B': ['You have done well. Your efforts are clearly seen. But, I know you can still do better. Just a little more refinement till absolute perfection!!',
                   'Going really good! Just a teensy bit more till you get there!!',
                   '2 Steps to be done: 1. Pat Yourself on the back for making this far. 2. Continue on the same road, climb to the peak!!',
                   'Very good! Work just a little bit more to excellence!!'],
               'C': ['You\'re doing okay. But thats the problem: Youre "okay". Not great. Dont Worry, you can still get better! Use the links below, help yourself get back on track',
                    'Hey, Need some improvement here! Dont worry, Use the links below, get yourself back on track. We still have some time, do we not?',
                    'Satisfactory. We need to do better, as we know you can do better. Come on! Lets push oursleves harder!',
                    'Use the links, get yourself better, work even harder, and get there! Lets do it!!'],
               'D': ['Woah there! That\'s not good at all! We really need you to get better. Use the links to improve. Its high time we started the grinding!!',
                    'Hey, now that\'s not cool. Please work harder, you HAVE to improve here. You can do it! Use the links below, get an idea, and start working!!',
                    'Man..... Something went wrong here. This is really unexpected of you. Please try harder. Use the links, find a way, get better!!',
                    'No, no noo! That\'s not how you roll. Something must have gone wrong. Find a groove that works for you, and get this lap back! Use the links, help yourself. You really need to.']
             }
tot_mks = {'am_tot':100,
          'ap_tot': 75,
          'ac_tot': 75,
          'ed_tot': 75,
          'spa_tot': 100,
          'cs_tot' : 60,
          'ws_tot' : 50}


def analysis(uid,sub):
    df = load_data()
    df1 = df[df['UID']==uid]
    sub_tot = tot_mks[sub]
    p = (list(df1[sub])[0]*100)/sub_tot
    if p>80:
        grade = 'A'
    elif p>60 and p<=80:
        grade = 'B'
    elif p>40 and p<=60:
        grade = 'C'
    else:
        grade = 'D'
    return grade_dict[grade][np.random.randint(0,3)]

def dict_out():
    df=load_data()
    df_entries = []
    for i in range(len(df)):
        entry_dict = {}
        for j in list(df.columns):
            entry_dict[j] = df[j][i]
        df_entries.append(entry_dict)
    return df_entries


def geti(request):
    df = load_data()
    a= request.user.username
    for i in range(len(df)):
        if str(df['UID'][i]) == a:
            break
    return i,df

def analysis2(request):

    i,df=geti(request)
    sub_tot = sum(list(tot_mks.values()))
    mks_tot = list(df[['am_tot','ap_tot','ac_tot','ed_tot','spa_tot','cs_tot']].sum(axis=1))[i]
    p = mks_tot*100/sub_tot
    if p>75:
        grade = 4
    elif p>60 and p<=75:
        grade = 3
    elif p>50 and p<=60:
        grade = 2
    else:
        grade = 1
    return grade
