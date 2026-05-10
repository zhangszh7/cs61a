.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet from students where color = 'blue' and pet = 'dog';

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song from students where color = 'blue' and pet = 'dog' ;


CREATE TABLE smallest_int AS
  SELECT time, smallest from students where smallest > 2 order by smallest limit 20  ;
  

CREATE TABLE matchmaker AS
  SELECT a.pet as shared_pet, b.song as shared_song, a.color as first_color, b.color as second_color from students as a, students as b where a.time != b.time and a.pet = b.pet and a.song = b.song;


CREATE TABLE sevens AS
  SELECT a.seven from students as a, numbers as b where a.number = 7 and b."7" = "True" and a.time = b.time;

