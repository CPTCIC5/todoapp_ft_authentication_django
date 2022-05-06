from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import generics
from .serializers import TodoSerializer
from app1.models import Todo
from rest_framework.decorators import api_view,permission_classes
from django.views.decorators.cache import cache_page
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
from rest_framework.decorators import throttle_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from users.forms import RegisterForm
from rest_framework.parsers import JSONParser
from django.db import IntegrityError

class IndexAPI(generics.ListCreateAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer
    cache_page=(60*15)
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[UserRateThrottle,AnonRateThrottle]

@api_view(['GET','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
@throttle_classes([UserRateThrottle])
def detail_view(request,question_id):
    if request.method=='GET':
        tasks=Todo.objects.get(id=question_id)
        serializer= TodoSerializer(tasks, many=False)
        return Response(serializer.data)
        
    if request.method=='DELETE':
        post=Todo.objects.get(id=question_id)
        if post.author == request.user:
            post.delete()
            return Response("Success,Deleted!!")
        else:
            return Response("U cannot delete any other user posts BRUH!!")

@csrf_exempt
def signup(request):
    if request.method=='POST':
        try:
            data=JSONParser().parse(request.POST)
            form=RegisterForm(data)
            if form.is_valid():
                form.save()
                token = Token.objects.create(user=form)
                return JsonResponse({'token':str(token)},status=201)
        except IntegrityError:
            return JsonResponse({'error':'That username has already been taken. Please choose a new username'}, status=400)

#@csrf_exempt
#def login(request):