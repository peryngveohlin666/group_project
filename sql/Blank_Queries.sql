INSERT INTO customer (id,is_regular,is_valued,name,surname,address)
VALUES (452,1,1,'Peter','Stefanov','15 Red Wall');

INSERT INTO `group` (id,name)
VALUES (10,'Peter');

INSERT INTO user (id,staff_code,password,name,surname,address,agency,Groupid)
VALUES (452,11,990403,'Peter','Stefanov','15 Red Wall','HH',10);

INSERT INTO user_blank_assignment (Userid,Blanknumber,comission_rate)
VALUE (452,41236,12);

INSERT INTO blank (number,type,is_sold,is_refunded,Customerid,date,User_Blank_AssignmentUserid,User_Blank_AssignmentBlanknumber)
VALUES	(41236,3,1,0,452,'2008-11-11',452,41236);

INSERT INTO currency (type,rate)
VALUES (true,13);

INSERT INTO discount (type,rate)
VALUES (true,13);

INSERT INTO payment (Blanknumber, amount, type, is_valid, is_regular, Currencytype, Discounttype)
VALUES (41236,100,true,1,1,true,true);
