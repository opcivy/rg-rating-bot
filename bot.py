import nextcord
import dotenv
import os
from nextcord.ext import commands
dotenv.load_dotenv()
from algorithms import ratings

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="Chusan (NEW-LUMINOUS) Rating Calculation")
async def chusan(interaction: nextcord.Interaction,
                 score: int = nextcord.SlashOption(description="Score of play", required=True),
                 constant: float = nextcord.SlashOption(description="Constant of song", required=True)):
    rate = 0
    try:
        rate = ratings.chusan(score, constant)
    except Exception as error:
        await interaction.send(error)
    
    if rate:
         await interaction.send(f"Rating of play: {rate}")

@bot.slash_command(description="Chunithm (FIRST-PARADISE LOST) Rating Calculation")
async def chunithm(interaction: nextcord.Interaction,
                 score: int = nextcord.SlashOption(description="Score of play", required=True),
                 constant: float = nextcord.SlashOption(description="Constant of song", required=True)):
    rate = 0
    try:
        rate = ratings.chusan(score, constant)
    except Exception as error:
        await interaction.send(error)
    
    if rate:
        await interaction.send(f"Rating of play: {rate}")

@bot.slash_command(description="ONGEKI Rating Calculation")
async def ongeki(interaction: nextcord.Interaction,
                 score: int = nextcord.SlashOption(description="Score of play", required=True),
                 constant: float = nextcord.SlashOption(description="Constant of song", required=True)):
    rate = 0
    try:
        rate = ratings.ongeki(score, constant)
    except Exception as error:
        await interaction.send(error)
    
    if rate:
        await interaction.send(f"Rating of play: {rate}")

@bot.slash_command(description="WACCA Rating Calculation")
async def wacca(interaction: nextcord.Interaction,
                 score: int = nextcord.SlashOption(description="Score of play", required=True),
                 constant: float = nextcord.SlashOption(description="Constant of song", required=True)):
    rate = 0
    try:
        rate = ratings.wacca(score, constant)
    except Exception as error:
        await interaction.send(error)
    
    if rate:
        await interaction.send(f"Rating of play: {rate}")

@bot.slash_command(description="GITADORA Skill Calculation")
async def gitadora(interaction: nextcord.Interaction,
                   score: float = nextcord.SlashOption(description="Score of play, in percent. (98.01% : 98.01)", required=True),
                   level: float = nextcord.SlashOption(description="Level of chart", required=True)):
    rate = 0
    try:
        rate = ratings.gitadora(score, level)
    except Exception as error:
        await interaction.send(error)

    if rate:
        await interaction.send(f'Rating of play: {rate}')

@bot.slash_command(description="Museca Curator Score Calculation")
async def museca(interaction: nextcord.Interaction,
                 score: int = nextcord.SlashOption(description="Score of play", required=True),
                 chartlevel: int = nextcord.SlashOption(description="Level of chart", required=True)):
    rate = 0
    try:
        rate = ratings.museca(score, chartlevel)
    except Exception as error:
        await interaction.send(error)
    
    if rate:
        await interaction.send(f"Curator skill from play: {rate}")

@bot.slash_command(description="Jubeat Jubility Calculation")
async def jubeat(interaction: nextcord.Interaction,
                 score: int = nextcord.SlashOption(description="Score of play", required=True),
                 musicrate: float = nextcord.SlashOption(description="Music rate of play", required=True),
                 chartlevel: float = nextcord.SlashOption(description="Level of chart", required=True)):
    rate = 0
    try:
        rate = ratings.jubeat(score, musicrate, chartlevel)
    except Exception as error:
        await interaction.send(error)
    
    if rate:
        await interaction.send(f"Jubility from play: {rate}")

@bot.slash_command(description="SOUND VOLTEX Volforce Calculation")
async def sdvx(interaction: nextcord.Interaction,
               score: int = nextcord.SlashOption(description="Score of play", required=True),
               lamp: str = nextcord.SlashOption(
                   name="lamp",
                   description="Which lamp you received for the play",
                   choices={
                       "PUC": "PERFECT ULTIMATE CHAIN",
                       "UC": "ULTIMATE CHAIN",
                       "EXCESSIVE CLEAR": "EXCESSIVE CLEAR",
                       "HARD CLEAR": "HARD CLEAR",
                       "CLEAR": "CLEAR",
                       "FAILED": "FAILED",
                       "PLAYED": "PLAYED"
                   }
               ),
               chartlevel: int = nextcord.SlashOption(description="Level of chart", required=True)):
    rate = 0
    try:
        rate = ratings.sdvx(score, lamp, chartlevel)
    except Exception as error:
        await interaction.send(error)
    
    if rate:
        await interaction.send(f"VOLFORCE from play: {rate}")

@bot.slash_command(description="Popn Music class points calculation")
async def popn(interaction: nextcord.Interaction,
               score: int = nextcord.SlashOption(description="Score of play", required=True),
               lamp: str = nextcord.SlashOption(
                   name="lamp",
                   description="Which lamp you received for the play",
                   choices={
                       "CLEAR": "CLEAR",
                       "EASY CLEAR": "EASY CLEAR",
                       "FULL COMBO": "FULL COMBO",
                       "PERFECT": "PERFECT",
                       "FAILED": "FAILED"
                   }
               ),
               chartlevel: int = nextcord.SlashOption(description="Level of chart", required=True)):
    rate = 0
    try:
        rate = ratings.popn(score, lamp, chartlevel)
    except Exception as error:
        await interaction.send(error)
    
    if rate:
        await interaction.send(f"Classpoints from play: {rate}")

bot.run(os.getenv("TOKEN"))
