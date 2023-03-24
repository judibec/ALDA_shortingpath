# ALDA_shortingpath

## Description
In this project we can see differents algorithms for shorting path, we use Dijsktra, Bellman Ford and Floyd Warshall, each algorithm has different complexity and we could see that in the plots below

## Running locally and testing
* Create virtual enviroment: `virtualenv env`
* To install dependencies: `pip install -r requirements.txt`

## Test
In this test we create some graphs, the first one initialize with 500 nodes and the last one with 2000 nodes, but to time issues with the floyd algorithm ranges were changed from 50 to 200 because is very slow.

### Dijsktra
This is the fastest algorithm, for that reason the changes for each iteration are almost not perceived and in some cases looks constant
![image](https://user-images.githubusercontent.com/90010884/227402111-4ee9c282-ba08-4a85-9c93-4060ebfec300.png)
![image](https://user-images.githubusercontent.com/90010884/227402121-9afefee0-3bf9-443e-9449-cc70e067139c.png)

### Bellman Ford
This plot try to be linear it has some variations, but the results try to grow steadily
![image](https://user-images.githubusercontent.com/90010884/227402210-ea9dd16f-86ae-4ee1-ab31-bdbfdcd75344.png)
![image](https://user-images.githubusercontent.com/90010884/227402223-9906bbc6-3f3d-4606-9c81-3a97a2efe883.png)

### Floyd Warshall
In this we can see a similar behavior with Bellman Ford but remember that the first graph start with 50 nodes and the time is high, this is because the algorithm check all nodes with the distance of its neighbors
![image](https://user-images.githubusercontent.com/90010884/227402266-1b4dc487-a5c1-456c-b2db-125ae87cdf32.png)
![image](https://user-images.githubusercontent.com/90010884/227402280-58c170ed-e7e0-4491-bd42-4cb7465ea687.png)

## Current Coverage

To run `coverage`, make sure that you have it installed in your pc, if not run `pip install coverage`, then run the requirements.txt. After that run `coverage run -m unittest discover` and `coverage report` it show you the following table:

![image](https://user-images.githubusercontent.com/90010884/227403077-78dbaf92-ade8-431d-b2a3-2034e42c7248.png)

## Code Beautifer

After install Black, run de comand `black . -l 120` to beautifier you code
