import logging
import discord
# import asyncio

from discord_bot import python_lib

from discord_bot.settings import DISCORD_BOT_BASE_MESSAGE_CACHE
from discord_bot.settings import DISCORD_BOT_TOKEN

# TODO: Finish creating class for base discord bot
# class DiscordBot(object):
#
#     def __init__(self):


class DiscordClient(object):

    def __init__(self, client_token):

        self.logger = self._setup_logger()
        self._client = self._setup_client(client_token)
        print(self._client)

    @staticmethod
    def _setup_logger():

        logger = logging.getLevelName(__name__)
        return logger

    def _setup_client(self, token):

        client = discord.Client(max_messages=DISCORD_BOT_BASE_MESSAGE_CACHE)
        client.close()
        try:
            client.login(token)
        except (discord.LoginFailure, discord.HTTPException, TypeError) as e:
            python_lib.log('Client failed to login using token: {token}'.format(token=token),
                           log_severity='error', logger_obj=self.logger)
            print(e)

        return client

    @property
    def client(self):
        return self._client


if __name__ == '__main__':
    test_client = DiscordClient(DISCORD_BOT_TOKEN)
    test_client.client.close()
