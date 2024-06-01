# pip install discord.py
import discord
import asyncio
import time
import discord.ui
import nextcord
# pip install requests
from discord.ext import commands
from discord.ext import tasks
import requests as rq
import datetime
import random
from gtts import gTTS
from discord.ui import Button
import keep_alive
# setting
client = commands.Bot(command_prefix='.', intents=discord.Intents.all())
client.remove_command('help')
# Config


class config:
    # IP:PORT | Example: 87.98.246.41:30120 | Use 127.0.0.1:PORT if you're running it on same Server as FiveM Server.
    serverIP = "139.99.24.100:30120"
    # Your Discord Server ID, must be int. | Example: 721939142455459902
    guildID = 1055570554310103210
    # Your Discord Bot Token
    channelID = "1205520470888288286"
# Events


@client.event
async def on_ready():
    print('Bot đã sẵn sàng!')
    print('NẾU bạn có bất kỳ vấn đề gì, hãy thêm tôi vào bất hòa, tôi sẽ giúp bạn.!')
    print('Hanzo#1233')
    client.my_current_task = live_status.start()


async def server(ctx):
    guild = discord.Guild.member_count
    await ctx.send(guild)

# Players Count Function // Callable Everywhere, returns number


def pc():
    try:
        resp = rq.get('http://'+config.serverIP+'/players.json').json()
        return (len(resp))
    except:
        return ('0')
# Tạo Nút


