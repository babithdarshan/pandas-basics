{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "df = pd.DataFrame(data=[[2,4,6,-3],[3,-4,-1],[-10,3,5,-7]],\n",
    " \n",
    " columns=['c1','c2','c3','c4'],\n",
    " index=['R1','R2','R3'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
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
       "      <th>c4</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>R1</th>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>6</td>\n",
       "      <td>-3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>R2</th>\n",
       "      <td>3</td>\n",
       "      <td>-4</td>\n",
       "      <td>-1</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>R3</th>\n",
       "      <td>-10</td>\n",
       "      <td>3</td>\n",
       "      <td>5</td>\n",
       "      <td>-7.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    c1  c2  c3   c4\n",
       "R1   2   4   6 -3.0\n",
       "R2   3  -4  -1  NaN\n",
       "R3 -10   3   5 -7.0"
      ]
     },
     "execution_count": 2,
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
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['R1', 'R2', 'R3'], dtype='object')"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['c1', 'c2', 'c3', 'c4'], dtype='object')"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
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
       "      <th>index</th>\n",
       "      <th>c1</th>\n",
       "      <th>c2</th>\n",
       "      <th>c3</th>\n",
       "      <th>c4</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>R1</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>6</td>\n",
       "      <td>-3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>R2</td>\n",
       "      <td>3</td>\n",
       "      <td>-4</td>\n",
       "      <td>-1</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>R3</td>\n",
       "      <td>-10</td>\n",
       "      <td>3</td>\n",
       "      <td>5</td>\n",
       "      <td>-7.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  index  c1  c2  c3   c4\n",
       "0    R1   2   4   6 -3.0\n",
       "1    R2   3  -4  -1  NaN\n",
       "2    R3 -10   3   5 -7.0"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.reset_index() # creating new index"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
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
       "      <th>c4</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>R1</th>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>6</td>\n",
       "      <td>-3.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    c1  c2  c3   c4\n",
       "R1   2   4   6 -3.0"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "df['newc'] = df['c1'] +5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
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
       "      <th>c4</th>\n",
       "      <th>newc</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>R1</th>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>6</td>\n",
       "      <td>-3.0</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>R2</th>\n",
       "      <td>3</td>\n",
       "      <td>-4</td>\n",
       "      <td>-1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>R3</th>\n",
       "      <td>-10</td>\n",
       "      <td>3</td>\n",
       "      <td>5</td>\n",
       "      <td>-7.0</td>\n",
       "      <td>-5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    c1  c2  c3   c4  newc\n",
       "R1   2   4   6 -3.0     7\n",
       "R2   3  -4  -1  NaN     8\n",
       "R3 -10   3   5 -7.0    -5"
      ]
     },
     "execution_count": 15,
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
   "execution_count": 16,
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
       "      <th>c4</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>R1</th>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>6</td>\n",
       "      <td>-3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>R2</th>\n",
       "      <td>3</td>\n",
       "      <td>-4</td>\n",
       "      <td>-1</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>R3</th>\n",
       "      <td>-10</td>\n",
       "      <td>3</td>\n",
       "      <td>5</td>\n",
       "      <td>-7.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    c1  c2  c3   c4\n",
       "R1   2   4   6 -3.0\n",
       "R2   3  -4  -1  NaN\n",
       "R3 -10   3   5 -7.0"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.drop('newc', axis=1)"
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
       "      <th>c1</th>\n",
       "      <th>c2</th>\n",
       "      <th>c3</th>\n",
       "      <th>c4</th>\n",
       "      <th>newc</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>R2</th>\n",
       "      <td>3</td>\n",
       "      <td>-4</td>\n",
       "      <td>-1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>R3</th>\n",
       "      <td>-10</td>\n",
       "      <td>3</td>\n",
       "      <td>5</td>\n",
       "      <td>-7.0</td>\n",
       "      <td>-5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    c1  c2  c3   c4  newc\n",
       "R2   3  -4  -1  NaN     8\n",
       "R3 -10   3   5 -7.0    -5"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.drop('R1', axis=0)"
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
       "      <th>c1</th>\n",
       "      <th>c2</th>\n",
       "      <th>c3</th>\n",
       "      <th>c4</th>\n",
       "      <th>newc</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>R1</th>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>6</td>\n",
       "      <td>-3.0</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>R2</th>\n",
       "      <td>3</td>\n",
       "      <td>-4</td>\n",
       "      <td>-1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>R3</th>\n",
       "      <td>-10</td>\n",
       "      <td>3</td>\n",
       "      <td>5</td>\n",
       "      <td>-7.0</td>\n",
       "      <td>-5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    c1  c2  c3   c4  newc\n",
       "R1   2   4   6 -3.0     7\n",
       "R2   3  -4  -1  NaN     8\n",
       "R3 -10   3   5 -7.0    -5"
      ]
     },
     "execution_count": 18,
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
       "      <th>index</th>\n",
       "      <th>c1</th>\n",
       "      <th>c2</th>\n",
       "      <th>c3</th>\n",
       "      <th>c4</th>\n",
       "      <th>newc</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>R1</td>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>6</td>\n",
       "      <td>-3.0</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>R2</td>\n",
       "      <td>3</td>\n",
       "      <td>-4</td>\n",
       "      <td>-1</td>\n",
       "      <td>NaN</td>\n",
       "      <td>8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>R3</td>\n",
       "      <td>-10</td>\n",
       "      <td>3</td>\n",
       "      <td>5</td>\n",
       "      <td>-7.0</td>\n",
       "      <td>-5</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  index  c1  c2  c3   c4  newc\n",
       "0    R1   2   4   6 -3.0     7\n",
       "1    R2   3  -4  -1  NaN     8\n",
       "2    R3 -10   3   5 -7.0    -5"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.reset_index()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
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
       "      <th>c4</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>R1</th>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>6</td>\n",
       "      <td>-3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>R2</th>\n",
       "      <td>3</td>\n",
       "      <td>-4</td>\n",
       "      <td>-1</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>R3</th>\n",
       "      <td>-10</td>\n",
       "      <td>3</td>\n",
       "      <td>5</td>\n",
       "      <td>-7.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    c1  c2  c3   c4\n",
       "R1   2   4   6 -3.0\n",
       "R2   3  -4  -1  NaN\n",
       "R3 -10   3   5 -7.0"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.drop('newc',axis=1)"
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
       "c1      3.0\n",
       "c2     -4.0\n",
       "c3     -1.0\n",
       "c4      NaN\n",
       "newc    8.0\n",
       "Name: R2, dtype: float64"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.iloc[1,:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "c2   -4.0\n",
       "c3   -1.0\n",
       "Name: R2, dtype: float64"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.iloc[1,1:3]"
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
