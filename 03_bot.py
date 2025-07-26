import pyautogui
import time
import pyperclip
from openai import OpenAI
import re

client = OpenAI(api_key="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")

def clean_chat_text(chat_text):
    # Remove timestamp like [23:56, 7/22/2025]
    cleaned_text = re.sub(r'\[\d{2}:\d{2}, \d{1,2}/\d{1,2}/\d{4}\] ', '', chat_text)
    return cleaned_text.strip()

def is_last_message_from_other(chat_text, your_name_keywords):
    # Clean timestamps first
    chat_text = clean_chat_text(chat_text)
    
    # Split by lines
    lines = chat_text.strip().split('\n')
    
    # Reverse to check from last message
    for line in reversed(lines):
        if ':' in line:
            sender = line.split(':')[0].strip()
            for keyword in your_name_keywords:
                if keyword.lower() in sender.lower():
                    return False  # It's from you
            return True  # It's from someone else
    return False

# Step 1: Click the icon to open chat
pyautogui.click(1070, 1050)
time.sleep(1)

while True:
    time.sleep(3.5)

    # Step 2: Select chat
    pyautogui.moveTo(580, 200)
    pyautogui.mouseDown()
    pyautogui.moveTo(1184, 955, duration=0.5)
    pyautogui.mouseUp()

    time.sleep(0.5)

    # Step 3: Copy chat
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.click(690, 200)
    time.sleep(0.5)

    # Step 4: Read clipboard
    chat_history = pyperclip.paste()
    print("Chat History (raw):", chat_history)

    # Check if last message is from someone else
    if is_last_message_from_other(chat_history, ["Juβαye®~βiswαs😎"]):
        cleaned_history = clean_chat_text(chat_history)

        completion = client.chat.completions.create(
            model="gpt-4-0613",
            messages=[
                {"role": "system", "content": "You are a person named Jubayer who speaks Bangla and English. You're from Bangladesh. You analyze chat history and reply like Jubayer. Output only the next message (text only)."},
                {"role": "user", "content": cleaned_history}
            ]
        )

        response = completion.choices[0].message.content
        pyperclip.copy(response)

        time.sleep(2)
        pyautogui.click(1400, 300)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        pyautogui.press('enter')