class DefaultView(nextcord.ui.View):
    def __init__(self):
        super().__init__()

        default_button = nextcord.ui.Button(
            label='Menu Lệnh .help', style=nextcord.ButtonStyle.primary)
        default_button.callback = self.default_button_callback
        self.add_item(default_button)

        url_button = nextcord.ui.Button(
            label='Thuê Bot', style=nextcord.ButtonStyle.link, url='https://discord.com/users/995860121013981184')
        self.add_item(url_button)

        url_button = nextcord.ui.Button(
            label='Kết Bạn Phở Bò', style=nextcord.ButtonStyle.link, url='https://fb.com/datbgkepvl')
        self.add_item(url_button)

    async def default_button_callback(self, interaction: nextcord.Interaction):
        await interaction.response.defer(ephemeral=True)
        await interaction.followup.send(f'{interaction.user.mention}', ephemeral=True)
        timenow = time.strftime("%H:%M | %d/%m/%Y")
        result = (
            "```"
            "💕 .id -----  Check Theo ID Vd: .id 12\n"
            "💕 .iddc -----  Check Theo ID Discord Vd: .iddc 1234567891234567 (Đây là check người chơi trong Server đang kết nối Discord với Fivem chứ không phải là thông tin Discord)\n"
            "💕 .job -----  Check TT Theo Tên Vd: .job tên\n"
            "💕 .search -----  Tìm Theo Tên Vd: .search Bạch Hổ\n"
            "💕 .gang -----  Danh Sách Online Gang\n"
            "💕 .ip -----  Hướng Dẫn Vào Server\n"
            "💕 .uptime -----  TT Uptime SERVER\n"
            "💕 .check -----  Người Chơi Trong Server\n"
            "💕 .avatar -----  Check Avatar Của Bạn\n"
            "💕 .user -----  Check Thông tin Discord\n"
            "💕 .n -----  Chị Google Vd: .n lời muốn nói\n"
            "💕 .help -----  Xem các lệnh mới được cập nhật"
            "```"
        )

        result2 = (
            "```"
            "💕 .ca -----  Công An\n"
            "💕 .qy -----  Quân Y\n"
            "💕 .med -----  Bác Sĩ\n"
            "💕 .ch -----  Cứu Hộ"
            "```"
        )

        result3 = (
            "```"
            "💕 .md -----  Ma Đạo\n"
            "💕 .tt -----  Thiên Triều\n"
            "💕 .titans -----  TiTans\n"
            "💕 .cc -----  Cột Chèo\n"
            "💕 .gn -----  Gungnir\n"
            "```"
        )

        result4 = (
            "```"
            "💕.prd -----  Paradise\n"
            "💕 .konoha ----- Konoha\n"
            "💕 .th -----  Thiên Hoàng"
            "```"
        )
        embed = nextcord.Embed(title="BẠCH HỔ GANGS™",
                               description="__*SERVER AnF*__", color=0xfff700)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
        embed.set_author(name="BẠCH HỔ GANGS™",
                         icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.add_field(name="**▔▔▔▔▔▔▔◥ 🧡 ◤▔▔▔▔▔▔▔**",
                        value="\u200b", inline=False)
        embed.add_field(name="⚽ Lệnh Cơ Bản ⚽", value=result, inline=False)
        embed.add_field(name="💖 Lệnh tìm ngành 💖", value=result2, inline=False)
        embed.add_field(name="❀ Lệnh tìm Gang ❀", value=result3, inline=False)
        embed.add_field(name="✌ Lệnh tìm Nhóm ✌", value=result4, inline=False)
        embed.add_field(name="**▔▔▔▔▔▔▔◥ 🧡 ◤▔▔▔▔▔▔▔**",
                        value="\u200b", inline=False)
        embed.set_footer(text=f'copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | AnF | {timenow}')

        await interaction.followup.send(embed=embed, ephemeral=True)

# info


@client.command()
async def user(ctx, member: discord.Member = None):
    # Check if the command is used in the allowed channel
    allowed_channel_id = 1205467153680044063  # Replace with the allowed channel ID
    if ctx.channel.id != allowed_channel_id:
        await ctx.send("Lệnh này chỉ có thể được sử dụng trong kênh Check User.")
        return

    if member is None:
        member = ctx.author
    timenow = time.strftime("%H:%M")
    statuses = {
        discord.Status.online: '`Trực Tuyến`',
        discord.Status.idle: '`Chờ`',
        discord.Status.offline: '`Ngoại Tuyến`',
        discord.Status.dnd: '`Đừng Làm Phiền`',
    }

    response = discord.Embed(
        title=f"ღ Thông Tin Cá Nhân ღ", color=member.color)
    response.set_author(name=member.name, url=member.avatar.url)
    response.set_thumbnail(url=member.avatar.url)
    response.color = discord.Color.random()

    response.add_field(name="ID Discord:", value=str(member.id), inline=False)
    response.add_field(name="Tên Người Dùng:",
                       value=f"<@{member.id}>", inline=False)
    roles_str = ' '.join(
        [f'<@&{r.id}>' for r in member.roles if r.name != "everyone"])
    response.add_field(name="Roles:", value=roles_str, inline=False)
    response.add_field(name="Tình Trạng", value=statuses.get(
        member.status, '`Ngoại Tuyến`'), inline=True)
    join_date = member.joined_at.strftime('%A, %d %B %Y %H:%M').replace('Monday', 'Thứ Hai').replace('Tuesday', 'Thứ Ba').replace('Wednesday', 'Thứ Tư').replace('Thursday', 'Thứ Năm').replace('Friday', 'Thứ Sáu').replace('Saturday', 'Thứ Bảy').replace('Sunday', 'Chủ Nhật').replace('January', 'Tháng Một').replace('February', 'Tháng Hai').replace(
        'March', 'Tháng Ba').replace('April', 'Tháng Tư').replace('May', 'Tháng Năm').replace('June', 'Tháng Sáu').replace('July', 'Tháng Bảy').replace('August', 'Tháng Tám').replace('September', 'Tháng Chín').replace('October', 'Tháng Mười').replace('November', 'Tháng Mười Một').replace('December', 'Tháng Mười Hai')
    response.add_field(name="Ngày Tham Gia Máy Chủ:",
                       value=join_date, inline=False)

    # Sửa đoạn này để hiển thị tháng bằng tiếng Việt và thêm thứ
    creation_date = member.created_at.strftime('%A, %d %B %Y %H:%M').replace('Monday', 'Thứ Hai').replace('Tuesday', 'Thứ Ba').replace('Wednesday', 'Thứ Tư').replace('Thursday', 'Thứ Năm').replace('Friday', 'Thứ Sáu').replace('Saturday', 'Thứ Bảy').replace('Sunday', 'Chủ Nhật').replace('January', 'Tháng Một').replace(
        'February', 'Tháng Hai').replace('March', 'Tháng Ba').replace('April', 'Tháng Tư').replace('May', 'Tháng Năm').replace('June', 'Tháng Sáu').replace('July', 'Tháng Bảy').replace('August', 'Tháng Tám').replace('September', 'Tháng Chín').replace('October', 'Tháng Mười').replace('November', 'Tháng Mười Một').replace('December', 'Tháng Mười Hai')
    response.add_field(name="Ngày Tạo Tài Khoản:",
                       value=creation_date, inline=False)
    response.set_footer(
        text=f"{ctx.message.author} | AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}")
    await ctx.reply(embed=response,  view=DefaultView())

# chi google


@client.command()
async def n(ctx, *args):
    # Kiểm tra xem lệnh được gọi từ kênh chỉ định
    if ctx.channel.id == 1061247621236277268:  # Thay YOUR_SPECIFIC_CHANNEL_ID bằng ID của kênh bạn muốn cho phép
        text = " ".join(args)
        if len(text) > 500:
            await ctx.send("**Vượt quá 500 ký tự rồi. Vui lòng nhập lại.**")
            return
        user = ctx.message.author
        if user.voice is not None:
            try:
                vc = await user.voice.channel.connect()
            except:
                vc = ctx.voice_client
            sound = gTTS(text=text, lang="vi", slow=False)
            sound.save("tts-audio.mp3")
            if vc.is_playing():
                vc.stop()
            source = await nextcord.FFmpegOpusAudio.from_probe("tts-audio.mp3", method="fallback")

            vc.play(source)

            # Đặt hẹn giờ 2 phút để rời kênh thoại
            await asyncio.sleep(120)
            await vc.disconnect()
        else:
            await ctx.send("**Vui lòng tham gia kênh thoại để sử dụng.**")
    else:
        await ctx.send("**Lệnh này chỉ có thể được sử dụng trong kênh chị Google.**")
# avatar


@client.command()
async def avatar(ctx, member: discord.Member = None):
    # Kiểm tra xem message được gửi từ kênh có ID mong muốn
    allowed_channel_id = 1205467153680044063  # Thay ID kênh mong muốn vào đây
    if ctx.channel.id != allowed_channel_id:
        await ctx.send("Lệnh này chỉ có thể được sử dụng trong kênh Check User.")
        return

    if member is None:
        member = ctx.author

    timenow = time.strftime("%H:%M")

    embed = discord.Embed(
        title=f"**Avatar của {member.name}**", color=member.color)

    embed.set_author(name="**BẠCH HỔ GANGS™**",
                     icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")

    embed.set_image(url=member.avatar.url)
    embed.set_footer(
        text=f"{ctx.message.author} | AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}")

    await ctx.send(embed=embed, view=DefaultView())


# Say Commands
@client.command(pass_content=True, aliases=['s'])
@commands.has_permissions(administrator=True)
async def say(ctx, *, text):

    try:
        await ctx.message.delete()
        timenow = time.strftime("%H:%M")
        embed = discord.Embed(title="", description=" ", color=0xfff705)
        embed.set_author(name="**BẠCH HỔ GANGS™**",
                         icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.add_field(name="Message:", value=text, inline=False)
        embed.set_footer(
            text=f"{ctx.message.author} | AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}")
        await ctx.send(embed=embed)
    except Exception as err:
        print(err)


@client.command(pass_context=True, aliases=['hs'])
@commands.has_permissions(administrator=True)
async def hsay(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(text)
# Uptime
last_boot_time = datetime.datetime.now()

# Tính thời gian uptime từ thời điểm server được khởi động lần cuối đến thời điểm hiện tại


def get_uptime():
    uptime = datetime.datetime.now() - last_boot_time
    return str(uptime).split('.')[0]  # Chuyển đổi sang định dạng giờ:phút


@client.command()
async def uptime(ctx):
    global last_boot_time
    if ctx.channel.id != int(config.channelID):
        await ctx.send("Bạn không thể sử dụng lệnh này trong kênh này.")
        return

    resp = rq.get('http://' + config.serverIP + '/players.json').json()

    if not resp:
        embed = discord.Embed(title="BẠCH HỔ GANGS™",
                              description="**Uptime**", color=0xff1414)
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
        embed.add_field(name="**Thông tin Server:**",
                        value="```Server Đang Reset Vui Lòng Chờ Khoảng 2 Phút```", inline=False)
        embed.set_footer(text=f'copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {
                         time.strftime("%H:%M | %d/%m/%Y")}')
        await ctx.send(embed=embed)
        return

    content = ""
    timenow = time.strftime("%H:%M | %d/%m/%Y")
    police_count = 0
    ems_count = 0
    mechanic_count = 0
    qy_count = 0
    bs_count = 0
    for player in resp:
        if "name" not in player:
            continue
        name = player["name"]
        if "|" not in name:
            continue
        job = name.split("|")[0].strip()
        if job == "CA" or job == "PGĐCA |" or job == "GĐCA |" or job == "SWAT |" or job == "S.W.A.T |" or job == "QLS.W.A.T |":
            police_count += 1
        elif job == "Quân Y":
            qy_count += 1
        elif job == "QLMED" or job == "MED |" or job == "PGĐBS" or job == "GĐBS":
            ems_count += 1
        elif job == "CH" or job == "GSCH |" or job == "PGĐCH |" or job == "QLCH |" or job == "GĐCH |":
            mechanic_count += 1
        if job == "QLMED" or job == "MED |" or job == "PGĐBS |" or job == "GĐBS |" or job == "Quân Y |":
            bs_count += 1

    total_count = len(resp)
    result = f"""```Người Chơi: {total_count}/550 | 👮‍♀️: {police_count}
        🚨: {qy_count} 👨‍⚕️: {ems_count} 🔧: {mechanic_count}```"""
    result2 = f"""```Người Chơi: {
        total_count}/550 | 👮‍♀️: {police_count} 👨‍⚕️: {bs_count} 🔧: {mechanic_count}```"""
    embed = discord.Embed(title="BẠCH HỔ GANGS™", description=f"```Uptime: {
                          get_uptime()}```", color=0xff1414)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
    embed.add_field(
        name="Tổng Người Chơi Trong Ngành (Icon QY = 🚨)", value=result, inline=False)
    embed.add_field(name="Tổng Người Chơi Trong Ngành (Trong F10)",
                    value=result2, inline=False)
    embed.set_footer(text=f'copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
    await ctx.send(embed=embed,  view=DefaultView())
    if total_count == 0:
        last_boot_time = datetime.datetime.now()
# auto nhắn tin


@client.event
async def on_message(message):
    # Ignore messages from bots to avoid infinite loops
    if message.author.bot:
        return

    # Handle commands
    await client.process_commands(message)

    # Handle auto-reply
    await auto_reply(message)


async def auto_reply(message):
    # Check if message is in the designated channel
    if message.channel.id == 1061246138801459201 and not message.author.bot:
        # Delete previous bot messages in the channel
        async for old_message in message.channel.history():
            if old_message.author == client.user:
                await old_message.delete()

        # Create embed and send auto-reply message
        color = discord.Color.from_rgb(random.randint(
            0, 255), random.randint(0, 255), random.randint(0, 255))
        timenow = time.strftime("%H:%M | %d/%m/%Y")
        embed = discord.Embed(title="⚠ Vui Lòng Đọc Kỹ Để Tránh Lừa Đảo ⚠", description="```✔ Luôn tỉnh táo trong mọi trường hợp. Khi mua bán hãy tìm hiểu kỹ người bán có thật sự uy tín hay không để tránh mất tiền đáng tiếc.\n\n✔ Khi đăng bán hoặc mua trên Discord của chúng tôi, bạn bắt buộc phải có link Steam. Nếu không có link Steam, bạn sẽ bị kích khỏi Discord này.\n\n✔ Trước khi thực hiện giao dịch, hãy kiểm tra thông tin người bán trong Profiles của Discord có ngày tạo tài khoản, ngày vào máy chủ đã lâu hay chưa. Có máy chủ chung hay không.\n\n✔ Nếu bạn không chắc chắn về độ uy tín của người đó. Bạn có thể nhờ ADMIN trung gian giúp đỡ.\n\n✔ Chúng tôi không chịu trách nhiệm trong mọi trường hợp bị scam!!!```", color=color)
        embed.set_footer(text=f'copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await message.channel.send(embed=embed)


# tìm theo tên
@client.command()
async def job(ctx, *args):
    if ctx.channel.id != int(config.channelID):
        await ctx.send("Bạn không thể sử dụng lệnh này trong kênh này.")
        return
    name = ' '.join(args)
    if not name:
        await ctx.send('<@{}>, Hãy nhập tên người chơi'.format(ctx.author.id))
        return

    resp = rq.get('http://'+config.serverIP+'/players.json')
    found_player = False
    for _ in resp.json():
        if name.lower() == _['name'].lower():
            found_player = True
            steam_id = ''
            discord_id = ''
            for arg in _['identifiers']:
                arg = arg.lower()
                if arg.startswith('steam:'):
                    steam_id = arg[6:]
                    # Chuyển SteamID sang SteamID64
                    steam_id = int(steam_id, 16)
                elif arg.startswith('discord:'):
                    discord_id = arg[8:]

            pembed = discord.Embed(
                title='𝕋ℍÔℕ𝔾 𝕋𝕀ℕ ℕ𝔾ƯỜ𝕀 ℂℍƠ𝕀', color=discord.Color.dark_green())
            pembed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
            pembed.add_field(
                name='```Tên Nhân Vật :``` {}\u200b \u200b \u200b \u200b ```ID :```{}\u200b \u200b \u200b \u200b ```Ping :``` {}'.format(_[
                                                                                                                                         'name'], _['id'], _['ping']),
                value='\u200b',
                inline=False
            )

            if steam_id:
                pembed.add_field(
                    name='```Steam :``` ', value=f'https://steamcommunity.com/profiles/{steam_id}', inline=False)
            if discord_id:
                pembed.add_field(name='```Discord :``` ',
                                 value=f'<@{discord_id}>', inline=False)
            discord_user = await client.fetch_user(discord_id)
            discord_name = f"{discord_user.name}#{discord_user.discriminator}"
            pembed.add_field(name='```Discord ID :``` ', value=f'{
                             discord_name}\n[Nhấp vào đây để liên hệ](https://discord.com/users/{discord_id})', inline=False)

            await ctx.send(embed=pembed,  view=DefaultView())
            break

    if not found_player:
        timenow = time.strftime("%H:%M | %d/%m/%Y")
        nembed = discord.Embed(title='__**Tìm Kiếm Người Chơi**™__',
                               description='Không tìm thấy người chơi nào có tên "{}".'.format(name), color=discord.Color.dark_red())
        nembed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
        nembed.set_footer(text=f'copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
    await ctx.send(embed=nembed,  view=DefaultView())

# tìm danh sách search


@client.command()
async def search(ctx, *, name: str):
    if ctx.channel.id != int(config.channelID):
        await ctx.send("Bạn không thể sử dụng lệnh này trong kênh này.")
        return

    timenow = time.strftime("%H:%M | %d/%m/%Y")
    resp = rq.get('http://' + config.serverIP + '/players.json').json()
    matching_players = [player for player in resp if name.lower().replace(
        " ", "") in player['name'].lower().replace(" ", "")]
    total_matching_players = len(matching_players)

    if total_matching_players > 0:
        if total_matching_players > 25:
            pages = []
            for i in range(0, total_matching_players, 25):
                page = discord.Embed(title='__**Tìm Kiếm Người Chơi**™__',
                                     description=f'Người chơi trong máy chủ có tên chứa "{name}"', color=discord.Color.blurple())
                page.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
                page.set_footer(text=f'Tổng số kết quả tìm thấy: {
                                total_matching_players} | copyright © DatKaa | AnF | {timenow}')
                for index, player in enumerate(matching_players[i:i+25]):
                    page.add_field(name=f"```#{
                                   i+index+1} {player['name']}```", value='ID : ' + str(player['id']), inline=False)

                pages.append(page)

            # Implement a paginator (you need to define the paginator function)
            await paginator(ctx, pages)
        else:
            embed = discord.Embed(title='__**Tìm Kiếm Người Chơi**™__',
                                  description=f'Người chơi trong máy chủ có tên chứa "{name}"', color=discord.Color.blurple())
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
            embed.set_footer(text=f'Tổng số kết quả tìm thấy: {
                             total_matching_players} | copyright © DatKaa | AnF | {timenow}')
            for index, player in enumerate(matching_players):
                embed.add_field(name=f"```#{
                                index+1} {player['name']}```", value='ID : ' + str(player['id']), inline=False)
            await ctx.send(embed=embed,  view=DefaultView())
    else:
        embed = discord.Embed(title='__**Tìm Kiếm Người Chơi**™__',
                              description=f'Không có người chơi nào có tên chứa "{name}"', color=discord.Color.blurple())
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
        embed.set_footer(text=f'Tổng số người chơi : {len(
            resp)} | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | AnF | {timenow}')
        await ctx.send(embed=embed,  view=DefaultView())
# Define a simple paginator function


async def paginator(ctx, pages):
    current_page = 0
    message = await ctx.send(embed=pages[current_page])

    await message.add_reaction("⬅️")
    await message.add_reaction("➡️")

    def check(reaction, user):
        return user == ctx.message.author and str(reaction.emoji) in ["⬅️", "➡️"]

    while True:
        try:
            reaction, user = await ctx.bot.wait_for("reaction_add", timeout=60, check=check)

            if str(reaction.emoji) == "➡️" and current_page < len(pages) - 1:
                current_page += 1
                await message.edit(embed=pages[current_page])
            elif str(reaction.emoji) == "⬅️" and current_page > 0:
                current_page -= 1
                await message.edit(embed=pages[current_page])

            await message.remove_reaction(reaction, user)
        except TimeoutError:
            break

# Danh sách Gang


@client.command()
async def gang(ctx):
    if ctx.channel.id != int(config.channelID):
        await ctx.send("Bạn không thể sử dụng lệnh này trong kênh này.")
        return
    timenow = time.strftime("%H:%M | %d/%m/%Y")
    resp = rq.get('http://' + config.serverIP + '/players.json').json()

    gangster_list = {}
    for player in resp:
        name = player['name'].lower()
        if 'ma đạo |' in name or 'mđ |' in name:
            gangster_list['Ma Đạo'] = gangster_list.get('Ma Đạo', 0) + 1
        if 'thiên triều |' in name or 'tt |' in name:
            gangster_list['Thiên Triều'] = gangster_list.get(
                'Thiên Triều', 0) + 1
        if 'gn |' in name or 'gungnir |' in name:
            gangster_list['Gungnir'] = gangster_list.get('Gungnir', 0) + 1
        if 'thiên hoàng |' in name:
            gangster_list['Thiên Hoàng'] = gangster_list.get(
                'Thiên Hoàng', 0) + 1
        if 'cột chèo |' in name or 'cc |' in name:
            gangster_list['Cột Chèo'] = gangster_list.get('Cột Chèo', 0) + 1
        if 'paradise |' in name:
            gangster_list['Paradise'] = gangster_list.get('Paradise', 0) + 1
        if 'konoha |' in name or 'konoha |' in name:
            gangster_list['Konoha'] = gangster_list.get('Konoha', 0) + 1
        elif 'titans |' in name or 'titans |' in name:
            gangster_list['TiTans'] = gangster_list.get('TiTans', 0) + 1

    embed = discord.Embed(title="__*DANH SÁCH GANG, NHÓM*__", color=0x00ff00)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
    embed.set_footer(text="copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | " + timenow)

    count = 1
    for gangster in gangster_list:
        embed.add_field(name=f"```#{count} {gangster}```", value=f"```Đang Online: {
                        gangster_list[gangster]}```", inline=False)
        count += 1
    await ctx.send(embed=embed,  view=DefaultView())
# Thông tin theo ID DISCORD


@client.command()
async def iddc(ctx, discord_id):
    if ctx.channel.id != int(config.channelID):
        await ctx.send("Bạn không thể sử dụng lệnh này trong kênh này.")
        return

    found_player = False

    if not discord_id:
        await ctx.send('<@{}>, Thông tin người chơi trong Server')
        return

    resp = rq.get('http://'+config.serverIP+'/players.json')

    for player in resp.json():
        for identifier in player['identifiers']:
            if identifier.startswith('discord:') and discord_id in identifier:
                found_player = True
                steam_id = ''
                discord_id = ''
                for arg in player['identifiers']:
                    arg = arg.lower()
                    if arg.startswith('steam:'):
                        steam_id = arg[6:]
                        # Chuyển SteamID sang SteamID64
                        steam_id = int(steam_id, 16)
                    elif arg.startswith('discord:'):
                        discord_id = arg[8:]

                timenow = time.strftime("%H:%M | %d/%m/%Y")
                pembed = discord.Embed(
                    title='𝕋ℍÔℕ𝔾 𝕋𝕀ℕ ℕ𝔾ƯỜ𝕀 ℂℍƠ𝕀', color=discord.Color.dark_green())
                pembed.set_thumbnail(
                    url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
                pembed.add_field(
                    name='Tên INGAME : {}\u200b \u200b \u200b \u200b ID : {}\u200b \u200b \u200b \u200b Ping : {}'.format(
                        player['name'], player['id'], player['ping']),
                    value='\u200b',
                    inline=False
                )
                if steam_id:
                    pembed.add_field(
                        name='Link Steam : ', value=f'https://steamcommunity.com/profiles/{steam_id}', inline=False)
                if discord_id:
                    pembed.add_field(name='Discord Tag : ',
                                     value=f'<@{discord_id}>', inline=False)
                    discord_user = await client.fetch_user(discord_id)
                    discord_name = f"{discord_user.name}#{
                        discord_user.discriminator}"
                    pembed.add_field(name='Discord ID : ', value=f'{
                                     discord_name}\n[Nhấp vào đây để liên hệ](https://discord.com/users/{discord_id})', inline=False)
                    pembed.set_footer(
                        text=f'copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')

                await ctx.send(embed=pembed,  view=DefaultView())

    if not found_player:
        timenow = time.strftime("%H:%M | %d/%m/%Y")
        pembed_offline = discord.Embed(
            title='BẠCH HỔ GANGS™', color=discord.Color.dark_green())
        pembed_offline.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
        pembed_offline.add_field(
            name='Người chơi không online', value='Vui lòng kiểm tra lại ID', inline=False)
        pembed_offline.set_footer(text=f'copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')

        await ctx.send(embed=pembed_offline,  view=DefaultView())

# Thông tin theo ID


@client.command(aliases=['playerid', 'loid', 'server'])
async def id(ctx, pids):
    if ctx.channel.id != int(config.channelID):
        await ctx.send("Bạn không thể sử dụng lệnh này trong kênh này.")
        return
    found_player = False
    if not pids:
        await ctx.send('<@{}>, Thông tin người chơi trong Server')
        return
    resp = rq.get('http://'+config.serverIP+'/players.json')
    for _ in resp.json():
        if _['id'] == int(pids):
            found_player = True
            steam_id = ''
            discord_id = ''
            for arg in _['identifiers']:
                arg = arg.lower()
                if arg.startswith('steam:'):
                    steam_id = arg[6:]
                    # Chuyển SteamID sang SteamID64
                    steam_id = int(steam_id, 16)
                elif arg.startswith('discord:'):
                    discord_id = arg[8:]
            timenow = time.strftime("%H:%M | %d/%m/%Y")
            pembed = discord.Embed(
                title='𝕋ℍÔℕ𝔾 𝕋𝕀ℕ ℕ𝔾ƯỜ𝕀 ℂℍƠ𝕀', color=discord.Color.dark_green())
            pembed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
            pembed.add_field(
                name='Tên INGAME : {}\u200b \u200b \u200b \u200b ID : {}\u200b \u200b \u200b \u200b Ping : {}'.format(_[
                                                                                                                      'name'], _['id'], _['ping']),
                value='\u200b',
                inline=False
            )
            if steam_id:
                pembed.add_field(
                    name='Link Steam : ', value=f'https://steamcommunity.com/profiles/{steam_id}', inline=False)
            if discord_id:
                pembed.add_field(name='Discord Tag : ',
                                 value=f'<@{discord_id}>', inline=False)
                discord_user = await client.fetch_user(discord_id)
                discord_name = f"{discord_user.name}#{
                    discord_user.discriminator}"
                pembed.add_field(name='Discord ID : ', value=f'{
                                 discord_name}\n[Nhấp vào đây để liên hệ](https://discord.com/users/{discord_id})', inline=False)
                pembed.set_footer(text=f'copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')

            await ctx.send(embed=pembed,  view=DefaultView())

    if not found_player:
        timenow = time.strftime("%H:%M | %d/%m/%Y")
        pembed_offline = discord.Embed(
            title='BẠCH HỔ GANGS™', color=discord.Color.dark_green())
        pembed_offline.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
        pembed_offline.add_field(
            name='Người chơi không online', value='Vui lòng kiểm tra lại ID', inline=False)
        pembed_offline.set_footer(text=f'copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
    await ctx.send(embed=pembed_offline,  view=DefaultView())
# HD vào


@client.command()
async def ip(ctx):
    if ctx.channel.id != int(config.channelID):
        await ctx.send("Bạn không thể sử dụng lệnh này trong kênh này.")
        return
    content = ""
    timenow = time.strftime("%H:%M | %d/%m/%Y")
    result = f"""```Vào FiveM tìm ACE And Friends và Connect```"""
    result2 = f"""```Bấm F8 và nhập IP: connect anfcity.com```"""
    embed = discord.Embed(title="Server ACE And Friends™",
                          description="**Hướng dẫn vào server AnF**", color=0xff1414)
    embed.set_thumbnail(
        url="https://servers-live.fivem.net/servers/icon/86zggv/1908881564.png")
    embed.add_field(name="**Cách 1**", value=result, inline=False)
    embed.add_field(name="**Cách 2**", value=result2, inline=False)
    embed.set_footer(text=f'copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
    await ctx.send(embed=embed, content=content,  view=DefaultView())
# help commands


@client.command()
async def help(ctx):
    if ctx.channel.id != int(config.channelID):
        await ctx.send("Bạn không thể sử dụng lệnh này trong kênh này.")
        return

    timenow = time.strftime("%H:%M | %d/%m/%Y")

    result = (
        "```"
        "💕 .id -----  Check Theo ID Vd: .id 12\n"
        "💕 .iddc -----  Check Theo ID Discord Vd: .iddc 1234567891234567 (Đây là check người chơi trong Server đang kết nối Discord với Fivem chứ không phải là thông tin Discord)\n"
        "💕 .job -----  Check TT Theo Tên Vd: .job tên\n"
        "💕 .search -----  Tìm Theo Tên Vd: .search Bạch Hổ\n"
        "💕 .gang -----  Danh Sách Online Gang\n"
        "💕 .ip -----  Hướng Dẫn Vào Server\n"
        "💕 .uptime -----  TT Uptime SERVER\n"
        "💕 .check -----  Người Chơi Trong Server\n"
        "💕 .avatar -----  Check Avatar Của Bạn\n"
        "💕 .user -----  Check Thông tin Discord\n"
        "💕 .n -----  Chị Google Vd: .n lời muốn nói\n"
        "💕 .help -----  Xem các lệnh mới được cập nhật"
        "```"
    )

    result2 = (
        "```"
        "💕 .ca -----  Công An\n"
        "💕 .qy -----  Quân Y\n"
        "💕 .med -----  Bác Sĩ\n"
        "💕 .ch -----  Cứu Hộ"
        "```"
    )

    result3 = (
        "```"
        "💕 .md -----  Ma Đạo\n"
        "💕 .tt -----  Thiên Triều\n"
        "💕 .titans -----  TiTans\n"
        "💕 .cc -----  Cột Chèo\n"
        "💕 .gn -----  Gungnir\n"
        "```"
    )

    result4 = (
        "```"
        "💕.prd -----  Paradise\n"
        "💕 .konoha ----- Konoha\n"
        "💕 .th -----  Thiên Hoàng"
        "```"
    )
    embed = discord.Embed(title="BẠCH HỔ GANGS™",
                          description="__*SERVER AnF*__", color=0xfff700)
    embed.set_thumbnail(
        url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
    embed.set_author(name="BẠCH HỔ GANGS™",
                     icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
    embed.add_field(name="**▔▔▔▔▔▔▔◥ 🧡 ◤▔▔▔▔▔▔▔**",
                    value="\u200b", inline=False)
    embed.add_field(name="⚽ Lệnh Cơ Bản ⚽", value=result, inline=False)
    embed.add_field(name="💖 Lệnh tìm ngành 💖", value=result2, inline=False)
    embed.add_field(name="❀ Lệnh tìm Gang ❀", value=result3, inline=False)
    embed.add_field(name="✌ Lệnh tìm Nhóm ✌", value=result4, inline=False)
    embed.add_field(name="**▔▔▔▔▔▔▔◥ 🧡 ◤▔▔▔▔▔▔▔**",
                    value="\u200b", inline=False)
    embed.set_footer(text=f'copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | AnF | {timenow}')

    message = await ctx.send(embed=embed, view=DefaultView())

# Tất cả trong server


@client.command()
async def check(ctx):
    if ctx.channel.id != int(config.channelID):
        await ctx.send("Bạn không thể sử dụng lệnh này trong kênh này.")
        return
    timenow = time.strftime("%H:%M | %d/%m/%Y")
    resp = rq.get('http://' + config.serverIP + '/players.json').json()
    total_players = len(resp)
    if len(resp) > 25:
        players_chunked = [resp[i:i+25] for i in range(0, len(resp), 25)]
        for chunk in players_chunked:
            embed = discord.Embed(title='__**BẠCH HỔ GANGS™**__',
                                  description='__**Người chơi trong máy chủ**__', color=discord.Color.blurple())
            embed.set_thumbnail(
                url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
            embed.set_author(
                name="BẠCH HỔ GANGS™", icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
            embed.set_footer(text=f'Tổng số người chơi : {
                             total_players} | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | AnF |{timenow}')
            for player in chunk:
                embed.add_field(
                    name=f'```{player["name"]} - ID: {player["id"]}```', value='\u200b', inline=True)
            await ctx.send(embed=embed,  view=DefaultView())
    else:
        embed = discord.Embed(title='__**BẠCH HỔ GANGS™**__',
                              description='Người chơi trong máy chủ', color=discord.Color.blurple())
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
        embed.set_author(name="BẠCH HỔ GANGS™",
                         icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_footer(text=f'Tổng số người chơi : {
                         total_players} | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | AnF | {timenow}')
        for player in resp:
            embed.add_field(
                name=f'```{player["name"]} - ID: {player["id"]}```', value='\u200b', inline=True)
        await ctx.send(embed=embed,  view=DefaultView())

# tÌM Gang
# công an


@client.command(aliases=['congan'])
async def ca(ctx):
    if ctx.channel.id != int(config.channelID):
        await ctx.send("Bạn không thể sử dụng lệnh này trong kênh này.")
        return

    timenow = time.strftime("%H:%M | %d/%m/%Y")
    resp = rq.get('http://' + config.serverIP + '/players.json').json()
    ca_players = []
    swat_players = []
    qlca_players = []
    quan_y_players = []

    for player in resp:
        if 'name' in player:
            if any(player['name'].startswith(prefix) for prefix in ['CA |']):
                ca_players.append(player)
            elif any(player['name'].lower().startswith(prefix.lower()) for prefix in ['SWAT |', 'S.W.A.T |', 'PGDSWAT |', 'GDSWAT |', 'QLSWAT |']):
                swat_players.append(player)
            elif any(player['name'].lower().startswith(prefix.lower()) for prefix in ['QLCA |', 'PGĐCA |', 'GĐCA |']):
                qlca_players.append(player)
            elif any(player['name'].startswith(prefix) for prefix in ['Quân Y |']):
                quan_y_players.append(player)

    ca_players = sorted(ca_players, key=lambda k: k['name'])
    swat_players = sorted(swat_players, key=lambda k: k['name'])
    qlca_players = sorted(qlca_players, key=lambda k: k['name'])
    quan_y_players = sorted(quan_y_players, key=lambda k: k['name'])

    if len(ca_players) > 0 or len(swat_players) > 0 or len(qlca_players) > 0 or len(quan_y_players) > 0:
        embed = discord.Embed(color=discord.Color.blurple())
        embed.set_author(name="BẠCH HỔ GANGS™",
                         icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')

        if len(ca_players) > 0:
            paginated_ca_players = [ca_players[i:i + 25]
                                    for i in range(0, len(ca_players), 25)]
            for index, page in enumerate(paginated_ca_players, start=1):
                paginated_result = '\n'.join(f'#{count} [ID:{player["id"]}] {
                                             player["name"]}' for count, player in enumerate(page, start=1))
                embed.add_field(name=f"Công An Online: {len(
                    ca_players)} - Trang {index}", value=f'```{paginated_result}```', inline=False)

        if len(swat_players) > 0:
            paginated_swat_players = [swat_players[i:i + 25]
                                      for i in range(0, len(swat_players), 25)]
            for index, page in enumerate(paginated_swat_players, start=1):
                paginated_result = '\n'.join(f'#{count} [ID:{player["id"]}] {
                                             player["name"]}' for count, player in enumerate(page, start=1))
                embed.add_field(name=f"SWAT Online: {len(
                    swat_players)} - Trang {index}", value=f'```{paginated_result}```', inline=False)

        if len(qlca_players) > 0:
            paginated_qlca_players = [qlca_players[i:i + 25]
                                      for i in range(0, len(qlca_players), 25)]
            for index, page in enumerate(paginated_qlca_players, start=1):
                paginated_result = '\n'.join(f'#{count} [ID:{player["id"]}] {
                                             player["name"]}' for count, player in enumerate(page, start=1))
                embed.add_field(name=f"QLCA Online: {len(
                    qlca_players)} - Trang {index}", value=f'```{paginated_result}```', inline=False)

        if len(quan_y_players) > 0:
            paginated_quan_y_players = [quan_y_players[i:i + 25]
                                        for i in range(0, len(quan_y_players), 25)]
            for index, page in enumerate(paginated_quan_y_players, start=1):
                paginated_result = '\n'.join(f'#{count} [ID:{player["id"]}] {
                                             player["name"]}' for count, player in enumerate(page, start=1))
                embed.add_field(name=f"Quân Y Online: {len(
                    quan_y_players)} - Trang {index}", value=f'```{paginated_result}```', inline=False)

        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())
    else:
        embed = discord.Embed(title='__**Danh sách Công An, Quân Y**__', description='```Không có Công An, Quân Y nào Online```',
                              color=discord.Color.blurple())
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
        embed.set_author(
            name="BẠCH HỔ GANGS™",
            icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())

# 2 QUÂN Y


@client.command(aliases=['quany'])
async def qy(ctx):
    if ctx.channel.id != int(config.channelID):
        await ctx.send("Bạn không thể sử dụng lệnh này trong kênh này.")
        return

    timenow = time.strftime("%H:%M | %d/%m/%Y")
    resp = rq.get('http://' + config.serverIP + '/players.json').json()
    ca_players = []

    for player in resp:
        if any(player['name'].startswith(prefix) for prefix in ['Quân Y |']):
            ca_players.append(player)

    # sắp xếp theo tên bảng chữ cái
    ca_players = sorted(ca_players, key=lambda k: k['name'])

    if len(ca_players) > 0:
        embed = discord.Embed(color=discord.Color.blurple())
        embed.set_author(name="BẠCH HỔ GANGS™",
                         icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')

        paginated_players = [ca_players[i:i + 25]
                             for i in range(0, len(ca_players), 25)]

        for index, page in enumerate(paginated_players, start=1):
            paginated_result = '\n'.join(f'#{count} [ID:{player["id"]}] {
                                         player["name"]}' for count, player in enumerate(page, start=1) if player.get('group') != 'Quân Y |')
            embed.add_field(name=f"Quân Y Online: {len(
                ca_players)} - Trang {index}", value=f'```{paginated_result}```', inline=False)

        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())
    else:
        embed = discord.Embed(title='__**Danh sách Quân Y**__', description='```Không có Quân Y nào Online```',
                              color=discord.Color.blurple())
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
        embed.set_author(
            name="BẠCH HỔ GANGS™",
            icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())
