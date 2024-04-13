/*
 Navicat Premium Data Transfer

 Source Server         : Ankoo_anfu
 Source Server Type    : MariaDB
 Source Server Version : 100616 (10.6.16-MariaDB-0ubuntu0.22.04.1)
 Source Host           : 192.168.30.177:3306
 Source Schema         : darknet_crawler_info

 Target Server Type    : MariaDB
 Target Server Version : 100616 (10.6.16-MariaDB-0ubuntu0.22.04.1)
 File Encoding         : 65001

 Date: 11/04/2024 16:36:39
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for crawler_info
-- ----------------------------
DROP TABLE IF EXISTS `crawler_info`;
CREATE TABLE `crawler_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(255) NOT NULL COMMENT '暗网域名',
  `url` varchar(255) NOT NULL COMMENT '暗网URL',
  `release_time` datetime DEFAULT NULL COMMENT '发布时间',
  `title` varchar(255) DEFAULT NULL COMMENT '对应标题',
  `content` text NOT NULL COMMENT '发布内容',
  `add_time` datetime DEFAULT NULL ON UPDATE current_timestamp() COMMENT '添加的时间',
  PRIMARY KEY (`id`,`url`) USING BTREE
) ENGINE=MyISAM AUTO_INCREMENT=1776 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_general_ci ROW_FORMAT=DYNAMIC;

SET FOREIGN_KEY_CHECKS = 1;
