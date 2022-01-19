# George W. Bush Twitter Bot
### Background
For over a year now, my girlfriend has been asking me to build her something
that will send her a famous bush quote every morning. So I finally made it. This
Bot is currently operating through my personal AWS account and is tweeting a random
quote every morning at 6:38 AM. 

### Bush-isms
George Bush did some questionable things while in office, but one of the best things to come
out of his tenure was his "Bush-isms." I would like to give a lot of credit to Jacob Weisberg, who spent
the time and actually recorded and published over 500 of these ridiculous quotes (over a span of 5 books). All possible quotes can be found
in "The Complete Bushisms.html" file in the repo. This quotes cover just about every topic and are from all parts
of his presidency.

### How it works
Using AWS CloudEvents, I call the lambda function (TwitterAPI/aws_stuff/lambda_function.py) every morning. 
The lambda function utilizes AWS's S3 buckets which store my keys and all the quotes used for the twitter bot.
I understand that it is a better, more secure idea to store my keys in AWS secrets, but at the moment I would like to keep this implementation
free and this works well. As you can see from the quotes.json file, all the quotes from the article have been saved and can be easily accessed.
Once the quote is loaded in, it is posted 280 characters at a time. If the quote happens to be longer than 280 quotes,
the quote will simply continue as a reply to the initial tweet. The actual posting of the tweet is incredibly simple and can be seen
in better detail through the two API sample codes included.

### Twitter API Sample Code
I have included in the TwitterAPI folder 2 tutorials for posting a tweet to 
Twitter using their API and Python. The Three-Way-HandshakeOAUTH file is taken directly
from Twitter's documentation with some minor changes (changed the callback uri, so you don't have to
have your own website). The other one, simplePost, is a quick tutorial I wrote myself that utilizes Token 
keys instead of the Three-way-handshake which I found to be a much easier implementation.