# 3 Cứu Hộ


@client.command(aliases=['cuuho'])
async def ch(ctx):
    if ctx.channel.id != int(config.channelID):
        await ctx.send("Bạn không thể sử dụng lệnh này trong kênh này.")
        return

    timenow = time.strftime("%H:%M | %d/%m/%Y")
    resp = rq.get('http://' + config.serverIP + '/players.json').json()
    ch_players = []
    qlch_players = []

    for player in resp:
        if 'name' in player:
            if any(player['name'].startswith(prefix) for prefix in ['CH |']):
                ch_players.append(player)
            elif any(player['name'].lower().startswith(prefix.lower()) for prefix in ['QLCH |', 'GSCH |', 'PGĐCH |', 'GĐCH |', 'PGDCH |', 'GDCH |']):
                qlch_players.append(player)

    ch_players = sorted(ch_players, key=lambda k: k['name'])
    qlch_players = sorted(qlch_players, key=lambda k: k['name'])

    if len(ch_players) > 0 or len(qlch_players) > 0:
        embed = discord.Embed(color=discord.Color.blurple())
        embed.set_author(name="BẠCH HỔ GANGS™",
                         icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')

        if len(ch_players) > 0:
            paginated_ch_players = [ch_players[i:i + 25]
                                    for i in range(0, len(ch_players), 25)]
            for index, page in enumerate(paginated_ch_players, start=1):
                paginated_result = '\n'.join(f'#{count} [ID:{player["id"]}] {
                                             player["name"]}' for count, player in enumerate(page, start=1))
                embed.add_field(name=f"CH Online: {len(
                    ch_players)} - Trang {index}", value=f'```{paginated_result}```', inline=False)

        if len(qlch_players) > 0:
            paginated_qlch_players = [qlch_players[i:i + 25]
                                      for i in range(0, len(qlch_players), 25)]
            for index, page in enumerate(paginated_qlch_players, start=1):
                paginated_result = '\n'.join(f'#{count} [ID:{player["id"]}] {
                                             player["name"]}' for count, player in enumerate(page, start=1))
                embed.add_field(name=f"QLCH Online: {len(
                    qlch_players)} - Trang {index}", value=f'```{paginated_result}```', inline=False)

        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())
    else:
        embed = discord.Embed(title='__**Danh sách CH**__', description='```Không có CH hoặc Quản Lý CH nào Online```',
                              color=discord.Color.blurple())
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
        embed.set_author(
            name="BẠCH HỔ GANGS™",
            icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())

