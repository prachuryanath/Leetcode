class Solution:
    def interpret(self, command: str) -> str:
        parser = {'G':'G',
                 '()':'o',
                 '(al)':'al'}
        for key in parser.keys():
          command = command.replace(key, parser[key])
        return command