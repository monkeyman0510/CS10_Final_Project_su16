import webbrowser
from random import randint, shuffle


def start():
	title = "\033[1m\033[35m\nFinal Project by Devin Rosenthal\n\033[0m"
	instructions = "\ntemp - fill in later"
	temp=""
	while("start" not in temp.lower()):
		temp = input("Type \"Help\" for Rules\nType \"Start\" to Start\nType \"Credits\" for Credits\n")
		if("help" in temp.lower()):
			webbrowser.open("http://www.cribbage.org/rules/rule1.asp")
		if ("credits" in temp.lower()):
			print(title)

list_of_all_cards = [['A','s'],[2,'s'],[3,'s'],[4,'s'],[5,'s'],[6,'s'],[7,'s'],[8,'s'],[9,'s'],['T','s'],['J','s'],['Q','s'],['K','s'],['A','c'],[2,'c'],[3,'c'],[4,'c'],[5,'c'],[6,'c'],[7,'c'],[8,'c'],[9,'c'],['T','c'],['J','c'],['Q','c'],['K','c'],['A','h'],[2,'h'],[3,'h'],[4,'h'],[5,'h'],[6,'h'],[7,'h'],[8,'h'],[9,'h'],['T','h'],['J','h'],['Q','h'],['K','h'],['A','d'],[2,'d'],[3,'d'],[4,'d'],[5,'d'],[6,'d'],[7,'d'],[8,'d'],[9,'d'],['T','d'],['J','d'],['Q','d'],['K','d']]

cardvals = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":10,"Q":10,"K":10}

def make_a_shuffled_deck(cards):
	#Takes list of all possible values and shuffles it to return a new deck
	newCards=cards[:]
	i=0
	shuf = input("How many times should the deck be shuffled?\n") #Takes user input
	print("Shuffling Cards")
	while(i<int(shuf)):
		shuffle(newCards)
		i+=1
	if(shuf==1):
		print("Shuffled 1 time")
	else:
		print("Shuffled "+shuf+" times")
	return newCards

def if_x_is_y_replace_with_z(x,y,z): #Used for abstraction
	if(x==y):
		return z
	else:
		return x

def get_value_of_card(inp):
	temp=inp[0]
	return cardvals[str(temp)]

def convert_card_list_to_symbols(cards):
	#Makes easy for user to read the cards
	symb=[]
	temp=""
	s=u"\u2660" #unicode value of spades
	c=u"\u2663" #unicode value of clubs
	h=u"\u2665" #unicode value of hearts
	d=u"\u2666" #unicode value of diamonds
	#return(s,c,h,d)
	for i in cards:
		temp=i[1]
		temp=if_x_is_y_replace_with_z(temp,'s',s) #Abstraction for instead of typing:
		temp=if_x_is_y_replace_with_z(temp,'c',c) #		if(temp=='s'):
		temp=if_x_is_y_replace_with_z(temp,'h',h) #			temp=s
		temp=if_x_is_y_replace_with_z(temp,'d',d) #4 times over (Also saves a little bit of space)
		symb.append([str(i[0])+" of "+temp]) 
	return symb

def remove_number_n_from_p_and_place_in_x(n,p,x):
	if (n>len(p) or n<=0):
		n=len(p)
	x.append(player_hand.pop(n-1)) #Assists with abstraction

def deal_n_using_deck(n): 
	#Takes n cards out of the deck variable and returns them as a seperate list
	player=[]
	for i in range(0,n):
		cardno=randint(0,len(deck)-1)
		player.append(deck[cardno])
		deck.remove(deck[cardno])
	return(player)

def debug():
	print("\nstart_card:\n"+str(convert_card_list_to_symbols(start_card)))
	print("\nplayer_hand:\n"+str(convert_card_list_to_symbols(player_hand)))
	print("\ncomp_hand:\n"+str(convert_card_list_to_symbols(comp_hand)))
	print("\ncrib:\n"+str(convert_card_list_to_symbols(crib)))
	print("\ndeck:\n"+str(convert_card_list_to_symbols(deck)))

def ptotal():
	print("\nThe current total is "+str(total))

