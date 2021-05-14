{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "df = pd.DataFrame([[np.nan, 2,np.nan, 0],[3,4, np.nan, 1],\n",
    "                   [np.nan,np.nan, np.nan,5], [np.nan,np.nan, np.nan, np.nan]],\n",
    "            \n",
    "                  columns=list(\"ABCD\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
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
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>NaN</td>\n",
       "      <td>2.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     A    B   C    D\n",
       "0  NaN  2.0 NaN  0.0\n",
       "1  3.0  4.0 NaN  1.0\n",
       "2  NaN  NaN NaN  5.0\n",
       "3  NaN  NaN NaN  NaN"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
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
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>NaN</td>\n",
       "      <td>2.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     A    B    D\n",
       "0  NaN  2.0  0.0\n",
       "1  3.0  4.0  1.0\n",
       "2  NaN  NaN  5.0\n",
       "3  NaN  NaN  NaN"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dropna(axis=1,how='all')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
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
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>-10.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>-10.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>-10.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>-10.0</td>\n",
       "      <td>-10.0</td>\n",
       "      <td>-10.0</td>\n",
       "      <td>5.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>-10.0</td>\n",
       "      <td>-10.0</td>\n",
       "      <td>-10.0</td>\n",
       "      <td>-10.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      A     B     C     D\n",
       "0 -10.0   2.0 -10.0   0.0\n",
       "1   3.0   4.0 -10.0   1.0\n",
       "2 -10.0 -10.0 -10.0   5.0\n",
       "3 -10.0 -10.0 -10.0 -10.0"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.fillna(-10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
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
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>NaN</td>\n",
       "      <td>2.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>5.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     A    B   C    D\n",
       "0  NaN  2.0 NaN  0.0\n",
       "1  3.0  4.0 NaN  1.0\n",
       "2  NaN  NaN NaN  5.0\n",
       "3  NaN  NaN NaN  NaN"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    2.0\n",
       "1    4.0\n",
       "2    3.0\n",
       "3    3.0\n",
       "Name: B, dtype: float64"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['B'].fillna(df['B'].mean())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.0"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['B'].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
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
       "      <th>A</th>\n",
       "      <th>B</th>\n",
       "      <th>C</th>\n",
       "      <th>D</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>there was missing value here</td>\n",
       "      <td>2</td>\n",
       "      <td>there was missing value here</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>there was missing value here</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>there was missing value here</td>\n",
       "      <td>there was missing value here</td>\n",
       "      <td>there was missing value here</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>there was missing value here</td>\n",
       "      <td>there was missing value here</td>\n",
       "      <td>there was missing value here</td>\n",
       "      <td>there was missing value here</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                              A                             B  \\\n",
       "0  there was missing value here                             2   \n",
       "1                             3                             4   \n",
       "2  there was missing value here  there was missing value here   \n",
       "3  there was missing value here  there was missing value here   \n",
       "\n",
       "                              C                             D  \n",
       "0  there was missing value here                             0  \n",
       "1  there was missing value here                             1  \n",
       "2  there was missing value here                             5  \n",
       "3  there was missing value here  there was missing value here  "
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.replace(np.NaN, \"there was missing value here\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(data=[['mi','p1','male',54,15],\n",
    "                        ['m1','p2','female',21,19],\n",
    "                        ['DO','p3','male',69,26],\n",
    "                        ['RR','p4','female',96,28],\n",
    "                        ['GT','p5','male',33,28],\n",
    "                        ['MI','p5','male',33,24],\n",
    "                        ['KNR','p6','female',51,33],\n",
    "                        ['GT','p7','male',24,40],\n",
    "                        ['RR','p9','female',78,19],\n",
    "                        ['KNR','p10','male',33,17],\n",
    "                        ['MI','p11','female',87,20],\n",
    "                        ['GT','p12','male',81,21],\n",
    "                        ['KNR','p13','female',36,29]],columns=['team','player','sex','score','Age'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
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
       "      <th>team</th>\n",
       "      <th>player</th>\n",
       "      <th>sex</th>\n",
       "      <th>score</th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>mi</td>\n",
       "      <td>p1</td>\n",
       "      <td>male</td>\n",
       "      <td>54</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>m1</td>\n",
       "      <td>p2</td>\n",
       "      <td>female</td>\n",
       "      <td>21</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>DO</td>\n",
       "      <td>p3</td>\n",
       "      <td>male</td>\n",
       "      <td>69</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>RR</td>\n",
       "      <td>p4</td>\n",
       "      <td>female</td>\n",
       "      <td>96</td>\n",
       "      <td>28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>GT</td>\n",
       "      <td>p5</td>\n",
       "      <td>male</td>\n",
       "      <td>33</td>\n",
       "      <td>28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>MI</td>\n",
       "      <td>p5</td>\n",
       "      <td>male</td>\n",
       "      <td>33</td>\n",
       "      <td>24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>KNR</td>\n",
       "      <td>p6</td>\n",
       "      <td>female</td>\n",
       "      <td>51</td>\n",
       "      <td>33</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>GT</td>\n",
       "      <td>p7</td>\n",
       "      <td>male</td>\n",
       "      <td>24</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>RR</td>\n",
       "      <td>p9</td>\n",
       "      <td>female</td>\n",
       "      <td>78</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>KNR</td>\n",
       "      <td>p10</td>\n",
       "      <td>male</td>\n",
       "      <td>33</td>\n",
       "      <td>17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>MI</td>\n",
       "      <td>p11</td>\n",
       "      <td>female</td>\n",
       "      <td>87</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>GT</td>\n",
       "      <td>p12</td>\n",
       "      <td>male</td>\n",
       "      <td>81</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>KNR</td>\n",
       "      <td>p13</td>\n",
       "      <td>female</td>\n",
       "      <td>36</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   team player     sex  score  Age\n",
       "0    mi     p1    male     54   15\n",
       "1    m1     p2  female     21   19\n",
       "2    DO     p3    male     69   26\n",
       "3    RR     p4  female     96   28\n",
       "4    GT     p5    male     33   28\n",
       "5    MI     p5    male     33   24\n",
       "6   KNR     p6  female     51   33\n",
       "7    GT     p7    male     24   40\n",
       "8    RR     p9  female     78   19\n",
       "9   KNR    p10    male     33   17\n",
       "10   MI    p11  female     87   20\n",
       "11   GT    p12    male     81   21\n",
       "12  KNR    p13  female     36   29"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "28    2\n",
       "19    2\n",
       "15    1\n",
       "29    1\n",
       "40    1\n",
       "26    1\n",
       "24    1\n",
       "17    1\n",
       "21    1\n",
       "20    1\n",
       "33    1\n",
       "Name: Age, dtype: int64"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Age'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "GT     3\n",
       "KNR    3\n",
       "RR     2\n",
       "MI     2\n",
       "m1     1\n",
       "mi     1\n",
       "DO     1\n",
       "Name: team, dtype: int64"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['team'].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "def congrats(x):\n",
    "    if x > 70:\n",
    "        return\"congratulation\"\n",
    "    else:\n",
    "        return \"\"\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['player']= df['score'].apply(congrats) +df['player']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
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
       "      <th>team</th>\n",
       "      <th>player</th>\n",
       "      <th>sex</th>\n",
       "      <th>score</th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>mi</td>\n",
       "      <td>p1</td>\n",
       "      <td>male</td>\n",
       "      <td>54</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>m1</td>\n",
       "      <td>p2</td>\n",
       "      <td>female</td>\n",
       "      <td>21</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>DO</td>\n",
       "      <td>p3</td>\n",
       "      <td>male</td>\n",
       "      <td>69</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>RR</td>\n",
       "      <td>congratulationp4</td>\n",
       "      <td>female</td>\n",
       "      <td>96</td>\n",
       "      <td>28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>GT</td>\n",
       "      <td>p5</td>\n",
       "      <td>male</td>\n",
       "      <td>33</td>\n",
       "      <td>28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>MI</td>\n",
       "      <td>p5</td>\n",
       "      <td>male</td>\n",
       "      <td>33</td>\n",
       "      <td>24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>KNR</td>\n",
       "      <td>p6</td>\n",
       "      <td>female</td>\n",
       "      <td>51</td>\n",
       "      <td>33</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>GT</td>\n",
       "      <td>p7</td>\n",
       "      <td>male</td>\n",
       "      <td>24</td>\n",
       "      <td>40</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>RR</td>\n",
       "      <td>congratulationp9</td>\n",
       "      <td>female</td>\n",
       "      <td>78</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>KNR</td>\n",
       "      <td>p10</td>\n",
       "      <td>male</td>\n",
       "      <td>33</td>\n",
       "      <td>17</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>MI</td>\n",
       "      <td>congratulationp11</td>\n",
       "      <td>female</td>\n",
       "      <td>87</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>GT</td>\n",
       "      <td>congratulationp12</td>\n",
       "      <td>male</td>\n",
       "      <td>81</td>\n",
       "      <td>21</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>KNR</td>\n",
       "      <td>p13</td>\n",
       "      <td>female</td>\n",
       "      <td>36</td>\n",
       "      <td>29</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   team             player     sex  score  Age\n",
       "0    mi                 p1    male     54   15\n",
       "1    m1                 p2  female     21   19\n",
       "2    DO                 p3    male     69   26\n",
       "3    RR   congratulationp4  female     96   28\n",
       "4    GT                 p5    male     33   28\n",
       "5    MI                 p5    male     33   24\n",
       "6   KNR                 p6  female     51   33\n",
       "7    GT                 p7    male     24   40\n",
       "8    RR   congratulationp9  female     78   19\n",
       "9   KNR                p10    male     33   17\n",
       "10   MI  congratulationp11  female     87   20\n",
       "11   GT  congratulationp12    male     81   21\n",
       "12  KNR                p13  female     36   29"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(data=[[2,3],[\"hello\",\"world\"],[34,True]],index=['R1','R2','R3'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
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
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>R1</th>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>R2</th>\n",
       "      <td>hello</td>\n",
       "      <td>world</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>R3</th>\n",
       "      <td>34</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        0      1\n",
       "R1      2      3\n",
       "R2  hello  world\n",
       "R3     34   True"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3, 2)"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
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
       "6"
      ]
     },
     "execution_count": 58,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.size"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv('sampleCsv.Csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
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
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>R1</th>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>R2</th>\n",
       "      <td>hello</td>\n",
       "      <td>world</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>R3</th>\n",
       "      <td>34</td>\n",
       "      <td>True</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        0      1\n",
       "R1      2      3\n",
       "R2  hello  world\n",
       "R3     34   True"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(data=np.random.randint(1,100, (100,3)), columns=['c1','c2','c3'])"
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
       "      <th>c1</th>\n",
       "      <th>c2</th>\n",
       "      <th>c3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>42</td>\n",
       "      <td>58</td>\n",
       "      <td>81</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>72</td>\n",
       "      <td>76</td>\n",
       "      <td>62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>9</td>\n",
       "      <td>23</td>\n",
       "      <td>83</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>97</td>\n",
       "      <td>31</td>\n",
       "      <td>68</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>42</td>\n",
       "      <td>66</td>\n",
       "      <td>98</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>95</th>\n",
       "      <td>77</td>\n",
       "      <td>79</td>\n",
       "      <td>77</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>96</th>\n",
       "      <td>61</td>\n",
       "      <td>39</td>\n",
       "      <td>87</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>97</th>\n",
       "      <td>45</td>\n",
       "      <td>1</td>\n",
       "      <td>98</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>98</th>\n",
       "      <td>20</td>\n",
       "      <td>5</td>\n",
       "      <td>24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99</th>\n",
       "      <td>42</td>\n",
       "      <td>55</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>100 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    c1  c2  c3\n",
       "0   42  58  81\n",
       "1   72  76  62\n",
       "2    9  23  83\n",
       "3   97  31  68\n",
       "4   42  66  98\n",
       "..  ..  ..  ..\n",
       "95  77  79  77\n",
       "96  61  39  87\n",
       "97  45   1  98\n",
       "98  20   5  24\n",
       "99  42  55   5\n",
       "\n",
       "[100 rows x 3 columns]"
      ]
     },
     "execution_count": 70,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(100, 3)"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
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
       "      <th>c1</th>\n",
       "      <th>c2</th>\n",
       "      <th>c3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>42</td>\n",
       "      <td>58</td>\n",
       "      <td>81</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>72</td>\n",
       "      <td>76</td>\n",
       "      <td>62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>9</td>\n",
       "      <td>23</td>\n",
       "      <td>83</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>97</td>\n",
       "      <td>31</td>\n",
       "      <td>68</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>42</td>\n",
       "      <td>66</td>\n",
       "      <td>98</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   c1  c2  c3\n",
       "0  42  58  81\n",
       "1  72  76  62\n",
       "2   9  23  83\n",
       "3  97  31  68\n",
       "4  42  66  98"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(data=np.random.randint(1,100, (100,3)), columns=['c1','c2','c3'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
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
       "      <th>c1</th>\n",
       "      <th>c2</th>\n",
       "      <th>c3</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>92</td>\n",
       "      <td>62</td>\n",
       "      <td>91</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>95</td>\n",
       "      <td>26</td>\n",
       "      <td>94</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>77</td>\n",
       "      <td>66</td>\n",
       "      <td>75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>35</td>\n",
       "      <td>56</td>\n",
       "      <td>47</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>86</td>\n",
       "      <td>88</td>\n",
       "      <td>39</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>95</th>\n",
       "      <td>47</td>\n",
       "      <td>50</td>\n",
       "      <td>88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>96</th>\n",
       "      <td>36</td>\n",
       "      <td>10</td>\n",
       "      <td>81</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>97</th>\n",
       "      <td>8</td>\n",
       "      <td>62</td>\n",
       "      <td>60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>98</th>\n",
       "      <td>5</td>\n",
       "      <td>69</td>\n",
       "      <td>71</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99</th>\n",
       "      <td>65</td>\n",
       "      <td>69</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>100 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    c1  c2  c3\n",
       "0   92  62  91\n",
       "1   95  26  94\n",
       "2   77  66  75\n",
       "3   35  56  47\n",
       "4   86  88  39\n",
       "..  ..  ..  ..\n",
       "95  47  50  88\n",
       "96  36  10  81\n",
       "97   8  62  60\n",
       "98   5  69  71\n",
       "99  65  69   4\n",
       "\n",
       "[100 rows x 3 columns]"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 91,
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
    "%matplotlib inline\n",
    "df['c1'].plot.area()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 98,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 98,
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
    "df['c1'].plot.bar()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 101,
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
    "df.plot.barh()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:ylabel='Density'>"
      ]
     },
     "execution_count": 102,
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
    "df['c2'].plot.kde()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:ylabel='Frequency'>"
      ]
     },
     "execution_count": 105,
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
    "df.plot.hist(bins=20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
