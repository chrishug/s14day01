from django.shortcuts import render,HttpResponse,redirect
from app01 import models
# Create your views here.

def index(request):
    if request.method == "GET":
        user_list = models.UserInfo.objects.all()
        group_list = models.Group.objects.all()
        return render(request, 'index.html', {'user_list': user_list, "group_list":group_list })
    elif  request.method == "POST":
        u = request.POST.get("user")
        p = request.POST.get("pwd")
        e = request.POST.get("email")
        g = request.POST.get("group_id")
        models.UserInfo.objects.create(username=u, password=p, email=e, group_id=g)
    return redirect("/index")

# def user_detail(request, nid):
def user_detail(request, *args,**kwargs):
    if request.method == "GET":
        user_info = models.UserInfo.objects.filter(id=kwargs['nid']).first()
        return render(request, 'user_detail.html', {"user_info":user_info})

def user_del(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/index")

def user_edit(request,nid):
    if request.method == "GET":
        group_list = models.Group.objects.all()
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request, 'user_edit.html', {'obj':obj,"group_list":group_list})
    elif request.method == "POST":
        id = request.POST.get("id")
        u = request.POST.get("user")
        p = request.POST.get("pwd")
        e = request.POST.get("email")
        g = request.POST.get("group_id")
        print(nid,u,p,e,g)
        models.UserInfo.objects.filter(id=id).update(username=u, password=p, email=e, group_id=g)
        return redirect("/index")