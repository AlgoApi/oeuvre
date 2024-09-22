from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import TgUser, AgentId
from django.core.files.storage import FileSystemStorage
import asyncio
import rsa
import ast
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required


async def acreate_person(tg_url, tg_name, name, photo, description):
    person = await TgUser.objects.acreate(tg_url=tg_url, tg_name=tg_name, name=name, photo=photo,
                                          description=description)
    print(person.name)


@csrf_exempt
def tguser(request):
    if request.method == "POST":
        tg_url = request.POST.getlist('tg_url', default="unknown")[0]
        tg_name = request.POST.getlist('tg_name', default="unknown")[0]
        name = request.POST.getlist('name', default="unknown")[0]
        description = request.POST.getlist('description', default="unknown")[0]
        fs = FileSystemStorage()
        file = request.FILES['photo']
        file_url = fs.url(fs.save(file.name, file))
        asyncio.run(acreate_person(tg_url, tg_name, name, file_url, description))
        return HttpResponse(200)
    else:
        with open("/home/AlgoApiRubin/oeuvre/telebot/pubServer.pem", "rb") as f:
            pubkeyC = rsa.PublicKey.load_pkcs1(f.read())

        with open("/home/AlgoApiRubin/oeuvre/telebot/privServer.pem", "rb") as f:
            privkeyC = rsa.PrivateKey.load_pkcs1(f.read())

        id_agent = request.GET.getlist('ID', default="unknown")[0]
        return HttpResponse(id_agent)
        clear_id_agent = rsa.decrypt(ast.literal_eval(id_agent), privkeyC).decode()
        mode = request.GET.getlist('mode', default="unknown")[0]
        id_agents = AgentId.objects.all()
        for i in range(len(id_agents)):
            if str(clear_id_agent) == str(id_agents[i].id):
                if mode == "all":
                    api_id = '20427673'
                    api_hash = '046f9b91f1158d77b8d9765c00849b82'
                    raw_token = ('github_pat_11AOWETKY05iTCa7OXHMaW_nTz6Shj9bElVZB2LCnAr2yslUNHE7MXKOnb16ZSVGpFIHDDHGTI'
                                 'crP1TZl7')
                    return HttpResponse(headers={"code": 200, "api_id": rsa.encrypt(api_id.encode(), pubkeyC),
                                                 "api_hash": rsa.encrypt(api_hash.encode(), pubkeyC),
                                                 "raw_token": rsa.encrypt(raw_token.encode(), pubkeyC)})
        return HttpResponse(403)


class View_tgusers(View):
    @method_decorator(permission_required(perm='telebot.view_tg_users', raise_exception=True), name='dispatch')
    def get(self, request):
        # получаем все значения модели
        data = TgUser.objects.all()
        return render(request, 'home_telebot.html', {'data': data})
