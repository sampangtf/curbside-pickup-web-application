# NCR BSP API Challenge: One Go!

## Motivation
Our team attempts to explore innovative applications in a world that are significantly impacted by **COVID-19**. The food hospitality industry, which is traditionally dominated by dine-in services, witnesses an enormous increase in demands for contact-free services such as delivery and curbside pickup. While delivery is supported by a wide range of awesome apps such as DoorDash and UberEats, there haven't been a lot of applications that are specifically curtailed to **curbside pickup**, which offers a more flexible option of food at a much affordable cost. This shortage inspires our idea to use NCR BSP APIs to create a curbside pick-up optimization platform, as our project for the HackGT 8 challenge.

Here is a quick video demo of our website.
[![Watch the video](https://img.youtube.com/vi/9d7NmMlag4Q/maxresdefault.jpg)](https://youtu.be/9d7NmMlag4Q)

## Project Description
One day, you have an irrational thirst for sushi :sushi: and boba tea :bubble_tea:. However, you're not sure which sushi restaurant and which boba tea shop you should drop by so that you can achieve both of the following objectives in a **one single** pickup route with the shortest distance:car::
1. **Shortest route**
2. **Best food quality of both restaurants together**

This is precisely where our web application comes in. Our “bundling” option allows customers to order from multiple restaurants and pick up their orders in a single trip. Given a list of multiple keywords, we conduct **fuzzy search** on each one of them and create a set of combinations between each search. **_Each combination is treated as one item, and for each combination, our ranking algorithm computes a combined score from 1) the weighted average rating of all restaurants in this combination, and 2) the total distance of the shortest route that covers all restaurants in this combination._**

## User Guide
1. Create an account by typing personal information.

2. Enter keywords for multiple search (for example, "sushi" + "boba")

<img src="https://github.com/charlie-nik/hackgt/blob/main/images/start.png?raw=true" width=800>

3. Browse the ranked bundles of the restaurants from search results

<img src="https://github.com/charlie-nik/hackgt/blob/main/images/search.jpg?raw=true" width=800>

4. Choose the combination you prefer and place a bundling order on all restaurants in it

<img src="https://github.com/charlie-nik/hackgt/blob/main/images/order.png?raw=true" width=800>

5. Get out and get delicious :car:!

## NCR BSP APIs
* CDM API
* Site API (including Custom Attribute)
* Order API
* (Menu) (Desireable to be added in future extension, yet unavailable in this Challenge)

## Tools
* Backend: ```Python``` ```Flask```
* Frontend: ```JavaScript``` ```React``` ```HTML/CSS```
