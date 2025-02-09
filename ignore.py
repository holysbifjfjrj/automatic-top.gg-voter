import discord
from discord.ext import tasks, commands

# Replace 'your_token_here' with your Discord account token
TOKEN = 'your_token_here'

# Replace 'channel_id' with the ID of the channel where you want to send the command
CHANNEL_ID = 123456789012345678

# Initialize the bot with self_bot=True
bot = commands.Bot(command_prefix='!', self_bot=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    # Start the task to run every 10 minutes
    send_mine_command.start()

@tasks.loop(minutes=10)
async def send_mine_command():
    channel = bot.get_channel(CHANNEL_ID)
    if channel is not None:
        # Fetch the list of slash commands in the channel
        async for command in channel.slash_commands():
            if command.name == 'mine':
                # Execute the /mine command
                await command(channel)
                print('Executed /mine command')
                break
    else:
        print(f'Channel with ID {CHANNEL_ID} not found.')

# Run the bot
bot.run(TOKEN)
