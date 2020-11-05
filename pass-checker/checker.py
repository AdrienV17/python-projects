# Libraries
import requests
import hashlib
import sys

# API function
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again')

    return res

# Function that gets different hashes related to password entered...
def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

# Function that converts password submitted in sha1 algorithm
def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    resp = request_api_data(first5_char)

    return get_password_leaks_count(resp, tail)

# Main function
def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password.capitalize()} was hacked {count} times... you should probably change it!')
        else:
            print(f'{password.capitalize()} was NOT found. Carry on!!')
    return 'Done! have a great day...'

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
