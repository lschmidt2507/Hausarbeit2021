from linear_congruence import linear_congruence,to_range
from sign_test import  sign_test
from runs_test import runs_test, runs_test_new
from frequency_test import frequency_test
import data


linear=linear_congruence(4001,101,2**15,1,500)
f_machine = to_range(0,1,linear[400:500])
f_manual = data.t1_bin[:100] #entsprechende Folge aus data
print(frequency_test(f_machine,0,1)) #Testmethode jeweils geändert
print(frequency_test(f_manual,0,1))

