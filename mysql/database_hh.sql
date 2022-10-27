use db;

CREATE TABLE hh(
    DateID int not null AUTO_INCREMENT,
    DateTimeNow DATETIME,
    msc_anal int,
    msc_scienist int,
    spb_anal int,
    spb_scienist int,
    PRIMARY KEY (DateID)
);
