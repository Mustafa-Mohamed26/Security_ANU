-- Create the users table
create table users (
    id int primary key auto_increment,
    username varchar(50),
    password varchar(50)
);

--------------------------------------------------------------

-- Insert data into the users table
insert into users (username, password) values
    ('admin', 'password'),
    ('user1', 'password1'),
    ('user2', 'password2'),
    ('user3', 'password3');

--------------------------------------------------------------

-- Select all data from the users table
select * from users;

--------------------------------------------------------------

-- Select specific data from the users table
select * form users where username = 'admin' and password = 'password';

--------------------------------------------------------------

-- SQL injection
select * from users where username = 'admin'-- ' and password = 'password';
select * from users where username = 'admin' or 1=1-- ' and password = 'password';
select * from users where username = '' or 1=2-- ' and password = 'password';
select * from users where username = ''; 

-- Delete the users table 
drop table users;
-- Delete all data from the users table
delete from users;
--------------------------------------------------------------