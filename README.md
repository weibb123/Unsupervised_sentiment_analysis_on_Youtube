# Unsupervised Sentiment Analysis on Youtube Video Comments

Link to WEB APP: https://weibb123-unsupervised-sentiment-analysis-on-youtube-app-byza60.streamlit.app/


<h2>Problem statement</h2>
Detect emotions behind users text specifically social media text such as (emojis, :), :(, lol, etc)...

<h2>Backstory</h2>
As someone who first tries to break into the field of Natural Language Processing, I was astonished by how ML algorithms can detect emotions behind text messages. I

turn to Youtube and decide to analyze comments in 3Blue1Brown's(one of my favorite math educator) video. Next, I want to use ML algorithm to predict whether a text gives positive,negative, or neutral emotions.

<h2>Methods</h2>
Thankfully with Youtube API, I can extract comments from any videos that I desire.
Dataset: acquired from Youtube API (3BLUE1BROWN's video and presidential debate)

utilized NLTK, numpy, Pandas, Sklearn, matplotlib, Seaborn, Wordcloud to analyze the performance of a video(3Blue1Brown) based on comments section.

UPDATED(Dec 2022): Come back to project and eager to turn model into web app.

UPDATED(Dec 2022): utilizied streamlit to build a web app of text emotion detector and deploy onto streamlit cloud.

For ML algorithm, I used Vader to perform sentiment analysis. Because Vader is a lexicon(dictionary of sentiment), I can assess the sentiment of phrases and sentences without the need to look at anything. Next, I can identify emotion behind text even when comments are not label as positive, negative, or neutral. Not only that Vader algorithm does not need a dataset to train on.

<h2>Challenge</h2>
Learning about sentiment analysis, how to use YouTube API, and documentation on how to build webapp. I find myself reading tons of other blogs and documentation in order to adapt examples to my own use case.

<h2>Result</h2>
Data analysis on 3Blue1Brown's videos and 2020 Presidential Debate
<img width="288" alt="Screen Shot 2021-11-02 at 4 56 01 PM" src="https://user-images.githubusercontent.com/84426364/139952010-e16b8d0d-24c4-484f-9014-6a44e5918212.png">

<img width="288" alt="Screen Shot 2021-11-02 at 4 55 31 PM" src="https://user-images.githubusercontent.com/84426364/139952041-dbcbdf13-aaa3-43ac-a858-52c2eb648ffd.png">

Web APP
<img src="https://user-images.githubusercontent.com/84426364/208281878-2fb8320e-7811-44d9-9649-df5355eedc6b.png">


<h2>Conclusion</h2>
Vader sentiment analysis is convenient (no need collect data, good for social media text, no need labeled comments)

Scale up using State of Art Algorithms like BERT

Scale up and analyze comments of multiple videos of youtuber to understand their video quality.

<h3> Create your own csv file from youtube video comment 
Obtain your youtube videoID and put in the "grab-youtube-comments.ipynb" </h3>

Credit to:
<br> Vader algorithm
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.
http://comp.social.gatech.edu/papers/icwsm14.vader.hutto.pdf
<br>https://towardsdatascience.com/how-to-build-your-own-dataset-of-youtube-comments-39a1e57aade</br>
