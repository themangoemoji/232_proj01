import pythomon
import pythomon_creatures
import random
import time

def setup_battle():	master_name = input('What is your name, young master??')
    wild_random_int = random.randint(1,2)
    master_random_int = random.randint(3,4)
    creature_dict = {1:pythomon_creatures.Pythee,2:pythomon_creatures.Seeplus,3:pythomon_creatures.Roobee,4:pythomon_creatures.Javas}
    wild_creature = creature_dict[wild_random_int]
    master_creature = creature_dict[master_random_int]
    return (wild_creature, master_creature,master_name)

def pick_pythomon():
	pass

def end_battle(wild_creature,master_creature):
	game_over = False
	if wild_creature.dead == True:
		game_over = True

def critical_hit_bool():
	critical_hit = False
	critical_hit_int = random.randint(1,2)
	if critical_hit_int == 1:
		critical_hit = True
	return critical_hit

def attack_normal(master_creature,wild_creature,master_move):
	master_creature.attack(wild_creature,master_move)
	time.sleep(0.4)
	print('.',end = '')
	time.sleep(0.4)
	print('.',end = '')
	time.sleep(0.4)
	print('.',end = '')
	print(wild_creature.name,' has ',wild_creature.remainingHP,' health points left.')

def attack_with_CritHit(master_creature,wild_creature,master_move):
	time.sleep(0.4)
	print('.',end = '')
	time.sleep(0.4)
	print('.',end = '')
	time.sleep(0.4)
	print('.',end = '')
	time.sleep(0.4)
	print('.',end = '')
	time.sleep(0.4)
	print('.')
	time.sleep(1)
	print('\n\nCRITICAL HIT!!!')
	master_creature.attack(wild_creature,master_move)
	master_move = 4
	master_creature.critical_hit(wild_creature,master_move)
	#only print health points after critical hit
	print(wild_creature.name,' has ',wild_creature.remainingHP,' health points left.')

def wild_creature_attack(wild_creature,master_creature,wild_move_lst_length):
	wild_creature_move = random.randint(0,wild_move_lst_length-1)
	print('\nThe wild ',wild_creature.name,' used ',wild_creature.move_list[wild_creature_move])
	time.sleep(0.4)
	print('.',end = '')
	time.sleep(0.4)
	print('.',end = '')
	time.sleep(0.4)
	print('.',end = '')
	wild_creature.attack(master_creature,wild_creature_move)
	print('Your ',master_creature.name,' has ',master_creature.remainingHP,' health points left.')

def display_help(master_move_lst_length,master_creature):
	#HELP display and Move information
				print('\nHELP MENU\n---------\nYou can attack the wild Pythomon by commanding your Pythomon with a move from your move list.\nYour available moves are: \n')
				for i in range(master_move_lst_length + 1):
					print('{}:{:<15}-->{:>3} damage, {} moves left'.format(i+1,master_creature.move_list[i].name,master_creature.move_list[i].power,master_creature.move_list[i].ml))

def display_intro(wild_creature,master_creature,master_name):
	print('You, ',master_name,', a novice master, find yourself walking in some tall grass...',)
	time.sleep(2)
	print('\n\nAnd all of the sudden.',end ='')
	time.sleep(0.4)
	print('.',end = '')
	time.sleep(0.4)
	print('.',end = '')
	time.sleep(0.4)
	print('.',end = '')
	time.sleep(0.4)
	print('.',end = '')
	time.sleep(0.4)
	print('.')
	time.sleep(1)
	print('\n\nA wild pythomon appears!!!\n\n')

	print('You are battling a ',wild_creature.name,'with ',wild_creature.remainingHP,' health points with your',master_creature.name,'!')

	#help menu
	master_move_lst_length = len(master_creature.move_list)
	wild_move_lst_length = len(wild_creature.move_list)
	print('press a number 1-',master_move_lst_length,' to attack the wild pokemon!')

def wild_creature_dies(wild_creature,master_name):
	if wild_creature.dead() == True:
		time.sleep(0.4)
		print('.',end = '')
		time.sleep(0.4)
		print('.',end = '')
		time.sleep(0.4)
		print('.',end = '')
		time.sleep(0.4)
		print('.',end = '')
		time.sleep(0.4)
		print('.')
		print('\n\nThe wild ',wild_creature.name,' died!')
		time.sleep(1)
		print('\n\nYOU WON, ',master_name,'!!!')

def play(setup_tuple):
	wild_creature = setup_tuple[0]
	master_creature = setup_tuple[1]
	master_name = setup_tuple[2]
	#calling the <display_intro> function to print the introduction to battle
	#display_intro(wild_creature,master_creature,master_name)

	#help menu
	master_move_lst_length = len(master_creature.move_list) -1
	wild_move_lst_length = len(wild_creature.move_list) -1
	print('press a number 1-',master_move_lst_length,' to attack the wild pokemon!')
	game_over = False
	user_input = None
	while not game_over:
		try:
			user_input = input('\nYour turn!\n')
			if user_input == 'h':
				#HELP display and Move information
				display_help(master_move_lst_length,master_creature)				
			#Attacking Wild Pokemon
			else:
				#user move to attack the wild pokemon
				#this adjusts the user input to align with the indexing
					#1 = 0, 2 = 1, etc.
				master_move = int(user_input) - 1
				print(str(master_name)+'\'s ',master_creature.name,' used ',master_creature.move_list[master_move])
				critical_hit = critical_hit_bool()

				#attacking in instance of Critical Hit
				if critical_hit == True:
					attack_with_CritHit(master_creature,wild_creature,master_move)

					#If the creature died after your attack and critical hit
					if wild_creature.dead() == True:
						wild_creature_dies(wild_creature,master_name)
						game_over = True

					elif wild_creature.dead() == False:
						wild_creature_attack(wild_creature,master_creature,wild_move_lst_length)
						if master_creature.dead() == True:
							print('\n\nYou\'re ',master_creature.name,' died!\nYou lost the battle, ',master_name,'!!!')
							game_over = True

				#Attacking without critical hit, if wild creature dies
				elif critical_hit == False:
					attack_normal(master_creature,wild_creature,master_move)
					#if wild creature died from that attack					
					if wild_creature.dead() == True:
						wild_creature_dies(wild_creature,master_name)
					else:
						game_over = False
				#Attacking without critical hit, if wild creature survives
					if game_over == False:
						wild_creature_attack(wild_creature,master_creature,wild_move_lst_length)
						if master_creature.dead() == True:
							print('\n\nYou\'re ',master_creature.name,' died!\nYou lost the battle, ',master_name,'!!!')
							game_over = True
			if wild_creature.dead() == True:
				wild_creature_dies(wild_creature,master_name)
				game_over = True
		except (IndexError,ValueError):
			print('Don\'t get distracted! You\'re in a battle!!!')

play(setup_battle())
