# Twitter-Image-Bot
Basic twitter bot that posts images from a folder

This twitter bot works with the twitter API to conect to and post images randomly selected from a screenshots folder using Python. I ran this from home on a Rasberry pi.

Setup instuctions

  Set the image folder you would like to use on line 39 (imagebot("screenshots/"))
  In the config.cfg file, enter your twitter api key, secret, oauth token, and oauth token secret.
  Set the status you would like to post on line 30
  Posted screenshots will be copied to the folder listed on line 36
  Images must be under 3MB
  It's also sensitive to some unusual ascii symbols
