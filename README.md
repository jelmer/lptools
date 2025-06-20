These are some tools for use with projects hosted on Launchpad.

* review-notifier <project1> [[project2] ...]

This tool will present notifications for changes to merge proposals on a
project. You currently must pass the list of projects on the command line.

* review-list <project1> [[project2] ...]

This tool will present a list of all the branches currently in the
Needs Review state. The list includes the branch name, and the votes
on the proposal. You can double-click on a row to open the merge proposal
page in your browser.


Both tools use launchpadlib, and refresh automatically every 5 minutes
as a hardcoded value. The former is not particularly useful with the new
review-list script, but I've included it here for completeness.


* milestone2ical <project>

This tool will convert all the milestones on a project or project group,
into an iCalendar 2.0 format file, for importing into a calendar program.

* recipe-status <person>

This tool will render a status table for all of the recipe builds owned
by the specified person.
