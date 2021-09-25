# Football Manager - The Moneyball Strategy

This script lets you improve your scouting approach by using in-game-date, processing it via Python and give advices on which players in your scouting field are statistically the most valuable.

## Table of Contents
1. What is 'Moneyball'?
2. Why do we use the 'Moneyball' approach?
3. What are we doing in detail?
4. How are we doing it?
5. Possible Mistakes and Uncertainties
6. Upcoming features

## 1. What is 'Moneyball'?
The 'Moneyball' scouting approach was originally established in baseball sport in the late 1990s. 
The success of the Oakland Athletics made this approach popular in the sports field.
In recent times, football clubs adopted this approach and some even transformed their whole business and sports analytics sections (including scouting). 
Famous examples are newly promoted Premier League side Brentford and three-times Danish Champions FC Midtjylland.\
See more: https://www.si.com/soccer/2015/05/15/soccer-analytics-brentford-midtjylland-matthew-benham

### But what is the core message of the 'Moneyball' strategy?
Every decision you are making - in this case scouting and subsequently transfer decisions - should be driven by hard and rational facts, rather than emotional and irrational facts.
The best way to generate these hard facts is by evaluating all kinds of data and creating decision models based on your preferences. 
The goal is to always get the most effective outcome to get the biggest success.\
<br><br>
**To visualize it in the sense of football:**\
The former worldclass player, whose performances ceclined since three years but still has a good reputation and high market value is worse in terms of economical and sporty aspects than a player, who showed constantly good performances over the last three years but is somehow flying under the radar.\
The moneyball approach wants to bring these 'underdogs' together in your team to gain maximal success but at the same time use minimal ressources.

## 2. Why do we use the 'Moneyball' approach?
As a football and statistics enthusiast, the usage of statistical data in this fiels always fascinates me. 
With the very realistic simulation *Football Manager* you can take on the role to make these statistical decisions by yourself and see the long-term in no time. 
The game produces and provides a lot of fictional yet realistical data. 
Unfortunately there is no in-game tool to smoothly generate decision models through the data set but there is at least the option to export it on your local device. 
This is where Python with its powerful libraries comes into play and can I can get a first look on the practical usage of fundamental data science skills such as data wrangling, data manipulation and visualization.

## 3. What are we doing in detail?

### Data wrangling
The exported data is available as html file. 
The library *BeautifulSoup* is used to parse over the file to get the names of the columns and the specific value for each player.
The data gets stored in a *Pandas* dataframe. 
From here on we are able to clean up the table by eliminating unused columns and fields with empty values.

### Data manipulation
Now that we have a clean source of data, we are able to manipulate the data for our needs. 
As the in-game statistics are not stored in a similar manner, we have to transform them first through simple arithmetric functions.
In the we have three types of values:
- events with two possible outcomes (success of fail): e.g. tackles, passes
- success-fail-ratio of these events measured in per cent: e.g. aerial data with percentage
- standalone events: key passes, goals
These values whether they were considered necessary for the specific evaluation in the first playce define the final rating based on their given rating.

### Data visualization
The data visualization is the last step in which you can decide whether you want to get a graphical or non-graphical output for your final decision. 
In the rational sense of 'Moneyball' the best would be to get a list of one or more player (if you want to have back-ups available) ordered descending by their rating.
But sometimes it can be helpful to have a view on a few players and compare their performance in key values. Therefore we create a graph with subplots.
The choosen values get displayed and ordered based on their weighting.
The plot contains all necessary facts but is otherwise kept simple.

## 4. How are we doing it?
- Import the ***custom_view.fmf*** in the 'scouted' tab ingame.
- Make sure to set the right filters if you want to use them
- CTRL-A --> CTRL-P to mark all entries and export it as html
- install Python along with the libraries *Pandas*, *Numpy* and *Matplotlib* 
- go into the file ***settings.py*** 
  - define the name of your input file: e.g. 'scouting_file.html'
  - set the attributes you want to include to 'True'
  - set the weighting for each attribute
  - set the FILTER variable to how many players you want to get as output
  - define the type of output you want to get
    - 'plot' or 'table'

## 5. Possible Mistakes and Uncertainties
- only works for field players yet
- at some places it does not follow the 'Moneyball' principle
 - e.g. passing and distance covered are not considered relevant variables
- the data FM delivers is just for the current season
  - only analysis at the end of the season are recommended

## 6. Upcoming features
- [ ] add a GUI for even easier selecting and weighting
- [ ] add goalkeeper stats and rating mechanism
- [ ] overthink attributes
- [ ] add new attributes
- [ ] create a database to allow a yearly update and a better analysis
- [ ] bring in new factors such as
 - market value and salary (for potential bargain evaluation)
 - current team statistics, performance and playstyle
 - age
- [ ] new project approach
  - use ML to see how the in-game ratings are calculated




