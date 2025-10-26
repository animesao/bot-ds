# Discord Bot

A comprehensive Discord bot with moderation, welcomes, and leveling systems.

## Features

- **Moderation System**: Commands like !warn, !ban, !kick, !mute. Auto-moderation for banned words and spam.
- **Custom Welcomes**: Set welcome channel and message with variables like {user}, {server}.
- **Leveling System**: Gain XP from messages, check rank with !rank, view top 10 with !top10.
- **Database**: SQLite with SQLAlchemy ORM for storing settings, users, warnings, etc.
- **Config**: JSON config for defaults, logging setup.

## Installation

1. Clone or download the project.
2. Navigate to the `discord_bot` directory.
3. Create virtual environment: `python -m venv venv`
4. Activate venv: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/Mac)
5. Install dependencies: `pip install -r requirements.txt`
6. Edit `.env` and add your Discord bot token: `DISCORD_TOKEN=your_token_here`
7. Run the bot: `python main.py`

## Configuration

- `config.json`: Default settings, logging config.
- `.env`: Discord token.

## Usage Examples

- Moderation: `!warn @user reason`, `!ban @user reason`, `!kick @user reason`, `!mute @user 1h`
- Welcomes: `!set_welcome_channel #general`, `!set_welcome_message Welcome {user} to {server}!`
- Leveling: `!rank`, `!top10`

## Recommendations for Improvement

- Implement full spam detection with message history tracking.
- Add role-based permissions for commands.
- Enhance mute with time-based unmute.
- Add more customization options.
- Use async database operations for better performance.
- Add error handling and user feedback.
