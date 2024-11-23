import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Replace with your Bot Token
TOKEN = "8160386397:AAECCAzPpWfR0GvWx0VyD2kKC_Lm0r7xvAc"


# Set up logging to help track the flow and errors
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()

# Start command to greet the user
async def start(update: Update, context: CallbackContext) -> None:
    logger.info(f"Start command received from {update.message.from_user.username}")
    options = ("Here are some things I can help you with:\n"
               "/resources - Get study resources\n"
               "/explain [topic] - Get an explanation for any topic\n"
               "/study_groups - Find study groups on Telegram\n"
               "Just type your question and I'll do my best to help!")
    await update.message.reply_text("Hello! I'm your study assistant bot. How can I help you with your studies today?")
    logger.info("Replied to /start command")

# Command to handle 'explain' command
async def explain(update: Update, context: CallbackContext) -> None:
    logger.info(f"Explain command received from {update.message.from_user.username}")
    topic = " ".join(context.args)
    
    if topic:
        logger.info(f"Explaining topic: {topic}")
        # Here you would call the explanation logic, for now, we just send a placeholder response
        await update.message.reply_text(f"Here's an explanation of {topic}: [Provide Explanation Here]")
        logger.info(f"Explained topic: {topic}")
    else:
        await update.message.reply_text("Please specify a topic to explain. Example: /explain Physics")
        logger.info("User did not provide a topic, asked for clarification")

# Command to provide study resources
async def resources(update: Update, context: CallbackContext) -> None:
    logger.info(f"Resources command received from {update.message.from_user.username}")
    # Here you would provide actual resource links
    await update.message.reply_text("Here are some resources for studying:\n1. [Resource Link 1]\n2. [Resource Link 2]\n3. [Resource Link 3]")
    logger.info("Replied with study resources")

# Command to share study group links
async def study_groups(update: Update, context: CallbackContext) -> None:
    logger.info(f"Study groups command received from {update.message.from_user.username}")
    # Here you would provide actual group links
    await update.message.reply_text("Here are some study groups on Telegram:\n1. [Group Name 1] - [Link]\n2. [Group Name 2] - [Link]")
    logger.info("Replied with study group links")

# Function to respond to non-study related queries
async def handle_non_study_query(update: Update, context: CallbackContext) -> None:
    logger.info(f"Non-study query received from {update.message.from_user.username}: {update.message.text}")
    await update.message.reply_text("Sorry, I can only help with study-related questions. Please ask me about study resources, topics, or study groups!")
    logger.info("Replied with non-study query warning")

# Main function to set up the bot and handlers
def main():
    logger.info("Starting bot...")
    # Create an Application object with the bot token
    application = Application.builder().token(TOKEN).build()

    # Command Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("explain", explain))
    application.add_handler(CommandHandler("resources", resources))
    application.add_handler(CommandHandler("study_groups", study_groups))

    # Message Handler to catch any non-command text and filter out non-study related queries
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_non_study_query))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()
