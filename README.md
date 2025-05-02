Since our Ableton scripts run locally on the user's computer and not through an API, we at Harmoniq are developing a new client host in order to account for the control surface tooling functionality of Ableton. While we develop this, try out our server running locally on your computer

Step 1:
a. if you're familiar with git, clone this repository

b. Download the repository, unzip it, and open the folder at terminal

Step 2: Move the init

Step 2: run the following commands
brew install uv
uv sync
source .venv/bin/activate
cd backend
uv run agent.py

This will start up the MCP server

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"