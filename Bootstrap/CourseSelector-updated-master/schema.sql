drop table if exists majors_lookup;
drop table if exists course_lookup;
drop table if exists student_account_details;
drop table if exists student_academic_details;
drop table if exists student_course_details;


create table student_course_details(
  id integer not null,
  course_name varchar not null,
  course_code varchar not null,
  semester varchar not null

);

create table student_account_details(
  id integer primary key AUTOINCREMENT,
  title varchar not null,
  first_name varchar not null,
  middle_name varchar,
  last_name varchar not null,
  street varchar,
  city varchar ,
  state varchar ,
  country varchar ,
  birth_date date not null,
  email varchar not null,
  password varchar not null
);

create table student_academic_details(
  id integer primary key AUTOINCREMENT,
  degree varchar not null,
  major varchar,
  semester integer not null
);


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
  major_code varchar,
  course_rating integer
  );

insert into majors_lookup(major_code,major_name) values ("INFM","Information Management");
insert into majors_lookup(major_code,major_name) values ("CMSC","Computer Science");
insert into majors_lookup(major_code,major_name) values ("ENTS","Telecommunication");
insert into majors_lookup(major_code,major_name) values ("ENEE","Electrical and Computer Engineering");

insert into course_lookup(course_code,course_name,major_code,course_rating) values ("INFM600","INFM600 - Information Environments","INFM",1);
insert into course_lookup(course_code,course_name,major_code,course_rating) values ("INFM603","INFM603 - Information Technology and Organizational Context","INFM",2);
insert into course_lookup(course_code,course_name,major_code,course_rating) values ("INFM605","INFM605 - Users and Use Context","INFM",4);
insert into course_lookup(course_code,course_name,major_code,course_rating) values ("INFM612","INFM612 - Management of Information Program and Services","INFM",5);
insert into course_lookup(course_code,course_name,major_code,course_rating) values ("INFM620","INFM620 - Introduction to Strategic Informatino Management","INFM",2);
insert into course_lookup(course_code,course_name,major_code,course_rating) values ("INFM700","INFM700 - Information Technology and Organizational Context","INFM",4);




insert into course_lookup(course_code,course_name,major_code) values ("CMSC122","CMSC122 - Introduction to Computer Programming via the Web","CMSC");
insert into course_lookup(course_code,course_name,major_code) values ("CMSC131","CMSC131 - Object Oriented Programming I","CMSC");

insert into student_account_details(title,first_name,middle_name,last_name,email,birth_date,password) values ("Miss","Prajakta","Sanjeev","Arolker","admin","24-AUG-1990","admin");


insert into student_academic_details(degree,major,semester) values ("Masters","Information Management","Fall 2014");

insert into student_course_details(id, course_name, course_code, semester) values (1,"INFM600 - Information Environments","INFM600","Fall 2014");
insert into student_course_details(id, course_name, course_code, semester) values (1,"INFM603 - Information Technology","INFM603","Fall 2014");