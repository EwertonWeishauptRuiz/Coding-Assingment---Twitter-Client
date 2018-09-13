
# Cludo Assingment - Ewerton Weishaupt Ruiz

## Preface

This documents gives an overview of the codebase for this programming assingment. 
The purpose of this document is to give an understanding of the project structure and 
sequence of operations. 

## Overview
    User can search for tweets, making a search, and can filter through those results using the filter input field. 

    Every time a filter is done, a file is saved, with the filtering result with a JSON format to disk, inside the RESULTS folder, created by the appliaction in the root where the script is located. 

    User can make the search and use the submenu to save the file to disk. The file will be saved with the query input passed by the user. 
    
    Each file saved, if it alread exists with the same name, then the file will be created with an incremented number in the end to differentiate the files. 

    User can load the files through the submenu, which will be loaded to the screen, showing the contents of the JSON that file has.

## Structure

# 1. setupUI function that contains
    a. Instantiation code
    b. UI handling
# 2. set_text function that handles the UI results
    a. Appends to the UI the result of the tweets, interating through the index passed as a parameter.

# 3. perform_query function that handles the query
    a. Set up the API Keys
    b. Receives the query from the user input
    c. Saves the results to a Key-Value pair dictionary
    d. Passes the text to the UI

# 4. save_json_file function 
    a. Checks if the file already exists, and if so, increments the file name. 
    b. Saves the file to the disk, inside the results folder.

# 5. filter_text function called when filter button is pressed
    a. Receives the user input for filtering of the query tweets.
    b. Clears and add to the UI relevant twitters with a filtered header.
    c. Saves to a filteres_results array the results of the fiter.
    d. Saves to disk a file with the results of the filtering.

# 6. save_results function called when save buttons is pressed on the submenu
    a. Saves to disk the result of a query.    

# 7. load_results function called when load button is pressed on the submenu            
    a. Open a dialog box to select a file
    b. Load the file and loads the JSON response.
    c. Append the results to the UI.

# 8. retranslateUI
    a. Set the names for the UI elements. 

        


