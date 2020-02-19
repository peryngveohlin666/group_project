CREATE TABLE `User` (
  id         int(10) NOT NULL AUTO_INCREMENT, 
  staff_code int(10) NOT NULL UNIQUE, 
  password   int(10) NOT NULL, 
  name       varchar(255), 
  surname    varchar(255), 
  address    varchar(255), 
  agency     varchar(255) NOT NULL, 
  Groupid    int(10) NOT NULL, 
  PRIMARY KEY (id));
CREATE TABLE Permission (
  id              int(10) NOT NULL AUTO_INCREMENT, 
  codename        varchar(10) NOT NULL UNIQUE, 
  name            varchar(10) NOT NULL UNIQUE, 
  content_type_id int(10) NOT NULL UNIQUE, 
  PRIMARY KEY (id));
CREATE TABLE Blank (
  number                           int(10) NOT NULL AUTO_INCREMENT, 
  type                             int(10) NOT NULL, 
  is_sold                          bit(1) NOT NULL, 
  is_refunded                      bit(1) NOT NULL, 
  Customerid                       int(10) NOT NULL, 
  `date`                           date NOT NULL, 
  User_Blank_AssignmentUserid      int(10) NOT NULL, 
  User_Blank_AssignmentBlanknumber int(10) NOT NULL, 
  PRIMARY KEY (number), 
  UNIQUE INDEX (number));
CREATE TABLE Payment (
  Blanknumber  int(10) NOT NULL, 
  amount       int(10) NOT NULL, 
  type         bit(1) NOT NULL, 
  is_valid     bit(1) NOT NULL, 
  is_regular   bit(1) NOT NULL, 
  Currencytype int(10) NOT NULL, 
  Discounttype bit(1), 
  PRIMARY KEY (Blanknumber));
CREATE TABLE Report (
  id                 int(10) NOT NULL AUTO_INCREMENT, 
  period_from        date NOT NULL, 
  period_to          date NOT NULL, 
  created_on         date NOT NULL, 
  is_global          bit(1) NOT NULL, 
  number             int(10) NOT NULL, 
  sales_office_place varchar(255) NOT NULL, 
  PRIMARY KEY (id));
CREATE TABLE `Group` (
  id   int(10) NOT NULL AUTO_INCREMENT, 
  name varchar(255) NOT NULL UNIQUE, 
  PRIMARY KEY (id));
CREATE TABLE Report_Blank_Inclusion (
  Reportid    int(10) NOT NULL, 
  Blanknumber int(10) NOT NULL, 
  PRIMARY KEY (Reportid, 
  Blanknumber));
CREATE TABLE Group_Permissions (
  Groupid      int(10) NOT NULL UNIQUE, 
  Permissionid int(10) NOT NULL, 
  PRIMARY KEY (Groupid, 
  Permissionid));
CREATE TABLE Ticket_Stock_Turnover_Report (
  Reportid                  int(10) NOT NULL, 
  agent_received_blank_from int(10) NOT NULL, 
  agent_received_blank_to   int(10) NOT NULL, 
  agent_used_from           int(10) NOT NULL, 
  agent_used_to             int(10) NOT NULL, 
  sub_agent_from            int(10) NOT NULL, 
  sub_agent_to              int(10) NOT NULL, 
  PRIMARY KEY (Reportid));
CREATE TABLE Domestic_Sales_Report (
  Reportid                      int(10) NOT NULL, 
  fare_base_ngl                 int(10) NOT NULL, 
  fare_base_usd                 int(10) NOT NULL, 
  cash_bgl                      int(10) NOT NULL, 
  cheque_bgl                    int(10) NOT NULL, 
  invoice_bgl                   int(10) NOT NULL, 
  credit_usd                    int(10) NOT NULL, 
  taxes                         int(10) NOT NULL, 
  total_amount_paid             int(10) NOT NULL, 
  commissions_assessable_amount int(10) NOT NULL, 
  commission_rate               int(10) NOT NULL, 
  notes                         varchar(255), 
  total_net_amount_airvia       int(10) NOT NULL, 
  total_commission_amount       int(10) NOT NULL, 
  net_amounts_for_agent_debit   int(10) NOT NULL, 
  PRIMARY KEY (Reportid));
