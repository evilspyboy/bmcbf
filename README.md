Super simple Discord bot that passes mentions off to a webhook.  Good for use with other automation/workflow services where you just need the discord bot to work like duct tape to connect the two.

To use this you will need to:

1. Configure a Discord Bot, get it's secret token and add the bot to your discord
2. It is better practice to not put the secret token directly into the python but that comes down to level of risk you are ok with (aka how much damage can someone do with that)
3. Run up a pico/smallest VM server you can on AWS or GCP and ensure that Python 2.8 or above is supported on it (pretty standard now)
4. If you are going to use this with a webhook, add in your webhook, if not and you are using this as a bit of simple code to modify then enjoy.
5. After uploading the python and requirements.txt to your cloud vm (or local if you want, Im not your mum do what you want) make sure you have given it permission to run as a service so that when you close your terminal session it will keep running.

And that is about it. This isn't too complicated and Im just uploading it in case it helps someone else looking for a simple discord bot to call a webhook.
