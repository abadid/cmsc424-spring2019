
create table organs(organ varchar(20), primary key (organ));

insert into organs (organ) values ('Heart');
insert into organs (organ) values ('Liver');
insert into organs (organ) values ('Kidney');
insert into organs (organ) values ('Lung');
insert into organs (organ) values ('Pancreas');

create table blood_type (type varchar(4), primary key (type));

insert into blood_type (type) values ('O+');
insert into blood_type (type) values ('O-');
insert into blood_type (type) values ('A+');
insert into blood_type (type) values ('A-');
insert into blood_type (type) values ('B+');
insert into blood_type (type) values ('B-');
insert into blood_type (type) values ('AB+');
insert into blood_type (type) values ('AB-');

create table doctors  (
	id SERIAL,
	name VARCHAR(20),
	specialty VARCHAR(20),
	experience INT,
    Primary key (id),
    foreign key (specialty) references organs (organ)
);


create table person (
	id SERIAL,
	first_name VARCHAR(50),
	last_name VARCHAR(50),
	birthdate DATE,
	blood_type VARCHAR(4),
	doctor_id INT,
    primary key (id),
    foreign key (blood_type) references blood_type (type),
    foreign key (doctor_id) references doctors (id)
);

create table needs (
	id INT,
	organ VARCHAR(20),
	by DATE,
	primary key (id,organ),
	foreign key (id) references person (id),
	foreign key (organ) references organs (organ)
);

create table available (
	id INT,
	organ VARCHAR(20),
	primary key (id,organ),
	foreign key (id) references person (id),
	foreign key (organ) references organs (organ)
);

