from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import TgUser, AgentId
from django.core.files.storage import FileSystemStorage
import asyncio
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
        id_agent = request.GET.get('ID')
        id_agents = AgentId.objects.all()
        for i in id_agents:
            if int(id_agent) == int(id_agents[i].id_agent):
                return HttpResponse(200)
        return HttpResponse(403)


class View_tgusers(View):
    @method_decorator(permission_required(perm='telebot.view_tg_users', raise_exception=True), name='dispatch')
    def get(self, request):
        # получаем все значения модели
        data = TgUser.objects.all()
        return render(request, 'home_telebot.html', {'data': data})
