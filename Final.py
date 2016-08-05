import webbrowser
from random import randint, shuffle
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

cardvals = {'A':1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,'T':10,'J':10,'Q':10,'K':10}

def make_a_shuffled_deck(cards):
	i=0
	shuf = input("How many times should the deck be shuffled?\n") #Takes user input
	print("Shuffling Cards")
	while(i<int(shuf)):
		shuffle(cards)
		i+=1
		if(i==1):
			print("1 Shuffle")
		else:
			print(str(i)+" Shuffles")
	return cards

def if_x_is_y_replace_with_z(x,y,z):
	if(x==y):
		return z
	else:
		return x

def convert_card_list_to_symbols(cards):
	symb=[]
	temp=""
	s=u"\u2660" #unicode value of spades
	c=u"\u2663" #unicode value of clubs
	h=u"\u2665" #unicode value of hearts
	d=u"\u2666" #unicode value of diamonds
	#return(s,c,h,d)
	for i in cards:
		temp=i[1]
		temp=if_x_is_y_replace_with_z(temp,'s',s) #instead of typing:
		temp=if_x_is_y_replace_with_z(temp,'c',c) #		if(temp=='s'):
		temp=if_x_is_y_replace_with_z(temp,'h',h) #			temp=s
		temp=if_x_is_y_replace_with_z(temp,'d',d) #4 times
		symb.append([str(i[0])+" of "+temp]) #Makes easy for user to read the cards
	return symb

def deal_n_using_deck(n): 
	#Takes n cards out of the deck variable and returns them as a seperate list
	player=[]
	for i in range(0,n):
		cardno=randint(0,len(deck))
		player.append(deck[cardno])
		deck.remove(deck[cardno])
	return(player)

deck = make_a_shuffled_deck(list_of_all_cards)

player_hand=deal_n_using_deck(6)
comp_hand=deal_n_using_deck(4)
crib=deal_n_using_deck(2) #Auto adds computer's cards to crib - May add AI to do this instead (To make it more advanced)

print(convert_card_list_to_symbols(deck))
print(" ")
print(convert_card_list_to_symbols(player_hand))
print(" ")
print(convert_card_list_to_symbols(comp_hand))
print(" ")
print(convert_card_list_to_symbols(crib))
print(" ")
print(convert_card_list_to_symbols(deck))