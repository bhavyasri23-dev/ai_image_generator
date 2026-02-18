# ai_image_generator
# 🎨 AI Creative Studio

Advanced AI-powered image generation web application using Streamlit and HuggingFace Stable Diffusion API.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=HuggingFace&logoColor=black)

## ✨ Features

### Image Generation
- **Prompt Input**: Enter detailed text prompts for image generation
- **Prompt Enhancement**: Automatically enhance prompts for better results
- **Style Selector**: Choose from 12+ artistic styles (Photorealistic, Anime, Digital Art, etc.)
- **Negative Prompt**: Specify what you don't want in the image
- **Resolution Options**: Multiple resolution choices including portrait and landscape
- **Display & Download**: View and download generated images

### Advanced Features
- **Prompt History**: Track all generated prompts with session state
- **Image Gallery**: Browse and download previously generated images
- **Multiple Images**: Generate up to 4 images per prompt
- **Usage Counter**: Track number of generations
- **Response Time**: Monitor API response times

### Technical Features
- **Stable Diffusion 2**: Powered by stabilityai/stable-diffusion-2 model
- **Secure Token**: API token stored using Streamlit secrets
- **Modular Code**: Clean, maintainable code structure
- **Error Handling**: Comprehensive exception handling
- **Production Ready**: Professional structure and organization

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- HuggingFace API Token

### Installation

1. **Clone or download this repository**

2. **Install dependencies**:
   
```
bash
   pip install -r requirements.txt
   
```

3. **Set up your HuggingFace API Token**:

   Create a `.streamlit/secrets.toml` file in your project directory:
   
```
toml
   HUGGINGFACE_TOKEN = "your_huggingface_token_here"
   
```

   Or set as environment variable:
   
```
bash
   export HUGGINGFACE_TOKEN="your_huggingface_token_here"
   
```

4. **Run the application**:
   
```
bash
   streamlit run app.py
   
```

5. **Open in browser**: Navigate to `http://localhost:8501`

## 📖 Usage Guide

### Getting Your HuggingFace Token

1. Go to [HuggingFace](https://huggingface.co/)
2. Sign in or create an account
3. Navigate to Settings → Access Tokens
4. Create a new token with "Write" permissions
5. Copy the token

### Generating Images

1. **Enter a Prompt**: Type your image description in the text area
2. **Enhance Prompt** (Optional): Select an enhancement type for better results
3. **Choose Style**: Select an artistic style from the sidebar
4. **Set Resolution**: Choose your preferred image size
5. **Add Negative Prompt** (Optional): Specify elements to avoid
6. **Configure Settings**: Adjust inference steps and guidance scale
7. **Generate**: Click the "Generate Image" button
8. **Download**: Save your generated images

### Using the Gallery

- Click "View Gallery" to see all previously generated images
- Each entry shows the prompt, settings, and generation time
- Download any image from the gallery

## ☁️ Deployment to Streamlit Cloud

### Step 1: Prepare Your Repository

1. Push your code to a GitHub repository
2. Ensure these files are included:
   - `app.py`
   - `requirements.txt`
   - `README.md`

### Step 2: Deploy on Streamlit Cloud

1. Go to [Streamlit Cloud](https://share.streamlit.io/)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository, branch, and main file path
5. Click "Deploy"

### Step 3: Configure Secrets

1. In your deployed app settings, go to "Secrets"
2. Add your HuggingFace token:
   
```
toml
   HUGGINGFACE_TOKEN = "your_token_here"
   
```
3. Click "Save"
4. The app will automatically restart with your secrets

### Alternative: Using Streamlit CLI

```
bash
# Install streamlit if not already installed
pip install streamlit

# Deploy
streamlit deploy https://github.com/yourusername/your-repo/tree/main/app.py
```

## 📁 Project Structure

```
ai_image_generator/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Documentation
└── .streamlit/
    └── secrets.toml       # Configuration secrets (local only)
```

## 🔧 Configuration Options

### Style Presets

| Style | Description |
|-------|-------------|
| Photorealistic | Realistic, high-quality photos |
| Anime | Japanese animation style |
| Artistic | Painterly, creative expression |
| Digital Art | Concept art, illustrations |
| 3D Render | CGI, professional 3D |
| Oil Painting | Classical painting style |
| Watercolor | Soft, flowing artwork |
| Sketch | Hand-drawn line art |
| Cyberpunk | Futuristic, neon-lit |
| Fantasy | Magical, mythical scenes |
| Portrait | Professional photography |

### Resolution Options

- 512x512 (Square)
- 768x768 (Large Square)
- 1024x1024 (High Res Square)
- 512x768 (Portrait)
- 768x1024 (Large Portrait)
- 1024x768 (Landscape)

### Advanced Settings

- **Inference Steps** (20-100): Higher values = more detail
- **Guidance Scale** (1-20): Higher = more prompt adherence
- **Number of Images** (1-4): Images to generate per prompt

## ⚠️ Important Notes

- **API Rate Limits**: HuggingFace free tier has rate limits
- **Generation Time**: Higher resolution = longer generation time
- **Image Quality**: Results depend on prompt quality
- **Token Security**: Never commit your API token to version control

## 🐛 Troubleshooting

### "API Token not found" Error
- Ensure your token is correctly set in secrets or environment variable
- Check for typos in the token

### Slow Generation
- Try lower resolution
- Reduce inference steps
- Check your internet connection

### Poor Image Quality
- Use more detailed prompts
- Try different styles
- Adjust guidance scale
- Increase inference steps

### Rate Limit Errors
- Wait a few minutes between generations
- Consider upgrading to HuggingFace Pro

## 📝 License

MIT License - Feel free to use and modify this project.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

Built with ❤️ using [Streamlit](https://streamlit.io/) and [HuggingFace](https://huggingface.co/)
