from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from django.utils.http import is_safe_url
from django.contrib.auth.models import User
#rest_framework
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated 
#internal fs
from .models import share
from .forms import shareForm
from .serializers import ShareSerializer_GET,ShareSerializer_POST


def home(request, *args, **kwargs):
    return render(request, "pages/home.html")


@api_view(['POST'])
#@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def shareView(request, *args, **kwargs):
    serializer = ShareSerializer_POST(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        serial=serializer.save(user=request.user)        
        serial_1=ShareSerializer_GET(serial).data
        serial_1["user"]=request.user.username
        return Response(serial_1, status=201)
    return Response({}, status=400)
    
@api_view(['GET'])
def commit_list(request, *args, **kwargs):
    qs = share.objects.all()
    serializer = ShareSerializer_GET(qs, many=True) #many=True for mutiple object
    for serial in serializer.data:
        serial["user"] = User.objects.get(id=serial["user"]).username
    return Response(serializer.data, status=200)


@api_view(['GET'])
def commit_detail(request, share_id, *args, **kwargs):

    qs = share.objects.filter(id=share_id)
    if not qs.exists():
        return Response({}, status=404)
    obj = qs.first()
    serializer = ShareSerializer(obj)
    return Response(serializer.data, status=200)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def commit_delete(request,pk,*args,**kwargs):
    qs=share.objects.filter(id=pk)
    if not qs.exists():
        return Response({},status=404) 
    qs=qs.filter(user=request.user)
    if not qs.exists():
        return Response({'message':'You do not have permission for delete this commit'},status=401)
    qs.delete()
    return Response({'message':'Commit removed'},status=200)   













def shareView_Django_Form(request, *args, **kwargs):
#________________Check in Authenticated User_______________________________________________#
    if not request.user.is_authenticated:
        if request.is_ajax():
            return JsonResponse({}, status=401)
        return redirect(settings.LOGIN_URL)
# ___________________________________________________________________________________
    form = shareForm(request.POST or None)
    next_url=request.POST.get("next")or None
    
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user= request.user #_____________Associate Authenticated User to Object___________________#
        obj.save()

        if request.is_ajax():
            return JsonResponse(obj.serialize(),status=201)
        if next_url!= None and is_safe_url(next_url,settings.ALLOWED_HOSTS):
            return redirect(next_url)
        
        return redirect("/")     
    
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors,status=400)    

    return render(request, "pages/form.html", {"form": shareForm(),"title":" Share"})


