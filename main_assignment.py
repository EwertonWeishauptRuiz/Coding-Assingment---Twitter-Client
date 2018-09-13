import sys
import os
import oauth2
import json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # UI Elements from PyQt
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1077, 649)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 1051, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.search_parameters = QtWidgets.QLineEdit(self.gridLayoutWidget)        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_parameters.sizePolicy().hasHeightForWidth())
        # Search Input
        self.search_parameters.setSizePolicy(sizePolicy)
        self.search_parameters.setMaximumSize(QtCore.QSize(900, 16777215))
        self.search_parameters.setObjectName("search_parameters")
        self.search_parameters.setText('Your search...')
        # Filter Button
        self.gridLayout.addWidget(self.search_parameters, 0, 0, 1, 1)
        self.filter_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.filter_button.setMaximumSize(QtCore.QSize(80, 16777215))
        self.filter_button.setObjectName("filter_button")
        self.filter_button.clicked.connect(self.filter_text)
        # Search Button
        self.gridLayout.addWidget(self.filter_button, 1, 1, 1, 1)
        self.search_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.search_button.setMaximumSize(QtCore.QSize(80, 16777215))
        self.search_button.setObjectName("search_button")
        self.search_button.clicked.connect(self.perform_query)

        self.gridLayout.addWidget(self.search_button, 0, 1, 1, 1)
        self.filter_parameters = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filter_parameters.sizePolicy().hasHeightForWidth())
        # Filter Input
        self.filter_parameters.setSizePolicy(sizePolicy)
        self.filter_parameters.setMaximumSize(QtCore.QSize(900, 16777215))
        self.filter_parameters.setObjectName("filter_parameters")
        self.filter_parameters.setText('Your filter...')
        # Scroll Area
        self.gridLayout.addWidget(self.filter_parameters, 1, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 90, 1051, 511))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1032, 613))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # Layout for text
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")       
        self.result_text_ui = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.result_text_ui.setObjectName("result_text_ui")
        self.gridLayout_2.addWidget(self.result_text_ui, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # Status Bar
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1077, 21))
        # Menu bar
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionSave")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menubar.addAction(self.menuFile.menuAction())
        # Action of the buttons Save and Load from the submenu
        self.actionSave.triggered.connect(self.save_results)
        self.actionLoad.triggered.connect(self.load_results)

        # Change names of the UI elements
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)        

        # Initiates an array called result_list
        self.results_list = []
        
        # If there is no folder called result, create one
        if not os.path.exists("Results"):
            os.makedirs("Results")

    # Function that sets the text to the UI
    def set_text(self, results, index):
        # Set the text to the UI. Sets the tweet user name to bold and blue, text body to black.
        self.result_text_ui.append("<p style=\" font-size:12pt; font-weight:600; color:#0000FF;\" >" + results[index]['Name'] + "</p>" + 
                                        "<p style=\" font-size:12pt; color:#000000;\" >" + results[index]['Tweet'] + "<br>" + "</p>")

    # Function that performs the Query to the Twitter API
    def perform_query(self):
        # Consumer Keys
        consumer_key = 'R5ggcjZMm6AF8oT6qpLZTpqS1'
        consumer_secret = 'VIEADbFib7LDbQtmg6Km78hjiafbxgsHrNKmWFStlaLR6gEz6t'
        # Token Keys
        token_key = '999628296932425728-C510cajlxBJKSFDYhCFrzKyot005eO9'
        token_secret = 'svl05ByLZ51kG4HzXdXjtuqrV87DWv13xJ5Xd22bu61kX'

        # Use the oauth2 library for authorization
        consumer = oauth2.Consumer(consumer_key, consumer_secret)
        token = oauth2.Token(token_key, token_secret)
        
        #User input
        self.query = self.search_parameters.text()

        # Add the Hashtag safe url
        hashtag_symbol = '%23'
        #Client puts together the cosumer and token info
        client = oauth2.Client(consumer, token)
        # Make the request
        request = client.request('https://api.twitter.com/1.1/search/tweets.json?q=' + hashtag_symbol + self.query + "&tweet_mode=extended")
        # Decode the Json result
        decode = request[1].decode()
        # Add the result to an Object
        jsonObject = json.loads(decode)     

        count = 0 
        # Clear the UI, if there is text there.     
        self.results_list.clear()

        # Check if there is any results from the query.
        if len(jsonObject['statuses']) == 0:
            # Set a text to let user know, there are no results for that query.
            self.result_text_ui.append('No results found with #' + self.query)
        else:
            # Interact through the results.
            for x in jsonObject['statuses']:    
                # Add to the Dictionary the results
                self.results_list.append({'Name': x['user']['screen_name'], 'Tweet': x['full_text']})            
                # Write to the UI the results.
                self.set_text(self.results_list, count)
                count += 1       
    
    # Function that save the results to a file
    def save_json_file(self, file_name, results):
        # Create a counter
        i = 0
        # Check if the path already exists
        while os.path.exists("Results/" + file_name + str(i)):
            # If the file already existis, increment the number of the file
            i += 1
        # Open the file with writting aturhorization
        file = open("Results/" + file_name + str(i), "w+")
        # Dumps the json text to the file
        file.write(json.dumps(results))
        # Closes the file with the changes
        file.close() 

    # Action called when the filter button is pressed
    def filter_text(self):
        # Get the text from the user input.
        self.user_filter = self.filter_parameters.text()        
        # Initializate an array for the filtered results
        self.filtered_results = []
        # Clear the UI Text
        self.result_text_ui.clear()
        # Set a header
        self.result_text_ui.append("<p style=\" font-size:14pt; font-weight:600; color:#00FF00;\" >" + "Filtered results:" + "<br>" + "</p>")
        # Interate through the results_list
        for i in range(len(self.results_list)):
            # Check if the user input is in any of the tweets. 
            # Passes both strings as lowercase.
            if self.user_filter.lower() in self.results_list[i]['Tweet'].lower(): 
                # Set the text of the UI
                self.set_text(self.results_list, i)                                               
                # Add the results to the filtered_results list
                self.filtered_results.append({'Name': self.results_list[i]['Name'], 'Tweet': self.results_list[i]['Tweet']})  
        
        # If there are itens in filtered_result    
        if(len(self.filtered_results) == 0):
            # Set UI Text to let user know there are no results with the filter
            self.result_text_ui.append("No record found with " + self.user_filter)      
        else:            
            # Saves the filter to a file in disk, with a JSON format
            self.save_json_file(self.user_filter, self.filtered_results)

    # Action called when the save button is pressed
    def save_results(self):
        # Check if there is any itens in the dictionary to save to a file
        if(len(self.results_list) != 0):
            # Saves the filter to a file in disk, with a JSON format
            self.save_json_file(self.query, self.results_list)            
    
    # Action called when the load button is pressed
    def load_results(self):
        # Opens the dialog box to choose a file to load.
        fileName, _ = QFileDialog.getOpenFileName(None,"QFileDialog.getOpenFileName()", "Results/","All Files (*)")        
        # Opens the file
        file = open(fileName)        
        # Loads the Json from the file
        jsonObject = json.load(file)
        # Clear the text 
        self.result_text_ui.clear()
        # Set a header
        self.result_text_ui.append("<p style=\" font-size:14pt; font-weight:600; color:#00FF00;\" >" + "Loaded results from file" + fileName + ":" + "<br>" + "</p>")
        # Interate and write to the UI the results.
        for tweets in range(len(jsonObject)):
            self.set_text(jsonObject, tweets)           

    # Function that gives the UI their text
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cludo assignment"))
        self.filter_button.setText(_translate("MainWindow", "Filter"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))

# Run the main body of the application
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())