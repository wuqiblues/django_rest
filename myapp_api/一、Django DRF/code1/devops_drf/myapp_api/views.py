from .serializers import UserSerializer, ProjectSerializer, AppSerializer, ServerSerializer
from myapp_api.models import User, Project, App, Server
from rest_framework.views import APIView
from rest_framework.response import Response

class UserView(APIView):
    def get(self, request, pk=None):
        if pk:
            # 获取单个用户
            user_obj = User.objects.get(id=pk)
            # 调用序列化器将queryset对象转换为json
            ser = UserSerializer(user_obj)
        else:
            # 获取所有用户
            queryset = User.objects.all()
            # 调用序列化器将queryset对象转换为json
            ser = UserSerializer(queryset, many=True) # 如果有多条数据，指定many=True
        # 从.data属性获取序列化结果
        return Response(ser.data)
    def post(self, request):
        print(request.data)
        # 调用序列化器将提交的数据进行反序列化
        ser = UserSerializer(data=request.data)
        ser.is_valid(raise_exception=True) # 如果格式不正确返回400状态并明确错误
        ser.save()
        # if ser.is_valid():
        #     ser.save()  # 调用的create()方法
        #     msg = "创建用户成功"
        #     code = 200
        # else:
        #     msg = "提交的数据格式错误！"
        #     code = 400
        result = {'code': 200, 'msg': "创建用户成功"}
        return Response(result)
    def put(self, request, pk=None):
        user_obj = User.objects.get(id=pk)
        # 调用序列化器，将提交的数据进行反序列化
        ser = UserSerializer(instance=user_obj, data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        # if ser.is_valid():
        #     ser.save()  # 调用的update()方法
        #     msg = "更新用户成功"
        #     code = 200
        # else:
        #     msg = "提交的数据格式错误！"
        #     code = 400
        result = {'code': 200, 'msg': "创建用户成功"}
        return Response(result)
    def delete(self, request, pk=None):
        try:
            User.objects.get(id=pk).delete()
            msg = "删除用户成功"
            code = 200
        except Exception as e:
            msg = "删除用户失败：%s" %e
            code = 400
        result = {'code': code, 'msg': msg}
        return Response(result)

class ProjectView(APIView):
    def get(self, request):
        queryset = Project.objects.all()
        ser = ProjectSerializer(queryset, many=True)
        result = {'code': 200, 'msg': "获取成功", 'data': ser.data}
        return Response(result)
    def post(self, request):
        ser = ProjectSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        result = {'code': 200, 'msg': "创建成功"}
        return Response(result)
    def put(self, request):
        pass
    def delete(self, request):
        pass

class AppView(APIView):
    def get(self, request):
        queryset = App.objects.all()
        ser = AppSerializer(queryset, many=True)
        result = {'code': 200, 'msg': "获取成功", 'data': ser.data}
        return Response(result)
    def post(self, request):
        ser = AppSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        result = {'code': 200, 'msg': "创建成功"}
        return Response(result)
    def put(self, request):
        pass
    def delete(self, request):
        pass

class ServerView(APIView):
    def get(self, request):
        queryset = Server.objects.all()
        ser = ServerSerializer(queryset, many=True)
        result = {'code': 200, 'msg': "获取成功", 'data': ser.data}
        return Response(result)
    def post(self, request):
        ser = ServerSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        result = {'code': 200, 'msg': "创建成功"}
        return Response(result)
    def put(self, request):
        pass
    def delete(self, request):
        pass