#!/usr/bin/python3

# IP Notifyer
# Copyright (C) 2020 aramcap (https://github.com/aramcap/ipnotifyer)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import smtplib
import requests
import os
from email.message import EmailMessage

from datetime import datetime

ADDRESS_FILE = '/tmp/old_ip_address.txt'

def notify_ip_change(newIp):
    sender = 'sen@server.com'
    sender_pass = 'pass'
    recipient = 'rec@server.com'
    msg = EmailMessage()
    msg['Subject'] = 'La IP ha cambiado'
    msg['From'] = sender
    msg['To'] = recipient
    msg.set_content("""\
La nueva IP es {}
""".format(newIp))
    session = smtplib.SMTP('server.com', 587)
    session.starttls()
    session.login(sender, sender_pass)
    session.sendmail(sender, [recipient], msg.as_string())
    session.quit()

def detect_ip_change():
    blnDelta = False
    req = requests.get('https://api.ipify.org')
    currIp = req.text
    if not os.path.isfile(ADDRESS_FILE):
        persist_ip('127.0.0.1')
    oldIp = read_old_ip()
    if currIp != oldIp:
        blnDelta = True
    persist_ip(currIp)
    # check status code test
    if req.status_code != 200:
        now = datetime.now()
        f = open('/tmp/status_code_check', 'a')
        f.write("{} -> {}".format(now.strftime("%Y/%m/%d, %H:%M:%S"), req.status_code))
        f.close()
    return (blnDelta, currIp)

def persist_ip(ip):
    f = open(ADDRESS_FILE, 'w')
    f.write(ip)
    f.close()

def read_old_ip():
    f = open(ADDRESS_FILE, 'r')
    oldIp = f.read()
    f.close()
    return oldIp

def main():
    deltaTuple = detect_ip_change()
    if deltaTuple[0] is True:
        notify_ip_change(deltaTuple[1])
        #print("La IP ha cambiado. Email enviado!")

if __name__ == '__main__':
    main()