insert into doctors  (name, specialty, experience) values ('Smith', 'Pancreas', 4);
insert into doctors  (name, specialty, experience) values ('Johnson', 'Heart', 8);
insert into doctors  (name, specialty, experience) values ('Williams', 'Kidney', 5);
insert into doctors  (name, specialty, experience) values ('Jones', 'Heart', 2);
insert into doctors  (name, specialty, experience) values ('Brown', 'Lung', 3);
insert into doctors  (name, specialty, experience) values ('Davis', 'Lung', 8);
insert into doctors  (name, specialty, experience) values ('Miller', 'Liver', 4);
insert into doctors  (name, specialty, experience) values ('Wilson', 'Pancreas', 5);
insert into doctors  (name, specialty, experience) values ('Moore', 'Liver', 6);
insert into doctors  (name, specialty, experience) values ('Taylor', 'Kidney', 9);
insert into doctors  (name, specialty, experience) values ('Anderson', 'Heart', 5);
insert into doctors  (name, specialty, experience) values ('Thomas', 'Liver', 1);
insert into doctors  (name, specialty, experience) values ('Jackson', 'Lung', 6);
insert into doctors  (name, specialty, experience) values ('White', 'Liver', 7);
insert into doctors  (name, specialty, experience) values ('Harris', 'Pancreas', 4);
insert into doctors  (name, specialty, experience) values ('Martin', 'Kidney', 8);
insert into doctors  (name, specialty, experience) values ('Thompson', 'Kidney', 3);
insert into doctors  (name, specialty, experience) values ('Garcia', 'Liver', 9);
insert into doctors  (name, specialty, experience) values ('Martinez', 'Kidney', 4);
insert into doctors  (name, specialty, experience) values ('Robinson', 'Lung', 4);
insert into doctors  (name, specialty, experience) values ('Clark', 'Kidney', 7);
insert into doctors  (name, specialty, experience) values ('Rodriguez', 'Liver', 7);
insert into doctors  (name, specialty, experience) values ('Lewis', 'Heart', 10);
insert into doctors  (name, specialty, experience) values ('Lee', 'Liver', 10);
insert into doctors  (name, specialty, experience) values ('Walker', 'Kidney', 1);
insert into doctors  (name, specialty, experience) values ('Hall', 'Lung', 8);
insert into doctors  (name, specialty, experience) values ('Allen', 'Pancreas', 1);
insert into doctors  (name, specialty, experience) values ('Young', 'Lung', 6);
insert into doctors  (name, specialty, experience) values ('Hernandez', 'Heart', 4);
insert into doctors  (name, specialty, experience) values ('King', 'Pancreas', 4);
insert into doctors  (name, specialty, experience) values ('Wright', 'Liver', 8);
insert into doctors  (name, specialty, experience) values ('Lopez', 'Kidney', 5);
insert into doctors  (name, specialty, experience) values ('Hill', 'Liver', 5);
insert into doctors  (name, specialty, experience) values ('Scott', 'Liver', 7);
insert into doctors  (name, specialty, experience) values ('Green', 'Lung', 9);
insert into doctors  (name, specialty, experience) values ('Adams', 'Kidney', 9);
insert into doctors  (name, specialty, experience) values ('Baker', 'Lung', 7);
insert into doctors  (name, specialty, experience) values ('Gonzalez', 'Kidney', 4);
insert into doctors  (name, specialty, experience) values ('Nelson', 'Pancreas', 2);
insert into doctors  (name, specialty, experience) values ('Carter', 'Kidney', 7);
insert into doctors  (name, specialty, experience) values ('Mitchell', 'Heart', 9);
insert into doctors  (name, specialty, experience) values ('Perez', 'Liver', 3);
insert into doctors  (name, specialty, experience) values ('Roberts', 'Liver', 7);
insert into doctors  (name, specialty, experience) values ('Turner', 'Lung', 2);
insert into doctors  (name, specialty, experience) values ('Phillips', 'Kidney', 7);
insert into doctors  (name, specialty, experience) values ('Campbell', 'Pancreas', 7);
insert into doctors  (name, specialty, experience) values ('Parker', 'Lung', 6);
insert into doctors  (name, specialty, experience) values ('Evans', 'Pancreas', 2);
insert into doctors  (name, specialty, experience) values ('Edwards', 'Pancreas', 7);
insert into doctors  (name, specialty, experience) values ('Collins', 'Heart', 3);
insert into doctors  (name, specialty, experience) values ('Stewart', 'Lung', 7);
insert into doctors  (name, specialty, experience) values ('Sanchez', 'Liver', 6);
insert into doctors  (name, specialty, experience) values ('Morris', 'Kidney', 8);
insert into doctors  (name, specialty, experience) values ('Rogers', 'Kidney', 6);
insert into doctors  (name, specialty, experience) values ('Reed', 'Heart', 4);
insert into doctors  (name, specialty, experience) values ('Cook', 'Lung', 8);
insert into doctors  (name, specialty, experience) values ('Morgan', 'Liver', 9);
insert into doctors  (name, specialty, experience) values ('Bell', 'Kidney', 6);
insert into doctors  (name, specialty, experience) values ('Murphy', 'Kidney', 6);
insert into doctors  (name, specialty, experience) values ('Bailey', 'Heart', 10);
insert into doctors  (name, specialty, experience) values ('Rivera', 'Heart', 7);
insert into doctors  (name, specialty, experience) values ('Cooper', 'Liver', 10);
insert into doctors  (name, specialty, experience) values ('Richardson', 'Kidney', 1);
insert into doctors  (name, specialty, experience) values ('Cox', 'Heart', 1);
insert into doctors  (name, specialty, experience) values ('Howard', 'Heart', 7);
insert into doctors  (name, specialty, experience) values ('Ward', 'Liver', 7);
insert into doctors  (name, specialty, experience) values ('Torres', 'Lung', 9);
insert into doctors  (name, specialty, experience) values ('Peterson', 'Kidney', 2);
insert into doctors  (name, specialty, experience) values ('Gray', 'Lung', 8);
insert into doctors  (name, specialty, experience) values ('Ramirez', 'Lung', 1);
insert into doctors  (name, specialty, experience) values ('James', 'Liver', 6);
insert into doctors  (name, specialty, experience) values ('Watson', 'Lung', 5);
insert into doctors  (name, specialty, experience) values ('Brooks', 'Liver', 10);
insert into doctors  (name, specialty, experience) values ('Kelly', 'Heart', 2);
insert into doctors  (name, specialty, experience) values ('Sanders', 'Heart', 2);
insert into doctors  (name, specialty, experience) values ('Price', 'Liver', 4);
insert into doctors  (name, specialty, experience) values ('Bennett', 'Heart', 8);
insert into doctors  (name, specialty, experience) values ('Wood', 'Liver', 4);
insert into doctors  (name, specialty, experience) values ('Barnes', 'Lung', 8);
insert into doctors  (name, specialty, experience) values ('Ross', 'Heart', 8);
insert into doctors  (name, specialty, experience) values ('Henderson', 'Lung', 4);
insert into doctors  (name, specialty, experience) values ('Coleman', 'Kidney', 3);
insert into doctors  (name, specialty, experience) values ('Jenkins', 'Pancreas', 4);
insert into doctors  (name, specialty, experience) values ('Perry', 'Heart', 1);
insert into doctors  (name, specialty, experience) values ('Powell', 'Liver', 1);
insert into doctors  (name, specialty, experience) values ('Long', 'Pancreas', 5);
insert into doctors  (name, specialty, experience) values ('Patterson', 'Heart', 2);
insert into doctors  (name, specialty, experience) values ('Hughes', 'Liver', 3);
insert into doctors  (name, specialty, experience) values ('Flores', 'Kidney', 9);
insert into doctors  (name, specialty, experience) values ('Washington', 'Lung', 1);
insert into doctors  (name, specialty, experience) values ('Butler', 'Lung', 2);
insert into doctors  (name, specialty, experience) values ('Simmons', 'Heart', 4);
insert into doctors  (name, specialty, experience) values ('Foster', 'Liver', 2);
insert into doctors  (name, specialty, experience) values ('Gonzales', 'Kidney', 4);
insert into doctors  (name, specialty, experience) values ('Bryant', 'Pancreas', 10);
insert into doctors  (name, specialty, experience) values ('Alexander', 'Pancreas', 3);
insert into doctors  (name, specialty, experience) values ('Russell', 'Pancreas', 6);
insert into doctors  (name, specialty, experience) values ('Griffin', 'Heart', 2);
insert into doctors  (name, specialty, experience) values ('Diaz', 'Liver', 5);
insert into doctors  (name, specialty, experience) values ('Hayes', 'Pancreas', 6);



insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Ric', 'Vescovini', '06/10/1961', 'A-', 31);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Jacquelyn', 'Dukes', '05/09/1976', 'B-', 49);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Dorree', 'Grimmett', '11/14/1969', 'A-', 26);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Burk', 'Aldren', '03/27/1962', 'O-', 89);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Lilia', 'Heyns', '12/16/1975', 'B-', 86);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Emmott', 'Grinikhinov', '09/09/1964', 'AB+', 4);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Danya', 'Brisland', '02/13/1969', 'A-', 78);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Archambault', 'Braune', '02/17/1966', 'O+', 9);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Bryana', 'Marran', '10/03/1969', 'O+', 99);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Lockwood', 'Trill', '07/04/1967', 'B+', 91);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Barbe', 'Udale', '05/08/1973', 'B-', 55);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Patrizius', 'Ashlee', '02/02/1961', 'B+', 40);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Donavon', 'Tolland', '06/09/1979', 'B+', 58);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Morten', 'Ricardin', '11/27/1966', 'B-', 32);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Vania', 'Gummie', '06/28/1963', 'AB+', 47);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Velvet', 'Pesic', '04/05/1968', 'B-', 100);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Tally', 'Oleszkiewicz', '03/16/1975', 'B+', 92);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Sherwood', 'Matushenko', '06/24/1980', 'B+', 85);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Alix', 'Luparti', '03/31/1961', 'AB-', 1);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Blakelee', 'D''Avaux', '05/23/1965', 'A+', 51);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Helyn', 'Baldree', '03/24/1976', 'A+', 9);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Carol', 'Lowndsborough', '05/09/1983', 'A-', 32);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Cory', 'Moberley', '04/03/1977', 'A+', 64);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Ezequiel', 'Mattis', '09/14/1978', 'B-', 13);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Kane', 'Davenhill', '07/16/1969', 'O+', 83);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Emmott', 'Frances', '05/10/1961', 'AB+', 27);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Nicolas', 'Philippsohn', '01/29/1990', 'AB+', 85);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Antonella', 'Woolbrook', '12/21/1976', 'B-', 84);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Enoch', 'Kasper', '10/05/1965', 'AB+', 86);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Puff', 'Bullingham', '02/08/1974', 'A+', 39);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Filmer', 'Thorald', '10/16/1976', 'B-', 51);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Florance', 'Godsal', '05/07/1961', 'AB-', 51);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Melicent', 'Bearham', '06/28/1969', 'O+', 14);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Romy', 'Spleving', '07/29/1988', 'B-', 3);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Connor', 'Birks', '02/27/1970', 'AB-', 3);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Lilias', 'Lockney', '01/01/1976', 'AB+', 4);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Sophie', 'Ducker', '08/31/1977', 'O+', 16);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Lila', 'Whitsey', '05/27/1968', 'B-', 92);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Jason', 'Kunzler', '06/04/1984', 'B-', 3);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Nicola', 'Zorn', '10/06/1965', 'O+', 83);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Gabrila', 'Siddaley', '01/24/1966', 'O-', 12);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Miquela', 'Moule', '03/02/1981', 'AB-', 40);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Calypso', 'Van Der Hoog', '09/01/1964', 'B+', 53);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Trevar', 'Daish', '02/28/1978', 'AB+', 72);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Shena', 'Grigoli', '04/06/1966', 'AB+', 100);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Teddy', 'Garrettson', '08/19/1969', 'B+', 88);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Trumaine', 'Polino', '08/20/1985', 'A-', 75);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Inglebert', 'Pohls', '08/08/1961', 'AB+', 81);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Felita', 'Blastock', '05/05/1979', 'O+', 80);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Tamqrah', 'Hartop', '03/30/1967', 'AB+', 63);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Yorke', 'Cobby', '11/17/1982', 'A-', 81);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Quintus', 'Kik', '05/12/1977', 'O+', 82);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Oriana', 'Kunzel', '09/09/1977', 'O-', 1);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Cordie', 'Jeanel', '08/13/1970', 'AB+', 71);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Murray', 'Clipston', '01/06/1976', 'AB+', 35);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Cozmo', 'Preskett', '06/22/1970', 'B-', 28);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Dave', 'Foltin', '05/02/1974', 'AB-', 1);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Susie', 'Bills', '12/26/1979', 'AB+', 64);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Benny', 'Schober', '03/23/1977', 'O-', 99);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Lesly', 'Phizacklea', '02/03/1972', 'AB-', 59);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Dacia', 'Normanvill', '04/10/1966', 'A-', 67);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Quincey', 'Applin', '07/01/1961', 'B+', 19);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Rene', 'Lansdale', '03/15/1982', 'A+', 36);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Constantin', 'Adamoli', '11/22/1962', 'B-', 90);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Nathanial', 'Lindmark', '08/12/1960', 'O+', 29);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Chalmers', 'Gamlen', '07/01/1987', 'B+', 58);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Sybyl', 'Grutchfield', '04/08/1986', 'O+', 28);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Carmelita', 'King', '09/12/1979', 'AB+', 45);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Gayel', 'Fetters', '03/23/1964', 'O-', 79);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Dorette', 'McMoyer', '05/18/1980', 'AB-', 28);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Gerald', 'Hildred', '12/12/1975', 'B-', 40);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Norean', 'Paolino', '06/02/1983', 'A+', 8);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Tally', 'Samways', '09/03/1968', 'B+', 88);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Rickard', 'Disbrow', '08/26/1988', 'B+', 98);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Yancy', 'Burston', '06/10/1971', 'A-', 53);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Krishnah', 'Szymoni', '07/09/1964', 'A+', 93);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Beatrisa', 'Cocking', '06/29/1961', 'O+', 60);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Farrel', 'Billborough', '10/10/1965', 'O-', 67);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Alexander', 'Rennox', '06/28/1960', 'AB+', 14);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Glenda', 'Polet', '10/13/1961', 'A-', 24);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Felicle', 'McMonnies', '01/17/1961', 'O+', 21);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Ddene', 'Murrell', '11/24/1962', 'AB+', 100);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Heall', 'Jerrolt', '04/26/1985', 'AB+', 30);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Emmit', 'Whotton', '12/03/1966', 'AB-', 6);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Portia', 'Fishly', '09/09/1973', 'A+', 42);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Jaclyn', 'Dodle', '03/20/1962', 'O+', 75);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Cinnamon', 'Ramsay', '04/15/1977', 'AB+', 94);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Andrew', 'McHardy', '10/14/1974', 'A-', 44);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Edwina', 'Teasdale-Markie', '12/11/1968', 'A-', 5);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Mufinella', 'Laite', '08/24/1977', 'B+', 58);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Tobe', 'Stratiff', '06/13/1968', 'B-', 20);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Evania', 'Keward', '04/24/1969', 'O-', 19);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Melinde', 'Slograve', '02/06/1964', 'A-', 90);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Courtnay', 'Brundrett', '01/29/1973', 'A+', 67);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Cly', 'Jindrich', '04/27/1977', 'AB-', 68);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Viv', 'Bridgwood', '09/25/1968', 'O+', 54);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Erena', 'Urpeth', '12/29/1988', 'B+', 92);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Shaughn', 'Martinolli', '09/08/1981', 'AB-', 6);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Margaretta', 'Northam', '10/25/1989', 'B-', 96);
insert into person (first_name, last_name, birthdate, blood_type, doctor_id) values ('Burr', 'Kadwallider', '02/13/1988', 'AB+', 94);

