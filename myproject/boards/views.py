from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Board, Topic, Post
from django.http import Http404
from django.contrib.auth.models import User
from .forms import NewTopicForm


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

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first() # TODO: get the currently logged in user

    if request.method == 'POST': # check if request is a POST or GET
        form = NewTopicForm(request.POST) #instantiate a form instance passing the POST data to the form
        
        if form.is_valid(): #verify the data, if the data was invalid, Django will add a list of errors to the form
            topic = form.save(commit=False) # save the data in the database
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )

            # redirect the user somewhere else to aboid the user resubmitting the form
            # by pressing F5 and also to keep the flow of the application
            return redirect('board_topics', pk=board.pk) # TODO: redirect to the created topic page
    else: # if the request was a GET, initialize a new and empty form
        form = NewTopicForm()
   
    return render(request, 'new_topic.html', {'board' : board, 'form': form})       