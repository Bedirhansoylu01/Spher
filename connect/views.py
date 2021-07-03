from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.conf import settings
from django.utils.http import is_safe_url
#from django.contrib.auth.models import User
# internal fs
from .forms import shareForm


def home(request, *args, **kwargs):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    return render(request, "pages/home.html", context={"username": username}, status=200)


def spher_list_view(request, *args, **kwargs):
    return render(request, "components/list.html")


def spher_detail_view(request, share_id, *args, **kwargs):
    return render(request, "components/detail.html", context={'share_id': share_id})


def shareView_Django_Form(request, *args, **kwargs):
    #________________Check in Authenticated User_______________________________________________#
    if not request.user.is_authenticated:
        if request.is_ajax():
            return JsonResponse({}, status=401)
        return redirect(settings.LOGIN_URL)
# ___________________________________________________________________________________
    form = shareForm(request.POST or None)
    next_url = request.POST.get("next") or None

    if form.is_valid():
        obj = form.save(commit=False)
        # _____________Associate Authenticated User to Object___________________#
        obj.user = request.user
        obj.save()

        if request.is_ajax():
            return JsonResponse(obj.serialize(), status=201)
        if next_url != None and is_safe_url(next_url, settings.ALLOWED_HOSTS):
            return redirect(next_url)

        return redirect("/")

    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status=400)
    context = {"form": shareForm(),
               "title": " Share",
               'btn': 'commit'}
    return render(request, "pages/form.html", context)
