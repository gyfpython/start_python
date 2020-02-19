import binascii

print(binascii.crc32('ldap@CN=jira-users,OU=Groups,OU=ArrayComm,DC=ygomi,DC=net'.encode()))

