DROP TABLE hospital_db;
CREATE DATABASE hospital_db;
\c hospital_db;

CREATE TABLE doctors (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

CREATE TABLE diseases (
    id SERIAL PRIMARY KEY,
    name TEXT,
    area TEXT,
    description TEXT
);

CREATE TABLE doctor_patient_visits (
    id SERIAL PRIMARY KEY,
    date DATE,
    doctor_id INT REFERENCES doctors ON DELETE SET NULL,
    patient_id INT REFERENCES patients ON DELETE SET NULL
);

CREATE TABLE patient_diagnoses (
    id SERIAL PRIMARY KEY,
    disease_id INT REFERENCES diseases ON DELETE SET NULL,
    visit_id INT REFERENCES doctor_patient_visits ON DELETE SET NULL
);

INSERT INTO doctors (first_name, last_name) VALUES
('John', 'Doe'),
('Sarah', 'Connor'),
('Gregory', 'House'),
('Emily', 'Blunt'),
('Michael', 'Clark');

INSERT INTO patients (first_name, last_name) VALUES
('Anna', 'Smith'),
('James', 'Wilson'),
('Laura', 'Palmer');

INSERT INTO diseases (name, area, description) VALUES
('Diabetes', 'Endocrine', 'A chronic condition that affects how the body processes blood sugar.'),
('Influenza', 'Respiratory', 'A viral infection that attacks the respiratory system.'),
('Hypertension', 'Cardiovascular', 'A condition where the blood pressure in the arteries is persistently elevated.'),
('Asthma', 'Respiratory', 'A condition in which your airways narrow and swell and may produce extra mucus.'),
('Migraine', 'Neurological', 'A neurological condition characterized by intense, debilitating headaches.');

INSERT INTO doctor_patient_visits (date, doctor_id, patient_id) VALUES
('2023-09-01', 1, 1),
('2023-09-02', 2, 2),
('2023-09-03', 3, 1),
('2023-09-04', 4, 3),
('2023-09-05', 5, 3);

INSERT INTO patient_diagnoses (disease_id, visit_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5);