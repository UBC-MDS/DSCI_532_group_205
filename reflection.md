# Reflection

We managed to accomplish our original goals for this app in that we answered our research questions and delivered an app to handle the usage scenario that we set out to achieve. We now reflect upon our completed work.

## Accomplishments

- Our UI, while not of professional quality, is pretty decent. The controls and charts are pretty self-explanatory. We ended up revising the charts a few times to remove redundant information.
- It is easy to use and very responsive.
- We found that the lower scatter plot turned out to be quite effective in interpreting ratings. Basically, the more to the upper-right a dot is, the better. This is intuitive.
- The app was successfully deployed on Heroku. It can now be used as an effective tool to select what movies to watch.

## Limitations

- The layout had to be made large enough to properly accommodate the charts. Depending on the user's screen size, some scrolling may be necessary in the vertical and/or horizontal directions.
- After the user adjust the filter controls, the bargraph shows the top 10 grossing films based on the chosen criteria. However, there is no way of seeing past the top 10. If the user has already seen these 10 movies, the only way to see more movies is to change the selection criteria.
- The dataset doesn't have detailed information about the movies which makes it limited in helping the user to choose a movie.
- Originally, we wanted to use a range slider for the year range but there were too many years to display so had to switch to dropdown boxes.
- Any set of criteria that results in no movies will result in blank charts with no appropriate message to the user.

## Issues

- When a single movie is selected from the bargraph, the other bars turn grey. It would have been nice to also fade out the colour (with an alpha value) so that it didn't remain so prominent. This also means that if you select a grey bar, it is hard to tell which movie is selected.
- We were not able to make good use of the white space around the lower scatterplot due to possible Altair limitations when vertically concatenating charts. The space is caused by the upper chart's movie text labels being so long.
- There was no apparent way to write Dash callback that could validate the year range and output change back to the same controls. This would form an input/output loop. This is a known limitation of Dash. This means that the user could select a _from_ year that is larger than the _to_ year.

## Possible Future Improvements

- UI refinements
- Year range validation
- User message when there are no charts to show (based on selected criteria)
- Allow user to see more than the top 10 movies for the selected criteria
- Allow user to select between US and worldwide gross movie income.

## TA Feedback

> - Ensure everyone is getting a chance to code and submit pull requests, and that work is being distributed equally.
> - Some commit messages are not informative enough, for example “updates”.
> - Moving forward, remember to communicate with your team by creating new Issues or using Github projects functionality.

- Work was equally distributed among all the team members. All got the chance to make pull requests with their part of the work. Also, team members were free to make changes to tasks assigned to other members also. It was a good teamwork. All members first focused on their assigned tasks and later contributed to other's work as well. So there are sufficient pull requests from all team members.

- A few commits in the beginning may have been less descriptive but all team members tried to make all commit messages meaningful by reflecting the changes in that particular commit.

- We primarily used Github issues as the mode of communication. Issues were created where feedbacks or suggestions were required from each team member.
