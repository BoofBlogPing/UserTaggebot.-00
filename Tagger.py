import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []

tekli_calisan = []



@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("Salam Mən DejavuTagBot Group'da User Tag Edmək üçün Yaradıldım...\n\nƏtrafli Məlumat Almaq üçün /help Əmrinə Toxunaraq Məlumat Əldə Edə Bilərsən.",
                    buttons=(
                   
		      [Button.url('➕ Məni Qrupa Sal ➕', 'http://t.me/DejavuTaggerBot?startgroup=a')],
                      [Button.url('Sahib 👨🏻‍💻', 'https://t.me/MUCVE_M')],
                      [Button.url('Qurup 📣', 'https://t.me/DejavuGurup')],
		      [Button.url('Kanal 🛠', 'https://t.me/DejavuSupport')],
                    ),
                    link_preview=False
                   )
###@client.on(events.NewMessage(pattern="^/help$"))
*/async def help(event):
  helptext = "** DejavuTagBot'un Kömək Menyusu.**\n\nƏmrlər:\n/add <Mesajınız> = Beş'li Tag Eləmə Əmri. \n/tektag <Mesajınız> = Tək-Tək Tag Eləmə Əmri. \n/etag <Mesajınız> = Emojilərlə Tag Eləmə Əmri.\n/admins <Mesajınız> = Adminləri Tag Eləmə Əmri."
  await event.reply(helptext,
                    buttons=(
                      [Button.url('➕ Məni Qrupa Sal ➕', 'http://t.me/DejavuTaggerBot?startgroup=a')],
                      [Button.url('Sahib 👨🏻‍💻', 'https://t.me/MUCVE_M')],
                      [Button.url('Qurup 📣', 'https://t.me/DejavuGurup')],
		      [Button.url('Kanal 🛠', 'https://t.me/DejavuSupport')],
                    ),
                    link_preview=False
                   )
	*/
###@client.on(events.NewMessage(pattern="^/reklam$"))
async def help(event):
  helptext = "**Çox Funksiyalı Tag Botunu Tapmağa Çalışan Qrup Sahibləri üçün @DejavuTaggerBot Sizin üçündür:\n\n📌 Beş'li Tag Eləmə Əmri.\n📌 Tək-Tək Tag Eləmə Əmri.\n📌 Emojilərlə Tag Eləmə Əmri.\n📌 Adminləri Tag Eləmə Əmri.\n📌\n\n Belə bir çox Funksiyalı @DejavuTaggerBot-u Admin Olaraq Qrupunuza Əlavə edə və Asanlıqla Qoşula, Userleri Tag Edə Bilərsiniz. **" 
   await event.reply(helptext,  
                    buttons=(
                  [Button.url('➕ Məni Qrupa Sal ➕', 'http://t.me/DejavuTaggerBot?startgroup=a')],
                    ),
                    link_preview=False
                   )
	
	

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")


@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu Əmr Qruplar üçün Etibarlıdır!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu Əmri Yalnız Adminlər İstifadə Edə Bilər!**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Köhnə Mesajlar üçün Userləri Tag edə Bilmərəm.**")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Tag Eləmək üçün Səbəb Yoxdur! ")
  else:
    return await event.respond("**Tag'a Başlamaq üçün Səbəb Yazın...**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**Tag Uğurlu Şəkildə Dayandırıldı** ")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Tag Uğurlu Şəkildə Dayandırıldı** ")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/all ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu Əmr Qruplar üçün Etibarlıdır! **")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu Əmri Yalnız Adminlər İstifadə Edə Bilər. **")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Köhnə Mesajlar üçün Userləri TagEedə Bilmərəm. ")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Tag'a Bbaşlamaq üçün Səbəb Yoxdur! ")
  else:
    return await event.respond("**Tag'a Başlamaq üçün Səbəb Yazın...**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"👤 [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**Tag Uğurlu Şəkildə Dayandırıldı. ** ")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"👤 [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**Tag Uğurlu Şəkildə Dayandırıldı. ** ")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**Bu Əmr Qruplar üçün Etibarlıdır! **")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu Əmri Yalnız Adminlər İstifadə Edə Bilər. **")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**Köhnə Mesajlar üçün Userləri Tag Edə Bilmərəm. **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Tagı başlamaq üçün səbəb yoxdur! ")
  else:
    return await event.respond("**Taga Başlamaq üçün Səbəb Yazın...**")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**👤 [{usr.first_name}](tg://user?id={usr.id}) \n**"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Tag Uuğurlu Şəkildə Dayandırıldı.** ")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"👤 [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("**Tag Uğurlu Şəkildə Dayandırıldı. ** ")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	


@client.on(events.NewMessage(pattern="^/tagadmin ?(.*)"))
async def mentionall(tagadmin):

        if tagadmin.pattern_match.group(1):
               seasons = tagadmin.pattern_match.group(1)
        else:
               seasons = ""

        chat = await tagadmin.get_input_chat()
        a_=0
        await tagadmin.delete()
        async for i in client.iter_participants(chat, filter=cp):
                if a_ == 500:
                        break
                a_+=5
                await tagadmin.client.send_message(tagadmin.chat_id, "{} {}".format(i.first_name, i.id, seasons))
                sleep(0.5)


print(">> Bot İşləyir Narahat olma 🚀 Məlumat Almaq üçün @MUCVE_M yazın. <<")
client.run_until_disconnected()
