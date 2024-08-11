import r_and_t
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def setUp(self):
        self.first = r_and_t.Runner('Усейн', 10)
        self.second = r_and_t.Runner('Андрей', 9)
        self.third = r_and_t.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for test_k, test_v in cls.all_results.items():
            print(f'Test: {test_k}')
            for k, v in test_v.items():
                print(f'\t{k}: {v.name}')

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_1(self):
        t1 = r_and_t.Tournament(90, self.first, self.third)
        result = t1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Тест 1-го турнира'] = result

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_2(self):
        t2 = r_and_t.Tournament(90, self.second, self.third)
        result = t2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Тест 2-го турнира'] = result

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_3(self):
        t3 = r_and_t.Tournament(90, self.first,
                                self.second, self.third)
        result = t3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results['Тест 3-го турнира'] = result

    if __name__ == '__main__':
        unittest.main()


