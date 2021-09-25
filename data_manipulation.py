# Import the required modules
import pandas as pd
import numpy as np

# Import the created table
import data_wrangling as dw
import settings as st

# Define formulas for an easier use in the following.
# These formulas get used to make the stats comparable among each other in the following step

# Define a standardized score formula:
# This lets us distribute our values around the mean value
# 'Good values' get a high positive value, 'bad values' get a high negative value
# and 'average values' get a value around 0
def stand(a):
    try:
        return (a - np.mean(a)) / np.std(a)

    # The standard deviation may be 0, if all players got a '0' value in a category.
    # For this case we will return 1, which represents all players as equally good in this category.
    except ZeroDivisionError:
        return a + 1

# Define a normalized score formula:
# This lets us distribute our values between 0 and 1.
# 'Good values' get a value near 1, while 'bad values' get a value near 0.
def norm(a):
    try:
        return (a - np.min(a)) / (np.max(a) - np.min(a))  # formula to create a normalized score

    # The maximum and minimum values may be 0, if all players got a '0' value in a category.
    # For this case we will return 1, which represents all players as equally good in this category.
    except ZeroDivisionError:
        return a + 1

# Create a function which creates a rating (0-100%) for our defined stats and weightings
# value[0] = True/False
# value[1] = weighting
# value[2] = attributes
def create_rating(dict,table):

    # The summed weighted values of the each player: In the following every weighted value
    # of the current player gets added to this variable.
    summed_weighted_values_player= 0

    # The summed weighted values total: In the following every weighting gets added to this variable.
    summed_weighted_values_total= 0

    # Iterate over the input dictionary. If the category is 'actived' (==True) another iteration over
    # the attributes of each category follows. If this value is > 0 (saying this category is relevant)
    # the attribute value for each player gets multiplied with the weighting and divided by the amount of
    # attributes a category has.
    # At the same time the weightings get accumulated in a variable. In the end, the sum of each players values gets
    # divided by the total weightings value and multiplied with 100 to get the final rating.
    for key, value in dict.items():
        if value[0] == True:
            for attribute in value[2]:
                if value[1] > 0:
                    weighted_values_player = norm(table[attribute])*value[1]/len(value[2])
                    weighted_values_total = value[1]/len(value[2])
                    summed_weighted_values_player += weighted_values_player
                    summed_weighted_values_total += weighted_values_total
                else:
                    pass
    return summed_weighted_values_player/summed_weighted_values_total*100

# This step represents the transforming of the given attributes to the final rating attributes.
def data_manipulation():
    
    # Import the clean table and the selected stats
    clean_table, stats_selection = dw.data_wrangling()

    # create an empty dataframe, in which we will store our new values
    rating_table = pd.DataFrame()

    # The majority of the stats are defined as "... per 90 minutes" so we create
    # a games variable to use it as in the following steps.
    games = clean_table["Mins"]/90

    # In the following, we will create values for each category:
    # the standard and normalized scores are used as well as simple math operations.
    # By a simple if condition, we check, if the category is 'activated' and make the calculations
    # on these attributes afterwards.

    # We basically want to reward good performances over time:
    # Therefore we multiply some values with our games value

    # General value: distance covered
    if stats_selection["general"][0]:
        rating_table["dis"] = norm(clean_table["Distance"]/games)
        stats_selection["general"].append(["dis"])

    # Tackling values: tackles, key tackles and fouls
    if stats_selection["tackling"][0]:
        clean_table["tackles_q"] = stand(clean_table["Tck R"]/100)
        clean_table["tackles"] = norm(clean_table["Tck W"]/(clean_table["Tck R"]/100))
        rating_table["ta"] = norm(clean_table["tackles_q"]*clean_table["tackles"])
        rating_table["kta"] = norm(clean_table["K Tck"] / games)
        rating_table["fls"] = norm((clean_table["Fls"] / games)*-1)
        stats_selection["tackling"].append(["ta","kta","fls"])

    # Aerial duels values: headers and key headers
    if stats_selection["aerial_duels"][0]:
        clean_table["header_q"] = stand(clean_table["Hdrs W/90"]/clean_table["Aer A/90"])
        clean_table["headers"] = norm(clean_table["Aer A/90"]*games)
        rating_table["he"] = norm(clean_table["header_q"]*clean_table["headers"])
        rating_table["khe"] = norm(clean_table["K Hdrs"] / games)
        stats_selection["aerial_duels"].append(["he","khe"])

    # Passing values: passes and key passes
    if stats_selection["passing"][0]:
        clean_table["passes_q"] = stand(clean_table["Pas %"]/100)
        clean_table["passes"] = norm(clean_table["Pas A"])
        rating_table["pa"] = norm(clean_table["passes_q"]*clean_table["passes"])
        rating_table["kpa"] = norm(clean_table["K Pas"] / games)
        stats_selection["passing"].append(["pa","kpa"])

    # Crossing values: crosses
    if stats_selection["crossing"][0]:
        clean_table["crosses"] = norm(clean_table["Cr A"])
        clean_table["crosses_q"] = stand(clean_table["Cr C/A"]/100)
        rating_table["cro"] = norm(clean_table["crosses_q"]*clean_table["crosses"])
        stats_selection["crossing"].append(["cro"])

    # Chances values: chances created and assists
    if stats_selection["chances"][0]:
        rating_table["cha"] = norm(clean_table["Ch C/90"]*games)
        rating_table["ass"] = norm(clean_table["Ast"])
        stats_selection["chances"].append(["cha","ass"])

    # Shooting values: shots and shots per goal
    if stats_selection["shooting"][0]:
        clean_table["shots"] = norm(clean_table["Shots"])
        clean_table["shots_q"] = stand(clean_table["Shot %"])
        clean_table["goals"] = norm(clean_table["Gls"])
        rating_table["sho"] = norm(clean_table["shots_q"]*clean_table["shots"])
        rating_table["spg"] = norm(clean_table["goals"]/(clean_table["shots"]+0.01))
        stats_selection["shooting"].append(["sho","spg"])

    # Dribbling values: dribbles
    if stats_selection["dribbling"][0]:
        rating_table["dri"] = norm(clean_table["Drb"])
        stats_selection["dribbling"].append(["dri"])

    # Interceptions values: interceptions
    if stats_selection["interceptions"][0]:
        rating_table["int"] = norm(clean_table["Int/90"]*games)
        stats_selection["interceptions"].append(["int"])

    # Defensive mistakes values: defensive mistakes leading to goals
    if stats_selection["defensive_mistakes"][0]:
        rating_table["mis"] = norm(clean_table["Gl Mst"]*(-1))
        stats_selection["defensive_mistakes"].append(["mis"])

    # Apply the generated rating for every player to the rating column and sort it afterwards.
    rating_table["rating"] = create_rating(stats_selection,rating_table)
    rating_table = rating_table.sort_values(by="rating", ascending=False)

    # Filter the table by rating and return the table and once again the selected stats.
    rating_table = rating_table.astype(float).nlargest(st.FILTER,"rating")
    return rating_table, stats_selection

# If the output option "Table" is given, this function gets activated and exports the returned
# table to an excel file.
def export_excel():
    data_manipulation()[0].to_excel("output_table.xlsx")