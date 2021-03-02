{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Collecting Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Nama</th>\n",
       "      <th>PAPI</th>\n",
       "      <th>Admission</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Dominance</th>\n",
       "      <th>Influence</th>\n",
       "      <th>Steadiness</th>\n",
       "      <th>Conscientious</th>\n",
       "      <th>Inisiatif</th>\n",
       "      <th>Motivasi</th>\n",
       "      <th>Jiwa Kepemimpinan</th>\n",
       "      <th>Kepemimpinan</th>\n",
       "      <th>Kerjasama</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Dedi andrianto</td>\n",
       "      <td>7</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Laki-laki</td>\n",
       "      <td>0.28</td>\n",
       "      <td>0.10</td>\n",
       "      <td>0.18</td>\n",
       "      <td>0.12</td>\n",
       "      <td>Inisiatif dan kreatifitas tinggi</td>\n",
       "      <td>Motivasi kuat</td>\n",
       "      <td>Tinggi</td>\n",
       "      <td>Pemimpin yang baik</td>\n",
       "      <td>Nilai kerjasama tim baik</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>roy aditya putra</td>\n",
       "      <td>8</td>\n",
       "      <td>0.0</td>\n",
       "      <td>Laki-laki</td>\n",
       "      <td>0.23</td>\n",
       "      <td>0.18</td>\n",
       "      <td>0.26</td>\n",
       "      <td>0.18</td>\n",
       "      <td>Inisiatif dan kreatifitas tinggi</td>\n",
       "      <td>Masih ragu-ragu</td>\n",
       "      <td>Tinggi</td>\n",
       "      <td>Cukup</td>\n",
       "      <td>Nilai kerjasama tim baik</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>dimas angga</td>\n",
       "      <td>5</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Laki-laki</td>\n",
       "      <td>0.16</td>\n",
       "      <td>0.18</td>\n",
       "      <td>0.26</td>\n",
       "      <td>0.24</td>\n",
       "      <td>Inisiatif dan kreatifitas sedang</td>\n",
       "      <td>Masih ragu-ragu</td>\n",
       "      <td>Tinggi</td>\n",
       "      <td>Cukup</td>\n",
       "      <td>Nilai kerjasama tim sedang</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>nur aini</td>\n",
       "      <td>4</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Perempuan</td>\n",
       "      <td>0.25</td>\n",
       "      <td>0.25</td>\n",
       "      <td>0.18</td>\n",
       "      <td>0.18</td>\n",
       "      <td>Inisiatif dan kreatifitas tinggi</td>\n",
       "      <td>Motivasi kuat</td>\n",
       "      <td>Tinggi</td>\n",
       "      <td>Pemimpin yang baik</td>\n",
       "      <td>Nilai kerjasama tim baik</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>tiara nur annisa</td>\n",
       "      <td>8</td>\n",
       "      <td>0.0</td>\n",
       "      <td>Perempuan</td>\n",
       "      <td>0.13</td>\n",
       "      <td>0.29</td>\n",
       "      <td>0.17</td>\n",
       "      <td>0.25</td>\n",
       "      <td>Inisiatif dan kreatifitas sedang</td>\n",
       "      <td>Motivasi kuat</td>\n",
       "      <td>Sangat tinggi</td>\n",
       "      <td>Cukup</td>\n",
       "      <td>Nilai kerjasama tim baik</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>muhammad wahyu</td>\n",
       "      <td>8</td>\n",
       "      <td>0.0</td>\n",
       "      <td>Laki-laki</td>\n",
       "      <td>0.18</td>\n",
       "      <td>0.16</td>\n",
       "      <td>0.29</td>\n",
       "      <td>0.21</td>\n",
       "      <td>Inisiatif dan kreatifitas sedang</td>\n",
       "      <td>Masih ragu-ragu</td>\n",
       "      <td>Tinggi</td>\n",
       "      <td>Masih perlu pengembangan</td>\n",
       "      <td>Nilai kerjasama tim sedang</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>ludfi aprilia</td>\n",
       "      <td>8</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Perempuan</td>\n",
       "      <td>0.17</td>\n",
       "      <td>0.25</td>\n",
       "      <td>0.23</td>\n",
       "      <td>0.29</td>\n",
       "      <td>Inisiatif dan kreatifitas sedang</td>\n",
       "      <td>Masih ragu-ragu</td>\n",
       "      <td>Tinggi</td>\n",
       "      <td>Masih perlu pengembangan</td>\n",
       "      <td>Nilai kerjasama tim buruk</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>bre anoraga</td>\n",
       "      <td>8</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Laki-laki</td>\n",
       "      <td>0.16</td>\n",
       "      <td>0.18</td>\n",
       "      <td>0.26</td>\n",
       "      <td>0.24</td>\n",
       "      <td>Inisiatif dan kreatifitas sedang</td>\n",
       "      <td>Masih ragu-ragu</td>\n",
       "      <td>Tinggi</td>\n",
       "      <td>Pemimpin yang baik</td>\n",
       "      <td>Nilai kerjasama tim baik</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>fatahial untung</td>\n",
       "      <td>5</td>\n",
       "      <td>0.0</td>\n",
       "      <td>Laki-laki</td>\n",
       "      <td>0.24</td>\n",
       "      <td>0.16</td>\n",
       "      <td>0.19</td>\n",
       "      <td>0.26</td>\n",
       "      <td>Inisiatif dan kreatifitas rendah</td>\n",
       "      <td>Masih ragu-ragu</td>\n",
       "      <td>Tinggi</td>\n",
       "      <td>Cukup</td>\n",
       "      <td>Nilai kerjasama tim baik</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>sasa aprilina</td>\n",
       "      <td>6</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Perempuan</td>\n",
       "      <td>0.29</td>\n",
       "      <td>0.15</td>\n",
       "      <td>0.19</td>\n",
       "      <td>0.26</td>\n",
       "      <td>Inisiatif dan kreatifitas sedang</td>\n",
       "      <td>Masih ragu-ragu</td>\n",
       "      <td>Tinggi</td>\n",
       "      <td>Cukup</td>\n",
       "      <td>Nilai kerjasama tim sedang</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                Nama  PAPI  Admission     Gender  Dominance  Influence  \\\n",
       "0    Dedi andrianto      7        1.0  Laki-laki       0.28       0.10   \n",
       "1   roy aditya putra     8        0.0  Laki-laki       0.23       0.18   \n",
       "2       dimas angga      5        NaN  Laki-laki       0.16       0.18   \n",
       "3           nur aini     4        1.0  Perempuan       0.25       0.25   \n",
       "4  tiara nur annisa      8        0.0  Perempuan       0.13       0.29   \n",
       "5     muhammad wahyu     8        0.0  Laki-laki       0.18       0.16   \n",
       "6     ludfi aprilia      8        1.0  Perempuan       0.17       0.25   \n",
       "7        bre anoraga     8        NaN  Laki-laki       0.16       0.18   \n",
       "8   fatahial untung      5        0.0  Laki-laki       0.24       0.16   \n",
       "9     sasa aprilina      6        1.0  Perempuan       0.29       0.15   \n",
       "\n",
       "   Steadiness  Conscientious                          Inisiatif  \\\n",
       "0        0.18           0.12  Inisiatif dan kreatifitas tinggi    \n",
       "1        0.26           0.18  Inisiatif dan kreatifitas tinggi    \n",
       "2        0.26           0.24  Inisiatif dan kreatifitas sedang    \n",
       "3        0.18           0.18  Inisiatif dan kreatifitas tinggi    \n",
       "4        0.17           0.25  Inisiatif dan kreatifitas sedang    \n",
       "5        0.29           0.21  Inisiatif dan kreatifitas sedang    \n",
       "6        0.23           0.29  Inisiatif dan kreatifitas sedang    \n",
       "7        0.26           0.24  Inisiatif dan kreatifitas sedang    \n",
       "8        0.19           0.26  Inisiatif dan kreatifitas rendah    \n",
       "9        0.19           0.26  Inisiatif dan kreatifitas sedang    \n",
       "\n",
       "           Motivasi Jiwa Kepemimpinan               Kepemimpinan  \\\n",
       "0    Motivasi kuat             Tinggi        Pemimpin yang baik    \n",
       "1  Masih ragu-ragu             Tinggi                     Cukup    \n",
       "2  Masih ragu-ragu             Tinggi                     Cukup    \n",
       "3    Motivasi kuat             Tinggi        Pemimpin yang baik    \n",
       "4    Motivasi kuat     Sangat tinggi                      Cukup    \n",
       "5  Masih ragu-ragu             Tinggi  Masih perlu pengembangan    \n",
       "6  Masih ragu-ragu             Tinggi  Masih perlu pengembangan    \n",
       "7  Masih ragu-ragu             Tinggi        Pemimpin yang baik    \n",
       "8  Masih ragu-ragu             Tinggi                     Cukup    \n",
       "9  Masih ragu-ragu             Tinggi                     Cukup    \n",
       "\n",
       "                    Kerjasama  \n",
       "0   Nilai kerjasama tim baik   \n",
       "1   Nilai kerjasama tim baik   \n",
       "2  Nilai kerjasama tim sedang  \n",
       "3   Nilai kerjasama tim baik   \n",
       "4   Nilai kerjasama tim baik   \n",
       "5  Nilai kerjasama tim sedang  \n",
       "6  Nilai kerjasama tim buruk   \n",
       "7   Nilai kerjasama tim baik   \n",
       "8   Nilai kerjasama tim baik   \n",
       "9  Nilai kerjasama tim sedang  "
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "% matplotlib inline\n",
    "import math\n",
    "\n",
    "Psycho_data= pd.read_csv(\"Data_Psycho.csv\")\n",
    "Psycho_data.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Jumlah Karyawan yang dianalisis:18\n"
     ]
    }
   ],
   "source": [
    "print(\"Jumlah Karyawan yang dianalisis:\" +str(len(Psycho_data.index)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Analyzing Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x9719050>"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x=\"Gender\", data=Psycho_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x97419f0>"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x=\"Admission\", data=Psycho_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x9773e10>"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x=\"Admission\", hue=\"Gender\", data=Psycho_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x97ad990>"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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dNNN5OTkkJWVRffu3QE4//zzyc3NJT09nWHDhvGDH/wgpjry8vIYNmwYnTp1orCwkOzsbK688kouvfRScnNzATh48CA333wzZWVluHv0BfPKbrrpJkaPHs2rr77KU089FdPckydP5q677iIzM5Ps7GwyMzNp164dF110EdOnT6d379507tyZtLQ02rVrF9OYjUHtkeNM7ZHrTu2RJd6OHTvG0aNHSU5OZtu2bQwcOJBPPvmEli1bcujQIVq3bk15eTkjR47k7rvvZuTIkQ0yb33bI+sIX0Skjg4fPkz//v05evQo7s4zzzxDy5YtgYrTL999913KysoYPHgwt9xyS5yr/RcFvohIHbVp04aaViPifa59bfSirYhISCjwRURCQoEvIhISCnwRkZDQi7aS8Br61NZYTjtVe+SGE+/2yPUxY8aMKn14mjoFvkhA1B45NvFujxwmWtIRqQe1R07s9sgA7733HllZWWRlZZGdnR1ts/DYY49F70Pl8R599FEuv/xyBg0axMcffxy9/te//jU9e/bkqquuYtSoURw+fDj6e77nnnvo06cPl156afR3fvz4cSZPnsyVV17J8OHDueGGG86o3UVd6AhfpJ7UHjlx2yNDxXnzc+bMITc3l0OHDpGcnMzSpUv59NNPWbNmDe7OiBEjWLlyJa1atWLBggUUFxdTXl5Ojx49uPrqq4GKrpoTJ04E4Cc/+Qnz5s1j6tSpAHzxxResWrWKrVu3MmLECEaPHs3LL79MaWkpGzZsYM+ePVxxxRXR31NQdIQvUk9qj5zY7ZFzc3O59957efLJJ9m/fz8tWrRg6dKlLF26lOzsbHr06MHWrVv59NNPef/99xk5ciTnnHMObdu2ZcSIEdFxNm7cyLXXXktGRgbz58+v8tjecsstNGvWjLS0tOh9XrVqFbfeeivNmjXjwgsvbJSlOQW+SD3F2h65X79+zJkzhwkTJlTZfqJt8aJFi9iwYQMTJ04MtD1yTfPE2h45OTmZ4uLiKtdX1x65pKSEkpISPv/8cwYPHsz8+fOj7ZFLSkq44IILGrw98rJly1i/fj033nhjlfbIo0aN4pVXXmHo0KGn3PaBBx7gueee48iRI1xzzTVs3boVd+fHP/5x9D589tlnfO973wOqf2yhYulm9uzZbNiwgYceeqjax/bE41P5e2NS4IsETO2Rm3Z75G3b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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x=\"Admission\", hue=\"Inisiatif\", data=Psycho_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x97ea690>"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x=\"Admission\", hue=\"PAPI\", data=Psycho_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0xa80a1f0>"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXwAAAEKCAYAAAARnO4WAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMi4zLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvIxREBQAAF8NJREFUeJzt3XuUVeWZ5/HvI2BAwJgJxBARSjOkUREL5BbEKEwywUuIF+SiRpP0iNdoM9GMca0AMcuMMUyMSTqD2J1WMTEYHROMmoQVxUvUmALKErGNGayRGm1FVJRpkds7f9ShLBGKA5xdt/f7WasW57L3fp9TnPWrfd6z97MjpYQkqfPbp60LkCS1DgNfkjJh4EtSJgx8ScqEgS9JmTDwJSkTBr4kZcLAl6RMGPiSlImubV1Ac3369ElVVVVtXYYkdRhLly59LaXUt5xl21XgV1VVUVNT09ZlSFKHERH/p9xlndKRpEwY+JKUCQNfkjLRrubwJe25TZs20dDQwIYNG9q6FBWge/fu9O/fn27duu3xNgx8qZNoaGigd+/eVFVVERFtXY4qKKXE2rVraWho4JBDDtnj7RQa+BFRD7wNbAE2p5RGFDmelLMNGzYY9p1URPDRj36UNWvW7NV2WmMPf3xK6bVWGEfKnmHfeVXi/9YvbSUpE0UHfgL+EBFLI2JGwWNJaucigi996UtN9zdv3kzfvn05+eSTW1xvyZIlPPbYY033582bx6233lqxuhYtWsS1115bse21V0VP6RyTUnopIj4GLI6If00pPdx8gdIfghkAAwYMKLicfLx49ZFtXUK7MWDW021dgkp69uzJihUreOedd+jRoweLFy/moIMO2uV6S5YsoVevXowdOxaACy64oKJ1TZo0iUmTJlV0m+1RoXv4KaWXSv++CtwNjNrBMvNTSiNSSiP69i2rHYSkDuyEE07g3nvvBeD2229n+vTpTc+9/vrrnHLKKQwdOpQxY8ZQV1dHfX098+bN4/rrr6e6uppHHnmEOXPmMHfuXJ599llGjXovVurr6xk6dCgAV199NSNHjmTIkCHMmDGDlBIAP/rRjzj88MMZOnQo06ZNA+Dmm2/mkksuaa1fQZspLPAjomdE9N52G/jPwIqixpPUMUybNo1f/vKXbNiwgbq6OkaPHt303OzZsxk2bBh1dXV897vf5ZxzzqGqqooLLriAmTNnUltby7HHHtu0/GGHHcbGjRtZtWoVAAsXLmTKlCkAXHLJJfzlL39p+kTx29/+FoBrr72W5cuXU1dXx7x581rxlbe9IvfwDwQejYingCeBe1NKvytwPEkdwNChQ6mvr+f222/nxBNPfN9zjz76aNMc/4QJE1i7di3r1q1rcXtTpkzhjjvuABoDf+rUqQA8+OCDjB49miOPPJIHHniAZ555pmn8s846i9tuu42uXfM6FamwwE8prUopHVX6OSKldE1RY0nqWCZNmsTll1/+vukcoGnapbldHY44depU7rjjDv76178SEQwaNIgNGzZw0UUXceedd/L0009z3nnnNZ2BfO+993LxxRezdOlSjj76aDZv3ly5F9bOeVimpFb31a9+lVmzZnHkke8/uOAzn/kMP//5z4HGL2r79OnD/vvvT+/evXn77bd3uK1PfvKTdOnShe985ztNe/fbwr1Pnz6sX7+eO++8E4CtW7eyevVqxo8fz3XXXcebb77J+vXri3qZ7U5en2cktQv9+/fnsssu+8Djc+bM4Stf+QpDhw5lv/3245ZbbgHgC1/4ApMnT+Y3v/kNP/7xjz+w3tSpU7niiit44YUXADjggAM477zzOPLII6mqqmLkyJEAbNmyhbPPPpt169aRUmLmzJkccMABBb7S9iV29BGqrYwYMSJ5AZTK8LDM9+RyWOazzz7LYYcd1tZlqEA7+j+OiKXltq1xSkeSMmHgS1ImDHxJyoSBL0mZMPAlKRMGviRlwuPwpU7q6Csq1z4YYOn3z9nlMhHB2WefzYIFC4DG9sf9+vVj9OjRTb1sdmTJkiXsu+++Td0w582bx3777cc55+x6zHIsWrSIlStXcuWVV77v8Tlz5tCrVy8uv/zyvdp+fX09jz32GGeeeeZebadoBr6kism1/XF9fT2/+MUv2n3gO6UjqaI6avvjm266iRNOOIF33nmH448/nm0ngb722mtUVVU1jX/ssccyfPhwhg8f3nRRliuvvJJHHnmE6upqrr/++gr8Foth4EuqqI7Y/vgnP/kJ99xzD7/+9a/p0aPHTpf72Mc+xuLFi1m2bBkLFy7k0ksvbRrz2GOPpba2lpkzZ+7eL6wVGfiSKqqjtT9esGAB999/P3fddRcf+tCHWlx206ZNTT16zjjjDFauXLnL7bcnBr6k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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x=\"Admission\", hue=\"Motivasi\", data=Psycho_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0xa8486b0>"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(x=\"Admission\", hue=\"Jiwa Kepemimpinan\", data=Psycho_data)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Data Wrangling"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Nama</th>\n",
       "      <th>PAPI</th>\n",
       "      <th>Admission</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Dominance</th>\n",
       "      <th>Influence</th>\n",
       "      <th>Steadiness</th>\n",
       "      <th>Conscientious</th>\n",
       "      <th>Inisiatif</th>\n",
       "      <th>Motivasi</th>\n",
       "      <th>Jiwa Kepemimpinan</th>\n",
       "      <th>Kepemimpinan</th>\n",
       "      <th>Kerjasama</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>True</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "      <td>False</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Nama   PAPI  Admission  Gender  Dominance  Influence  Steadiness  \\\n",
       "0   False  False      False   False      False      False       False   \n",
       "1   False  False      False   False      False      False       False   \n",
       "2   False  False       True   False      False      False       False   \n",
       "3   False  False      False   False      False      False       False   \n",
       "4   False  False      False   False      False      False       False   \n",
       "5   False  False      False   False      False      False       False   \n",
       "6   False  False      False   False      False      False       False   \n",
       "7   False  False       True   False      False      False       False   \n",
       "8   False  False      False   False      False      False       False   \n",
       "9   False  False      False   False      False      False       False   \n",
       "10  False  False      False   False      False      False       False   \n",
       "11  False  False       True   False      False      False       False   \n",
       "12  False  False      False   False      False      False       False   \n",
       "13  False  False      False   False      False      False       False   \n",
       "14  False  False       True   False      False      False       False   \n",
       "15  False  False       True   False      False      False       False   \n",
       "16  False  False       True   False      False      False       False   \n",
       "17  False  False      False   False      False      False       False   \n",
       "\n",
       "    Conscientious  Inisiatif  Motivasi  Jiwa Kepemimpinan  Kepemimpinan  \\\n",
       "0           False      False     False              False         False   \n",
       "1           False      False     False              False         False   \n",
       "2           False      False     False              False         False   \n",
       "3           False      False     False              False         False   \n",
       "4           False      False     False              False         False   \n",
       "5           False      False     False              False         False   \n",
       "6           False      False     False              False         False   \n",
       "7           False      False     False              False         False   \n",
       "8           False      False     False              False         False   \n",
       "9           False      False     False              False         False   \n",
       "10          False      False     False              False         False   \n",
       "11          False      False     False              False         False   \n",
       "12          False      False     False              False         False   \n",
       "13          False      False     False              False         False   \n",
       "14          False      False     False              False         False   \n",
       "15          False      False     False              False         False   \n",
       "16          False      False     False              False         False   \n",
       "17          False      False     False              False         False   \n",
       "\n",
       "    Kerjasama  \n",
       "0       False  \n",
       "1       False  \n",
       "2       False  \n",
       "3       False  \n",
       "4       False  \n",
       "5       False  \n",
       "6       False  \n",
       "7       False  \n",
       "8       False  \n",
       "9       False  \n",
       "10      False  \n",
       "11      False  \n",
       "12      False  \n",
       "13      False  \n",
       "14      False  \n",
       "15      False  \n",
       "16      False  \n",
       "17      False  "
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Psycho_data.isnull()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Nama                 0\n",
       "PAPI                 0\n",
       "Admission            6\n",
       "Gender               0\n",
       "Dominance            0\n",
       "Influence            0\n",
       "Steadiness           0\n",
       "Conscientious        0\n",
       "Inisiatif            0\n",
       "Motivasi             0\n",
       "Jiwa Kepemimpinan    0\n",
       "Kepemimpinan         0\n",
       "Kerjasama            0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 64,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Psycho_data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0xa886b10>"
      ]
     },
     "execution_count": 65,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(Psycho_data.isnull(), yticklabels=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "metadata": {},
   "outputs": [],
   "source": [
    "Psycho_data.dropna(inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0xa8c6c30>"
      ]
     },
     "execution_count": 67,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.heatmap(Psycho_data.isnull(), yticklabels=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Nama                 0\n",
       "PAPI                 0\n",
       "Admission            0\n",
       "Gender               0\n",
       "Dominance            0\n",
       "Influence            0\n",
       "Steadiness           0\n",
       "Conscientious        0\n",
       "Inisiatif            0\n",
       "Motivasi             0\n",
       "Jiwa Kepemimpinan    0\n",
       "Kepemimpinan         0\n",
       "Kerjasama            0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Psycho_data.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Laki-laki</th>\n",
       "      <th>Perempuan</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Laki-laki  Perempuan\n",
       "0          1          0\n",
       "1          1          0\n",
       "3          0          1\n",
       "4          0          1\n",
       "5          1          0"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Gender= pd.get_dummies(Psycho_data[\"Gender\"])\n",
    "Gender.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Inisiatif dan kreatifitas rendah</th>\n",
       "      <th>Inisiatif dan kreatifitas sedang</th>\n",
       "      <th>Inisiatif dan kreatifitas tinggi</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Inisiatif dan kreatifitas rendah   Inisiatif dan kreatifitas sedang   \\\n",
       "0                                  0                                  0   \n",
       "1                                  0                                  0   \n",
       "3                                  0                                  0   \n",
       "4                                  0                                  1   \n",
       "5                                  0                                  1   \n",
       "\n",
       "   Inisiatif dan kreatifitas tinggi   \n",
       "0                                  1  \n",
       "1                                  1  \n",
       "3                                  1  \n",
       "4                                  0  \n",
       "5                                  0  "
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Inisiatif= pd.get_dummies(Psycho_data[\"Inisiatif\"])\n",
    "Inisiatif.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Masih ragu-ragu</th>\n",
       "      <th>Motivasi kuat</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Masih ragu-ragu   Motivasi kuat \n",
       "0                 0               1\n",
       "1                 1               0\n",
       "3                 0               1\n",
       "4                 0               1\n",
       "5                 1               0"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Motivasi= pd.get_dummies(Psycho_data[\"Motivasi\"])\n",
    "Motivasi.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Sangat tinggi</th>\n",
       "      <th>Tinggi</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Sangat tinggi   Tinggi\n",
       "0               0       1\n",
       "1               0       1\n",
       "3               0       1\n",
       "4               1       0\n",
       "5               0       1"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Jiwa_Kepemimpinan= pd.get_dummies(Psycho_data[\"Jiwa Kepemimpinan\"])\n",
    "Jiwa_Kepemimpinan.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Cukup</th>\n",
       "      <th>Masih perlu pengembangan</th>\n",
       "      <th>Pemimpin yang baik</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Cukup   Masih perlu pengembangan   Pemimpin yang baik \n",
       "0       0                          0                    1\n",
       "1       1                          0                    0\n",
       "3       0                          0                    1\n",
       "4       1                          0                    0\n",
       "5       0                          1                    0"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Kepemimpinan= pd.get_dummies(Psycho_data[\"Kepemimpinan\"])\n",
    "Kepemimpinan.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Nilai kerjasama tim baik</th>\n",
       "      <th>Nilai kerjasama tim buruk</th>\n",
       "      <th>Nilai kerjasama tim sedang</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Nilai kerjasama tim baik   Nilai kerjasama tim buruk   \\\n",
       "0                          1                           0   \n",
       "1                          1                           0   \n",
       "3                          1                           0   \n",
       "4                          1                           0   \n",
       "5                          0                           0   \n",
       "\n",
       "   Nilai kerjasama tim sedang  \n",
       "0                           0  \n",
       "1                           0  \n",
       "3                           0  \n",
       "4                           0  \n",
       "5                           1  "
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Kerjasama= pd.get_dummies(Psycho_data[\"Kerjasama\"])\n",
    "Kerjasama.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Nama</th>\n",
       "      <th>PAPI</th>\n",
       "      <th>Admission</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Dominance</th>\n",
       "      <th>Influence</th>\n",
       "      <th>Steadiness</th>\n",
       "      <th>Conscientious</th>\n",
       "      <th>Inisiatif</th>\n",
       "      <th>Motivasi</th>\n",
       "      <th>...</th>\n",
       "      <th>Masih ragu-ragu</th>\n",
       "      <th>Motivasi kuat</th>\n",
       "      <th>Sangat tinggi</th>\n",
       "      <th>Tinggi</th>\n",
       "      <th>Cukup</th>\n",
       "      <th>Masih perlu pengembangan</th>\n",
       "      <th>Pemimpin yang baik</th>\n",
       "      <th>Nilai kerjasama tim baik</th>\n",
       "      <th>Nilai kerjasama tim buruk</th>\n",
       "      <th>Nilai kerjasama tim sedang</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Dedi andrianto</td>\n",
       "      <td>7</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Laki-laki</td>\n",
       "      <td>0.28</td>\n",
       "      <td>0.10</td>\n",
       "      <td>0.18</td>\n",
       "      <td>0.12</td>\n",
       "      <td>Inisiatif dan kreatifitas tinggi</td>\n",
       "      <td>Motivasi kuat</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>roy aditya putra</td>\n",
       "      <td>8</td>\n",
       "      <td>0.0</td>\n",
       "      <td>Laki-laki</td>\n",
       "      <td>0.23</td>\n",
       "      <td>0.18</td>\n",
       "      <td>0.26</td>\n",
       "      <td>0.18</td>\n",
       "      <td>Inisiatif dan kreatifitas tinggi</td>\n",
       "      <td>Masih ragu-ragu</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>nur aini</td>\n",
       "      <td>4</td>\n",
       "      <td>1.0</td>\n",
       "      <td>Perempuan</td>\n",
       "      <td>0.25</td>\n",
       "      <td>0.25</td>\n",
       "      <td>0.18</td>\n",
       "      <td>0.18</td>\n",
       "      <td>Inisiatif dan kreatifitas tinggi</td>\n",
       "      <td>Motivasi kuat</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>tiara nur annisa</td>\n",
       "      <td>8</td>\n",
       "      <td>0.0</td>\n",
       "      <td>Perempuan</td>\n",
       "      <td>0.13</td>\n",
       "      <td>0.29</td>\n",
       "      <td>0.17</td>\n",
       "      <td>0.25</td>\n",
       "      <td>Inisiatif dan kreatifitas sedang</td>\n",
       "      <td>Motivasi kuat</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>muhammad wahyu</td>\n",
       "      <td>8</td>\n",
       "      <td>0.0</td>\n",
       "      <td>Laki-laki</td>\n",
       "      <td>0.18</td>\n",
       "      <td>0.16</td>\n",
       "      <td>0.29</td>\n",
       "      <td>0.21</td>\n",
       "      <td>Inisiatif dan kreatifitas sedang</td>\n",
       "      <td>Masih ragu-ragu</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 28 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                Nama  PAPI  Admission     Gender  Dominance  Influence  \\\n",
       "0    Dedi andrianto      7        1.0  Laki-laki       0.28       0.10   \n",
       "1   roy aditya putra     8        0.0  Laki-laki       0.23       0.18   \n",
       "3           nur aini     4        1.0  Perempuan       0.25       0.25   \n",
       "4  tiara nur annisa      8        0.0  Perempuan       0.13       0.29   \n",
       "5     muhammad wahyu     8        0.0  Laki-laki       0.18       0.16   \n",
       "\n",
       "   Steadiness  Conscientious                          Inisiatif  \\\n",
       "0        0.18           0.12  Inisiatif dan kreatifitas tinggi    \n",
       "1        0.26           0.18  Inisiatif dan kreatifitas tinggi    \n",
       "3        0.18           0.18  Inisiatif dan kreatifitas tinggi    \n",
       "4        0.17           0.25  Inisiatif dan kreatifitas sedang    \n",
       "5        0.29           0.21  Inisiatif dan kreatifitas sedang    \n",
       "\n",
       "           Motivasi             ...             Masih ragu-ragu   \\\n",
       "0    Motivasi kuat              ...                            0   \n",
       "1  Masih ragu-ragu              ...                            1   \n",
       "3    Motivasi kuat              ...                            0   \n",
       "4    Motivasi kuat              ...                            0   \n",
       "5  Masih ragu-ragu              ...                            1   \n",
       "\n",
       "  Motivasi kuat  Sangat tinggi   Tinggi  Cukup   Masih perlu pengembangan   \\\n",
       "0              1              0       1       0                          0   \n",
       "1              0              0       1       1                          0   \n",
       "3              1              0       1       0                          0   \n",
       "4              1              1       0       1                          0   \n",
       "5              0              0       1       0                          1   \n",
       "\n",
       "   Pemimpin yang baik   Nilai kerjasama tim baik   Nilai kerjasama tim buruk   \\\n",
       "0                    1                          1                           0   \n",
       "1                    0                          1                           0   \n",
       "3                    1                          1                           0   \n",
       "4                    0                          1                           0   \n",
       "5                    0                          0                           0   \n",
       "\n",
       "   Nilai kerjasama tim sedang  \n",
       "0                           0  \n",
       "1                           0  \n",
       "3                           0  \n",
       "4                           0  \n",
       "5                           1  \n",
       "\n",
       "[5 rows x 28 columns]"
      ]
     },
     "execution_count": 75,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Psycho_data=pd.concat([Psycho_data,Gender,Inisiatif,Motivasi,Jiwa_Kepemimpinan,Kepemimpinan,Kerjasama], axis=1)\n",
    "Psycho_data.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [],
   "source": [
    "Psycho_data.drop(['Nama','Gender','Inisiatif','Motivasi','Jiwa Kepemimpinan','Kepemimpinan','Kerjasama'],axis=1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PAPI</th>\n",
       "      <th>Admission</th>\n",
       "      <th>Dominance</th>\n",
       "      <th>Influence</th>\n",
       "      <th>Steadiness</th>\n",
       "      <th>Conscientious</th>\n",
       "      <th>Laki-laki</th>\n",
       "      <th>Perempuan</th>\n",
       "      <th>Inisiatif dan kreatifitas rendah</th>\n",
       "      <th>Inisiatif dan kreatifitas sedang</th>\n",
       "      <th>...</th>\n",
       "      <th>Masih ragu-ragu</th>\n",
       "      <th>Motivasi kuat</th>\n",
       "      <th>Sangat tinggi</th>\n",
       "      <th>Tinggi</th>\n",
       "      <th>Cukup</th>\n",
       "      <th>Masih perlu pengembangan</th>\n",
       "      <th>Pemimpin yang baik</th>\n",
       "      <th>Nilai kerjasama tim baik</th>\n",
       "      <th>Nilai kerjasama tim buruk</th>\n",
       "      <th>Nilai kerjasama tim sedang</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>7</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.28</td>\n",
       "      <td>0.10</td>\n",
       "      <td>0.18</td>\n",
       "      <td>0.12</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>8</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.23</td>\n",
       "      <td>0.18</td>\n",
       "      <td>0.26</td>\n",
       "      <td>0.18</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.25</td>\n",
       "      <td>0.25</td>\n",
       "      <td>0.18</td>\n",
       "      <td>0.18</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>8</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.13</td>\n",
       "      <td>0.29</td>\n",
       "      <td>0.17</td>\n",
       "      <td>0.25</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>8</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.18</td>\n",
       "      <td>0.16</td>\n",
       "      <td>0.29</td>\n",
       "      <td>0.21</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>...</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 21 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "   PAPI  Admission  Dominance  Influence  Steadiness  Conscientious  \\\n",
       "0     7        1.0       0.28       0.10        0.18           0.12   \n",
       "1     8        0.0       0.23       0.18        0.26           0.18   \n",
       "3     4        1.0       0.25       0.25        0.18           0.18   \n",
       "4     8        0.0       0.13       0.29        0.17           0.25   \n",
       "5     8        0.0       0.18       0.16        0.29           0.21   \n",
       "\n",
       "   Laki-laki  Perempuan  Inisiatif dan kreatifitas rendah   \\\n",
       "0          1          0                                  0   \n",
       "1          1          0                                  0   \n",
       "3          0          1                                  0   \n",
       "4          0          1                                  0   \n",
       "5          1          0                                  0   \n",
       "\n",
       "   Inisiatif dan kreatifitas sedang              ...              \\\n",
       "0                                  0             ...               \n",
       "1                                  0             ...               \n",
       "3                                  0             ...               \n",
       "4                                  1             ...               \n",
       "5                                  1             ...               \n",
       "\n",
       "   Masih ragu-ragu   Motivasi kuat   Sangat tinggi   Tinggi  Cukup   \\\n",
       "0                 0               1               0       1       0   \n",
       "1                 1               0               0       1       1   \n",
       "3                 0               1               0       1       0   \n",
       "4                 0               1               1       0       1   \n",
       "5                 1               0               0       1       0   \n",
       "\n",
       "   Masih perlu pengembangan   Pemimpin yang baik   Nilai kerjasama tim baik   \\\n",
       "0                          0                    1                          1   \n",
       "1                          0                    0                          1   \n",
       "3                          0                    1                          1   \n",
       "4                          0                    0                          1   \n",
       "5                          1                    0                          0   \n",
       "\n",
       "   Nilai kerjasama tim buruk   Nilai kerjasama tim sedang  \n",
       "0                           0                           0  \n",
       "1                           0                           0  \n",
       "3                           0                           0  \n",
       "4                           0                           0  \n",
       "5                           0                           1  \n",
       "\n",
       "[5 rows x 21 columns]"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Psycho_data.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Training & Testing Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "X= Psycho_data.drop(\"Admission\",axis=1)\n",
    "y= Psycho_data[\"Admission\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,\n",
       "          intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,\n",
       "          penalty='l2', random_state=None, solver='liblinear', tol=0.0001,\n",
       "          verbose=0, warm_start=False)"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "logmodel=LogisticRegression()\n",
    "logmodel.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Accuracy Check"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [],
   "source": [
    "predictions = logmodel.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.metrics import classification_report"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'             precision    recall  f1-score   support\\n\\n        0.0       1.00      0.67      0.80         3\\n        1.0       0.50      1.00      0.67         1\\n\\navg / total       0.88      0.75      0.77         4\\n'"
      ]
     },
     "execution_count": 86,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "classification_report(y_test,predictions)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[2, 1],\n",
       "       [0, 1]], dtype=int64)"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import confusion_matrix\n",
    "confusion_matrix(y_test, predictions)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.75"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.metrics import accuracy_score\n",
    "accuracy_score(y_test,predictions)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Warning: Maximum number of iterations has been exceeded.\n",
      "         Current function value: 0.000208\n",
      "         Iterations: 35\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\user\\Anaconda3\\lib\\site-packages\\statsmodels\\base\\model.py:508: ConvergenceWarning: Maximum Likelihood optimization failed to converge. Check mle_retvals\n",
      "  \"Check mle_retvals\", ConvergenceWarning)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                           Logit Regression Results                           \n",
      "==============================================================================\n",
      "Dep. Variable:              Admission   No. Observations:                   12\n",
      "Model:                          Logit   Df Residuals:                        0\n",
      "Method:                           MLE   Df Model:                           11\n",
      "Date:                Wed, 16 Sep 2020   Pseudo R-squ.:                  0.9997\n",
      "Time:                        15:31:44   Log-Likelihood:             -0.0025004\n",
      "converged:                      False   LL-Null:                       -7.6382\n",
      "                                        LLR p-value:                    0.1704\n",
      "=====================================================================================================\n",
      "                                        coef    std err          z      P>|z|      [0.025      0.975]\n",
      "-----------------------------------------------------------------------------------------------------\n",
      "const                               -29.4804        nan        nan        nan         nan         nan\n",
      "PAPI                                  0.7175   3.73e+07   1.93e-08      1.000    -7.3e+07     7.3e+07\n",
      "Dominance                            12.2187   1.03e+09   1.18e-08      1.000   -2.03e+09    2.03e+09\n",
      "Influence                           -13.7127   5.24e+09  -2.62e-09      1.000   -1.03e+10    1.03e+10\n",
      "Steadiness                            8.7246        nan        nan        nan         nan         nan\n",
      "Conscientious                       -10.1352        nan        nan        nan         nan         nan\n",
      "Laki-laki                           -16.4973        nan        nan        nan         nan         nan\n",
      "Perempuan                            94.9205        nan        nan        nan         nan         nan\n",
      "Inisiatif dan kreatifitas rendah     21.5136   1.36e+09   1.58e-08      1.000   -2.67e+09    2.67e+09\n",
      "Inisiatif dan kreatifitas sedang    -26.8806        nan        nan        nan         nan         nan\n",
      "Inisiatif dan kreatifitas tinggi     12.0291   1.42e+09   8.47e-09      1.000   -2.78e+09    2.78e+09\n",
      "Masih ragu-ragu                       3.0354      2e+11   1.52e-11      1.000   -3.91e+11    3.91e+11\n",
      "Motivasi kuat                         3.4839        nan        nan        nan         nan         nan\n",
      "Sangat tinggi                       -26.7801   1.21e+11  -2.21e-10      1.000   -2.38e+11    2.38e+11\n",
      "Tinggi                               33.2993        nan        nan        nan         nan         nan\n",
      "Cukup                                12.9639      2e+11   6.49e-11      1.000   -3.91e+11    3.91e+11\n",
      "Masih perlu pengembangan            -49.5783        nan        nan        nan         nan         nan\n",
      "Pemimpin yang baik                   43.1337        nan        nan        nan         nan         nan\n",
      "Nilai kerjasama tim baik            -47.4049        nan        nan        nan         nan         nan\n",
      "Nilai kerjasama tim buruk            -9.5766      2e+11   -4.8e-11      1.000   -3.91e+11    3.91e+11\n",
      "Nilai kerjasama tim sedang           63.5007        nan        nan        nan         nan         nan\n",
      "=====================================================================================================\n",
      "\n",
      "Possibly complete quasi-separation: A fraction 0.92 of observations can be\n",
      "perfectly predicted. This might indicate that there is complete\n",
      "quasi-separation. In this case some parameters will not be identified.\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\user\\Anaconda3\\lib\\site-packages\\scipy\\stats\\_distn_infrastructure.py:879: RuntimeWarning: invalid value encountered in greater\n",
      "  return (self.a < x) & (x < self.b)\n",
      "C:\\Users\\user\\Anaconda3\\lib\\site-packages\\scipy\\stats\\_distn_infrastructure.py:879: RuntimeWarning: invalid value encountered in less\n",
      "  return (self.a < x) & (x < self.b)\n",
      "C:\\Users\\user\\Anaconda3\\lib\\site-packages\\scipy\\stats\\_distn_infrastructure.py:1821: RuntimeWarning: invalid value encountered in less_equal\n",
      "  cond2 = cond0 & (x <= self.a)\n"
     ]
    }
   ],
   "source": [
    "from statsmodels.api import Logit \n",
    "from statsmodels.tools.tools import add_constant\n",
    "\n",
    "Psycho_data = add_constant(Psycho_data)\n",
    "model = Logit(Psycho_data['Admission'], Psycho_data.drop(['Admission'], axis=1))\n",
    "result = model.fit()\n",
    "\n",
    "print(result.summary())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "const                                1.573409e-13\n",
      "PAPI                                 2.049346e+00\n",
      "Dominance                            2.025362e+05\n",
      "Influence                            1.108275e-06\n",
      "Steadiness                           6.152125e+03\n",
      "Conscientious                        3.966059e-05\n",
      "Laki-laki                            6.843723e-08\n",
      "Perempuan                            1.672826e+41\n",
      "Inisiatif dan kreatifitas rendah     2.204077e+09\n",
      "Inisiatif dan kreatifitas sedang     2.117830e-12\n",
      "Inisiatif dan kreatifitas tinggi     1.675613e+05\n",
      "Masih ragu-ragu                      2.080831e+01\n",
      "Motivasi kuat                        3.258544e+01\n",
      "Sangat tinggi                        2.341892e-12\n",
      "Tinggi                               2.895296e+14\n",
      "Cukup                                4.267177e+05\n",
      "Masih perlu pengembangan             2.940340e-22\n",
      "Pemimpin yang baik                   5.404090e+18\n",
      "Nilai kerjasama tim baik             2.584075e-21\n",
      "Nilai kerjasama tim buruk            6.933539e-05\n",
      "Nilai kerjasama tim sedang           3.784421e+27\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "print(np.exp(result.params))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
