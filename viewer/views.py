from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView, FormView

from viewer.models import Movie, Genre
from viewer.forms import MovieForm


def index(request):
    # In cazul in care utilizator intra pe linkul 127.0.0.1:8000/
    # va fi automat redirectionat pe pagina de /movies
    return redirect('/movies')

    # Functia redirect() poate redirectiona utilizatorul inclusiv
    # spre link-uri externe, de exemplu:
    # return redirect('http://google.com')

# class MoviesView(View):
#     def get(self, request):
#         return render(
#             request, template_name='movies.html',
#             context={'movies': Movie.objects.all()}
#         )
# SAU
# class MoviesView(TemplateView):
#     template_name = 'movies.html'
#     extra_context = {'movies': Movie.objects.all()}
# SAU
class MoviesView(ListView):
    # In aceasta clasa se apeleaza implicit
    # objects_list = Movie.objects.all()

    template_name = 'movies.html'
    model = Movie


class MoviesViewDetail(DetailView):
    template_name = 'movies_detail.html'
    model = Movie


class GenreMoviesView(ListView):
    template_name = 'movies.html'
    model = Movie

    def get_queryset(self):
        qs = super().get_queryset()
        genre = Genre.objects.get(name=self.kwargs['genre_name'])
        return qs.filter(genre=genre)

class MovieCreateView(FormView):
    template_name = 'form.html'
    form_class = MovieForm

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Movie.objects.create(
            title=cleaned_data['title'],
            genre=cleaned_data['genre'],
            rating=cleaned_data['rating'],
            released=cleaned_data['released'],
            description=cleaned_data['description']
        )
        return result

    def form_invalid(self, form):
        print('User provided invalid data.')
        return super().form_invalid(form)