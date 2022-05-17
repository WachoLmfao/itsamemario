import discord
import random
import asyncio
from discord.ext import commands, tasks

bot = commands.Bot(command_prefix='m!')
bot.remove_command('help')

@bot.event
async def on_ready():
  print('Mario bot is online!')

@bot.command()
async def help(ctx):
  embed = discord.Embed(title="Mario bot help!", description=f"*The bot is created by <@900064677982248960> *\n **m!marioparty** \n Main mario-party screen! \n **m!start:** \n Pick a mario party game you'd like to play! \n **m!mariokart** \n Start mariokart game! \n **m!roulette** \n Picks a game for you!")
  embed.set_image(url="https://64.media.tumblr.com/0ec006a16e01c94ff411677be05bbf9e/tumblr_msu1lxL0Ny1scncwdo1_500.gif")
  embed.set_footer(text="*Also there is !mkill @member to kill a member mario style*")
  await ctx.send(embed=embed)
  return

@bot.command()
async def marioparty(ctx):
  embed = discord.Embed(title="Mario Party Games!", description=f"Type !start to play")  
  embed.set_image(url="https://64.media.tumblr.com/4ac2c5f35ccaca1af567930c43eb6a15/tumblr_nw4jlfhNdb1s3uawvo2_r1_500.gif")
  await ctx.send(embed=embed)

@bot.command()
async def start(ctx):
  embed = discord.Embed(title="Mario party games!", description="Which game would you like to play? \n **Bustling buttons:** \n Type !bustlingbuttons to choose a button which can kill you! Yay \n **Bumper balloon:** \n Type !bumperballoon to kill mario, luigi, peach or wario! How nice ay? \n **Hexagon heat:** \n !hexagonheat to pick a color and survive... or not \n **Bungling slots** \n Under developement! \n **Lights out:** \n SMASH PEOPLE WITH A HAMMER USING !lightsout")
  embed.set_image(url="https://images-ext-1.discordapp.net/external/dvdGwGL2LYHG5O_bzzNQm08zalg2hrS00KjxFImcsWI/https/giant.gfycat.com/SimpleGrandioseAntarcticfurseal.gif")
  await ctx.send(embed=embed)

@bot.command()
async def bustlingbuttons(ctx):
   responses =[ f"Red", "Green", "White", "Pink", "Yellow"]
   embed = discord.Embed(title="Mario Party Games!", description=f"What colour do you pick?")
   embed.set_image(url="https://i.makeagif.com/media/11-21-2015/4wfHk4.gif")
   await ctx.send(embed=embed)

   try:
        msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=12.0)

   except asyncio.TimeoutError:
     await ctx.send('You took too long...')

   else:
        if msg.content == f"{random.choice(responses)}":
            embed = discord.Embed(name="Mario party games!", description=f"**{ctx.message.author.mention} picked {msg.content} and won!**")
            embed.set_image(url="https://i0.wp.com/i.gifer.com/embedded/download/YJBm.gif")
            embed.set_footer(text="Yay lets GOOO")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Mario party games!", description=f"**{ctx.message.author.mention} picked {msg.content} and died! R.I.P**")
            embed.set_image(url="https://64.media.tumblr.com/85dfa2426b29a8a693ac067218f43a0f/tumblr_mhd2j0PxDV1rrftcdo1_500.gif")
            embed.set_footer(text="oof rip")
            await ctx.send(embed=embed)
          
@bot.command()
async def bumperballoon(ctx):
   responses =[ f"Mario","Luigi","Peach","Wario","mario","luigi","peach","wario"]
   embed = discord.Embed(title="Mario Party Games!", description=f"Which car are you gonna attack?")
   embed.set_image(url="https://thumbs.gfycat.com/MagnificentGrotesqueGoldenmantledgroundsquirrel-size_restricted.gif")
   await ctx.send(embed=embed)

   try:
        msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=12.0)

   except asyncio.TimeoutError:
     await ctx.send('You took too long...')

   else:
        if msg.content == f"{random.choice(responses)}":
            embed = discord.Embed(name="Mario party games!", description=f"**{ctx.message.author.mention} picked {msg.content} and won!**")
            embed.set_image(url="https://i0.wp.com/i.gifer.com/embedded/download/YJBm.gif")
            embed.set_footer(text="Yay lets GOOO")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Mario party games!", description=f"**{ctx.message.author.mention} picked {msg.content} and died cuz he was too bad! R.I.P**")
            embed.set_image(url="https://64.media.tumblr.com/85dfa2426b29a8a693ac067218f43a0f/tumblr_mhd2j0PxDV1rrftcdo1_500.gif")
            embed.set_footer(text="oof rip")
            await ctx.send(embed=embed)

