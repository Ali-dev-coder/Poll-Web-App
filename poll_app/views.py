from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import pollmodel
from .forms import pollforms
# Create your views here.
def home(request):
    polls = pollmodel.objects.all()
    context = {'polls':polls}
    return render(request, 'poll/home.html', context)

def create(request):
    if request.method == 'POST':
        form = pollforms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = pollforms()        
    context = {'form':form}
    return render(request, 'poll/create.html', context)

def vote(request, poll_id):
    polls = pollmodel.objects.get(pk = poll_id)
    if request.method == 'POST':
        selected_option = request.POST['poll']
        if selected_option == 'option_one':
            polls.poll_option_one_count += 1
        elif selected_option == 'option_two':
            polls.poll_option_two_count += 1
        elif selected_option == 'option_three':
            polls.poll_option_three_count += 1
        else:
            return HttpResponse(400, 'invalid option')
        polls.save()
        return redirect('result', polls.id)           
    context = {'polls':polls}
    return render(request, 'poll/vote.html', context)

def result(request, poll_id):
    polls = pollmodel.objects.get(pk = poll_id)
    context = {'polls':polls}
    return render(request, 'poll/result.html', context)
