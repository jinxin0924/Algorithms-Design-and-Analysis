__author__ = 'Xing'
# SampleSort类似快速排序，其基本思路是：
#
# 用P-1个分隔值（splitter），将序列分散到P个bucket（桶）中。
# 每个Processor（处理器）按照这些分隔值，把元素送到合适的bucket中。
# 对每个桶排序，归并。
# 具体过程如下：
#
# 为每个processor分配n/p个元素
# 每个processor对自己分配的元素排序
# 每个processor从自己分配的元素中选出p-1个分隔元素，将已排序元素分隔为平等的p段
# 将每个processor选出的分隔元素（共有p(p-1)个）合并，再从中选出p-1个分隔元素，将这p(p-1)个元素平分为p段
# 以上一步选出的p-1个元素为界限，每个processor分配给自己的元素划分为p段
# 每个processor将位于自己第i段的元素送到编号为i的processor
# 使用radix sort（基数排序）对这些bucket进行排序，即先对每个bucket排序，再按顺序将各个bucket中的元素收集起来。

