DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS flags;

CREATE TABLE products (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  description TEXT NOT NULL
);

CREATE TABLE flags (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  flag TEXT NOT NULL
);

INSERT INTO products (name, description) VALUES ('Laptop', 'A powerful laptop for all your needs.');
INSERT INTO products (name, description) VALUES ('Mouse', 'A comfortable and ergonomic mouse.');
INSERT INTO products (name, a_description) VALUES ('Keyboard', 'A mechanical keyboard with RGB lighting.');

INSERT INTO flags (flag) VALUES ('ICIMS{SQL_INJ3CTI0N_IS_A_T0P_VULN}');
