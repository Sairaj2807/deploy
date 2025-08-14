from django.shortcuts import render, redirect
from .forms import ScheduledMessageForm
from .models import ScheduledMessage

def schedule_message(request):
    if request.method == 'POST':
        form = ScheduledMessageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ScheduledMessageForm()
    return render(request, 'scheduler/form.html', {'form': form})

def success(request):
    return render(request, 'scheduler/success.html')