@bot.command()
async def hexagonheat(ctx):
   responses =[ f"Red", "Green", "White", "Pink", "Yellow", "Blue", "Cyan"]
   embed = discord.Embed(title="Mario Party Games!", description=f"Which hexagon are you jumping on?")
   embed.set_image(url="https://i.makeagif.com/media/12-14-2015/QUGHnk.gif")
   await ctx.send(embed=embed)

   try:
        msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=12.0)

   except asyncio.TimeoutError:
     await ctx.send('You took too long...')

   else:
        if msg.content == f"{random.choice(responses)}":
            embed = discord.Embed(name="Mario party games!", description=f"**{ctx.message.author.mention} picked {msg.content} and won!**")
            embed.set_image(url="https://i0.wp.com/i.gifer.com/embedded/download/YJBm.gif")
            embed.set_footer(text="Yay lets GOOO")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Mario party games!", description=f"**{ctx.message.author.mention} picked {msg.content} and died cuz he was too bad! R.I.P**")
            embed.set_image(url="https://64.media.tumblr.com/85dfa2426b29a8a693ac067218f43a0f/tumblr_mhd2j0PxDV1rrftcdo1_500.gif")
            embed.set_footer(text="oof rip")
            await ctx.send(embed=embed)

@bot.command()
async def bunglingslots(ctx):
  responses = [
    "<:downloadiconkey13198251881024706:972916630118080584>", "<:cheszx:972916315469783071>", "<:super_mario_world_gold_mushroom_:972916223526440970>",
  ]
  embed = discord.Embed(title="Mario Party Games!", description=f"Roll timingly so you can get correct slots")
    
  embed.set_image(url="https://64.media.tumblr.com/969e59c9adc82e0b125493d621c32a89/67c333da52d52300-ac/s400x600/63ea9a4123f05a7ba3bfa3bba2eda5318cd02e54.gif")
  await ctx.send(embed=embed)

  try:
        msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=12.0)

  except asyncio.TimeoutError:
       await ctx.send('You took too long...')

  else:
        if msg.content == f"roll":
          await ctx.send(f'{random.choice(responses)} {random.choice(responses)} {random.choice(responses)}')
          responses2 = [f"{ctx.message.author.mention} won!", f"{ctx.message.author.mention} lost"
            
          ]
          embed = discord.Embed(name="Mario party games!", description=f"**{random.choice(responses2)}**")
          embed.set_image(url="https://i0.wp.com/i.gifer.com/embedded/download/YJBm.gif")
          embed.set_footer(text="Party games")
          await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Mario party games!", description=f"**{ctx.message.author.mention} Lost **")
            embed.set_image(url="https://64.media.tumblr.com/2f0fad7a11da74951ddbbe72246b4e62/tumblr_p299vc94KX1s3uawvo1_500.gif")
            embed.set_footer(text="oof rip")
            await ctx.send(embed=embed)

@bot.command()
async def lightsout(ctx):
   responses =[ f"Mario", "Luigi", "Peach",]
   embed = discord.Embed(title="Mario Party Games!", description=f"Who are you attacking ?")
   embed.set_image(url="https://64.media.tumblr.com/2f0fad7a11da74951ddbbe72246b4e62/tumblr_p299vc94KX1s3uawvo1_500.gif")
   await ctx.send(embed=embed)

   try:
        msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=12.0)

   except asyncio.TimeoutError:
     await ctx.send('You took too long...')

   else:
        if msg.content == f"{random.choice(responses)}":
            embed = discord.Embed(name="Mario party games!", description=f"**{ctx.message.author.mention} picked {msg.content} and won!**")
            embed.set_image(url="https://i0.wp.com/i.gifer.com/embedded/download/YJBm.gif")
            embed.set_footer(text="Yay lets GOOO")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Mario party games!", description=f"**{ctx.message.author.mention} picked {msg.content} and died cuz he was too bad! R.I.P**")
            embed.set_image(url="https://64.media.tumblr.com/85dfa2426b29a8a693ac067218f43a0f/tumblr_mhd2j0PxDV1rrftcdo1_500.gif")
            embed.set_footer(text="oof rip")
            await ctx.send(embed=embed)

