// ## **Part One: Solidify Terminology**

// In your own terms, define the following terms:

// - What is HTTP? Hyper Text Transfer Protocol is the protocol, or order of information to be transfered from a server to a device typically using a browser.
// - What is a URL? Uniform Resource Locator is the text we use to find specific IP servers using HTTP.
// - What is DNS? Domain Naming System acts as the phonebook of the internet so we dont have to remember numbers for the names of servers to connect to.
// - What is a query string? A query string is an additional perameter attached to an HTTP request to load specific content from a given page.
// - What are two HTTP verbs and how are they different? GET and POST. Get is onle retreving information where a post is modifying information in some way.
// - What is an HTTP request? An HTTP request is when a user sends a request to a server to recive data. This request returns what is loaded on the site (HTML/ CSS/ JS)
// - What is an HTTP response? An HTTP response is what the server sends back to the browser and is processed to display a page.
// - What is an HTTP header? Give a couple examples of request and response headers you have seen. An HTTP header would be specific perameters for the page such as language, casheing, or cookies.
// - What are the processes that happen when you type “http://somesite.com/some/page.html” into a browser? The broser resolves the string using DNS and the name is changed into a server IP that is the location of the date we are seeking. This sends a request and the server resonds with what is displayed on the page.


// ## **Part Two: Practice Tools**

// 1. Using ***curl***, make a ***GET*** request to the *icanhazdadjoke.com* API to find all jokes involving the word “pirate”
// 2. Use ***dig*** to find what the IP address is for *icanhazdadjoke.com*
// 3. Make a simple web page and serve it using ***python3 -m http.server***. Visit the page in a browser.


// ## **Part Three: Explore Dev Tools**

// Build a very simple HTML form that uses the GET method (it can use the same page URL for the action) when the form is submitted.

// Add a field or two to the form and, after submitting it, explore in Chrome Developer tools how you can view the request and response headers.

// Edit the page to change the form type to POST, refresh in the browser and re-submit. Do you still see the field in the query string? Explore in Chrome how you can view the request and response headers, as well as the form data.

// ## **Part Four: Explore the URL API**

// At times, it’s useful for your JavaScript to look at the URL of the browser window and change how the script works depending on parts of that (particularly the query string).

// [Read about the URL API](https://developer.mozilla.org/en-US/docs/Web/API/URL)

// Try some of the code examples in the Chrome Console so that you can get comfortable with the basic methods and properties for instances of the URL class.