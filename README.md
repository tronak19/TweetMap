# TweetMap

This project collects live tweets using Twitter Streaming API and Tweepy. The live tweets are stored on AWS ElasticSearch. By employing Google Maps API, the tweets are plotted on the map based on their corresponding coordinates. Tweets are plotted in batches and are retrieved from ElasticSearch at regular intevals. Search functionality in ElasticSearch is used to search the stored live tweets for a given search term. The tweets are plotted on the map with different colors based on the language of a particular tweet.
Technologies:
Django Framework
Amazon Web Services
