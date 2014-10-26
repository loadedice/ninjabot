# magic 8 ball plugin
import random

class Plugin:
	def load(self, bot, config):
		self.bot = bot
		self.config = config

	def trigger_magic8(self, msg):
		"Get your question answered by a magic 8 ball!"
		answers = ["It is certain","It is decidedly so","Without a doubt","Yes definitely","You may rely on it","As I see it, yes","Most likely","Outlook good","Yes","Signs point to yes","Reply hazy try again","Ask again later","Better not tell you now","Cannot predict now","Concentrate and ask again","Don't count on it","My reply is no","My sources say no","Outlook not so good","Very doubtful"]
		self.bot.privmsg(msg.channel, "{}: {}".format(msg.nick, random.choice(answers)))
