CREATE TABLE Сотрудник (
    id INT PRIMARY KEY
    имя VARCHAR(100) NOT NULL,
    отдел VARCHAR(100) NOT NULL,
    начальник_id INT NULL,
    FOREIGN KEY (начальник_id) REFERENCES Сотрудник(id)
);