@bot.command()
async def roulette(ctx):
   responses =[ f"!bustlingbuttons", "!bumperballoon", "!hexagonheat","!lightsout","!bunglingslots"]
   embed = discord.Embed(title="Mario Party Games!", description=f"Roulette picked {random.choice(responses)}")
   embed.set_image(url="https://thumbs.gfycat.com/IdioticUnlawfulBird-max-1mb.gif")
   await ctx.send(embed=embed)

@bot.command()
async def mariokart(ctx):
  embed = discord.Embed(title="Mario kart!", description="Its'a me! Mario!")
  embed.set_image(url='https://64.media.tumblr.com/40da7a23ec40b93f6e5f06495e9430d2/tumblr_nnqhxg2JSH1s3uawvo2_r1_540.gif')
  embed.add_field(name="Type !startkart to start playing!", value="Hehee")
  await ctx.send(embed=embed)

@bot.command()
async def startkart(ctx):
  embed = discord.Embed(title="Mario kart!", description="Select player!")
  embed.set_image(url='https://c.tenor.com/Jo9FNYqQiLEAAAAC/character-select-player-select.gif')
  await ctx.send(embed=embed)

  try:
        msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=12.0)

  except asyncio.TimeoutError:
     await ctx.send('You took too long...')

  else:
   if msg.content == "":
                  embed = discord.Embed(name="Mario Kart", description=f"**{ctx.message.author.mention} picked {msg.content}!**")
                  embed.add_field(name="Select map!", value="Pick a map!")                                    
                  embed.set_image(url="https://64.media.tumblr.com/dc77c9d637e7c9bf43d1e06046363b55/tumblr_mgppw8EjGj1rtoyhxo1_500.gif")
                  await ctx.send(embed=embed)
     
   else:
         embed = discord.Embed(name="Mario Kart", description=f"**{ctx.message.author.mention} picked {msg.content}!**")
         embed.add_field(name="Select map!", value="Pick a map!")
         embed.set_image(url="https://64.media.tumblr.com/dc77c9d637e7c9bf43d1e06046363b55/tumblr_mgppw8EjGj1rtoyhxo1_500.gif")
         await ctx.send(embed=embed)

  try:
        msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel, timeout=12.0)

  except asyncio.TimeoutError:
     await ctx.send('You took too long...')

  else:
   if msg.content == "":
        embed = discord.Embed(title="Game started!", description="Mario kart!")
        embed.set_image(url="https://64.media.tumblr.com/tumblr_lem03aHobm1qbj1hto1_500.gif")
        await ctx.send(embed=embed)

   else:
        embed = discord.Embed(title="Game started!", description="Mario kart! Type !startgame")
        embed.set_image(url="https://64.media.tumblr.com/tumblr_lem03aHobm1qbj1hto1_500.gif")
        await ctx.send(embed=embed)

@bot.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def startgame(ctx):
  embed = discord.Embed(title="", description="")
  embed.set_image(url="https://64.media.tumblr.com/tumblr_m2qvhhvSUh1r404njo1_500.gif")
  await ctx.send(embed=embed)

  embed = discord.Embed(title="", description="")
  embed.set_image(url="https://c.tenor.com/JCoMTk0paycAAAAC/mario_kart_64-mario-kart.gif")
  await ctx.send(embed=embed)

  embed = discord.Embed(title="", description="")
  embed.set_image(url="https://thumbs.gfycat.com/FakeDemandingFairyfly-size_restricted.gif")
  await ctx.send(embed=embed)

@bot.command()
async def kill(ctx, member: discord.Member):
  responses =[
    "https://c.tenor.com/N5yrpnzeqKYAAAAd/mario-party-we-are-going-to-beat-you-to-death.gif","https://mtv.mtvnimages.com/uri/mgid:file:http:shared:mtv.com/news/wp-content/uploads/2016/01/Super-Mario-64-2-1452724498.gif?quality=.8&height=275&width=390"
  ]
  
  embed = discord.Embed(title=f"You killed {member}!",description="Yo thats kinda cool")
  embed.set_image(url=f"{random.choice(responses)}")
  await ctx.send(embed=embed)

