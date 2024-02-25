import streamlit as st
import requests

API_TOKEN = st.secrets["API_TOKEN"]

def classify_dog_breed(image):
    url = "https://api-inference.huggingface.co/models/skyau/dog-breed-classifier-vit"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/octet-stream"  
    }
    response = requests.post(url, headers=headers, data=image)
    return response.json()


def main():
    st.title('Dog Breed Classifier')

    uploaded_file = st.file_uploader("Upload a dog image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image_bytes = uploaded_file.getvalue()
        results = classify_dog_breed(image_bytes)

        if 'error' not in results:
            st.write("Predicted Breed:")
            top_prediction = results[0]  
            breed = top_prediction.get('label')  
            confidence = top_prediction.get('score')  
            st.write(f" {breed}, Confidence: {confidence:.2f}")
        else:
            st.error(f"Error in prediction: {results.get('error', 'Unknown error')}")

if __name__ == "__main__":
    main()
