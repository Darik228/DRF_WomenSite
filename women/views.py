from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import *
from rest_framework import generics, viewsets
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import WomenSerializer
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.authentication import TokenAuthentication, BaseAuthentication, SessionAuthentication


class WomenViewSet(viewsets.ModelViewSet):  # обеспечивает весь функционал 4 классов ниже
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

    @action(methods=['get'], detail=True)
    def category(self, request, pk=None):
        if pk:
            cats = Category.objects.get(pk=pk)
            return Response({'cats': cats.name})
        else:
            cats = Category.objects.all()
            return Response({'cats': [c.name for c in cats]})

    def get_queryset(self):
        queryset = Women.objects.filter(pk__lte=3)
        return queryset


class WomenApiView(generics.ListCreateAPIView):
    authentication_classes = [SessionAuthentication]  # встроено в джанго, можно не прописывать
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class WomenApiUpdateView(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Women.objects.all()  # Ленивый запрос - выполняется только тогда, когда нужны данные(Жадные-всегда)
    serializer_class = WomenSerializer
    permission_classes = (IsAuthenticated,)


class WomenApiDeleteView(generics.DestroyAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
    permission_classes = (IsAdminOrReadOnly,)


# class WomenApiDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


#  class WomenApiView(APIView):
#
#     def get(self, request):
#         queryset = Women.objects.all().values()
#
#         return Response({'posts': list(queryset)})
#
#     def post(self, request):
#         post_new = Women.objects.create(
#             title=request.data['title'],
#             content=request.data['content'],
#             cat_id=request.data['cat_id']
#         )
#
#         return Response({'post': model_to_dict(post_new)})
#
#     def delete(self, request, pk):
#         queryset = Women.objects.all().values()
#         post = Women.objects.get(pk=pk)
#         post.delete()
#         return Response({'posts': list(queryset)})
#
#     def put(self, request, pk):
#         post = Women.objects.filter(pk=pk).update(
#             title=request.data['title'],
#             content=request.data['content'],
#             cat_id=request.data['cat_id']
#         )
#         result = Women.objects.get(pk=pk)
#         return Response({'posts': model_to_dict(result)})


def index(request):
    return HttpResponse('hi')



