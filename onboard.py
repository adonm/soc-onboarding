#!/usr/bin/env python3
from subprocess import run, check_output
import json
accounts = json.loads(check_output("az account list", shell=True))
for account in account:
    print(f"Name: {account["name"]}, TenantID: {account["tenantId"]}")