''' ITERATION 1

Module: Elen Analytics - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Process:

We don't write code from top to bottom; instead, we often write it from the outside in.
Here's what a first draft of my utils_case.py might look like:

1. I start with this docstring at the very beginning.
   I use it to clarify the purpose of my Python file and organize my thoughts.
   
2. I'll declare a global variable for my byline string and just set it to some simple text.

3. I'll declare a main() function for my module. When I run this script, I can use main() to test my byline.

4. I'll add the boilerplate conditional execution code so I only run the main() function when 
   this script is executed directly (but not when I import it into another file).

I'll test it in an online interpreter to ensure this version runs correctly before continuing.
'''

#####################################
# Declare a global variable named byline.
#####################################

byline: str = 'Elen Analytics: Delivering Professional Insights'
def get_byline() -> str:
    return byline
#####################################
# Define a main() function for this module.
#####################################

# Create a function named main.
# A function is a block of code that performs a specific task.
# This function will simply print the byline to the console.
# Add a type hint to indicate that this function doesn't return anything when called 
# (that is, it has a Python type of None).
# It doesn't need any additional information passed in, 
# so there's nothing needed inside the parentheses.
# Everything afer the colon (:) must be indented (usually 4 spaces)

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main () when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
    
''' ITERATION 2 
Module: Elen Analytics: Delivering Professional Insights

This module provides a simple, reusable foundation for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.
Process:
Second iteration adds a function to return a string via byline.
I’ll create a function named get_byline().
It’ll return by line to whatever calls the get_byline() function.
I’ll update the main() function to use the new get_byline() function 

Same conditional boilerplate at the end.
I’ll test this version before adding more code that show:
-	My ability to declare variables of different types
-	My ability to use python to calculate basic descriptive statistics'''
#####################################
# Declare a global variable named byline.
#####################################

byline: str ='Elen Analytics: Delivering Professional Insights'

def get_byline() -> str:
    '''Return a byline for the project.'''
    return byline
    
#####################################
# Define a main () function for this module.
#####################################

# Main function calls get_byline() to retrieve the byline.
def main () -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main () when executing this module as a script.
#####################################

if __name__ == '__main__':
    main ()    
''' ITERATION 3
  Module: 'Elen Analytics: Delivering Professional Insights'
 
 This module proves a simple, reusable foundation for my analytics projects

Process:
Declare additional variables to show skills with different data types.
'''
#####################################
# Declare global variables - keep byline at the end
# We will use this information in a smarter byline
#####################################

# Boolean variable to indicate if the company has international clients
has_international_clients: bool = True

# Integer variable for the number of years in operation
years_in_operation: int = 10 
    
# List of strings representing the skills offered by the company
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]

# List of floats representing individual client satisfaction scores
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

#####################################
# Declare a global variable named byline
# Make it a multiline f-string to show our information
#####################################

byline: str = f"""

-----------------------------------------------------------
Elen Analytics: Delivering Professional Insights
----------------------------------------------------------

Has International Clients: {has_international_clients}
Years in Operation:        {years_in_operation}
Skills Offered:            {skills_offered }
Client Satisfaction Scores: {client_satisfaction_scores}
"""
#####################################
# Define the get_byline() function
#####################################  

def get_byline() -> str:
    '''Return a buline for my analytics projects.'''
    return byline
    
#########################################
# Define a main() function for this module.
#########################################

''' ITERATION 4
 
 Module:'Elen Analytics: Delivering Professional Insights'

Process:
In this fourth iteration, I introduce some basic stats using Python.
    - min () is a built in function to find the smallest value passed in 
    - max is a built in function to find the largegst value passed in
    - The statistics module offers methods to calculate mean and standard deviation
    '''
    
###########################
    # Import Modules at the Top
    ###########################
    
    # In Python, we can import modules to add extra tools and functions.
    # Below, we're importing:
    # - 'statistics: This gives us tools to calculate things like averages.
    # Use CTRL F and type statistics to see where it is used in the code.
    # Did you find statistics.mean()?
    # Did you find statistics.stdev() ?
    
import statistics
    
    ##########################
    # Declare global variables
    ###########################
    
    # Boolean variable to indicate if the company has international Clients
has_international_clients: bool = True
    
    # Integer variable for the number of years in Operation
years_in_operation: int = 10
    
    # Float variable for teh average client satisfaction Score
