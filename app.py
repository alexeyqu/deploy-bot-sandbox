#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


class DockeredBot:
    def __init__(self, token, build_ts, deploy_ts):
        self.updater = Updater(token, use_context=True)
        self.build_ts = build_ts
        self.deploy_ts = deploy_ts

    def start(self, update, context):
        update.message.reply_text(f'Hi! I was built at {self.build_ts} and deployed at {self.deploy_ts}')

    def help(self, update, context):
        """Send a message when the command /help is issued"""
        update.message.reply_text('This is a bot which learns to be deployed')

    def error(self, update, context):
        """Log Errors caused by Updates."""
        logger.warning(f'Update {update} caused error {context.error}')

    def main(self):
        """Start the bot."""
        dispatcher = self.updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", self.start))
        dispatcher.add_handler(CommandHandler("help", self.help))

        dispatcher.add_error_handler(self.error)

        self.updater.start_polling()

        self.updater.idle()


if __name__ == '__main__':
    with open('telegram.token') as token_file:
        token = token_file.read().strip()
    with open('build_timestamp') as ts_file:
        build_ts = ts_file.read().strip()
    with open('deploy_timestamp') as ts_file:
        deploy_ts = ts_file.read().strip()
    app = DockeredBot(token, build_ts, deploy_ts)
    app.main()
