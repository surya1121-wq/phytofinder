import streamlit as st
import random
from PIL import Image

# Sample medicinal plants info (for simulation)
medicinal_plants = {
    "Tulsi (Holy Basil)": "Used to treat colds, inflammation, malaria, heart disease, and many more.",
    "Neem": "Powerful antibacterial and antiviral properties, used for skin disorders.",
    
}

# Streamlit App
st.set_page_config(page_title="Medicinal Plant Classifier", layout="centered")
st.title("🌿 Medicinal Plant Classifier ")

st.write("Upload an image of a medicinal plant, and we’ll try to classify it (simulated).")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Simulate classification
    if st.button("Classify"):
        plant_name, plant_desc = random.choice(list(medicinal_plants.items()))
        st.success(f"✅ Identified as: **{plant_name}**")
        st.info(plant_desc)

st.markdown("---")
st.caption("Note: This is a simulated demo. Real classification requires a trained model and dataset.")
