# bilibili-discord-bot
A simple discord using py-cord to implement bilibili live streaming start notifcation to discord channel

# Installation
`pip3 install -r requirements.txt`

# Usage
rename `.env.example` file to `.env`
and fill your discord bot token  
rename `config.json.example` file to `config.json` and fill the user id, room id and channel id

change uid and room id in `./cogs/check.py`
change the channelID to the message you want to send

start the bot
`python main.py`
or
`pm2 start ecosystem.json`
