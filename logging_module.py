# import logging

# logging.basicConfig(filename="app.log",level=logging.DEBUG,format="%(asctime)s - %(levelname)s - %(message)s")

# def login(username,password):
#     logging.debug(f"trying to login for {username}")
#     if username=="dhruv" and password==1234:
#         logging.info("user login successful")
#     else:
#         logging.warning("login failed")


# def connect_db():
#     logging.debug("trying to connect database")
#     success=False

#     if not success:
#         logging.critical("database failed! app cannot continue")


# login("dhruv",1234)
# connect_db()


import logging 

logger=logging.getLogger(__name__)


logger.setLevel(logging.DEBUG)

file_handler=logging.FileHandler("app.log")
file_handler.setLevel(logging.ERROR)

console_handler=logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s - [in %(filename)s:%(lineno)d")

file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)



logger.debug("this is debug message")
logger.error("this is erorr message")


