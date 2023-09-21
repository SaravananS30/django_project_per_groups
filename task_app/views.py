from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.models import Token
from rest_framework.generics import *
from .serializer import *
from .models import *
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import status, permissions, mixins
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType



# Create your views here.

def index(request):
    return HttpResponse("Hello World")


class RegisterUser(CreateAPIView):
    serializer_class = RegisterUserSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer_class = RegisterUserSerializer(data=request.data)
            hpass = make_password(request.data['password'])
            if serializer_class.is_valid():
                serializer_class.validated_data['id'] = 'VIV'+''.join(random.choice(string.digits) for _ in range(5))
                serializer_class.validated_data['password']=hpass
                serializer_class.save()
                data = {
                    'Response Code': status.HTTP_201_CREATED,
                    'Status': 'TRUE',
                    'Message': 'User Details Created Successfully',
                    "Error": 'None',
                    "StatusFlag": True,
                    'Data': serializer_class.data,
                }
                return Response(data)
            else:
                data = {
                    'Response Code': status.HTTP_400_BAD_REQUEST,
                    'Status': 'FALSE',
                    'Message': 'Incorrect Details',
                    "Error": serializer_class.errors,
                    "StatusFlag": False,
                    'Data': [],
                }
                return Response(data)
        except Exception as e:
            data = {
                'Response Code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'Status': 'FALSE',
                'Message': 'Creating Process is failed',
                "Error": str(e),
                "StatusFlag": False,
                'Data': [],
            }
            return Response(data)


class LoginUser(CreateAPIView):
    serializer_class = LoginSerializer
    queryset = CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            user = authenticate(request, email=request.data['email'], password=request.data['password'])
            if user is not None:
                token, create = Token.objects.get_or_create(user=user)
                USER = CustomUser.objects.filter(email=request.data['email']).first()
                if USER and USER.role == "ADMIN":
                    admin_group, created = CustomGroup.objects.get_or_create(name='ADMIN', department='Software Dep',
                                                                             description='Admin has all permissions',
                                                                             level=1)
                    perm_model = ContentType.objects.get_for_model(Products)
                    permission = Permission.objects.filter(content_type=perm_model)
                    for i in permission:
                        admin_group.permissions.add(i)
                        admin_group.save()
                    user = CustomUser.objects.get(email=request.data['email'])
                    user.groups.add(admin_group)
                    user.save()


                elif USER and USER.role == "USER 1":
                    user1_group, created = CustomGroup.objects.get_or_create(name='USER 1', department='Software Dep',
                                                                             description='User 1 has two permissions',
                                                                             level=2)
                    list1 = ["add_products", "view_products"]
                    for i in list1:
                        id = Permission.objects.get(codename=i).id
                        user1_group.permissions.add(id)
                        user1_group.save()
                    user = CustomUser.objects.get(email=request.data['email'])
                    user.groups.add(user1_group)
                    user.save()


                elif USER and USER.role == "USER 2":
                    user2_group, created = CustomGroup.objects.get_or_create(name='USER 2', department='Software Dep',
                                                                             description='User 3 has three permissions',
                                                                             level=2)
                    list2 = ["add_products", "view_products", "change_products"]
                    for i in list2:
                        id = Permission.objects.get(codename=i).id
                        user2_group.permissions.add(id)
                        user2_group.save()
                    user = CustomUser.objects.get(email=request.data['email'])
                    user.groups.add(user2_group)
                    user.save()

                data = {
                    'Response Code': status.HTTP_202_ACCEPTED,
                    'Status': 'SUCCESS',
                    'Message': 'Login Successful',
                    "Error": 'None',
                    "StatusFlag": True,
                    'Data': []
                }
                return Response(data)

            else:
                data = {
                    'Response Code': status.HTTP_400_BAD_REQUEST,
                    'Status': 'FALSE',
                    'Message': 'Incorrect Details',
                    "Error": None,
                    "StatusFlag": False,
                    'Data': [],
                }
                return Response(data)
        except Exception as e:
            data = {
                'Response Code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'Status': 'FALSE',
                'Message': 'Login Process is failed',
                "Error": str(e),
                "StatusFlag": False,
                'Data': [],
            }
            return Response(data)



class ListAPI(ListAPIView):
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]
    queryset = Products.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class Productsmixins(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     GenericAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [DjangoModelPermissions]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