# 4 MED


@client.command()
async def med(ctx):
    if ctx.channel.id != int(config.channelID):
        await ctx.send("Bạn không thể sử dụng lệnh này trong kênh này.")
        return

    timenow = time.strftime("%H:%M | %d/%m/%Y")
    resp = rq.get('http://' + config.serverIP + '/players.json').json()
    med_players = []
    quan_y_players = []
    qlmed_players = []

    for player in resp:
        if 'name' in player:
            if any(player['name'].startswith(prefix) for prefix in ['MED |']):
                med_players.append(player)
            elif any(player['name'].startswith(prefix) for prefix in ['Quân Y |']):
                quan_y_players.append(player)
            elif any(player['name'].lower().startswith(prefix.lower()) for prefix in ['QLMED |', 'GĐBS |', 'PGĐBS |', 'GDBS |', 'PGDBS |']):
                qlmed_players.append(player)

    med_players = sorted(med_players, key=lambda k: k['name'])
    quan_y_players = sorted(quan_y_players, key=lambda k: k['name'])
    qlmed_players = sorted(qlmed_players, key=lambda k: k['name'])

    if len(med_players) > 0 or len(quan_y_players) > 0 or len(qlmed_players) > 0:
        embed = discord.Embed(color=discord.Color.blurple())
        embed.set_author(name="BẠCH HỔ GANGS™",
                         icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')

        if len(med_players) > 0:
            paginated_med_players = [med_players[i:i + 25]
                                     for i in range(0, len(med_players), 25)]
            for index, page in enumerate(paginated_med_players, start=1):
                paginated_result = '\n'.join(f'#{count} [ID:{player["id"]}] {
                                             player["name"]}' for count, player in enumerate(page, start=1))
                embed.add_field(name=f"MED Online: {len(
                    med_players)} - Trang {index}", value=f'```{paginated_result}```', inline=False)

        if len(quan_y_players) > 0:
            paginated_quan_y_players = [quan_y_players[i:i + 25]
                                        for i in range(0, len(quan_y_players), 25)]
            for index, page in enumerate(paginated_quan_y_players, start=1):
                paginated_result = '\n'.join(f'#{count} [ID:{player["id"]}] {
                                             player["name"]}' for count, player in enumerate(page, start=1))
                embed.add_field(name=f"Quân Y Online: {len(
                    quan_y_players)} - Trang {index}", value=f'```{paginated_result}```', inline=False)

        if len(qlmed_players) > 0:
            paginated_qlmed_players = [qlmed_players[i:i + 25]
                                       for i in range(0, len(qlmed_players), 25)]
            for index, page in enumerate(paginated_qlmed_players, start=1):
                paginated_result = '\n'.join(f'#{count} [ID:{player["id"]}] {
                                             player["name"]}' for count, player in enumerate(page, start=1))
                embed.add_field(name=f"QLMED Online: {len(
                    qlmed_players)} - Trang {index}", value=f'```{paginated_result}```', inline=False)

        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())
    else:
        embed = discord.Embed(title='__**Danh sách MED , Quân Y**__', description='```Không có MED, Quân Y nào Online```',
                              color=discord.Color.blurple())
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
        embed.set_author(
            name="BẠCH HỔ GANGS™",
            icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())

