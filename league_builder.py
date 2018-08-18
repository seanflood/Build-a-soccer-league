#use dunder main 


if __name__ == "__main__":

	import csv
	
	players = [] 
    

#open csv file 
	def file_():
		with open('soccer_players.csv') as csv_file:
			reader = csv.reader(csv_file)
			for row in reader:
				del row[1] 
				players.append(row)
			del players[0] 


#create experienced/unexperienced lists and separate accordingly 	
	explay = []
	nonex = [] 
	
	
	def playerex():
		for player in players:
			if player[1] == "YES":
				explay.append(player)
			else:
				nonex.append(player)

                   
#Create team name lists and assign players by experience                 
                
	dragons = []
	raptors = []
	sharks = [] 
	
	def player_sort():
		for explayer in range(int(len(explay)/3)):
			dragons.append(explay.pop(explayer))
		
		for nonexplayer in range(int(len(nonex)/3)):
			dragons.append(nonex.pop(nonexplayer))

		for explayer in range(int(len(explay)/2)):
			raptors.append(explay.pop(explayer))

		for nonexplayer in range(int(len(nonex)/2)):
			raptors.append(nonex.pop(nonexplayer))

		for explayer in range(int(len(explay))):
			sharks.append(explay.pop())

		for nonexplayer in range(int(len(nonex))):
			sharks.append(nonex.pop())

			
#write text file with correct spaceing 			
			
			
	def textwrite():
		final = open("teams.txt", "w")
		final.write("Dragons")
		for dragon in dragons:
			final.write("\n")
			final.write(", ".join(dragon))

		final.write("\n \nRaptors")
		for raptor in raptors:
			final.write("\n")
			final.write(", ".join(raptor))

		final.write("\n \nSharks")
		for shark in sharks:
			final.write("\n")
			final.write(", ".join(shark))


	file_()
	playerex()
	player_sort()
	textwrite()
	