CREATE TABLE Interline_Sales_Report (
  Reportid            int(10) NOT NULL, 
  taxes_LZ            int(10) NOT NULL, 
  taxes_OTHS          int(10) NOT NULL, 
  commission_rate     int(10) NOT NULL, 
  cash                int(10) NOT NULL, 
  credit_lc           int(10) NOT NULL, 
  credit_usd          int(10) NOT NULL, 
  credit_bgl          int(10) NOT NULL, 
  non_assess_amount   int(10) NOT NULL, 
  total_net_to_airvia int(10) NOT NULL, 
  airvia_n            int(10) NOT NULL, 
  airvia_amount       int(10) NOT NULL, 
  airvia_bank_acc_no  int(10) NOT NULL, 
  airvia_doc_no       int(10) NOT NULL, 
  airvia_date         date NOT NULL, 
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
  type bit(1) NOT NULL, 
  rate int(10), 
  PRIMARY KEY (type));
CREATE TABLE Customer (
  id         int(10) NOT NULL AUTO_INCREMENT, 
  is_regular bit(1) NOT NULL, 
  is_valued  bit(1) NOT NULL, 
  name       varchar(255) NOT NULL, 
  surname    varchar(255) NOT NULL, 
  address    varchar(500), 
  PRIMARY KEY (id));
CREATE TABLE Report_User (
  Reportid          int(10) NOT NULL, 
  Userid            int(10) NOT NULL, 
  relationship_type int(10) NOT NULL, 
  PRIMARY KEY (Reportid, 
  Userid));
CREATE TABLE Global_Domestic_Sales (
  Domestic_Sales_ReportReportid int(10) NOT NULL, 
  agent_id                      int(10) NOT NULL, 
  ttl_ttk_reported_num          int(10) NOT NULL, 
  PRIMARY KEY (Domestic_Sales_ReportReportid));
CREATE TABLE Individual_Domestic_Sales_Report (
  Domestic_Sales_ReportReportid int(10) NOT NULL, 
  num_of_tickets                int(10) NOT NULL, 
  original_issued_num           int(10) NOT NULL, 
  other_details                 varchar(255), 
  airvia_n                      int(10) NOT NULL, 
  airvia_amount                 int(10) NOT NULL, 
  airvia_bank_acc               int(10) NOT NULL, 
  airvia_doc_no                 int(10) NOT NULL, 
  airvia_date                   date NOT NULL, 
  PRIMARY KEY (Domestic_Sales_ReportReportid));
CREATE TABLE Individual_Interline_Sales_Report (
  Interline_Sales_ReportReportid int(10) NOT NULL, 
  number_of_tickets              int(10) NOT NULL, 
  original_issue_no              int(10) NOT NULL, 
  fa_usd                         int(10) NOT NULL, 
  fa_usd_bgl                     int(10) NOT NULL, 
  airline_docs_no                int(10) NOT NULL, 
  airline_fc                     int(10) NOT NULL, 
  airline_pror_amnt              int(10) NOT NULL, 
  airline_cd                     int(10) NOT NULL, 
  PRIMARY KEY (Interline_Sales_ReportReportid));
CREATE TABLE Global_Interline_Sales_Report (
  Interline_Sales_ReportReportid int(10) NOT NULL, 
  advisor_no                     int(10) NOT NULL, 
  doc_no_acpns                   int(10) NOT NULL, 
  fare_amount                    int(10) NOT NULL, 
  airvia_docs                    int(10) NOT NULL, 
  airvia_fcpns                   int(10) NOT NULL, 
  airvia_prorate_amounts         int(10) NOT NULL, 
  other_airline_docs             int(10) NOT NULL, 
  other_airline_fcpns            int(10) NOT NULL, 
  other_airline_prorate_amounts  int(10) NOT NULL, 
  PRIMARY KEY (Interline_Sales_ReportReportid));
