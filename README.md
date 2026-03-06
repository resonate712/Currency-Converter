# Currency Converter
## Description:

Currency Converter is a program that is designed to make converting different currencies a breeze!  

The program operates entirely within the terminal.  After running the program the user is greeted and given a number of useful commands to retrieve the information that they the user wants.  The information that the program displays is pulled using an API from exchangerate-api.com.  The API is fast and responsive and returns information to the program quickly.

The several commands available to the user include list, convert, and rate.  List will provide to the user all of the currencies that are made available by the API. The current list is over 160 currencies. The convert command will allow the user to take two specific currencies and convert an amount between the two. The rate command will allow the user to get the most up-to-date conversion rate between 2 currencies. To quit the program simply enter the letter Q. 

In order to use the program effectively the user will need to create an exchange rate API account and receive their own key. Once the user has their own key they need to put it in the .env file for the program to work correctly.

The program folder includes a Pytest program that can be used to test the functions of the converter. Keep in mind that the values returned by the functions will change based upon the most current conversion rate. In order to have the Pytest return no errors you will need to update the check values to the most current conversion rates. The Pytest functions that check for invalid data however do not need to be updated. 

### Purpose:
Many people need to kept up to date to the current currency conversion rates. However for many people opening up an internet browser and typing in the current exchange is too tedious. Haven't we all wanted to look up conversion rates using a program directly installed on our computer? Of course! That's where this program comes in and shows the effectiveness and efficiency of a Python program using a quick and convenient API key to achieve better results in less time. Say goodbye to long arduous internet searches and say hello to quick Python based currency conversion. 

### Dependencies:
This program is compatible with Python running on Windows, Mac or Linux operating systems. The program was tested on Python 3.14.3.   The program needs several modules in order to be installed so that it can run correctly. These modules are listed in the requirements.txt file.

### License:
This program is free and requires no licensing because the API key will be procured by the user for personal or professional use. Please see exchange rate API.com for more details about their key usage.

### Installing:
Once the program has been downloaded it is fully ready to use after Python and the aforementioned modules are installed. Don’t forget your API key of course!

### Authors:
resonate712

### Version History:

- 1.0
    - Initial release