{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "df= pd.read_csv(\"E:\\Datascience project\\\\weather_by_cities.csv\")"
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
       "      <th>day</th>\n",
       "      <th>city</th>\n",
       "      <th>temperature</th>\n",
       "      <th>windspeed</th>\n",
       "      <th>event</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1/1/2017</td>\n",
       "      <td>newyork</td>\n",
       "      <td>32</td>\n",
       "      <td>6</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1/2/2017</td>\n",
       "      <td>newyork</td>\n",
       "      <td>36</td>\n",
       "      <td>7</td>\n",
       "      <td>sunny</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1/3/2017</td>\n",
       "      <td>newyork</td>\n",
       "      <td>28</td>\n",
       "      <td>12</td>\n",
       "      <td>snow</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1/4/2017</td>\n",
       "      <td>newyork</td>\n",
       "      <td>33</td>\n",
       "      <td>7</td>\n",
       "      <td>sunny</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1/1/2017</td>\n",
       "      <td>mumbai</td>\n",
       "      <td>90</td>\n",
       "      <td>5</td>\n",
       "      <td>sunny</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1/2/2017</td>\n",
       "      <td>mumbai</td>\n",
       "      <td>85</td>\n",
       "      <td>12</td>\n",
       "      <td>fog</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>1/3/2017</td>\n",
       "      <td>mumbai</td>\n",
       "      <td>87</td>\n",
       "      <td>15</td>\n",
       "      <td>fog</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>1/4/2017</td>\n",
       "      <td>mumbai</td>\n",
       "      <td>92</td>\n",
       "      <td>5</td>\n",
       "      <td>rain</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>1/1/2017</td>\n",
       "      <td>paris</td>\n",
       "      <td>45</td>\n",
       "      <td>20</td>\n",
       "      <td>sunny</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>1/2/2017</td>\n",
       "      <td>paris</td>\n",
       "      <td>50</td>\n",
       "      <td>18</td>\n",
       "      <td>cloudy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>1/3/2017</td>\n",
       "      <td>paris</td>\n",
       "      <td>54</td>\n",
       "      <td>8</td>\n",
       "      <td>cloudy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>1/4/2017</td>\n",
       "      <td>paris</td>\n",
       "      <td>42</td>\n",
       "      <td>10</td>\n",
       "      <td>cloudy</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         day     city  temperature  windspeed   event\n",
       "0   1/1/2017  newyork           32          6    rain\n",
       "1   1/2/2017  newyork           36          7   sunny\n",
       "2   1/3/2017  newyork           28         12    snow\n",
       "3   1/4/2017  newyork           33          7   sunny\n",
       "4   1/1/2017   mumbai           90          5   sunny\n",
       "5   1/2/2017   mumbai           85         12     fog\n",
       "6   1/3/2017   mumbai           87         15     fog\n",
       "7   1/4/2017   mumbai           92          5    rain\n",
       "8   1/1/2017    paris           45         20   sunny\n",
       "9   1/2/2017    paris           50         18  cloudy\n",
       "10  1/3/2017    paris           54          8  cloudy\n",
       "11  1/4/2017    paris           42         10  cloudy"
      ]
     },
     "execution_count": 17,
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
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        0\n",
      "0  Python\n",
      "1  Pandas\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd    \n",
    "# a list of strings    \n",
    "a = ['Python', 'Pandas']    \n",
    "# Calling DataFrame constructor on list    \n",
    "info = pd.DataFrame(a)    \n",
    "print(info) "
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
