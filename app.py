import streamlit as st
from PIL import Image
import os
import io

# ======= Load Required Artifacts (Assuming they are already defined) =======
# These should be defined and loaded beforehand
# model, tokenizer, max_caption_length, loaded_features, image_to_captions_mapping

INPUT_DIR = "/kaggle/input/flickr"  # You can update this if needed

# Dummy example functions — Replace with your actual implementations
def predict_caption(model, feature, tokenizer, max_length):
    return "This is a predicted caption."  # Replace with actual logic

# ========== Caption Generation Logic ========== #
def generate_caption_streamlit(uploaded_image, uploaded_filename):
    image_id = uploaded_filename.split('.')[0]
    image = Image.open(uploaded_image).convert("RGB")

    st.image(image, caption="📷 Uploaded Image", use_column_width=True)

    # Show Actual Captions
    st.markdown("### ✅ Actual Captions")
    captions = image_to_captions_mapping.get(image_id, ["Not found in mapping"])
    for i, cap in enumerate(captions):
        st.markdown(f"{i+1}. {cap}")

    # Show Predicted Caption
    st.markdown("### 🤖 Predicted Caption")
    if image_id in loaded_features:
        y_pred = predict_caption(model, loaded_features[image_id], tokenizer, max_caption_length)
        st.success(y_pred)
    else:
        st.warning("Image features not found! Make sure the image was in the training set.")

# ========== Streamlit UI ========== #
st.set_page_config(page_title="Image Captioning", page_icon="🖼️", layout="centered")

st.title("🖼️ AI Image Captioning")
st.markdown("Upload an image to view actual and predicted captions.")

uploaded_file = st.file_uploader("📂 Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        uploaded_filename = uploaded_file.name
        with st.spinner("🔍 Analyzing the image..."):
            generate_caption_streamlit(uploaded_file, uploaded_filename)
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("👆 Upload an image to get started.")

st.markdown(
    "<br><hr><p style='text-align: center; color: gray;'>🚀 GenAI Project</p>",
    unsafe_allow_html=True
)