average_client_satisfaction: float = 4.7
    
    # List of strings representing the skills offered by the company
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]
    
    #List of floats representing individual client satisfaction scores
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]
  #####################################
    # Calculate Basic Statistics
    # Do this BEFORE we declare the byline
    # So the values have been calculated 
     # and are ready for use in the byline.
    #####################################  
   
    # Calculate basic stats using built-in functions min (), max() and statistics module functions mean () and stdev().
min_score: float = min(client_satisfaction_scores)
max_score: float = max(client_satisfaction_scores)
stdev_score: float = statistics.stdev(client_satisfaction_scores)
    
    #####################################
    # Declare a global variable named byline
    # Make it a multiline f-string to show our information
    #####################################
    
byline: str = f"""

-----------------------------------------------------------
Elen Analytics: Delivering Professional Insights
----------------------------------------------------------

Has International Clients: {has_international_clients}
Years in Operation:      {years_in_operation}
Skills Offered:           {skills_offered }
Client Satisfaction Scores: {client_satisfaction_scores}
"""
#####################################
# Define the get_byline() function
#####################################  

def get_byline() -> str:
    '''Return a buline for my analytics projects.'''
    return byline
#####################################
# Define a main () function for this module
#####################################  
def main () -> None:
    '''Print results of get_byline() when main() is called.'''
print(get_byline())

#########################################
# Conditional Execution
#########################################

if __name__ == '__main__':
    main()


def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())
''' ITERATION 5
   Module: Elen Analytics: Delivering Professional Insights
   This module uses a simple, reusable foundation for my analytics projects.
 '''
 
import statistics
 
has_international_clients: bool = True
years_in_operation: int = 10
average_client_satisfaction: float = 4.7
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]
temperature_values: list = [40.8, 37.6, 44.9, 25.0, 44.7]

#####################################
# Calculate Basic Statistics using built in functions.

#####################################

# Calculate basic stats using built-in functions min(), max(), and statistics module functions mean() and stdev().
min_score:  float = min(client_satisfaction_scores)
max_score:  float = max(client_satisfaction_scores)
mean_score:  float = statistics.mean(client_satisfaction_scores)
stdev_score:  float = statistics.stdev(client_satisfaction_scores)
min_temp:  float = min(temperature_values)
max_temp:  float = max(temperature_values)
mean_temp:  float = statistics.mean(temperature_values)
stdev_temp:  float = statistics.stdev(temperature_values)

byline: str = f"""
-------------------------------------------------------------
Elen Analytics: Delivering Professional Insights
-------------------------------------------------------------
Has International Clients:  {has_international_clients}
Years in Operation:  {years_in_operation}
Skills Offered:  {skills_offered}
Client Satisfaction Scores:  {client_satisfaction_scores}
Minimum Client Satisfacton Score:  {min_score}
Maximum Client Satisfaction Score:  {max_score}
Average Client Satisfaction Score:  {mean_score}
Standard Deviation of Client Satisfaction Scores:  {stdev_score:.2f}
Minimum Temperature (F):  {min_temp}
Maximum Temperature (F):  {max_temp}
Mean Temperature (F):  {mean_temp}
Standard Deviation of Temperature (F):  {stdev_temp}

"""

#####################################
# Define the get_byline() function.
#####################################

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

# The main() function now calls the get_byline function to retrieve the byline.

def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()

 ''' FINAL EXAMPLE
 Module: Elen Analytics: Delivering Professional Insights
 This module uses a simple, reusable foundation for my analytics projects.
 '''
 
import statistics
 
has_international_clients: bool = True
years_in_operation: int = 10
average_client_satisfaction: float = 4.7
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]

# Calculate basic statistics using built-in functions and the statistics module
min_score: float = min(client_satisfaction_scores)  
max_score: float = max(client_satisfaction_scores)  
mean_score: float = statistics.mean(client_satisfaction_scores)  
stdev_score: float = statistics.stdev(client_satisfaction_scores)

byline: str = f"""
---------------------------------------------------------
Elen Analytics: Delivering Professional Insights
---------------------------------------------------------
Has International Clients:  {has_international_clients}
Years in Operation:         {years_in_operation}
Skills Offered:             {skills_offered}
Client Satisfaction Scores: {client_satisfaction_scores}
Minimum Satisfaction Score: {min_score}
Maximum Satisfaction Score: {max_score}
Mean Satisfaction Score: {mean_score:.2f}
Standard Deviation of Satisfaction Scores: {stdev_score:.2f}
"""

def get_byline() -> str:
    '''Return a byline for my analytics projects.'''
    return byline

def main() -> None:
    '''Print results of get_byline() when main() is called.'''
    print(get_byline())

if __name__ == '__main__':
    main()
