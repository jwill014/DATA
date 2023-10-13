# Data
The input for this repository is a csv file that contains the number of applicants for a Social Security card by year of birth and sex. The number of applicants is restricted to U.S. births where the year of birth, sex, State of birth, including the district of columbia, are known, and where the given name is at least 2 characters long.

The data set looked interesting, and was thought to be a google example for this lab, as it had a large amount of entries as it spans from 1910 to 2013. 

The output at this time is the data being plit into a training and a testing set for use later on. This can be done by just splitting the file, or by mixing up the file randomly then splitting it to get a better varrient of states in each set. 

This data set was found by looking through the datas sets provided in Google Open Datasets, and finding one that I found to be the most interesting.

You run the code by choosing which function you want to use, splitData or splitDataRandom, depending on how you want your data to be divied up. You type in the is function then provide your dataset, which is usa_1910_2013.csv along with trainData, testData, and ratio. trainData and testData are files to hold the data once it is split up using the ratio to determine how much of the data fgoes into each file.