@bot.command()
async def slap(ctx, member: discord.Member):
  embed = discord.Embed(title=f"{ctx.message.author} slapped {member}!", description="OOF")
  embed.set_image(url='https://c.tenor.com/yb6ozwhdavMAAAAC/terminal-montage-super-mario.gif')
  await ctx.send(embed=embed)

@bot.command()
async def say(ctx, *, text=''):
    if text == '':
        ctx.send("You need to say something")
    else:
        ctx.send(text)
        ctx.message.delete()

@bot.command()
async def wario(ctx):
  embed = discord.Embed(title="Concept and creation", description="Wario (Japanese: ワリオ, Hepburn: Wario, pronounced [waꜜɾio]; English: /ˈwɑːrioʊ, ˈwær-/) is a fictional character and antagonist in Nintendo's Mario series, designed as an arch-rival to Mario. He first appeared in the 1992 Game Boy game Super Mario Land 2: 6 Golden Coins as the main antagonist and final boss. His name is a portmanteau of Mario's name and the Japanese word warui (悪い), meaning bad. Wario was designed by Hiroji Kiyotake, and is voiced by Charles Martinet, who voices many other characters in the series, including Mario, Luigi, and Waluigi.Wario has become the protagonist and antihero of the Wario Land and WarioWare series, spanning handheld and console markets. In addition to appearances in spin-offs in the Mario series, he has appeared in other Nintendo properties, such as in the Super Smash Bros. series of crossover fighting games. He has also been featured in other media such as the Super Mario Adventures graphic novel. The character has received a largely positive critical reception.")
  embed.set_image(url="https://upload.wikimedia.org/wikipedia/en/thumb/8/81/Wario.png/250px-Wario.png")
  await ctx.send(embed=embed)

@bot.command()
async def mario(ctx):
  embed = discord.Embed(title="Concept and creation", description="Shigeru Miyamoto created Mario while developing Donkey Kong in an attempt to produce a best-selling video game for Nintendo; previous games, such as Sheriff, had not achieved the success of games such as Namco's Pac-Man. Originally, Miyamoto wanted to create a game that used the characters Popeye, Bluto, and Olive Oyl.[18] At the time, however, as Miyamoto was unable to acquire a license to use the characters (and would not until 1982 with Popeye), he would end up creating an unnamed player character, along with Donkey Kong, and Lady (later known as Pauline).[18]In the early stages of Donkey Kong, the focus of the game was to escape a maze, while Mario did not have the ability to jump. However, Miyamoto soon introduced jumping capabilities for the player character, reasoning that if you had a barrel rolling towards you, what would you do?")
  embed.set_image(url="https://upload.wikimedia.org/wikipedia/en/a/a9/MarioNSMBUDeluxe.png")
  await ctx.send(embed=embed)

@bot.command()
async def luigi(ctx):
  embed = discord.Embed(title="Concept and creation", description="The events leading to Luigi's creation began in 1982, during the development of Donkey Kong, where Shigeru Miyamoto had created Mario (then known as Jumpman), hoping that he would be able to recast the character in a variety of roles in future games.[5] Miyamoto was inspired by Joust to create a game with a simultaneous two-player mode, which led to his development of the game Mario Bros. in 1983. In that game, Luigi was given the role of Mario's brother as the second playable character. Miyamoto observed that the Japanese word ruiji means similar, thus explaining the similarities in size, shape, and gameplay of Luigi to Mario.[6]While Miyamoto originally portrayed Mario as a carpenter in Donkey Kong, both Mario and Luigi were styled as Italian plumbers in Mario Bros., on the suggestion of a colleague.[7] Software constraints at the time of the respective game's origins meant that Luigi's first appearance was restricted to a simple palette swap. In terms of graphics and gameplay, the characters were completely identical;[8] the green color scheme adopted for Luigi remained one of his defining physical characteristics in subsequent releases.After the success of Mario Bros., Luigi was introduced to a wider audience in 1985 with the release of the console game Super Mario Bros. Once again, his role was restricted to a palette swap and could only be used by the second player. The Japanese version of Super Mario Bros. 2 in 1986, later released in the west as Super Mario Bros.: The Lost Levels, marked the beginning of Luigi's development toward becoming a more distinguished character. Luigi's movement was no longer identical; he could now jump higher and farther than his brother, at the expense of movement response and precision.[9]While this version of Super Mario Bros. 2 was released in Japan, it was deemed to be too difficult for American audiences at the time.[7] Consequently, In 1988, an alternative release was developed to serve as Super Mario Bros. 2 for Western players (and later released in Japan as Super Mario USA); this version played a key role in shaping Luigi's current appearance.[7] The game was a conversion of Yume Kōjō: Doki Doki Panic, with the graphics altered to represent characters and scenes from the Mario franchise. In this release, the character of Mama, who had the highest jump among the original cast, served as the template for Luigi, resulting in his taller, thinner look, combined with his Mario-esque outfit and boasting green color scheme. There were earlier appearances of Luigi being taller than Mario: in Famicom Grand Prix II: 3D Hot Rally and in Super Mario Bros.: Peach-Hime Kyushutsu Dai Sakusen!; in the previously mentioned anime he wore a yellow shirt, a blue hat, and blue overalls and the color of his hat and overalls were blue. Promotional artwork for Super Mario Bros. 3 and Super Mario World depict Luigi with this new look, but the actual games did not adapt this different character design until the 1992 game Super Mario Kart. Luigi's distinctive appearance from Super Mario USA has been used ever since, even for remakes of older games.")
  embed.set_image(url="https://upload.wikimedia.org/wikipedia/en/thumb/7/73/Luigi_NSMBUDX.png/220px-Luigi_NSMBUDX.png")
  await ctx.send(embed=embed)

