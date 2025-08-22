DROP TABLE IF EXISTS users;

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL,
  password TEXT NOT NULL
);

INSERT INTO users (username, password) VALUES ('admin', 'T1M3_B453D_BL1ND');
INSERT INTO users (username, password) VALUES ('user', 'password123');
