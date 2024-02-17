import discord
from discord.ext import commands
from bot_mantik import gen_pass
from discord import FFmpegPCMAudio
import os
import time

current_time = time.strftime("%H:%M")
current_date = time.strftime("%d.%m.%Y")

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='/', intents=intents)




@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık.')
  


@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
       
    if message.content.startswith('merhaba'):
        await message.channel.send("Selam!")
    
    elif message.content.startswith('bye'):
        await message.channel.send("Görüşürüz")

    elif "bb" in message.content.lower().split():
        await message.channel.send("Görüşürüz")

    elif "naber" in message.content.lower().split():
        await message.channel.send("İyi, sen?")

    elif "nasilsin" in message.content.lower():
        await message.channel.send("İyi, sen?")

    elif "nasılsın" in message.content.lower():
        await message.channel.send("İyi, sen?")

    elif "adın ne" in message.content.lower():
        await message.channel.send("Benim adım YEK_1_BOT")

    elif "adın ne?" in message.content.lower():
        await message.channel.send("Benim adım YEK_1_BOT")

    elif message.content.startswith('/pass'):
        await message.channel.send(gen_pass(8))

    elif "/saat" in message.content.lower().split():
        await message.channel.send(current_time)

    elif "/tarih" in message.content.lower().split():
        await message.channel.send(current_date)

    elif "al nassr" in message.content.lower():
        await message.channel.send("Eğveeğt doğru ceğvap")


    argo_kelimeler = ["velet", "bok", "enayi", "şerefsiz", "mal", "salak", "gerizekalı","lan",]

    if any(word in message.content.lower().split() for word in argo_kelimeler):
        await message.channel.send("Lütfen düzgün konuşalım. Kötü kelimeler kullanmaktan kaçınalım.")
        return
    
    elif message.content.startswith('/math'):
        await message.channel.send("Hangi işlemi yapmak istiyorsunuz? (çıkarma, çarpma, bölme, toplama)")

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        msg = await client.wait_for("message", check=check)
        islem = msg.content.lower()

        if islem not in ["çıkarma", "çarpma", "bölme", "toplama"]:
            await message.channel.send("Geçersiz işlem seçimi.")
            return

        await message.channel.send("İlk sayıyı girin:")
        msg = await client.wait_for("message", check=check)
        sayi1 = int(msg.content)

        await message.channel.send("İkinci sayıyı girin:")
        msg = await client.wait_for("message", check=check)
        sayi2 = int(msg.content)

        if islem == "çıkarma":
            await message.channel.send(f"Sonuç: {sayi1 - sayi2}")
        elif islem == "çarpma":
            await message.channel.send(f"Sonuç: {sayi1 * sayi2}")
        elif islem == "bölme":
            await message.channel.send(f"Sonuç: {sayi1 / sayi2}")
        elif islem == "toplama":
            await message.channel.send(f"Sonuç: {sayi1 + sayi2}")

    elif "/oyun" in message.content:
        await message.channel.send("Kaç tur Taş, Kağıt, Makas oynamak istiyorsunuz? Lütfen bir sayı girin.")

        def check_rounds(msg):
            return msg.author == message.author and msg.channel == message.channel and msg.content.isdigit()

        msg = await client.wait_for("message", check=check_rounds)
        rounds = int(msg.content)

        for round_num in range(1, rounds + 1):
            await message.channel.send(f"TUR {round_num}")
            await message.channel.send("Taş, kağıt, makas oynamaya hazır mısın? Lütfen seçiminizi yapın: taş, kağıt, ya da makas.")

            def check_choice(msg):
                return msg.author == message.author and msg.channel == message.channel and msg.content.lower() in ["taş", "kağıt", "makas"]

            msg = await client.wait_for("message", check=check_choice)
            user_choice = msg.content.lower()

            import random
            choices = ["taş", "kağıt", "makas"]
            bot_choice = random.choice(choices)

            await message.channel.send(f"Ben {bot_choice} seçtim.")

            if user_choice == bot_choice:
                await message.channel.send("Berabere!")
            elif (user_choice == "taş" and bot_choice == "makas") or (user_choice == "kağıt" and bot_choice == "taş") or (user_choice == "makas" and bot_choice == "kağıt"):
                await message.channel.send("Tebrikler, kazandın!")
            else:
                await message.channel.send("Üzgünüm, kaybettin!")

    elif message.content.startswith('/futbolquiz'):
        await message.channel.send("Futbol quizine hoş geldiniz! İşte ilk soru:")
        await message.channel.send("Hangi futbolcu 5 kez Ballon d'Or kazanmıştır?")

        def check_answer(msg):
            return msg.author == message.author and msg.channel == message.channel

        correct_answer = "Cristiano Ronaldo" # Doğru cevap
        correct_answer2 = "Ronaldo"
        msg = await client.wait_for("message", check=check_answer)
        user_answer = msg.content

        if user_answer.lower().split == correct_answer.lower() or user_answer.lower() == correct_answer2.lower():
            await message.channel.send("Tebrikler, doğru cevap!")
        else:
            await message.channel.send("Üzgünüm, yanlış cevap. Doğru cevap Cristiano Ronaldo'dur.")

        await message.channel.send("Futbol quizine hoş geldiniz! İşte ikinci soru:")
        await message.channel.send("Hangi futbolcu 2022 yılında Ballon d'Or kazanmıştır?")

        def check_answer(msg):
            return msg.author == message.author and msg.channel == message.channel

        correct_answer = "Benzema"  # Doğru cevap
        correct_answer = "Karim Benzema"  
        msg = await client.wait_for("message", check=check_answer)
        user_answer = msg.content

        if user_answer.lower().split == correct_answer.lower() or user_answer.lower() == correct_answer2.lower():
            await message.channel.send("Tebrikler, doğru cevap!")
        else:
            await message.channel.send("Üzgünüm, yanlış cevap. Doğru cevap Karim Benzama'dır.")
    
    
        await message.channel.send("Futbol quizine hoş geldiniz! İşte üçüncü soru:")
        await message.channel.send("Cristiano Ronaldo, UEFA Şampiyonlar Ligi tarihinde en çok gol atan futbolcudur. Toplam kaç gol atmıştır?")

        def check_answer(msg):
            return msg.author == message.author and msg.channel == message.channel

        correct_answer = "140"  # Doğru cevap
        msg = await client.wait_for("message", check=check_answer)
        user_answer = msg.content

        if user_answer == correct_answer:
            await message.channel.send("Tebrikler, doğru cevap!")

            # Eğer doğru cevap verildiyse, yeni bir soru sor
            await message.channel.send("İşte bir sonraki soru:")
            await message.channel.send("Cristiano Ronaldo, hangi takımla UEFA Şampiyonlar Ligi'ni en fazla kazanmıştır?")

            # Yeni sorunun doğru cevabını belirle
            new_correct_answer = "Real Madrid"  # Yeni doğru cevap
            msg = await client.wait_for("message", check=check_answer)
            new_user_answer = msg.content

            if new_user_answer.lower() == new_correct_answer.lower():
                await message.channel.send("Tebrikler, doğru cevap!")
            else:
                await message.channel.send("Üzgünüm, yanlış cevap. Doğru cevap Real Madrid'dir.")
        else:
            await message.channel.send("Üzgünüm, yanlış cevap. Doğru cevap 140'tır.")





    elif "sa" in message.content.lower().split():
        await message.channel.send("as")

    await client.process_commands(message)

@client.command()
async def mem(ctx):
    with open('M2L1\RESİMLER\mem1.png','rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

client.run("MTIwMzI3NzYwMjYwMTcwNTUzMw.GrCs2A.KkPBroWxXFMCFEAKETAUbyC5ucKIbeeuIoFkDo")
