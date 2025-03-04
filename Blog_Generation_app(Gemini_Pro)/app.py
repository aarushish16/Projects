import streamlit as st
import google.generativeai as genai
from apikey import gemini_api_key

# Configure Google Generative AI API
genai.configure(api_key=gemini_api_key)

# Function to generate blog content using Gemini 1.5 Pro
def generate_text(blog_title, keywords, num_words):
    model_name = "gemini-1.5-pro"

    user_prompt = f"Generate a comprehensive, engaging blog post relevant to the given title: '{blog_title}' and keywords: '{keywords}'. " \
                  f"Ensure the blog is approximately {num_words} words in length, suitable for an online audience. The content should be original, informative, and maintain a consistent tone."

    model = genai.GenerativeModel(model_name)
    response = model.generate_content(user_prompt)
    
    return response.text if response else "Error generating content"

# Set app to wide mode
st.set_page_config(layout='wide')

# Display Title & Subtitle
st.title("📝 BlogCraft: Your AI Writing Companion 🚀")
st.markdown("✨ Craft perfect blogs with the power of AI - BlogCraft is your new AI companion! ✨")

# Sidebar for user input
with st.sidebar:
    st.title('🖋️ Input Your Blog Details')
    st.subheader('📌 Enter the details of the blog you want to generate')

    # Blog title input
    blog_title = st.text_input('📝 Blog Title', placeholder="Enter your blog title...")

    # Keyword input
    keywords = st.text_area('🔑 Keywords (comma-separated)', placeholder="Enter keywords...")

    # Number of words slider
    num_words = st.slider('📏 Number of Words', min_value=250, max_value=1000, step=250, value=500)

    # Submit Button
    submit_button = st.button('✨ Generate Blog')

# If the user clicks submit, generate and display images first
if submit_button:
        # Generate blog content after images
        st.subheader(f"📝 Generated Blog: {blog_title}")
        st.write("📄 *AI is writing your blog...*")  # Placeholder text while generating
        blog_content = generate_text(blog_title, keywords, num_words)
        st.write(blog_content)

else:
        st.warning("⚠️ Please enter both a blog title and keywords to generate the blog.")

