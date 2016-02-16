from matplotlib import pyplot as plt
from twython import TwythonStreamer
from collections import Counter
import re

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_SECRET = ""
TWEET_NUMBER = 1000
tweets = []

#create an array of emoji byte strings
emojis = [x + 128513 for x in range(58)]

new_emojis = []
for emoji in emojis:
	new_emojis.append(chr(emoji).encode('utf-8'))

emojis = new_emojis

#create a counter
emojiCount = Counter()

class Streamer(TwythonStreamer):
	def on_success(self, data):
		if (data['lang'] == 'en'):
			tweets.append(data['text'].encode('utf-8'))
			print("%i/%i tweets indexed..." % (len(tweets), TWEET_NUMBER))

		if (len(tweets) >= TWEET_NUMBER):
			self.disconnect()

	def on_error(self, status_code, data):
		print(status_code, data)
		self.disconnect()

stream = Streamer(CONSUMER_KEY, CONSUMER_SECRET,
				ACCESS_TOKEN, ACCESS_SECRET)

#get tweets live from SF
stream.statuses.filter(locations="-74,40,-73,41")

#examine each tweet for emojis
for tweet in tweets:
	for emoji in emojis:
		while emoji in tweet:
			tweet = tweet.partition(emoji)[0] + tweet.partition(emoji)[2]
			emojiCount[emoji] += 1

#xcors and heights of each plot
try:
	xs = [i + 0.1 for i, _ in enumerate(emojiCount.keys())]

	plt.bar(xs, emojiCount.values(), color="green")

	plt.ylabel("# of Emojis per %i Tweets" % TWEET_NUMBER)
	plt.xlabel("Unicode Representation of Emojis")
	plt.title("Twitter's Favorite Emojis")

	plt.xticks([i + 0.5 for i, _ in enumerate(emojiCount.keys())], emojiCount.keys())

	plt.show()
except Exception as e:
	print(e)