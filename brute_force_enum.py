import threading
import itertools
import string

def brute_force_password(candidate_password):
    # Add your brute-force logic here
    print(f"Trying password: {candidate_password}")

def threaded_brute_force_passwords():
    threads = []
    password_length = 4  # Set the desired password length
    charset = string.ascii_lowercase + string.digits  # Use the desired character set

    passwords_to_try = itertools.product(charset, repeat=password_length)

    for candidate_password in passwords_to_try:
        candidate_password = ''.join(candidate_password)
        thread = threading.Thread(target=brute_force_password, args=(candidate_password,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    threaded_brute_force_passwords()

