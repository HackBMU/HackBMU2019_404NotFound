{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
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
       "      <th>States/UTs</th>\n",
       "      <th>District</th>\n",
       "      <th>Year</th>\n",
       "      <th>Murder</th>\n",
       "      <th>Attempt to commit Murder</th>\n",
       "      <th>Culpable Homicide not amounting to Murder</th>\n",
       "      <th>Attempt to commit Culpable Homicide</th>\n",
       "      <th>Rape</th>\n",
       "      <th>Custodial Rape</th>\n",
       "      <th>Custodial_Gang Rape</th>\n",
       "      <th>...</th>\n",
       "      <th>Offences promoting enmity between different groups</th>\n",
       "      <th>Promoting enmity between different groups</th>\n",
       "      <th>Imputation, assertions prejudicial to national integration</th>\n",
       "      <th>Extortion</th>\n",
       "      <th>Disclosure of Identity of Victims</th>\n",
       "      <th>Incidence of Rash Driving</th>\n",
       "      <th>HumanTrafficking</th>\n",
       "      <th>Unnatural Offence</th>\n",
       "      <th>Other IPC crimes</th>\n",
       "      <th>Total Cognizable IPC crimes</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Andhra Pradesh</td>\n",
       "      <td>Anantapur</td>\n",
       "      <td>2014</td>\n",
       "      <td>134</td>\n",
       "      <td>171</td>\n",
       "      <td>8</td>\n",
       "      <td>0</td>\n",
       "      <td>35</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1038</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3800</td>\n",
       "      <td>8376</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Andhra Pradesh</td>\n",
       "      <td>Chittoor</td>\n",
       "      <td>2014</td>\n",
       "      <td>84</td>\n",
       "      <td>170</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>32</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>19</td>\n",
       "      <td>0</td>\n",
       "      <td>249</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2567</td>\n",
       "      <td>5374</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Andhra Pradesh</td>\n",
       "      <td>Cuddapah</td>\n",
       "      <td>2014</td>\n",
       "      <td>80</td>\n",
       "      <td>162</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>28</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>948</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2604</td>\n",
       "      <td>5803</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Andhra Pradesh</td>\n",
       "      <td>East Godavari</td>\n",
       "      <td>2014</td>\n",
       "      <td>64</td>\n",
       "      <td>84</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>85</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>32</td>\n",
       "      <td>0</td>\n",
       "      <td>39</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3791</td>\n",
       "      <td>7630</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Andhra Pradesh</td>\n",
       "      <td>Guntakal Railway</td>\n",
       "      <td>2014</td>\n",
       "      <td>14</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>37</td>\n",
       "      <td>490</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 91 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       States/UTs          District  Year  Murder  Attempt to commit Murder  \\\n",
       "0  Andhra Pradesh         Anantapur  2014     134                       171   \n",
       "1  Andhra Pradesh          Chittoor  2014      84                       170   \n",
       "2  Andhra Pradesh          Cuddapah  2014      80                       162   \n",
       "3  Andhra Pradesh     East Godavari  2014      64                        84   \n",
       "4  Andhra Pradesh  Guntakal Railway  2014      14                         4   \n",
       "\n",
       "   Culpable Homicide not amounting to Murder  \\\n",
       "0                                          8   \n",
       "1                                          2   \n",
       "2                                          1   \n",
       "3                                          2   \n",
       "4                                          0   \n",
       "\n",
       "   Attempt to commit Culpable Homicide  Rape  Custodial Rape  \\\n",
       "0                                    0    35               0   \n",
       "1                                    0    32               0   \n",
       "2                                    0    28               0   \n",
       "3                                    0    85               0   \n",
       "4                                    0     0               0   \n",
       "\n",
       "   Custodial_Gang Rape             ...               \\\n",
       "0                    0             ...                \n",
       "1                    0             ...                \n",
       "2                    0             ...                \n",
       "3                    0             ...                \n",
       "4                    0             ...                \n",
       "\n",
       "   Offences promoting enmity between different groups  \\\n",
       "0                                                  0    \n",
       "1                                                  0    \n",
       "2                                                  0    \n",
       "3                                                  0    \n",
       "4                                                  0    \n",
       "\n",
       "   Promoting enmity between different groups  \\\n",
       "0                                          0   \n",
       "1                                          0   \n",
       "2                                          0   \n",
       "3                                          0   \n",
       "4                                          0   \n",
       "\n",
       "   Imputation, assertions prejudicial to national integration  Extortion  \\\n",
       "0                                                  0                   0   \n",
       "1                                                  0                  19   \n",
       "2                                                  0                   0   \n",
       "3                                                  0                  32   \n",
       "4                                                  0                   0   \n",
       "\n",
       "   Disclosure of Identity of Victims  Incidence of Rash Driving  \\\n",
       "0                                  0                       1038   \n",
       "1                                  0                        249   \n",
       "2                                  0                        948   \n",
       "3                                  0                         39   \n",
       "4                                  0                          1   \n",
       "\n",
       "   HumanTrafficking  Unnatural Offence  Other IPC crimes  \\\n",
       "0                 0                  0              3800   \n",
       "1                 0                  0              2567   \n",
       "2                 0                  0              2604   \n",
       "3                 0                  0              3791   \n",
       "4                 0                  0                37   \n",
       "\n",
       "   Total Cognizable IPC crimes  \n",
       "0                         8376  \n",
       "1                         5374  \n",
       "2                         5803  \n",
       "3                         7630  \n",
       "4                          490  \n",
       "\n",
       "[5 rows x 91 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "crime =pd.read_csv('01_District_wise_crimes_committed_IPC_2014.csv')\n",
    "crime.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 838 entries, 0 to 837\n",
      "Data columns (total 91 columns):\n",
      "States/UTs                                                          838 non-null object\n",
      "District                                                            838 non-null object\n",
      "Year                                                                838 non-null int64\n",
      "Murder                                                              838 non-null int64\n",
      "Attempt to commit Murder                                            838 non-null int64\n",
      "Culpable Homicide not amounting to Murder                           838 non-null int64\n",
      "Attempt to commit Culpable Homicide                                 838 non-null int64\n",
      "Rape                                                                838 non-null int64\n",
      "Custodial Rape                                                      838 non-null int64\n",
      "Custodial_Gang Rape                                                 838 non-null int64\n",
      "Custodial_Other Rape                                                838 non-null int64\n",
      "Rape other than Custodial                                           838 non-null int64\n",
      "Rape_Gang Rape                                                      838 non-null int64\n",
      "Rape_Others                                                         838 non-null int64\n",
      "Attempt to commit Rape                                              838 non-null int64\n",
      "Kidnapping & Abduction_Total                                        838 non-null int64\n",
      "Kidnapping & Abduction                                              838 non-null int64\n",
      "Kidnapping & Abduction in order to Murder                           838 non-null int64\n",
      "Kidnapping for Ransom                                               838 non-null int64\n",
      "Kidnapping & Abduction of Women to compel her for marriage          838 non-null int64\n",
      "Other Kidnapping                                                    838 non-null int64\n",
      "Dacoity                                                             838 non-null int64\n",
      "Dacoity with Murder                                                 838 non-null int64\n",
      "Other Dacoity                                                       838 non-null int64\n",
      "Making Preparation and Assembly for committing Dacoity              838 non-null int64\n",
      "Robbery                                                             838 non-null int64\n",
      "Criminal Trespass/Burglary                                          838 non-null int64\n",
      "Criminal Trespass or Burglary                                       838 non-null int64\n",
      "House Trespass & House Breaking                                     838 non-null int64\n",
      "Theft                                                               838 non-null int64\n",
      "Auto Theft                                                          838 non-null int64\n",
      "Other Thefts                                                        838 non-null int64\n",
      "Unlawful Assembly                                                   838 non-null int64\n",
      "Riots                                                               838 non-null int64\n",
      "Riots_Communal                                                      838 non-null int64\n",
      "Riots_Industrial                                                    838 non-null int64\n",
      "Riots_Political                                                     838 non-null int64\n",
      "Riots_Caste Conflict                                                838 non-null int64\n",
      "Riots_SC/STs Vs Non-SCs/STs                                         838 non-null int64\n",
      "Riots_Other Caste Conflict                                          838 non-null int64\n",
      "Riots_Agrarian                                                      838 non-null int64\n",
      "Riots_Students                                                      838 non-null int64\n",
      "Riots_Sectarian                                                     838 non-null int64\n",
      "Riots_Others                                                        838 non-null int64\n",
      "Criminal Breach of Trust                                            838 non-null int64\n",
      "Cheating                                                            838 non-null int64\n",
      "Forgery                                                             838 non-null int64\n",
      "Counterfeiting                                                      838 non-null int64\n",
      "Counterfeit Offences related to Counterfeit Coin                    838 non-null int64\n",
      "Counterfeiting Government Stamp                                     838 non-null int64\n",
      "Counterfeit currency & Bank notes                                   838 non-null int64\n",
      "Counterfeiting currency notes/Bank notes                            838 non-null int64\n",
      "Using forged or counterfeiting currency/Bank notes                  838 non-null int64\n",
      "Possession of forged or counterfeiting currency/Bank notes          838 non-null int64\n",
      "Making or Possessing materials for forged currency/Bank notes       838 non-null int64\n",
      "Making or Using documents resembling currency                       838 non-null int64\n",
      "Arson                                                               838 non-null int64\n",
      "Grievous Hurt                                                       838 non-null int64\n",
      "Hurt                                                                838 non-null int64\n",
      "Acid attack                                                         838 non-null int64\n",
      "Attempt to Acid Attack                                              838 non-null int64\n",
      "Dowry Deaths                                                        838 non-null int64\n",
      "Assault on Women with intent to outrage her Modesty                 838 non-null int64\n",
      "Sexual Harassment                                                   838 non-null int64\n",
      "Assault or use of criminal force to women with intent to Disrobe    838 non-null int64\n",
      "Voyeurism                                                           838 non-null int64\n",
      "Stalking                                                            838 non-null int64\n",
      "Other Assault on Women                                              838 non-null int64\n",
      "Insult to the Modesty of Women                                      838 non-null int64\n",
      "At Office premises                                                  838 non-null int64\n",
      "Other places related to work                                        838 non-null int64\n",
      "In Public Transport system                                          838 non-null int64\n",
      "Places other than 231, 232 & 233                                    838 non-null int64\n",
      "Cruelty by Husband or his Relatives                                 838 non-null int64\n",
      "Importation of Girls from Foreign Country                           838 non-null int64\n",
      "Causing Death by Negligence                                         838 non-null int64\n",
      "Deaths due to negligent driving/act                                 838 non-null int64\n",
      "Deaths due to Other Causes                                          838 non-null int64\n",
      "Offences against State                                              838 non-null int64\n",
      "Sedition                                                            838 non-null int64\n",
      "Other offences against State                                        838 non-null int64\n",
      "Offences promoting enmity between different groups                  838 non-null int64\n",
      "Promoting enmity between different groups                           838 non-null int64\n",
      "Imputation, assertions prejudicial to national integration          838 non-null int64\n",
      "Extortion                                                           838 non-null int64\n",
      "Disclosure of Identity of Victims                                   838 non-null int64\n",
      "Incidence of Rash Driving                                           838 non-null int64\n",
      "HumanTrafficking                                                    838 non-null int64\n",
      "Unnatural Offence                                                   838 non-null int64\n",
      "Other IPC crimes                                                    838 non-null int64\n",
      "Total Cognizable IPC crimes                                         838 non-null int64\n",
      "dtypes: int64(89), object(2)\n",
      "memory usage: 595.8+ KB\n"
     ]
    }
   ],
   "source": [
    "crime.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Year                                                                 1615.250000\n",
       "Murder                                                                810.632141\n",
       "Attempt to commit Murder                                             1102.495649\n",
       "Culpable Homicide not amounting to Murder                             289.658184\n",
       "Attempt to commit Culpable Homicide                                   294.113185\n",
       "Rape                                                                  808.242591\n",
       "Custodial Rape                                                        129.278926\n",
       "Custodial_Gang Rape                                                   105.405011\n",
       "Custodial_Other Rape                                                  128.630198\n",
       "Rape other than Custodial                                             807.909423\n",
       "Rape_Gang Rape                                                        181.174864\n",
       "Rape_Others                                                           767.887185\n",
       "Attempt to commit Rape                                                331.559886\n",
       "Kidnapping & Abduction_Total                                         1793.453219\n",
       "Kidnapping & Abduction                                                987.035688\n",
       "Kidnapping & Abduction in order to Murder                             188.073498\n",
       "Kidnapping for Ransom                                                 119.173090\n",
       "Kidnapping & Abduction of Women to compel her for marriage           1085.641723\n",
       "Other Kidnapping                                                      537.137249\n",
       "Dacoity                                                               223.724336\n",
       "Dacoity with Murder                                                   107.789993\n",
       "Other Dacoity                                                         221.983617\n",
       "Making Preparation and Assembly for committing Dacoity                253.209112\n",
       "Robbery                                                              1366.880101\n",
       "Criminal Trespass/Burglary                                           2453.770481\n",
       "Criminal Trespass or Burglary                                        1936.245863\n",
       "House Trespass & House Breaking                                       620.604597\n",
       "Theft                                                               10756.754780\n",
       "Auto Theft                                                           4134.436271\n",
       "Other Thefts                                                         7513.338991\n",
       "                                                                        ...     \n",
       "Dowry Deaths                                                          431.844823\n",
       "Assault on Women with intent to outrage her Modesty                  1503.624565\n",
       "Sexual Harassment                                                     702.801003\n",
       "Assault or use of criminal force to women with intent to Disrobe      259.023104\n",
       "Voyeurism                                                             119.134287\n",
       "Stalking                                                              218.019506\n",
       "Other Assault on Women                                                918.699380\n",
       "Insult to the Modesty of Women                                        456.535798\n",
       "At Office premises                                                    106.243194\n",
       "Other places related to work                                          125.648571\n",
       "In Public Transport system                                            113.296049\n",
       "Places other than 231, 232 & 233                                      436.164863\n",
       "Cruelty by Husband or his Relatives                                  3279.697341\n",
       "Importation of Girls from Foreign Country                             105.421744\n",
       "Causing Death by Negligence                                          2174.691028\n",
       "Deaths due to negligent driving/act                                  2151.435015\n",
       "Deaths due to Other Causes                                            301.714428\n",
       "Offences against State                                                112.161819\n",
       "Sedition                                                              107.162280\n",
       "Other offences against State                                          111.981616\n",
       "Offences promoting enmity between different groups                    113.472802\n",
       "Promoting enmity between different groups                             112.700195\n",
       "Imputation, assertions prejudicial to national integration            105.542328\n",
       "Extortion                                                             272.151348\n",
       "Disclosure of Identity of Victims                                     121.964802\n",
       "Incidence of Rash Driving                                           14568.962508\n",
       "HumanTrafficking                                                      124.871272\n",
       "Unnatural Offence                                                     131.177072\n",
       "Other IPC crimes                                                    17774.325924\n",
       "Total Cognizable IPC crimes                                         39058.672437\n",
       "Length: 89, dtype: float64"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "crime.describe().mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       221.363636\n",
       "1       142.204545\n",
       "2       150.806818\n",
       "3       205.818182\n",
       "4        16.022727\n",
       "5       182.943182\n",
       "6       157.522727\n",
       "7       184.704545\n",
       "8       216.147727\n",
       "9       217.625000\n",
       "10      166.045455\n",
       "11       66.431818\n",
       "12      120.806818\n",
       "13      103.306818\n",
       "14      217.534091\n",
       "15       41.215909\n",
       "16       79.284091\n",
       "17      206.909091\n",
       "18      131.738636\n",
       "19      230.102273\n",
       "20     3058.534091\n",
       "21        0.829545\n",
       "22        5.352273\n",
       "23        0.090909\n",
       "24        0.113636\n",
       "25        4.056818\n",
       "26        3.909091\n",
       "27        1.454545\n",
       "28        8.193182\n",
       "29        2.636364\n",
       "          ...     \n",
       "808       8.181818\n",
       "809       8.181818\n",
       "810       5.568182\n",
       "811       0.920455\n",
       "812       6.488636\n",
       "813     266.352273\n",
       "814       1.318182\n",
       "815     563.784091\n",
       "816       1.954545\n",
       "817      12.397727\n",
       "818      78.022727\n",
       "819      73.806818\n",
       "820     251.897727\n",
       "821     515.250000\n",
       "822     415.113636\n",
       "823     627.920455\n",
       "824      58.625000\n",
       "825     538.897727\n",
       "826     461.477273\n",
       "827     343.545455\n",
       "828       0.454545\n",
       "829       3.659091\n",
       "830       0.000000\n",
       "831     563.420455\n",
       "832    4777.897727\n",
       "833       2.295455\n",
       "834       2.295455\n",
       "835      16.738636\n",
       "836      75.170455\n",
       "837      91.909091\n",
       "Length: 838, dtype: float64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "crime[crime.columns[3:]].mean(axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7241.534090909091"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "crime[crime.columns[3:]].mean(axis=1).max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.0"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "crime[crime.columns[3:]].mean(axis=1).min()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "crime['mean_crime']=crime[crime.columns[3:]].mean(axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0       221.363636\n",
       "1       142.204545\n",
       "2       150.806818\n",
       "3       205.818182\n",
       "4        16.022727\n",
       "5       182.943182\n",
       "6       157.522727\n",
       "7       184.704545\n",
       "8       216.147727\n",
       "9       217.625000\n",
       "10      166.045455\n",
       "11       66.431818\n",
       "12      120.806818\n",
       "13      103.306818\n",
       "14      217.534091\n",
       "15       41.215909\n",
       "16       79.284091\n",
       "17      206.909091\n",
       "18      131.738636\n",
       "19      230.102273\n",
       "20     3058.534091\n",
       "21        0.829545\n",
       "22        5.352273\n",
       "23        0.090909\n",
       "24        0.113636\n",
       "25        4.056818\n",
       "26        3.909091\n",
       "27        1.454545\n",
       "28        8.193182\n",
       "29        2.636364\n",
       "          ...     \n",
       "808       8.181818\n",
       "809       8.181818\n",
       "810       5.568182\n",
       "811       0.920455\n",
       "812       6.488636\n",
       "813     266.352273\n",
       "814       1.318182\n",
       "815     563.784091\n",
       "816       1.954545\n",
       "817      12.397727\n",
       "818      78.022727\n",
       "819      73.806818\n",
       "820     251.897727\n",
       "821     515.250000\n",
       "822     415.113636\n",
       "823     627.920455\n",
       "824      58.625000\n",
       "825     538.897727\n",
       "826     461.477273\n",
       "827     343.545455\n",
       "828       0.454545\n",
       "829       3.659091\n",
       "830       0.000000\n",
       "831     563.420455\n",
       "832    4777.897727\n",
       "833       2.295455\n",
       "834       2.295455\n",
       "835      16.738636\n",
       "836      75.170455\n",
       "837      91.909091\n",
       "Name: mean_crime, Length: 838, dtype: float64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "crime.mean_crime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "#     if x[(x['mean_crime']>=0)&(x['mean_crime']<2431)]:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "def zone(x):\n",
    "    if (x[\"mean_crime\"] >= 0) & (x[\"mean_crime\"]<100):\n",
    "        return 0\n",
    "    elif (x[\"mean_crime\"] >= 100) & (x[\"mean_crime\"]<200):\n",
    "        return 1\n",
    "    else:\n",
    "        return 2\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "crime = crime.assign(alert_zone=crime.apply(zone, axis=1))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 838 entries, 0 to 837\n",
      "Data columns (total 93 columns):\n",
      "States/UTs                                                          838 non-null object\n",
      "District                                                            838 non-null object\n",
      "Year                                                                838 non-null int64\n",
      "Murder                                                              838 non-null int64\n",
      "Attempt to commit Murder                                            838 non-null int64\n",
      "Culpable Homicide not amounting to Murder                           838 non-null int64\n",
      "Attempt to commit Culpable Homicide                                 838 non-null int64\n",
      "Rape                                                                838 non-null int64\n",
      "Custodial Rape                                                      838 non-null int64\n",
      "Custodial_Gang Rape                                                 838 non-null int64\n",
      "Custodial_Other Rape                                                838 non-null int64\n",
      "Rape other than Custodial                                           838 non-null int64\n",
      "Rape_Gang Rape                                                      838 non-null int64\n",
      "Rape_Others                                                         838 non-null int64\n",
      "Attempt to commit Rape                                              838 non-null int64\n",
      "Kidnapping & Abduction_Total                                        838 non-null int64\n",
      "Kidnapping & Abduction                                              838 non-null int64\n",
      "Kidnapping & Abduction in order to Murder                           838 non-null int64\n",
      "Kidnapping for Ransom                                               838 non-null int64\n",
      "Kidnapping & Abduction of Women to compel her for marriage          838 non-null int64\n",
      "Other Kidnapping                                                    838 non-null int64\n",
      "Dacoity                                                             838 non-null int64\n",
      "Dacoity with Murder                                                 838 non-null int64\n",
      "Other Dacoity                                                       838 non-null int64\n",
      "Making Preparation and Assembly for committing Dacoity              838 non-null int64\n",
      "Robbery                                                             838 non-null int64\n",
      "Criminal Trespass/Burglary                                          838 non-null int64\n",
      "Criminal Trespass or Burglary                                       838 non-null int64\n",
      "House Trespass & House Breaking                                     838 non-null int64\n",
      "Theft                                                               838 non-null int64\n",
      "Auto Theft                                                          838 non-null int64\n",
      "Other Thefts                                                        838 non-null int64\n",
      "Unlawful Assembly                                                   838 non-null int64\n",
      "Riots                                                               838 non-null int64\n",
      "Riots_Communal                                                      838 non-null int64\n",
      "Riots_Industrial                                                    838 non-null int64\n",
      "Riots_Political                                                     838 non-null int64\n",
      "Riots_Caste Conflict                                                838 non-null int64\n",
      "Riots_SC/STs Vs Non-SCs/STs                                         838 non-null int64\n",
      "Riots_Other Caste Conflict                                          838 non-null int64\n",
      "Riots_Agrarian                                                      838 non-null int64\n",
      "Riots_Students                                                      838 non-null int64\n",
      "Riots_Sectarian                                                     838 non-null int64\n",
      "Riots_Others                                                        838 non-null int64\n",
      "Criminal Breach of Trust                                            838 non-null int64\n",
      "Cheating                                                            838 non-null int64\n",
      "Forgery                                                             838 non-null int64\n",
      "Counterfeiting                                                      838 non-null int64\n",
      "Counterfeit Offences related to Counterfeit Coin                    838 non-null int64\n",
      "Counterfeiting Government Stamp                                     838 non-null int64\n",
      "Counterfeit currency & Bank notes                                   838 non-null int64\n",
      "Counterfeiting currency notes/Bank notes                            838 non-null int64\n",
      "Using forged or counterfeiting currency/Bank notes                  838 non-null int64\n",
      "Possession of forged or counterfeiting currency/Bank notes          838 non-null int64\n",
      "Making or Possessing materials for forged currency/Bank notes       838 non-null int64\n",
      "Making or Using documents resembling currency                       838 non-null int64\n",
      "Arson                                                               838 non-null int64\n",
      "Grievous Hurt                                                       838 non-null int64\n",
      "Hurt                                                                838 non-null int64\n",
      "Acid attack                                                         838 non-null int64\n",
      "Attempt to Acid Attack                                              838 non-null int64\n",
      "Dowry Deaths                                                        838 non-null int64\n",
      "Assault on Women with intent to outrage her Modesty                 838 non-null int64\n",
      "Sexual Harassment                                                   838 non-null int64\n",
      "Assault or use of criminal force to women with intent to Disrobe    838 non-null int64\n",
      "Voyeurism                                                           838 non-null int64\n",
      "Stalking                                                            838 non-null int64\n",
      "Other Assault on Women                                              838 non-null int64\n",
      "Insult to the Modesty of Women                                      838 non-null int64\n",
      "At Office premises                                                  838 non-null int64\n",
      "Other places related to work                                        838 non-null int64\n",
      "In Public Transport system                                          838 non-null int64\n",
      "Places other than 231, 232 & 233                                    838 non-null int64\n",
      "Cruelty by Husband or his Relatives                                 838 non-null int64\n",
      "Importation of Girls from Foreign Country                           838 non-null int64\n",
      "Causing Death by Negligence                                         838 non-null int64\n",
      "Deaths due to negligent driving/act                                 838 non-null int64\n",
      "Deaths due to Other Causes                                          838 non-null int64\n",
      "Offences against State                                              838 non-null int64\n",
      "Sedition                                                            838 non-null int64\n",
      "Other offences against State                                        838 non-null int64\n",
      "Offences promoting enmity between different groups                  838 non-null int64\n",
      "Promoting enmity between different groups                           838 non-null int64\n",
      "Imputation, assertions prejudicial to national integration          838 non-null int64\n",
      "Extortion                                                           838 non-null int64\n",
      "Disclosure of Identity of Victims                                   838 non-null int64\n",
      "Incidence of Rash Driving                                           838 non-null int64\n",
      "HumanTrafficking                                                    838 non-null int64\n",
      "Unnatural Offence                                                   838 non-null int64\n",
      "Other IPC crimes                                                    838 non-null int64\n",
      "Total Cognizable IPC crimes                                         838 non-null int64\n",
      "mean_crime                                                          838 non-null float64\n",
      "alert_zone                                                          838 non-null int64\n",
      "dtypes: float64(1), int64(90), object(2)\n",
      "memory usage: 608.9+ KB\n"
     ]
    }
   ],
   "source": [
    "crime.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "model = LogisticRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "X = crime[crime.columns[3:90]]\n",
    "Y = crime[crime.columns[92]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/vivek-singh/anaconda3/lib/python3.7/site-packages/sklearn/linear_model/logistic.py:433: FutureWarning: Default solver will be changed to 'lbfgs' in 0.22. Specify a solver to silence this warning.\n",
      "  FutureWarning)\n",
      "/home/vivek-singh/anaconda3/lib/python3.7/site-packages/sklearn/linear_model/logistic.py:460: FutureWarning: Default multi_class will be changed to 'auto' in 0.22. Specify the multi_class option to silence this warning.\n",
      "  \"this warning.\", FutureWarning)\n",
      "/home/vivek-singh/anaconda3/lib/python3.7/site-packages/sklearn/svm/base.py:922: ConvergenceWarning: Liblinear failed to converge, increase the number of iterations.\n",
      "  \"the number of iterations.\", ConvergenceWarning)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,\n",
       "          intercept_scaling=1, max_iter=100, multi_class='warn',\n",
       "          n_jobs=None, penalty='l2', random_state=None, solver='warn',\n",
       "          tol=0.0001, verbose=0, warm_start=False)"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.fit(X,Y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      ">Gwalior\n",
      ">Agra\n",
      ">exit\n"
     ]
    }
   ],
   "source": [
    "s = []\n",
    "while True:\n",
    "    inp = input(\">\")\n",
    "    if inp == 'exit':\n",
    "        break\n",
    "    s.append(crime.loc[crime['District'] == inp]['alert_zone'].values)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[array([2]), array([2])]\n"
     ]
    }
   ],
   "source": [
    "print(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [],
   "source": [
    "k= pd.DataFrame(s)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    2.0\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "z=np.floor(k.sum(0)/len(k))\n",
    "print(z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([1])"
      ]
     },
     "execution_count": 72,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "crime.loc[crime['District'] == \"Chittoor\"]['alert_zone'].values"
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
