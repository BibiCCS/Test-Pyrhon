
from django.urls import path, reverse

from viewer.views import MoviesView, MoviesViewDetail, GenreMoviesView, MovieCreateView

# Important: Atunci cand avemt path-uri definite in alte apps
# in fisierul urls.py din acel app trebuie sa existe o lista
# numita 'urlpatterns' in care ne definim path-urile in mod normal
urlpatterns = [
    path('', MoviesView.as_view(), name='movie-list'),
    path('create', MovieCreateView.as_view(success_url='/'), name='movie_create'),
    path('<slug:slug>', MoviesViewDetail.as_view(), name='movie-detail'),
    path('genre/<str:genre_name>', GenreMoviesView.as_view(), name='genre-movies-list'),
]