drop table if exists majors_lookup;
drop table if exists course_lookup;

create table majors_lookup (
  id integer primary key AUTOINCREMENT,
  major_code varchar not null,
  major_name varchar not null,
  add_column1 varchar ,
  add_column2 varchar
  );

create table course_lookup (
  id integer primary key AUTOINCREMENT,
  course_code varchar not null,
  course_name varchar not null,
  major_code varchar
  );

insert into majors_lookup(major_code,major_name) values ("INFM","Information Management");
insert into majors_lookup(major_code,major_name) values ("CMSC","Computer Science");
insert into majors_lookup(major_code,major_name) values ("ENTS","Telecommunication");
insert into majors_lookup(major_code,major_name) values ("ENEE","Electrical and Computer Engineering");

insert into course_lookup(course_code,course_name,major_code) values ("INFM600","INFM600 - Information Environments","INFM");
insert into course_lookup(course_code,course_name,major_code) values ("INFM603","INFM603 - Information Technology and Organizational Context","INFM");
insert into course_lookup(course_code,course_name,major_code) values ("CMSC122","CMSC122 - Introduction to Computer Programming via the Web","CMSC");
insert into course_lookup(course_code,course_name,major_code) values ("CMSC131","CMSC131 - Object Oriented Programming I","CMSC");


