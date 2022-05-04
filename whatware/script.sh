#!/bin/sh

socat tcp-listen:8005,fork exec:"/rop1"
