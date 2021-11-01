# Z-score

# EM-multiple

# Pandas how to

## Making Reuters datasets more sensible

By default, Reuters gives, for example, balance sheet figures in a format like this:

```
     ticker financialReport  year                                    metric          value
0    AMZN.O   balance_sheet  2020                        Cash & Equivalents   42122.000000
1    AMZN.O   balance_sheet  2019                        Cash & Equivalents   36092.000000
2    AMZN.O   balance_sheet  2018                        Cash & Equivalents   31750.000000
3    AMZN.O   balance_sheet  2017                        Cash & Equivalents   20522.000000
4    AMZN.O   balance_sheet  2016                        Cash & Equivalents   19334.000000
5    AMZN.O   balance_sheet  2015                        Cash & Equivalents   15890.000000
6    AMZN.O   balance_sheet  2020                    Short Term Investments   42274.000000
7    AMZN.O   balance_sheet  2019                    Short Term Investments   18929.000000
8    AMZN.O   balance_sheet  2018                    Short Term Investments    9500.000000
9    AMZN.O   balance_sheet  2017                    Short Term Investments   10464.000000
10   AMZN.O   balance_sheet  2016                    Short Term Investments    6647.000000
```

Not very nice.

### Years into columns

* [Stackoverflow solution](https://stackoverflow.com/a/48958287)

Example dataset

```
Business    Date    Value
a         1/1/2017   127
a         2/1/2017   89
b         2/1/2017   122
a         1/1/2018   555
a         2/1/2018   455
```

Desired format:

```
Business    1/1/2017  2/1/2017 1/1/2018  2/1/2018
 a           127         89     555        455
 b           N/A        122      N/A       N/A
```

Solution

```python
pivoted = df.pivot(index='Business', columns='Date', values='Value')\
            .reset_index()
pivoted.columns.name=None
print(pivoted)
#  Business  1/1/2017  1/1/2018  2/1/201  2/1/2017
#0        a     127.0     555.0    455.0      99.0
#1        b       NaN       NaN      NaN     122.0
```

Results

| Company         | Z-score            | EM-multiple | Symbol   |
|-----------------|--------------------|-------------|----------|
| Apple           | 7.231694203651083  |             | AAPL.O   |
| ABB Ltd         | 3.3000370958045706 |             | ABBN.S   |
| Amazon          | 6.150276669527528  |             | AMZN.O   |
| Caterpillar     | 2.5539932349424705 |             | CAT.N    |
| Facebook        | 18.83279960308495  |             | FB.O     |
| Tesla           | 15.724801553412236 |             | TSLA.O   |
| Google/Alphabet | 7.32827376015526   |             | GOOGL.OQ |
| Nokia           | ----               |             | ---      |

* Apple - no unfunded/underfunded pension(?)
Z-score example