ALTER TABLE Payment ADD CONSTRAINT FKPayment981424 FOREIGN KEY (Blanknumber) REFERENCES Blank (number);
ALTER TABLE Report_Blank_Inclusion ADD CONSTRAINT FKReport_Bla496473 FOREIGN KEY (Blanknumber) REFERENCES Blank (number);
ALTER TABLE Group_Permissions ADD CONSTRAINT FKGroup_Perm423461 FOREIGN KEY (Groupid) REFERENCES `Group` (id);
ALTER TABLE Group_Permissions ADD CONSTRAINT FKGroup_Perm527187 FOREIGN KEY (Permissionid) REFERENCES Permission (id);
ALTER TABLE Domestic_Sales_Report ADD CONSTRAINT FKDomestic_S819725 FOREIGN KEY (Reportid) REFERENCES Report (id);
ALTER TABLE Interline_Sales_Report ADD CONSTRAINT FKInterline_761250 FOREIGN KEY (Reportid) REFERENCES Report (id);
ALTER TABLE Ticket_Stock_Turnover_Report ADD CONSTRAINT FKTicket_Sto281292 FOREIGN KEY (Reportid) REFERENCES Report (id);
ALTER TABLE User_Blank_Assignment ADD CONSTRAINT FKUser_Blank506842 FOREIGN KEY (Userid) REFERENCES `User` (id);
ALTER TABLE Payment ADD CONSTRAINT FKPayment811398 FOREIGN KEY (Currencytype) REFERENCES Currency (type);
ALTER TABLE Payment ADD CONSTRAINT FKPayment232106 FOREIGN KEY (Discounttype) REFERENCES Discount (type);
ALTER TABLE Report_Blank_Inclusion ADD CONSTRAINT FKReport_Bla560650 FOREIGN KEY (Reportid) REFERENCES Report (id);
ALTER TABLE Blank ADD CONSTRAINT FKBlank371617 FOREIGN KEY (Customerid) REFERENCES Customer (id);
ALTER TABLE Blank ADD CONSTRAINT FKBlank490598 FOREIGN KEY (User_Blank_AssignmentUserid, User_Blank_AssignmentBlanknumber) REFERENCES User_Blank_Assignment (Userid, Blanknumber);
ALTER TABLE `User` ADD CONSTRAINT FKUser810444 FOREIGN KEY (Groupid) REFERENCES `Group` (id);
ALTER TABLE Report_User ADD CONSTRAINT FKReport_Use649540 FOREIGN KEY (Reportid) REFERENCES Report (id);
ALTER TABLE Report_User ADD CONSTRAINT FKReport_Use116167 FOREIGN KEY (Userid) REFERENCES `User` (id);
ALTER TABLE Global_Domestic_Sales ADD CONSTRAINT FKGlobal_Dom370294 FOREIGN KEY (Domestic_Sales_ReportReportid) REFERENCES Domestic_Sales_Report (Reportid);
ALTER TABLE Individual_Domestic_Sales_Report ADD CONSTRAINT FKIndividual345877 FOREIGN KEY (Domestic_Sales_ReportReportid) REFERENCES Domestic_Sales_Report (Reportid);
ALTER TABLE Individual_Interline_Sales_Report ADD CONSTRAINT FKIndividual995737 FOREIGN KEY (Interline_Sales_ReportReportid) REFERENCES Interline_Sales_Report (Reportid);
ALTER TABLE Global_Interline_Sales_Report ADD CONSTRAINT FKGlobal_Int467036 FOREIGN KEY (Interline_Sales_ReportReportid) REFERENCES Interline_Sales_Report (Reportid);
