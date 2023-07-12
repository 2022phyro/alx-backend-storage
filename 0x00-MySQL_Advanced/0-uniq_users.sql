-- Intro into specializations and databases. This creates a table of users

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (id)
);
