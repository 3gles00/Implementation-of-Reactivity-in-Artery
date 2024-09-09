#!/usr/bin/env python

# reference variable to Storyboard Omnet++ module: board
import storyboard
import timeline

print ("demo.py successfully imported...")

def createStories(board):
	# Create coordinates needed for the PolygonCondition
	
		# Create coordinates needed for the PolygonCondition, the cordination correspond to Järnvägsleden
	coord4 = storyboard.Coord(2650, 1439)
	coord5 = storyboard.Coord(2755, 1439)
	coord6 = storyboard.Coord(2755, 1550)
	coord7 = storyboard.Coord(2650, 1550)
	# Create coordinates needed for the PolygonCondition, the cordination correspond to the roundabaout
	coord0 = storyboard.Coord(2931, 1340)
	coord1 = storyboard.Coord(2994, 1340)
	coord2 = storyboard.Coord(2994, 1428)
	coord3 = storyboard.Coord(2931, 1428)
	

	# Create PolygonCondition
	cond00 = storyboard.PolygonCondition([coord0, coord1, coord2, coord3])

	# Create TimeCondition
	cond1 = storyboard.TimeCondition(timeline.seconds(212), timeline.seconds(232))
	cond1a = storyboard.TimeCondition(timeline.seconds(312), timeline.seconds(332))



	# Create SpeedEffect
	effect0 = storyboard.SpeedEffect(2.44) #increasing the speed to see the outcome in a dense traffic area with complicated routes


	# Create AndConditions
	and0 = storyboard.AndCondition(cond00, cond1)
	and1 = storyboard.AndCondition(cond00,cond1a)
	



	cond4 = storyboard.PolygonCondition([coord4, coord5, coord6, coord7])

	cond5 = storyboard.TimeCondition(timeline.seconds(280), timeline.seconds(300))
	cond6 = storyboard.TimeCondition(timeline.seconds(500), timeline.seconds(520))
	cond7 = storyboard.TimeCondition(timeline.seconds(800), timeline.seconds(820))
	cond8 = storyboard.TimeCondition(timeline.seconds(380), timeline.seconds(400))
	cond9 = storyboard.TimeCondition(timeline.seconds(600), timeline.seconds(620))
	cond10 = storyboard.TimeCondition(timeline.seconds(900), timeline.seconds(920))
	cond11 = storyboard.TimeCondition(timeline.seconds(990), timeline.seconds(999))


	and2 = storyboard.AndCondition(cond4,cond5)
	and3 = storyboard.AndCondition(cond4,cond6)
	and4 = storyboard.AndCondition(cond4,cond7)
	and5 = storyboard.AndCondition(cond4,cond8)
	and6 = storyboard.AndCondition(cond4,cond9)
	and7 = storyboard.AndCondition(cond4,cond10)
	and8 = storyboard.AndCondition(cond4,cond11)


	#each stories are run in ~100ms with their speed doubled before setting the speed back to normal
	story0 = storyboard.Story(and0,[effect0])
	story1 = storyboard.Story(and1,[effect0])

	story2 = storyboard.Story(and2,[effect0])
	story3 = storyboard.Story(and3,[effect0])
	story4 = storyboard.Story(and4,[effect0])
	story5 = storyboard.Story(and5,[effect0])
	story6 = storyboard.Story(and6,[effect0])
	story7 = storyboard.Story(and7,[effect0])
	story8 = storyboard.Story(and8,[effect0])

		#3-lane
	board.registerStory(story0)
	board.registerStory(story1)

		#all roundabout
	board.registerStory(story2)
	board.registerStory(story3)
	board.registerStory(story4)
	board.registerStory(story5)
	board.registerStory(story6)
	board.registerStory(story7)
	board.registerStory(story8)

	print("Stories loaded!")