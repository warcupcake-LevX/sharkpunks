import discord
import json
import requests

client = discord.Client()

class BD_Character:
    def __init__(self, name, types, moves, EVs, health='==================='):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 # Amount of health bars

#Define Characters
Bitmint = BD_Character('Bitmint', 'Fulltime', ['Lead Scrum', 'Weekly Catch Up', 'Phase I Assessment', 'Onboarding'], {'ATTACK':12, 'DEFENSE': 8})
Bitfern = BD_Character('Bitfern', 'Intern', ['Write Minutes', 'Remind Green of Meetings', 'Monday.com', 'Write SOP'],{'ATTACK': 10, 'DEFENSE':10})
PRuam = BD_Character('P-Ruam', 'Management', ['Meeting', 'Pray Emoji', 'Push Product', 'Order Tequila'],{'ATTACK':8, 'DEFENSE':12})

Possible_Names = ['Bitmint','Bitfern','P-Ruam']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$pickcharacter'):
        channel = message.channel
        await channel.send('Choose your BD member! \n1. Bitmint\n2. Bitfern\n3. P-Ruam')

        def check_char(m):
            if m.content in Possible_Names :
                return m.content

        def assign_character(m):
            if m.content == 'Bitmint':
                return Bitmint
            if m.content == 'Bitfern':
                return Bitfern
            if m.content == 'P-Ruam':
                return PRuam

        def check_fight(m):
            if m.content == 'fight' :
                return m.content


        ChosenCharacter = await client.wait_for('message', check=check_char)
        global Player1
        Player1 = assign_character(ChosenCharacter)
        await channel.send("You've chosen "+ ChosenCharacter.content)

        await channel.send("Chose your opponent! \n1. Bitmint\n2. Bitfern\n3. P-Ruam")
        ChosenCharacter = await client.wait_for('message', check=check_char)

        global Player2
        Player2 = assign_character(ChosenCharacter)
        await channel.send("It's "+Player1.name+" VS "+ Player2.name)

    if message.content.startswith('$fight'):
        # Print fight information
        channel = message.channel
        try:
            await channel.send("-----BD BATTLE-----\n"+
            Player1.name+"TYPE: "+Player1.types+"\n ATTACK: "+str(Player1.attack)+"\n DEFENSE: "+str(Player1.defense)+"\n"+
            Player2.name+"TYPE: "+Player2.types+"\n ATTACK: "+str(Player2.attack)+"\n DEFENSE: "+str(Player2.defense))
        except:
            await channel.send("Please pick your characters first.")

        def fight(self, BD_Character2):
        # Allow two pokemon to fight each other
            # Consider type advantages
            version = ['Full Time', 'Management', 'Intern']
            for i,k in enumerate(version):
                if self.types == k:
                    # Both are same type
                    if Player2.types == k:
                        string_1_attack = '\nIts not very effective...'
                        string_2_attack = '\nIts not very effective...'

                    # Player2 is STRONG
                    if Player2.types == version[(i+1)%3]:
                        Player2.attack *= 2
                        Player2.defense *= 2
                        self.attack /= 2
                        self.defense /= 2
                        string_1_attack = '\nIts not very effective...'
                        string_2_attack = '\nIts super effective!'

                    # Player2 is WEAK
                    if Player2.types == version[(i+2)%3]:
                        self.attack *= 2
                        self.defense *= 2
                        Player2.attack /= 2
                        Player2.defense /= 2
                        string_1_attack = '\nIts super effective!'
                        string_2_attack = '\nIts not very effective...'

                # Now for the actual fighting...
                # Continue while pokemon still have health
            while (Player1.bars > 0) and (Player2.bars > 0):
                # Print the health of each pokemon
                client.loop.create_task(channel.send(Player1.name+" Health :"+Player1.health))
                client.loop.create_task(channel.send(Player2.name+" Health :"+Player2.health))
                client.loop.create_task(channel.send("Go "+Player1.name+"!"))
                for i, x in enumerate(Player1.moves):
                    print(f"{i+1}.", x)
                index = int(input('Pick a move: '))
                delay_print(f"\n{Player1.name} used {Player1.moves[index-1]}!")
                time.sleep(1)
                delay_print(string_1_attack)

                # Determine damage
                Player2.bars -= Player1.attack
                Player2.health = ""

                # Add back bars plus defense boost
                for j in range(int(Player2.bars+.1*Player2.defense)):
                    Player2.health += "="

                time.sleep(1)
                print(f"\n{self.name}\t\tHLTH\t{self.health}")
                print(f"{BD_Character2.name}\t\tHLTH\t{BD_Character2.health}\n")
                time.sleep(.5)

                # Check to see if Pokemon fainted
                if BD_Character2.bars <= 0:
                    delay_print("\n..." + BD_Character2.name + ' fainted.')
                    break

                # BD_Character2s turn

                print(f"Go {BD_Character2.name}!")
                for i, x in enumerate(BD_Character2.moves):
                    print(f"{i+1}.", x)
                index = int(input('Pick a move: '))
                delay_print(f"\n{BD_Character2.name} used {BD_Character2.moves[index-1]}!")
                time.sleep(1)
                delay_print(string_2_attack)

                # Determine damage
                self.bars -= BD_Character2.attack
                self.health = ""

                # Add back bars plus defense boost
                for j in range(int(self.bars+.1*self.defense)):
                    self.health += "="

                time.sleep(1)
                print(f"{self.name}\t\tHLTH\t{self.health}")
                print(f"{BD_Character2.name}\t\tHLTH\t{BD_Character2.health}\n")
                time.sleep(.5)

                # Check to see if Pokemon fainted
                if self.bars <= 0:
                    delay_print("\n..." + self.name + ' fainted.')
                    break

client.run('OTE3MDAwNTMzNjU3NjY1NTY2.YayVTA.ihcOGPD7Z61-96jUl9qYAnNVqN0')
