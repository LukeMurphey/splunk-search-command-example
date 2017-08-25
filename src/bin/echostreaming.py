from search_command_example_app.search_command import SearchCommand
import time

class EchoStreaming(SearchCommand):
    
    def __init__(self, what_to_echo="Hello World", count=10):
        
        # Save the parameters
        self.what_to_echo = what_to_echo
        self.count = int(count)
        
        # Initialize the class
        SearchCommand.__init__( self, run_in_preview=True, logger_name='echo_streaming_search_command')
    
    def handle_results(self, results, session_key, in_preview):
        
        for i in range(0, self.count):
            time.sleep(1)

            self.output_results_streaming([{
                'echo' : self.what_to_echo,
                'number' : str(i)
            }])


if __name__ == '__main__':
    EchoStreaming.execute()
