import argparse
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import signal
import sys
import time
from threading import Thread
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


web_scan = None

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    global EXIT
    EXIT=True
    web_scan.stop()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


def main():
    parser = argparse.ArgumentParser(description="Tiny web fuzzer")
    parser.add_argument("--url", "-u", type=str, default=None, help="Target URL")
    parser.add_argument("--wordlist", "-w", type=str, default=None, help="Specify a wordlist file")
    parser.add_argument("--ic",type=str, default=None, help="Include response code ex: 200,301,500")
    parser.add_argument("--timeout","-t",type=int, default=5, help="Request timeout")

    args = parser.parse_args()
    
        
    if args.wordlist:
        include_code_list = []
        if args.ic:
            for code in args.ic.split(","):
                include_code_list.append(int(code.strip()))
        if args.url:
            file = open(args.wordlist, "r", encoding="utf-8")
            while True:
                word=file.readline()
                if not word:
                    break
                attack_url = args.url.replace("FUZZ", word.strip())
                try:
                    response = requests.get(attack_url, timeout=args.timeout)
                    if len(include_code_list)==0 or (len(include_code_list)>0 and response.status_code in include_code_list):
                            print(f"{attack_url}\t[Code: {response.status_code}]\t[Size: {len(response.text)}]")
                except Exception as ex:
                    print(f"Error: {attack_url}\t{str(ex)}")
            file.close()
    else:
        print("Error: you need to specify a wordlist file")
        
        
        
if __name__ == '__main__':
    main()
    