import discord
from modelo import get_class
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(
                model_path="./keras_enf.h5",
                labels_path="./labels.txt",
                image_path=f"./{attachment.filename}"
            ))
                
            #await ctx.send(f"File '{file_name}' has been saved from {file_url}")
    else:
        await ctx.send("No file attached.")

bot.run("tokennnnnnn")