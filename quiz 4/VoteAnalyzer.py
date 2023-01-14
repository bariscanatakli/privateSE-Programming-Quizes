import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

sysFileName = sys.argv[1]
sysNomineesList = (sys.argv[2]).split(",")


def retrieveData(fileName, filteredList):
    file = pd.read_csv(fileName)
    filteredList = file.filter(filteredList)

    electionDataList = list()
    retrievedData = open("retrievedData.txt", "w")

    for election in sysNomineesList:
        for data in filteredList[election].to_list():
            electionDataList.append(data)

    retrievedData.write(str(electionDataList))
    return electionDataList


def DispBarPlot():
    file = pd.read_csv(sysFileName)
    filteredList = file.filter(sysNomineesList)
    sums = filteredList.sum(axis=0, skipna=True)
    nominees = dict(sums.sort_values())
    # print(nominees)
    firstNominee = max(nominees, key=nominees.get)
    del nominees[firstNominee]
    secondNominee = max(nominees, key=nominees.get)
    del nominees[secondNominee]
    firstNomineVotes = filteredList[firstNominee].to_list()
    secondNomineVotes = filteredList[secondNominee].to_list()

    width = 0.3
    plt.rc('font', size=7)
    statesList = file["State of Dist"].to_list()
    x = np.arange(len(statesList))

    fig, ax = plt.subplots()

    bar1 = ax.bar(x+width/2, firstNomineVotes, 0.3,
                  label=firstNominee, color="b")
    bar2 = ax.bar(x-width/2, secondNomineVotes, 0.3,
                  label=secondNominee, color="r")

    ax.set_xticks(x)
    ax.set_xticklabels(statesList)
    ax.yaxis.get_offset_text().set_visible(False)

    current_values = ax.get_yticks()

    ax.set_yticklabels(['{:.0f}'.format(x) for x in current_values])
    ax.legend()
    plt.xticks(rotation=90)
    plt.xlabel("States")
    plt.ylabel("Vote Counts")

    plt.savefig('ComparativeVotes.pdf', format="pdf")
    plt.show()


def compareVoteonBar():
    file = pd.read_csv(sysFileName)
    filteredList = file.filter(sysNomineesList)
    sums = filteredList.sum(axis=0, skipna=True)
    nominees = dict(sums.sort_values())
    sumNominees = sum(nominees.values())

    plt.rc('font', size=7)

    x = np.array(list(reversed(nominees.keys())))

    y = np.array(list(reversed(nominees.values())))

    fig, ax = plt.subplots()
    votePercentages = list()
    for nominee, votes in zip(x, y):
        votePercentage = (votes/sumNominees*100).round(3)
        votePercentages.append(votePercentage)
        ax.bar(nominee, votePercentage, label=nominee)

    ax.set_xticklabels(votePercentages)
    plt.legend()

    plt.xlabel("Nominees")
    plt.ylabel("Vote Percentages")

    plt.savefig('CompVotePercs.pdf', format="pdf")
    plt.show()


def obtainHistogram(inputList):
    repeatedNumbers = list()
    returnList = list()
    for number in inputList:
        if len(str(number)) == 1:
            firstDigit = number
            secondDigit = 0
        else:
            firstDigit = int(str(number)[len(str(number))-1])
            secondDigit = int(str(number)[len(str(number))-2])

        repeatedNumbers.append(firstDigit)
        repeatedNumbers.append(secondDigit)

    for number in range(10):
        returnList.append((repeatedNumbers.count(number))/(len(inputList)*2))
    return returnList


def plotHistogram(name, obtainList):
    yLine = list()
    for number in range(10):
        yLine.append(0.10)
    y1 = obtainHistogram(obtainList)
    y2 = yLine
    fig, ax = plt.subplots()
    ax.plot(y1, label="Digit Dist.")
    ax.plot(y2, linestyle="dashed", label="Mean")

    ax.set_xticks(range(10))
    plt.legend()
    plt.xlabel("Distribution")
    plt.ylabel("Digits")
    if type(name) == tuple:

        plt.title(f"Histogram of least sign. digits - {name[1]}")
        plt.savefig(name[0], format="pdf")
    else:
        plt.title(f"Histogram of least sign. digits")
        plt.savefig(name, format="pdf")

    plt.show()


def createRandomList(size):
    return np.random.randint(100, size=size)


def plotHistogramWidthSample():
    randomPdfList = [10, 50, 100, 1000, 10000]
    for listSize in randomPdfList:
        index = randomPdfList.index(listSize)+1
        plotHistogram(
            (f"HistogramofSample{index}.pdf", f"Sample:{index}"), createRandomList(listSize))


def calculateMSE(firstList):
    secondList = list()
    for number in range(10):
        secondList.append(0.10)
    total = int()
    lengthOfList = len(firstList) or len(secondList)
    for i in range(lengthOfList):
        total += (firstList[i] - secondList[i])**2
    return total/lengthOfList


retrieveData(sysFileName, sysNomineesList)

DispBarPlot()

compareVoteonBar()

plotHistogram("Histogram.pdf", retrieveData(sysFileName, sysNomineesList))

plotHistogramWidthSample()

MSE_value = calculateMSE(obtainHistogram(retrieveData(
    sysFileName, sysNomineesList)))

print(MSE_value)
