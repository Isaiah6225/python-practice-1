from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, VARCHAR


app = Flask(__name__)

#Connection to db 
url = 'mysql+pymysql://isaiah6225:root@localhost:3306/password_manager_db'
 
#engine object
engine = create_engine(url)
Base = declarative_base()


#users table model
class users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, autoincrement = True)
    username = Column(VARCHAR(50), nullable=True)
    password = Column(VARCHAR(50), nullable=True)

class user_pass_info(Base):
    __tablename__ = 'user_pass_info'

    pass_info_id = Column(Integer, primary_key=True, autoincrement=True)
    password_purpose = Column(VARCHAR(50), nullable=True)
    user_user_name = Column(VARCHAR(50), nullable=True)
    user_password = Column(VARCHAR(50), nullable=True)    

#ensure flask is running  
@app.route('/')
def flask():
        return 'Flask is running!'

#check database connection 
@app.route('/db-connection')
def test_db_connection():
    try:
        connection = engine.connect()
        return 'Flask is connected to database!'
    except Exception as e:
        # Handle connection error
        print("Connection failed: ", e)
    connection.close()


#sign up page route 
@app.route('/SignUp', methods=['POST'])
def sign_up():
    data =request.json
    username = data.get('username')
    password = data.get('password')
    
    #Create sesssion object to interact wiht the database 
    Session = sessionmaker(bind=engine)
    session = Session()

    # new object 
    new_user = users(username = username, password = password)

    session.add(new_user)
    session.commit()
    session.close()

    return 'Success writing to db!'

#login page route
@app.route('/login', methods=['POST'])
def login_page():
    data = request.json
    username = data['username']
    password = data['password']

    Session = sessionmaker(bind=engine)
    session = Session()

    user = session.query(users).filter_by(username=username, password=password).first()
    session.close()
    if user.username == username and user.password == password:
        return 'Login successful'
    
    else: 
        return 'Login unsuccessful'
    
    

#Home page route 
@app.route('/home', methods=['POST'])
def home_page():
    data = request.json
    password_purpose_back = data['passwordPurpose']
    user_user_name_back = data['userUserName']
    user_password_back = data['userPassword']

    Session = sessionmaker(bind=engine)
    session = Session()

    new_user_pass_info = user_pass_info(passsword_purpose = password_purpose_back, user_user_name = user_user_name_back, user_password = user_password_back)

    session.add(new_user_pass_info)
    session.commit()
    session.close()

    return 'Success writing pass info to db!'
    

if __name__ == '__main__':
    app.run(host='0.0.0.0' ,debug=True)