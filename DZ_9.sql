-- Д.З.8 Транзакции

-- 1.

start transaction;
select * from users where users.id = 1;
insert into sample.users select * from shop_1.users where users.id = 1;
delete from shop_1.users where users.id = 1;
commit;

-- 2. 

create view prod_cat as
select p.name prod, c.name cat
from products as p
join catalogs as c
where p.catalog_id = c.id;

select * from prod_cat;

-- 4.

delimiter //
drop procedure if exists delete_old_entries//
create procedure delete_old_entries()
begin
	drop table if exists latest_5_entries;
	create temporary table latest_5_entries select * from users order by created_at desc limit 5;
	truncate table users;
	insert into users select * from latest_5_entries;	
end//

call delete_old_entries ();

-- Хранимые процедуры

-- 1. 
select current_time();

delimiter //
drop procedure if exists Hello//
create procedure Hello()
begin
	set @time = current_time();
	select
		case
			when @time >= '00:00:00' and @time < '06:00:00' then 'Доброй ночи!'
			when @time >= '06:00:00' and @time < '12:00:00' then 'Доброе утро'
			when @time >= '12:00:00' and @time < '18:00:00' then 'Добрый день'
			when @time >= '18:00:00' and @time < '23:59:59' then 'Добрый вечер'
		end as greeting;
end//

call Hello();

-- 2.

delimiter //
drop trigger if exists products_not_null//
create trigger products_not_null before insert on products
for each row
begin 
  	IF new.name is NULL and new.description is NULL THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Введите Name или Description';
  	END IF;
end//

drop trigger products_not_null;

-- Проверка:
INSERT INTO products
  (name, description, price, catalog_id)
VALUES
  (NULL, NULL, 7890.00, 1);
  