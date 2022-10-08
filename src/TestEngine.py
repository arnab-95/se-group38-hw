from . import utils
import random
import test.test_code

#This is the Test Engine file
class TestEngine:
    def runs(self, k):
        status = False
        out = False
        error="None"
        testEG=test.test_code.TestEG()
        k_fun = getattr(testEG, k)
        if not k_fun:
            return
        #Reset seed
        random.seed(utils.the['seed'])

        #Cache the default settings
        old = {}
        for key in utils.the:
            old[key] = utils.the[key]

        #Print error messages or stack dumps as required
        if utils.the['dump']:
            status = True
            out = k_fun()
        else:
            try:
                out = k_fun()
                status = True
            except Exception as e:
                status = False
                error=str(e)

        #Restore settings after test
        for key in old:
            utils.the[key] = old[key]

        msg = ("PASS" if out == True else "FAIL") if status == True else "CRASH"

        print(msg)
        print(k)
        print("Status is "+str(status))
        print("Error is "+error)

        return out
