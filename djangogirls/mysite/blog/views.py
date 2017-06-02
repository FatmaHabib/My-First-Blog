from django.shortcuts import render
from django.utils import timezone
from .models import Chat

# Create your views here.
def chat_list(request):
    chats=Chat.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/chat_list.html',  {'chats': chats})


