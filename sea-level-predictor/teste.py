import unittest
import sea_level_predictor
import numpy as np
import matplotlib as mpl

# Usar backend sem display para os testes
mpl.use('Agg')


class SeaLevelPlotTests(unittest.TestCase):

    def setUp(self):
        # Gera o gráfico sem exibir janela
        self.ax = sea_level_predictor.draw_plot(show=False)

    def test_title_and_labels(self):
        self.assertEqual(self.ax.get_title(), "Rise in Sea Level")
        self.assertEqual(self.ax.get_xlabel(), "Year")
        self.assertEqual(self.ax.get_ylabel(), "Sea Level (inches)")

    def test_xticks(self):
        expected_ticks = [1850.0, 1875.0, 1900.0, 1925.0,
                          1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0]
        actual_ticks = self.ax.get_xticks().tolist()
        self.assertEqual(actual_ticks, expected_ticks)

    def test_scatter_points(self):
        scatter_points = self.ax.collections[0].get_offsets().data
        first_points = scatter_points[:5].tolist()

        expected = [
            [1880.0, 0.0],
            [1881.0, 0.220472441],
            [1882.0, -0.440944881],
            [1883.0, -0.232283464],
            [1884.0, 0.590551181]
        ]

        np.testing.assert_almost_equal(first_points, expected, 7)

    def test_best_fit_lines(self):
        lines = self.ax.get_lines()
        self.assertGreaterEqual(len(lines), 2)

        xdata_first = lines[0].get_xdata()
        self.assertIn(1880, xdata_first)
        self.assertIn(2050, xdata_first)

        xdata_second = lines[1].get_xdata()
        self.assertIn(2000, xdata_second)
        self.assertIn(2050, xdata_second)

    def test_file_created(self):
        import os
        self.assertTrue(os.path.exists("sea_level_plot.png"))


if __name__ == "__main__":
    unittest.main()