# 5 Gungnir


@client.command(aliases=['gungnir'])
async def gn(ctx):
    if ctx.channel.id != int(config.channelID):
        await ctx.send("Bạn không thể sử dụng lệnh này trong kênh này.")
        return
    timenow = time.strftime("%H:%M | %d/%m/%Y")
    resp = rq.get('http://' + config.serverIP + '/players.json').json()
    hacma_players = []
    hm_players = []
    for player in resp:
        if ('group' in player and player['group'] == 'Gungnir |') or ('name' in player and any(player['name'].lower().startswith(prefix.lower()) for prefix in ['gungnir |'])):
            hacma_players.append(player)
        elif ('group' in player and player['group'] == 'GN |') or ('name' in player and any(player['name'].lower().startswith(prefix.lower()) for prefix in ['GN |'])):
            hm_players.append(player)

    hacma_players = sorted(hacma_players, key=lambda k: k['name'])
    hm_players = sorted(hm_players, key=lambda k: k['name'])

    if len(hacma_players) > 0 or len(hm_players) > 0:
        embed = discord.Embed(color=discord.Color.blurple())
        embed.set_author(name="BẠCH HỔ GANGS™",
                         icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')

        if len(hacma_players) > 0:
            paginated_hacma_players = [hacma_players[i:i + 25]
                                       for i in range(0, len(hacma_players), 25)]
            for index, page in enumerate(paginated_hacma_players, start=1):
                paginated_result = '\n'.join(f'#{count} [ID:{player["id"]}] {
                                             player["name"]}' for count, player in enumerate(page, start=1))
                embed.add_field(name=f"Gungnir Online: {len(
                    hacma_players)} - Trang {index}", value=f'```{paginated_result}```', inline=False)

        if len(hm_players) > 0:
            paginated_hm_players = [hm_players[i:i + 25]
                                    for i in range(0, len(hm_players), 25)]
            for index, page in enumerate(paginated_hm_players, start=1):
                paginated_result = '\n'.join(f'#{count} [ID:{player["id"]}] {
                                             player["name"]}' for count, player in enumerate(page, start=1))
                embed.add_field(name=f"GN Online: {len(
                    hm_players)} - Trang {index}", value=f'```{paginated_result}```', inline=False)

        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())
    else:
        embed = discord.Embed(title='__**Danh sách Gungnir và GN**__', description='```Không có Gungnir hoặc GN nào Online```',
                              color=discord.Color.blurple())
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
        embed.set_author(
            name="BẠCH HỔ GANGS™",
            icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())

