
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



# Contribute
[(Back to top)](#table-of-contents)

Use Pull requests to contribute to this project.


# License
[(Back to top)](#table-of-contents)

[MIT license](./LICENSE)


