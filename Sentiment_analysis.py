from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
import pandas as pd

obj = SentimentIntensityAnalyzer()

def sentimentAnalysis(ticker,headlines, date):
    dict_name = ['date','ticker','headline','sentiment']
    sentiment_data = {}
    for i in range(len(dict_name)):
        sentiment_data[dict_name[i]] = []

    counter = 0
    for headline in headlines:
        
        sentiment_eg=obj.polarity_scores(headline)
        sentiment_compound = sentiment_eg['compound']
        print(headline,ticker[counter],counter,"\ln")
        sentiment_value = [date[counter],ticker[counter],headline,sentiment_compound]
        counter +=1
        for i in range(len(sentiment_value)):
 
                sentiment_data[dict_name[i]].append(sentiment_value[i])
    df = pd.DataFrame.from_dict(sentiment_data) 

    return df


