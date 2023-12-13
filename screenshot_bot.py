import time
import pyautogui
import asyncio
from telegram import Bot

# Telegram Bot API Token and Channel ID
telegram_token = '6484212119:AAFWIIRE6ikSCt77lgRgf9moD4xl0GReQfo'
chat_id = '-1002043845078'  # Replace this with your obtained chat ID

# Path to save screenshots
screenshot_path = '/Users/karankumar/Pictures/Screenshots/'

# Initialize Telegram bot
bot = Bot(token=telegram_token)

# Function to take a screenshot and send it to the Telegram channel
async def send_screenshot():
    try:
        # Take a screenshot
        screenshot = pyautogui.screenshot()

        # Save the screenshot to the specified path
        file_name = f"screenshot_{int(time.time())}.png"  # Unique filename based on timestamp
        file_path = screenshot_path + file_name
        screenshot.save(file_path)

        # Send the screenshot to the Telegram channel
        with open(file_path, 'rb') as file:
            await bot.send_photo(chat_id=chat_id, photo=file)

        # Remove the saved file if needed
        # Comment out this line if you want to keep the screenshots
        # import os
        # os.remove(file_path)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Adjust the interval according to your needs (in seconds)
    interval = 5  # Take a screenshot every 10 seconds

    loop = asyncio.get_event_loop()
    while True:
        loop.run_until_complete(send_screenshot())
        time.sleep(interval)
