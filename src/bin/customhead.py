from search_command_example_app.search_command import SearchCommand

class CustomHead(SearchCommand):
    
    def __init__(self, count=1):
        
        # Save the parameters
        self.count = int(count)
        
        # Initialize the class
        SearchCommand.__init__( self, run_in_preview=True, logger_name='customhead_search_command')
    
    def handle_results(self, results, session_key, in_preview):
        results_to_output = []

        # Cut the output to only the number we want to send
        results = results[:self.count]

        self.logger.info("%r", dir(results[0]))
        #for result in results:
        #    results_to_output
        self.output_results(results)
        
if __name__ == '__main__':
    CustomHead.execute()
