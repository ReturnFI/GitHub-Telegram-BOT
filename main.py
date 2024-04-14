import telebot
from api import GitHubAPI
from dotenv import load_dotenv
import os
import html

# Load environment variables from .env file
load_dotenv()

# Initialize your bot with the Telegram API token
telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telebot.TeleBot(telegram_token)

# Initialize your GitHubAPI with your GitHub token
github_token = os.getenv("GITHUB_ACCESS_TOKEN")
github_api = GitHubAPI(github_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to GitHub Bot! Choose an action:", reply_markup=create_keyboard())

user_actions = {}

@bot.message_handler(func=lambda message: message.text == "User Repositories")
def send_user_repos(message):
    reply_message = "Please enter your GitHub username:, e.g.:\n\n"\
                    "`octocat`"
    bot.reply_to(message, reply_message, parse_mode="Markdown")
    user_actions[message.chat.id] = "get_user_repos"

@bot.message_handler(func=lambda message: message.text == "View Issues")
def send_view_issues(message):
    reply_message = "Please enter the GitHub username and repository name separated by enter, e.g.:\n\n"\
                    "`octocat\nHello-world`"
    bot.reply_to(message, reply_message, parse_mode="Markdown")
    user_actions[message.chat.id] = "get_repo_issues"

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if user_actions.get(message.chat.id) == "get_user_repos":
        username = message.text
        repos = github_api.get_user_repos(username)
        if repos:
            formatted_repos = []
            for idx, repo in enumerate(repos, start=1):
                repo_link = f'<a href="{repo["html_url"]}">{repo["name"]}</a>'
                formatted_repo = f"{idx}. {repo_link}"
                formatted_repos.append(formatted_repo)

            formatted_repos_str = '\n'.join(formatted_repos)

            bot.reply_to(message, f"50 Repositories for {username} with more stars:\n\n{formatted_repos_str}", parse_mode="HTML")
        else:
            bot.reply_to(message, "Failed to fetch user repositories. Please check the username or try again later.")

    elif user_actions.get(message.chat.id) == "get_repo_issues":
        inputs = message.text.split()
        if len(inputs) != 2:
            bot.reply_to(message, "Invalid input. Please enter the GitHub username and repository name separated by space.")
            return

        username, repo_name = inputs
        issues = github_api.get_repo_issues(username, repo_name)
        if issues:
            formatted_issues = []
            for idx, issue in enumerate(issues, start=1):
                issue_title = html.escape(issue['title'])
                issue_link = f'<a href="{issue["html_url"]}">LINK</a>'
                formatted_issue = f"{idx} -{issue_title}\n{issue_link}"
                formatted_issues.append(formatted_issue)
            
            formatted_issues_str = '\n---------\n'.join(formatted_issues)
            try:
                bot.reply_to(message, f"Issues for {username}/{repo_name}:\n\n{formatted_issues_str}", parse_mode="HTML")
            except telebot.apihelper.ApiTelegramException as e:
                print(f"Error sending message: {e}")
                bot.reply_to(message, "Failed to send issues. Please try again later.")
        else:
            bot.reply_to(message, "Failed to fetch issues. Please check the username, repository name, or try again later.")
    user_actions.pop(message.chat.id, None)

def create_keyboard():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("User Repositories", "View Issues")
    return markup

bot.polling()
