
import time

import splunk.rest
import splunk.search

from search_command_example_app.search_command import SearchCommand

class RunSearch(SearchCommand):

    def __init__(self, search_name=None):

        # Save the parameters
        self.search_name = search_name

        # Initialize the class
        SearchCommand.__init__(self, run_in_preview=True, logger_name='runsearch_search_command')

    def handle_results(self, results, session_key, in_preview):

        # Dispatch the search
        job = splunk.search.dispatchSavedSearch(self.search_name, session_key)

        # Wait until the job is done
        while not job.isDone:
            time.sleep(1)

        # Get the results
        dataset = job.results

        # Prep the output
        events = []
        for event in dataset:
            events.append(event)

        # Output the results
        self.output_results(events)

if __name__ == '__main__':
    RunSearch.execute()