insert into needs (id, organ, by) values (20, 'Kidney', '10/15/2025');
insert into needs (id, organ, by) values (41, 'Heart', '06/30/2022');
insert into needs (id, organ, by) values (96, 'Lung', '05/01/2023');
insert into needs (id, organ, by) values (6, 'Heart', '10/23/2024');
insert into needs (id, organ, by) values (89, 'Heart', '01/22/2026');
insert into needs (id, organ, by) values (23, 'Kidney', '08/01/2023');
insert into needs (id, organ, by) values (32, 'Liver', '06/20/2023');
insert into needs (id, organ, by) values (65, 'Lung', '05/13/2025');
insert into needs (id, organ, by) values (86, 'Kidney', '01/21/2025');
insert into needs (id, organ, by) values (10, 'Liver', '08/25/2023');
insert into needs (id, organ, by) values (31, 'Kidney', '11/24/2023');
insert into needs (id, organ, by) values (3, 'Heart', '08/28/2022');
insert into needs (id, organ, by) values (91, 'Heart', '08/15/2022');
insert into needs (id, organ, by) values (59, 'Kidney', '03/14/2025');
insert into needs (id, organ, by) values (12, 'Kidney', '03/31/2025');
insert into needs (id, organ, by) values (85, 'Heart', '05/03/2025');
insert into needs (id, organ, by) values (39, 'Heart', '12/05/2023');
insert into needs (id, organ, by) values (45, 'Lung', '06/28/2023');
insert into needs (id, organ, by) values (14, 'Heart', '01/15/2025');
insert into needs (id, organ, by) values (88, 'Lung', '02/07/2024');
insert into needs (id, organ, by) values (18, 'Heart', '01/03/2025');
insert into needs (id, organ, by) values (5, 'Pancreas', '01/05/2026');
insert into needs (id, organ, by) values (12, 'Liver', '09/01/2022');
insert into needs (id, organ, by) values (49, 'Lung', '02/05/2024');
insert into needs (id, organ, by) values (9, 'Pancreas', '11/17/2022');
insert into needs (id, organ, by) values (29, 'Lung', '07/28/2022');
insert into needs (id, organ, by) values (74, 'Liver', '06/14/2023');
insert into needs (id, organ, by) values (64, 'Kidney', '09/14/2025');
insert into needs (id, organ, by) values (7, 'Pancreas', '01/09/2023');
insert into needs (id, organ, by) values (100, 'Kidney', '12/15/2023');
insert into needs (id, organ, by) values (61, 'Kidney', '01/03/2025');
insert into needs (id, organ, by) values (27, 'Lung', '04/05/2024');
insert into needs (id, organ, by) values (39, 'Pancreas', '12/30/2024');
insert into needs (id, organ, by) values (19, 'Pancreas', '09/29/2022');
insert into needs (id, organ, by) values (29, 'Heart', '01/12/2023');
insert into needs (id, organ, by) values (36, 'Liver', '06/03/2023');
insert into needs (id, organ, by) values (20, 'Pancreas', '10/17/2024');
insert into needs (id, organ, by) values (91, 'Liver', '04/14/2023');
insert into needs (id, organ, by) values (93, 'Kidney', '08/19/2022');
insert into needs (id, organ, by) values (56, 'Pancreas', '05/10/2025');
insert into needs (id, organ, by) values (31, 'Pancreas', '08/04/2022');
insert into needs (id, organ, by) values (59, 'Pancreas', '02/25/2026');
insert into needs (id, organ, by) values (69, 'Pancreas', '05/25/2022');
insert into needs (id, organ, by) values (73, 'Pancreas', '11/21/2025');
insert into needs (id, organ, by) values (69, 'Kidney', '01/30/2026');
insert into needs (id, organ, by) values (17, 'Heart', '10/19/2025');
insert into needs (id, organ, by) values (57, 'Liver', '11/05/2025');
insert into needs (id, organ, by) values (91, 'Lung', '05/18/2025');