# 6Ma Đạo


@client.command(aliases=['madao'])
async def md(ctx):
    if ctx.channel.id != int(config.channelID):
        await ctx.send("Bạn không thể sử dụng lệnh này trong kênh này.")
        return
    timenow = time.strftime("%H:%M | %d/%m/%Y")
    resp = rq.get('http://' + config.serverIP + '/players.json').json()
    hacma_players = []
    hm_players = []
    for player in resp:
        if ('group' in player and player['group'] == 'Ma Đạo |') or ('name' in player and any(player['name'].lower().startswith(prefix.lower()) for prefix in ['ma đạo |'])):
            hacma_players.append(player)
        elif ('group' in player and player['group'] == 'MĐ |') or ('name' in player and any(player['name'].lower().startswith(prefix.lower()) for prefix in ['mđ |'])):
            hm_players.append(player)

    hacma_players = sorted(hacma_players, key=lambda k: k['name'])
    hm_players = sorted(hm_players, key=lambda k: k['name'])

    if len(hacma_players) > 0 or len(hm_players) > 0:
        embed = discord.Embed(color=discord.Color.blurple())
        embed.set_author(name="BẠCH HỔ GANGS™",
                         icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')

        if len(hacma_players) > 0:
            paginated_hacma_players = [hacma_players[i:i + 25]
                                       for i in range(0, len(hacma_players), 25)]
            for index, page in enumerate(paginated_hacma_players, start=1):
                paginated_result = '\n'.join(f'#{count} [ID:{player["id"]}] {
                                             player["name"]}' for count, player in enumerate(page, start=1))
                embed.add_field(name=f"Ma Đạo Online: {len(
                    hacma_players)} - Trang {index}", value=f'```{paginated_result}```', inline=False)

        if len(hm_players) > 0:
            paginated_hm_players = [hm_players[i:i + 25]
                                    for i in range(0, len(hm_players), 25)]
            for index, page in enumerate(paginated_hm_players, start=1):
                paginated_result = '\n'.join(f'#{count} [ID:{player["id"]}] {
                                             player["name"]}' for count, player in enumerate(page, start=1))
                embed.add_field(name=f"MĐ Online: {len(
                    hm_players)} - Trang {index}", value=f'```{paginated_result}```', inline=False)

        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())
    else:
        embed = discord.Embed(title='__**Danh sách Ma Đạo và MĐ**__', description='```Không có Ma Đạo hoặc MĐ nào Online```',
                              color=discord.Color.blurple())
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
        embed.set_author(
            name="BẠCH HỔ GANGS™",
            icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())


