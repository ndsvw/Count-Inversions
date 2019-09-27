# Count-Inversions

The code was executed on a MacBook Pro (Early 2015) - 2,7 GHz Intel Core i5 processor.

```python
time python3 exhaustive.py 100
time python3 divide_and_conquer.py 100
```

| # random array entries       | exhaustive           | divide and conquer           |
| ------------- |:-------------:|:-------------:|
| 100 | 0m 0.040s | 0m 0.043s
| 1,000 | 0m 0.105s | 0m 0.046s
| 10,000 | 0m 5.924s | 0m 0.126s
| 100,000 | 10m 3.636s | 0m 0.917s
| 1,000,000 | > 1h | 0m 10.375s
| 10,000,000 | - | 2m 2.791s
| 100,000,000 | - | 25m 11.034s
| 1,000,000,000 | - | > 1h