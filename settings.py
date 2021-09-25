# Import the data_manipulation and data_visualisation modules that run our program
import data_manipulation as dm
import data_visualisation as dv

# Set the file name. If the file is not in the working directory, you have to add the path as well
file = "scouting_file2.html"

# Set the filter variable. This defines, how many players you get as output.
FILTER = 3

# Decide whether you want to include the attribute and set the weighting for each attribute

# Define the weighting for the general attribute:
# - Distance Covered -
# As the general attributes get considered by default, there is no option to include it or not
general_weighting = 0.25

# Activate and define the weighting for the tackling attribute:
# - Tackles _
# - Key Tackles -
# - Fouls -
tackling_active = True
tackling_weighting = 2

# Activate and define the weighting for the aerial_duels attribute:
# - Headers -
# - Key Headers -
aerial_duels_active = False
aerial_duels_weighting = 1

# Activate and define the weighting for the passing attribute:
# - Passes
# - Key Passes
passing_active = False
passing_weighting = 0.5

# Activate and define the weighting for the crossing attribute:
# - Crosses
crossing_active = False
crossing_weighting = 0.25

# Activate and define the weighting for the chances attribute:
# - Chances Created
# - Assists
chances_active = False
chances_weighting = 0.25

# Activate and define the weighting for the shooting attribute:
# - Shots
# - Shots per Goal
shooting_active = True
shooting_weighting = 1

# Activate and define the weighting for the dribbling attribute:
# - Dribbles
dribbling_active = False
dribbling_weighting = 0.5

# Activate and define the weighting for the interceptions attribute:
# - Interceptions
interceptions_active = False
interceptions_weighting = 2

# Activate and define the weighting for the tackling attribute:
# - Defensive Mistakes leading to Goals
defensive_mistakes_active = True
defensive_mistakes_weighting = 0.25

# Set the output type. You may decide between a plot ("Plot") and an excel output ("Table")
output_type = "Plot"


# Run the program based on the set output type
if __name__ == "__main__":
    if output_type == "Table":
        dm.export_excel()
    elif output_type == "Plot":
        dv.data_visualisation()
    else:
        print("False output type. Please select either 'Table' or 'Plot'")
