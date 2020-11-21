-- Д.З. 6 “Операторы, фильтрация, сортировка и ограничение. Агрегация данных”

-- 2. 

use snet2910;

select
	firstname,
	lastname,
	(select count(*) talks from messages where to_user_id = 1 group by from_user_id order by talks desc limit 1) number_of_msgs
from users u where u.id = 1;

-- 3.

select count(*) from photo_likes pl 
where who_likes in (select id from users u where timestampdiff(year, u.birthday, now())<14);

-- 4.

select 
	(select count(*) who_likes from photo_likes pl where pl.who_likes in 
		(select id from users u where u.gender = 'f')) likes_by_women,
	(select count(*) who_likes from photo_likes pl where pl.who_likes in 
		(select id from users u where u.gender = 'm')) likes_by_men;

-- 5.

select
	id,
	((select count(*) who_likes from photo_likes pl where pl.who_likes = u.id) +
	(select count(*) from_user_id from messages m2 where m2.from_user_id = u.id) +
	(select count(*) user_id from photos p where p.user_id = u.id) +
	(select count(*) initiator_user_id from friend_requests fr where fr.initiator_user_id = u.id)) as total_activities
from users u order by total_activities;
