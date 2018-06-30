from django.shortcuts import render

from .utils import wordUtils


def index(request):
    return render(request,'words/index.html')


def results(request):
    """
     Get the word list based on the submitted letters
     """
    word_list = wordUtils.get_word_list(request.POST['letters'])

    context = {'word_list': word_list,
               'letters': request.POST['letters']}

    return render(request, 'words/results.html', context)
