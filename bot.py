import discord
from discord.ext import commands, tasks

import os
import time
from dotenv import load_dotenv
from users import save_user, get_users
from checklist import checklist

load_dotenv()
TOKEN = os.getenv("TOKEN")
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="*", intents=intents)


@tasks.loop(seconds=50)
async def scheduled_task():
    current_time = time.localtime()
    if current_time.tm_wday < 5 and current_time.tm_hour == 11 and current_time.tm_min == 0:
        checklist_users()


@bot.event
async def on_ready():
    print(f"En línea como {bot.user.name} 😎")
    scheduled_task.start()


@bot.event
async def on_message(message):
    # If the message it's from himself or from another bot:
    if message.author == bot.user or message.author.bot:
        return
    # If it is a private massage:
    if isinstance(message.channel, discord.DMChannel):
        text = str(message.content)

        # If the message is a command:
        if text.startswith("*yop "):
            try:
                parts = text.split(maxsplit=2)
                id = str(message.author.id)
                save_user(id, parts[1], parts[2])
                await message.channel.send("\nYa estás, flac@ 😎\nPasaré tu asistencia. Despreocúpate...")
            except:
                await message.channel.send("Híjole, mano, no pude entenderte 😔\nA la vuelta...")
        else:
            await message.channel.send("Kiúbole man@. ¿Te quieres apuntar para que pase lista por ti en la clase de Guido? 🧐\n¡Sastre!, escribe el comando `*yop usuario contraseña`\nPor ejemplo: `*yop al246834 Contr4seña p3rrona.`\nNo temas que ocultaré tu contraseña 🤫")
    await bot.process_commands(message)


@bot.command()
async def yop(message):
    if isinstance(message.channel, discord.DMChannel):
        return
    elif message.author.bot:
        await message.reply("Tú no juegas 😠")
    else:
        await message.reply("Aquí no, bestia. Por mensaje privado :3")


def checklist_users():
    users = get_users()
    for user in users:
        try:
            checklist(user["username"], user["password"])
        except:
            # Envía mensaje en Discord...
            raise ValueError(f"Error trying to check \"{user["username"]}\"")


bot.run(TOKEN)