.. hginit.com (Simplified Chinese) documentation master file, created by
   sphinx-quickstart on Wed Jun 30 15:00:09 2010.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

HgInit (中文版)
============================

译者前言
-----------------

Mercurial 一款非常优秀的 DVCS, 文档也日趋齐全. 但实际上要掌握 Hg, 手头上有两本书就足够了. 一本就是你正在阅读的 `Hg Init: a Mercurial tutorial <http://hginit.com>`_, 另一本则是官方推荐的大部头 `Mercurial : The Definitive Guide <http://hgbook.red-bean.com/>`_.

Joel Spolsky 在技术写作和表达方面可谓是非常优秀. HgInit 不仅仅是扔给我们几条命令, 它深入浅出, 层层推进, 不断的融入和帮助我们理解 Hg 和 DVCS 的理念. 阅读 HgInit 会有一种同作者一起探索软件开发的复杂性及其应对策略的感觉.

相比其它教程, HgInit 是 Hg 初学者的最佳入门指导. 之后手边再放一本 "Mercurial : The Definitive Guide" 供随时查阅, 便可独步水星, 行走江湖了.


术语翻译对照表
------------------

+-----------------+-----------+----------------------------------+
| 英文术语        | 中文翻译  | 解释                             |
+=================+===========+==================================+
| ``push``        | 推送      | 对应于 ``hg push`` 动作,         |
|                 |           | 用于将变更集同步至 中央 (或其它) |
|                 |           | 版本库                           |
+-----------------+-----------+----------------------------------+
| ``pull``        | 取出/获取 | 对应于 ``hg pull`` 动作,         |
|                 |           | 用于将变更集从 中央 (或其它) 库  |
|                 |           | 同步至本地库                     |
+-----------------+-----------+----------------------------------+
| ``changeset``   | 变更集    | 指对版本库一系列的修改,          |
|                 |           | 包括 添加/删除/修改文件, 以及    |
|                 |           | 修改版本库属性, 配置等操作       |
+-----------------+-----------+----------------------------------+
| ``head``        | 版本头    | 处于变更堆栈栈顶的变更集         |
|                 |           |                                  |
|                 |           |                                  |
+-----------------+-----------+----------------------------------+
| ``tip``         | 顶端变更  | ``tip`` 可以理解为 ``head`` 的代 |
|                 |           | 号 (标签), 始终指向变更堆栈栈顶  |
+-----------------+-----------+----------------------------------+

目录索引
---------


.. toctree::
   :maxdepth: 2
   
   re-education
   groundup
   setting-up
   fixing
   merging
   architecture


* :ref:`搜索 <search>`

