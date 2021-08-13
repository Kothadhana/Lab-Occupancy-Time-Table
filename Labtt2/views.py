from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Listing
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from Labtt2.forms import LabForm,UsRgt
from django.contrib.auth.decorators import login_required
def search(request):
	res=""
	if request.method=='POST':
		lab=request.POST["lab"]
		day=request.POST["day"]
		day+=request.POST["session"]
		form=Listing.objects.get(id=lab)
		if (day=="monm"):
			res=form.monm
		elif(day=="mone"):
			res=form.mone
		elif(day=="tuem"):
			res=form.tuem
		elif(day=="tuee"):
			res=form.tuee
		elif(day=="wedm"):
			res=form.wedm
		elif(day=="wede"):
			res=form.wede
		elif(day=="thum"):
			res=form.thum
		elif(day=="thue"):
			res=form.thue
		elif(day=="frim"):
			res=form.frim
		elif(day=="frie"):
			res=form.frie
		elif(day=="satm"):
			res=form.satm
		elif(day=="sate"):
			res=form.sate
		forms=Listing.objects.all()
		if(res==None or res==""):
			return render(request,'demo/search.html',{'forms':forms,'no':day });
		else:
			return render(request,'demo/search.html',{'forms':forms,'msg':res});
		#return render(request,'demo/search.html', message='Save complete')
		#if (form.day=="None" or form.day==""):
			#messages.info(request, 'Lab is Vacant')
		#else:
			#messages.danger(request, 'Lab is occupied by form.day')
		#return render('demo/search.html', message='res')
		#return redirect('search')
		#forms=Listing.objects.all()
		#return render(request,'demo/search.html',{'forms':forms});
	#else:
	forms=Listing.objects.all()
	return render(request,'demo/search.html',{'forms':forms});
@login_required
def regd(request):
	return(request,'demo/registered.html')
@login_required
def usrg(request):
	if request.method == "POST":
		t = UsRgt(request.POST)
		if t.is_valid():
			t.save()
			return render(request,'demo/registered.html')
	t = UsRgt()
	return render(request,'demo/registration.html',{'y':t})
def home(request):
    forms=Listing.objects.all()
    return render(request,'demo/home.html',{'forms':forms})
def central(request):
    forms=Listing.objects.all()
    return render(request,'demo/central.html', {'forms': forms})
@login_required
def add_new(req):
	if req.method=="POST":
		form=LabForm(req.POST)
		if form.is_valid():
			form.save()
		forms=Listing.objects.all()
		return render(req,'demo/central.html',{'forms':forms})
	return render(req,'demo/add.html')

def view_select(request,id):
    form=Listing.objects.get(id=id)
    return render(request,'demo/select.html',{'form':form})
@login_required
def delete(request,id):
    form=Listing.objects.get(id=id)
    form.delete()
    forms=Listing.objects.all()
    return render(request,'demo/central.html',{'forms':forms})
@login_required
def update(request,id):
    form=Listing.objects.get(id=id)
    if request.method=='POST':
        obj=LabForm(request.POST)
        if obj.is_valid():
            form.lab_name=request.POST["lab_name"].upper()
            form.systems=request.POST["systems"]
            form.monm=request.POST["monm"]
            form.mone=request.POST["mone"]
            form.tuem=request.POST["tuem"]
            form.tuee=request.POST["tuee"]
            form.wedm=request.POST["wedm"]
            form.wede=request.POST["wede"]
            form.thum=request.POST["thum"]
            form.thue=request.POST["thue"]
            form.frim=request.POST["frim"]
            form.frie=request.POST["frie"]
            form.satm=request.POST["satm"]
            form.sate=request.POST["sate"]
            form.save()
            forms=Listing.objects.all()
            return render(request,'demo/central.html',{'forms':forms})
        return render(request,'demo/update.html',{'form':form})
