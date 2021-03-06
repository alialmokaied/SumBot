#########################################################################################
# MIT License                                                                           #
#                                                                                       #
# Copyright (c) 2021 SumBot team                                                        #
#                                                                                       #
# Permission is hereby granted, free of charge, to any person obtaining a copy          #
# of this software and associated documentation files (the "Software"), to deal         #
# in the Software without restriction, including without limitation the rights          #
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell             #
# copies of the Software, and to permit persons to whom the Software is                 #
# furnished to do so, subject to the following conditions:                              #
#                                                                                       #
# The above copyright notice and this permission notice shall be included in all        #
# copies or substantial portions of the Software.                                       #
#                                                                                       #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR            #
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,              #
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE           #
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER                #
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,         #
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE         #
# SOFTWARE.                                                                             #
# © 2021 GitHub, Inc.                                                                   #
#########################################################################################

import io
from random import randint
import aiohttp
import discord
import pyfiglet
from discord.ext import commands


class Fun(commands.Cog):
    """
    Fun commands
    """
    def __init__(self, client):
        self.client = client

    @commands.command(help='To take a random number')
    @commands.guild_only()
    async def roll(self, ctx, faces: int = 100):

        number = randint(1, faces)
        await ctx.send(f'🎲 You have got {number} !')

    @roll.error
    async def roll_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('🙄 An error occurred, please check the value')

        if isinstance(ctx.channel, discord.channel.DMChannel):
            pass

    @commands.command(name='iq', help="IQ proportions to fun")
    @commands.guild_only()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def smart(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author

            nam = randint(1, 200)

            embed = discord.Embed(
                description=f'For {member.display_name} IQ = `{nam}`',
                color=ctx.author.color,
                timestamp=ctx.message.created_at)
            embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
            embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
            await ctx.send(embed=embed)

        elif member == self.client.user:
            embed = discord.Embed(
                description='For SumBot is High IQ = `:-)`',
                color=ctx.author.color,
                timestamp=ctx.message.created_at)
            embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
            embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
            await ctx.send(embed=embed)

        else:
            nam = randint(1, 200)
            embed = discord.Embed(
                description=f'For {member.display_name} IQ = `{nam}`',
                color=ctx.author.color,
                timestamp=ctx.message.created_at)
            embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
            embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
            await ctx.send(embed=embed)

    @smart.error
    async def smart_error(self, ctx, error):
        if isinstance(error, commands.errors.MemberNotFound):
            await ctx.send('🙄 I could not find this member')
        
        elif isinstance(ctx.channel, discord.channel.DMChannel):
            pass
        else:
            await ctx.send(error)

    @commands.command(help='Rewrite what you say fondly')
    async def tag(self, ctx, *, arg: str):
        if len(arg) >= 30:
            await ctx.send("The number of characters must be less than `30`")
        else:
            await ctx.send(f"""```javascript\n{pyfiglet.figlet_format(arg)}```""")

    @tag.error
    async def tag_error(self, ctx, error):
        if isinstance(ctx.channel, discord.channel.DMChannel):
            pass
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                description='**Used:** `{}tag <messgae>`\n**Type:** Fun'.format(self.client.command_prefix),
                color=ctx.author.color,
                timestamp=ctx.message.created_at)
            embed.set_author(name=self.client.user.display_name, icon_url=self.client.user.avatar_url)
            embed.set_image(url='http://g.recordit.co/fAUUIm1npn.gif')
            await ctx.send(embed=embed)

    @commands.command(aliases=['reverse', 'rev'], help='to reverse message to fun')
    @commands.guild_only()
    async def revers(self, ctx, *, message):
        await ctx.send(message[::-1])

    @revers.error
    async def rev_error(self, ctx, error):       
        if isinstance(ctx.channel, discord.channel.DMChannel):
            pass
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                description='**Used:** `{}rev <message>`\n**Type:** Fun'.format(self.client.command_prefix),
                color=ctx.author.color,
                timestamp=ctx.message.created_at)
            embed.set_author(name=self.client.user.display_name, icon_url=self.client.user.avatar_url)
            embed.set_image(url='http://g.recordit.co/fxPjNqrbLV.gif')
            await ctx.send(embed=embed)

    @commands.command(help='To make a clyde bot write whatever you want')
    @commands.guild_only()
    async def clyde(self, ctx, *, text):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=clyde&text={text}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=ctx.author.color,
                    description=f"Clyde Bot, [link Img]({res['message']})",
                    timestamp=ctx.message.created_at
                )
                embed.set_image(url=res['message'])
                embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.send(embed=embed)

    @clyde.error
    async def clyde_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=ctx.author.color,
                description='**Used:** `{}clyde <text>`\n**Type:** fun'.format(self.client.command_prefix),
                timestamp=ctx.message.created_at
            )
            embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
            embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(help='To make a competitive match between two people')
    @commands.guild_only()
    async def vs(self, ctx, member1: discord.Member, member2: discord.Member):
        member1 = member1.avatar_url_as(size=1024, format=None, static_format='png')
        member2 = member2.avatar_url_as(size=1024, format=None, static_format='png')
        async with aiohttp.ClientSession() as cs:
            async with cs.get(
                    f"https://nekobot.xyz/api/imagegen?type=whowouldwin&user1={member1}&user2={member2}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=ctx.author.color,
                    description=f"Who Would Win, [Link img]({res['message']})",
                    timestamp=ctx.message.created_at
                )
                embed.set_image(url=res["message"])
                embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                msg = await ctx.send(embed=embed)

                await msg.add_reaction('1️⃣')
                await msg.add_reaction('2️⃣')

    @vs.error
    async def vs_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=ctx.author.color,
                description='**Used:** `{}vs <member1> <member2>`\n**Type:** fun'.format(self.client.command_prefix),
                timestamp=ctx.message.created_at
            )
            embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
            embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=ctx.author.color,
                description='**Used:** `{}vs <member1> <member2>`\n**Type:** fun'.format(self.client.command_prefix),
                timestamp=ctx.message.created_at
            )
            embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
            embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(help='Modify the profile picture to become funny')
    @commands.guild_only()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def magik(self, ctx, member: discord.Member, intensity: int = 5):
        avatar = member.avatar_url_as(size=1024, format=None, static_format='png')
        emoji = "🐧"

        message = await ctx.send(f"{emoji} — **Processing the image please wait!**")
        await message.delete(delay=7)

        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=magik&image={avatar}&intensity={intensity}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=ctx.author.color,
                    description=f"[Magik]({res['message']})",
                    timestamp=ctx.message.created_at
                )
                embed.set_image(url=res["message"])
                embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.send(embed=embed)

    @magik.error
    async def magik_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color=ctx.author.color,
                description='**Used:** `{}magik <member>`\n**Type:** fun'.format(self.client.command_prefix),
                timestamp=ctx.message.created_at
            )
            embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
            embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
            await ctx.send(embed=embed)
        elif isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=ctx.author.color,
                description='**Used:** `{}magik <member>`\n**Type:** fun'.format(self.client.command_prefix),
                timestamp=ctx.message.created_at
            )
            embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
            embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(help='Modify the profile picture to be on iPhone 11 Pro')
    @commands.guild_only()
    async def iphone(self, ctx, member: discord.Member):
        if member == None:
            member = ctx.author
        picture = member.avatar_url_as(size=1024, format=None, static_format='png')
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=iphonex&url={picture}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=ctx.author.color,
                    description=f"[Link Img]({res['message']})",
                    timestamp=ctx.message.created_at
                )
                embed.set_image(url=res["message"])
                embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.send(embed=embed)

    @iphone.error
    async def iphone_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=ctx.author.color,
                description='**Used:** `{}iphone <member>`\n**Type:** fun'.format(self.client.command_prefix),
                timestamp=ctx.message.created_at
            )
            embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
            embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(help='To write a comment in YouTube for fun')
    @commands.guild_only()
    async def youtube(self, ctx, *, comment):
        picture = ctx.author.avatar_url_as(size=1024, format=None, static_format='png')
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://some-random-api.ml/canvas/youtube-comment?avatar={picture}&username={ctx.author.name}&comment={comment}") as r:
                res = io.BytesIO(await r.read())
                youtube_file = discord.File(res, filename=f"youtube.jpg")
                embed = discord.Embed(
                    color=ctx.author.color,
                    description=f"Youtube comment, [Link Img]()",
                    timestamp=ctx.message.created_at
                )
                embed.set_image(url="attachment://youtube.jpg")
                embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)

                await ctx.send(embed=embed, file=youtube_file)

    @youtube.error
    async def youtube_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=ctx.author.color,
                description='**Used:** `{}youtube <message>`\n**Type:** fun'.format(self.client.command_prefix),
                timestamp=ctx.message.created_at
            )
            embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
            embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(help='To make his photos look really interesting')
    @commands.guild_only()
    async def captcha(self, ctx, member: discord.Member):
        if member == None:
            member = ctx.author
        avatar = member.avatar_url_as(size=1024, format=None, static_format='png')
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=captcha&url={avatar}&username=Orange") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=ctx.author.color,
                    description=f"Captcha Verification, [Link Img]({res['message']})",
                    timestamp=ctx.message.created_at
                )
                embed.set_image(url=res["message"])
                embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.send(embed=embed)

    @commands.command(help='Writing his tweet on Twitter')
    @commands.guild_only()
    async def tweet(self, ctx, username: str, *, text: str):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={text}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=ctx.author.color,
                    description=f"User Tweet, [Link Img]({res['message']})",
                    timestamp=ctx.message.created_at
                )
                embed.set_image(url=res["message"])
                embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.send(embed=embed)

    @tweet.error
    async def tweet_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color=ctx.author.color,
                description='**Used:** `{}tweet <username> <text>`\n**Type:** fun'.format(self.client.command_prefix),
                timestamp=ctx.message.created_at
            )
            embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
            embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
            await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def triggered(self, ctx, member: discord.Member):
        if member == None:
            member = ctx.author
        picture = member.avatar_url_as(size=1024, format=None, static_format='png')
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://some-random-api.ml/canvas/triggered?avatar={picture}") as r:
                res = io.BytesIO(await r.read())
                triggered_file = discord.File(res, filename=f"triggered.gif")
                embed = discord.Embed(
                    color=ctx.author.color,
                    description=f"Triggered",
                    timestamp=ctx.message.created_at
                )
                embed.set_image(url="attachment://triggered.gif")
                embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.send(embed=embed, file=triggered_file)



    @commands.command(help='to show random img cat')
    @commands.guild_only()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://some-random-api.ml/img/cat') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=ctx.author.color,
                    description=f"[Random Cat]({res['link']})",
                    timestamp=ctx.message.created_at
                )
                embed.set_image(url=res['link'])
                embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.send(embed=embed)

    @commands.command(help='to show random img panda')
    @commands.guild_only()
    async def panda(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/img/panda") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=ctx.author.color,
                    description=f"[Random Panda]({res['link']})",
                    timestamp=ctx.message.created_at
                )
                embed.set_image(url=res['link'])
                embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.send(embed=embed)

    @commands.command(help='to show random img coffee')
    @commands.guild_only()
    async def coffee(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://coffee.alexflipnote.dev/random.json") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=ctx.author.color,
                    description=f"Daily Coffee, [link Img]({res['file']})",
                    timestamp=ctx.message.created_at
                )
                embed.set_image(url=res["file"])
                embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.send(embed=embed)

    @commands.command(help='to show random img dog')
    @commands.guild_only()
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://dog.ceo/api/breeds/image/random') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=ctx.author.color,
                    description=f"Random Dog, [Link img]({res['message']})",
                    timestamp=ctx.message.created_at
                )
                embed.set_image(url=res['message'])
                embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.send(embed=embed)

    @commands.command(help='to show random img fox')
    @commands.guild_only()
    async def fox(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://randomfox.ca/floof/') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=ctx.author.color,
                    description=f"Random Fox, [link Img]({res['image']})",
                    timestamp=ctx.message.created_at
                )
                embed.set_image(url=res['image'])
                embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.send(embed=embed)

    @commands.command(help='to show random img redpanda')
    @commands.guild_only()
    async def redpanda(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/img/red_panda") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=ctx.author.color,
                    description=f"Random Panda, [Link Img]({res['link']})",
                    timestamp=ctx.message.created_at
                )
                embed.set_image(url=res['link'])
                embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
                embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))
