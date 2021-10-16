# AlgorithmsProjectOne, Python Implementation

## Hardware Information
The project was ran on a Red Hat Linux research server, with many cores and over 1TB of ram. I created a test.sh script that would run all of the required tests and outputted them to a text file. This text file was then migrated into the given csv file.

The projext, was written, tested, and developed in a linux environment and has not been tested to work
on mac or windows, however it should.

## How to run
In order to run the program you must enter the same directory as main.py. Main.py is the driver function
that will take command line arguments and send them to the respective algorithm.

Run command structure: 
```
python main.py <ALGORITHM> <SIZE> <TYPE_OF_DATA>
```

The valid choices for ALGORITHM are:
    q - Quicksort
    i - Insertion Sort
    s - Selection Sort

The valid choices for SIZE are:
    Any positive integer value, bad inputs are rejected.

The valid choices for TYPE_OF_DATA are:
    s - Sorted Data Array
    c - Constant Data Array
    r - Random Data Array

Example command to run:
```
python main.py q 10000 s
```

This will run quicksort on a sorted array of size 10000.

I have also left a smaller version of the  test.sh script as an example of what I used to run them.
