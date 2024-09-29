from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import TgUser, AgentId
from django.core.files.storage import FileSystemStorage
import asyncio
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required


async def acreate_person(tg_url, tg_name, name, photo, description, agent_name):
    person = await TgUser.objects.acreate(tg_url=tg_url, tg_name=tg_name, name=name, photo=photo,
                                          description=description, agent_name=agent_name)
    print(person.name)


@csrf_exempt
def tguser(request):
    if request.method == "POST":
        tg_url = request.POST.getlist('tg_url', default="unknown")[0]
        tg_name = request.POST.getlist('tg_name', default="unknown")[0]
        name = request.POST.getlist('name', default="unknown")[0]
        description = request.POST.getlist('description', default="unknown")[0]
        agent_name = request.POST.getlist('agent_name', default="unknown")[0]
        fs = FileSystemStorage()
        file = request.FILES['photo']
        file_url = fs.url(fs.save(file.name, file))
        asyncio.run(acreate_person(tg_url, tg_name, name, file_url, description, agent_name))
        return HttpResponse(200)
    else:
        id_agent = request.GET.getlist('ID', default="unknown")[0]
        id_agents = AgentId.objects.all()
        for i in range(len(id_agents)):
            if str(id_agent) == str(id_agents[i].id):
                return HttpResponse(200)
        return HttpResponse(403)


class View_tgusers(View):
    @method_decorator(permission_required(perm='telebot.view_tg_users', raise_exception=True), name='dispatch')
    def get(self, request):
        data = ""
        HttpResponse(request.user.is_authenticated + ", " + request.user.username)
        # получаем все значения модели
        if request.user.is_authenticated:
            id_agent = request.user.username
            data = TgUser.objects.filter(agent_name=id_agent)
        return render(request, 'home_telebot.html', {'data': data})