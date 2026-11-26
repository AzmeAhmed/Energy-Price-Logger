
CREATE TABLE cities (
city_id INT AUTO_INCREMENT PRIMARY KEY,
city_name VARCHAR(50) NOT NULL,
grid_zone VARCHAR(50) NOT NULL,
region VARCHAR(50)

);

CREATE TABLE appliances (
appliance_id INT AUTO_INCREMENT PRIMARY KEY,
appliance_name VARCHAR(100) NOT NULL,
avg_wattage INT NOT NULL,
category VARCHAR(100)
);

CREATE TABLE energy_logs (
log_id INT AUTO_INCREMENT PRIMARY KEY,
log_date DATETIME,
energy_kwh DECIMAL (10, 2),
city_id INT,
appliance_id INT,
FOREIGN KEY (city_id) REFERENCES cities(city_id),
FOREIGN KEY (appliance_id) REFERENCES appliances(appliance_id)
);
 