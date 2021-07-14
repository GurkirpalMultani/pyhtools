#!usr/bin/env python3
from UI.colors import *
import json
import attackers.Network.arpspoofer as arp
import attackers.Network.nwscan as nwscan
import attackers.Network.machngr as machngr
import attackers.Websites.login_guesser.login as web_login
from attackers.Websites.vuln_scanner.scanner import Scanner

# NETWORK ATTACKS
# TODO: Create functions for Network Attackers : codeinjector, dnsspoofer, download replacer, packet_sniffer.
def arpspoofer():
    '''
    perform arp poisoning attack.
    '''
    target_ip = input('[+] TARGET IP : ')
    spoof_ip = input('[+] SPOOF IP : ')
    perform_mitm = input('[+] Perform MITM attack (y/n)(default=y): ').lower()
    if perform_mitm == 'n':
        perform_mitm = False
    else:
        perform_mitm = True
    arp.run_spoofer(target_ip, spoof_ip, perform_mitm)


def nw_scan():
    '''
    perform network scan.
    '''
    ip_range = input('[+] IP RANGE : ')
    nwscan.run_nwscan(ip_range)


def mac_changer():
    '''
    changes mac of network interface.
    '''
    interface = input('[+] Interface : ')
    print(BRIGHT_YELLOW + '[!] To generate random mac enter "random" (without quotes)')
    new_mac = input('[+] New Mac : ')
    if new_mac == 'random':
        print(BRIGHT_WHITE + '[*] Generating Random Mac')
        new_mac = machngr.generate_random_mac()
    
    machngr.run_macchanger(interface, new_mac)


# WEBSITE ATTACKS
# TODO: Create functions for Website Attackers : 
def brute_login():
    '''
    description: bruteforce website login page.
    params: None
    returns: None
    '''
    target_url = input('[+] TARGET URL : ')
    wordlist_file = input('[+] WORDLIST PATH : ')
    print(BRIGHT_YELLOW + '[!] Enter string in post values, eg. {"username":"admin", "password":"", "Login":"submit"} (inspect element in your webbrowser)')
    post_data = input('[+] POST VALUES : ') .strip()
    post_values = json.loads(post_data)

    web_login.bruteforce_login(target_url, wordlist_file, post_values)


def webvulnscan():
    '''
    description: scans for vulnerabilities in the website
    params: None
    returns: None
    '''
    target_url = input('[+] TARGET URL : ')

    
    print(BRIGHT_YELLOW + '[!] Enter links to be ignored separated by commas(,)')
    ignore_links = input('[+] IGNORE LINKS : ')

    ignore_links = [link.strip() for link in ignore_links.split(',')]

    vuln_scanner = Scanner(target_url, ignore_links)

    auth_required = input('[+] AUTH REQUIRED? (y/n) (default=n): ').lower().strip()
    login_link = ''
    login_post_values =''
    if auth_required == 'y':
        login_link  = input('[+] LOGIN LINK : ')
        print(BRIGHT_YELLOW + "[!] Enter login post values, eg: {'username':'yourusername', 'password':'yourpassword', 'login':'submit'}")
        print(BRIGHT_WHITE + '[!] Inspect element in webbrowser to extract values, they might vary for every website.')
        login_post_values = input('[+] LOGIN POST VALUES : ')
        login_post_values = json.loads(login_post_values)
        
        vuln_scanner.session.post(login_link, data=login_post_values)

    vuln_scanner.run()

   
if __name__ == "__main__":
    print('[*] Attackers module!. Exiting...')