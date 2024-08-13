# lyrics/views.py
from django.shortcuts import render
from .sentiment_analysis import preprocess_text, get_sentiment

def index(request):
    return render(request, 'index.html')

def analyze_lyrics(request):
    sentiment = None
    if request.method == 'POST':
        user_lyrics = request.POST.get('lyrics')
        if user_lyrics:
            # Preprocess and get sentiment
            processed_lyrics = preprocess_text(user_lyrics)
            sentiment = get_sentiment(processed_lyrics)

    return render(request, 'index.html', {'sentiment': sentiment})
