-- Д.З. 5 "Операторы, фильтрация, сортировка и ограничение"

-- 1.

use snet2910;
alter table users
drop column updated_at;

alter table users 
add column updated_at datetime;

update users set updated_at = now();

select * from users limit 2;

-- 2.

alter table 
users modify created_at datetime;

alter table 
users modify updated_at datetime;

-- 3.

use Homework;
create table storehouse_products(
	id serial primary key,
	product_name varchar(50),
	quantity int(4)
);

insert into storehouse_products (product_name, quantity) values ('qwe', 129), ('rty', 2342), ('uio', 0), ('asd', 934), ('fgh', 302), ('jkl', 234);

select * from storehouse_products order by if (quantity > 0, 0, 1), quantity;


-- "Агрегация данных"

-- 1. 

use snet2910;
select avg((to_days(now()) - to_days(birthday))/365.25) from users;

-- 2.

select
    count(*),
	case(weekday(concat (2020, (substring(birthday, 5, 6)))))
		when 0 then 'Monday'
		when 1 then 'Tuesday'
		when 2 then 'Wednesday'
		when 3 then 'Thursday'
		when 4 then 'Friday'
		when 5 then 'Saturday'
		when 6 then 'Sunday'
	end as birthday2020
from users group by birthday2020;

