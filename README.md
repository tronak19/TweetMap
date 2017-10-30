# TweetMap

The aim of this project is to collect live Twitter tweets, identify the location and language of the tweet, provide search functionality and plot the tweets on a map.

Live tweets are collected using Twitter Streaming API. The live tweets are stored on AWS ElasticSearch. By employing Google Maps API, the tweets are plotted on the map based on their corresponding coordinates and with different color markers based on the language of the tweet. Tweets are plotted in batches and are retrieved from ElasticSearch at regular intevals. Search functionality in ElasticSearch is used to search the stored tweets for a given keyword.

Technologies:
- Django Framework
- Amazon Web Services
