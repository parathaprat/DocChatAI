import streamlit as st
import base64

def get_image_as_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Define paths
bot_image_path = "assets/robb.jpg"
user_image_path = "assets/human.jpg"

bot_avatar = get_image_as_base64(bot_image_path)
user_avatar = get_image_as_base64(user_image_path)

css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="data:image/png;base64,{bot_avatar}" alt="Bot Avatar">
    </div>
    <div class="message">{message}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="data:image/jpg;base64,{user_avatar}" alt="User Avatar">
    </div>    
    <div class="message">{message}</div>
</div>
'''

# Function to format bot message
def format_bot_message(message):
    return bot_template.format(bot_avatar=bot_avatar, message=message)

# Function to format user message
def format_user_message(message):
    return user_template.format(user_avatar=user_avatar, message=message)
