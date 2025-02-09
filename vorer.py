from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Replace with your top.gg bot URL and a list of tokens
BOT_URL = "https://top.gg/bot/YOUR_BOT_ID/vote"
TOKENS = ["token1", "token2", "token3"]  # Add your tokens here

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Path to ChromeDriver
chrome_driver_path = "/usr/local/bin/chromedriver"  # Default path after installation

def vote_with_token(token):
    try:
        # Set up the WebDriver
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Navigate to the bot's voting page
        driver.get(BOT_URL)
        time.sleep(3)

        # Use the token to log in (this is a placeholder, as top.gg may not support direct token login)
        driver.execute_script(f"localStorage.setItem('token', '{token}');")
        driver.refresh()
        time.sleep(5)

        # Click the vote button
        vote_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Vote')]")
        vote_button.click()
        time.sleep(3)

        print(f"Vote successful with token: {token}")
    except Exception as e:
        print(f"An error occurred with token {token}: {e}")
    finally:
        driver.quit()

# Function to vote every 12 hours
def schedule_votes():
    while True:
        for token in TOKENS:
            vote_with_token(token)
        print("Waiting 12 hours before the next round of votes...")
        time.sleep(43200)  # 12 hours in seconds

# Start the voting process
schedule_votes()
