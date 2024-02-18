# Manual Testing

 Manual testing is a crucial step I take to ensure the quality and functionality of my application. While automated testing is helpful, manual testing allows me to explore real-world scenarios and catch any issues that automated tests might overlook.

In this section, I'll show you how to set up your testing environment, execute tests, and document any issues you encounter. Whether you're a developer, tester, or end-user, this guide will help you understand how I ensure the reliability of my project through manual testing.


### Header Navigation Bar Display
- Ensure Correct Display and Functionality of Links and Elements


| TEST |  ACTION  | <center>EXPECT RESULT<center/> | <center>RESULT <center/>| <center>PASS / FAIL<center/>| 
|:-----|:--------:|----------:|----------:|----:|
| T01   | **Open the application in a web browser** |<center> The header navigation bar should display the application logo or title "DBZ EICHE" as the navbar brand</center>|<center>All elements of the header navigation bar are displayed correctly</center> | <center>PASS</center>|
| T02   |  **Navigate to a page where the header navigation bar is visible.**  | <center> The navigation menu should expand smoothly and display the expected links and buttons.</center>|<center>The logo or title "DBZ EICHE" is visible as the navbar brand</center>|<center>PASS</center>|
| T03   |  **If the user is not authenticated** | <center> "Sign in" and "Create account" links should be present.</center>|<center> Authentication-specific links "Sign in" and "Create account"are present and functional based on the user's authentication status. </center>|<center>PASS</center>|
| T04   |  **If the user is authenticated** | <center> "Dashboard" and "Logout"  links should be present.</center>|<center> Authentication-specific links "Dashboard" and "Logout"  are present and functional based on the user's authentication status. </center>|<center>PASS</center>|
| T05   |  **Click on the toggle button (navbar-toggler) to expand the navigation menu** | <center>The cart icon should be displayed </center>|<center>The cart icon is displayed, and cart-related information is visible upon interaction</center>|<center>PASS</center>|


###  Search Functionality 
- Validate Relevance of Search Results Based on User Input


| TEST |  ACTION  | <center>EXPECT RESULT<center/> | <center>RESULT <center/>| <center>PASS / FAIL<center/>| 
|:-----|:--------:|----------:|----------:|----:|
| T06   |  **Open the search page in a web browser** | <center>The search input field should be visible and accessible</center>|<center>As expected</center>|<center>PASS</center>|
| T07   |  **Inspect the search input field visually to ensure it is displayed correctly** | <center>Upon entering a search term and submitting the query, the search results should be relevant to the input provided</center>|<center> As expected </center>|<center>PASS</center>|
| T08   |  **Enter a search term (e.g., a product name or keyword) into the search input field** | <center>Upon entering a search term and submitting the query, the search results should be relevant to the input provided</center>|<center>As expected </center>|<center>PASS</center>|
| T09   |  **Submit the search query by pressing the Enter key or clicking on the search button** | <center>If no matching products are found, a message indicating "No products found" or similar should be displayed</center>|<center>As expected </center>|<center>PASS</center>|
| T10   |  **Review the search results displayed on the page** | <center>The search results should be displayed in a clear and organized manner, allowing users to easily identify relevant products</center>|<center> As expected </center>|<center>PASS</center>|




### Categories Navigation Display
- Confirm Correct Rendering and Functionality of Links and Dropdown Menus


| TEST |  ACTION  | <center>EXPECT RESULT<center/> | <center>RESULT <center/>| <center>PASS / FAIL<center/>| 
|:-----|:--------:|----------:|----------:|----:|
| T11   |  **Open the page where the categories navigation section is located in a web browser** | <center>The categories navigation section should be displayed correctly with all elements visible and accessible</center>|<center> As expected </center>|<center> PASS</center>|
| T12   |  **Check that the "All categories" link is displayed and clickable, leading to the main page** | <center>Clicking on the "All categories" link should redirect to the main page</center>|<center> As expected </center>|<center> PASS</center>|
| T13   |  **Check that the "Men's" dropdown menu is displayed and clickable** | <center>The "Men's" dropdown menu should expand to display relevant categories for men's products</center>|<center> As expected </center>|<center> PASS</center>|
| T14   |  **Check that the "Women's" dropdown menu is displayed and clickable** | <center>The "Women's" dropdown menu should expand to display relevant categories for women's products</center>|<center> As expected </center>|<center> PASS</center>|


