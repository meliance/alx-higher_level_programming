-- create the database hbtn_od_usa and table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_od_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
