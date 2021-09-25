# Import the required modules.
from bs4 import BeautifulSoup
import pandas as pd
import settings as st

# First we parse over the html-file and append all values to lists.
def parse_html():

    # Open the exported html file from FM and decode it.
    with open(st.file, "rb") as fp:
        html = fp.read().decode("utf-8")
        soup = BeautifulSoup(html, features="lxml")

    # Parse the html-file with bs4 and find the column names as well as their belonging values.
    column_name = soup.find_all("th")
    column_value = soup.find_all("td")

    # Fill the player_stats list with the matching values in the html-document.
    player_stats = []
    for value in column_name:
        player_stats.append(value.get_text())

    # Same goes for the values of all player stats in the document.
    player_stats_values = []
    for value in column_value:
        player_stats_values.append(value.get_text())

    return player_stats, player_stats_values

# Now we've got all categories and their belonging values extracted from the html and stored in two lists
# In the next step we create a Pandas Dataframe and fill it with the extracted data
def create_raw_table():
    
    # Get the two lists which store the column names and values
    player_stats, player_stats_values = parse_html()
    
    # Create the dataframe
    raw_table = pd.DataFrame()
    
    # As the data in player_stats_values is stored one after another for each player, we have to create
    # a temporary list and dictionary. The temporary list is filled step by step with all values for ONE player
    # The temporary dict stores the column name as key and the belonging value as value.
    # Afterwards it gets appended to the dataframe before going on with the next player
    for i in range(1,len(player_stats_values),len(player_stats)):
        temporary_list = []
        temporary_dict = {}
        for j in range(1,len(player_stats)+1):
            temporary_list.append(player_stats_values[(i-1)+(j-1)])
        for value in player_stats:
             temporary_dict[value] = temporary_list[player_stats.index(value)]
        raw_table = raw_table.append(temporary_dict,ignore_index=True)

    # Drop unnecessary columns which get exported by default and set the name-column as index
    raw_table = raw_table.set_index("Name")
    raw_table = raw_table.drop(columns=["Rec","Inf"])

    # Finally return the raw_table for our next process step
    return raw_table

