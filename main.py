import random

Race_list = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Half-Orc", "Halfling", "Human", "Tiefling"]

Background_list = ["Acolyte", "Anthropologist", "Archaeologist", "Athlete", "Charlatan", "City Watch", "Clan Crafter", "Cloistered Scholar", "Courtier", "Criminal", "Entertainer", "Faceless", "Faction Agent", "Far Traveler", "Fisher", "Folk Hero", "Gladiator", "Guild Artisan", "Guild Merchant", "Haunted One", "Hermit","House Agent", "Inheritor", "Investigator", "Knight", "Knight of the Order", "Marine", "Mercenary Veteran", "Noble", "Outlander", "Pirate", "Sage", "Sailor", "Shipwright", "Smuggler", "Soldier", "Spy", "Urban Bounty Hunter", "Urchin", "Uthgardt Tribe Member", "Waterdhavian Noble"]

Class_list = {
  "The Artificer": ["Alchemist", "Armorer", "Artillerist", "Battle Smith"],
  "The Barbarian": ["Path of the Ancestral Guardian", "Path of the Battlerager", "Path of the Beast", "Path of the Berserker", "Path of the Storm Herald", "Path of the Totem Warrior", "Path of the Wild Magic", "Path of the Zealot"],
  "The Bard": ["College of Creation","College of Eloquence", "College of Glamour", "College of Lore", "College of Spirits", "College of Swords", "College of Valor", "College of Whispers"],
  "The Cleric": ["Arcana Domain", "Death Domain", "Forge Domain", "Grave Domain", "Knowledge Domain", "Life Domain", "LIght Domain", "Nature Domain", "Order Domain", "Peace Domain", "Tempest Domain", "Trickery Domain", "Twilight Domain", "War Domain"],
  "The Druid": ["Circle of Dreams", "Circle of the Land", "Circle of the Moon", "Circle of the Shepherd", "Circle of the Spores", "Circle of the Stars", "Circle of Wildfire" ],
  "The Fighter": ["Arcane Archer", "Banneret", "Battle Master", "Cavalier", "Champion", "Echo Knight", "Eldright Knight", "Psi Warrior", "Rune Knight", "Samurai"],
  "The Monk": ["Way of Mercy", "Way of the Astral Self", "Way of the Drunken Master", "Way of the Four Elements", "Way of the Kensei", "Way of the Long Death", "Way of the Open Hand", "Way of Shadow", "Way of the Sun Soul"],
  "The Paladin": ["Oath of the Ancients", "Oath of Conquest", "Oath of the Crown", "Oath of Devotion", "Oath of Glory", "Oath of Redemption", "Oath of Vengeance", "Oath of the Watchers", "Oathbreaker"],
  "The Ranger": ["Beast Master Conclave", "Fey Wanderer", "Gloom Stalker Conclave", "Horizon Walker Conclave", "Hunter Conclave", "Monster Slayer Conclave", "Swarmkeeper"],
  "The Rogue": ["Arcane Trickster", "Assassin", "Inquisitive", "Mastermind", "Phantom", "Scout", "Soulknife", "Swashbuckler", "Thief"],
  "The Sorcerer": ["Aberrant Mind", "Clockwork Soul", "Draconic Bloodline","Divine Soul", "Shadow Magic", "Storm Sorcery", "Wild Magic"],
  "The Wizard": ["School of Abjuration", "School of Bladesinging", "School of Chronurgy", "School of Conjuration", "School of Divination", "School of Enchantment", "School of Evocation", "School of Graviturgy", "School of Illusion", "School of Necromancy", "School of Scribes", "School of Transmutation", "School of War Magic"],
}



print(f"""You can use this machine to randomly draw your character's race, 
background,class and corresponding subclass, or just one or two of these. The 
machine first asks you to type in your choice of race, background or class, which 
you can do if you so wish. However, if you wish for the machine to draw these for 
you just press 'enter' on each input prompt. All values left empty will be drawn by 
the machine. If you want to choose a class but want the machine to draw a subclass 
for you, please be precise with your input. It needs to be, for example, 'The Druid' 
whereas 'the druid' or just 'druid' will give you an error.""")

while True: 
	Race = input("Race: ")
	BG = input("Background: ")
	Class = input("Class: ")


	if Race == "":
		Race = random.choice(Race_list)

	if BG == "":
		BG = random.choice(Background_list)
		
	if Class == "":
		Class = random.choice(list(Class_list))

	x = len(Class_list[Class])
	x-=1

	y = random.randint(0, x)

	z = Class_list[Class]

	UClass = z[y]

	print(f"""Race: {Race}
Background: {BG}
Class: {Class} - {UClass}""")

	again = " "

	while again != "y" and again != "n":
		again = input("Want to try again? y/n: ")

	if again == "n":
		break
