# Random Quote Generator
# -->Motive
The motive is to create Random Quotes using File Handling
# -->Statment and Modules
* Random module
* with statment
* readlines()
* strip()
 # -->Source code
  <img width="479" alt="code q" src="https://github.com/Shreegraphy/random-code-generator/assets/133193730/54b87058-addd-47c5-81aa-044e346c545a">

1. The random module is imported at the beginning of the script using the statement import random.
2. The function get_random_quote() is defined to get and print a random quote from the text file.
3. Inside the function, the with open('qoutes.txt', 'r') as file: statement opens the text file in read mode and assigns it to the variable file.
4. The method readlines() is called on the file object to read all the lines in the text file and store them in a list named quotes.
5. The random.choice() function from the random module is used to select a random element from the quotes list and assign it to the variable random_quote.
6. The strip() method is called on the random_quote string to remove any leading or trailing whitespace characters, and then it is printed using the print() function.
7. Finally, the function get_random_quote() is called at the end of the script to execute it and print a random quote from the text file.
#  --> OutPut
<img width="518" alt="op code q" src="https://github.com/Shreegraphy/random-code-generator/assets/133193730/1d346e70-03d5-407d-9b45-4193814b46fe">

# -->Button source code
<img width="497" alt="code q org" src="https://github.com/Shreegraphy/random-code-generator/assets/133193730/57cc2c87-c036-448b-97c0-9d5733515da0">

1. The random module and the Tkinter library are imported at the beginning of the script using the statements import random and from tkinter import *.
2. The function random_quote() is defined to get and print a random quote from the text file.
3. Inside the function, the with open('qoutes.txt', 'r') as file: statement opens the text file in read mode and assigns it to the variable file.
4. The method readlines() is called on the file object to read all the lines in the text file and store them in a list named q.
5. The random.choice() function from the random module is used to select a random element from the q list and assign it to the variable random_q.
6. The strip() method is called on the random_q string to remove any leading or trailing whitespace characters, and then it is printed using the print() function.
7. The Tk() class is used to create a new top-level window named root, and its size is set using the geometry() method.
8. A new button widget named btn is created using the Button() class, with its text set to 'Click me!', its border width set to '5', and its command set to call the random_quote() 
   function when clicked.
9. The button widget is added to the top-level window using the pack() method with its side set to 'top'.
10. Finally, the main event loop of the top-level window is started using the mainloop() method, which keeps the window open and responsive to user interactions until it is closed.
