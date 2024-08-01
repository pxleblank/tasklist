from django.shortcuts import render
from django.http import HttpResponse


def todolist(request):
    return render(request, 'todo/html_todo_list.html',
                  context={
                      'user': 'blank.',
                      'is_tasks': False,
                  }
                  )
