BEGIN TRANSACTION;
CREATE TABLE Client (
                        ID_Client INTEGER PRIMARY KEY,
                        Name TEXT,
                        Address TEXT,
                        Data TEXT
                    );
CREATE TABLE Company (
                        ID_Company INTEGER PRIMARY KEY,
                        Name TEXT,
                        Address TEXT
                    );
CREATE TABLE Delivery (
                        ID_Delivery INTEGER PRIMARY KEY,
                        ID_Partner INTEGER,
                        ID_Product INTEGER,
                        Quantity INTEGER,
                        Date TEXT,
                        Status TEXT,
                        Delivery_Address TEXT,
                        FOREIGN KEY (ID_Partner) REFERENCES Partner(ID_Partner),
                        FOREIGN KEY (ID_Product) REFERENCES Product(ID_Product)
                    );
CREATE TABLE Orders (
                        ID_Order INTEGER PRIMARY KEY,
                        ID_Client INTEGER,
                        Date TEXT,
                        Status TEXT,
                        FOREIGN KEY (ID_Client) REFERENCES Client(ID_Client)
                    );
CREATE TABLE Partner (
                        ID_Partner INTEGER PRIMARY KEY,
                        Name TEXT,
                        Address TEXT,
                        Data TEXT,
                        ID_Company INTEGER,
                        FOREIGN KEY (ID_Company) REFERENCES Company(ID_Company)
                    );
INSERT INTO "Partner" VALUES(1,'qwe','qwe','qwe',1);
INSERT INTO "Partner" VALUES(2,'121212','1212','1212',1);
CREATE TABLE Product (
                        ID_Product INTEGER PRIMARY KEY,
                        Name TEXT,
                        Price REAL,
                        Quantity INTEGER,
                        Description TEXT,
                        ID_Company INTEGER,
                        FOREIGN KEY (ID_Company) REFERENCES Company(ID_Company)
                    );
COMMIT;
