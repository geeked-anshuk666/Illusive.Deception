import torch
from diffusers import StableDiffusionPipeline
import streamlit as st
from PIL import Image
from authtoken import auth_token

# Load the Stable Diffusion model (optimized for CPU performance)
modelid = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(modelid, torch_dtype=torch.float32, use_auth_token=auth_token).to("cpu")

# Disable the safety checker for performance
pipe.safety_checker = None

# Reduce sample size to generate smaller images faster (e.g., 256x256)
pipe.unet.config.sample_size = 256  # Smaller image resolution for faster generation

def generate_image(prompt, seed):
    # Set the seed for reproducibility
    generator = torch.Generator().manual_seed(seed)

    # Generate the image with lower guidance scale for faster processing
    with torch.no_grad():
        image = pipe(prompt, guidance_scale=5.0, generator=generator).images[0]

    return image

# Streamlit app layout
st.title("Illusive Deception: Text-to-Image Generator: Optimized for CPU")

# Input field for prompt
prompt = st.text_input("Enter your prompt", value="A scenic view of mountains at sunset")

# Seed input for reproducibility
seed = st.number_input("Seed (optional)", value=42, min_value=0, max_value=10000)

# Generate button
if st.button("Generate"):
    if prompt:
        with st.spinner('Generating image...'):
            image = generate_image(prompt, seed)
            st.image(image, caption="Generated Image", use_column_width=True)
    else:
        st.warning("Please enter a prompt to generate the image.")