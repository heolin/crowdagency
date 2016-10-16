from django.shortcuts import render, redirect

from lazysignup.decorators import allow_lazy_user
from django.contrib.auth.decorators import login_required

from clients.models import Client
from clients.forms import SurveyForm

@allow_lazy_user
def list(request):
    """Display list of clients"""
    print (request.user.username)
    return render(request, 'clients/list.html', {})

@allow_lazy_user
def view(request, client_id):
    """Display a certain client"""
    client = Client.objects.get(id=client_id)
    client_index_path = "clients/{0}/index.html".format(client.package_name)
    is_embeded = client.is_embeded

    return render(request, 'clients/view.html', {'client_id':client_id, 'client_index_path':client_index_path, 'is_embeded':is_embeded})


@allow_lazy_user
def survey(request, client_id):
    """Display a survey certain client"""
    client = Client.objects.get(id=client_id)
    survey_form = SurveyForm()

    if request.POST:
        survey_form = SurveyForm(request.POST)
        if survey_form.is_valid():
            survey = survey_form.save(commit=False)
            survey.user = request.user
            survey.save()
            return redirect("/")
    return render(request, 'clients/survey.html', {'client_id':client_id, 'form':survey_form})

