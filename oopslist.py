import logging
logging.basicConfig(filename = 'list.log',level = logging.DEBUG,format='%(levelname)s %(name)s %(asctime)s %(message)s')

class list_s:
    logging.info('we are creating a class called list')
    def extract_list(self,l):
        logging.info('we are creating a function to extract list')
        try:
            self.l = l
            for i in l:
                if type(i) == list:
                    print(i)
        except Exception as e:
            logging.exception(e)

    def reverse_list(self,l):
        logging.info('we are creating a function to reverse the list')
        try:
            self.l = l
            print(l[::-1])
            logging.info(l[::-1])
        except Exception as e:
            logging.exception(e)

    def extract_init_list(self,l):
        logging.info('we are creating a function to extract int')
        try:
            self.l = l
            n = []
            for i in l:
                if type(i) == list or type(i) == tuple or type(i) == set :
                    for j in i :
                        if type(j)==int:
                            n.append(j)
            for k in l[4].items():
                for m in k:
                    if type(m)==int:
                        n.append(m)
                        logging.info(n)
            print(n)
        except Exception as e:
            logging.exception(e)

    def extract_string(self,l):
        logging.info('we are creating a function to extract string from a list')
        try:
            self.l = l
            o = []
            for i in l:
                if type(i)==list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j)==str:
                            o.append(j)
            for k in l[4].items():
                for n in k:
                    if type(n)==str:
                        o.append(n)
                        logging.info(o)
            print(o)
        except Exception as e:
            logging.exception(e)

    def extract_ineuron(self,l):
        logging.info('we are creating a function to extract ineuron from the list')
        try:
            self.l = l
            p = []
            for i in l:
                if type(i)==list:
                        for j in i:
                            if j=='ineuron':
                                p.append(j)

            for k in l[4].items():
                for n in k:
                    if n=='ineuron':
                            p.append(n)
                            logging.info(p)
            print(p)
        except Exception as e:
            logging.exception(e)

    def extract_flat_list(self,l):
        logging.info('we are creating a function to extract_flat list')
        try:
            self.l = l
            n = []
            for i in l:
                if type(i)==list or type(i)==set or type(i)==tuple:
                    for j in i:
                        n.append(j)
                if type(i)==dict:
                    for k in i.items():
                        for g in k:
                            if type(g) == int or type(g) == str:
                                n.append(g)
                                logging.info(g)
            print(n)
        except Exception as e:
            logging.exception(e)

    def print_prime(self):
        """  To create list of prime numbers between 1 to 1000"""
        logging.info("Inside print_prime function")
        try:
            self.l = []
            for i in range(1, 1000):
                c = 0
                for j in range(2, i):
                    if i % j == 0:
                        c = 1
                if c != 1:
                    self.l.append(i)
            logging.info("Output %s", self.l)
            return self.l
        except Exception as e:
            logging.exception(e)
            return e

    def occur_element(self):
        logging.info('we are creating a function to find the number of occurance of each element')
        try:
            self.l = l
            n = []
            for i in l:
                if type(i)==list or type(i)== tuple or type(i)==set:
                    for j in i:
                        n.append(j)

                if type(i)==dict:
                    for k in i.items():
                        for g in k:
                            if type(g)==int or type(g)==str:
                                n.append(g)

            for o in n:
                logging.info(n.count(o))
                print(o,":",n.count(o))
        except Exception as e:
            logging.exception(e)

logging.shutdown()





l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7),set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
     {'k1': "sudh", 'k2': "ineuron", 'k3': "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]]
obj = list_s()
obj.extract_list(l)
obj.reverse_list(l)
obj.extract_init_list(l)
obj.extract_string(l)
obj.extract_ineuron(l)
obj.extract_flat_list(l)
print(obj.print_prime())
obj.occur_element()