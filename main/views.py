from django.shortcuts import render
from gtts import gTTS 
import time,io 
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method=='POST':
        text=request.POST.get("txt")
        tts=gTTS(text=text,lang='en')
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        response=HttpResponse(mp3_fp,content_type="audio/mpeg")
        timestamp = int(time.time())
        response['Content-Disposition'] = f'attachment; filename="audio_{timestamp}.mp3" '
        return response
    return render(request,"index.html")