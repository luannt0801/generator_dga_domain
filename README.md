<!-- ```
git remote add origin https://github.com/luannt0801/generator_dga_domain.git
git branch -M main
git push -u origin main
``` -->

### To generator domain dga:
1. number_of_file
2. number_of_sample: sample in each file

#### --type | normal | dirichlet | non_iid
#### --n | number of sample
#### --num_file | quantity of file
#### --num_client | quantity of client
#### --data_dirichlet | total sample dga in each client
#### --name_client | jetson | machine

### Running
```python
python Script.py --n 100000 --num_file 1 --name_client dai --num_client 1
```