# Thiên Triều
@client.command(aliases=['thientrieu'])
async def tt(ctx):
    if ctx.channel.id != int(config.channelID):
        await ctx.send("Bạn không thể sử dụng lệnh này trong kênh này.")
        return
    timenow = time.strftime("%H:%M | %d/%m/%Y")
    resp = rq.get('http://' + config.serverIP + '/players.json').json()
    ca_players = []

    for player in resp:
        if ('group' in player and player['group'] == 'Thiên Triều |') or ('name' in player and any(player['name'].lower().startswith(prefix.lower()) for prefix in ['Thiên Triều |'])):
            ca_players.append(player)

    # sắp xếp theo tên bảng chữ cái
    ca_players = sorted(ca_players, key=lambda k: k['name'])

    if len(ca_players) > 0:
        embed = discord.Embed(color=discord.Color.blurple())
        embed.set_author(name="BẠCH HỔ GANGS™",
                         icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')

        paginated_players = [ca_players[i:i + 25]
                             for i in range(0, len(ca_players), 25)]

        for index, page in enumerate(paginated_players, start=1):
            paginated_result = '\n'.join(f'#{count} [ID:{player["id"]}] {player["name"]}' for count, player in enumerate(
                page, start=1) if player.get('group') != 'Thiên Triều |')
            embed.add_field(name=f"Thiên Triều Online: {len(
                ca_players)} - Trang {index}", value=f'```{paginated_result}```', inline=False)

        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())
    else:
        embed = discord.Embed(title='__**Danh sách Gang Thiên Triều**__', description='```Không có Thiên Triều nào Online```',
                              color=discord.Color.blurple())
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
        embed.set_author(
            name="BẠCH HỔ GANGS™",
            icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())
# Cột Chèo


@client.command(aliases=['cotcheo'])
async def cc(ctx):
    if ctx.channel.id != int(config.channelID):
        await ctx.send("Bạn không thể sử dụng lệnh này trong kênh này.")
        return
    timenow = time.strftime("%H:%M | %d/%m/%Y")
    resp = rq.get('http://' + config.serverIP + '/players.json').json()
    hacma_players = []
    hm_players = []
    for player in resp:
        if ('group' in player and player['group'] == 'Cột Chèo |') or ('name' in player and any(player['name'].lower().startswith(prefix.lower()) for prefix in ['cột chèo |'])):
            hacma_players.append(player)
        elif ('group' in player and player['group'] == 'CC |') or ('name' in player and any(player['name'].lower().startswith(prefix.lower()) for prefix in ['cc |'])):
            hm_players.append(player)

    hacma_players = sorted(hacma_players, key=lambda k: k['name'])
    hm_players = sorted(hm_players, key=lambda k: k['name'])

    if len(hacma_players) > 0 or len(hm_players) > 0:
        embed = discord.Embed(color=discord.Color.blurple())
        embed.set_author(name="BẠCH HỔ GANGS™",
                         icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')

        if len(hacma_players) > 0:
            paginated_hacma_players = [hacma_players[i:i + 25]
                                       for i in range(0, len(hacma_players), 25)]
            for index, page in enumerate(paginated_hacma_players, start=1):
                paginated_result = '\n'.join(f'#{count} [ID:{player["id"]}] {
                                             player["name"]}' for count, player in enumerate(page, start=1))
                embed.add_field(name=f"Cột Chèo Online: {len(
                    hacma_players)} - Trang {index}", value=f'```{paginated_result}```', inline=False)

        if len(hm_players) > 0:
            paginated_hm_players = [hm_players[i:i + 25]
                                    for i in range(0, len(hm_players), 25)]
            for index, page in enumerate(paginated_hm_players, start=1):
                paginated_result = '\n'.join(f'#{count} [ID:{player["id"]}] {
                                             player["name"]}' for count, player in enumerate(page, start=1))
                embed.add_field(name=f"CC Online: {len(
                    hm_players)} - Trang {index}", value=f'```{paginated_result}```', inline=False)

        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())
    else:
        embed = discord.Embed(title='__**Danh sách Cột Chèo và CC**__', description='```Không có Cột Chèo hoặc CC nào Online```',
                              color=discord.Color.blurple())
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
        embed.set_author(
            name="BẠCH HỔ GANGS™",
            icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())
# Paradise


