import discord
import datetime
import time


TOKEN = 'OTU4NDIwMTg1Mzk0NTk3OTM4.YkNEWg.GjJ7DL2l6gmOEWMj--XBMtvDGOc'  # Token from discord developement portal

client = discord.Client()
STARTCOMMAND = '!SAT'
TESTCOMMAND = '!DEMO'

@client.event
async def on_ready():  # bot start function,on ready function
    print("SAT Bot is online as {0.user} ".format(client))  # takes username from discord client object and prints username & confirms bot is online

run = True
inTest = False
endtimes = [65,35,25,55] #Reading, Writing, Math1, Math2
breaktimes = [10, 0 , 5, 0]
counter  = {
    0: "Reading",
    1: "Writing",
    2: "Math No Calucalator",
    3: "Math with Calculator"
}


@client.event
async def on_message(message):
    #Global Variable
    global inTest
    global run
    channel = message.channel
    msg = message.content

    if msg.startswith(STARTCOMMAND):
        await test(channel, 60)
    if msg.startswith(TESTCOMMAND):
        await test(channel, 0.1)
    if msg.startswith("!STOP"):
        run = False


async def test(channel, tmulti):
    global inTest
    global run

    if inTest == False:
        await channel.send("Starting test!")
        inTest = True
        for i in range(3):
            await channel.send(3 - i)
            time.sleep(1)
        await channel.send("Test has begun!")
        for i in range(len(counter)):
            if run == True:
                await channel.send(f"Current section is {counter[i]}, you have {endtimes[i]} minutes left.")
                time.sleep(endtimes[i] * tmulti)
                if breaktimes[i] > 0:
                    await channel.send(f" {counter[i]} section is over. You have a break for {breaktimes[i]} minutes.")
                    time.sleep(breaktimes[i] * tmulti)
                    await channel.send(f"Break is over.")
                await channel.send(f"{counter[i]} has been completed. Next section starts in 5 seconds")
                for i in range(5):
                    await channel.send(5 - i)
                    time.sleep(1)
            else:
                await channel.send("Test has stopped.")
                break
            await channel.send("Test is over! Congrats on sitting through it!")
            inTest = False

    if inTest == True:
        await channel.send("You are already in a test.")


client.run(TOKEN) # Runs bot