### Main Page Display and Interaction
- Validate Product Details and Functionality of Interactive Elements


| TEST |  ACTION  | <center>EXPECT RESULT<center/> | <center>RESULT <center/>| <center>PASS / FAIL<center/>| 
|:-----|:--------:|----------:|----------:|----:|
| T15   |  **Check that each product displayed includes: Image,Name, Price, Season.** | <center>The main page displays products correctly with their respective details: image, name, price, and season.</center>|<center> As expected </center>|<center> PASS</center>|
| T16   |  **Click on the "Add to Cart" button of any product and verify that it updates the cart icon or quantity.** | <center>Clicking on the "Add to Cart" button of a product successfully updates the cart icon or quantity</center>|<center> As expected </center>|<center> PASS</center>|
| T17   |  **Click on the "View" button of any product and verify that it redirects to the product details page** | <center>Clicking on the "View" button of a product successfully redirects to the product details page</center>|<center> As expected </center>|<center> PASS</center>|
| T18  |  **Verify that the pagination controls are displayed correctly** | <center>If pagination is present, the pagination controls work as expected, allowing users to navigate through multiple pages of products</center>|<center> As expected </center>|<center> PASS</center>|


## Product Display and Interaction
- Product details are displayed correctly and interactable elements function as expected

| TEST |  ACTION  | <center>EXPECT RESULT<center/> | <center>RESULT <center/>| <center>PASS / FAIL<center/>| 
|:-----|:--------:|----------:|----------:|----:|
| T19  |  **Inspect the page visually to ensure the product image is displayed with high quality and is responsive** | <center>The product image is displayed with high quality and is responsive, adapting to different screen sizes.</center>|<center> As expected </center>|<center> PASS</center>|
| T20  |  **Check that the product name, price, color, and description are all displayed correctly and accurately** | <center>The product name, price, color, and description are all accurately displayed</center>|<center> As expected </center>|<center> PASS</center>|
| T21  |  **Verify that the "Add to Cart" button is present and clickable** | <center>The "Add to Cart" button is present and clickable</center>|<center> As expected </center>|<center> PASS</center>|
| T22  |  **Click on the "Add to Cart" button** | <center>Clicking on the "Add to Cart" button successfully adds the product to the cart</center>|<center> As expected </center>|<center> PASS</center>|
| T23  |  **Verify that the product is successfully added to the cart** | <center>The product is added to the cart without any errors or issues</center>|<center> As expected </center>|<center> PASS</center>|
| T24  |  **Ensure that the product is already added to the cart** | <center>The "Add to Cart" button should display "Added" if the product is already in the cart.</center>|<center> As expected </center>|<center> PASS</center>|


## Review Display and Interaction
- Verify the behavior of the review section for authenticated users.

- If the user is authenticated

| TEST |  ACTION  | <center>EXPECT RESULT<center/> | <center>RESULT <center/>| <center>PASS / FAIL<center/>| 
|:-----|:--------:|----------:|----------:|----:|
| T25  |  **Verify that the review section is displayed only if the user is authenticated** | <center>The review section should only be displayed if the user is authenticated</center>|<center> As expected </center>|<center> PASS</center>|
| T26  |  **submitting a review form** | <center>Reviews should display the username, date, and buttons to update and delete</center>|<center> As expected </center>|<center> PASS</center>|
| T27  |  **Click on the "update" button of a review** | <center>Clicking on the "update" button should redirect to a page to update the review</center>|<center> As expected </center>|<center> PASS</center>|
| T28  |  **Click on the "delete" button of a review** | <center>Clicking on the "delete" button should prompt for confirmation to delete the review</center>|<center> As expected </center>|<center> PASS</center>|
| T29  |  **Confirm deletion** | <center>Confirming deletion should remove the review from the review section</center>|<center> As expected </center>|<center> PASS</center>|


