#!/bin/sh

socat tcp-listen:8002,fork exec:"/executive"
