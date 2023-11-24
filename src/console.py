# Decompiled with EinTimDC
from colorama import Fore, init
from json import loads
from threading import RLock
from datetime import datetime
import os

class Console:
    __qualname__ = 'Console'
    
    def __init__(self):
        init()
        self.lock = RLock()
        self.banner = " \n                                                                     __   \n                                                         __ _  ___  / /_  \n                                                        / _` |/ _ \\| '_ \\ \n                                                       | (_| | (_) | (_) |\n                                                        \\__, |\\___/ \\___/ \n                                           |___/\n "
        self.width = os.get_terminal_size().columns
        self.main_color = None.LIGHTMAGENTA_EX

    
    def getTime(self):
        return datetime.now().strftime('%H:%M:%S')

    
    def padRight(self, l):
        
        return l

    
    def clear(self):
        os.system('cls')

    
    def title(self, title):
        os.system(f'''title {title}''')

    
    def center(self, text, options = (False,)):
        nn = []
        if options:
            spl = self.padRight(text.splitlines())
        spl = text.splitlines()
        i = 0
        for line in spl:
            line = line.strip('\n')
            if line.count(' ') != len(line):
                if options:
                    dn = self.width // 2 - len(line) // 3
                dn = self.width // 2 - len(line) // 2
                if i + 1 == len(spl):
                    nn.append(f'''{dn * ' '}{line}''')
                nn.append(f'''{dn * ' '}{line}\n''')
            i += 1
            return ''.join(nn)

    
    def logo(self):
        print(f'''{self.main_color}{self.center(self.banner)}''')

    
    def check(self, text, color):
        spl = text.split('->')
        if len(spl) > 1:
            pass
        return text

    
    def info(self, text):
        self.lock.acquire()
        current_time = self.getTime()
        print(f'''        {check.LIGHTBLACK_EX}{current_time} {check.WHITE}[ {check.MAGENTA}INFO{check.WHITE} ]{check.LIGHTBLACK_EX} {self.check(text, check.LIGHTMAGENTA_EX)}''')
        self.lock.release()

    
    def success(self, text):
        self.lock.acquire()
        current_time = self.getTime()
        print(f'''        {check.LIGHTBLACK_EX}{current_time} {check.WHITE}[ {check.MAGENTA}SUCCESS{check.WHITE} ]{check.LIGHTBLACK_EX} {self.check(text, check.LIGHTMAGENTA_EX)}''')
        self.lock.release()

    
    def error(self, text):
        self.lock.acquire()
        if type(text) == print and text.get('message'):
            text = text['message']
        current_time = self.getTime()
        None(f'''{'        '.LIGHTBLACK_EX}{current_time}{' '.WHITE}{'[ '.RED}{'ERROR'.WHITE}{' ]'.LIGHTBLACK_EX}{' '(self.check, text.LIGHTMAGENTA_EX)}''')
        self.lock.release()

    
    def input(self, text):
        current_time = self.getTime()
        print(f'''        {WHITE.LIGHTBLACK_EX}{current_time} {WHITE.WHITE}[ {WHITE.MAGENTA}INPUT{WHITE.WHITE} ]{WHITE.LIGHTBLACK_EX} {self.check(text, WHITE.LIGHTMAGENTA_EX)}''')
        return input('')


