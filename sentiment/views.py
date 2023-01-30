from django.shortcuts import render, redirect, HttpResponse
from .forms import Sentiment_Typed_Tweet_analyse_form
from .sentiment_analysis_code import sentiment_analysis_code
from .forms import Sentiment_Imported_Tweet_analyse_form
from .tweepy_sentiment import Import_tweet_sentiment


from django.http import HttpResponse
from django.template import loader


def sentiment_analysis(request):
    # return render(request, 'home/sentiment.html')
    template = loader.get_template('home/sentiment.html')
    return HttpResponse(template.render())

def sentiment_analysis_type(request):
    if request.method == 'POST':
        form = Sentiment_Typed_Tweet_analyse_form(request.POST)
        analyse = sentiment_analysis_code()
        if form.is_valid():
            tweet = form.cleaned_data['sentiment_typed_tweet']
            sentiment = analyse.get_tweet_sentiment(tweet)
            args = {'tweet':tweet, 'sentiment':sentiment}
            return render(request, 'home/sentiment_type_result.html', args)
            # template = loader.get_template('home/sentiment_type_result.html')
            # return HttpResponse(template.render())

    else:
        form = Sentiment_Typed_Tweet_analyse_form()
        # return render(request, 'home/sentiment_type.html')
        template = loader.get_template('home/sentiment_type.html')
        return HttpResponse(template.render())

def sentiment_analysis_import(request):
    if request.method == 'POST':
        form = Sentiment_Imported_Tweet_analyse_form(request.POST)
        tweet_text = Import_tweet_sentiment()
        analyse = sentiment_analysis_code()

        if form.is_valid():
            handle = form.cleaned_data['sentiment_imported_tweet']

            if handle[0]=='#':
                list_of_tweets = tweet_text.get_hashtag(handle)
                list_of_tweets_and_sentiments = []
                for i in list_of_tweets:
                    list_of_tweets_and_sentiments.append((i,analyse.get_tweet_sentiment(i)))
                args = {'list_of_tweets_and_sentiments':list_of_tweets_and_sentiments, 'handle':handle}
                return render(request, 'home/sentiment_import_result_hashtag.html', args)

                # template = loader.get_template('home/sentiment_import_result_hashtag.html')
                # return HttpResponse(template.render())

            list_of_tweets = tweet_text.get_tweets(handle)
            list_of_tweets_and_sentiments = []
            if handle[0]!='@':
                handle = str('@'+handle)
            for i in list_of_tweets:
                list_of_tweets_and_sentiments.append((i,analyse.get_tweet_sentiment(i)))
            args = {'list_of_tweets_and_sentiments':list_of_tweets_and_sentiments, 'handle':handle}
            return render(request, 'home/sentiment_import_result.html', args)
            # template = loader.get_template('home/sentiment_import_result.html')
            # return HttpResponse(template.render())

    else:
        form = Sentiment_Imported_Tweet_analyse_form()
        # return render(request, 'home/sentiment_import.html')
        template = loader.get_template('home/sentiment_import.html')
        return HttpResponse(template.render())
