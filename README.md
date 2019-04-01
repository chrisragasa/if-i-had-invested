# If I Had Invested
___
A Flask application that leverages the Alpha Vantage API to calculate your gains/losses if you had invested in a particular stock at a given time.
### https://ancient-tundra-23314.herokuapp.com/
___

### Project Introduction:
Have you ever had a conversation with someone about a particular stock/asset that recently skyrocketed in value? I'd bet that at some point in that conversation, a version of the following was said: "If only I had invested in *company xyz*, I'd be so rich right now!". This app will tell you exactly how rich you could have been if you had invested. Of course, not all stocks are created equally, so you could have ended up losing money too.

I know... I know... it's a silly idea for an application. However, investing is one of my hobbies, and this project was made out of pure fun and a personal interest to learn Flask since Python is one of my favorite languages (and brush up on some front-end skills). All in all, it ended up being a cool project to build!

### Project Limitations / Future Improvements:
1) The Alpha Vantage API does not provide any information on stock splits. Therefore, calculations done by this app will be inaccurate if the company underwent a stock split in between the entered investment date and the current date. In a future version, this miscalculation needs to be addressed.
2) In a future version, I would hope to implement a login system so that users can keep track of their assets. This would involve creating my own RESTful API.

### Built With:
Backend - Flask/Python

Frontend - HTML, CSS, JavaScript/jQuery

### Credits:
https://www.pexels.com

https://www.flaticon.com

___
### Development / Compile Instructions
In root directory:
```bash
$ pip install -r requirements.txt
$ python run.py
```