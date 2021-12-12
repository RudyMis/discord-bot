from redbot.core import commands
import urllib.request


class Ip(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def ip(self, ctx):
        """Daje Ci ip serwera"""
        # Your code will go here
        await ctx.send(urllib.request.urlopen('https://ident.me').read().decode('utf8'))
