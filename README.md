# Radagast

## Introduction
radagast is an open source penetration testing tool, able to perform a web fuzzer attack against http services. 

## Installation


### local install
```bash
pip install .
 ```

## Usage
```bash


usage: radagast.py [-h] [--url URL] [--wordlist WORDLIST] [--ic IC] [--timeout TIMEOUT]

Tiny web fuzzer

options:
  -h, --help            show this help message and exit
  --url URL, -u URL     Target URL
  --wordlist WORDLIST, -w WORDLIST
                        Specify a wordlist file
  --ic IC               Include response code ex: 200,301,500
  --timeout TIMEOUT, -t TIMEOUT
                        Request timeout


```
### Default wordlist fuzzing
```bash
python radagast.py --url http://localhost:8000/vulnerabilities/FUZZ --wordlist wordlist.txt


```

### Wordlist fuzzing filter by response code
```bash
python radagast.py --url http://localhost:8000/vulnerabilities/FUZZ --wordlist wordlist.txt --ic 200 --timeout 1


```



### Wordlist fuzzing specify timeout
```bash
python radagast.py --url http://localhost:8000/vulnerabilities/FUZZ --timeout 1


```