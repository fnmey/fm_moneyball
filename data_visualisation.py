# Import required modules
import matplotlib.pyplot as plt

# Import the module
import data_manipulation as dm

# This function gets run, if the selected output type is "Plot".
# Unsurprisingly it visualizes our rating table via subplots.
def data_visualisation():
    
    # Import the rating table and the selected stats.
    rating_table, stats_selection = dm.data_manipulation()

    # Get the columns and drop the rating-column which will not be displayed in the plots
    rating_table_columns = [i for i in rating_table.columns]
    rating_table_columns.remove("rating")

    # Filter the table by rating and define the players names as selection
    selection = rating_table.index

    # In the final plot, we want to visualize the weightings of each category. Therefore the
    # alpha-value of the RGBA-color-code gets defined based on the weighting.
    # This basically means, that the graphs color is more saturated the higher the weighting is.

    # Create a color dictionary and color list as well as a weighting list:
    # Color dictionary:
    # This dictionary will contain all attributes as keys and the belonging weightings as values.
    color_dict = {}

    # Color list:
    # In the end this list consists of four numbers (RGBA),
    # that will later represent the color code for our plots.
    color_list = []

    # Weightings:
    # All set weightings get later stored here, to easily extract the maximum value.
    weightings = []

    # This for loop appends all weightings for selected values to find out the maximum value.
    # In the nested loop we will append these weightings to each value.
    for key,values in stats_selection.items():
        if values[0]:
            weightings.append(values[1])
            for i in values[2]:
                color_dict[i] = values[1]
    # Get the maximum weighting
    max_value = max(weightings)

    # This for loop iterates over the color_dict and appends the RGBA-code to our color_list
    # divide each value with max_value to get a number between 0 and 1
    for key,values in color_dict.items():
        color_list.append((0,0.49,0,values/max_value))

    # Define the figure, which contains all subplots
    fig, ax = plt.subplots(1,len(selection))
    fig.set_figwidth(22)
    fig.set_figheight(6)
    fig.set_dpi(80)

    # Define the colors and labels
    edgecolor = (0.6,0.6,0.6,1)
    y_ticks = [0,0.25,0.5,0.75,1]
    y_labels = ["0%","","50%","","100%"]

    # Define the font sizes
    titlesize = 18
    y_labelsize = 15
    x_labelsize = 10


    # This loop creates a subplot for with data from each selected value.
    for i in range(0,len(selection)):
        plt.rc('axes', titlesize=15)

        # Create a list to store the values represented on the y-axis
        # = attribute values from 0 - 1
        y_axis_value = []

        # Create a list to store all column names represented on the x-axis
        # = attribute names
        x_axis_columns = []

        # Iterate over the column list to store ...
        # ... the value for each column to our y_axis list
        # ... the column name to our x-axis list
        for column in rating_table_columns:
            y_axis_value.append(rating_table[column][i])
            x_axis_columns.append(column)

        # The if-clause defines, that the y-axis labeling only applies for the first plot.
        if i == 0:

            # The ticks on the axis should be on the outside.
            plt.tick_params(direction="out")

            # Define a subplot at the specified place.
            plt.subplot(1,len(selection),i+1)

            # Define a barplot with the above defined values. Color them with our predefined color.
            plt.bar(x_axis_columns,y_axis_value,color=color_list,edgecolor=edgecolor)

            # Define the title for each subplot. It consists of the name ('index') and
            # the overall rating in a new line
            plt.title(rating_table.index[i]+"\n"+str(round(rating_table["rating"][i],2))+"%",size=titlesize)

            # Define the values for the ticks on the y-axis
            plt.yticks(ticks=y_ticks,labels=y_labels,size=y_labelsize)

            # Define the values for the ticks on the x-axis
            plt.xticks(ticks=x_axis_columns,labels=x_axis_columns,size=x_labelsize)

            # Set the limit on the y-axis from 0 to 1, as all values are in this range.
            plt.ylim(0,1)
        else:
            plt.tick_params(direction="out")
            plt.subplot(1, len(selection), i + 1)
            plt.bar(x_axis_columns, y_axis_value, color=color_list, edgecolor=edgecolor)
            plt.title(rating_table.index[i] + "\n" + str(round(rating_table["rating"][i], 2)) + "%",size=titlesize)

            # The only line different from the ones in the if-clause:
            # Leave the y-ticks specification empty.
            plt.yticks([])
            plt.xticks(ticks=x_axis_columns, labels=x_axis_columns,size=x_labelsize)
            plt.ylim(0, 1)




    # In the end show the plots.
    plt.show()
