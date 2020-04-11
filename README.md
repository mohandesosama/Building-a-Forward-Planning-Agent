
## Introduction
Planning is an important topic in AI because intelligent agents are expected to automatically plan their own actions in uncertain domains. Planning and scheduling systems are commonly used in automation and logistics operations, robotics and self-driving cars, and for aerospace applications like the Hubble telescope and NASA Mars rovers.

This project is split between implementation and analysis. First you will combine symbolic logic and classical search to implement an agent that performs progression search to solve planning problems. Then you will experiment with different search algorithms and heuristics, and use the results to answer questions about designing planning systems.

Read all of the instructions below and the project rubric [here](https://review.udacity.com/#!/rubrics/1800/view) carefully before starting the project so that you understand the requirements for successfully completing the project. Understanding the project requirements will help you avoid repeating parts of the experiment, some of which can have long runtimes.

**NOTE:** You should read "Artificial Intelligence: A Modern Approach" 3rd edition chapter 10 *or* 2nd edition Chapter 11 on Planning, available [on the AIMA book site](http://aima.cs.berkeley.edu/2nd-ed/newchap11.pdf) before starting this project.

See the [Project Enhancements](#optional-project-enhancements) section at the end for additional notes about limitations of the code in this exercise.

![Progression air cargo search](images/Progression.PNG)


## Getting Started (Local Environment)
If you would prefer to complete the exercise in your own local environment, then follow the steps below:

#### Create and activate Conda Environment
* Open a terminal and run conda `env create -f aind-universal-v3.yml` to create the environment.
* Activate the environment
run `source activate aind` (OSX & Linux)
run `activate aind` (Windows)

**WARNING: SOME OPERATING SYSTEMS MAY PRODUCE ERRORS WHILE INSTALLING Z3 -- DO NOT PANIC. The exercise using Z3 can be run directly in the classroom.**


## Instructions

1. Start by running the example problem (this example implements the "have cake" problem from Fig 10.7 of AIMA 3rd edition). The script will print information about the problem domain and solve it with several different search algorithms, however these algorithms cannot solve larger, more complex problems so next you'll have to implement a few more sophisticated heuristics.
```
$ python example_have_cake.py
```

2. Open `my_planning_graph.py` and complete the TODO sections. Documentation for the planning graph classes is provided in the docstrings and examples [here](examples.md). Refer to the heuristics pseudocode [here](pseudocode/heuristics.md), chapter 10 of AIMA 3rd edition or chapter 11 of AIMA 2nd edition (available [on the AIMA book site](http://aima.cs.berkeley.edu/2nd-ed/newchap11.pdf)) and the detailed instructions inline with each TODO statement for help. You should implement the following functions:

  - `ActionLayer._inconsistent_effects`
  - `ActionLayer._interference`
  - `ActionLayer._competing_needs`
  - `LiteralLayer._inconsistent_support`
  - `LiteralLayer._negation`
  - `PlanningGraph.h_levelsum`
  - `PlanningGraph.h_maxlevel`
  - `PlanningGraph.h_setlevel`

After you complete each function, test your solution by running `python -m unittest -v`. **YOU SHOULD PASS EACH TEST CASE IN ORDER.** Some of the later test cases depend on correctly implementing the earlier functions, so working on the test cases out of order will be more difficult.


3. Experiment with different search algorithms using the `run_search.py` script. (See example usage below.) The goal of your experiment is to understand the tradeoffs in speed, optimality, and complexity of progression search as problem size increases. You will record your results in a report (described below in [Report Requirements](#report-requirements)).

  - Run the search experiment manually (you will be prompted to select problems & search algorithms)
```
$ python run_search.py -m
```

  - You can also run specific problems & search algorithms - e.g., to run breadth first search and UCS on problems 1 and 2:
```
$ python run_search.py -p 1 2 -s 1 2
```


### Experiment with the planning algorithms

The `run_search.py` script allows you to choose any combination of eleven search algorithms (three uninformed and eight with heuristics) on four air cargo problems. The cargo problem instances have different numbers of airplanes, cargo items, and airports that increase the complexity of the domains.

- You should run **all** of the search algorithms on the first two problems and record the following information for each combination:
    - number of actions in the domain
    - number of new node expansions
    - time to complete the plan search

- Use the results from the first two problems to determine whether any of the uninformed search algorithms should be excluded for problems 3 and 4. You must run **at least** one uninformed search, two heuristics with greedy best first search, and two heuristics with A* on problems 3 and 4.


## Report Requirements

Your submission for review **must** include a report named "report.pdf" that includes all of the figures (charts or tables) and written responses to the questions below. You may plot multiple results for the same topic on the same chart or use multiple charts. (Hint: you may see more detail by using log space for one or more dimensions of these charts.)

- Use a table or chart to analyze the number of nodes expanded against number of actions in the domain
- Use a table or chart to analyze the search time against the number of actions in the domain
- Use a table or chart to analyze the length of the plans returned by each algorithm on all search problems

Use your results to answer the following questions:

- Which algorithm or algorithms would be most appropriate for planning in a very restricted domain (i.e., one that has only a few actions) and needs to operate in real time?

- Which algorithm or algorithms would be most appropriate for planning in very large domains (e.g., planning delivery routes for all UPS drivers in the U.S. on a given day)

- Which algorithm or algorithms would be most appropriate for planning problems where it is important to find only optimal plans?

## Submission
Before you can submit your project for review in the classroom, you must run `udacity submit` from the project folder in your terminal. (Typically that will be `.../artificial-intelligence/Projects/2_planning/ $`) The script will automatically create a zip archive of the required files (`my_planning_graph.py` and `report.pdf`) and submit your code to a remote server for testing.

You can only submit a zip archive created by the PA script (even if you're only submitting a partial solution), and you must submit the exact zip file created by the Project Assistant in your classroom for review. The classroom verifies the zip file submitted against records on the Project Assistant system; any changes in the file will cause your submission to be rejected. 

The detailed steps are shown in the following figure
![steps of project submission](https://github.com/mohandesosama/Building-a-Forward-Planning-Agent/blob/master/images/submission%20steps.png)

### Additional Search Topics

- Regression search with GraphPlan (ref. [GraphPlan](https://github.com/aimacode/aima-pseudocode/blob/master/md/GraphPlan.md) in the AIMA pseudocode). Regression search can be very fast in some problem domains, but progression search has been more popular in recent years because it is more easily extended to real-world problems, for example to support resource constraints (like planning for battery recharging in mobile robots).

- Progression search with Monte Carlo Tree Search (e.g., ["Using Monte Carlo Tree Search to Solve Planning Problems in Transportation Domains"](https://link.springer.com/chapter/10.1007%2F978-3-642-45111-9_38))
