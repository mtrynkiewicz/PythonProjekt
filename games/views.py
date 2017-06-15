from django.views import generic
from .models import PaczkaGier
from django.views.generic.edit import CreateView,UpdateView,DeleteView

class IndexView(generic.ListView):
    template_name = 'games/index.html'
    context_object_name = 'all_games'
    def  get_queryset(self):
        return PaczkaGier.objects.all()


class DetailView(generic.DetailView):
    model=PaczkaGier
    context_object_name = 'paczka'
    template_name = 'games/detail.html'


class PaczkaCreate(CreateView):
    model= PaczkaGier
    fields = [ 'kreator_paczki', 'nazwa_paczki' , 'rodzaj_gier' , 'logo_paczki']





