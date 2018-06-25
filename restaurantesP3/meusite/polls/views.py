from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Cliente as Clientes
from .forms import Cliente

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Clientes.objects.order_by('-pub_date')[:5]
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Clientes.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class ContactView(generic.ListView):
    template_name = 'polls/contact.html'

    def get_queryset(self):
        form = Clientes(self.request.POST or None)
        """Return the last five published questions."""
        return Clientes.objects.order_by('-pub_date')[:5]
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Clientes.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


    def cadastrar(request):
        form = 	Cliente(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                cliente = form.save(commit==True)
                cliente.save()
                return render(request,'contact.html')
        return render(request,'index.html')



class MenuView(generic.ListView):
    template_name = 'polls/menu.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Clientes.objects.order_by('-pub_date')[:5]
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Clientes.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class BlogView(generic.ListView):
    template_name = 'polls/blog.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Clientes.objects.order_by('-pub_date')[:5]
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Clientes.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class EventsView(generic.ListView):
    template_name = 'polls/events.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Clientes.objects.order_by('-pub_date')[:5]
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Clientes.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class SingleView(generic.ListView):
    template_name = 'polls/single.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Clientes.objects.order_by('-pub_date')[:5]
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Clientes.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class TypoView(generic.ListView):
    template_name = 'polls/typo.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Clientes.objects.order_by('-pub_date')[:5]
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Clientes.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]




def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
