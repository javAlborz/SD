import streamlit as st
import requests

# Your Hugging Face API token
API_TOKEN = st.secrets["API_TOKEN"]

def classify_dog_breed(image):
    url = "https://api-inference.huggingface.co/models/skyau/dog-breed-classifier-vit"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/octet-stream"  # Assuming raw binary support
    }
    # Sending image as raw binary data
    response = requests.post(url, headers=headers, data=image)
    return response.json()


# Streamlit UI
def main():
    st.title('Dog Breed Classifier')

    uploaded_file = st.file_uploader("Upload a dog image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # Convert the uploaded file to bytes
        image_bytes = uploaded_file.getvalue()
        # Call the classify function with the image bytes
        results = classify_dog_breed(image_bytes)

        # Display results
        if 'error' not in results:
            st.write("Predicted Breed:")
            st.json(results)
        else:
            st.error(f"Error in prediction: {results['error']}")

if __name__ == "__main__":
    main()
