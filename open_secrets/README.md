file system extraction challenge.

The file system has two hardcoded secrets.
1. The hash of the root password found in /etc/shadow
2. A web app password in a lua file

The first secret is pretty straightforward: just find the
hash and crack it (it is administrator)

The challenge is more focused around the second one. These are not
regular lua files. They are files compiled for a very specific 
type of lua (miwifi). Ther eis a miwifi specific decompiler out there
called LuaDec_miwifi. With that, you can decompile the files in the
api directory (pointed to by RE-ing the web app) and see there is a 
hardcoded check for the password "admin"

To submit the challenge, send the passwords to the hosted remote program:
echo "admin" "administrator" | nc 45.32.102.46  8003
