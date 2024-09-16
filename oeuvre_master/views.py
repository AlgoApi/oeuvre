from django.views import View
from django.http import HttpResponse
from django.shortcuts import render,redirect
import git

class Home(View):
    def post(self, request):
        return HttpResponse(0)

    def get(self, request):
        return render(request, 'home.html')


class Update(View):
    def post(self, request):
        repo = git.Repo('https://github.com/AlgoApi/oeuvre')
        origin = repo.remotes.origin
        origin.pull()
        return HttpResponse(200)

    def get(self, request):
        return redirect('/')
