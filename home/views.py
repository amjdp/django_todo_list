from django.shortcuts import render, HttpResponse
from home.models import Task

# Create your views here.
def home(request):
    context = {'success':False}
    if request.method == "POST":
        # Handle the form
        title = request.POST["title"]
        desc = request.POST["desc"]
        print(title,desc)
        # create a new task instance
        newInstance = Task(taskTitle = title, taskDesc = desc)
        newInstance.save()
        # create a python dictionary
        context = {'success':True}
    return render(request, 'index.html', context)

def tasks(request):
    allTasks = Task.objects.all()
    print(allTasks)
    # allTasks contain all the tasks - in the form of a queryset 
    # we can use a for loop to iterate this query set
    # for item in allTasks:
    #     print(item.taskTitle)
    #     print(item.taskDesc)
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)