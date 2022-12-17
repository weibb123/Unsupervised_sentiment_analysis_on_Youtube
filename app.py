import nltk
nltk.download('stopwords')
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
import pandas as pd
import numpy as np
import streamlit as st

# instantiate sentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()

# helper function for setting decision boundary
def score_sentiment(x):
    """ given input x, we will classify whether this text is positive, negative, neutral 
    based on decision boundary that we set
    parameter:
    x -> score that model gives
    return:
    predictions -> whether the comment is positive, negative or neutral"""

    if x >= 0.05:
        return "Positive text! You make this world a better place"
    elif x <= -0.05:
        return "Negative text! The world needs you to be positive"
    else:
        return "Neutral! Your text has no emotion"

## algorithms ##
def predict(comment):
    """ given a comment from user, we will predict the emotion of the word
    return:
    comment -> original text back to user
    sentiment -> predicted emotion of users text"""

    score = analyser.polarity_scores(comment)
    output = score['compound']
    sentiment = score_sentiment(output)
    return comment, sentiment

## building webapp

# happy image https://www.makaitalia.com/wp-content/uploads/2019/04/Emoji-happy-face-free-printable-1.jpg
# sad image https://images.emojiterra.com/google/noto-emoji/v2.034/512px/1f625.png
# neutral image https://hotemoji.com/images/dl/r/straight-face-emoji-by-twitter.png

def display_image(text):
    """
    display image based on the input what the result of prediction is
    parameters:
    x -> text
    return:
    1 of the 3 images"""
    happy = 'https://www.makaitalia.com/wp-content/uploads/2019/04/Emoji-happy-face-free-printable-1.jpg'
    sad = 'https://images.emojiterra.com/google/noto-emoji/v2.034/512px/1f625.png'
    neutral = 'https://hotemoji.com/images/dl/r/straight-face-emoji-by-twitter.png'

    score = analyser.polarity_scores(text)
    output = score['compound']
    
    if output >= 0.05: # return happy image
        return happy

    elif output <= -0.05: # return sad image
        return sad

    else: # return netural image
        return neutral

print(display_image('sad'))
st.title("Predict emotions of your text")
st.text("")
st.text("")

user_input = st.text_area("Type your text below so I can know your emotion") # textbox for user to type their text

buffer1, col1, buffer2 = st.columns([1.45, 1, 1])
clicked = col1.button(label="Predict") 

if clicked: # once user click the button
     st.write('Your text:', user_input) # give user the original text
     comment, result = predict(user_input) # make prediction of user text
     st.write(result) # write out the prediction
     img = display_image(comment) # pass user_input/comment to display_image function to get the img correspond to the class 
     st.image(img) # display the image



