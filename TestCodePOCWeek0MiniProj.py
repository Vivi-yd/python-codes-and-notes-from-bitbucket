""" Test code for 2048 by Vivi and her bf """

import poc_simpletest

line1 = [0, 0, 2, 0]
line2 = [0, 4, 4, 0]
line3 = [2, 2, 4, 0]
line4 = [0, 4, 2, 2]
line5 = [8, 16, 16, 8]
line6 = [2, 2, 2, 2]
line7 = [4, 0, 4, 0]
line8 = [0, 2, 2, 0]
line9 = [2, 2, 2, 2]
line10 = [8, 0, 3, 2, 4, 0, 3, 0, 0]
line11 = [0, 0, 2, 0, 0, 0]


def zero_to_right_test(zero_to_right):
       
    suite = poc_simpletest.TestSuite()
    
    zero_to_right_test1 = zero_to_right(line1)
    suite.run_test(str(zero_to_right_test1), str([2, 0, 0, 0]), "test 0.0.1: zero_to_right_test")
    zero_to_right_test2 = zero_to_right(line2)
    suite.run_test(str(zero_to_right_test2), str([4, 4, 0, 0]), "test 0.0.2: zero_to_right_test")
    zero_to_right_test3 = zero_to_right(line3)
    suite.run_test(str(zero_to_right_test3), str([2, 2, 4, 0]), "test 0.0.3: zero_to_right_test")
    
    suite.report_results()
        

def next_occ_test(next_occ):
    
    suite = poc_simpletest.TestSuite()
    
    next_occ_test1 = next_occ(line7, 1)
    suite.run_test(str(next_occ_test1), str(3), "test 0.1.1: next_occ_test")
    next_occ_test2 = next_occ(line8, 0)
    suite.run_test(str(next_occ_test2), str(3), "test 0.1.2: next_occ_test")
    next_occ_test3 = next_occ(line9, 0)
    suite.run_test(str(next_occ_test3), str(1), "test 0.1.3: next_occ_test")
    next_occ_test4 = next_occ(line10, 2)
    suite.run_test(str(next_occ_test4), str(6), "test 0.1.4: next_occ_test")
    
    suite.report_results()
    
    
def check_gap_test(check_gap):
    
    suite = poc_simpletest.TestSuite()
    
    check_gap_test1 = check_gap(line8, 0, 3)
    suite.run_test(str(check_gap_test1), str(True), "test 0.2.1: check_gap_test")
    check_gap_test2 = check_gap(line9, 0, 3)
    suite.run_test(str(check_gap_test2), str(True), "test 0.2.2: check_gap_test")
    check_gap_test3 = check_gap(line10, 2, 6)
    suite.run_test(str(check_gap_test3), str(True), "test 0.2.3: check_gap_test")
    check_gap_test4 = check_gap(line11, 2, 5)
    suite.run_test(str(check_gap_test4), str(False), "test 0.2.4: check_gap_test")
    
    suite.report_results()
    

def merge_test(merge):
    
    suite = poc_simpletest.TestSuite()
    
    #test merge helping function
    
    
    merged_line1 = merge(line1)
    suite.run_test(str(merged_line1), str([2, 0, 0, 0]), "test 1.1: merging lines")
    merged_line2 = merge(line2)
    suite.run_test(str(merged_line2), str([8, 0, 0, 0]), "test 1.2: merging lines")
    merged_line3 = merge(line3)
    suite.run_test(str(merged_line3), str([4, 4, 0, 0]), "test 1.3: merging lines")
    merged_line4 = merge(line4)
    suite.run_test(str(merged_line4), str([4, 4, 0, 0]), "test 1.4: merging lines")
    merged_line5 = merge(line5)
    suite.run_test(str(merged_line5), str([8, 32, 8, 0]), "test 1.5: merging lines")
    merged_line6 = merge(line6)
    suite.run_test(str(merged_line6), str([4, 4, 0, 0]), "test 1.6: merging lines")
    
    suite.report_results()     



def run_test(class_to_be_tested):
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # create a object from the class to be tested
    game = class_to_be_tested()
    pass
    
    