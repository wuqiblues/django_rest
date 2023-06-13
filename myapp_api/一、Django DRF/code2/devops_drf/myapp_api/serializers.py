from myapp_api.models import User, Project, App, Server
from rest_framework import serializers

"""
# 自定义验证器
def check_name(data):
    if data.startswith('x'):
        raise serializers.ValidationError('姓名不能以x开头！')
    return data

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20, validators=[check_name],
                                 error_messages={
                                     "blank": "请输入姓名",
                                     'required': "该字段必填",
                                     'max_length': '字段长度不超过20'
                                 })
    city = serializers.CharField(max_length=20)
    sex = serializers.CharField(max_length=10)
    age = serializers.IntegerField(min_value=16, max_value=100,
                                   error_messages={
                                       "blank": "请输入年龄",
                                       'required': "该字段必填",
                                       'min_value': '年龄不低于16岁',
                                       'max_value': '年龄不高于100岁',
                                   })

    # 重写create()方法实现入库
    def create(self, validated_data): # validated_data反序列化后的数据
        return User.objects.create(**validated_data)

    # 重写create()方法实现更新库
    def update(self, instance, validated_data):# instance当前操作的用户对象，validated_data反序列化后的数据
        instance.name = validated_data.get('name')
        instance.city = validated_data.get('city')
        instance.sex = validated_data.get('sex')
        instance.age = validated_data.get('age')
        instance.save()
        return instance

    # 局部钩子：validate_字段名
    def validate_sex(self, attrs): # attrs是sex字段的值
        if attrs == "男" or attrs == "女":
            return attrs
        else:
            raise serializers.ValidationError("性别不能是人妖！")

    # 全局钩子
    def validate(self, attrs):
        # 姓名不能包含数字
        from re import findall
        if findall('\d+', attrs.get('name')):
            raise serializers.ValidationError("姓名不能包含数字！")
        return attrs
"""

class UserSerializer(serializers.ModelSerializer):
    """
    用户表序列化器
    """
    class Meta:
        model = User  # 指定关联的模型
        fields = "__all__" # 显示所有字段
        # fields = ('name', 'city', 'sex')
        # exclude = ('age',) # 排除不显示的字段，这个不能与fields一起用
        extra_kwargs = {
            'name': {'max_length': 20, 'required': True},
            'age': {'min_value': 16, 'max_value': 100}
        }

class ProjectSerializer(serializers.ModelSerializer):
    app_count = serializers.SerializerMethodField() # 增加一个统计项目下关联的app数量的字段
    class Meta:
        model = Project  # 指定关联的模型
        fields = "__all__" # 显示所有字段
    # 格式：get_字段名
    def get_app_count(self, obj):  # obj 是当前project的对象
        # 如何通过project对象获取关联的所有app？ 反向查询
        return len(obj.app_set.all())

    # 效验前处理数据
    def to_internal_value(self, data):  # data 提交的数据
        project_data = data['project']
        return super().to_internal_value(project_data)  # 把正确的数据格式再传给to_internal_value

    # 响应前处理
    def to_representation(self, instance):
        data = super().to_representation(instance) # 获取要返回数据
        data['app_count2'] = len(instance.app_set.all())  # 增加一个统计app数量的字段
        return data

class AppSerializer(serializers.ModelSerializer):
    project = ProjectSerializer(read_only=True)  # 一对多，显示详情
    class Meta:
        model = App  # 指定关联的模型
        fields = "__all__" # 显示所有字段
        # depth = 1

class ServerSerializer(serializers.ModelSerializer):
    app = AppSerializer(read_only=True, many=True)  # 多对多
    class Meta:
        model = Server  # 指定关联的模型
        fields = "__all__" # 显示所有字段
        # depth = 2


class TestSerializer(serializers.ModelSerializer):
    """
    用户表序列化器
    """
    class Meta:
        model = User  # 指定关联的模型
        fields = "__all__" # 显示所有字段