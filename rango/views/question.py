# coding: utf-8
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from rango.models import QuestionModel, ChoiceModel
from django.core.urlresolvers import reverse


def detail(request, question_id):
    question = get_object_or_404(QuestionModel, pk=question_id)
    return render(request, 'rango/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(QuestionModel, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, ChoiceModel.DoesNotExist):
        return render(request, 'rango/detail.html', {
            'question': question,
            'error_message': "Deve selecionar uma escolha!",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('rango:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(QuestionModel, pk=question_id)
    return render(request, 'rango/results.html', {'question': question})