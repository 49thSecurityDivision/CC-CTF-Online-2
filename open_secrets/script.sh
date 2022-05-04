#!/bin/sh

socat tcp-listen:8003,fork exec:"/open_secrets"
