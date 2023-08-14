CREATE TABLE `accounts_type` (
  `accounts_types_code` varchar(255) PRIMARY KEY,
  `accounts_types_description` varchar(255)
);

CREATE TABLE `accounts` (
  `id` int PRIMARY KEY,
  `accounts_name` varchar(255),
  `date_opened` date,
  `details` varchar(255),
  `account_types_code` int,
  `account_wallet` int
);

CREATE TABLE `accounts_detail` (
  `id` int PRIMARY KEY,
  `name` varchar(255),
  `age` int,
  `phone` varchar(255),
  `email` varchar(255),
  `last_login` varchar(255),
  `description` varchar(255)
);

CREATE TABLE `wallet` (
  `id` int PRIMARY KEY,
  `amount` int
);

CREATE TABLE `transaction_types` (
  `transaction_types_code` varchar(255) PRIMARY KEY,
  `transaction_types_description` varchar(255)
);

CREATE TABLE `transactions` (
  `id` int PRIMARY KEY,
  `date` date,
  `amount` float,
  `account` int,
  `transaction_to` int_null,
  `transaction_type` varchar(255)
);

ALTER TABLE `accounts_type` ADD FOREIGN KEY (`accounts_types_code`) REFERENCES `accounts` (`account_types_code`);

ALTER TABLE `accounts_detail` ADD FOREIGN KEY (`id`) REFERENCES `accounts` (`details`);

ALTER TABLE `wallet` ADD FOREIGN KEY (`id`) REFERENCES `accounts` (`account_wallet`);

ALTER TABLE `accounts` ADD FOREIGN KEY (`id`) REFERENCES `transactions` (`account`);

ALTER TABLE `transaction_types` ADD FOREIGN KEY (`transaction_types_code`) REFERENCES `transactions` (`transaction_type`);
