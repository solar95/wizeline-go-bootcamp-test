# wizeline-go-bootcamp-test
A test for the Go Bootcamp

Instructions: Create a REST API in the language you feel more comfortable with.

Acceptance Criteria:
Support two endpoints
- An endpoint should display the typical "Hello, World."
- An endpoint is open to your consideration. You can consume an external DB or API, e.g., weather, location.
Add relevant unit testing following best practices from the selected language.

Endpoint 1

It was developed with Python3 and placed in a Lambda function inside AWS. The public endpoint for calling the function is https://1fqnslntj8.execute-api.us-east-1.amazonaws.com/dev/endpoint1. It returns two greetings.

You can find the code inside the file endpoint1.py. 

Endpoint 2

It was developed with Python3 and placed in a Lambda function inside AWS. The public endpoint for calling the function is: https://1fqnslntj8.execute-api.us-east-1.amazonaws.com/dev/endpoint2. It returns the number of Covid cases in a Mexican state. The state is selected randomly. The API that I used to obtain the data is https://api.covid19api.com/

You can find the code inside the file endpoint2.py. 

Due to the 2 functions don't accept any parameter, I don't find it relevant to create unit testing for the code.