def possible_discard(deck):
	global total
	for i in deck:
		if(int(cardvals[str([i][0][0])]) <= 31 - total):
			#print(get_value_of_card([i][0]))  #<-Used for testing
			return True
	return False

go=0
last_card=0

def discard_round(turn,total):
	global go
	if(len(player_remaining)==0 and len(comp_remaining)==0):
		print("There are no remaining cards. Now scoring")
	else:
		if(go==2):
			if(last_card==1):
				print("You placed the last card. You get 1 point!")
				player_score+=1
			else:
				print("The computer placed the last card and now gets a point")
				computer_score+=1
		if(turn==1):
			if(len(player_remaining)==0):
				print("You have run out of cards")
				discard_round(2,total)
			if(possible_discard(player_remaining)):
				print("\nHere is your hand") 
				print(convert_card_list_to_symbols(player_remaining))
				ptotal()
				temp=input("Which card would you like to play?\n")
				temp = int(temp)
				if(temp>len(player_remaining) or temp<1):
					print("The number that you have entered is out of range.")
					discard_round(1,total)
				if(int(get_value_of_card(player_remaining[temp-1])) + total > 31):
					print("The calue of that card is too high. The highest that the total can be is 31")
					discard_round(1,total)
				else:
					print("You have played the "+str(convert_card_list_to_symbols([player_remaining[temp-1]])))
					remove_number_n_from_p_and_place_in_x(temp,player_remaining,[])
					total = int(get_value_of_card(player_remaining[temp-1])) + total
					last_card=1
					if(total==15):
						print("You got the total to 15! You get 2 points!")
						player_score+=2
					if(total==31):
						print("You got the total to 31! You get 2 points!")
						player_score+=2
						total=0 
					discard_round(2,total)
			else:
				print("No possible moves. It is now the computer\'s turn")
				go+=1
				discard_round(2,total)
		else:
			if(len(comp_remaining)==0):
				print("The computer has run out of cards")
				discard_round(1,total)
			elif(possible_discard(comp_remaining)):
				temp=randint(1,len(comp_remaining))			
				if(temp>len(comp_remaining) or temp<1):
					discard_round(2,total)
					if(int(get_value_of_card(comp_remaining[temp-1])) + total > 31):
						discard_round(1,total)
					else:
						print("The computer has played the "+str(convert_card_list_to_symbols(comp_remaining[temp-1])))
						remove_number_n_from_p_and_place_in_x(temp,comp_remaining,[])
						total = int(get_value_of_card(comp_remaining[temp-1])) + total
						last_card=2 				
						if(total==15): 
							print("The comuputer got the total to 15 and has recieved 2 points.")
							computer_score+=2
						if(total==31): 
							print("The comuputer got the total to 31 and has recieved 2 points.")
							computer_score+=2
							total=0
						discard_round(1,total)
			else:
				go+=1
				print("The computer said go. It is now your turn.")
				discard_round(1,total)

start()



deck = make_a_shuffled_deck(list_of_all_cards)

player_hand=deal_n_using_deck(6)
comp_hand=deal_n_using_deck(4)
crib=deal_n_using_deck(2) #Auto adds computer's cards to crib - May add AI to do this instead (To make it more advanced)
start_card=deal_n_using_deck(1)[0]
player_score=0
computer_score=0
turn=1
total=0

print("\nHere is your hand. Please say the number (1-6) of one of the cards that you would like to place into the crib.\nPlease note \'T\' stands for 10 and that entering a number higher than your hand will use your last card.")
print(convert_card_list_to_symbols(player_hand))
temp=input("")
remove_number_n_from_p_and_place_in_x(int(temp),player_hand,crib)
print("\nPlease place one more card into the crib.")
print(convert_card_list_to_symbols(player_hand))
temp=input("")
remove_number_n_from_p_and_place_in_x(int(temp),player_hand,crib)
#print("\nHere is your hand")
#print(convert_card_list_to_symbols(player_hand)) 
#print("\nThe starting card is "+str(convert_card_list_to_symbols([start_card])))
player_remaining=player_hand[:]
comp_remaining=comp_hand[:]
discard_round(turn,0)


