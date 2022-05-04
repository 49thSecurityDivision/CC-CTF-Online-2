#!/bin/sh

#socat -u tcp-l:8001,fork exec:"/rop1",pty,ctty,setsid
socat tcp-listen:8001,fork exec:"/we_got_the_func"
