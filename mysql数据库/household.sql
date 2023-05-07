/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50620
Source Host           : localhost:3306
Source Database       : household

Target Server Type    : MYSQL
Target Server Version : 50620
File Encoding         : 65001

Date: 2020-08-01 15:49:02
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `auth_group`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_group_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_permission`
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add 客户信息表', '1', 'add_customer');
INSERT INTO `auth_permission` VALUES ('2', 'Can change 客户信息表', '1', 'change_customer');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete 客户信息表', '1', 'delete_customer');
INSERT INTO `auth_permission` VALUES ('4', 'Can view 客户信息表', '1', 'view_customer');
INSERT INTO `auth_permission` VALUES ('5', 'Can add 类型表', '2', 'add_type');
INSERT INTO `auth_permission` VALUES ('6', 'Can change 类型表', '2', 'change_type');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete 类型表', '2', 'delete_type');
INSERT INTO `auth_permission` VALUES ('8', 'Can view 类型表', '2', 'view_type');
INSERT INTO `auth_permission` VALUES ('9', 'Can add 用户表', '3', 'add_user');
INSERT INTO `auth_permission` VALUES ('10', 'Can change 用户表', '3', 'change_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete 用户表', '3', 'delete_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can view 用户表', '3', 'view_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add 家政人员信息表', '4', 'add_worker');
INSERT INTO `auth_permission` VALUES ('14', 'Can change 家政人员信息表', '4', 'change_worker');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete 家政人员信息表', '4', 'delete_worker');
INSERT INTO `auth_permission` VALUES ('16', 'Can view 家政人员信息表', '4', 'view_worker');
INSERT INTO `auth_permission` VALUES ('17', 'Can add 订单信息表', '5', 'add_order');
INSERT INTO `auth_permission` VALUES ('18', 'Can change 订单信息表', '5', 'change_order');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete 订单信息表', '5', 'delete_order');
INSERT INTO `auth_permission` VALUES ('20', 'Can view 订单信息表', '5', 'view_order');
INSERT INTO `auth_permission` VALUES ('21', 'Can add 财务表', '6', 'add_finance');
INSERT INTO `auth_permission` VALUES ('22', 'Can change 财务表', '6', 'change_finance');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete 财务表', '6', 'delete_finance');
INSERT INTO `auth_permission` VALUES ('24', 'Can view 财务表', '6', 'view_finance');
INSERT INTO `auth_permission` VALUES ('25', 'Can add log entry', '7', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('26', 'Can change log entry', '7', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete log entry', '7', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('28', 'Can view log entry', '7', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('29', 'Can add permission', '8', 'add_permission');
INSERT INTO `auth_permission` VALUES ('30', 'Can change permission', '8', 'change_permission');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete permission', '8', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('32', 'Can view permission', '8', 'view_permission');
INSERT INTO `auth_permission` VALUES ('33', 'Can add group', '9', 'add_group');
INSERT INTO `auth_permission` VALUES ('34', 'Can change group', '9', 'change_group');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete group', '9', 'delete_group');
INSERT INTO `auth_permission` VALUES ('36', 'Can view group', '9', 'view_group');
INSERT INTO `auth_permission` VALUES ('37', 'Can add user', '10', 'add_user');
INSERT INTO `auth_permission` VALUES ('38', 'Can change user', '10', 'change_user');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete user', '10', 'delete_user');
INSERT INTO `auth_permission` VALUES ('40', 'Can view user', '10', 'view_user');
INSERT INTO `auth_permission` VALUES ('41', 'Can add content type', '11', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('42', 'Can change content type', '11', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('43', 'Can delete content type', '11', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('44', 'Can view content type', '11', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('45', 'Can add session', '12', 'add_session');
INSERT INTO `auth_permission` VALUES ('46', 'Can change session', '12', 'change_session');
INSERT INTO `auth_permission` VALUES ('47', 'Can delete session', '12', 'delete_session');
INSERT INTO `auth_permission` VALUES ('48', 'Can view session', '12', 'view_session');

-- ----------------------------
-- Table structure for `auth_user`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$150000$3cBt9OIXNRDx$8ShiDhn9yXDCFTd3aF97xXMz8EB1VTrQYKN6zUAWTjM=', '2020-08-01 07:34:12.653887', '1', 'admin', '', '', 'admin@126.com', '1', '1', '2020-07-21 15:25:06.065665');

-- ----------------------------
-- Table structure for `auth_user_groups`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------

-- ----------------------------
-- Table structure for `auth_user_user_permissions`
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for `django_admin_log`
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2020-07-21 15:58:22.612117', '1', '2020-07-21 14:22:52', '1', '[{\"added\": {}}]', '5', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2020-08-01 07:37:23.743125', '2', '2020-08-01 11:22:33', '1', '[{\"added\": {}}]', '5', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2020-08-01 07:38:46.494470', '1', '1', '1', '[{\"added\": {}}]', '6', '1');

-- ----------------------------
-- Table structure for `django_content_type`
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('7', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('9', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('8', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('10', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('11', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('1', 'MyApp', 'customer');
INSERT INTO `django_content_type` VALUES ('6', 'MyApp', 'finance');
INSERT INTO `django_content_type` VALUES ('5', 'MyApp', 'order');
INSERT INTO `django_content_type` VALUES ('2', 'MyApp', 'type');
INSERT INTO `django_content_type` VALUES ('3', 'MyApp', 'user');
INSERT INTO `django_content_type` VALUES ('4', 'MyApp', 'worker');
INSERT INTO `django_content_type` VALUES ('12', 'sessions', 'session');

-- ----------------------------
-- Table structure for `django_migrations`
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'MyApp', '0001_initial', '2020-07-21 15:24:39.190807');
INSERT INTO `django_migrations` VALUES ('2', 'MyApp', '0002_auto_20200721_2324', '2020-07-21 15:24:39.680110');
INSERT INTO `django_migrations` VALUES ('3', 'contenttypes', '0001_initial', '2020-07-21 15:24:39.780378');
INSERT INTO `django_migrations` VALUES ('4', 'auth', '0001_initial', '2020-07-21 15:24:40.138165');
INSERT INTO `django_migrations` VALUES ('5', 'admin', '0001_initial', '2020-07-21 15:24:40.823031');
INSERT INTO `django_migrations` VALUES ('6', 'admin', '0002_logentry_remove_auto_add', '2020-07-21 15:24:40.973435');
INSERT INTO `django_migrations` VALUES ('7', 'admin', '0003_logentry_add_action_flag_choices', '2020-07-21 15:24:40.988977');
INSERT INTO `django_migrations` VALUES ('8', 'contenttypes', '0002_remove_content_type_name', '2020-07-21 15:24:41.145392');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0002_alter_permission_name_max_length', '2020-07-21 15:24:41.213073');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0003_alter_user_email_max_length', '2020-07-21 15:24:41.293704');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0004_alter_user_username_opts', '2020-07-21 15:24:41.312253');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0005_alter_user_last_login_null', '2020-07-21 15:24:41.376424');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0006_require_contenttypes_0002', '2020-07-21 15:24:41.386452');
INSERT INTO `django_migrations` VALUES ('14', 'auth', '0007_alter_validators_add_error_messages', '2020-07-21 15:24:41.402995');
INSERT INTO `django_migrations` VALUES ('15', 'auth', '0008_alter_user_username_max_length', '2020-07-21 15:24:41.480703');
INSERT INTO `django_migrations` VALUES ('16', 'auth', '0009_alter_user_last_name_max_length', '2020-07-21 15:24:41.566197');
INSERT INTO `django_migrations` VALUES ('17', 'auth', '0010_alter_group_name_max_length', '2020-07-21 15:24:41.639391');
INSERT INTO `django_migrations` VALUES ('18', 'auth', '0011_update_proxy_permissions', '2020-07-21 15:24:41.688521');
INSERT INTO `django_migrations` VALUES ('19', 'sessions', '0001_initial', '2020-07-21 15:24:41.762219');

-- ----------------------------
-- Table structure for `django_session`
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('cfoeua09y5o1ntmqx4ywixosfxxzq0zl', 'YjJkZmVkZWUwYTFjZGQ2MWU5MGNmMWNjYTdiZDUyNmY3NDljNzA4ZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzOWY3ZjQ0MmM0NzYxMGNhYmQ4NTVmNjQyMDkyOTc2NTkyNGQwYzI2In0=', '2020-08-04 15:57:08.030764');

-- ----------------------------
-- Table structure for `myapp_customer`
-- ----------------------------
DROP TABLE IF EXISTS `myapp_customer`;
CREATE TABLE `myapp_customer` (
  `customer_name` varchar(50) NOT NULL,
  `customer_sex` varchar(10) NOT NULL,
  `customer_age` varchar(10) NOT NULL,
  `customer_telephone` varchar(50) NOT NULL,
  `customer_address` varchar(50) NOT NULL,
  `customer_id` varchar(50) NOT NULL,
  PRIMARY KEY (`customer_telephone`),
  UNIQUE KEY `customer_id` (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of myapp_customer
-- ----------------------------
INSERT INTO `myapp_customer` VALUES ('王忠', '男', '20', '13688886666', '四川成都', '513030199812124253');
INSERT INTO `myapp_customer` VALUES ('王客户', '男', '23', 'cus001', '四川成都', '513030199611223598');

-- ----------------------------
-- Table structure for `myapp_finance`
-- ----------------------------
DROP TABLE IF EXISTS `myapp_finance`;
CREATE TABLE `myapp_finance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `platform_cost` double NOT NULL,
  `income` double NOT NULL,
  `order_id` int(11) NOT NULL,
  `worker_id` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `MyApp_finance_worker_id_80f38531_fk_MyApp_worker_worker_id` (`worker_id`),
  KEY `MyApp_finance_order_id_2cb71b5e_fk_MyApp_order_order_id` (`order_id`),
  CONSTRAINT `MyApp_finance_order_id_2cb71b5e_fk_MyApp_order_order_id` FOREIGN KEY (`order_id`) REFERENCES `myapp_order` (`order_id`),
  CONSTRAINT `MyApp_finance_worker_id_80f38531_fk_MyApp_worker_worker_id` FOREIGN KEY (`worker_id`) REFERENCES `myapp_worker` (`worker_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of myapp_finance
-- ----------------------------
INSERT INTO `myapp_finance` VALUES ('1', '200', '3000', '2', '1002');

-- ----------------------------
-- Table structure for `myapp_order`
-- ----------------------------
DROP TABLE IF EXISTS `myapp_order`;
CREATE TABLE `myapp_order` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_price` double NOT NULL,
  `order_time` varchar(50) NOT NULL,
  `customer_id` varchar(50) NOT NULL,
  `worker_id` varchar(50) NOT NULL,
  PRIMARY KEY (`order_id`),
  KEY `MyApp_order_customer_id_39b3d150_fk_MyApp_cus` (`customer_id`),
  KEY `MyApp_order_worker_id_7edea8f6_fk_MyApp_worker_worker_id` (`worker_id`),
  CONSTRAINT `MyApp_order_customer_id_39b3d150_fk_MyApp_cus` FOREIGN KEY (`customer_id`) REFERENCES `myapp_customer` (`customer_telephone`),
  CONSTRAINT `MyApp_order_worker_id_7edea8f6_fk_MyApp_worker_worker_id` FOREIGN KEY (`worker_id`) REFERENCES `myapp_worker` (`worker_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of myapp_order
-- ----------------------------
INSERT INTO `myapp_order` VALUES ('1', '200', '2020-07-21 14:22:52', '13688886666', '1001');
INSERT INTO `myapp_order` VALUES ('2', '3200', '2020-08-01 11:22:33', 'cus001', '1002');

-- ----------------------------
-- Table structure for `myapp_type`
-- ----------------------------
DROP TABLE IF EXISTS `myapp_type`;
CREATE TABLE `myapp_type` (
  `type_id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(50) NOT NULL,
  PRIMARY KEY (`type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of myapp_type
-- ----------------------------
INSERT INTO `myapp_type` VALUES ('1', '全职');

-- ----------------------------
-- Table structure for `myapp_user`
-- ----------------------------
DROP TABLE IF EXISTS `myapp_user`;
CREATE TABLE `myapp_user` (
  `user_telephone` varchar(50) NOT NULL,
  `user_password` varchar(50) NOT NULL,
  `user_identity` varchar(50) NOT NULL,
  PRIMARY KEY (`user_telephone`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of myapp_user
-- ----------------------------
INSERT INTO `myapp_user` VALUES ('13412345678', '123456', '员工');
INSERT INTO `myapp_user` VALUES ('13611112222', '123456', '员工');
INSERT INTO `myapp_user` VALUES ('13688886666', '123456', '客户');
INSERT INTO `myapp_user` VALUES ('cus001', '123456', '客户');

-- ----------------------------
-- Table structure for `myapp_worker`
-- ----------------------------
DROP TABLE IF EXISTS `myapp_worker`;
CREATE TABLE `myapp_worker` (
  `worker_id` varchar(50) NOT NULL,
  `worker_name` varchar(50) NOT NULL,
  `worker_sex` varchar(50) NOT NULL,
  `worker_age` varchar(50) NOT NULL,
  `worker_address` varchar(50) NOT NULL,
  `worker_idcard` varchar(50) NOT NULL,
  `worker_experience` varchar(50) NOT NULL,
  `worker_salary` varchar(50) NOT NULL,
  `worker_information` varchar(50) NOT NULL,
  `worker_telephone` varchar(50) NOT NULL,
  `worker_type_id` int(11) NOT NULL,
  PRIMARY KEY (`worker_id`),
  UNIQUE KEY `worker_telephone` (`worker_telephone`),
  KEY `MyApp_worker_worker_type_id_6a6b103f_fk_MyApp_type_type_id` (`worker_type_id`),
  CONSTRAINT `MyApp_worker_worker_type_id_6a6b103f_fk_MyApp_type_type_id` FOREIGN KEY (`worker_type_id`) REFERENCES `myapp_type` (`type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of myapp_worker
-- ----------------------------
INSERT INTO `myapp_worker` VALUES ('1001', '张轩', '男', '22', '', '513030199811241034', '', '', '', '13412345678', '1');
INSERT INTO `myapp_worker` VALUES ('1002', '李小丽', '女', '24', '', '513033199407224234', '', '', '', '13611112222', '1');
