from django.shortcuts import render


def index(request):
    context ={
        'Title':"Torque Hotels"
    }
    return render(request, 'visitors/index.html', context=context)
