DROP TABLE IF EXISTS transactions;

DROP TABLE IF EXISTS merchants;

DROP TABLE IF EXISTS tags;

DROP TABLE IF EXISTS budget;

CREATE TABLE budget (
    id SERIAL PRIMARY KEY,
    alloted FLOAT
);

CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE merchants (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    amount FLOAT,
    tag_id INT REFERENCES tags(id),
    merchant_id INT REFERENCES merchants(id),
    when DATE,
    description VARCHAR(255),
);