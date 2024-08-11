import unittest
from Runners import Runner


class TestStudent(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner = Runner("First")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50, "Distances are not equal (Расстояния не равны!)")

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner = Runner("Second")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100, "Distances are not equal (Расстояния не равны!)")

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner = Runner("Third")
        runner.walk()
        runner.run()
        self.assertEqual(runner.distance, 15, "Distances are not equal (Расстояния не равны!)")


if __name__ == '__main__':
    unittest.main()