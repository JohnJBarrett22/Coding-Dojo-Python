# Amadon

## Topics
* Session and Post Handling
* Mixing post handling with html render - why this should be avoided
* Basic security - why you should be careful about what you put inside <form>tags

You've decided to build your own e-commerce site called Amadon as a Django app.  Have your app store, in the database, all the items customers have ordered.

Once your customer bought the item, say your customer reloaded the page.  Would your customer be happy if your app re-orders the same product and charges his/her credit card again?  Probably not!  Make sure your app doesn't charge the card again when the customer reloads the 'checkout' page ('checkout' page defined as localhost/amadon/checkout where they see a thank you message).

## Highlighting some lessons

IMPORTANT LESSON 1: A good developer should not have a method handle both the POST data and render HTML.  In fact, this is such a common mistake made by developers that we should always double-check that we haven't made this mistake ourselves. Instead, for example, have the http post request sent to '/amadon/buy'. Have this route handle the POST data then redirect to '/amadon/checkout' which displays the thank you html.  This way, even when the user reloads the thank you page, it will not re-process the submitted order.

For this assignment, include CSS. Either create your own CSS file or use a library, such as Twitter Bootstrap.

IMPORTANT LESSON 2: One reason we designed this assignment is for you to see how easy it is to manipulate the form.  For example, say that the form for ordering a Dojo T-shirt looked like this.

A somewhat sophisticated user could, for example, use Inspect Element to change the price to '0.01' and order lots of T-shirts for very cheap!  A better way to handle this would be to have, for example, product_id as a hidden variable.  This way, if they change the product_id using inspect element, they would just get a different item for their order.

In other words, have the form look more like below:

Surprisingly, a lot of e-commerce sites are built where you could easily change the price.  What if you built a web crawler/scraper to go through lots of e-commerce sites to specifically look for sites where price is part of the shopping cart form?  You could order lots of items for very cheap (although you'll probably get caught) or also reach out to them and tell them about the security flaw in their site.  Maybe they'll hire you to make their site more secure? :)
