from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import subprocess

def chat_page(request):
    return render(request, 'chatbot/chat.html')

def ask_ollama(request):
    if request.method == 'POST':
        user_input = request.POST.get('message')
        try:
            result = subprocess.run(
                ["ollama", "run", "mistral"],
                input=user_input.encode(),
                capture_output=True
            )
            reply = result.stdout.decode().strip()
        except Exception as e:
            reply = f"Error: {str(e)}"
        return JsonResponse({'reply': reply})