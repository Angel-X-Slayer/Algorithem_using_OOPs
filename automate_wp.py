import pyautogui
import time
# Replace 'YOUR_NUMBER' with your own phone number.
# Replace 'YOUR_MESSAGE' with the message you want to send.
def send_whatsapp_message(phone_number, message):
    # Open WhatsApp
    pyautogui.press('win')
    pyautogui.write('whatsapp')
    pyautogui.press('enter')
    # Wait for WhatsApp to load
    time.sleep(5)
    # Click on the search bar
    pyautogui.click(x=100, y=100)
    # Type the phone number
    pyautogui.write(phone_number)
    # Click on the contact
    pyautogui.click(x=100, y=200)
    # Click on the message bar
    pyautogui.click(x=100, y=300)
    # Type the message
    pyautogui.write(message)
    # Click on the send button
    pyautogui.click(x=100, y=400)
# Example usage
send_whatsapp_message('YOUR_NUMBER', 'YOUR_MESSAGE')