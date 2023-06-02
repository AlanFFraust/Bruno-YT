import random
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from myapp.models import Video
# Create your views here.

#Llamar manualmente para llenar la bd con la lista de videos
def get_video_list():
    youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)
    #Parametros de busqueda
    params = {
        'part': 'snippet',
        'channelId': 'UCGrMCMK-90u9T8vSJ7d52uA',
        'maxResults': 186  
    }

    # Realiza la solicitud para obtener los videos del canal
    next_page_token = None
    
    while True:
        if next_page_token:
            params['pageToken'] = next_page_token
            
        videos = youtube.search().list(**params).execute()

        for video in videos['items']:
            if 'videoId' in video['id']:
                video_id = video['id']['videoId']
                title = video['snippet']['title']
                description = video['snippet']['description']
                published_at = video['snippet']['publishedAt']

                if Video.objects.filter(video_id=video_id).exists():
                    Video.objects.filter(video_id=video_id).delete()

                video_obj = Video(video_id=video_id, title=title, description=description, published_at=published_at)
                video_obj.save()

        next_page_token = videos.get('nextPageToken')
        if not next_page_token:
            break


def index(request):
    videos = Video.objects.all()
    if videos:
        random_video = random.choice(videos)
        video_id = random_video.video_id
        video_url = f'https://www.youtube.com/embed/{video_id}'
        return render(request, 'index.html', {'video_url': video_url})
    return render(request,'index.html')

def get_random_video(request):
    if request.method == 'POST':
        videos = Video.objects.all()
        
        if videos:
            random_video = random.choice(videos)
            video_id = random_video.video_id
            video_url = f'https://www.youtube.com/watch?v={video_id}'

            data = {'video_id': video_id, 'video_url': video_url}
            return JsonResponse(data)
        else:
            return JsonResponse({'success': False, 'error': 'No videos found'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request'})
