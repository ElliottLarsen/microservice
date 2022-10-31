# URL Builder Microservice
This microservice builds and returns a URL based on the query parameters it receives.

## Technologies
* Python
* Flask

## Installation
* Make sure you have Python and Flask installed.
* Clone this repository.
* Run ```export FLASK_APP=main```.
* Start the program by running ```flask run```.
* Go to http://127.0.0.1:5000/ in your web browser.

## Communication Contract
### How to request data
To request URL data, go to http://127.0.0.1:5000/data and pass prefix, project name, and ticket number as query parameters.
#### Example Call
```http://127.0.0.1:5000/data?prefix=johndoe&project=myproject&ticket=123```

### How to receive data
After receiving the user's request, the microservice will return the following in the form of JSON.
* Complete URL built by the microservice.
* Data the microservice received.

If incorrect queries are used, the microservice will return 400 with "Invalid input" message.
#### Example Response
```JSON
{
    "complete_url": "https://johndoe.atlassian.net/browse/myproject-123",
    "data_received": {
        "prefix": "johndoe",
        "project": "myproject",
        "ticket": "123"
    }
}
```

### UML Sequence Diagram


## Contact
Elliott Larsen
* Email elliottlrsn@gmail.com
* GitHub [@elliottlarsen](https://github.com/elliottlarsen)
* LinkedIn [@elliottlarsen](https://www.linkedin.com/in/elliottlarsen)