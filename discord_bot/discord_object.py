import discord


class DiscordObject(object):

    def __init__(self):

        self._discord_version = discord.__version__

    def __repr__(self):
        return 'discordObject.discord_v{0}'.format(self.discord_version)

    @property
    def discord_version(self):
        return self._discord_version
