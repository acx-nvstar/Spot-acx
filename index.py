import discord
from discord.ext import commands
import os

prefix = "!!!"
token = "NTA0MjI5MzE1MzQxMzIwMjEz.W87uJA.wlmNKyAOCGh3rAOmywfRSN96TyM"

client = commands.Bot(command_prefix = prefix)
client.remove_command("help") #remove the help command from internal so i can use mednoob help command in client.command

@client.event
async def on_ready():
    print('{0.user} is Ready!'.format(client)) #i just realized, this format method from python 2.7, so i will use this format method for this file
    return

# @client.command()
# async def help(ctx): #this is help embed from mednoob, i just make it separated from client event
#     helpembed = discord.Embed(title = "Help Command", description = "List of **Commands** of this bot.\nLook **Below**.")
#     helpembed.add_field(name = "Basic Commands", value = "`help`", inline = True)
#     helpembed.add_field(name = "More Commands", value = "Coming soon!", inline = False)
#     helpembed.set_footer(text = "Discord.Py Example")
#     await ctx.channel.send(embed = helpembed)

# @client.command()
# async def reload(ctx, extension):
#     client.reload_extension("Cogs.{}".format(extension)) #reload the extension in the "Cogs" folder
#     await ctx.send("Reloaded \"{}\"".format(extension))
#     print("Reloaded \"{}\"".format(extension))
#     return

# @client.command()
# async def load(ctx, extension):
#     client.load_extension("Cogs.{}".format(extension)) #loads the extension in the "Cogs" folder
#     await ctx.send("Loaded \"{}\"".format(extension))
#     print("Loaded \"{}\"".format(extension))
#     return


# @client.command()
# async def unload(ctx, extension):
#     client.unload_extension("Cogs.{}".format(extension)) #unloads the extension in the "Cogs" folder
#     await ctx.send("Unloaded \"{}\"".format(extension))
#     print("Unoaded \"{}\"".format(extension))
#     return

for filename in os.listdir('./Cogs'): #loads all files (*.py)
    if filename.endswith('.py'):
        client.load_extension('Cogs.{}'.format(filename[:-3])) #loads the file without ".py" for example: Cogs.ping
        print('Loaded {}'.format(filename[:-3]))

client.run(token)
