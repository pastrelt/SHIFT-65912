import sqlite3


connnection = sqlite3.connect("bank.bd")
cursor = connnection.cursor()

cursor.execute("""
INSERT INTO tbl_tariffs (name, cost) VALUES ('Тариф за выдачу кредита', 10);
INSERT INTO tbl_tariffs (name, cost) VALUES ('Тариф за открытие счета', 10);
INSERT INTO tbl_tariffs (name, cost) VALUES ('Тариф за обслуживание карты', 10);


INSERT INTO tbl_products_types (name, begin_date, end_date, tariff_ref) VALUES ('КРЕДИТ', DATE('2018-01-01'),'DD.MM.YYYY'), null, 1);
INSERT INTO tbl_products_types (name, begin_date, end_date, tariff_ref) VALUES ('ДЕПОЗИТ', DATE('2018-01-01'),'DD.MM.YYYY'), null, 2);
INSERT INTO tbl_products_types (name, begin_date, end_date, tariff_ref) VALUES ('КАРТА', DATE('2018-01-01'),'DD.MM.YYYY'), null, 3);


INSERT INTO tbl_clients (name, place_of_birth, date_of_birth, address, passport) VALUES ('Сидоров Иван Петрович', 
                                            'Россия, Московская облать, г. Пушкин', 
                                            DATE('2001-01-01'), 
                                            'Россия, Московская облать, г. Пушкин, ул. Грибоедова, д. 5', 
                                            '2222 555555, выдан ОВД г. Пушкин, 10.01.2015');
INSERT INTO tbl_clients (name, place_of_birth, date_of_birth, address, passport) VALUES ('Иванов Петр Сидорович', 
                                            'Россия, Московская облать, г. Клин', 
                                            DATE('2001-01-01'), 
                                            'Россия, Московская облать, г. Клин, ул. Мясникова, д. 3', 
                                            '4444 666666, выдан ОВД г. Клин, 10.01.2015');
INSERT INTO tbl_clients (name, place_of_birth, date_of_birth, address, passport) VALUES ('Петров Сиодр Иванович', 
                                            'Россия, Московская облать, г. Балашиха', 
                                            DATE('2001-01-01'), 
                                            'Россия, Московская облать, г. Балашиха, ул. Пушкина, д. 7', 
                                            '2222 666666, выдан ОВД г. Клин, 10.01.2015');


INSERT INTO tbl_products (name, open_date, close_date, client_ref, products_type_id) VALUES ('Кредитный договор с Сидоровым И.П.', 
                                            DATE('2015-06-01'), null, 1, 1));
INSERT INTO tbl_products (name, open_date, close_date, client_ref, products_type_id) VALUES ('Депозитный договор с Ивановым П.С.', 
                                            DATE('2017-08-01'), null, 2, 2);
INSERT INTO tbl_products (name, open_date, close_date, client_ref, products_type_id) VALUES ('Карточный договор с Петровым С.И.', 
                                            DATE('2017-08-01'), null, 3, 3);


INSERT INTO tbl_accounts (name, saldo, open_date, close_date, acc_num, client_ref, product_ref) VALUES ('Кредитный счет для Сидоровым И.П.',
                                            -2000, DATE('2015-06-01'), null, '45502810401020000022', 1, 1);
INSERT INTO tbl_accounts (name, saldo, open_date, close_date, acc_num, client_ref, product_ref) VALUES ('Депозитный счет для Ивановым П.С.',
                                            6000, DATE('2017-08-01'), null, '42301810400000000001', 2, 2);
INSERT INTO tbl_accounts (name, saldo, open_date, close_date, acc_num, client_ref, product_ref) VALUES ('Карточный счет для Петровым С.И.',
                                            8000, DATE('2017-08-01'), null, '40817810700000000001', 3, 3);


INSERT INTO tbl_records (dt, open_date, sum, acc_ref) VALUES (True, DATE('2015-06-01'), 5000, 1);
INSERT INTO tbl_records (dt, open_date, sum, acc_ref) VALUES (False, DATE('2015-07-01'), 1000, 1);
INSERT INTO tbl_records (dt, open_date, sum, acc_ref) VALUES (False, DATE('2015-08-01'), 2000, 1);
INSERT INTO tbl_records (dt, open_date, sum, acc_ref) VALUES (False, DATE('2015-09-01'), 3000, 1);
INSERT INTO tbl_records (dt, open_date, sum, acc_ref) VALUES (True, DATE('2015-10-01'), 5000, 1);
INSERT INTO tbl_records (dt, open_date, sum, acc_ref) VALUES (False, DATE('2015-10-01'), 3000, 1);

INSERT INTO tbl_records (dt, open_date, sum, acc_ref) VALUES (False, DATE('2017-08-01'), 10000, 2);
INSERT INTO tbl_records (dt, open_date, sum, acc_ref) VALUES (True, DATE('2017-08-01'), 1000, 2);
INSERT INTO tbl_records (dt, open_date, sum, acc_ref) VALUES (True, DATE('2017-09-01'), 2000, 2);
INSERT INTO tbl_records (dt, open_date, sum, acc_ref) VALUES (True, DATE('2017-10-01'), 5000, 2);
INSERT INTO tbl_records (dt, open_date, sum, acc_ref) VALUES (False, DATE('2017-11-01'), 6000, 2);

INSERT INTO tbl_records (dt, open_date, sum, acc_ref) VALUES (False, DATE('2017-09-01'), 120000, 3);
INSERT INTO tbl_records (dt, open_date, sum, acc_ref) VALUES (True, DATE('2017-10-01'), 1000, 3);
INSERT INTO tbl_records (dt, open_date, sum, acc_ref) VALUES (True, DATE('2017-10-01'), 2000, 3);
INSERT INTO tbl_records (dt, open_date, sum, acc_ref) VALUES (True, DATE('2017-010-01'), 5000, 3);
""")


connnection.commit()
connnection.close()
