
"""my_string = "this is My First Python programming class and i am learNING python string and its function"
1 . Try to extract data from index one to index 300 with a jump of 3
2. Try to reverse a string without using reverse function
3. Try to split a string after conversion of entire string in uppercase
4. try to convert the whole string into lower case
5 . Try to capitalize the whole string
6 . Write a diference between isalnum() and isalpha()
7. Try to give an example of expand tab
8 . Give an example of strip , lstrip and rstrip
9.  Replace a string charecter by another charector by taking your own example
"sudhanshu"
10 . Try  to give a defination of string center function with and exmple
11 . Write your own definition of compiler and interpretor without copy paste form internet in your own language
12 . Python is a interpreted of compiled language give a clear ans with your understanding
13 . Try to write a usecase of python with your understanding"""

import logging
logging.basicConfig(filename = 'string.log',level = logging.DEBUG,format='%(levelname)s %(name)s %(asctime)s %(message)s')

class string_s:
    logging.info(' we are creating a class to do string process')
    def extract_data(self):
        logging.info('we are creating a function to extract string data')
        try:
            logging.info('we are entering into try block')
            self.s = s
            logging.info(s[0:300:3])
            print(s[0:300:3])
        except Exception as e:
            logging.exception(e)

    def reverse_str(self):
        logging.info('we are creating a function to extract string data')
        try:
            logging.info('we are entering into try block')
            self.s = s
            logging.info(s[::-1])
            print(s[::-1])
        except Exception as e:
            logging.exception(e)

    def split_strr(self):
        logging.info('we are creating a function to extract string data')
        try:
            logging.info('we are entering into try block')
            self.s = s
            l = s.upper()
            split_str = l.split()
            logging.info(split_str)
            print(split_str)
        except Exception as e:
            logging.exception(e)

    def split_strr_low(self):
        logging.info('we are creating a function to extract string data')
        try:
            logging.info('we are entering into try block')
            self.s = s
            l = s.lower()
            split_str_lower = l.split()
            logging.info(split_str_lower)
            print(split_str_lower)
        except Exception as e:
            logging.exception(e)

    def cap_strr(self):
        logging.info('we are creating a function to extract string data')
        try:
            logging.info('we are entering into try block')
            self.s = s
            l = s.capitalize()
            logging.info(l)
            print(l)
        except Exception as e:
            logging.exception(e)

    def alph_alnum(self):
        logging.info('we are creating a function to extract string data')
        try:
            logging.info('we are entering into try block')
            a = 'senthurapandi'
            logging.info('#isalpha is going to return true if the string is alphabetic and isalnum is going to retunr true if the string is numeric+alphabetic')
            print(a.isalnum(),a.isalpha())
        except Exception as e:
            logging.exception(e)

    def expand_strr(self):
        logging.info('we are creating a function to extract string data')
        try:
            logging.info('we are entering into try block')
            m = 'senthurapandi\tis\ta\tgood\tboy.'
            logging.info(m.expandtabs())
            print(m.expandtabs())
        except Exception as e:
            logging.exception(e)

    def etrip_strr(self):
        logging.info('we are creating a function to extract string data')
        try:
            logging.info('we are entering into try block')
            s = '   senthurapandi is a good boy              '
            r = '                       senthura pandi is a boy                '
            p = '        senthura pandi is a boy'
            logging.info(p.strip())
            logging.info(s.lstrip())
            logging.info(r.rstrip())
            print(p.strip())
            print(s.lstrip())
            print(r.rstrip())
        except Exception as e:
            logging.exception(e)

    def replace_strr(self):
        logging.info('we are creating a function to extract string data')
        try:
            logging.info('we are entering into try block')
            m = 'senthurapandi is a good boy.'
            logging.info(m.replace('senthurapandi','sudh'))
            print(m.replace('senthurapandi','sudh'))
        except Exception as e:
            logging.exception(e)
logging.shutdown()


s = "this is My First Python programming class and i am learNING python string and its function"
obj = string_s()
obj.extract_data()
obj.reverse_str()
obj.split_strr()
obj.split_strr_low()
obj.cap_strr()
obj.alph_alnum()
obj.expand_strr()
obj.etrip_strr()
obj.replace_strr()