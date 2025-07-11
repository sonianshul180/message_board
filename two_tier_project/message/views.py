

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .models import Message

@csrf_protect
def message_board(request):
    if request.method == 'POST':
        sender = request.POST.get('sender', 'Anonymous')
        content = request.POST.get('content', '')
        if content:
            msg = Message.objects.create(sender=sender, content=content)
            return JsonResponse({
                'id': msg.id,
                'sender': msg.sender,
                'content': msg.content,
                'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M')
            })
    messages = Message.objects.all().order_by('-timestamp')
    return render(request, 'message/message.html', {'messages': messages})

@csrf_protect
def delete_message(request, msg_id):
    if request.method == 'POST':
        try:
            Message.objects.get(id=msg_id).delete()
            return JsonResponse({'status': 'deleted'})
        except Message.DoesNotExist:
            return JsonResponse({'error': 'Message not found'}, status=404)
