```
git remote add origin https://github.com/luannt0801/generator_dga_domain.git
git branch -M main
git push -u origin main
```

### To generator domain dga:
1. number_of_file
2. number_of_sample: sample in each file

```
python .\Script.py --type normal --n 100 --num_file 1 --name_client jetson --num_client 1
python .\Script.py --type dirichlet --num_file 1 --data_dirichlet 1000 --num_client 1 --name_client luan
```