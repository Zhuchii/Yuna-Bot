import json
import random
import discord
import asyncio
import datetime
from discord.ext import commands

with open('fun/quizz/anime_data.json', 'r') as file:
        json_data = json.load(file)

with open('fun/quizz/anime_data.json', 'r') as rr:
    all_anime = json.load(rr)

def animes():
    filtered_data = []
    for i in all_anime:
        try:
            characters_data = i['data']['Media']['characters']
            filtered_data.append(i)
        except:
            pass
    return filtered_data

def get_characters_for_series(series_id):
    json_file = 'fun/quizz/anime_data.json'

    with open(json_file, 'r') as file:
        json_data = json.load(file)
    filtered_data = []
    for i in json_data:
        try:
            characters_data = i['data']['Media']['characters']
            character = random.choice(characters_data['edges'])['node']
            character_name = character['name']['full']
            character_image_url = character['image']['large']
            filtered_data.append(i)
        except:
            pass
        
    for i in filtered_data:
        if i['data']['Media']['id'] == series_id:
            characters_data = i['data']['Media']['characters']
            break

    return characters_data


class guessB(discord.ui.View):
    def __init__(self, ctx, listapepi, correct, message, points, timeout, e, lifes, stage) -> None:
        super().__init__(timeout=timeout)
        if e == 1:
            asyncio.create_task(self.first(ctx))

        else:
            self.ctx = ctx
            self.lista = listapepi
            self.message = message
            self.correct = correct
            self.points = points
            self.lifes = lifes
            self.stage = stage
            x=0
            row = 0
            options = [
                discord.SelectOption(label=x, value=str(index), description=f'{label[:100]}')
                for index, (label, x) in enumerate(self.lista)
                ]
            
            select = discord.ui.Select(
                placeholder='Select a character',
                options=options,
                custom_id='select_character'
            )
            select.callback = self.select_option_callback
            self.add_item(select)
        
        
    async def on_timeout(self):
        await self.again(self.ctx, self.message, self.points, 3)
        
    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        if interaction.user != self.ctx.author:
            await interaction.response.send_message("You cannot interact with this menu.", ephemeral=True)
            return False
        return True

    async def select_option_callback(self, interaction: discord.Interaction):
        selected_value = interaction.data['values'][0]
        if self.lista[int(selected_value)]==self.correct:
            await interaction.response.defer(ephemeral=True)
            await self.again(self.ctx, self.message, self.points, 1)
        else:
            await interaction.response.defer(ephemeral=True)
            await self.again(self.ctx, self.message, self.points, 2)
            
    async def again(self, ctx, message, points, boolean):
        mult=1
        if points>=0 and points<=15:
            self.stage=1
        elif points>=16 and points<=50:
            self.stage=2
        elif points>=51 and points<=150:
            self.stage=3
        elif points>=151 and points<=300:
            self.stage=4
        elif points>=301 and points<=600:
            self.stage=5
        elif points>=601 and points<=1000:
            self.stage=6
        elif points>=1000:
            self.stage=7
        
        if self.stage==2:
            mult=2
        elif self.stage==3:
            mult=3
        elif self.stage==4:
            mult=4
        elif self.stage==5:
            mult=6
        elif self.stage==6:
            mult=8
        elif self.stage>=7:
            mult=10
        if boolean==1:
            points+=1*mult
        embed = discord.Embed(title='ANIME QUIZ', description=f'Points: {points}', color= discord.Color.blue())
        if boolean==1:
            embed.add_field(name='CORRECT!!!', value='', inline=False)
        elif boolean==2:
            embed.add_field(name='WRONG!!!', value=f'', inline=False)
            embed.add_field(name='',value='', inline=False)
            embed.add_field(name='', value=f'The character was:\n**{self.correct[1]}**\n{self.correct[0]}', inline=False)
            self.lifes-=1
        else:
            embed.add_field(name='TIMEOUT!!!', value=f'', inline=False)
            embed.add_field(name='',value='', inline=False)
            embed.add_field(name='', value=f'The character was:\n**{self.correct[1]}**\n{self.correct[0]}', inline=False)
            self.lifes-=1
        if self.lifes>0:
            await message.edit(embed=embed, view = None)
            await asyncio.sleep(2)
            anime = animes()
            serie_id = []
            nombre = []
            for i in anime:
                serie_id.append(int(i['data']['Media']['id']))
                nombre.append(str(i['data']['Media']['title']['romaji']))
            serie = random.choice(serie_id)
            index = serie_id.index(serie)
            get_nombre = nombre[index]
            characters_data = get_characters_for_series(serie)
            character = random.choice(characters_data['edges'])['node']
            character_name = character['name']['full']
            character_image_url = character['image']['large']
            series_random = random.sample(anime, 3)
            
            f_serie_id = []
            f_nombre = []
            for i in series_random:
                f_serie_id.append(int(i['data']['Media']['id']))
                f_nombre.append(str(i['data']['Media']['title']['romaji']))
            
            listapepi = []
            listapepi.append((get_nombre, character_name))
            correct = (get_nombre, character_name)
            contador = 0
            for i in f_serie_id:
                characters_data = get_characters_for_series(serie)
                character = random.choice(characters_data['edges'])['node']
                character_name = character['name']['full']
                listapepi.append((f_nombre[contador],character_name))
                contador += 1
            papa = ''
            random.shuffle(listapepi)
            end_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=30)
            embed = discord.Embed(title='ANIME QUIZ', description=f"Guess the anime character{'‎ '*40}**Points:** {points}{'‎ '*10}", color= discord.Color.blue())
            embed.add_field(name='', value=f'**Time left:** <t:{int(end_time.timestamp())}:R>\n**Lifes:** {self.lifes}\n**Stage:** {self.stage}', inline=False)
            
            for i, n in listapepi:
                embed.add_field(name=n, value=i, inline=False)
            
            guessB.stop(self)
                    
            embed.add_field(name='', value=papa)
            embed.set_image(url=character_image_url)
            self.view = guessB(ctx, listapepi, correct, message, points, 29, 2, self.lifes, self.stage)
            await message.edit(embed=embed, view = self.view)
        else:
            guessB.stop(self)
            embed = discord.Embed(title='ANIME QUIZ', description=f'', color= discord.Color.blue())
            embed.add_field(name='You have run out of lives!',value=f'', inline= False)
            embed.add_field(name='', value=f'**Points:** {points}')
            embed.add_field(name='',value=f'**Stage:** {self.stage}')
            await message.edit(embed=embed, view=None)
    async def first(self, ctx):
        stage = 1
        points = 0
        lifes = 3
        anime = animes()
        serie_id = []
        nombre = []
        for i in anime:
            serie_id.append(int(i['data']['Media']['id']))
            nombre.append(str(i['data']['Media']['title']['romaji']))
        serie = random.choice(serie_id)
        index = serie_id.index(serie)
        get_nombre = nombre[index]
        characters_data = get_characters_for_series(serie)
        character = random.choice(characters_data['edges'])['node']
        character_name = character['name']['full']
        character_image_url = character['image']['large']
        series_random = random.sample(anime, 3)
        
        f_serie_id = []
        f_nombre = []
        for i in series_random:
            f_serie_id.append(int(i['data']['Media']['id']))
            f_nombre.append(str(i['data']['Media']['title']['romaji']))
        
        listapepi = []
        listapepi.append((get_nombre, character_name))
        correct = (get_nombre, character_name)
        contador = 0
        for i in f_serie_id:
            characters_data = get_characters_for_series(serie)
            character = random.choice(characters_data['edges'])['node']
            character_name = character['name']['full']
            listapepi.append((f_nombre[contador],character_name))
            contador += 1
        papa = ''
        random.shuffle(listapepi)
        end_time = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=30)
        embed = discord.Embed(title='ANIME QUIZ', description=f"Guess the anime character{'‎ '*40}**Points:** {points}{'‎ '*10}", color= discord.Color.blue())
        embed.add_field(name='', value=f'Time left: <t:{int(end_time.timestamp())}:R>\nlifes: {lifes}', inline=False)
        for i, n in listapepi:
            embed.add_field(name=n, value=i, inline=False)

        embed.add_field(name='', value=papa)
        embed.set_image(url=character_image_url)
        message = await ctx.send(embed=embed)
        self.view = guessB(ctx, listapepi, correct, message, points, 29, 2, lifes, stage)
        await asyncio.sleep(1)
        await message.edit(view=self.view)
        
class guess(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        @bot.command(aliases=['guess'])
        async def gues(ctx):
            guessB(ctx, None, None, None, None, 86400, 1, None, None)


