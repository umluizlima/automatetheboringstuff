https://automatetheboringstuff.com/chapter10/

1. assert spam >= 10, 'Spam must be equal or larger than 10!'
2. assert eggs.lower() != bacon.lower(), 'Eggs and bacon must be different!'
3. assert False, 'Trigger happy'
4. "import logging" and "logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')"
5. "import logging" and "logging.basicConfig(filename='programLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')"
6. The five logging levels are: logging.debug(), logging.info(), logging.warning(), logging.error(), logging.critical()
7. Adding logging.disable(logging.CRITICAL) will disable all logging messages in my program.
8. Logging messages are better than print() to display messages because they can be disabled all at once by the programmer.
9. Step will enter a function or method and run its contents. Over will skip over a function or method, staying on your program. Out will exit a function or method that's been stepped.
10. After clicking Go in the Debug Control Window, the debugger will only stop at breakpoints.
11. A breakpoint is a line that is set to stop the running program during debugging.
12. To set a breakpoint on a line of code in IDLE you must right-click it and click on Set Breakpoint