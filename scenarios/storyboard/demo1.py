#!/usr/bin/env python

# reference variable to Storyboard Omnet++ module: board
import storyboard
import timeline

print ("demo.py successfully imported...")

def createStories(board):
	# Create coordinates needed for the PolygonCondition

	#the cordination correspond to the roundabaout
	coord0 = storyboard.Coord(2931, 1340)
	coord1 = storyboard.Coord(2994, 1340)
	coord2 = storyboard.Coord(2994, 1428)
	coord3 = storyboard.Coord(2931, 1428)
	
	# Create PolygonCondition
	cond0 = storyboard.PolygonCondition([coord0, coord1, coord2, coord3])

	# Create TimeCondition
	cond1 = storyboard.TimeCondition(timeline.seconds(115), timeline.seconds(150))
	cond2 = storyboard.TimeCondition(timeline.seconds(150), timeline.seconds(200))

	# Create SpeedEffect
	effect0 = storyboard.SpeedEffect(17) #increasing the speed to see the outcome in a dense traffic area with complicated routes

	# Create AndConditions
	and0 = storyboard.AndCondition(cond0, cond1)
	
	# the cordination correspond to J채rnv채gsleden
	coord4 = storyboard.Coord(2650, 1439)
	coord5 = storyboard.Coord(2755, 1439)
	coord6 = storyboard.Coord(2755, 1550)
	coord7 = storyboard.Coord(2650, 1550)

	cond4 = storyboard.PolygonCondition([coord4, coord5, coord6, coord7])

	and1 = storyboard.AndCondition(cond4,cond2)

	#each stories are run in with their speed doubled
	story0 = storyboard.Story(and0,[effect0])
	story1 = storyboard.Story(and1,[effect0])

	#roundabout
	board.registerStory(story0)

	#j채rnv채gsleden
	board.registerStory(story1)

	print("Stories loaded!")
