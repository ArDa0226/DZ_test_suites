import unittest
import Method_unittesting
import DZ_unittesting

calsST = unittest.TestSuite()
calsST.addTest(unittest.TestLoader().loadTestsFromTestCase(Method_unittesting.TournamentTest))
calsST.addTest(unittest.TestLoader().loadTestsFromTestCase(DZ_unittesting.TestStudent))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calsST)  