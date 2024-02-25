import streamlit as st
import requests
import json


def analyze_sentiment(review_text):
    API_TOKEN = st.secrets["API_TOKEN"]
    url = "https://api-inference.huggingface.co/models/juliensimon/reviews-sentiment-analysis"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }
    data = json.dumps({"inputs": review_text})
    response = requests.post(url, headers=headers, data=data)
    return response.json()

def main():
    st.title('Reviews Sentiment Analysis')

    user_input = st.text_area("Enter a review", "The game was quite sucky, if I'm being honest")
    if st.button('Analyze'):
        results = analyze_sentiment(user_input)
        
        if results:
            st.write("Sentiment Analysis Result:")
            sentiment_scores = results[0]  
            for sentiment in sentiment_scores:
                label = sentiment['label']
                score = sentiment['score']
                sentiment_text = "GOOD" if label == "LABEL_1" else "BAD"
                st.write(f"Sentiment: {sentiment_text}, Confidence: {score:.2f}")
        else:
            st.error("Error in sentiment analysis.")

if __name__ == "__main__":
    main()