@bot.command()
async def peach(ctx):
  embed = discord.Embed(title="Overview", description="Peach is the native resident princess of the Mushroom Kingdom. Within her castle are Royal Guards known as mushroom retainers. Peach's first appearance is in Super Mario Bros. (1985) as a NPC, in which she was captured by Bowser and Mario had to rescue her. However, the game suggests that Peach is not helpless as she is the only person capable of breaking the curse hanging over the Mushroom Kingdom.[16] In Super Mario Bros. 2, she became a playable character, uniquely able to hover.Mostly playable, her roles vary between damsel in distress and protagonist, like in Super Mario Run.[17] She is at the center of her own story with Princess Toadstool's Castle Run (1990).[18][19] Her most prominent role is in Super Princess Peach (2005) on the Nintendo DS, where she must save Mario, Luigi, and Toads from Bowser.[20] She is not a playable character in New Super Mario Bros. Wii because a satisfactory mechanism to use her dress was not found.[21] She is a playable character in Super Mario 3D World, is the main protagonist in Super Princess Peach, and is a playable character in most Mario spin-offs such as Mario Party, Mario Kart, Mario Tennis, and Mario Golf.In Super Mario RPG and Paper Mario, a cabinet minister or chancellor is part of the Mushroom Kingdom government.[citation needed] Her father, the Mushroom King, though mentioned in the instruction manual to Super Mario Bros.,[22] has never made an appearance in the mainstream games. In the game New Super Mario Bros. U Deluxe, while Peach herself is not playable, she partially reprises her role in Super Mario Bros 2, but a character in the Switch port named Toadette had a unique crown powerup, turning her into a version of Peach with pigtails.[clarification needed]In other mediaIn the cartoon series by DiC, she is always referred to as Princess Toadstool, because the name Peach had not been used in the Western world until Yoshi's Safari in 1993, and she had red hair instead of yellow. Unlike in video games, she is occasionally seen using power-ups such as the Tanooki Leaf. She is voiced by Jeannie Elias in The Super Mario Bros. Super Show! and Tracey Moore in the two follow up series, The Adventures of Super Mario Bros. 3 and Super Mario World.Shogakukan published between 1992 and 1994 a manga named Otenba Pīchi-hime, with a plot revolving around a younger version of the princess.[23][24] From February 2006 to March 2007, the magazine Famitsu DS+Wii published a comical manga based on the Super Princess Peach called Peach no Daiboken!? created by Kazumi Sugiyama.[25][26]Peach will be voiced by Anya Taylor-Joy in the [[upcoming 2023 film adaptation.[4]")
  embed.set_image(url="https://upload.wikimedia.org/wikipedia/en/1/16/Princess_Peach_Stock_Art.png")
  await ctx.send(embed=embed)


bot.run('OTczNjMxNjQ1NDU2NDE2ODM4.GxSmI0.EvC_xCR1ArKlPxzYXnArH9OC4ohDQ75rhoJd9E')