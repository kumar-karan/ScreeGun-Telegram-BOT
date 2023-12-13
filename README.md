# ScreeGun Telegram Bot

ScreeGun is a Python-based Telegram bot designed to capture screenshots at regular intervals and seamlessly share them to a specified Telegram channel. This bot utilizes the `pyautogui` library for screenshot capture and the `python-telegram-bot` library for Telegram integration.

## Features:

- **Automated Screenshot Capturing:** Takes screenshots at defined intervals using the `pyautogui` library.
- **Telegram Channel Integration:** Sends captured screenshots as photos to a specified Telegram channel.
- **Customizable Interval:** Set the frequency for taking screenshots to suit your monitoring or tracking needs.
- **Simple Configuration:** Easy setup and deployment for initiating screenshot capture and transmission.

## Getting Started:

### Prerequisites:

- Python 3.x installed on your system.
- Required Python libraries: `pyautogui` and `python-telegram-bot`.

### Installation:

1. Clone this repository:
    ```bash
    git clone https://github.com/your_username/ScreeGun-Telegram-Bot.git
    cd ScreeGun-Telegram-Bot
    ```

2. Install the required dependencies:
    ```bash
    pip install pyautogui python-telegram-bot
    ```

### Configuration:

1. Obtain your Telegram Bot API Token from the [BotFather](https://t.me/botfather) on Telegram.
2. Identify and obtain the chat ID of the target Telegram channel where you want to send the screenshots.
3. Open the `screegun_bot.py` file and update the following variables:
    - `telegram_token`: Replace `'YOUR_TELEGRAM_BOT_TOKEN'` with your actual Telegram Bot API Token.
    - `chat_id`: Replace `'-YOUR_CHANNEL_CHAT_ID'` with the chat ID of your Telegram channel.
    - `screenshot_path`: Set the path where you want to save the captured screenshots.

### Usage:

Run the `screegun_bot.py` script using Python:
```bash
python screegun_bot.py
```

The bot will start capturing screenshots at the specified interval and send them to your Telegram channel.

### Contributing:

Contributions are welcome! If you have suggestions, feature requests, or found a bug, please open an issue or submit a pull request.

### License:

This project is licensed under the [MIT License](LICENSE).
