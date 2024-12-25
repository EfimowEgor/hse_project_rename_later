
CREATE TABLE Lv (
    id INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL
);

CREATE TABLE Types (
    id INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL
);

CREATE TABLE Program (
    id INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    LvID INT,
    FOREIGN KEY (LvID) REFERENCES Lv(id)
);

CREATE TABLE Students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Surname VARCHAR(255) NOT NULL,
    Patronymic VARCHAR(255)
);

CREATE TABLE Stats (
    id INT PRIMARY KEY AUTO_INCREMENT,
    StudentID INT,
    Rating VARCHAR(255),
    MeanGrade DECIMAL(4, 2),
    MinGrade DECIMAL(5, 2),
    Percentile VARCHAR(255),
    GPA DECIMAL(4, 2),
    Course INT,
    Years VARCHAR(255),
    TypeID INT,
    MODULES VARCHAR(255),
    ProgramID INT,
    FOREIGN KEY (StudentID) REFERENCES Students(id),
    FOREIGN KEY (TypeID) REFERENCES Types(id),
    FOREIGN KEY (ProgramID) REFERENCES Program(id)
);

INSERT INTO Lv (Name) VALUES
('ba'),
('ma');

INSERT INTO Types (Name) VALUES
('current'),
('cumulative'),
('grad');