- If the user is authenticated

| TEST |  ACTION  | <center>EXPECT RESULT<center/> | <center>RESULT <center/>| <center>PASS / FAIL<center/>| 
|:-----|:--------:|----------:|----------:|----:|
| T30  |  **If the user is not authenticated** | <center>Verify that a message "You must be logged in to post a review. Click here to login" is displayed</center>|<center> As expected </center>|<center> PASS</center>|


## Cart
- cart page displays correctly with the appropriate items, quantity, and price details.

| TEST |  ACTION  | <center>EXPECT RESULT<center/> | <center>RESULT <center/>| <center>PASS / FAIL<center/>| 
|:-----|:--------:|----------:|----------:|----:|
| T31  |  **Verify that the cart page displays correctly** | <center>The cart page displays correctly with appropriate items, quantity, and price details</center>|<center> As expected </center>|<center> PASS</center>|
| T32  |  **Verify that each item in the cart is displayed with its details (name, image, price, quantity)** | <center>each item should be displayed with its details and total price calculated correctly.</center>|<center> As expected </center>|<center> PASS</center>|
| T33  |  **Verify that the "increment" button increases the quantity of the item by one and updates the subtotal accordingly** | <center>The "increment" button should increase the quantity of the item by one and update the subtotal accordingly</center>|<center> As expected </center>|<center> PASS</center>|
| T35  |  **Verify that the "decrement" button decreases the quantity of the item by one and updates the subtotal accordingly** | <center>The "decrement" button should decrease the quantity of the item by one and update the subtotal accordingly</center>|<center> As expected </center>|<center> PASS</center>|
| T36  |  **If the quantity of the item is decremented to 0** | <center>If the quantity of the item is decremented to 0, the item should be removed from the cart and the subtotal should be updated accordingly</center>|<center> As expected </center>|<center> PASS</center>|
| T37  |  **Verify that the "remove" button removes the item from the cart and updates the subtotal accordingly** | <center>The "remove" button should remove the item from the cart and update the subtotal accordingly</center>|<center> As expected </center>|<center> PASS</center>|
| T38  |  **Verify that the total price of the cart is updated after each action** | <center>The total price of the cart should be updated after each action</center>|<center> As expected </center>|<center> PASS</center>|
| T39  |  **Verify that a summary section is displayed** | <center>The summary section should include buttons to continue shopping and proceed to checkout, and the total price of the cart should be displayed accurately </center>|<center> As expected </center>|<center> PASS</center>
| T40  |  **Click on the "Checkout" button.** | <center>After clicking on the "Checkout" button, the user should be redirected to the checkout page</center>|<center> As expected </center>|<center> PASS</center>


##  Secure Checkout Process for Customer Orders
- Payment and Delivery Information Collection


| TEST |  ACTION  | <center>EXPECT RESULT<center/> | <center>RESULT <center/>| <center>PASS / FAIL<center/>| 
|:-----|:--------:|----------:|----------:|----:|
| T41  |  **Check if the shipping information fields (First Name, Last Name, Address, Zip Code, City) are displayed correctly** | <center>Each field (First Name, Last Name, Address, Zip Code, City) should be visible and labeled appropriately </center>|<center> As expected </center>|<center> PASS</center>|
| T42  |  **Verify that the email field is displayed and pre-filled with the user's email if available.** | <center>If the user is logged in and has provided their email, the field should be pre-filled with their email address.</center>|<center> As expected </center>|<center> PASS</center>|
| T43  |  **Verify that the summary section displays the total cost of items in the cart** | <center>The total cost of items in the cart should be displayed prominently in the summary section </center>|<center> As expected </center>|<center> PASS</center>|
| T44  |  **Click the "Confirm Checkout" button without filling in any required fields** | <center>Error messages should be displayed next to each required field that is left empty</center>|<center> As expected </center>|<center> PASS</center>|
| T45  |  **Click the "Confirm Checkout" button** | <center>The user should be redirected to the Stripe checkout page to complete the payment process</center>|<center> As expected </center>|<center> PASS</center>|
| T46  |  **Upon successful payment** | <center>The user should be redirected to a success page indicating that the payment was successful</center>|<center> As expected </center>|<center> PASS</center>|


