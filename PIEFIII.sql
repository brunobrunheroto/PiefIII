/* Lógico_1: */
drop database if exists pief;

create database pief;
use pief;
CREATE TABLE Profissional (
    Nome VARCHAR(256),
    CRM VARCHAR(10) PRIMARY KEY
);

CREATE TABLE Paciente (
    Nome VARCHAR(256),
    Telefone VARCHAR(11) PRIMARY KEY
);

CREATE TABLE Atende (
    Atende_PK VARCHAR(10) NOT NULL PRIMARY KEY,
    Atende VARCHAR(256)
);

CREATE TABLE Consulta (
    fk_Profissional_CRM VARCHAR(10),
    fk_Paciente_Telefone VARCHAR(11),
    Horario TIME,
    Dia DATE,
    PRIMARY KEY (Horario, Dia, fk_Profissional_CRM, fk_Paciente_Telefone)
);

ALTER TABLE Atende ADD CONSTRAINT FK_Atende_1
    FOREIGN KEY (Atende_PK)
    REFERENCES Profissional (CRM);
 
ALTER TABLE Consulta ADD CONSTRAINT FK_Consulta_2atende
    FOREIGN KEY (fk_Profissional_CRM)
    REFERENCES Profissional (CRM)
    ON DELETE RESTRICT;
 
ALTER TABLE Consulta ADD CONSTRAINT FK_Consulta_3
    FOREIGN KEY (fk_Paciente_Telefone)
    REFERENCES Paciente (Telefone)
    ON DELETE RESTRICT;