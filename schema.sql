drop table if exists majors_lookup;

create table majors_lookup (
  id integer primary key AUTOINCREMENT,
  major_code varchar not null,
  major_name varchar not null,
  add_column1 varchar ,
  add_column2 varchar
  );

insert into majors_lookup(major_code,major_name) values ("INFM","Information Management");
insert into majors_lookup(major_code,major_name) values ("CS","Computer Science");

