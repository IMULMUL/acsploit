import abc
import cmdline
import inspect
import re
import sys

class AcsploitCommandLine(cmdline.BaseCmd):
	def preloop(self):
		self.select_commands = {}

	@staticmethod
	def start_instance():
		prompt = AcsploitCommandLine()
		prompt.prompt = "> "
		prompt.cmdloop('***************Acsploit***************\nSelect an algorithm to being. Type \'help\' for available commands')

	def get_select_commands(self):
		if not self.select_commands:
			for name, obj in inspect.getmembers(cmdline, inspect.isclass):
				try:
					if isinstance(obj(), cmdline.ExploitCommandLine) and obj is not cmdline.ExploitCommandLine:
						arg_name = re.sub("CommandLine", '', name).lower()
						self.select_commands[arg_name] = obj()
				except TypeError:
					pass

		return self.select_commands

	def help_use(self):
		commands = self.get_select_commands()
		print("Available exploitable algorithms and data structures are:")
		for key in commands.keys():
			print(key)

	def do_use(self, args):
		algorithm_name = args.split()[0]

		commands = self.get_select_commands()
		if algorithm_name in commands:
			commands[algorithm_name].start_instance()
		else:
			print("Invalid argument: " + algorithm_name)
			self.help_select()


def main():
	AcsploitCommandLine.start_instance()

main()


