from search_command_example_app.search_command import SearchCommand

class Echo(SearchCommand):
    
    def __init__(self, what_to_echo="Hello World"):
        
        # Save the parameters
        self.what_to_echo = what_to_echo
        
        # Initialize the class
        SearchCommand.__init__( self, run_in_preview=True, logger_name='echo_search_command')
    
    def handle_results(self, results, session_key, in_preview):
        self.output_results([{'echo' : self.what_to_echo}])
        
if __name__ == '__main__':
    Echo.execute()