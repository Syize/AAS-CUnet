# -*- coding: utf-8 -*-
# @Author: Taurus_Moon
# @Date:   2019-04-16 08:44:59
# @Last Modified by:   Taurus_Moon
# @Last Modified time: 2019-04-16 09:13:06
# @Version : 1.0
# @Description : Logging


def write_Score(file_Name,iteration,training_Loss,test_Loss,EC_mse,cor_Mae,EC_Mae,time_used,time_now):

	with open(file_Name,"a") as f:
		f.write("{0:^8}\t{1:^8.4f}\t{2:^8.4f}\t{3:^8.4f}\t{4:^8.4f}\t{5:^8.4f}\t{6:^8.6f}\t{7:^8}\n".format(iteration,training_Loss,
                                                                                                        test_Loss,EC_mse,cor_Mae,EC_Mae,
                                                                                                        time_used,time_now))

