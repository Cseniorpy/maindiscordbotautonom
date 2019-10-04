from discord.ext import commands 
from datetime import datetime 
import discord
import time 
import random 
import asyncio 

#SELF-MODULES
#from channelapprove import channel_approve


bot = commands.Bot(command_prefix='.')
"""def token():
    global content
    token_file = open("/root/Desktop/IntermediatePythonProjects/maindiscordTOKEN.txt", "r")
    if token_file.mode == "r":
        content = token_file.read()

if __name__ == "__main__":
    token()

TOKEN = str(content)"""
token1 = 'NjI3ODEwODQ1OTcxMzE2NzM3.XZNZyw.'
token2 = 'JCLzL2K_s0M-VHt89nzKsBfOOcQ'
TOKEN = token1+token2

bot.remove_command('help')



#--------------------------- INFORMATION SECTION ---------------------------#
#                                                                           #
#---------------------------------------------------------------------------#







#------------------------------ EVENT SECTION ------------------------------#
#                                                                           #
#---------------------------------------------------------------------------#

@bot.event
async def on_ready():
    global public_channel_list
    global channel_test
    game = discord.Game(".yardım(bot-test)")
    await bot.change_presence(status=discord.Status.idle, activity=game)
    channel_test = bot.get_channel(627807374736097310)
    public_channel_list = [channel_test]
    

#----------------------------GLOBAL VARIABLES-------------------------------#
#                                                                           #
#---------------------------------------------------------------------------#


    print("BOT is ready!")





@bot.event 
async def on_member_remove(member):

    channel = bot.get_channel(627812771450454046)
    await channel.send("{} Sunucudan ayrıldı..".format(member.name))



#------------------------------ COMMAND SECTION ------------------------------#
#                                                                             #
#-----------------------------------------------------------------------------#



@bot.command()
async def yardım(ctx):

    user = ctx.author
   
    if not ctx.channel in public_channel_list:
        await ctx.channel.send("**Bu kanalı kullanmalısın :point_right: {0.mention}**".format(channel_bot_test))

    else:
      
        embed = discord.Embed(title='YARDIMCI KOMUTLAR', description='Bu komutları Sunucu içerisindeki **bot-test** kanalında kullanmalısın', color=0x4ad7ed)

        embed.add_field(name='**> kanal**', value='```Sunucuda bulunan kanalların açıklamasını gösterir```')
        embed.add_field(name='**> sunucu**', value='```Sunucu hakkında bilgi verir```')
        #embed.add_field(name='****', value='``````')
        #embed.add_field(name='****', value='``````')
        #embed.add_field(name='****', value='``````')

        await user.send(embed=embed)


@bot.command()
async def kanal(ctx):

    if not ctx.channel in public_channel_list:
        await ctx.channel.send("**Bu kanalı kullanmalısın :point_right: {0.mention}**".format(channel_bot_test))

    else:

    
        embed = discord.Embed(title='**KANAL REHBERİ**', description='**Sunucuda bulunan kanalların bulunduğu kategoriye göre bilgi sahibi olmak için rehberi okuyunuz**', color=0xfc0303)

        embed.add_field(name="**AUTONOMOUS**", value="```Proje hakkında genel bilgi almak için inceleyebilirsiniz```")
        embed.add_field(name="**CHAT**", value="```Burada sohbet edebilirsiniz```")
        embed.add_field(name="**PROJECT PROCESS**", value="```Bu bölümde, Projenin dört temel süreci hakkında bilgi edinebilirsiniz```")
        embed.add_field(name="**ACADEMIC PROCESS**", value="```Road MAP süresince karşılaşacağınız sorunları buradan paylaşarak projenin gelişmesine katkı sağlayabilirsiniz```")
        embed.add_field(name="**SUGGESTIONS&QUESTIONS**", value="```Proje, Discord ve BOT hakkındaki sorularınız ve görüşleriniz için burayı kullanabilirsiniz```")
        embed.add_field(name="**VOICE CHANNELS**", value="```Bu bölümde sesli olarak sohbet edebilirsiniz```")
        #embed.add_field(name="****", value="****")


        await ctx.send(embed=embed)

@bot.command()
async def sunucu(ctx):

    if not ctx.channel in public_channel_list:
        await ctx.channel.send("**Bu kanalı kullanmalısın :point_right: {0.mention}**".format(channel_bot_test))

    else:

        #ID BELONGS TO DEVELOPER
        server_admin = bot.get_user(627792025764495360)
        server = ctx.author.guild
        server_member_count = server.member_count

        embed = discord.Embed(title=f'**{str(server).upper()}**', description='', color = 0x32a8a4)
    
        embed.add_field(name='**Yönetici**', value=f'```{server_admin.name}```')
        embed.add_field(name='**Üye Sayısı**', value=f'```{int(server_member_count)-2}```')
        embed.add_field(name='**Kuruluş zamanı**', value='```29/09/19```')

        await ctx.send(embed=embed)

@bot.command()
async def sil(ctx, amount: int):

    user_list = [627792025764495360]
  
    if ctx.author.id in user_list:
        await ctx.channel.purge(limit = amount)
    else:
        await ctx.send("Bu komutu kullanmak için yetkiye sahip değilsin .. ")

@bot.command()
async def toplantı(ctx):
    if not ctx.channel in public_channel_list:
        await ctx.channel.send("**Bu kanalı kullanmalısın :point_right: {0.mention}**".format(channel_bot_test))

    else:
        from datetime import datetime 
        from datetime import date 

        import time 


        current_day = datetime.now().replace(microsecond=0)
        list_of_fridays = [10,17,24]



        new_list = []
        for i in list_of_fridays:
            name_of_day = datetime(2019, 10, i, 17, 30, 0, 0)

            new_list.append((abs(current_day - name_of_day)))

        next = f"Bir sonraki toplantıya {new_list[0]} saat kaldı"

        final = f"{next[0:25]}gün{next[29:]}"


        embed = discord.Embed(title=final, description='', color=0xebde34)
        await ctx.send(embed = embed)


bot.run(TOKEN)
