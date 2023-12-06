'''
--- Day 5: If You Give A Seed A Fertilizer ---
You take the boat and find the gardener right where you were told he would be: managing a giant "garden" that looks more to you like a farm.

"A water source? Island Island is the water source!" You point out that Snow Island isn't receiving any water.

"Oh, we had to stop the water because we ran out of sand to filter it with! Can't make snow with dirty water. Don't worry, I'm sure we'll get more sand soon; we only turned off the water a few days... weeks... oh no." His face sinks into a look of horrified realization.

"I've been so busy making sure everyone here has food that I completely forgot to check why we stopped getting more sand! There's a ferry leaving soon that is headed over in that direction - it's much faster than your boat. Could you please go check it out?"

You barely have time to agree to this request when he brings up another. "While you wait for the ferry, maybe you can help us with our food production problem. The latest Island Island Almanac just arrived and we're having trouble making sense of it."

The almanac (your puzzle input) lists all of the seeds that need to be planted. It also lists what type of soil to use with each kind of seed, what type of fertilizer to use with each kind of soil, what type of water to use with each kind of fertilizer, and so on. Every type of seed, soil, fertilizer and so on is identified with a number, but numbers are reused by each category - that is, soil 123 and fertilizer 123 aren't necessarily related to each other.

The gardener and his team want to get started as soon as possible, so they'd like to know the closest location that needs a seed. Using these maps, find the lowest location number that corresponds to any of the initial seeds. To do this, you'll need to convert each seed number through other categories until you can find its corresponding location number. In this example, the corresponding types are:

Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.
So, the lowest location number in this example is 35.

What is the lowest location number that corresponds to any of the initial seed numbers?

'''
# not 922601426

import logger

def readInput(filename):
    with open(filename, 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    # create list of seeds
    seedslist = [int(x) for x in (lines[0])[6:].split()]
    
    # name these individually so I get less confused instead of doing them all in a more efficient loop
    seedSoilMap = []
    soilFertilizerMap = []
    fertilizerWaterMap = []
    waterLightMap = []
    lightTempMap = []
    tempHumidMap = []
    humidLocMap = []

    soilStart = lines.index('soil-to-fertilizer map:')-1
    fertStart = lines.index('fertilizer-to-water map:')-1
    waterStart = lines.index('water-to-light map:')-1
    lightStart = lines.index('light-to-temperature map:')-1
    tempStart = lines.index('temperature-to-humidity map:')-1
    humidStart = lines.index('humidity-to-location map:')-1
    
    # seed Soil Map Creation
    for line in lines[3:soilStart]:
        mapVal = [int(x) for x in line.split()]
        seedSoilMap.append(mapVal)
    
    # soil fertilizer map creation
    for line in lines[soilStart+2:fertStart]:
        mapVal = [int(x) for x in line.split()]
        soilFertilizerMap.append(mapVal)
 
    # fertilizer water map creation
    for line in lines[fertStart+2:waterStart]:
        mapVal = [int(x) for x in line.split()]
        fertilizerWaterMap.append(mapVal)
        
    # water light map creation
    for line in lines[waterStart+2:lightStart]:
        mapVal = [int(x) for x in line.split()]
        waterLightMap.append(mapVal)
    
    # light temp map creation
    for line in lines[lightStart+2:tempStart]:
        mapVal = [int(x) for x in line.split()]
        lightTempMap.append(mapVal)
    
    # temperature humidity map creation
    for line in lines[tempStart+2:humidStart]:
        mapVal = [int(x) for x in line.split()]
        tempHumidMap.append(mapVal)
    
    # humidity location map creation
    for line in lines[humidStart+2:]:
        mapVal = [int(x) for x in line.split()]
        humidLocMap.append(mapVal)
    
    return seedslist, [seedSoilMap, soilFertilizerMap, fertilizerWaterMap, 
            waterLightMap, lightTempMap, tempHumidMap, humidLocMap]


def updateMappingsToStartEnd(mappingsList):
    '''takes the list of mappings
    format of input: the destination range start, the source range start, and the range length 
    returns: list of lists with 3 items: startOfEligibleMapItems,endOfEligibleMapItems, shiftAmount'''

    updatedMappings = []
    for item in mappingsList:
        destStart = item[0]
        sourceStart = item[1]
        rangeLength = item[2]

        shift = destStart - sourceStart

        startOfEligibleMapItems = sourceStart
        endOfEligibleMapItems = sourceStart+rangeLength

        updatedMappings.append([startOfEligibleMapItems, endOfEligibleMapItems, shift])
    
    return updatedMappings

def mapStep(seedlist, updatedMappings):
    ''' calculates the mapping of a seed to its new value based on the given mapping '''
    mappedSeeds = []
    for seed in seedlist:
        for mapping in updatedMappings:
            startOfEligibleMapItems = mapping[0]
            endOfEligibleMapItems = mapping[1]
            shift = mapping[2]
            # if it is a part of this mapping, we will map it to this
            if startOfEligibleMapItems <= seed < endOfEligibleMapItems:
                seed = seed+shift
                break
        mappedSeeds.append(seed)
    return mappedSeeds

def seedLocationMapping(seedsList, allMapsList):
    for mappingList in allMapsList:
        updatedMapping = updateMappingsToStartEnd(mappingList)
        seedsList = mapStep(seedsList, updatedMapping)
    return seedsList

if __name__ == '__main__':
    seedList, initMappingList = readInput('day5/input.txt')
    seedsList = seedLocationMapping(seedList, initMappingList)
    print("minimum seed: ", min(seedsList))