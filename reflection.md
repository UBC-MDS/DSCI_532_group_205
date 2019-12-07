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
  - To work around this issue for now, we do the validation in the filtering logic. If the start year is greater than the end year, we swap the values before performing the filter query.

## Possible Future Improvements

- UI refinements
- User message when there are no charts to show (based on selected criteria)
- Allow user to see more than the top 10 movies for the selected criteria
- Allow user to select between US and worldwide gross movie income.

## Peer Feedback

The peer review feedback sessions were very helpful as it gave us a chance to see how a typical user might use the app and determine some of the shortcomings of the app. The initial fly-on-the-wall period was particularly enlightening as it simulated what other users would experience, using the app for the first time without any guidance. Users were able to easily understand how the filters worked and quickly gravitated to the filters and started adjusting them. After making some selections, they then focused on the charts, as expected, and started trying to interpret the data. The chart tooltips were easily discoverable both in the upper and lower charts. However, it was not very evident that they could select individual bars so that they could zone in on a single movie.

Here are some points that were raised:

* some people may not be familiar with MPAA rating, it would be better to put a brief intro to explain what is meaning of this filter.
* some points on the second chart are covered by other points
* the tooltip in the second chart is helpful, but perhaps it does not need to be interactive/moving?
* Should look into removing Open and None Ratings because they gave back an empty graph
* Tool tip - show movie names for all points
* Choosing just Action as genre gives NA in titles in tooltip
* You should make selection area narrower, so plots could be bigger
* Graph is empty when nothing is selected. Maybe set it so selections can never be empty, or if they are empty, reset back to default
* Need to restrict that from year is less than or equal to to year in release year drop down

Based on the feedback, we decided to prioritize improvements based on trying to improve the user experience but also on difficulty level as well, given the limited time. These were the prioritized issues we attempted to tacle:

* MPAA ratings: More than one of our peer reviewers commented on MPAA ratings. One didn't know what all the codes meant, whereas another user discovered that some ratings led to no data. This seemed to be important to the user experience with a low difficulty level.
* Related to filtering was the year range selection and trying to prevent the user from selecting a start year that was greater than the end year. We discussed this during initial development and it also came up in the peer review. We decided to try to fix this even though we anticipated some difficulty based on Dash limitations.
* Before doing any work on the charts, we wanted to address the issue that the filters were taking up a lot of space and that if we made that column narrower, we'd have more room for the charts. We felt that we should get this issue out of the way before making chart adjustments.
* Our first chart improvement was to rethink how we used colours to convey the data. Should we really be using a different colour for each movie? What would happen if we displayed more than 10 movies? Can we convey the information with a single colour. This needed some prototyping and experimentation.
* Displaying a friendly user message when filter selection lead to no results. Though this was a nice-to-have, it didn't prevent the user from being able to use the app so didn't make it very high in the priority list. This also required HTML class attribute manipulation and was unsure if it would require JavaScript or if Dash could handle this. Some investigation would need to be done.
* Actual improvements to the charts themselves needed some deeper thinking. There were some users that wanted to be able to select the faded point on the scatterplot that represented all other movies. Later discussion with the TA revealed that we should think about removing them completely as there was too much overplotting. We will have greter discussions about this in the coming week so didn't think it would be wise to rush into making any major changes in this area for milestone 3.

## Summary of Changes for Milestone 3

* App Maintenance: moving app.py into src folder: We attempted to move the `app.py` file into the `src/` folder. However, this affected the way that functions were imported. Python expects imports to come from a module and files of a module must be in a separate folder. At this point, since we only have one `.py` file in the root of the project folder, we opted to leave as is for now as we rethink how we'd like to restucture the project in the future.
* MPAA ratings now have a legend. Open and None ratings were removed.

## Ongoing issues
* Year Selection: We attempted to work around year validation by swapping the variables when start year was greater than end year. This worked on a local instance but doesn't seem to be working on the deployed Heroku app. (Issue #33)
* Message when there is nothing to plot: we starting working on this issue but was not able to complete this for milestone 3. (Issue #40)
* We are still determining how to improve the charts

## TA Feedback

> commit frequently! It is best to commit smaller chunks of changes more frequently and design a PR that includes all smaller changes...

We have been working on committing more frequently with descriptive commits, where appropriate.

> OPTIONAL: in very big projects it is common to use tag words at the beginning of your commit message to indicate which part of the code was chaged, e.g. [DOC] for documentation, [BUG] for fixed bug or [ENH] for adding code or functionality.

We've been trying to tag our commits. This will take some getting used to but it's a start.
