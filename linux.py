import requests
import time

# Replace with your bot ID and list of tokens
BOT_ID = "YOUR_BOT_ID"
TOKENS = ["token1", "token2", "token3"]  # Add your tokens here

# Top.gg API endpoint
VOTE_URL = f"https://top.gg/api/bots/{BOT_ID}/vote"

# Function to send a vote using a token
def send_vote(token):
    headers = {"Authorization": token}
    try:
        response = requests.post(VOTE_URL, headers=headers)
        if response.status_code == 200:
            print(f"Vote successful with token: {token}")
        else:
            print(f"Failed to vote with token: {token} (Status Code: {response.status_code})")
    except Exception as e:
        print(f"An error occurred with token {token}: {e}")

# Function to rotate through tokens and vote
def schedule_votes():
    while True:
        for token in TOKENS:
            send_vote(token)
        print("Waiting 12 hours before the next round of votes...")
        time.sleep(43200)  # 12 hours in seconds

# Start the voting process
if __name__ == "__main__":
    schedule_votes()
