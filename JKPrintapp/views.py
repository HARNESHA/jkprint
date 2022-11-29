from pickletools import read_uint1
from django.shortcuts import redirect, render
from .forms import newuserForm
from .models import newuser

# Create your views here.

def index(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']
        user=newuser.objects.filter(username=unm,password=pas)
        if user:
            print("Login Successfully!")
            return redirect('home')
        else:
            print("Error! Please try again!")
    return render(request,'index.html')

def usersignup(request):
    if request.method=='POST':
        nwuser=newuserForm(request.POST)
        if nwuser.is_valid():
            nwuser.save()
            print("User created successfully!")
            return redirect('home')
        else:
            print(nwuser.errors)
    return render(request,'usersignup.html')



def home(request):
    gm=0.0
    finalpc=0.0
    if request.method=='POST':
        dc=request.POST["decale"]
        cut=request.POST["cutting"]
        gsm=request.POST["gsm"]
        
        x=(int(dc)*int(cut)*int(gsm))/1550
        gm=x/1000
        print("Your First Gram Value:",gm)
        #request.session['gm']=gm

        lin=request.POST["liner"]
        pc=request.POST["pc"]

        ans=gm*int(lin)
        request.session['ans']=ans

        finalpc=ans*int(pc)
        print("Final Paper Cost:",finalpc)
        request.session['finalpc']=finalpc
        return redirect('papercost')
    return render(request,'home.html',{'gm':gm,'finalpc':finalpc})

def papercost(request):
    getpc=0.0
    finalct=request.session.get('finalpc')
    ans=request.session.get('ans')
    if request.method=="POST":
        dc=request.POST["decale"]
        cut=request.POST["cutting"]
        gsm=request.POST["gsm"]
        pc=request.POST["pc"]
        pap=request.POST["paper"]
        
        x=(int(dc)*int(cut)*int(gsm))/1550
        gm=x/1000
        print("Your First Gram Value:",ans)
        print("Your Second Gram Value:",gm)

        print("Both Gram:",ans+gm)

        lc=ans+gm
        final_lc=lc*6
        request.session['final_lc']=final_lc
        print("Final LC:",final_lc)

        finalpc=gm*int(pc)
        getpc=finalpc*int(pap)
        print("Final Paper Cost:",getpc)

      

        ans=float(finalct)+float(getpc)
        print("Total:",ans)
        request.session['ans']=ans
        return redirect('final')
    return render(request,'papercost.html',{'finalct':finalct,'getpc':getpc})

def final(request):
    total_pr=0.0
    fc=0.0
    final_cost=0.0
    final_lc=request.session.get('final_lc')
    ans=request.session.get('ans')
    total=ans+final_lc

    if request.method=="POST":
        pr=request.POST["pr"]
        qu=request.POST["qu"]

        total_pr=float(total)*float(pr)
        print("Total PR:",total_pr)
        cost=total_pr+total
        print("Cost:",cost)
        final_cost=float(qu)*float(cost)
        print("Final Cost:",final_cost)
    return render(request,'final.html',{'ans':ans,'total':total,'total_pr':total_pr,'fc':final_cost})