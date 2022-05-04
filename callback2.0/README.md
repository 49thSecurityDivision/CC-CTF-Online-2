# Why?
Nifty twist on RE challenges that we did last year.

# What?
This binary parses user input and turns that input into an HTTP
request to a certain server. If the user (outside of the binary)
makes a GET request to that server, they will see the output of
the script parsing their requests. If they make a POST request 
with the required Header, the flag will be printed.

Also, the server.py file is being run at the remote server.

# How solve?
./main POST https://russian-bot.net:8000/the_oogey_boogey_man Jennys_Number 8675309

# Flag
flag{kf1YOxYxXQOwEvO8z3OYvHNy8I8BPnCx}
