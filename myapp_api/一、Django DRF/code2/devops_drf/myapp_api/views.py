from .serializers import UserSerializer, ProjectSerializer, AppSerializer, ServerSerializer, TestSerializer
from myapp_api.models import User, Project, App, Server
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ViewSet, ModelViewSet

class UserView(APIView):
    def get(self, request, pk=None):
        if pk:
            print(request.query_params)
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
        result = {'code': 200, 'msg': "查询成功", 'data': ser.data}
        return Response(result)
    def post(self, request):
        print(request.data.get('name'))
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

class TestView(GenericAPIView):
    queryset = User.objects.all() # 指定操作的数据，在下面用
    serializer_class = TestSerializer  # 指定序列化器
    lookup_field = 'id'  # 指定分组名称

    def get(self, request, id=None):
        if id:
            user_obj = self.get_object()  # 从列方法调用指定数据（默认根据pk）
            ser = self.get_serializer(instance=user_obj)  # 从类方法调用序列化器
        else:
            queryset = self.get_queryset()  #  从类方法调用数据
            ser = self.get_serializer(instance=queryset, many=True)  # 从类方法调用序列化器
        result = {'code': 200, 'msg': "查询成功", 'data': ser.data}
        return Response(result)

    def put(self, request, id=None):
        user_obj = self.get_object()
        ser = self.get_serializer(instance=user_obj, data=request.data)
        ser.is_valid(raise_exception=True)
        ser.save()
        result = {'code': 200, 'msg': "更新成功"}
        return Response(result)

"""
class Test2View(ViewSet):
    def retrieve(self, request, pk=None):
        return Response("列出单个数据")
    def list(self, request, pk=None):
        return Response("列出所有数据")
    def create(self, request, pk=None):
        return Response("创建")
    def update(self, request, pk=None):
        return Response("更新")
    def destory(self, request, pk=None):
        return Response("删除")
"""


class Test2View(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # 视图级别认证
    # from rest_framework.authentication import TokenAuthentication
    # from rest_framework.permissions import IsAuthenticated
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    from django_filters.rest_framework import DjangoFilterBackend

    # 搜索和排序
    from rest_framework import filters
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend] # 指定过滤器
    search_fields = ('name',)
    ordering_fields = ('age',)

    # 过滤
    filter_fields = ('name','sex',)

    # # 重写创建方法
    def create(self, request, *args, **kwargs):
        print(request.data)
        request.data['age'] += 1
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        result = {'code': 200, 'msg': "创建成功"}
        return Response(result)

    # # 重写获取所有数据方法
    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     result = {'code': 200, 'msg': "创建成功", 'data': serializer.data}
    #     return Response(result)

