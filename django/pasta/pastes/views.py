from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

from pasta.pastes.forms import PasteForm
from pasta.pastes.models import Paste


def home(request):
    pastes = Paste.objects.all()
    return render_to_response('home.html', {'pastes': pastes})


def show(requests, unique_id):
    paste = get_object_or_404(Paste, unique_id=unique_id)
    return render_to_response('show.html', {'paste': paste})


def create(request):
    if request.method == 'POST':
        form = PasteForm(request.POST)
        if form.is_valid():
            paste = form.save()
            url = reverse('pastes:show', kwargs={'unique_id': paste.unique_id})
            return redirect(url)
    else:
        form = PasteForm()
    context = RequestContext(request, {'form': form})
    return render_to_response('create.html', context)
