CREATE TABLE `User` (
  id         int(10) NOT NULL AUTO_INCREMENT, 
  staff_code int(10) NOT NULL UNIQUE, 
  password   int(10) NOT NULL, 
  name       varchar(255), 
  surname    varchar(255), 
  address    varchar(255), 
  PRIMARY KEY (id));
CREATE TABLE Permission (
  id              int(10) NOT NULL AUTO_INCREMENT, 
  codename        varchar(10) NOT NULL UNIQUE, 
  name            varchar(10) NOT NULL UNIQUE, 
  content_type_id int(10) NOT NULL UNIQUE, 
  PRIMARY KEY (id));
CREATE TABLE Blank (
  number      int(10) NOT NULL AUTO_INCREMENT, 
  type        int(10) NOT NULL, 
  is_sold     tinyint(1) NOT NULL, 
  is_refunded tinyint(1) NOT NULL, 
  Customerid  int(10) NOT NULL, 
  `date`      date NOT NULL, 
  PRIMARY KEY (number), 
  UNIQUE INDEX (number));
CREATE TABLE Payment (
  Blanknumber  int(10) NOT NULL, 
  amount       int(10) NOT NULL, 
  type         tinyint(1) NOT NULL, 
  is_valid     tinyint(1) NOT NULL, 
  is_regular   tinyint(1) NOT NULL, 
  Currencytype int(10) NOT NULL, 
  Discounttype tinyint(1), 
  PRIMARY KEY (Blanknumber));
CREATE TABLE Report (
  id          int(10) NOT NULL AUTO_INCREMENT, 
  period_from date NOT NULL, 
  period_to   date NOT NULL, 
  created_on  date NOT NULL, 
  PRIMARY KEY (id));
CREATE TABLE `Group` (
  id      int(10) NOT NULL AUTO_INCREMENT, 
  name    int(10) NOT NULL UNIQUE, 
  User_id int(10) NOT NULL, 
  PRIMARY KEY (id));
CREATE TABLE Report_Blank_Inclusion (
  Reportid    int(10) NOT NULL, 
  Blanknumber int(10) NOT NULL, 
  PRIMARY KEY (Reportid, 
  Blanknumber));
CREATE TABLE User_Report_Access (
  Userid   int(10) NOT NULL, 
  Reportid int(10) NOT NULL, 
  PRIMARY KEY (Userid, 
  Reportid));
CREATE TABLE Group_Permissions (
  Groupid      int(10) NOT NULL UNIQUE, 
  Permissionid int(10) NOT NULL, 
  PRIMARY KEY (Groupid, 
  Permissionid));
CREATE TABLE Stock_Turnover_Report (
  Reportid int(10) NOT NULL, 
  PRIMARY KEY (Reportid));
CREATE TABLE Domestic_Sales_Report (
  Reportid int(10) NOT NULL, 
  PRIMARY KEY (Reportid));
CREATE TABLE Interline_Sales_Report (
  Reportid int(10) NOT NULL, 
  PRIMARY KEY (Reportid));
CREATE TABLE User_Blank_Assignment (
  Userid         int(10) NOT NULL, 
  Blanknumber    int(10) NOT NULL, 
  comission_rate int(10) NOT NULL, 
  PRIMARY KEY (Userid, 
  Blanknumber));
CREATE TABLE Currency (
  type int(10) NOT NULL AUTO_INCREMENT, 
  rate int(10) NOT NULL, 
  PRIMARY KEY (type));
CREATE TABLE Discount (
  type tinyint(1) NOT NULL, 
  rate int(10), 
  PRIMARY KEY (type));
CREATE TABLE Customer (
  id         int(10) NOT NULL AUTO_INCREMENT, 
  is_regular tinyint(1) NOT NULL, 
  is_valued  tinyint(1) NOT NULL, 
  name       varchar(255) NOT NULL, 
  surname    varchar(255) NOT NULL, 
  address    varchar(500), 
  PRIMARY KEY (id));
ALTER TABLE Payment ADD CONSTRAINT FKPayment981424 FOREIGN KEY (Blanknumber) REFERENCES Blank (number);
ALTER TABLE `Group` ADD CONSTRAINT FKGroup247881 FOREIGN KEY (User_id) REFERENCES `User` (id);
ALTER TABLE Report_Blank_Inclusion ADD CONSTRAINT FKReport_Bla496473 FOREIGN KEY (Blanknumber) REFERENCES Blank (number);
ALTER TABLE User_Report_Access ADD CONSTRAINT FKUser_Repor60401 FOREIGN KEY (Userid) REFERENCES `User` (id);
ALTER TABLE User_Report_Access ADD CONSTRAINT FKUser_Repor377816 FOREIGN KEY (Reportid) REFERENCES Report (id);
ALTER TABLE Group_Permissions ADD CONSTRAINT FKGroup_Perm423461 FOREIGN KEY (Groupid) REFERENCES `Group` (id);
ALTER TABLE Group_Permissions ADD CONSTRAINT FKGroup_Perm527187 FOREIGN KEY (Permissionid) REFERENCES Permission (id);
ALTER TABLE Domestic_Sales_Report ADD CONSTRAINT FKDomestic_S819725 FOREIGN KEY (Reportid) REFERENCES Report (id);
ALTER TABLE Interline_Sales_Report ADD CONSTRAINT FKInterline_761250 FOREIGN KEY (Reportid) REFERENCES Report (id);
ALTER TABLE Stock_Turnover_Report ADD CONSTRAINT FKStock_Turn379238 FOREIGN KEY (Reportid) REFERENCES Report (id);
ALTER TABLE User_Blank_Assignment ADD CONSTRAINT FKUser_Blank506842 FOREIGN KEY (Userid) REFERENCES `User` (id);
ALTER TABLE User_Blank_Assignment ADD CONSTRAINT FKUser_Blank16908 FOREIGN KEY (Blanknumber) REFERENCES Blank (number);
ALTER TABLE Payment ADD CONSTRAINT FKPayment811398 FOREIGN KEY (Currencytype) REFERENCES Currency (type);
ALTER TABLE Payment ADD CONSTRAINT FKPayment232106 FOREIGN KEY (Discounttype) REFERENCES Discount (type);
ALTER TABLE Report_Blank_Inclusion ADD CONSTRAINT FKReport_Bla560650 FOREIGN KEY (Reportid) REFERENCES Report (id);
ALTER TABLE Blank ADD CONSTRAINT FKBlank371617 FOREIGN KEY (Customerid) REFERENCES Customer (id);
