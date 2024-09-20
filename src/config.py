import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'Suraj@14') 
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'surajsakhare142002@gmail.com') 
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'qisq eepd orny ledh') 
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'surajsakhare142002@gmail.com')
