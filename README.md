
# Illusive.Deception

This project is a web-based text-to-image generator that uses the Stable Diffusion v1-4 model to convert user-provided text prompts into images. The app is built using Streamlit for the web interface and the Diffusers library for handling the model. The application is optimized to run on CPUs, making it accessible for users without high-performance GPUs.

Key Features:
Text-to-Image Generation: Users can input any text prompt, and the model generates a corresponding image.

Seed Control: Users can specify a seed for reproducibility, ensuring the same image can be generated across multiple runs.

Optimized for CPU: The model runs on CPU with reduced image resolution and disabled safety checks to improve speed and performance.

Streamlit UI: The user interface is simple and intuitive, allowing users to input text and view generated images directly from the browser.

Technology Stack:

Stable Diffusion v1-4 (Diffusers Library)
Streamlit (Web UI Framework)
PyTorch for model operations

# Quick Start Demo

This is deployed on Hugging Face .The demo link is :[HuggingFace](https://huggingface.co/spaces/Anshuk666/Illusive.Deception)

# Table of Contents
- [Project Title:Illusive.Deception](#Illusive.Deception)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
- [Challenges faced during development](#Challenges-faced-during-development)
- [Contribute](#contribute)
- [License](#license)


# Installation
[(Back to top)](#table-of-contents)

How to Use:

1.Clone the repository.

2.Install the required dependencies using 
```shell
pip install -r requirements.txt
```

3. Run the Streamlit app with 
```shell
streamlit run app.py
```

4.Input a text prompt and generate an image.


# Usage
[(Back to top)](#table-of-contents)

Built with:

1. Stable Diffusion v1-4 (Diffusers Library)

2. Streamlit (Web UI Framework)

3 .PyTorch for model operations

# Challenges Faced During Development
[(Back to top)](#table-of-contents)

1. Model Optimization for CPU:

Challenge: Stable Diffusion is primarily optimized for GPU usage, and running it on CPU significantly increases processing time and resource consumption.
Solution: I reduced the image resolution from 512x512 to 256x256 and disabled the safety checker, which helped improve performance on CPU without significantly compromising image quality.

2. Handling Large Model Dependencies:

Challenge: Stable Diffusion is a large model, which can cause memory constraints and slow performance, especially when running on a machine without GPU support.
Solution: I optimized the model loading process by using a lighter precision format (torch.float32) and configured the app to use only the essential components of the pipeline.

3. Balancing Image Quality and Speed:

Challenge: Generating high-quality images requires a higher guidance scale, which increases computation time. On the other hand, lowering the guidance scale speeds up generation but can result in less coherent images.
Solution: I fine-tuned the guidance scale to 5.0 to strike a balance between generation time and image quality, making the prototype more responsive while maintaining acceptable visual results.

4. Streamlit Integration:

Challenge: Integrating the Stable Diffusion model with Streamlit, a web-based framework, presented some issues with responsiveness, especially when generating images.
Solution: To improve user experience, I used st.spinner() to provide feedback while the image is being generated, ensuring the UI remains responsive during long operations.

5. Reproducibility of Results:

Challenge: Generating the same image for a given prompt can be difficult without controlling the randomness in the model.
Solution: I implemented a seed mechanism that allows users to specify a seed value, ensuring that the generated image is consistent for repeated inputs of the same prompt.

6. Model Dependency Errors:

Challenge: Some model components, such as CLIPImageProcessor, caused errors when loading the model, as it was not necessary for CPU-optimized tasks.
Solution: I removed the dependency on CLIPImageProcessor and simplified the pipeline, which resolved the errors while keeping the functionality intact.


# Contribute
[(Back to top)](#table-of-contents)

Use Pull requests to contribute to this project.


# License
[(Back to top)](#table-of-contents)

[MIT license](./LICENSE)


