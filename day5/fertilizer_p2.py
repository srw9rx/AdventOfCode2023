'''--- Part Two ---
Everyone will starve if you only plant such a small number of seeds. Re-reading the almanac, it looks like the seeds: line actually describes ranges of seed numbers.

The values on the initial seeds: line come in pairs. Within each pair, the first value is the start of the range and the second value is the length of the range. So, in the first line of the example above:

seeds: 79 14 55 13
This line describes two ranges of seed numbers to be planted in the garden. The first range starts with seed number 79 and contains 14 values: 79, 80, ..., 91, 92. The second range starts with seed number 55 and contains 13 values: 55, 56, ..., 66, 67.

Now, rather than considering four seed numbers, you need to consider a total of 27 seed numbers.

In the above example, the lowest location number can be obtained from seed number 82, which corresponds to soil 84, fertilizer 84, water 84, light 77, temperature 45, humidity 46, and location 46. So, the lowest location number is 46.

Consider all of the initial seed numbers listed in the ranges on the first line of the almanac. What is the lowest location number that corresponds to any of the initial seed numbers?
'''
import logger

def readInput(filename):
    with open(filename, 'r') as f:
        lines = [x.strip() for x in f.readlines()]

    # create list of seeds
    seedslist = [int(x) for x in (lines[0])[6:].split()]
    starts = seedslist[0::2]
    counts = seedslist[1::2]
    seedsDict = [[start, count] for start, count in zip(starts, counts)]
    
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
    
    return seedsDict, [seedSoilMap, soilFertilizerMap, fertilizerWaterMap, 
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
    
    # sort to ensure that when we do batching, we do not miss something and can continue through the for loop
    updatedMappingsSorted = sorted(updatedMappings, key=lambda mapItem: mapItem[0])
    
    return updatedMappingsSorted

def mapStep(seedDict, updatedMappings):
    ''' calculates the mapping of a seed to its new value based on the given mapping '''
    mappedSeeds = []
    for seedStart, seedCount in seedDict:
        seeds = mapStepInd_Recursion(seedStart, seedCount, updatedMappings)
        mappedSeeds = mappedSeeds + seeds
    return mappedSeeds

def mapStepInd_Recursion(seedStart, seedCount, updatedMappings):
    for mapping in updatedMappings:
        startOfEligibleMapItems = mapping[0]
        endOfEligibleMapItems = mapping[1]
        shift = mapping[2]
        seedEnd = seedStart + seedCount
        mappingSeedCount = endOfEligibleMapItems - startOfEligibleMapItems
        
        # if start is a part of this mapping, consider. 
        if startOfEligibleMapItems <= seedStart < endOfEligibleMapItems:
            newSeedStart = seedStart+shift
            if mappingSeedCount <= seedCount:
                # base case, doesn't have to be split
                seedsList = [[newSeedStart, seedCount]]
                return seedsList
            else:
                seedsList = [[newSeedStart, mappingSeedCount]]
                newSeedCount = seedCount - mappingSeedCount
                return seedsList + mapStepInd_Recursion(seedStart+mappingSeedCount, newSeedCount, updatedMappings)
        else:
            # if no mapping to be done, return the same thing it was
            return [[seedStart, seedCount]]
                


def seedLocationMapping(seedsDict, allMapsList):
    for mappingList in allMapsList:
        updatedMapping = updateMappingsToStartEnd(mappingList)
        seedsList = mapStep(seedsDict, updatedMapping)
        print(seedsList)
    return seedsList

if __name__ == '__main__':
    seedsDict, initMappingList = readInput('day5/exampleinput.txt')
    print(seedsDict)
    seedsResults = seedLocationMapping(seedsDict, initMappingList)
    initialSeeds = [x[0] for x in seedsResults]
    print("minimum seed: ", min(initialSeeds))