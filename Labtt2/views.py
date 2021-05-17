from django.shortcuts import render,redirect
from .models import Listing
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from Labtt2.forms import LabForm,UsRgt
from django.contrib.auth.decorators import login_required

@login_required
def usrg(request):
	if request.method == "POST":
		t = UsRgt(request.POST)
		if t.is_valid():
			t.save()
			return redirect('clab/login')
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
