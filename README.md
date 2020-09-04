# QuickTip: EmbededPython
This is the Python Script from the Embeded Python QuickTip video featured here: https://youtu.be/iDi4OT9S8WQ

# How it works:
re.search takes in our regular expression and the input string which is sent from our bot.

It returns an re.Match object (postal_code) containing the start and end of the found match.

Within the try/except block - we're trying to extract the text from the address using the postal_code start and end locations...if this fails, we're passing back a message that the regular expression couldnt find the match within the text.

Of Note: There are many other ways to solve the problem introduced in the video...this was just a quick demonstration of how to embed Python within your bot.
