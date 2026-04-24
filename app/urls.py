from django.urls import path, re_path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register("lectures", LectureViewSet)
# router.register("episode", EpisodeViewSet)




urlpatterns = [
    path('list/', lectures,name='lecture_list' ),
    path('lecture/<int:id>/', lecture_details, name="details"),
    path('lectures/episodes/<int:id>/', episode_details, name="episode" ),
    path('search/', search, name='search'),
    path('', home, name='home'),

    # path('', include(router.urls)),  # Include the router URLs here
     path('lecturesApi/', LectureListView.as_view(), name='lecture-list'),
    path('lecturesApi/<int:id>/', LectureDetailView.as_view(), name='lecture-detail'),
    # path('searchApi/', SearchView.as_view(), name='search'),
    # path('episodesApi/<int:id>/', EpisodeDetailView.as_view(), name='episode-detail'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
