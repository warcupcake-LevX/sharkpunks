import discord
import json
import requests

client = discord.Client()

class Sharks:
    def __init__(self, name, types, moves, EVs, health):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = 20

#Define Characters
Bitmint = Sharks('Bitmint', 'Fulltime', ['Lead Scrum', 'Weekly Catch Up', 'Phase I Assessment', 'Onboarding'], {'ATTACK':12, 'DEFENSE': 8})
Bitfern = Sharks('Bitfern', 'Intern', ['Write Minutes', 'Remind Green of Meetings', 'Monday.com', 'Write SOP'],{'ATTACK': 10, 'DEFENSE':10})
PRuam = Sharks('P-Ruam', 'Management', ['Meeting', 'Pray Emoji', 'Push Product', 'Order Tequila'],{'ATTACK':8, 'DEFENSE':12})

Possible_Names = ['Bitmint','Bitfern','P-Ruam']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #Character Selection
    if message.content.startswith('$pickcharacter'):
        channel = message.channel
        await channel.send('Choose your BD member! \n1. Bitmint\n2. Bitfern\n3. P-Ruam')

        #checking correct character name entry
        def check_char(m):
            if m.content in Possible_Names :
                return m.content

        #assigning character Class to return
        def assign_character(m):
            if m.content == 'Bitmint':
                return Bitmint
            if m.content == 'Bitfern':
                return Bitfern
            if m.content == 'P-Ruam':
                return PRuam



        ChosenCharacter = await client.wait_for('message', check=check_char)
        global Player1
        Player1 = assign_character(ChosenCharacter)
        await channel.send("You've chosen "+ ChosenCharacter.content)

        await channel.send("Chose your opponent! \n1. Bitmint\n2. Bitfern\n3. P-Ruam")
        ChosenCharacter = await client.wait_for('message', check=check_char)

        global Player2
        Player2 = assign_character(ChosenCharacter)
        await channel.send("It's "+Player1.name+" VS "+ Player2.name)

    #start the fight
    if message.content.startswith('$fight'):
        # Print fight information
        channel = message.channel
        try:
            await channel.send("-----SHARKPUNK BATTLE-----\n"+
            Player1.name+"TYPE: "+Player1.types+"\n ATTACK: "+str(Player1.attack)+"\n DEFENSE: "+str(Player1.defense)+"\n"+
            Player2.name+"TYPE: "+Player2.types+"\n ATTACK: "+str(Player2.attack)+"\n DEFENSE: "+str(Player2.defense))
        except:
            await channel.send("Please pick your characters first.")

        #check move input
        def check_move(m):
            if m.content == '1':
                return "Bite"
            if m.content == '2':
                return "Body Slam"

        def fight(Player1, Player2):
        # Allow sharks
                # Continue while Shark still have health
            while (Player1.health > 0) and (Player2.health > 0):
                # Print the health of each pokemon
                client.loop.create_task(channel.send(Player1.name+" Health :"+Player1.health))
                client.loop.create_task(channel.send(Player2.name+" Health :"+Player2.health))
                client.loop.create_task(channel.send("Go "+Player1.name+"!"))
                client.loop.create_task(channel.send("Your moves are: /n1: Bite/n2: Body Slam")

                # Determine damage
                Player2.health =  Player2.health - Player1.attack

                time.sleep(1)
                print(f"\n{self.name}\t\tHLTH\t{self.health}")
                print(f"{Sharks2.name}\t\tHLTH\t{Sharks2.health}\n")
                time.sleep(.5)

                # Check to see if Pokemon fainted
                if Sharks2.bars <= 0:
                    delay_print("\n..." + Sharks2.name + ' fainted.')
                    break

                # Sharks2s turn

                print(f"Go {Sharks2.name}!")
                for i, x in enumerate(Sharks2.moves):
                    print(f"{i+1}.", x)
                index = int(input('Pick a move: '))
                delay_print(f"\n{Sharks2.name} used {Sharks2.moves[index-1]}!")
                time.sleep(1)
                delay_print(string_2_attack)

                # Determine damage
                self.bars -= Sharks2.attack
                self.health = ""

                # Add back bars plus defense boost
                for j in range(int(self.bars+.1*self.defense)):
                    self.health += "="

                time.sleep(1)
                print(f"{self.name}\t\tHLTH\t{self.health}")
                print(f"{Sharks2.name}\t\tHLTH\t{Sharks2.health}\n")
                time.sleep(.5)

                # Check to see if Pokemon fainted
                if self.bars <= 0:
                    delay_print("\n..." + self.name + ' fainted.')
                    break
#replace 'OTE3MDcyOTc3NjU1Mzk0MzE0.YazYxA.UhrT-U9gRDuq-hW6B5CkeJjmk-I' with bot token
client.run('OTE3MDcyOTc3NjU1Mzk0MzE0.YazYxA.UhrT-U9gRDuq-hW6B5CkeJjmk-I')