@client.command(aliases=['paradise'])
async def prd(ctx):
    if ctx.channel.id != int(config.channelID):
        await ctx.send("Bạn không thể sử dụng lệnh này trong kênh này.")
        return
    timenow = time.strftime("%H:%M | %d/%m/%Y")
    resp = rq.get('http://' + config.serverIP + '/players.json').json()
    ca_players = []

    for player in resp:
        if ('group' in player and player['group'] == 'Paradise') or ('name' in player and any(player['name'].lower().startswith(prefix.lower()) for prefix in ['paradise |', 'pr |'])):
            ca_players.append(player)

    # sắp xếp theo tên bảng chữ cái
    ca_players = sorted(ca_players, key=lambda k: k['name'])

    if len(ca_players) > 0:
        embed = discord.Embed(color=discord.Color.blurple())
        embed.set_author(name="BẠCH HỔ GANGS™",
                         icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')

        paginated_players = [ca_players[i:i + 25]
                             for i in range(0, len(ca_players), 25)]

        for index, page in enumerate(paginated_players, start=1):
            paginated_result = '\n'.join(f'#{count} [ID:{player["id"]}] {
                                         player["name"]}' for count, player in enumerate(page, start=1) if player.get('group') != 'Paradise')
            embed.add_field(name=f"Paradise Online: {len(
                ca_players)} - Trang {index}", value=f'```{paginated_result}```', inline=False)

        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())
    else:
        embed = discord.Embed(title='__**Danh sách Paradise**__', description='```Không có Paradise nào Online```',
                              color=discord.Color.blurple())
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
        embed.set_author(
            name="BẠCH HỔ GANGS™",
            icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())
# TiTans


@client.command(aliases=['titans'])
async def ti(ctx):
    if ctx.channel.id != int(config.channelID):
        await ctx.send("Bạn không thể sử dụng lệnh này trong kênh này.")
        return
    timenow = time.strftime("%H:%M | %d/%m/%Y")
    resp = rq.get('http://' + config.serverIP + '/players.json').json()
    ca_players = []

    for player in resp:
        if ('group' in player and player['group'] == 'TiTans |') or ('name' in player and any(player['name'].lower().startswith(prefix.lower()) for prefix in ['titans |'])):
            ca_players.append(player)

    # sắp xếp theo tên bảng chữ cái
    ca_players = sorted(ca_players, key=lambda k: k['name'])

    if len(ca_players) > 0:
        embed = discord.Embed(color=discord.Color.blurple())
        embed.set_author(name="BẠCH HỔ GANGS™",
                         icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')

        paginated_players = [ca_players[i:i + 25]
                             for i in range(0, len(ca_players), 25)]

        for index, page in enumerate(paginated_players, start=1):
            paginated_result = '\n'.join(f'#{count} [ID:{player["id"]}] {
                                         player["name"]}' for count, player in enumerate(page, start=1) if player.get('group') != 'titans')
            embed.add_field(name=f"TiTans Online: {len(
                ca_players)} - Trang {index}", value=f'```{paginated_result}```', inline=False)

        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())
    else:
        embed = discord.Embed(title='__**Danh sách Gang TiTans**__', description='```Không có TiTans nào Online```',
                              color=discord.Color.blurple())
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
        embed.set_author(
            name="BẠCH HỔ GANGS™",
            icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())
# Thiên Hoàng


@client.command(aliases=['thienhoang'])
async def th(ctx):
    if ctx.channel.id != int(config.channelID):
        await ctx.send("Bạn không thể sử dụng lệnh này trong kênh này.")
        return
    timenow = time.strftime("%H:%M | %d/%m/%Y")
    resp = rq.get('http://' + config.serverIP + '/players.json').json()
    ca_players = []

    for player in resp:
        if ('group' in player and player['group'] == 'Thiên Hoàng |') or ('name' in player and any(player['name'].lower().startswith(prefix.lower()) for prefix in ['thiên hoàng |'])):
            ca_players.append(player)

    # sắp xếp theo tên bảng chữ cái
    ca_players = sorted(ca_players, key=lambda k: k['name'])

    if len(ca_players) > 0:
        embed = discord.Embed(color=discord.Color.blurple())
        embed.set_author(name="BẠCH HỔ GANGS™",
                         icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')

        paginated_players = [ca_players[i:i + 25]
                             for i in range(0, len(ca_players), 25)]

        for index, page in enumerate(paginated_players, start=1):
            paginated_result = '\n'.join(f'#{count} [ID:{player["id"]}] {
                                         player["name"]}' for count, player in enumerate(page, start=1) if player.get('group') != 'thiên hoàng')
            embed.add_field(name=f"Thiên Hoàng Online: {len(
                ca_players)} - Trang {index}", value=f'```{paginated_result}```', inline=False)

        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())
    else:
        embed = discord.Embed(title='__**Danh sách Thiên Hoàng**__', description='```Không có Thiên Hoàng nào Online```',
                              color=discord.Color.blurple())
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
        embed.set_author(
            name="BẠCH HỔ GANGS™",
            icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())
# Konoha


@client.command(aliases=['konoha'])
async def kn(ctx):
    if ctx.channel.id != int(config.channelID):
        await ctx.send("Bạn không thể sử dụng lệnh này trong kênh này.")
        return
    timenow = time.strftime("%H:%M | %d/%m/%Y")
    resp = rq.get('http://' + config.serverIP + '/players.json').json()
    ca_players = []

    for player in resp:
        if ('group' in player and player['group'] == 'Konoha |') or ('name' in player and any(player['name'].lower().startswith(prefix.lower()) for prefix in ['konoha |'])):
            ca_players.append(player)

    # sắp xếp theo tên bảng chữ cái
    ca_players = sorted(ca_players, key=lambda k: k['name'])

    if len(ca_players) > 0:
        embed = discord.Embed(color=discord.Color.blurple())
        embed.set_author(name="BẠCH HỔ GANGS™",
                         icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')

        paginated_players = [ca_players[i:i + 25]
                             for i in range(0, len(ca_players), 25)]

        for index, page in enumerate(paginated_players, start=1):
            paginated_result = '\n'.join(f'#{count} [ID:{player["id"]}] {
                                         player["name"]}' for count, player in enumerate(page, start=1) if player.get('group') != 'Konoha')
            embed.add_field(name=f"Konoha Online: {len(
                ca_players)} - Trang {index}", value=f'```{paginated_result}```', inline=False)

        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())
    else:
        embed = discord.Embed(title='__**Danh sách Konoha**__', description='```Không có Konoha nào Online```',
                              color=discord.Color.blurple())
        embed.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/1012621076766937138/1071300811289800774/Logo.png')
        embed.set_author(
            name="BẠCH HỔ GANGS™",
            icon_url="https://media.discordapp.net/attachments/1047470436839079998/1066417043684991006/LOGO_PNG.png?width=441&height=441")
        embed.set_footer(text=f'AnF | copyright © 𝐷𝑎𝑡𝐾𝑎𝑎 𝐻𝑎𝑛𝑧𝑜 | {timenow}')
        await ctx.send(embed=embed, view=DefaultView())
# Live Status


@tasks.loop(seconds=15)
async def live_status():
    global last_boot_time

    Dis = client.get_guild(config.guildID)

    police_count = 0
    medic_count = 0
    rescue_count = 0
    pcount = 0

    try:
        resp = rq.get(f'http://{config.serverIP}/players.json').json()
        pcount = len(resp)  # Cập nhật số lượng người chơi
        for player in resp:
            name = player.get('name', '')
            if '|' in name:
                role = name.split('|')[0].strip()
                if role in ['CA', 'SWAT', 'S.W.A.T', 'QLCA', 'PGĐCA', 'GĐCA', 'PGDCA', 'GDCA']:
                    police_count += 1
                if role in ['MED', 'Quân Y', 'QLMED', 'GĐBS', 'PGĐBS', 'GDBS', 'PGDBS']:
                    medic_count += 1
                if role in ['QLCH', 'CH', 'GSCH', 'PGĐCH', 'GĐCH', 'PGDCH', 'GDCH']:
                    rescue_count += 1
    except Exception as e:
        print(f"Error fetching player data: {e}")

    # Hiển thị số lượng từng ngành trong trạng thái của bot
    activity = discord.Activity(
        type=discord.ActivityType.playing,
        name=f'Server AnF: {
            pcount}/350 | 👮‍♀️: {police_count} 👨‍⚕️: {medic_count} 🔧: {rescue_count}'
    )
    await client.change_presence(activity=activity)

    await asyncio.sleep(15)

    if pcount > 0:
        ()
keep_alive.keep_alive()
client.run(config.TOKEN)
