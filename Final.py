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
cards = [['A','s'],[2,'s'],[3,'s'],[4,'s'],[5,'s'],[6,'s'],[7,'s'],[8,'s'],[9,'s'],['T','s'],['J','s'],['Q','s'],['K','s'],['A','c'],[2,'c'],[3,'c'],[4,'c'],[5,'c'],[6,'c'],[7,'c'],[8,'c'],[9,'c'],['T','c'],['J','c'],['Q','c'],['K','c'],['A','h'],[2,'h'],[3,'h'],[4,'h'],[5,'h'],[6,'h'],[7,'h'],[8,'h'],[9,'h'],['T','h'],['J','h'],['Q','h'],['K','h'],['A','d'],[2,'d'],[3,'d'],[4,'d'],[5,'d'],[6,'d'],[7,'d'],[8,'d'],[9,'d'],['T','d'],['J','d'],['Q','d'],['K','d']]

cardvals = {'A':1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,'T':10,'J':10,'Q':10,'K':10}

def make_a_shuffled_deck(cards):
	i=0
	shuf = input("How many times should the deck be shuffled?\n")
	print("Shuffling Cards")
	while(i<int(shuf)):
		shuffle(cards)
		i+=1
		if(i==1):
			print("1 Shuffle")
		else:
			print(str(i)+" Shuffles")
	return cards

def convert_card_list_to_symbols(cards):
	symb=[]
	temp=""
	s=u"\u2660"
	c=u"\u2663"
	h=u"\u2665"
	d=u"\u2666"
	#return(s,c,h,d)
	for i in cards:
		temp=i[1]
		if(temp=="s"):
			temp=s
		if(temp=="c"):
			temp=c
		if(temp=="h"):
			temp=h
		if(temp=="d"):
			temp=d
		symb.append([str(i[0])+" of "+temp])
	return symb



print(convert_card_list_to_symbols(make_a_shuffled_deck(cards)))