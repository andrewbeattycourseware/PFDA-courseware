# basic descriptive statistics in pandas
# Author: Andrew Beatty

import pandas as pd

# a series with an even number of values
even_example_values = pd.Series([1, 2, 2, 3, 4, 5, 6, 10000])

print(f'Series Values: {even_example_values.to_list()}')
print(f'Series Mean:   {even_example_values.mean()}')
print(f'Series Median: {even_example_values.median()}')
print(f'series Mode: {even_example_values.mode()}')

# more basic
print(f'Series Values: {even_example_values.to_list()}')
print(f'Series Mean:   {even_example_values.mean()}')
print(f'Series Median: {even_example_values.median()}')
print(f'Series Mode:   {even_example_values.mode().to_list()}')
print(f'Series Min:    {even_example_values.min()}')
print(f'Series Max:    {even_example_values.max()}')
print(f'Series Count:  {even_example_values.count()}')
print(f'Series Length  {len(even_example_values)}')
print(even_example_values.describe())
