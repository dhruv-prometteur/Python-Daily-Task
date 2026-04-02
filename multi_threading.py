from threading import Thread
from multiprocessing import Process
from time import time






    # class Hello(Thread):
    #     def run(self):
    #         for i in range(5):
    #             print("say hello",i+1)

    # class Hi(Thread):
    #     def run(self):
    #         for i in range(5):
    #             print("say hi",i+1)


    # t1=Hello()
    # t2=Hi()

    # t1.start()
    # t2.start()

    # t1.join()
    # t2.join()

    # print("completed")





    # def hello():
    #     for i in range(5):
    #         print("say hello",i+1)


    # def hi():
    #     for i in range(5):
    #         print("say hi",i+1)


    # t1=Thread(target=hello)
    # t2=Thread(target=hi)

    # t1.start()
    # t2.start()



def calculate(n1,n2):
        sum=0
        for i in range(n1,n2):
            sum += i*i
            
if __name__=="__main__":
   
    num=500000

    start_time=time()
    calculate(0,num)
    end_time=time()

    print(f"serial time : {end_time-start_time:.2f} seconds")

    mid=num//2
    t1=Thread(target=calculate,args=(0,mid))
    t2=Thread(target=calculate,args=(mid,num))

    start_time=time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time=time()

    print(f"thread time: {end_time-start_time:.2f} seconds")


    t1=Process(target=calculate,args=(0,mid))
    t2=Process(target=calculate,args=(mid,num))

    start_time=time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time=time()

    print(f"process time: {end_time-start_time:.2f} seconds")



