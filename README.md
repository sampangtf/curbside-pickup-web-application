# NCR BSP API Challenge: One Go!

## Motivation
Our team attempts to explore innovation applications in a world that is significantly impacted by **COVID-19**. The food hospitality industry, which is traditioanlly dominated by dine-in services, witnesses an enormouse increase in demands of contact-free services such as delivery and curbside pickup. While delivery is supported by a wide range of awesome apps such as DoorDash and UberEats, there hasn't been a lot applications that are specifically curtailed to **curbside pickup**. This shortage inspires our idea to use NCR BSP APIs to create something as part of the HackGT 8 challenge.

## Project Description
One day, you have an irrational desire for sushi :sushi: and boba tea :bubble_tea:. However, you're not sure which sushi restaurant and which boba tea shop you should go to so that you can achieve both of the following objectives in a single pickup route :car::
1. **Shortest route**
2. **Best food quality of both restaurants together**

This is precisely where our web application comes in. Given a list of multiple keywords, we conduct **fuzzy search** on each one of them and create a set of combinations between each search. **_Each combination is treated as one item, and for each combination, our ranking algorithm computes a combined score from 1) the weighted average rating of all restaurants in this combination, and 2) the total distance of the shortest route that covers all restaurants in this combination._**

## Flow
1. Create account
2. Enter keywords for multiple search (for example, "sushi" + "boba")

<img src="https://github.com/charlie-nik/hackgt/blob/main/images/start.png?raw=true" width=800>

3. Browse the ranked combinations of the two sets of search results
4. Choose a combination and place an order on all restaurants in it

<img src="https://github.com/charlie-nik/hackgt/blob/main/images/order.png?raw=true" width=800>

5. Get out and get delicious :car:!

## BSP APIs
* CDM API
* Site API (including Custom Attribute)
* Order API

## Tools
* Backend: ```Python``` ```Flask```
* Frontend: ```JavaScript``` ```React``` ```HTML/CSS```
