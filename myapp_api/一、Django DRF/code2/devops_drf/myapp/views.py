from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myapp.models import User
from django.http import QueryDict

from django.views.generic import View

# 用户操作接口
"""
def user(request):
    if request.method == "GET":
        return HttpResponse('获取用户')
    elif request.method == "POST":
        name = request.POST.get('name')
        city = request.POST.get('city')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        User.objects.create(
            name=name,
            city=city,
            sex=sex,
            age=age
        )
        result = {'code': 200, 'msg': '创建用户成功'}
        return JsonResponse(result)
    elif request.method == "PUT":
        data = QueryDict(request.body)
        print(data.get('id'))
        id = data.get('id')
        # 用户更新
        user_obj = User.objects.get(id=id)
        user_obj.name = data.get('name')
        user_obj.city = data.get('city')
        user_obj.sex = data.get('sex')
        user_obj.age = data.get('age')
        user_obj.save()
        result = {'code': 200, 'msg': '更新用户成功'}
        return JsonResponse(result)
    elif request.method == "DELETE":
        # 根据用户id删除记录
        data = QueryDict(request.body)
        id = data.get('id')
        User.objects.get(id=id).delete()
        result = {'code': 200, 'msg': '删除用户成功'}
        return JsonResponse(result)
"""

class UserView(View):
    def get(self, request):
        return HttpResponse('获取用户')
    def post(self, request):
        name = request.POST.get('name')
        city = request.POST.get('city')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        User.objects.create(
            name=name,
            city=city,
            sex=sex,
            age=age
        )
        result = {'code': 200, 'msg': '创建用户成功'}
        return JsonResponse(result)

    def put(self, request):
        data = QueryDict(request.body)
        print(data.get('id'))
        id = data.get('id')
        # 用户更新
        user_obj = User.objects.get(id=id)
        user_obj.name = data.get('name')
        user_obj.city = data.get('city')
        user_obj.sex = data.get('sex')
        user_obj.age = data.get('age')
        user_obj.save()
        result = {'code': 200, 'msg': '更新用户成功'}
        return JsonResponse(result)

    def delete(self, request):
        # 根据用户id删除记录
        data = QueryDict(request.body)
        id = data.get('id')
        User.objects.get(id=id).delete()
        result = {'code': 200, 'msg': '删除用户成功'}
        return JsonResponse(result)

# 显示用户界面
def user_list(request):
    user_list = User.objects.all()
    return render(request, 'user_list.html', {'user_list': user_list})
# 创建用户页面
def user_add(request):
    return render(request, 'user_add.html')
# 编辑用户页面
def user_edit(request):
    id = request.GET.get('id')
    user_obj = User.objects.get(id=id)
    return render(request, 'user_edit.html', {'user': user_obj})


from django.core import serializers
def json_test(request):
    # user_obj = User.objects.all()
    # result = serializers.serialize('json', user_obj)
    computer = {'主机': 5000, '显示器': 1000}
    return JsonResponse(computer)