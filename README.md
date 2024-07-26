# GitHub-Telegram-BOT
Welcome to the GitHub-Telegram Bot repository! This bot allows you to interact with GitHub directly from your Telegram messenger. You can use this bot to fetch user repositories and view issues for specific repositories.

## Features
- **User Repositories:** Fetch and display the top 50 repositories of a GitHub user based on star count.
- **View Issues:** Display the issues for a specific GitHub repository.

## Getting Started
### Prerequisites
To run this bot, you need to have the following:

**1.** Python 3.6 or above

**2.** A Telegram bot token from [BotFather](https://telegram.me/BotFather)

**3.** A GitHub personal access token with repo scope. You can create one [here](https://github.com/settings/tokens).

### Installation

**1.** Clone the repository:

```shell
git clone https://github.com/ReturnFI/GitHub-Telegram-BOT.git
cd GitHub-Telegram-BOT
```

**2.** Create a virtual environment and activate it:

```python
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

**3.** Install the required packages:

```
pip install -r requirements.txt
```


**4.** Create a `.env` file in the root directory of the project and add your Telegram bot token and GitHub access token:

```
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
GITHUB_ACCESS_TOKEN=your-github-access-token
```

## Usage
Run the bot:

```
python main.py
```

## Commands

- /start: Start the bot and display the main menu.
- User Repositories: Prompts you to enter a GitHub username and then fetches the top 50 repositories of that user based on star count.
- View Issues: Prompts you to enter a GitHub username and repository name, then fetches and displays the issues of that repository.

## Example Usage

**1.Starting the Bot:**

When you start the bot, it will greet you with a welcome message and display the main menu.

`Welcome to GitHub Bot! Choose an action:`

**2.Fetching User Repositories:**

- Click on "User Repositories".
- Enter the GitHub username when prompted (e.g., `octocat`).
- The bot will display the top 50 repositories of the user with links to the repositories.

**3.Viewing Repository Issues:**

- Click on "View Issues".
- Enter the GitHub username and repository name separated by a space when prompted (e.g., `octocat Hello-world`).
- The bot will display the issues of the specified repository with links to the issues.

## Contributing
We welcome contributions! Please fork the repository and submit a pull request for any improvements or bug fixes.
