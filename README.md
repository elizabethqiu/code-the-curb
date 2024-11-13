# parking

- Resource: https://www.arlingtonva.us/files/sharedassets/public/v/1/transportation/documents/ppp/qa-summary_10232024.pdf
    - http://bit.ly/code-the-curb
    - Goals of the County: https://www.arlingtonva.us/Government/Programs/Transportation/Parking/Performance-Parking-Pilot/Performance-Parking-Frequently-Asked-Questions
    - FAQs for project: https://www.arlingtonva.us/files/sharedassets/public/v/1/transportation/documents/ppp/qa-summary_10232024.pdf
- API Access: https://api.exactpark.com/arlington
    - Price data: County's GIS Open Data Portal, real-time ExactPark API

- Data I found to maybe use, ranked (CSV for Python processing, or GeoJSON):
    - [Parking Meters Rate History](https://gisdata-arlgis.opendata.arcgis.com/datasets/9bbfca97a814415db1b5e50695a2712c_2/explore)
    - [Ortho 2021 Arlington - most recent]() - "orthophotography" - accurate pixels (today I learned!)
    - [Parking Meter Points - Viz to Map](https://gisdata-arlgis.opendata.arcgis.com/maps/ac5ab5a45b274e4798943e167afeb0f5/about)

- [Open Data](https://data.arlingtonva.us/)
- [PowerBI thing 1](https://app.powerbi.com/view?r=eyJrIjoiOGQwZmIwMzktYzE1MS00NWVjLTgwOWEtMTcxZDkwMzM4ODY1IiwidCI6IjgwMzU0ODA0LTFmZGYtNDI4ZS05ZjVmLTUwOTFlOTk0Y2Y1NCIsImMiOjF9), [thing 2](https://app.powerbi.com/view?r=eyJrIjoiMDc3YmRlODktNDQ1NC00Njg1LTg0NzUtYzIzZDY4NmFmNjhkIiwidCI6IjgwMzU0ODA0LTFmZGYtNDI4ZS05ZjVmLTUwOTFlOTk0Y2Y1NCIsImMiOjF9)
- [Parking Meters 2](https://experience.arcgis.com/experience/ee33d45e0d3848c8b99cfe51c00d4fca/page/Parking-Meters/)
- [Arlington 2](https://arlington.curbiq.io/public-default/)
- consumer side: https://eleven-x.com/exactnav/ & https://parkmobile.io/
- [On Policy](https://www.arlingtonva.us/Government/Projects/Planning/Smart-Growth/)

# NOTES

how would i go about this project? i have open data access: Price data is available - and all of these data are available through the project's API, and real-time parking occupancy data from close to 4,500 metered parking spaces in the commercial corridors. this is solely occupancy data on whether a parking space is occupied or not.

i want to first get real-time data. from there, i would likely want to analyze trends (if there is a history of parking available) for historical popular trends. then i want to access and calculate prices and obviously make prices lower for places that are less occupied / aiming to drive less traffic, and charging more for popular/congested places. the goal is optimization while also being able to make some profit.

other constraints: price, time limits, and hours of operation, permit parking, etc etc (control for now: price)

(if i have time i would increase the window of the parking trends by month/season/etc but for now let's stick to data from the past 30 days. also a takeaway is that this can impact human behavior (money talks). i can take a bridge anecdote from my hometown in potomac -- widening the bridge would just lead to more congestion. another example: amazon pricing on colors based on the shopper / their preferences. classpass does this with popular classes a user books) also lol [Efficient Market Hypothesis](https://en.wikipedia.org/wiki/Efficient-market_hypothesis) on inspo: ticketmaster (concert tix), "options" trading parking spaces. But also govt law: (quasi) policy - pass a law you can't resell parking spaces in public spaces

fixed supply -- unless you buy more land or build more parking spaces vertically (like housing crisis...)

1. ✅ python requests library, GET from API
2. ⭐ Database or Data Storage: Store data systematically to capture trends over time.
For real-time data, consider a time-series database (e.g., InfluxDB) or a relational database (e.g., PostgreSQL) to handle continuous updates efficiently.
I could really just do SQL it's not that deep
Automated Data Collection: script to automate data pulls
3. python matplotlib/etc: EDA for past 30 days trend
Trend Identification: Analyze historical occupancy data (e.g., past 30 days) to identify peak and off-peak times by:
Calculating average occupancy rates for different times (hourly, daily, weekly).
Examining variance in occupancy by location.
Pattern Detection: Check for any observable patterns, such as recurring congestion at specific times or during particular events.
Pricing Analysis: Explore historical pricing data to understand existing price fluctuation and identify if current pricing matches occupancy rates or if adjustments are needed.