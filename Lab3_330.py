"""
 Name: Jack Williams
 Assignment: Lab 3 - Process dataset
 Course: CS 330
 Semester: Fall 2021
 Instructor: Dr. Cao
 Date: the current date
 Sources consulted: any books, individuals, etc consulted

 Known Bugs: description of known bugs and other program imperfections

 Creativity: anything extra that you added to the lab

 Instructions: instructions to user on how to execute your program

"""
import sys
import argparse
import math
import pandas as pd

def splitData(data, trainData, testData, ratio):
    """
    Input: data
    Output: trainData, used for training your machine learning model
            testData, used to evaluate the performance of your machine learning model
            ratio, decide the percentage of training data on the whole dataset.
    Example:
            You have a training data with 10000 data record, ratio is 0.7, so you will split the whole dataset and store the first 7000 of them in trainData, and the rest 3000 in testData
    Instruction:
            There is no grading script for this function, because different group may select different dataset depending on their course project, but generally you should make sure that you code can divide the dataset correctly, since you may use it for the course project
    """
    if ratio < 0 or ratio > 1:
        raise ValueError("Ratio must be between 0 and 1.")

    split_index = int(len(data) * ratio)
    trainData = data[:split_index]
    testData = data[split_index:]
    return trainData, testData


def splitDataRandom(data, trainData, testData, ratio):
    """
    Input: data
    Output: trainData, used for training your machine learning model
            testData, used to evaluate the performance of your machine learning model
            ratio, decide the percentage of training data on the whole dataset.
    Example:
            You have a training data with 10000 data record, ratio is 0.7, so you will split the whole dataset and store 7000 of them in trainData, and 3000 in testData.
    Instruction:
            Almost same as splitData, the only difference is this function will randomly shuffle the input data, so you will randomly select data and store it in the trainData
    """
    if ratio < 0 or ratio > 1:
        raise ValueError("Ratio must be between 0 and 1.")

    data = data.sample(frac=1).reset_index(drop=True)
    split_index = int(len(data) * ratio)
    trainData = data[:split_index]
    testData = data[split_index:]
    return trainData, testData

def main():
    options = parser.parse_args()
    mode = options.mode       # first get the mode
    print("mode is " + mode)
    """
    similar to Lab 2, please add your testing code here
    """
    if mode == "train":
        print("Training mode is selected")
        train_model()

    elif mode == "test":
        print("Testing mode is selected")
        test_model()
    pass

def showHelper():
    """
    Similar to Lab 2, please update the showHelper function to show users how to use your code
    """
    parser.print_help(sys.stderr)
    print("\nUsage examples:")
    print("For random splitting:")
    print("python " + sys.argv[0] + " --mode R --input data.csv --train train_data.csv --test test_data.csv --ratio 0.7")

    print("For splitting:")
    print("python " + sys.argv[0] + " --mode N --input data.csv --train train_data.csv --test test_data.csv --ratio 0.7")

    print("\nOptions:")
    print("--mode: Select mode (R for random splitting, N for normal splitting).")
    print("--input: Path to the input data file.")
    print("--train: Path to store the training data file.")
    print("--test: Path to store the testing data file.")
    print("--ratio: The percentage of data to use for training (e.g., 0.7 for a 70/30 split).")
    sys.exit(0)


if __name__ == "__main__":
    #------------------------arguments------------------------------#
    #Shows help to the users                                        #
    #---------------------------------------------------------------#
    parser = argparse.ArgumentParser()
    parser._optionals.title = "Arguments"
    parser.add_argument('--mode', dest='mode',
    default = '',    # default empty!
    help = 'Mode: R for random splitting, and N for the normal splitting')

    """
    Similar to Lab 2, please update the argument, and add as you need
    """
    parser.add_argument('--mode', dest='mode', default='', help='Mode: R for random splitting, N for normal splitting')
    parser.add_argument('--input', dest='input', default='', help='Path to the input data file')
    parser.add_argument('--train', dest='train', default='', help='Path to store the training data file')
    parser.add_argument('--test', dest='test', default='', help='Path to store the testing data file')
    parser.add_argument('--ratio', dest='ratio', default=0.7, type=float, help='The percentage of data to use for training')

    if len(sys.argv)<3:
        showHelper()
    main()
