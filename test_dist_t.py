import unittest
import dist_t

class Dist_TTestCase(unittest.TestCase):

    def test_simpsons_rule(self):
        esperado = 0.3500593153649724
        observado = dist_t.simpsons_rule(1.1, 9)
        self.assertEqual(esperado, observado)

        esperado = 0.36757414139698186
        observado = dist_t.simpsons_rule(1.1812, 10)
        self.assertEqual(esperado, observado)

        esperado = 0.49499957783050624
        observado = dist_t.simpsons_rule(2.750, 30)
        self.assertEqual(esperado, observado)

    def test__gamma(self):
        esperado = 11.63172839656745
        observado = dist_t._gamma(9/2)
        self.assertEqual(esperado, observado)

        esperado = 24
        observado = dist_t._gamma(5)
        self.assertEqual(esperado, observado)

        self.assertRaises(RecursionError, dist_t._gamma, 0)

        self.assertRaises(RecursionError, dist_t._gamma, 1.2)

    def test__dist_t(self):
        esperado = 0.20651644224485097
        observado = dist_t._dist_t(1.1, 9)
        self.assertEqual(esperado, observado)

        esperado = 0.1897111440062021
        observado = dist_t._dist_t(1.1812, 10)
        self.assertEqual(esperado, observado)

        esperado = 0.012133231326559956
        observado = dist_t._dist_t(2.75, 30)
        self.assertEqual(esperado, observado)

        esperado = 0.3956321848940978
        observado = dist_t._dist_t(0, 30)
        self.assertEqual(esperado, observado)

        self.assertRaises(RecursionError, dist_t._dist_t, 1.1, 0)

    def test__sum_simp(self):
        esperado = 8
        observado = dist_t._sum_simp(4, 0, 4, True, lambda x, y: x * 2)
        self.assertEqual(esperado, observado)

        esperado = 32
        observado = dist_t._sum_simp(4, 0, 4, False, lambda x, y: x * 2)
        self.assertEqual(esperado, observado)

        esperado = 0.6578319265634369
        observado = dist_t._sum_simp(1.1, 9, 4, True)
        self.assertEqual(esperado, observado)

        esperado = 0.3068485546214168
        observado = dist_t._sum_simp(2.75, 30, 4, True)
        self.assertEqual(esperado, observado)

        esperado = 1.4446385447299261
        observado = dist_t._sum_simp(2.75, 30, 4, False)
        self.assertEqual(esperado, observado)

    def test__simp_rule(self):
        esperado = 16
        observado = dist_t._simp_rule(4, 0, 4, lambda x, y: x * 2)
        self.assertEqual(esperado, observado)

        esperado = 0.4948287014852501
        observado = dist_t._simp_rule(2.75, 30, 4)
        self.assertEqual(esperado, observado)

        esperado = 0.4949924596382772
        observado = dist_t._simp_rule(2.75, 30, 8)
        self.assertEqual(esperado, observado)

        esperado = 0.49499957783050624
        observado = dist_t._simp_rule(2.75, 30, 16)
        self.assertEqual(esperado, observado)

        esperado = 0.49500002306732915
        observado = dist_t._simp_rule(2.75, 30, 32)
        self.assertEqual(esperado, observado)
