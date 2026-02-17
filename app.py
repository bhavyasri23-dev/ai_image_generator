"""
AI Image Generator - Automatic Prompt Enhancer
A production-ready Streamlit application for image generation with automatic prompt enhancement.

Uses Hugging Face InferenceClient with stabilityai/stable-diffusion-xl-base-1.0 model.
Features automatic prompt enhancement with style, camera angle, and detail level control.
"""

import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image
from io import BytesIO
import base64
from typing import Optional, Tuple

# =============================================================================
# CONFIGURATION & CONSTANTS
# =============================================================================

# Page configuration
st.set_page_config(
    page_title="AI Image Generator - Auto Enhance",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# App constants
APP_NAME = "AI Image Generator - Auto Enhance"
APP_VERSION = "4.0.0"

# Model configuration
MODEL_NAME = "stabilityai/stable-diffusion-xl-base-1.0"

# Style options
STYLE_OPTIONS = [
    "Realistic",
    "3D Render",
    "Anime",
    "Cyberpunk",
    "Cinematic"
]

# Camera angle options
CAMERA_ANGLE_OPTIONS = [
    "Close-up",
    "Medium shot",
    "Wide angle",
    "Ultra wide angle",
    "Full body"
]

# Detail level options
DETAIL_LEVEL_OPTIONS = [
    "Low",
    "Medium",
    "High",
    "Ultra"
]

# =============================================================================
# SESSION STATE INITIALIZATION
# =============================================================================

def initialize_session_state():
    """Initialize session state variables."""
    if 'generated_image' not in st.session_state:
        st.session_state.generated_image = None
    if 'image_count' not in st.session_state:
        st.session_state.image_count = 0
    if 'error_message' not in st.session_state:
        st.session_state.error_message = None
    if 'final_prompt' not in st.session_state:
        st.session_state.final_prompt = None


# =============================================================================
# CONFIGURATION FUNCTIONS
# =============================================================================

def get_hf_token() -> Optional[str]:
    """Get Hugging Face API token from secrets."""
    try:
        if hasattr(st, 'secrets') and 'HF_TOKEN' in st.secrets:
            return st.secrets['HF_TOKEN']
        return None
    except Exception:
        return None


# =============================================================================
# PROMPT ENHANCEMENT
# =============================================================================

def enhance_prompt(user_prompt: str, style: str, camera_angle: str, detail_level: str) -> str:
    """
    Automatically enhance user prompt into a structured professional SDXL prompt.
    
    Args:
        user_prompt: The user's original prompt
        style: Selected style
        camera_angle: Selected camera angle
        detail_level: Selected detail level (Low, Medium, High, Ultra)
        
    Returns:
        Enhanced prompt string
    """
    # Base quality descriptors
    base_quality = "ultra detailed, high quality, cinematic lighting, realistic shadows"
    
    # Style mapping
    style_map = {
        "Realistic": "photorealistic, real world textures",
        "3D Render": "3D render, unreal engine style",
        "Anime": "anime style, vibrant colors",
        "Cyberpunk": "cyberpunk theme, neon lighting",
        "Cinematic": "dramatic lighting, movie scene composition"
    }
    
    # Detail level mapping
    detail_map = {
        "Low": "",
        "Medium": "detailed background",
        "High": "extremely detailed environment, volumetric lighting",
        "Ultra": "hyper detailed environment, global illumination, 8k resolution"
    }
    
    # Build final prompt
    final_prompt = f"{camera_angle}, {style_map.get(style)}, {user_prompt}, {detail_map.get(detail_level)}, {base_quality}"
    
    return final_prompt


# =============================================================================
# IMAGE GENERATION FUNCTIONS
# =============================================================================

def generate_image(prompt: str, negative_prompt: str) -> Tuple[Optional[Image.Image], str]:
    """
    Generate image using Hugging Face InferenceClient.
    
    Args:
        prompt: Enhanced text prompt for image generation
        negative_prompt: Negative prompt to avoid certain features
        
    Returns:
        Tuple of (PIL Image or None, error_message)
    """
    # Get API token
    HF_TOKEN = get_hf_token()
    if not HF_TOKEN:
        return None, "Hugging Face API token not configured. Please add HF_TOKEN to .streamlit/secrets.toml"
    
    try:
        # Initialize client
        client = InferenceClient(token=HF_TOKEN)
        
        # Generate image with fixed parameters
        image = client.text_to_image(
            prompt,
            model=MODEL_NAME,
            width=768,
            height=768,
            guidance_scale=8.5,
            num_inference_steps=30,
            negative_prompt=negative_prompt
        )
        
        # Convert to PIL Image if needed
        if not isinstance(image, Image.Image):
            image = Image.fromarray(image)
        
        # Convert to RGB if necessary
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        return image, ""
        
    except Exception as e:
        return None, f"Image generation failed: {str(e)}"


# =============================================================================
# UI COMPONENTS
# =============================================================================

def render_sidebar():
    """Render sidebar with configuration."""
    st.sidebar.title("🎨 AI Image Generator")
    st.sidebar.markdown("---")
    
    # API Token configuration
    st.sidebar.header("🔑 API Configuration")
    token = get_hf_token()
    if token:
        st.sidebar.success("✅ API Token configured")
    else:
        st.sidebar.error("❌ API Token not found")
        st.sidebar.info("Add HF_TOKEN to .streamlit/secrets.toml")
    
    st.sidebar.markdown("---")
    
    # Model info
    st.sidebar.header("📦 Model")
    st.sidebar.info(f"Using: **{MODEL_NAME}**")
    
    st.sidebar.markdown("---")
    
    # Statistics
    st.sidebar.header("📊 Statistics")
    
    return {}


def render_main_content(settings: dict):
    """Render main content area."""
    st.title("🎨 AI Image Generator - Auto Enhance")
    st.markdown(
        f"Generate images with **automatic prompt enhancement** using Stable Diffusion XL"
    )
    st.markdown("---")
    
    # Check API token
    if not get_hf_token():
        st.error("⚠️ Hugging Face API token not configured.")
        st.info("Please add HF_TOKEN to .streamlit/secrets.toml")
        
        # Show sample secrets.toml content
        with st.expander("How to configure API token"):
            st.code("""
# Create .streamlit/secrets.toml file:
HF_TOKEN = "your_huggingface_token_here"

# Get your token from:
# https://huggingface.co/settings/tokens
            """, language="toml")
        return
    
    # Main prompt input
    st.header("📝 Main Prompt")
    user_prompt = st.text_area(
        "Enter a simple prompt:",
        placeholder="A cat sitting on a couch",
        height=60,
        help="Enter your basic prompt - it will be automatically enhanced"
    )
    
    # Enhancement controls
    st.header("⚙️ Enhancement Controls")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Style dropdown
        style = st.selectbox(
            "🎭 Style",
            options=STYLE_OPTIONS,
            help="Select the visual style"
        )
        
        # Camera angle dropdown
        camera_angle = st.selectbox(
            "📷 Camera Angle",
            options=CAMERA_ANGLE_OPTIONS,
            help="Select the camera angle"
        )
    
    with col2:
        # Detail level dropdown
        detail_level = st.selectbox(
            "✨ Detail Level",
            options=DETAIL_LEVEL_OPTIONS,
            index=2,
            help="Select the level of detail"
        )
        
        # Show info about current settings
        st.info("📐 Image Size: 768x768 | Guidance: 8.5 | Steps: 30")
    
    # Preview enhanced prompt
    if user_prompt:
        enhanced_prompt = enhance_prompt(user_prompt, style, camera_angle, detail_level)
        with st.expander("🔍 Preview Enhanced Prompt"):
            st.code(enhanced_prompt, language="text")
    
    # Negative prompt (automatically set)
    negative_prompt = "blurry, low quality, cropped, distorted, extra limbs"
    
    # Generate button
    st.markdown("---")
    col1, col2 = st.columns([1, 4])
    
    with col1:
        generate_button = st.button(
            "🚀 Generate Image",
            type="primary",
            disabled=not user_prompt,
            use_container_width=True
        )
    
    with col2:
        clear_button = st.button("🗑️ Clear", use_container_width=True)
    
    # Handle clear
    if clear_button:
        st.session_state.generated_image = None
        st.session_state.error_message = None
        st.session_state.final_prompt = None
        st.rerun()
    
    # Process generation
    if generate_button and user_prompt:
        # Enhance the prompt
        final_prompt = enhance_prompt(user_prompt, style, camera_angle, detail_level)
        
        # Generate image with loading spinner
        with st.spinner("🎨 Generating image... This may take up to 3 minutes."):
            image, error = generate_image(
                prompt=final_prompt,
                negative_prompt=negative_prompt
            )
        
        if error:
            st.session_state.error_message = error
            st.session_state.final_prompt = None
            st.error(f"❌ {error}")
        elif image:
            # Update session state
            st.session_state.generated_image = image
            st.session_state.error_message = None
            st.session_state.final_prompt = final_prompt
            
            # Show success message
            st.success("✅ Image generated successfully!")
            
            # Display image
            st.markdown("### 🖼️ Generated Image")
            st.image(image, width=500, caption="Generated at 768x768")
            
            # Display enhanced prompt
            st.write("📝 Enhanced Prompt:", final_prompt)
            
            # Download button
            st.markdown("### 📥 Download")
            download_link = create_download_link(image, "generated_image.png")
            st.markdown(download_link, unsafe_allow_html=True)
    
    # Show current image if available
    elif st.session_state.generated_image and st.session_state.final_prompt:
        st.markdown("### 🖼️ Current Generation")
        st.image(st.session_state.generated_image, width=500, caption="Generated at 768x768")
        
        st.write("📝 Enhanced Prompt:", st.session_state.final_prompt)
        
        st.markdown("### 📥 Download")
        download_link = create_download_link(st.session_state.generated_image, "generated_image.png")
        st.markdown(download_link, unsafe_allow_html=True)


def create_download_link(image: Image.Image, filename: str = "image.png") -> str:
    """Create download link for an image."""
    buffer = BytesIO()
    image.save(buffer, format='PNG')
    buffer.seek(0)
    b64 = base64.b64encode(buffer.getvalue()).decode()
    href = f'<a href="data:file/png;base64,{b64}" download="{filename}"><button style="background-color: #FF4B4B; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-weight: bold;">📥 Download Image</button></a>'
    return href


def render_footer():
    """Render footer."""
    st.markdown("---")
    st.markdown(f"""
    <div style="text-align: center; color: #888; padding: 20px;">
        <p>🎨 {APP_NAME} v{APP_VERSION}</p>
        <p>Powered by Hugging Face Inference API</p>
    </div>
    """, unsafe_allow_html=True)


# =============================================================================
# MAIN APPLICATION
# =============================================================================

def main():
    """Main application entry point."""
    initialize_session_state()
    apply_custom_css()
    settings = render_sidebar()
    render_main_content(settings)
    render_footer()


def apply_custom_css():
    """Apply custom CSS for professional UI."""
    st.markdown("""
        <style>
        .main { background-color: #0e1117; }
        h1, h2, h3 { color: #ff4b4b; font-family: 'Helvetica Neue', sans-serif; }
        .sidebar-content { background-color: #1e1e1e; }
        .stButton > button { background-color: #ff4b4b; color: white; border: none; border-radius: 5px; padding: 10px 20px; font-weight: bold; }
        .stButton > button:hover { background-color: #ff6b6b; }
        .stButton > button:disabled { background-color: #555; color: #888; }
        .stMetric { background-color: #1e1e1e; padding: 10px; border-radius: 5px; }
        .stTextArea textarea { background-color: #1e1e1e; color: white; }
        .stSelectbox > div > div { background-color: #1e1e1e; }
        .stInfo, .stSuccess, .stError, .stWarning { background-color: #1e1e1e; }
        code { background-color: #1e1e1e; }
        hr { border-color: #333; }
        </style>
    """, unsafe_allow_html=True)


# =============================================================================
# ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    main()
