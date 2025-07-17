import streamlit as st
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
sid = SentimentIntensityAnalyzer()

st.title("🧠 Bhav Analyser - Sentiment Analyzer")
user_input = st.text_area("📝 Enter your sentence (English only for now):")

if user_input:
    scores = sid.polarity_scores(user_input)
    st.subheader("📊 Sentiment Scores")
    st.json(scores)

    compound_score = scores['compound']
    if compound_score >= 0.05:
        st.success("😄 Positive Bhav")
    elif compound_score <= -0.05:
        st.error("😠 Negative Bhav")
    else:
        st.warning("😐 Neutral Bhav")
