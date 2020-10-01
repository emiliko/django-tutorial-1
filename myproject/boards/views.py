from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Board
from django.http import Http404


def home(request):
    boards = Board.objects.all()
    
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):

    # saving this other way for reference
    #try:
    #    board = Board.objects.get(pk=pk)
    #except Board.DoesNotExist:
    #    raise Http404
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board' : board})    