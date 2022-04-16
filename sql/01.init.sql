create database if not exists `test` default character set utf8mb4 collate utf8mb4_general_ci;

use `test`;

CREATE TABLE IF NOT EXISTS `t_student` (
  `id` varchar(50) NOT NULL COMMENT '唯一主键',
  `name` varchar(255) DEFAULT NULL COMMENT '姓名',
  `age` varchar(255) DEFAULT NULL COMMENT '年龄',
  `remark` text DEFAULT NULL COMMENT '备注，描述信息',
  `create_by` varchar(50) DEFAULT NULL COMMENT '创建人',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `update_by` varchar(50) DEFAULT NULL COMMENT '最后修改人',
  `update_time` datetime DEFAULT NULL COMMENT '最后修改时间',
  `is_deleted` tinyint(1) DEFAULT '0' COMMENT '是否删除 (true:是, false:否)',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='学生信息表';
