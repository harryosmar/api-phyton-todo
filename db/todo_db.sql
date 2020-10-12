CREATE TABLE `users` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `full_name` varchar(255),
  `created_at` timestamp,
  `user_level` varchar(255)
);

CREATE TABLE `task` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `description` varchar(255),
  `deadline_date` datetime,
  `created_by` int,
  `created_date` timestamp,
  `update_by` int,
  `update_date` timestamp,
  `asign_user_id` int,
  `status` varchar(255),
  `done_date` timestamp
);

ALTER TABLE `task` ADD FOREIGN KEY (`created_by`) REFERENCES `users` (`id`);

ALTER TABLE `task` ADD FOREIGN KEY (`update_by`) REFERENCES `users` (`id`);

ALTER TABLE `task` ADD FOREIGN KEY (`asign_user_id`) REFERENCES `users` (`id`);
