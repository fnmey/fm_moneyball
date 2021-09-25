# Import the settings and parsing module
import parsing
import settings as st

# Import the regex library
import re

# In this step we want to clean up our raw table:
# - Drop unused columns
# - Eliminate empty values
# - Convert all entries to floats (to make calculations possible)
# In the first step we define, which columns we want to use (or want to drop respectively)
# Then we remove all lines with empty values (since these would impede the comparability between players)
# In the end, convert all values to floats by deleting the separator
def data_wrangling():
    raw_table = parsing.create_raw_table()



    # The categories and each belonging statistics get defined, so we just use relevant values in our table
    stats_categories = {"general" : ["Distance","Mins"],
                        "tackling" : ["Tck W","Tck R","K Tck","Fls"],
                        "aerial_duels" : ["Aer A/90","Hdrs W/90","K Hdrs"],
                        "passing" : ["K Pas","Pas A","Pas %"],
                        "crossing" : ["Cr A","Cr C/A"],
                        "chances" : ["Ch C/90","Ast"],
                        "shooting" : ["Shots","Shot %","Gls"],
                        "dribbling" : ["Drb"],
                        "interceptions" : ["Int/90"],
                        "defensive_mistakes": ["Gl Mst"]}


    # The 'active'-values and the weightings, we defined in the settings file are inserted into this dictionary
    stats_selection = {"general":[True,st.general_weighting],
                        "tackling":[st.tackling_active,st.tackling_weighting],
                        "aerial_duels":[st.aerial_duels_active,st.aerial_duels_weighting],
                        "passing":[st.passing_active,st.passing_weighting],
                        "crossing":[st.crossing_active,st.crossing_weighting],
                        "chances":[st.chances_active,st.chances_weighting],
                        "shooting":[st.shooting_active,st.shooting_weighting],
                        "dribbling":[st.dribbling_active,st.dribbling_weighting],
                        "interceptions":[st.interceptions_active,st.interceptions_weighting],
                        "defensive_mistakes":[st.defensive_mistakes_active,st.defensive_mistakes_weighting]}

    # We define a list that defines, which columns we will NOT drop in our table
    # by iterating over the stats_selection dictionary boolean value
    stats_selection_list = []
    for key,values in stats_selection.items():
        if values[0]:
            for i in stats_categories[key]:
                stats_selection_list.append(i)

    # Drop all columns that are not listed in our list
    for i in raw_table.columns:
        if i not in stats_selection_list:
            raw_table = raw_table.drop(columns=i)

    # Define the regex pattern to match all values starting with a decimal number
    # and may contain "." , "," or more numbers
    regex_pattern = re.compile(r"\d+[,.]*\d*")

    # Iterate over each column to clean up the Dataframe step by step
    for column_name in raw_table.columns:

        # Delete a row when there is an empty field in any column
        for k in raw_table[column_name].iteritems():
            raw_table = raw_table.drop(raw_table[raw_table[column_name] == "-"].index)

        # Iterate over every line in the specific column and search for the regex pattern
        # This eliminates the units such as 'km' and 'min'
        for j in range(len(raw_table[column_name])):
            clean_value = regex_pattern.search(raw_table[column_name].iloc[j])
            raw_table[column_name].iloc[j] = clean_value.group()

            # Eliminate the thousand-separator to be able to convert the string to float afterwards
            if "," in raw_table[column_name].iloc[j]:
                raw_table[column_name].iloc[j] = raw_table[column_name].iloc[j].replace(",","")
            else:
                pass

            # Convert all values to float if possible
            try:
                raw_table[column_name].iloc[j] = float(raw_table[column_name].iloc[j])
            except ValueError:
                pass

    # Return the cleaned-up table and the stats we selected
    return raw_table, stats_selection