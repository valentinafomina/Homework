drop if exists database example;
create database example;
use example;

create if not exists table users(
	id int,
	name varchar(100)
	);

insert into users values(1, 'ivan ivanov');


