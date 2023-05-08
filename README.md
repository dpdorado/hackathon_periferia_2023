# hackathon_periferia_2023

# Install proyect - python 3.10.6

1. Clone repository

```bash
git clone https://github.com/dpdorado/hackathon_periferia_2023.git
``` 

2. Enter directory

```bash
cd hackathon_periferia_2023
``` 

3. Install virtual environment

```bash
virtualenv env 
``` 

4. Active virtual environment

```bash
source env/bin/activate
``` 

5. Install requeriments

```bash
 pip install -r requirements.txt
```

6. Run migrations 

```bash
python manager.py makemigrations
```

7. Run migartions 

```bash
python manager.py migrate
```

# Run test

1. Generate data test

```bash
python ./mutations/test/generate.py
```

2. Run test

```bash
python manage.py test
```