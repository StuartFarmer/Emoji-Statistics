#Emoji Statistics
On my quest to teach myself machine learning, I decided to make a quick statistics experiement on which emojis are most widely used on Twitter. I consume live tweets from San Fransisco in a batch of 1000 and then plot the occurences of emojis on a bar chart.

The results? People love these three emojis the most with the order adjusting slightly on each run:

:heart_eyes:|:joy:|:sob:
--- | --- | ---

A la this chart.

[!Entire Chart](https://raw.githubusercontent.com/StuartFarmer/Emoji-Statistics/master/chart_all.png)

[!Zoomed in Chart](https://raw.githubusercontent.com/StuartFarmer/Emoji-Statistics/master/chart_zoom.png)

Note that Matlibplot doesn't support emoji / I found it pointless to bend over backwards to implement the best UI in this case because this was more for my own education so the X axis is the UTF-8 byte representation of each emoji. You can look up what each of the UTF-8 bytes represent [here.](http://apps.timwhitlock.info/emoji/tables/unicode)

Want to run it yourself? Cool. You'll need matplotlib and twython installed.

> $ pip install matplotlib

> $ pip install twython

After that, add your Twitter App API credentials and you're good to go!

###What's next?

Maybe I'll put this on a webserver that keeps a running total of every emoji and plots it to an interactive graph. Maybe I'll extend the emoji support beyond the emoticons. Most likely, I'll leave this on the shelf and continue learning machine learning to do something more productive.