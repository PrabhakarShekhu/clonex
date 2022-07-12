#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging

from telegram import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Dispatcher, CommandHandler

from utils.callback import callback_delete_message
from utils.config_loader import config
from utils.restricted import restricted

logger = logging.getLogger(__name__)


def init(dispatcher: Dispatcher):
    """Provide handlers initialization."""
    dispatcher.add_handler(CommandHandler('start', start))


@restricted
def start(update, context):
    rsp = update.message.reply_text('Send me Public drive link I will provide you index link.\n'
                                    'Access Your link here 👇\n'
                                    '🔗 https://0.leechzx.workers.dev/0:/AppDrive/ 🔗 \n\n'
                                    'Bot Developed by @ZX_bots')
    update.callback_query.message.edit_reply_markup(reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Source code", url="https://telegram.me/ZX_bots"
                    ),
                    InlineKeyboardButton("Project Channel", url="https://telegram.me/ZX_bots"),
                ],
                [InlineKeyboardButton("Share", url="https://telegram.me/share/url?url=https://telegram.me/ZX_bots")],
            ]
        ))

    rsp.done.wait(timeout=60)
    message_id = rsp.result().message_id
    if update.message.chat_id < 0:
        context.job_queue.run_once(callback_delete_message, config.TIMER_TO_DELETE_MESSAGE,
                                   context=(update.message.chat_id, message_id))
        context.job_queue.run_once(callback_delete_message, config.TIMER_TO_DELETE_MESSAGE,
                                   context=(update.message.chat_id, update.message.message_id))