## Dashboard Functionality
- Verify profile display, editing, and order history presentation.

| TEST |  ACTION  | <center>EXPECT RESULT<center/> | <center>RESULT <center/>| <center>PASS / FAIL<center/>| 
|:-----|:--------:|----------:|----------:|----:|
| T47  |  **Navigate to the dashboard page** | <center>User profile (name, username, email) displayed</center>|<center> As expected </center>|<center> PASS</center>|
| T48  |  **Click on the "Edit My Profile" button** | <center>User is redirected to the edit profile page for modifications</center>|<center> As expected </center>|<center> PASS</center>|
| T49  |  **If orders exist** | <center>Each order displays ID, items, quantity, date, total. </center>|<center> As expected </center>|<center> PASS</center>|
| T50  |  **If no orders** | <center>Order history is empty" message</center>|<center> As expected </center>|<center> PASS</center>|
| T51  |  **If no orders** | <center>Shopping" button to return to main page</center>|<center> As expected </center>|<center> PASS</center>|
| T52  |  **Navigate to the edit account page by clicking on the "Edit My Profile" button on the dashboard page** | <center>The page should display a form titled "Edit account"</center>|<center> As expected </center>|<center> PASS</center>|
| T52.1|  **""** | <center> Input fields for first name, last name, username, and email should be present and pre-filled with the user's current information</center>|<center> As expected </center>|<center> PASS</center>|
| T52.2|  **""** | <center>The Submit button should be visible</center>|<center> As expected </center>|<center> PASS</center>|
| T52.3|  **""** | <center>Upon submitting the form with updated information, the user's account details should be successfully updated in the system.</center>|<center> As expected </center>|<center> PASS</center>|
| T52.4|  **""** | <center>After successful submission, the user should be redirected to the dashboard page with a success message indicating the update was successful.</center>|<center> As expected </center>|<center> PASS</center>|


## Authentication
- To verify the functionality and security of the authentication features including signup, signin, signout, and password reset.

- Sign up

| TEST |  ACTION  | <center>EXPECT RESULT<center/> | <center>RESULT <center/>| <center>PASS / FAIL<center/>| 
|:-----|:--------:|----------:|----------:|----:|
| T53  |  **Verify successful signup with valid credentials** | <center>Enter a valid email address</center>|<center> As expected </center>|<center> PASS</center>|
| T53.1|  **""** | <center>Re-enter the email address to confirm</center>|<center> As expected </center>|<center> PASS</center>|
| T53.2|  **""** | <center>Enter a unique username.</center>|<center> As expected </center>|<center> PASS</center>|
| T53.3|  **""** | <center>Enter a strong password</center>|<center> As expected </center>|<center> PASS</center>|
| T53.4|  **""** | <center>Re-enter the password to confirm</center>|<center> As expected </center>|<center> PASS</center>|
| T53.5|  **""** | <center>Click on the "Sign Up" button</center>|<center> As expected </center>|<center> PASS</center>|
| T53.6|  **""** | <center>Ensure the user is redirected to a page confirming that an email for confirmation has been sent</center>|<center> As expected </center>|<center> PASS</center>|


