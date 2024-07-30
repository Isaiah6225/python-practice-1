CREATE DATABASE password_manager_db
use users; 

CREATE TABLE users(
    user_id int not null AUTO_INCREMENT,
    username varchar(50) not null,
    password varchar(50) not null, 
    PRIMARY KEY (user_id)
);

CREATE TABLE user_pass_info(
    pass_info_id int not null AUTO_INCREMENT,
    user_id INT NULL  AUTO_INCREMENT,
    password_purpose varchar(50)  NULL,
    user_user_name varchar(50)  NULL,
    user_password varchar(50)  NULL,
    PRIMARY KEY (user_id)
);