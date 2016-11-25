# coding: utf-8
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from rango.models import Question, Choice
from django.core.urlresolvers import reverse


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'rango/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'rango/detail.html', {
            'question': question,
            'error_message': "Deve selecionar uma escolha!",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('rango:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'rango/results.html', {'question': question})