| TEST |  ACTION  | <center>EXPECT RESULT<center/> | <center>RESULT <center/>| <center>PASS / FAIL<center/>| 
|:-----|:--------:|----------:|----------:|----:|
| T54  |  **Verify unsuccessful signup with invalid credentials:** | <center>Enter an invalid email address format</center>|<center> As expected </center>|<center> PASS</center>|
| T54.1|  **""** | <center>Re-enter the email address to confirm</center>|<center> As expected </center>|<center> PASS</center>|
| T54.2|  **""** | <center>Enter a username that already exists</center>|<center> As expected </center>|<center> PASS</center>|
| T54.3|  **""** | <center>Enter a weak password</center>|<center> As expected </center>|<center> PASS</center>|
| T54.4|  **""** | <center>Re-enter the password to confirm</center>|<center> As expected </center>|<center> PASS</center>|
| T54.5|  **""** | <center>Click on the "Sign Up" button</center>|<center> As expected </center>|<center> PASS</center>|
| T54.6|  **""** | <center>Verify appropriate error messages are displayed for each invalid input</center>|<center> As expected </center>|<center> PASS</center>|


- Sign in

| TEST |  ACTION  | <center>EXPECT RESULT<center/> | <center>RESULT <center/>| <center>PASS / FAIL<center/>| 
|:-----|:--------:|----------:|----------:|----:|
| T55  |  **The registered email address** | <center>Email address is accepted</center>|<center> As expected </center>|<center> PASS</center>|
| T56  |  **Enter the correct password** | <center>Password is accepted</center>|<center> As expected </center>|<center> PASS</center>|
| T57  |  **Click on the "Sign In" button** | <center>User is successfully logged in and redirected to the main page</center>|<center> As expected </center>|<center> PASS</center>|


- Sign out

| TEST |  ACTION  | <center>EXPECT RESULT<center/> | <center>RESULT <center/>| <center>PASS / FAIL<center/>| 
|:-----|:--------:|----------:|----------:|----:|
| T58  |  **Click on the "Sign Out" button while the user is logged in** | <center>User is redirected to the main page</center>|<center> As expected </center>|<center> PASS</center>|


- Reset Password

| TEST |  ACTION  | <center>EXPECT RESULT<center/> | <center>RESULT <center/>| <center>PASS / FAIL<center/>| 
|:-----|:--------:|----------:|----------:|----:|
| T59  |  **Click on the "Forgot Password" link** | <center>Password reset page is displayed</center>|<center> As expected </center>|<center> PASS</center>|
| T60  |  **Enter the registered email address** | <center>Email address is accepted</center>|<center> As expected </center>|<center> PASS</center>|
| T61  |  **Click on the "Reset Password" button.** | <center>User receives a reset password email</center>|<center> As expected </center>|<center> PASS</center>|
| T62  |  **Click on the password reset link received via email** | <center>Password reset page is displayed</center>|<center> As expected </center>|<center> PASS</center>|
| T63  |  **Enter a new password** | <center>New password is accepted</center>|<center> As expected </center>|<center> PASS</center>|
| T64  |  **Re-enter the new password to confirm** | <center>Confirmation matches the entered new password</center>|<center> As expected </center>|<center> PASS</center>|
| T65  |  **Click on the "Reset Password" button** | <center>User is redirected to the sign-in page with a confirmation message</center>|<center> As expected </center>|<center> PASS</center>|


## Admin 

- To verify the functionality and security of the admin interface for managing products, reviews, and users


| TEST |  ACTION  | <center>EXPECT RESULT<center/> | <center>RESULT <center/>| <center>PASS / FAIL<center/>| 
|:-----|:--------:|----------:|----------:|----:|
| T66   |  **Add a new product** | <center>Product is successfully added to the database and displayed in the main page</center>|<center> As expected </center>|<center> PASS</center>|
| T67  |  **Delete an existing product** | <center>Product is successfully removed from the database and no longer displayed in the main page</center>|<center> As expected </center>|<center> PASS</center>|
| T68  |  **Delete a review** | <center>Review is successfully deleted from the database and no longer displayed on the review section</center>|<center> As expected </center>|<center> PASS</center>|
| T69  |  **Delete a user account** | <center> User account is successfully deleted from the system, and associated data (orders, reviews) are removed</center>|<center> As expected </center>|<center> PASS</center>|


