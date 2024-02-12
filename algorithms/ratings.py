import math

def floor_to_ndp(number, dp):
    mul = 10 ** dp
    return ((number*mul)//1)/(mul)

def round_to_ndp(number, dp):
    mul = 10 ** dp
    return round(number * mul) / mul

def chusan(score, chartLevel):

    if score > 1_010_000:
        raise Exception("Score cannot be greater than 1.01 million. Score given: " + str(score))
    if score < 0:
        raise Exception("Score cannot be negative. Score given: " + str(score))
    if chartLevel < 0:
        raise Exception("Chart level cannot be negative. Chart level given: " + str(chartLevel))
    
    levelBase = chartLevel * 100

    val = 0

    if score >= 1_009_000:
        val = levelBase + 215
    elif score >= 1_007_500:
        val = levelBase + 200 + (score - 1_007_500) / 100
    elif score >= 1_005_000:
        val = levelBase + 150 + ((score - 1_005_000) * 10) / 500
    elif score >= 1_000_000:
        val = levelBase + 100 + ((score - 1_000_000) * 5) / 500
    elif score >= 975_000:
        val = levelBase + ((score - 975_000) * 2) / 500
    elif score >= 900_000:
         val = levelBase - 500 + ((score - 900_000) * 2) / 300
    elif score >= 800_000:
        val = (levelBase - 500) / 2 + ((score - 800_000) * ((levelBase - 500) / 2)) / 100_000
    elif score >= 500_000:
        val = (((levelBase - 500) / 2) * (score - 500_000)) / 300_000

    return max(math.floor(val)/100, 0)

def chunithm(score, chartLevel):

    if score > 1_010_000:
        raise Exception("Score cannot be greater than 1.01 million. Score given: " + str(score))
    if score < 0:
        raise Exception("Score cannot be negative. Score given: " + str(score))
    if chartLevel < 0:
        raise Exception("Chart level cannot be negative. Chart level given: " + str(chartLevel))
    
    levelBase = chartLevel * 100

    val = 0

    if score >= 1_007_500:
        val = levelBase + 200
    elif score >= 1_005_000:
        val = levelBase + 150 + ((score - 1_005_000) * 10) / 500
    elif score >= 1_000_000:
        val = levelBase + 100 + ((score - 1_000_000) * 5) / 500
    elif score >= 975_000:
        val = levelBase + ((score - 975_000) * 2) / 500
    elif score >= 900_000:
         val = levelBase - 500 + ((score - 900_000) * 2) / 300
    elif score >= 800_000:
        val = (levelBase - 500) / 2 + ((score - 800_000) * ((levelBase - 500) / 2)) / 100_000
    elif score >= 500_000:
        val = (((levelBase - 500) / 2) * (score - 500_000)) / 300_000

    return max(math.floor(val)/100, 0)

def ongeki(score, chartLevel):
    if score > 1_010_000:
        raise Exception("Score cannot be greater than 1.01 million. Score given: " + str(score))
    if score < 0:
        raise Exception("Score cannot be negative. Score given: " + str(score))
    if chartLevel < 0:
        raise Exception("Chart level cannot be negative. Chart level given: " + str(chartLevel))
    
    rate = 0

    if score >= 1_007_500:
        rate = chartLevel + 2
    elif score >= 1_000_000:
        rate = chartLevel + 1.5 + ((score - 1_000_000) / 15_000)
    elif score >= 970_000:
        rate = chartLevel + ((score - 1_000_000) / 15_000)
    else:
        rate = chartLevel - ((970_000 - score) / 17_500)

    return floor_to_ndp(max(rate, 0), 2)

def wacca(score, chartLevel):
    if score > 1_000_000:
        raise Exception("Score cannot be greater than 1.01 million. Score given: " + str(score))
    if score < 0:
        raise Exception("Score cannot be negative. Score given: " + str(score))
    if chartLevel < 0:
        raise Exception("Chart level cannot be negative. Chart level given: " + str(chartLevel))
    
    coef = 1

    if score >= 990_000:
        coef = 4
    elif score >= 980_000:
        coef = 3.75
    elif score >= 970_000:
        coef = 3.5
    elif score >= 960_000:
        coef = 3.25
    elif score >= 950_000:
        coef = 3
    elif score >= 940_000:
        coef = 2.75
    elif score >= 920_000:
        coef = 2.5
    elif score >= 900_000:
        coef = 2
    elif score >= 850_000:
        coef = 1.5

    return round_to_ndp(coef * chartLevel, 3)

def museca(score,chartLevel):

    if score > 1_000_000:
        raise Exception("Score cannot be greater than 1 million. Score given: " + str(score))
    if score < 0:
        raise Exception("Score cannot be negative. Score given: " + str(score))
    if chartLevel < 0:
        raise Exception("Chart level cannot be negative. Chart level given: " + str(chartLevel))
    return math.floor(chartLevel * (score / 10_000))

def gitadora(score, chartLevel):
    if score > 100:
        raise Exception("Score cannot be greater than 100%. Score given: " + str(score))
    if score < 0:
        raise Exception("Score cannot be negative. Score given: " + str(score))
    if chartLevel < 0:
        raise Exception("Chart level cannot be negative. Chart level given: " + str(chartLevel))
    
    true_rating = score / 100 * chartLevel * 20


    return floor_to_ndp(true_rating, 2)

def jubeat(score, musicRate, chartLevel):
    if score < 0:
        raise Exception("Score cannot be negative. Score given: " + str(score))
    if score > 1000000:
        raise Exception("Score cannot be over 1000000. Score given: " + str(score))
    if chartLevel < 0:
        raise Exception("Chart level cannot be negative. Chart level given: " + str(chartLevel))
    if musicRate < 0:
        raise Exception("Music Rate cannot be negative. Music Rate given: " + str(musicRate))
    if musicRate > 120:
        raise Exception("Music Rate cannot be over 120. Music Rate given: " + str(musicRate))
    
    if score < 700000:
        return 0
    
    flooredRate = floor_to_ndp(musicRate, 1)
    jubility = chartLevel * 12.5 * (flooredRate / 99)

    return floor_to_ndp(jubility, 1)

def sdvx(score, lamp, chartLevel):

    if score > 10_000_000:
        raise Exception("Score cannot be greater than 10 million. Score given: " + str(score))
    if score < 0:
        raise Exception("Score cannot be negative. Score given: " + str(score))

    lamps = {
        "PERFECT ULTIMATE CHAIN": 1.1,
        "ULTIMATE CHAIN": 1.05,
        "EXCESSIVE CLEAR": 1.02,
        "HARD CLEAR": 1.02,
        "CLEAR": 1.0,
        "FAILED": 0.5,
        "PLAYED": 0.5,
    }

    grades = {
        "S": 1.05,
        "AAA+": 1.02,
        "AAA": 1.0,
        "AA+": 0.97,
        "AA": 0.94,
        "A+": 0.91,
        "A": 0.88,
        "B": 0.85,
        "C": 0.82,
        "D": 0.8,
    }

    grade = grades[SDVX_score_to_grade(score)]
    lamp = lamps[lamp]

    return floor_to_ndp((chartLevel * 2 * score / 10_000_000 * grade * lamp / 100), 3)



def SDVX_score_to_grade(score):
    if score < 7_000_000:
        return "D"
    elif score < 8_000_000:
        return "C"
    elif score < 8_700_000:
        return "B"
    elif score < 9_000_000:
        return "A"
    elif score < 9_300_000:
        return "A+"
    elif score < 9_500_000:
        return "AA"
    elif score < 9_700_000:
        return "AA+"
    elif score < 9_800_000:
        return "AAA"
    elif score < 9_900_000:
        return "AAA+"

    return "S"

def popn(score, lamp, level):
    if score < 0:
        raise Exception("Score cannot be negative. Score given: " + str(score))
    if score > 100_000:
        raise Exception("Score cannot be over 100,000. Score given: " + str(score))
    if level < 0:
        raise Exception("Chart level cannot be negative. Level given: " + str(score))
    
    lamps = {
        "CLEAR": 3000,
        "EASY CLEAR": 3000,
        "FULL COMBO": 5000,
        "PERFECT": 5000,
        "FAILED": 0
    }

    if score <= 50000:
        return 0
    
    clearBonus = lamps[lamp]

    return round_to_ndp((( 10000 * level) + (score - 50000) + (clearBonus)) / 5440, 2)