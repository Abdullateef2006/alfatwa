from rest_framework.generics import ListAPIView
from .models import Lecture, Episodes, Questions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q


def lectures(request):
    items_per_page = 8
    lectures = Lecture.objects.all()
    paginator = Paginator(lectures, items_per_page)
    page_number = request.GET.get('page')
    lecture = paginator.get_page(page_number)
    return render(request, 'lecture_list.html', {'lecture': lecture})


def search(request):
    if request.method == 'POST':
        query = request.POST["search"]
        episode = Questions.objects.filter(
            Q(details__contains=query) )
        count = episode.count()
        context =  {
            'count': count,
            'query': query,
            'episode': episode
        }
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html', context)


def lecture_details(request, id):
    lecture = get_object_or_404(Lecture, id=id)
    episodes = Episodes.objects.filter(lecture=lecture)
    context = {
        'lecture': lecture,
        'episodes': episodes
    }

    return render(request, 'details.html', context)


def episode_details(request, id):
    episode = get_object_or_404(Episodes, id=id)
    question = Questions.objects.filter(episode=episode)
    return render(request, 'episodes.html', {'episodes': episode, 'question': question})


def home(request):
    return render(request, 'home.html', {})


# Create your views here.


# API DEVELOPMENT


# class LectureViewSet(ModelViewSet):
#     queryset = Lecture.objects.all()
#     serializer_class = lectureSerializer
#     filter_backends = [SearchFilter,]

#     permission_classes = [AllowAny, ]
#     pagination_class  = PageNumberPagination
#     search_fields = ['^title', '^description']


# class EpisodeViewSet(ModelViewSet):
#     queryset = Episodes.objects.all()
#     serializer_class = episodeSerializer
#     permission_classes = [AllowAny, ]

# views.py

# Custom paginator

class CustomPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 10


class LectureListView(ListAPIView):
    queryset = Lecture.objects.all()
    serializer_class = lectureSerializer
    pagination_class = CustomPagination
    filter_backends = [SearchFilter,]
    search_fields = ['title', 'description',]  # Add fields to be searched

# Lecture Details View


class LectureDetailView(APIView):
    def get(self, request, id):
        lecture = get_object_or_404(Lecture, id=id)
        episodes = Episodes.objects.filter(lecture=lecture)
        lecture_serializer = lectureSerializer(lecture)
        episode_serializer = episodeSerializer(episodes, many=True)
        return Response({
            'lecture': lecture_serializer.data,
            'episodes': episode_serializer.data
        })

# Search Lectures
# class SearchView(APIView):
#     def post(self, request):
#         query = request.data.get('search', '')
#         lectures = Lecture.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
#         count = lectures.count()
#         serializer = lectureSerializer(lectures, many=True)
#         return Response({
#             'count': count,
#             'query': query,
#             'lectures': serializer.data
#         })

# Episode Details View


# class EpisodeDetailView(APIView):
#     def get(self, request, id):
#         episode = get_object_or_404(Episodes, id=id)
#         questions = Questions.objects.filter(episode=episode)
#         episode_serializer = episodeSerializer(episode)
#         question_serializer = questionserializer(questions, many=True)
#         return Response({
#             'episode': episode_serializer.data,
#             'questions': question_serializer.data
#         })
