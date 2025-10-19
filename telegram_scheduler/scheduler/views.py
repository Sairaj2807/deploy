from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import ScheduledMessageForm
from .models import ScheduledMessage

def schedule_message(request):
    if request.method == 'POST':
        form = ScheduledMessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.created_at = timezone.now()
            message.save()
            return redirect('success')
    else:
        form = ScheduledMessageForm()
    
    # Get the last 10 messages for status display
    messages = ScheduledMessage.objects.all().order_by('-created_at')[:10]
    return render(request, 'scheduler/form.html', {'form': form, 'messages': messages})

def success(request):
    return render(request, 'scheduler/success.html')

def message_status(request):
    # Get the last 10 messages ordered by creation date (newest first)
    messages = ScheduledMessage.objects.all().order_by('-created_at')[:10]
    return render(request, 'scheduler/status.html', {'messages': messages})