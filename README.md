# At Home in Oregon

At Home In Oregon is a data visualization tool designed to help social services and education professionals in the state of Oregon gain insight into trends in student and family homelessness. This web application provides users with an interactive map to view and compare Oregon Department of Education student homelessness statistics, offering an array of visualizations for each county that highlights local trends in the data. This focus on statistics at the local level provides users with valuable insight around an affordable housing crisis with often hyper-local nuances.

## The Tool

When the page loads, users are presented with a large display of a map of the state of Oregon and invited to click marker icons throughout the map to explore the data for each county. Below the map, four charts display selected views of the data to highlight different aspects of trends in the statistics.

# <img src="static/readme/landing_page.png">




A user can hover over an individual marker to see the name of the county the marker represents, and clicking the a marker opens an info window with a stacked bar chart dispalying K-12 student homelessness statistics for that county by year. Public school students who are homeless are classified in one of four ways, and the bars are stacked according to these classifications:

1. Living in a motel temporarily.
2. Sharing housing with another family or multiple families (commonly referred to as "doubled up").
3. Living in a family homeless shelter.
4. Unsheltered--living in a tent, vehicle, sleeping on the streets, or living in some other structure unsuitable for use as housing.

# <img src="static/readme/click-markers-interactively.gif">




If a user would like to further investigate trends in a particular county, they can click the link for detailed statistics in that county's info window to refresh the page with the four charts at the bottom of the page displaying data for that particular county, rather than at the statewide level:

# <img src="static/readme/county_details.gif">

## Tech Stack

At Home in Oregon was developed using a Python/Flask framework and a PostgreSQL database. The map was written in JavaScript using the Google Maps API and the markers were placed by using an AJAX request to the PostgreSQL database. The response object from the AJAX request contained latitude and longitude data for each county, and markers were placed by looping over this object and using the location data to create the markers.

The charts were created using Vega and Vega-lite and they were hosted independently in an Observable notebook. Charts were appended to the DOM using a JavaScript callback function that selects and appends the appropriate chart from the notebook at runtime. 

This independent hosting of charts essentially means that as the developer, I have the ability to change the display of charts within the Observable notebook and those changes will be live as soon as I publish the notebook and without touching the code in my repository in any way. While this feature doesn't necessarily bring much value to this particular project, it has interesting implications for data visualization work within larger organizations. I imagine a potential scenario where employee A is responsible for developing a range of visualizations that may be applicable to a host of projects within an organization and does so in a centralized way using an Observable notebook. If employee B would like to use one of the visualizations that employee A has developed in a project, all employee B would need is the public URL to the notebook containing the visualizations. Employee B could append any single chart (or multiple charts) from that notebook using the public URL, and if employee A subsequently makes adjustments to the chart employee B is using, those changes will be live immediately. Exploring this idea and the potential uses of Observable notebooks for data visualization was one of my favorite pieces of this project to work on.