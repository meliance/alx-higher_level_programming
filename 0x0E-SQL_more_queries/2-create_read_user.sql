-- create the database hbtn_od_2 and user_0d_2
CREATE DATABASE IF NOT EXIST hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2';
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