## Conclusion

Throughout the development and testing phases of the DBZ EICHE application, I meticulously examined each feature to ensure its functionality, usability, and security. Manual testing played a crucial role in identifying and resolving potential issues that automated tests might overlook. Here's a summary of the key findings from the testing process:

During the testing of the header navigation, search functionality, and categories navigation, I verified that all elements were displayed correctly and that users could navigate through the application seamlessly. The main page displayed products accurately, allowing users to view essential details and interact with them effortlessly.

In the product and review management sections, I conducted thorough tests to add, delete, and update products and reviews. These tests ensured that administrators could manage the platform's content efficiently while maintaining data integrity and security.

The cart functionality and secure checkout process were examined extensively to guarantee a smooth and secure transaction experience for users. I verified that users could add items to their carts, adjust quantities, and complete purchases without encountering any issues.

The dashboard functionality provided users with insights into their profiles, order history, and account settings. I ensured that users could access and update their information conveniently, enhancing the overall user experience.

Authentication features such as signup, signin, signout, and password reset were thoroughly tested to ensure the security of user accounts. By implementing proper validation and error handling mechanisms, I aimed to protect user data and prevent unauthorized access.

Lastly, the admin interface underwent rigorous testing to empower administrators with the tools necessary to manage products, reviews, and user accounts effectively. Through comprehensive testing, I verified that administrators could perform their duties efficiently while upholding data security and integrity.

Overall, the manual testing process yielded positive results, with all test cases passing as expected. The DBZ EICHE application emerged as a reliable, user-friendly, and secure platform, ready to deliver an exceptional shopping experience to users while providing robust management capabilities for administrators.


## Validate Responsiveness

| TEST |  ACTION  | <center>EXPECT RESULT<center/> | <center>RESULT <center/>| <center>PASS / FAIL<center/>| 
|:-----|:--------:|----------:|----------:|----:|
| T01   |  **Open the application on a desktop or laptop computer with a standard screen size (e.g., 15 inches or larger)** | <center>The application should display optimally, utilizing the available screen space effectively, with all elements appropriately sized and positioned</center>|<center> As expected </center>|<center> PASS</center>|
| T02  |  **Open the application on a tablet device with a medium-sized screen (e.g., 7 to 10 inches)** | <center> The application should adapt to the smaller screen size, with elements rearranged to maintain readability and usability</center>|<center> As expected </center>|<center> PASS</center>|
| T03  |  **Open the application on a smartphone with a small screen size (e.g., 5 to 6 inches)** | <center>The application should provide a mobile-friendly layout, with navigation, text, and interactive elements optimized for touch input and smaller screens</center>|<center> As expected </center>|<center> PASS</center>|
| T04  |  **Access the application on a mobile device and rotate the device between portrait and landscape orientations** | <center>The application should adjust dynamically to the change in orientation, ensuring that content remains accessible and readable in both orientations</center>|<center> As expected </center>|<center> PASS</center>|
| T05  |  **Access the application using different web browsers (e.g., Chrome, Firefox, Safari)** | <center>The application should render consistently across browsers, maintaining functionality and appearance without significant variations</center>|<center> As expected </center>|<center> PASS</center>|

### Conclusion
The responsiveness test ensures that the DBZ EICHE application delivers a consistent and user-friendly experience across different devices and screen sizes. Passing this test indicates that the application adapts effectively to varying viewing environments, enhancing accessibility and usability for all users.


## Automated Testing Report


### Overview
This report provides a comprehensive overview of the unit tests executed to validate various components within the Django project. These meticulously crafted tests thoroughly assess the functionality of critical components such as the admin interface, forms, models, and views. By rigorously examining these components, the tests aim to bolster the application's robustness and reliability.

#### Test Statistics 
- <strong>Total Number of Tests Conducted:</strong> 53
- <strong>Errors:</strong> None


![TESTS](/media/readme/testing/automated_tests.jpeg)