insert into available (id, organ) values (37, 'Heart');
insert into available (id, organ) values (27, 'Heart');
insert into available (id, organ) values (90, 'Heart');
insert into available (id, organ) values (50, 'Heart');
insert into available (id, organ) values (59, 'Kidney');
insert into available (id, organ) values (24, 'Pancreas');
insert into available (id, organ) values (75, 'Heart');
insert into available (id, organ) values (82, 'Kidney');
insert into available (id, organ) values (14, 'Lung');
insert into available (id, organ) values (84, 'Heart');
insert into available (id, organ) values (53, 'Pancreas');
insert into available (id, organ) values (3, 'Heart');
insert into available (id, organ) values (85, 'Pancreas');
insert into available (id, organ) values (86, 'Heart');
insert into available (id, organ) values (17, 'Lung');
insert into available (id, organ) values (57, 'Lung');
insert into available (id, organ) values (9, 'Liver');
insert into available (id, organ) values (16, 'Lung');
insert into available (id, organ) values (27, 'Liver');
insert into available (id, organ) values (7, 'Pancreas');
insert into available (id, organ) values (36, 'Heart');
insert into available (id, organ) values (5, 'Lung');
insert into available (id, organ) values (23, 'Lung');
insert into available (id, organ) values (50, 'Pancreas');
insert into available (id, organ) values (49, 'Kidney');
insert into available (id, organ) values (16, 'Heart');
insert into available (id, organ) values (32, 'Kidney');
insert into available (id, organ) values (29, 'Pancreas');
insert into available (id, organ) values (64, 'Lung');
insert into available (id, organ) values (96, 'Liver');
insert into available (id, organ) values (66, 'Pancreas');
insert into available (id, organ) values (60, 'Lung');
insert into available (id, organ) values (33, 'Liver');
insert into available (id, organ) values (89, 'Liver');
insert into available (id, organ) values (28, 'Heart');
insert into available (id, organ) values (58, 'Lung');
insert into available (id, organ) values (96, 'Lung');
insert into available (id, organ) values (9, 'Pancreas');
insert into available (id, organ) values (27, 'Kidney');
insert into available (id, organ) values (45, 'Kidney');
insert into available (id, organ) values (43, 'Liver');
insert into available (id, organ) values (52, 'Kidney');
insert into available (id, organ) values (60, 'Heart');
insert into available (id, organ) values (54, 'Heart');
insert into available (id, organ) values (74, 'Liver');
insert into available (id, organ) values (38, 'Lung');
insert into available (id, organ) values (39, 'Pancreas');
