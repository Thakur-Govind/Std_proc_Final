
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import Http404, JsonResponse
from django.forms.utils import ErrorList
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import django
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import io
import matplotlib.pyplot as plt;plt.rcdefaults()
import urllib
import requests
from .logic1 import *
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import preprocessing as p

def home(request):
    student=Student()
    di=dict_out()

    for i in di:
        student.name = i['Name']
        student.uid = i['UID']
        student.extra_curr=i['extra_c']
        student.co_curr=i['co_c']

        student.sub_name1="Applied Mathematics-2"
        student.sub_name2="Applied Physics-2"
        student.sub_name3="Applied Chemistry-2"
        student.sub_name4="Engineering Drawing"
        student.sub_name5="Structured Programming Approach"
        student.sub_name6="Communication Skills"

        student.total1=i['am_tot']
        student.total2=i['ap_tot']
        student.total3=i['ac_tot']
        student.total4=i['ed_tot']
        student.total5=i['spa_tot']
        student.total6=i['cs_tot']

        student.theory1=i['am_th']
        student.theory2=i['ap_th']
        student.theory3=i['ac_th']
        student.theory4=i['ed_th']
        student.theory5=i['spa_th']
        student.theory6=i['cs_th']

        student.internal1=i['am_th']
        student.internal2=i['ap_th']
        student.internal3=i['ac_th']
        student.internal4=i['ed_th']
        student.internal5=i['spa_th']
        student.internal6=i['cs_th']
        student.tot_excc=i['tot_ex_cc']

        student.save()
        df = load_data()
        a = request.user.username
        for i in range(len(a)):
            if a[i] =='':
                a.remove('')
        for i in range(len(df)):
            if str(df['UID'][i]) == a:
                break
        name = df['Name'][i]
        math = df['am_tot'][i]
        phy = df['ap_tot'][i]
        chem = df['ac_tot'][i]
        ed = df['ed_tot'][i]
        spa = df['spa_tot'][i]
        cs = df['cs_tot'][i]

    return render(request,'student/home.html',{ 'uid': request.user.username, 'name':name, 'math': math, 'phy': phy, 'chem': chem,'spa':spa, 'ed':ed, 'cs':cs })

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('dashboard')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view

def maths (request):
    i,df=geti(request)
    p = df['am_tot'][i]*100 /tot_mks['am_tot']
    advice = analysis(df['UID'][i],'am_tot')
    return render(request, 'student/maths.html', {'theo': df['am_th'][i], 'int': df['am_in'][i], 'tot': df['am_tot'][i], 'per':p, 'adv': advice})
def phy (request):
    i,df=geti(request)
    p = df['ap_tot'][i]*100 /tot_mks['ap_tot']
    advice = analysis(df['UID'][i],'ap_tot')
    return render(request, 'student/phy.html', {'theo': df['ap_th'][i], 'int': df['ap_in'][i], 'tot': df['ap_tot'][i], 'per':p, 'adv': advice})
def chem (request):
    i,df=geti(request)
    p = df['ac_tot'][i]*100 /tot_mks['ac_tot']
    advice = analysis(df['UID'][i],'ac_tot')
    return render( request, 'student/chem.html', {'theo': df['ac_th'][i], 'int': df['ac_in'][i], 'tot': df['ac_tot'][i], 'per':p, 'adv': advice})
def ed (request):
    i,df=geti(request)
    p = df['ed_tot'][i]*100 /tot_mks['ed_tot']
    advice = analysis(df['UID'][i],'ed_tot')
    return render( request, 'student/ed.html', {'theo': df['ed_th'][i], 'int': df['ed_in'][i], 'tot': df['ed_tot'][i], 'per':p, 'adv': advice})
def spa (request):
    i,df=geti(request)
    p = df['spa_tot'][i]*100 /tot_mks['spa_tot']
    advice = analysis(df['UID'][i],'spa_tot')
    return render( request, 'student/spa.html', {'theo': df['spa_th'][i], 'int': df['spa_in'][i], 'tot': df['am_tot'][i], 'per':p, 'adv': advice})
def cs (request):
    i,df=geti(request)
    p = df['cs_tot'][i]*100 /tot_mks['cs_tot']
    advice = analysis(df['UID'][i],'cs_tot')
    return render( request, 'student/cs.html', {'theo': df['cs_th'][i], 'int': df['cs_in'][i], 'tot': df['cs_tot'][i], 'per':p, 'adv': advice})


def extra(request):
    i,df=geti(request)
    if df['tot_ex_cc'][i] =='none' and analysis2(request) >=3:
               advice= "Though you may be doing well in academics, you should also indulge in some extracurricular activities that might benifit you. Remember: ALL WORK AND NO PLAY MAKES JACK A DULL BOY. For an instance, you could try Basketball, Dancing, Swimming, or Music(singing or playing).Do find something of your interest, and maintain it as a hobby."
    elif df['tot_ex_cc'][i] =='none' and analysis2(request)  <=3:
               advice= "You dont have great marks as well. Take a hint! Maybe not doing any extras is a cause. Or maybe you're just not focused."
    elif df['tot_ex_cc'][i] !='none' and analysis2(request)  <=3:
              advice= "It seems you have been able to balance your academics and extras very well Great Job, Keep it Up!!!!"
    else:
              advice= "Whoa! You may have active in extras, and that's good! really! However, your marks are not that great. Maybe just dial down this side for a bit, and focus more on your credits?I think its high time for that."
    return render(request, 'student/eccc.html', {'EC': df['extra_c'][i], 'CC': df['co_c'][i], 'count':df['tot_ex_cc'][i], 'advice': advice})


def plotbar(request):
    sub = 'am_tot'
    fig = Figure()
    canvas = FigureCanvas(fig)
    df = load_data()
    a = request.user.username
    for i in range(len(a)):
        if a[i] =='':
            a.remove('')
    for i in range(len(df)):
        if str(df['UID'][i]) == a:
            break
    sub_tot = tot_mks[sub]
    sub_avg = df[sub].mean()
    sub_max = df[sub].max()
    sub_mks = df[sub][i]

    plt.bar(['Total Marks','Average Marks','Highest Marks','Your marks'],[sub_tot,sub_avg,sub_max,sub_mks])
    #plt.show()
    buf = io.BytesIO()
    abc={}
    plt.savefig(buf, format = 'png')
    return render(request, 'student/graph.html', abc)

def kmeans ():
    df=load_data()
    data = pd.DataFrame()
    data['tot_ex_cc'] = df['tot_ex_cc']
    data['total_marks']= tot_marks
    kmeans = KMeans(3)
    labels = kmeans.fit_predict(data) #fit kmeans to get the labels
    # Plot the original data with clusters
    fig,ax = plt.subplots()
    ax.scatter(data['tot_ex_cc'], data['total_marks'], c=labels, cmap='Set1')
    plt.scatter(data['tot_ex_cc'][10], data['total_marks'][10], c ="blue")
    plt.legend(['you'])
    plt.show()
