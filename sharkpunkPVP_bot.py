import discord
import json
import requests

client = discord.Client()

class Sharks:
    def __init__(self, name, types, moves, EVs, health = 20):
        # save variables as attributes
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health

#Define Characters
Shark1 = Sharks('Shark1', 'Daddy Shark', ['Bite', 'Body Slam'], {'ATTACK':12, 'DEFENSE': 8})
Shark2 = Sharks('Shark2', 'Baby Shark', ['Bite', 'Body Slam'],{'ATTACK': 10, 'DEFENSE':10})
Shark3 = Sharks('Shark3', 'Alpha Shark', ['Bite', 'Body Slam'],{'ATTACK':8, 'DEFENSE':12})

Player1 = Shark1
Player2 = Shark2

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$fight'):
        # Print fight information
        channel = message.channel
        try:
            await channel.send("-----SHARKPUNK BATTLE-----\n"+
            Player1.name+"\nTYPE: "+Player1.types+"\n ATTACK: "+str(Player1.attack)+"\n DEFENSE: "+str(Player1.defense)+"\n"+
            Player2.name+"\nTYPE: "+Player2.types+"\n ATTACK: "+str(Player2.attack)+"\n DEFENSE: "+str(Player2.defense))
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
            Turn = 1
                # Continue while Shark still have health

            while (Player1.health > 0) and (Player2.health > 0):
                # Print the health of each pokemon
                client.loop.create_task(channel.send(Player1.name+" Health :"+str(Player1.health)))
                client.loop.create_task(channel.send(Player2.name+" Health :"+str(Player2.health)))
                client.loop.create_task(channel.send("It's "+Player1.name+"'s turn!"))
                client.loop.create_task(channel.send("Your moves are: \n1: Bite \n2: Body Slam\n\nType '1' or '2' to choose!"))
                ChosenMove = client.wait_for('message', check=check_move)
                # Determine damage
                Player2.health -= Player1.attack
                client.loop.create_task(channel.send("You've hit "+Player2.name+" for "+str(Player1.attack)))

                # Check to see if Pokemon fainted
                if Player2.health <= 0:
                    client.loop.create_task(channel.send(Player2.name+" is dead!"))
                    break

                # Player2s turn

                client.loop.create_task(channel.send("It's "+Player2.name+"'s turn!"))
                #code should randomize Player2's move
                client.loop.create_task(channel.send(Player2.name+" uses 'dummy move'"))

                # Determine damage
                Player1.health -= Player2.attack

                # Check to see if Pokemon fainted
                if Player1.health <= 0:
                    client.loop.create_task(channel.send(Player2.name+" is dead!"))
                    break

                client.loop.create_task(channel.send("End of Turn "+ str(Turn)))

                Turn = Turn + 1

        fight(Player1, Player2)

#replace '' with bot token
client.run('')
