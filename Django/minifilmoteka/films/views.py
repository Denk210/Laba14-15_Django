from django.shortcuts import render, get_object_or_404

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Film
from .serializers import FilmSerializer
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
import io

class FilmList(generics.ListCreateAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FilmDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@api_view(['GET', 'POST'])
def film_list(request):
    if request.method == 'GET':
        films = Film.objects.all()
        serializer = FilmSerializer(films, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FilmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def film_detail(request, pk):
    try:
        film = Film.objects.get(pk=pk)
    except Film.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FilmSerializer(film)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FilmSerializer(film, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        film.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def film_detail_view(request, pk):
    film = get_object_or_404(Film, pk=pk)
    return render(request, 'film_detail.html', {'film': film})


def test_serialization(request):
    film = Film.objects.first()
    serializer = FilmSerializer(film)
    json_data = JSONRenderer().render(serializer.data)  # Сериализация в JSON

    # Десериализация
    stream = io.BytesIO(json_data)
    data = JSONParser().parse(stream)
    serializer = FilmSerializer(data=data)
    serializer.is_valid()

    return JsonResponse({'status': 'success', 'serialized_data': serializer.data})

def test_serialization_view(request):
    return render(request, 'test_serialization.html')

def film_list_view(request):
    films = get_object_or_404(Film)
    return render(request, 'film_list.html', {'films': films})