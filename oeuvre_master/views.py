from django.views import View
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
import git

class Home(View):
    def post(self, request):
        return HttpResponse(0)

    def get(self, request):
        return render(request, 'home.html')

@csrf_exempt
def update(request):
    if request.method == "POST":
        '''
        pass the path of the diectory where your project will be
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "test.pythonanywhere.com"
        '''
        repo = git.Repo("oeuvre")
        origin = repo.remotes.origin
        repo.create_head('master', origin.refs.master).set_tracking_branch(origin.refs.master).checkout()
        origin.pull(force=True)

        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("access denied11")

