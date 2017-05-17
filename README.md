# Splunk Custom Search Command Example

This repo contains an example of how to make a custom search command for Splunk. This includes a base class that makes it super easy to create one.

Here is how you make one:

## Step 1: Copy search_command.py

Copy the file search_command.py into the bin directory of your app. search_command.py is available within this repository under the path "/src/bin/search_command_example_app/search_command.py.

When you are done copying it, your app should have a file with this path:

    bin/search_command.py

## Step 2: Create your custom search command

In the steps below you will create the Python class that contains the code of your custom search command.

### 2.1: Create the custom search command file

Create the Python file that will contain your custom search command. We are going to make a simple search command that just echoes something back, so it will be named "echo.py". This would be in the file:

    bin/echo.py

### 2.2: Import the search command base class

Modify your search command to import the search command base class and sys:

    from search_command import SearchCommand
    import sys


### 2.3: Create your search command class

Create an new class that inherits from the SearchCommand class and calls the constructor from the super-class. Note that I have named the class "Echo":

    class Echo(SearchCommand):

        def __init__(self):
             
             # Initialize the class
            SearchCommand.__init__(self, run_in_preview=True, logger_name='echo_search_command')

        def handle_results(self, results, session_key, in_preview):
            pass

### 2.4: Modify the constructor to take the search command arguments

Modify the constructor to take whatever arguments you want it to take. In this case, I want the search command to take an argument "what_to_echo"; the constructor now takes the argument and stores it:

    from search_command_example_app.search_command import SearchCommand
    import sys

    class Echo(SearchCommand):

        def __init__(self, what_to_echo="Hello World"):

            # Save the parameters
            self.what_to_echo = what_to_echo

             # Initialize the class
            SearchCommand.__init__(self, run_in_preview=True, logger_name='echo_search_command')

        def handle_results(self, results, session_key, in_preview):
            pass

### 2.5: Implement handle_results()

Implement handle_results() to do whatever your search command is supposed to do. In this, mine will just output the contents of the "what_to_echo" argument.


    from search_command import SearchCommand
    import sys

    class Echo(SearchCommand):

        def __init__(self, what_to_echo="Hello World"):

            # Save the parameters
            self.what_to_echo = what_to_echo

             # Initialize the class
            SearchCommand.__init__(self, run_in_preview=True, logger_name='echo_search_command')

        def handle_results(self, results, session_key, in_preview):
            self.output_results([{'echo' : self.what_to_echo}])

### 2.5: Add the code to execute the search command

Finally, add the code to cause the search command to execute at the bottom of the file:
            
    from search_command import SearchCommand
    import sys

    class Echo(SearchCommand):

        def __init__(self, what_to_echo="Hello World"):

            # Save the parameters
            self.what_to_echo = what_to_echo

             # Initialize the class
            SearchCommand.__init__(self, run_in_preview=True, logger_name='echo_search_command')

        def handle_results(self, results, session_key, in_preview):
            self.output_results([{'echo' : self.what_to_echo}])

    if __name__ == '__main__':
        try:
            Echo.execute()
            sys.exit(0)
        except Exception as e:
            print e


## Step 3: Register your custom search command in commands.conf

Finally, register your search command by adding it to commands.conf. Create the file "default/commands.conf" in your app. The stanza name should match the name of the command as it will appear in Splunk; "filename" must match the filename of the search command in the bin directory:

    [echo]
    filename = echo.py
    generating = true
    passauth = false

"generating" is set to true since this search command doesn't accept Splunk results but rather creates new results. "passauth" is set to false because this search command doesn't need to have access to splunkd.

## FAQs

### How do I consume search results in a search command?

You will need to do two things if you need your search command to process results within SPL.

One, update the command in commands.conf to set generating to false.

Second, you will need to update handle_results() to do something with the results which will be in the "results" argument. Here is an example that adds a new field 'source_length' with the length of the source field:

        def handle_results(self, results, session_key, in_preview):
            
            for result in results:
                if 'source' in result:
                    result['source_length'] = len(result['source'])
            
            self.output_results(results)
