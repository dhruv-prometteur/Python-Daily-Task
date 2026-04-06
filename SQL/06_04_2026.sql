select * from students
insert into students (id,name,age,city,marks)
values(null,"HHH",50,null,89)
values(2,"Rolex",26,"valsad",56),
(null,"Brock",53,"Delhi",75),
(null,"Roman",45,"Mumbai",59),
(null,"John",39,"Pune",83),
(null,"Conor",26,"Surat",92);


select name,age from students
select name,marks from students where marks >70
select * from students where marks between 80 and 90
select name,city from students where city ="Mumbai"
select name,city from students where city !="Delhi"
select name,city from students where not city ="Delhi"
select name,city from students where city in ("Mumbai","Delhi")
select name,city from students where city not in ("Mumbai","Delhi")

select name,marks from students where marks>70 and marks<90
select name,marks from students where (marks>70 and age>30) or marks<90


select * from students order by city desc
select * from students where city is null
select * from students where city is not null

select name,city from students where city like '%i'
select name,city from students where city like 'v%'
select name,city from students where city like '%a%'
