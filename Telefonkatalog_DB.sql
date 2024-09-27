CREATE DATABASE telefonkatalog;
USE telefonkatalog;

CREATE TABLE personer (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fornavn VARCHAR(50),
    etternavn VARCHAR(50),
    telefonnummer VARCHAR(15)
);
